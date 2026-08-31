from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


def load_module():
    spec = importlib.util.spec_from_file_location("curate_sources", ROOT / "scripts" / "curate_sources.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class CurateSourcesTests(unittest.TestCase):
    def test_capability_covers_supporting_files_and_grouped_upstreams(self) -> None:
        curate_sources = load_module()
        self.assertEqual("grill", curate_sources.capability("skills/grill/GAP-REVIEW.md"))
        self.assertEqual(
            "domain-modeling",
            curate_sources.capability("skills/engineering/domain-modeling/SKILL.md"),
        )
        self.assertEqual("loop-me", curate_sources.capability("skills/in-progress/loop-me/SKILL.md"))
        self.assertEqual("migrate-to-shoehorn", curate_sources.capability("skills/misc/migrate-to-shoehorn/SKILL.md"))

    def test_provenance_requires_locked_revision_for_every_source_row(self) -> None:
        curate_sources = load_module()
        with tempfile.TemporaryDirectory() as directory:
            provenance = Path(directory) / "PROVENANCE.md"
            provenance.write_text(
                "| obra/superpowers: diagnose | deadbeef | adopt | diagnose | note |\n",
                encoding="utf-8",
            )
            self.assertTrue(curate_sources.provenance_has_revision(provenance, "obra-superpowers", "deadbeef00"))
            self.assertFalse(curate_sources.provenance_has_revision(provenance, "obra-superpowers", "feedface00"))

    def test_inventory_changes_reports_added_changed_and_removed_skills(self) -> None:
        curate_sources = load_module()
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.email", "test@example.com"], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"], check=True)
            for name, text in {"alpha": "old", "beta": "gone"}.items():
                target = repo / "skills" / name / "SKILL.md"
                target.parent.mkdir(parents=True)
                target.write_text(text, encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "-qm", "pin"], check=True)
            pinned = curate_sources.git(repo, "rev-parse", "HEAD")
            (repo / "skills" / "alpha" / "SKILL.md").write_text("new", encoding="utf-8")
            (repo / "skills" / "beta" / "SKILL.md").unlink()
            added = repo / "skills" / "gamma" / "SKILL.md"
            added.parent.mkdir()
            added.write_text("new", encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "-qm", "next"], check=True)
            self.assertEqual(
                [("added", "gamma"), ("changed", "alpha"), ("removed", "beta")],
                curate_sources.inventory_changes(repo, pinned, "HEAD"),
            )


if __name__ == "__main__":
    unittest.main()
