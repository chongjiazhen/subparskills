from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).parents[1]
HARNESSES = {"claude-code", "codex", "pi", "opencode", "qwen"}
PACKS = {"core", "delivery", "architecture", "tracker"}
COMMAND_PACKS = {
    "delivery": {"finish", "grill", "handoff", "implement", "plan"},
    "tracker": {"claim-ticket", "to-tickets", "triage", "work-frontier"},
}


def read_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}: (.+)$", text, re.M)
    if match is None:
        raise ValueError(f"catalog missing {key}")
    return match.group(1)


def entries(catalog: Path) -> list[tuple[str, Path]]:
    active_id: str | None = None
    found: list[tuple[str, Path]] = []
    for line in catalog.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*- id: (.+)", line)
        if match:
            active_id = match.group(1)
            continue
        match = re.match(r"\s*source: (.+)", line)
        if match and active_id:
            found.append((active_id, (catalog.parent / match.group(1)).resolve()))
            active_id = None
    return found


def pack_members(name: str) -> set[str]:
    path = ROOT / "packs" / f"{name}.yml"
    return {
        line.removeprefix("  - ")
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("  - ")
    }


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def copy_tracker_resources(target: Path) -> None:
    source_root = ROOT / "skills" / "tracker"
    for source in source_root.rglob("*.md"):
        copy_file(source, target / source.relative_to(source_root))


def command_members(pack: str | None) -> set[str]:
    if pack is None:
        return {path.stem for path in (ROOT / "commands").glob("*.md")}
    return COMMAND_PACKS.get(pack, set())


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Subparskills into native harness path")
    parser.add_argument("--harness", choices=sorted(HARNESSES), required=True)
    parser.add_argument("--pack", choices=sorted(PACKS))
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()

    catalog = ROOT / "adapters" / args.harness / "catalog.yml"
    native_path = read_value(catalog.read_text(encoding="utf-8"), "native_path")
    selected = pack_members(args.pack) if args.pack else None
    installed = [(skill_id, source) for skill_id, source in entries(catalog) if selected is None or skill_id in selected]
    for skill_id, source in installed:
        copy_file(source, args.destination / native_path / skill_id / "SKILL.md")
    if args.pack is None or args.pack == "tracker":
        copy_tracker_resources(args.destination / native_path / "tracker")
    if args.harness == "opencode":
        for command_name in command_members(args.pack):
            command = ROOT / "commands" / f"{command_name}.md"
            copy_file(command, args.destination / ".opencode/commands" / command.name)
    print(f"installed {len(installed)} skills for {args.harness} at {args.destination / native_path}")


if __name__ == "__main__":
    main()
