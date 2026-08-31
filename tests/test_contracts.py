from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILLS = ROOT / "skills"
EXPECTED_CORE = {"diagnose", "tdd", "verify", "review"}
EXPECTED_TRACKER = {"to-tickets", "triage", "claim-ticket", "work-frontier"}
TRACKER_RESOURCES = {
    "ticket-schema.md",
    "state-model.md",
    "backends/local.md",
    "backends/github.md",
}
EXPECTED_PACKS = {"core", "delivery", "architecture", "tracker"}
EXPECTED_ADAPTERS = {"claude-code", "codex", "pi", "opencode", "qwen"}
PERSONAL_MARKERS = ("~/", "C:\\Users\\", "C:\\", "/private-repo/", "private-layer", "worker-delegate")
PUBLIC_MARKERS = tuple(marker.lower() for marker in PERSONAL_MARKERS + ("private-repo", "factlog"))


def frontmatter(path: Path) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not match:
        raise AssertionError(f"{path}: missing frontmatter")
    return dict(
        (key.strip(), value.strip())
        for key, value in (
            line.split(":", 1)
            for line in match.group(1).splitlines()
            if ":" in line and not line.startswith((" ", "-"))
        )
    )


class FrameworkContracts(unittest.TestCase):
    def test_skill_frontmatter_is_portable_and_unique(self) -> None:
        seen: set[str] = set()
        for path in SKILLS.glob("*/SKILL.md"):
            data = frontmatter(path)
            self.assertEqual(
                {"name", "description", "license", "compatibility", "metadata"},
                set(data),
                path,
            )
            self.assertNotIn(data["name"], seen, path)
            seen.add(data["name"])
            self.assertEqual(path.parent.name, data["name"], path)
            self.assertEqual("MIT", data["license"], path)
            body = path.read_text(encoding="utf-8").split("---\n", 2)[2]
            self.assertFalse(any(marker.lower() in body.lower() for marker in PERSONAL_MARKERS), path)

    def test_public_skills_have_no_private_markers(self) -> None:
        for path in SKILLS.rglob("*.md"):
            self.assertFalse(
                any(token in path.read_text(encoding="utf-8").lower() for token in PUBLIC_MARKERS),
                path,
            )

    def test_architecture_references_are_relative_and_present(self) -> None:
        body = (SKILLS / "architecture-improvement/SKILL.md").read_text(encoding="utf-8")
        for name in ("LANGUAGE.md", "DEEPENING.md", "INTERFACE-DESIGN.md"):
            self.assertIn(f"[{name}]({name})", body)
            self.assertTrue((SKILLS / "architecture-improvement" / name).is_file())

    def test_readme_documents_private_overlay_boundary(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("`v0.2.0`", readme)
        self.assertIn("private overlay", readme.lower())

        changelog_path = ROOT / "CHANGELOG.md"
        self.assertTrue(changelog_path.is_file())

        changelog = changelog_path.read_text(encoding="utf-8")
        match = re.search(
            r"^## 0\.2\.0 - 2026-08-31\n\n(.+?)(?=\n## |\Z)",
            changelog,
            re.M | re.S,
        )
        self.assertIsNotNone(match)
        self.assertTrue(match.group(1).strip())

    def test_packs_reference_existing_skills(self) -> None:
        found: set[str] = set()
        for path in (ROOT / "packs").glob("*.yml"):
            found.add(path.stem)
            lines = path.read_text(encoding="utf-8").splitlines()
            for line in lines:
                if line.startswith("  - "):
                    self.assertTrue((SKILLS / line[4:] / "SKILL.md").is_file(), path)
        self.assertEqual(EXPECTED_PACKS, found)
        core = (ROOT / "packs/core.yml").read_text(encoding="utf-8")
        self.assertTrue(all(f"  - {name}" in core for name in EXPECTED_CORE))
        tracker = (ROOT / "packs/tracker.yml").read_text(encoding="utf-8")
        self.assertTrue(all(f"  - {name}" in tracker for name in EXPECTED_TRACKER))

    def test_tracker_skills_do_not_contain_github_access_instructions(self) -> None:
        for skill_id in EXPECTED_TRACKER:
            body = (SKILLS / skill_id / "SKILL.md").read_text(encoding="utf-8")
            for prohibited in ("gh ", "api.github.com", "/issues/"):
                self.assertNotIn(prohibited, body, skill_id)

    def test_adapters_are_thin_and_cover_catalog(self) -> None:
        catalog = sorted(path.parent.name for path in SKILLS.glob("*/SKILL.md"))
        found: set[str] = set()
        for adapter in (ROOT / "adapters").iterdir():
            if not adapter.is_dir():
                continue
            found.add(adapter.name)
            manifest = adapter / "catalog.yml"
            self.assertTrue(manifest.is_file(), adapter)
            text = manifest.read_text(encoding="utf-8")
            self.assertIn("../../skills/", text, manifest)
            self.assertIn("native_path:", text, manifest)
            self.assertNotIn("# ", text, manifest)
            for name in catalog:
                self.assertIn(f"id: {name}", text, manifest)
        self.assertEqual(EXPECTED_ADAPTERS, found)

    def test_provenance_inventory_and_licenses_exist(self) -> None:
        provenance = (ROOT / "PROVENANCE.md").read_text(encoding="utf-8")
        for source in ("obra/superpowers", "mattpocock/skills"):
            self.assertIn(source, provenance)
        self.assertIn("b36e0829c6d0140e93cfef2ca599b1b07d4a7797", provenance)
        self.assertIn("6654f6b60cd9d5be8b54c6fafe44346dabeb3b76", provenance)
        self.assertIn("Copyright (c) 2025 Jesse Vincent", (ROOT / "NOTICE").read_text(encoding="utf-8"))
        self.assertIn("Copyright (c) 2026 Matt Pocock", (ROOT / "NOTICE").read_text(encoding="utf-8"))

    def test_clean_install_fixtures_have_no_stock_collision(self) -> None:
        for fixture in (ROOT / "tests/fixtures").iterdir():
            self.assertTrue((fixture / ".gitignore").is_file(), fixture)
            self.assertFalse(any("superpowers" in str(path).lower() or "mattpocock" in str(path).lower() for path in fixture.rglob("*")), fixture)
        self.assertIsNotNone(shutil.which("git"))

    def test_fixture_installer_copies_canonical_bodies(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/verify_fixtures.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr + result.stdout)
        self.assertIn("5 harness fixtures verified", result.stdout)

    def test_claude_plugin_exposes_canonical_skills_and_commands(self) -> None:
        manifest = (ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        self.assertIn('"./skills"', manifest)
        self.assertIn('"./commands"', manifest)

    def test_skills_cli_discovers_root_catalog(self) -> None:
        result = subprocess.run(
            ["npx.cmd", "skills", "add", ".", "--list"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
        self.assertEqual(0, result.returncode, result.stderr + result.stdout)
        self.assertIn("Found 18 skills", result.stdout)

    def test_pack_install_selects_only_requested_skills(self) -> None:
        with tempfile.TemporaryDirectory(prefix="subparskills-pack-") as temp:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/install_adapter.py",
                    "--harness",
                    "codex",
                    "--pack",
                    "core",
                    "--destination",
                    temp,
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr + result.stdout)
            installed = {path.parent.name for path in (Path(temp) / ".agents/skills").glob("*/SKILL.md")}
            self.assertEqual(EXPECTED_CORE, installed)

    def test_tracker_pack_installs_only_tracker_skills_for_codex(self) -> None:
        with tempfile.TemporaryDirectory(prefix="subparskills-tracker-pack-") as temp:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/install_adapter.py",
                    "--harness",
                    "codex",
                    "--pack",
                    "tracker",
                    "--destination",
                    temp,
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr + result.stdout)
            installed = {path.parent.name for path in (Path(temp) / ".agents/skills").glob("*/SKILL.md")}
            self.assertEqual(EXPECTED_TRACKER, installed)

    def test_tracker_pack_installs_canonical_resources_for_codex(self) -> None:
        with tempfile.TemporaryDirectory(prefix="subparskills-tracker-resources-") as temp:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/install_adapter.py",
                    "--harness",
                    "codex",
                    "--pack",
                    "tracker",
                    "--destination",
                    temp,
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr + result.stdout)
            for relative_path in TRACKER_RESOURCES:
                source = SKILLS / "tracker" / relative_path
                installed = Path(temp) / ".agents/skills/tracker" / relative_path
                self.assertEqual(source.read_bytes(), installed.read_bytes(), relative_path)

    def test_tracker_pack_installs_only_tracker_commands_for_opencode(self) -> None:
        with tempfile.TemporaryDirectory(prefix="subparskills-opencode-tracker-") as temp:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/install_adapter.py",
                    "--harness",
                    "opencode",
                    "--pack",
                    "tracker",
                    "--destination",
                    temp,
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr + result.stdout)
            command_dir = Path(temp) / ".opencode/commands"
            installed = {path.stem for path in command_dir.glob("*.md")}
            self.assertEqual(EXPECTED_TRACKER, installed)


if __name__ == "__main__":
    unittest.main()
