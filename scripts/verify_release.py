import argparse
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class CheckSpec:
    name: str
    command: list[str]


@dataclass(frozen=True)
class CheckResult:
    name: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str


def python_command() -> str:
    return Path(sys.executable).name or sys.executable


def npx_command() -> str:
    return "npx.cmd" if sys.platform.startswith("win") else "npx"


def default_checks(root: Path) -> list[CheckSpec]:
    _ = root
    return [
        CheckSpec("git diff check", ["git", "diff", "--check"]),
        CheckSpec("fixture installs", [python_command(), "scripts/verify_fixtures.py"]),
        CheckSpec("pytest", ["pytest", "-q"]),
        CheckSpec("skills cli discovery", [npx_command(), "skills", "add", ".", "--list"]),
    ]


def run_command(command: list[str], cwd: Path) -> CheckResult:
    completed = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
        timeout=120,
    )
    return CheckResult(
        name=" ".join(command[:2]),
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def render_summary(root: Path, results: list[CheckResult], generated_at: datetime) -> str:
    overall = "PASS" if all(result.returncode == 0 for result in results) else "FAIL"
    lines = [
        "# Release Verification",
        "",
        f"- generated_at: {generated_at.astimezone(timezone.utc).isoformat().replace('+00:00', 'Z')}",
        f"- root: {root}",
        f"- overall: {overall}",
        "",
    ]
    for result in results:
        detail = (result.stdout or result.stderr).strip() or "no output"
        lines.extend(
            [
                f"## {result.name}",
                f"- command: `{' '.join(result.command)}`",
                f"- status: {'PASS' if result.returncode == 0 else 'FAIL'}",
                f"- detail: {detail}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_evidence(path: Path, root: Path, results: list[CheckResult], generated_at: datetime) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_summary(root, results, generated_at), encoding="utf-8")


def run(argv: list[str] | None = None, root: Path = ROOT, runner=run_command) -> tuple[int, str]:
    parser = argparse.ArgumentParser(description="Run Subparskills release verification gates")
    parser.add_argument("--evidence", type=Path, help="write timestamped Markdown evidence to this path")
    parser.add_argument("--skip-cli", action="store_true", help="skip `npx skills add . --list`")
    args = parser.parse_args(argv)

    checks = default_checks(root)
    if args.skip_cli:
        checks = [check for check in checks if check.command[0] != npx_command()]

    generated_at = datetime.now(timezone.utc)
    results = [runner(check.command, root) for check in checks]
    summary = render_summary(root, results, generated_at)
    if args.evidence:
        write_evidence(args.evidence, root, results, generated_at)
    return (0 if all(result.returncode == 0 for result in results) else 1), summary


def main(argv: list[str] | None = None) -> int:
    exit_code, summary = run(argv)
    print(summary, end="")
    return exit_code
