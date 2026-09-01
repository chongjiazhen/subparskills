import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).parents[1]


@dataclass(frozen=True)
class Source:
    id: str
    commit: str


def parse_lockfile(path: Path) -> dict[str, Source]:
    found: dict[str, Source] = {}
    source_id: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*- id: (.+)$", line)
        if match:
            source_id = match.group(1)
            continue
        match = re.match(r"\s+commit: (.+)$", line)
        if match and source_id:
            found[source_id] = Source(source_id, match.group(1))
            source_id = None
    return found


def git(path: Path, *args: str) -> str:
    completed = subprocess.run(["git", "-C", str(path), *args], capture_output=True, text=True, check=False)
    if completed.returncode:
        raise ValueError(completed.stderr.strip() or f"git failed: {' '.join(args)}")
    return completed.stdout.strip()


def capability(path: str) -> str | None:
    parts = Path(path.replace("\\", "/")).parts
    if len(parts) < 3 or parts[0] != "skills":
        return None
    if parts[1] in {"engineering", "productivity", "in-progress", "misc"} and len(parts) >= 4:
        return parts[2]
    return parts[1]


def provenance_has_revision(path: Path, source_id: str, revision: str) -> bool:
    source_name = {
        "obra-superpowers": "obra/superpowers",
        "mattpocock-skills": "mattpocock/skills",
    }.get(source_id, source_id)
    revisions = {
        columns[1]
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("| ")
        for columns in [[value.strip() for value in line.strip("|").split("|")]]
        if len(columns) >= 2 and columns[0].startswith(f"{source_name}:")
    }
    return bool(revisions) and revisions == {revision[:8]}


def inventory_changes(path: Path, pinned: str, ref: str) -> list[tuple[str, str]]:
    changes: dict[str, str] = {}
    for line in git(path, "diff", "--name-status", f"{pinned}..{ref}", "--", "skills").splitlines():
        fields = line.split("\t")
        if len(fields) < 2:
            continue
        kind = {"A": "added", "D": "removed"}.get(fields[0][0], "changed")
        for name in {item for item in (capability(value) for value in fields[1:]) if item}:
            previous = changes.get(name)
            changes[name] = "changed" if previous and previous != kind else kind
    return sorted((kind, name) for name, kind in changes.items())


def parse_mapping(value: str) -> tuple[str, Path]:
    source_id, separator, local_path = value.partition("=")
    if not separator or not source_id or not local_path:
        raise argparse.ArgumentTypeError("use SOURCE_ID=LOCAL_CLONE_PATH")
    return source_id, Path(local_path)


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report local upstream skill deltas without writing files")
    parser.add_argument("--upstream", action="append", type=parse_mapping, required=True)
    parser.add_argument("--lockfile", type=Path, default=ROOT / "sources.lock.yml")
    parser.add_argument("--provenance", type=Path, default=ROOT / "PROVENANCE.md")
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--check", action="store_true", help="exit 2 when a curation decision is required")
    args = parser.parse_args(argv)
    sources = parse_lockfile(args.lockfile)
    needs_curation = False
    for source_id, local_path in args.upstream:
        source = sources.get(source_id)
        if source is None:
            raise ValueError(f"{source_id}: missing from {args.lockfile}")
        current = git(local_path, "rev-parse", args.ref)
        changes = inventory_changes(local_path, source.commit, args.ref)
        provenance_ready = provenance_has_revision(args.provenance, source_id, source.commit)
        needs_curation |= bool(changes) or not provenance_ready
        print(f"source: {source_id}\npinned: {source.commit}\ncurrent: {current}")
        print(f"provenance: {'ready' if provenance_ready else 'missing locked revision'}")
        if changes:
            for kind, name in changes:
                print(f"{kind}: {name}")
            print("next: classify every capability in PROVENANCE.md; update lock only after review")
        else:
            print(
                "next: no curation decision required"
                if provenance_ready
                else "next: update PROVENANCE.md before accepting this lock"
            )
    return 2 if args.check and needs_curation else 0


def main() -> int:
    try:
        return run()
    except (OSError, ValueError) as error:
        print(f"error: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
