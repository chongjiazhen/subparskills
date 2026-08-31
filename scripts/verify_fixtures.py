from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).parents[1]


def catalog_sources(path: Path) -> list[tuple[str, Path]]:
    current_id: str | None = None
    found: list[tuple[str, Path]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        id_match = re.match(r"\s*- id: (.+)", line)
        source_match = re.match(r"\s*source: (.+)", line)
        if id_match:
            current_id = id_match.group(1)
        elif source_match and current_id:
            found.append((current_id, (path.parent / source_match.group(1)).resolve()))
            current_id = None
    return found


def main() -> None:
    fixtures = sorted((ROOT / "tests/fixtures").iterdir())
    with tempfile.TemporaryDirectory(prefix="subparskills-fixtures-") as temp:
        install_root = Path(temp)
        for fixture in fixtures:
            destination = install_root / fixture.name
            completed = subprocess.run(
                [
                    sys.executable,
                    "scripts/install_adapter.py",
                    "--harness",
                    fixture.name,
                    "--destination",
                    str(destination),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            if completed.returncode:
                raise RuntimeError(completed.stderr + completed.stdout)
            catalog = ROOT / "adapters" / fixture.name / "catalog.yml"
            native_path = re.search(r"^native_path: (.+)$", catalog.read_text(encoding="utf-8"), re.M)
            if native_path is None:
                raise RuntimeError(f"{fixture.name}: no native path")
            for skill_id, source in catalog_sources(catalog):
                target = destination / native_path.group(1) / skill_id / "SKILL.md"
                if target.read_bytes() != source.read_bytes():
                    raise RuntimeError(f"{fixture.name}: {skill_id} body changed during install")
                if "superpowers" in str(target).lower() or "mattpocock" in str(target).lower():
                    raise RuntimeError(f"{fixture.name}: stock collision")
            resource_root = ROOT / "skills/tracker"
            for source in resource_root.rglob("*.md"):
                relative_path = source.relative_to(resource_root)
                target = destination / native_path.group(1) / "tracker" / relative_path
                if target.read_bytes() != source.read_bytes():
                    raise RuntimeError(
                        f"{fixture.name}: tracker resource changed during install: {relative_path}"
                    )
            if fixture.name == "opencode":
                for command in (ROOT / "commands").glob("*.md"):
                    installed = destination / ".opencode/commands" / command.name
                    if installed.read_bytes() != command.read_bytes():
                        raise RuntimeError(f"opencode: command missing {command.name}")
    print(f"{len(fixtures)} harness fixtures verified")


if __name__ == "__main__":
    main()
