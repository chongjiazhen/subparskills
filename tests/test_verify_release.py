from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).parents[1]


def load_module():
    spec = importlib.util.spec_from_file_location(
        "verify_release", ROOT / "scripts" / "verify_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class VerifyReleaseTests(unittest.TestCase):
    def test_default_checks_cover_release_gate(self) -> None:
        module = load_module()
        commands = [check.command for check in module.default_checks(ROOT)]
        self.assertEqual(
            [
                ["git", "diff", "--check"],
                [module.python_command(), "scripts/verify_fixtures.py"],
                ["pytest", "-q"],
                [module.npx_command(), "skills", "add", ".", "--list"],
            ],
            commands,
        )

    def test_write_evidence_records_results(self) -> None:
        module = load_module()
        evidence = Path(tempfile.mkdtemp(prefix="subparskills-evidence-")) / "release.md"
        results = [
            module.CheckResult(
                name="pytest",
                command=["pytest", "-q"],
                returncode=0,
                stdout="16 passed",
                stderr="",
            ),
            module.CheckResult(
                name="npx skills add",
                command=["npx.cmd", "skills", "add", ".", "--list"],
                returncode=0,
                stdout="Found 17 skills",
                stderr="",
            ),
        ]

        module.write_evidence(
            evidence,
            ROOT,
            results,
            generated_at=datetime(2026, 8, 31, 3, 4, 5, tzinfo=timezone.utc),
        )

        text = evidence.read_text(encoding="utf-8")
        self.assertIn("2026-08-31T03:04:05Z", text)
        self.assertIn("`pytest -q`", text)
        self.assertIn("Found 17 skills", text)

    def test_run_returns_failure_when_any_check_fails(self) -> None:
        module = load_module()

        class FakeRunner:
            def __init__(self):
                self.calls = []

            def __call__(self, command, cwd):
                self.calls.append((command, cwd))
                return module.CheckResult(
                    name=" ".join(command[:2]),
                    command=command,
                    returncode=1 if command[0] == "pytest" else 0,
                    stdout="",
                    stderr="failure" if command[0] == "pytest" else "",
                )

        runner = FakeRunner()
        exit_code, output = module.run([], root=ROOT, runner=runner)

        self.assertEqual(1, exit_code)
        self.assertIn("FAIL", output)
        self.assertEqual(4, len(runner.calls))


if __name__ == "__main__":
    unittest.main()
