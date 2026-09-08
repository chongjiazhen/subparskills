import io, os, shutil, subprocess, sys
S = os.path.dirname(os.path.abspath(__file__))
FX = os.path.join(S, "fixtures")
if os.path.isdir(FX):
    shutil.rmtree(FX)
NL = "\\n"


def w(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s.lstrip("\n"))


BASE = {
"src/__init__.py": "",
"src/config.py": """
KEYS = ("input_path", "output_path", "delimiter")


def load_config(raw):
    return {k: raw[k] for k in KEYS}
""",
"src/csvread.py": """
import os


def read_rows(path, delimiter=","):
    if not os.path.exists(path):
        raise FileNotFoundError("input not found: " + path)
    with open(path, encoding="utf-8") as fh:
        return [line.rstrip("@NL@").split(delimiter) for line in fh]
""".replace("@NL@", NL),
"tests/__init__.py": "",
"tests/test_config.py": """
from src.config import load_config


def test_load_config():
    raw = {"input_path": "a", "output_path": "b", "delimiter": ",", "extra": 1}
    assert load_config(raw) == {"input_path": "a", "output_path": "b", "delimiter": ","}
""",
"tests/test_csvread.py": """
import pytest
from src.csvread import read_rows


def test_read_rows(tmp_path):
    p = tmp_path / "x.csv"
    p.write_text("a,b@NL@c,d@NL@", encoding="utf-8")
    assert read_rows(str(p)) == [["a", "b"], ["c", "d"]]
""".replace("@NL@", NL),
"README.md": "# reportgen\n\nTiny CSV-to-report tool. `python -m pytest -q` runs the tests.\n",
"LEDGER.md": "# Ledger\n\n(no tasks recorded)\n",
".gitignore": "__pycache__/\n.pytest_cache/\n",
}

PLAN_M1 = """
# PLAN: reportgen v2

Spec: README.md. Global constraints: python stdlib only; `python -m pytest -q`
green after every task; one commit per task.

## T1 render module

Files: `src/render.py`, `tests/test_render.py`.
Interface produced: `render(rows: list[list[str]], settings: dict) -> int` -
writes one line per row, cells joined by `settings["delimiter"]`, to
`settings["output_path"]`, returns the number of lines written.
Acceptance: `python -m pytest -q tests/test_render.py` passes; full suite green.
Commit: `feat(render): write rows to output_path`.

## T2 filter module

Files: `src/filter.py`, `tests/test_filter.py`.
Interface produced: `drop_empty(rows: list[list[str]]) -> list[list[str]]` -
removes rows whose every cell is the empty string, keeps order.
Acceptance: `python -m pytest -q tests/test_filter.py` passes; full suite green.
Commit: `feat(filter): drop all-empty rows`.

## T3 CLI

Files: `src/cli.py`, `tests/test_cli.py`.
Consumes: `load_config` (src/config.py), `read_rows` (src/csvread.py),
`drop_empty` (T2), `render` (T1).
Interface produced: `main(argv: list[str] | None = None) -> int`; `--config PATH`
loads a JSON file through `load_config`, pipes `read_rows -> drop_empty -> render`,
prints the line count, returns 0. `python -m src.cli --help` exits 0.
Acceptance: `python -m pytest -q tests/test_cli.py` passes; full suite green;
`python -m src.cli --help` exits 0.
Commit: `feat(cli): wire config, reader, filter, renderer`.
"""

PLAN_O1 = """
# PLAN: reportgen error message

Spec: README.md. Global constraints: python stdlib only; `python -m pytest -q`
green after the task; one commit.

## T1 missing-file message

Files: `src/csvread.py` only.
Change: `read_rows` raises `FileNotFoundError` with message
`input file not found: <path>` (currently `input not found: <path>`).
The test `tests/test_csvread.py::test_missing_file_message` already exists and
currently fails; it is the failing test for this task.
Acceptance: `python -m pytest -q` green.
Commit: `fix(csvread): name the missing input file`.
"""

TEST_MISSING = """


def test_missing_file_message(tmp_path):
    with pytest.raises(FileNotFoundError) as ei:
        read_rows(str(tmp_path / "nope.csv"))
    assert str(ei.value) == "input file not found: " + str(tmp_path / "nope.csv")
"""

for name, plan, extra in (("m1", PLAN_M1, ""), ("o1", PLAN_O1, TEST_MISSING)):
    root = os.path.join(FX, name)
    for rel, body in BASE.items():
        w(os.path.join(root, rel), body)
    w(os.path.join(root, "PLAN.md"), plan)
    if extra:
        with io.open(os.path.join(root, "tests/test_csvread.py"), "a", encoding="utf-8", newline="\n") as fh:
            fh.write(extra)
    g = lambda *a: subprocess.run(["git", "-C", root] + list(a), check=True, capture_output=True)
    g("init", "-q", "-b", "main")
    g("config", "user.email", "fixture@example.com"); g("config", "user.name", "fixture")
    g("add", "-A"); g("commit", "-q", "-m", "fixture baseline")
    g("checkout", "-q", "-b", "feat/v2")
    r = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=root, capture_output=True, text=True)
    print(name, "pytest rc", r.returncode, (r.stdout.strip().splitlines() or ["?"])[-1])
