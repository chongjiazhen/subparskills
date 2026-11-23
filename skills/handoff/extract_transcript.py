"""Extract the conversation text from a coding-agent session transcript.

Formats: Claude Code, Codex, pi, Qwen Code (JSONL) and OpenCode (SQLite).
Keeps user and assistant text only: drops tool calls, tool results, reasoning,
subagent entries and harness-injected context. Consecutive entries from one
role merge into one numbered turn.

Usage: python extract_transcript.py <session-id | transcript.jsonl | opencode.db> [--session ID] [--out PATH]
Prints the extract path, format, the session's working directory, and counts.
Exit 2: no transcript matches. Exit 3: unknown format or no conversation text -
never hand an empty extract on as a brief's input.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import tempfile
from pathlib import Path
from typing import Iterator

Turn = tuple[str, str]
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
CLAUDE_NOISE = ("<local-command-caveat>", "<local-command-stdout>", "[Request interrupted")
# Codex injects AGENTS.md and <environment_context>-style blocks as user input_text.
CODEX_NOISE = ("<", "# AGENTS.md instructions")
SCAN_LINES = 50  # format markers sit in the first entries of every JSONL format


class FormatError(Exception):
    pass


def home() -> Path:
    return Path.home()


def opencode_db() -> Path:
    base = os.environ.get("XDG_DATA_HOME") or str(home() / ".local" / "share")
    return Path(base) / "opencode" / "opencode.db"


def find_transcript(arg: str) -> tuple[Path, str | None] | None:
    """Return (path, opencode session id or None)."""
    path = Path(arg)
    if path.is_file():
        return path, None
    if arg.startswith("ses_"):
        db = opencode_db()
        return (db, arg) if db.is_file() else None
    codex = Path(os.environ.get("CODEX_HOME") or home() / ".codex")
    patterns = [
        (home() / ".claude" / "projects", f"*/{arg}.jsonl"),  # subagent files sit one level deeper
        (home() / ".qwen" / "projects", f"*/chats/{arg}.jsonl"),
        (home() / ".pi" / "agent" / "sessions", f"*/*_{arg}.jsonl"),
        (home() / ".pi" / "agent" / "sessions", f"*/*/forks/*_{arg}.jsonl"),
        (codex / "sessions", f"*/*/*/rollout-*{arg}.jsonl"),
    ]
    for root, pattern in patterns:
        hits = sorted(root.glob(pattern))
        if hits:
            return hits[0], None
    return None


def jsonl(source: Path) -> Iterator[dict]:
    with source.open(encoding="utf-8") as handle:
        for line in handle:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue  # a session killed mid-write leaves a torn last line
            if isinstance(entry, dict):
                yield entry


def detect(source: Path) -> str:
    for i, entry in enumerate(jsonl(source)):
        if i >= SCAN_LINES:
            break
        kind = entry.get("type")
        message = entry.get("message") if isinstance(entry.get("message"), dict) else {}
        if "payload" in entry and kind in ("session_meta", "response_item", "turn_context"):
            return "codex"
        if kind == "session" and "version" in entry:
            return "pi"
        if "parts" in message:
            return "qwen"
        if kind in ("user", "assistant") and "content" in message:
            return "claude"
    raise FormatError(f"unrecognised transcript format: {source}")


def claude(source: Path) -> tuple[list[Turn], str]:
    turns: list[Turn] = []
    cwd = ""
    for entry in jsonl(source):
        if entry.get("type") not in ("user", "assistant") or entry.get("isMeta") or entry.get("isSidechain"):
            continue
        cwd = entry.get("cwd") or cwd
        content = (entry.get("message") or {}).get("content")
        if isinstance(content, str):
            parts = [content]
        elif isinstance(content, list):
            parts = [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
        else:
            continue
        text = REMINDER.sub("", "\n".join(parts)).strip()
        if entry["type"] == "user" and text.startswith(CLAUDE_NOISE):
            continue
        turns.append(("summary" if entry.get("isCompactSummary") else entry["type"], text))
    return turns, cwd


def codex(source: Path) -> tuple[list[Turn], str]:
    turns: list[Turn] = []
    cwd = ""
    for entry in jsonl(source):
        payload = entry.get("payload") or {}
        if entry.get("type") in ("session_meta", "turn_context"):
            cwd = payload.get("cwd") or cwd
            continue
        # Reasoning and tool calls are separate payload types; developer is injected context.
        if entry.get("type") != "response_item" or payload.get("type") != "message":
            continue
        role = payload.get("role")
        if role not in ("user", "assistant"):
            continue
        for block in payload.get("content") or []:
            text = (block.get("text") or "").strip() if block.get("type") in ("input_text", "output_text") else ""
            if role == "user" and text.startswith(CODEX_NOISE):
                continue
            turns.append((role, text))
    return turns, cwd


def pi(source: Path) -> tuple[list[Turn], str]:
    turns: list[Turn] = []
    cwd = ""
    for entry in jsonl(source):
        kind = entry.get("type")
        if kind == "session":
            cwd = entry.get("cwd") or cwd
        elif kind == "compaction":
            turns.append(("summary", (entry.get("summary") or "").strip()))
        elif kind == "message":
            message = entry.get("message") or {}
            role = message.get("role")
            content = message.get("content")
            if role not in ("user", "assistant") or not isinstance(content, list):
                continue  # toolResult, system; custom_message is harness notices
            text = "\n".join(b.get("text", "") for b in content if b.get("type") == "text")
            turns.append((role, text.strip()))
    return turns, cwd


def qwen(source: Path) -> tuple[list[Turn], str]:
    turns: list[Turn] = []
    cwd = ""
    for entry in jsonl(source):
        if entry.get("type") not in ("user", "assistant"):
            continue  # system: telemetry, snapshots, compression; tool_result
        cwd = entry.get("cwd") or cwd
        parts = (entry.get("message") or {}).get("parts") or []
        text = "\n".join(p["text"] for p in parts if "text" in p and not p.get("thought"))
        turns.append(("assistant" if entry["type"] == "assistant" else "user", text.strip()))
    return turns, cwd


def opencode(db: Path, session_id: str | None) -> tuple[list[Turn], str]:
    if not session_id:
        raise FormatError("an OpenCode database needs --session ses_...")
    # Read-only, and only these three tables: the same file holds account tokens.
    conn = sqlite3.connect(f"file:{db.resolve().as_posix()}?mode=ro", uri=True)
    try:
        row = conn.execute("SELECT directory FROM session WHERE id = ?", (session_id,)).fetchone()
        if row is None:
            raise FormatError(f"no OpenCode session {session_id} in {db}")
        rows = conn.execute(
            "SELECT m.data, p.data FROM message m JOIN part p ON p.message_id = m.id"
            " WHERE m.session_id = ? ORDER BY m.time_created, m.id, p.time_created, p.id",
            (session_id,),
        ).fetchall()
    finally:
        conn.close()
    turns: list[Turn] = []
    for message_data, part_data in rows:
        role = json.loads(message_data).get("role")
        part = json.loads(part_data)
        if role in ("user", "assistant") and part.get("type") == "text" and not part.get("synthetic"):
            turns.append((role, (part.get("text") or "").strip()))
    return turns, row[0]


def merge(turns: list[Turn]) -> list[Turn]:
    merged: list[Turn] = []
    for role, text in turns:
        if not text:
            continue
        if merged and merged[-1][0] == role:
            merged[-1] = (role, merged[-1][1] + "\n\n" + text)
        else:
            merged.append((role, text))
    return merged


READERS = {"claude": claude, "codex": codex, "pi": pi, "qwen": qwen}


def extract(source: Path, session_id: str | None = None) -> tuple[list[Turn], str, str]:
    """Return (turns, cwd, format). Raises FormatError when nothing usable comes out."""
    if source.suffix == ".db":
        fmt = "opencode"
        turns, cwd = opencode(source, session_id)
    else:
        fmt = detect(source)
        turns, cwd = READERS[fmt](source)
    turns = merge(turns)
    if not turns:
        raise FormatError(f"no conversation text extracted from {source} ({fmt} format)")
    return turns, cwd, fmt


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("session", help="session id, transcript .jsonl, or opencode.db")
    parser.add_argument("--session", dest="session_id", help="OpenCode session id when passing a .db path")
    parser.add_argument("--out", type=Path, help="extract path (default: system temp dir)")
    args = parser.parse_args()

    found = find_transcript(args.session)
    if found is None:
        print(f"no transcript found for {args.session}", file=sys.stderr)
        return 2
    source, session_id = found
    session_id = args.session_id or session_id
    try:
        turns, cwd, fmt = extract(source, session_id)
    except FormatError as error:
        print(error, file=sys.stderr)
        return 3
    stem = session_id or source.stem
    out = args.out or Path(tempfile.gettempdir()) / f"handoff-extract-{stem}.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # Tags, not markdown headings: turn text carries its own headings.
    body = "\n\n".join(f'<turn n="{i}" role="{role}">\n{text}\n</turn>' for i, (role, text) in enumerate(turns, 1))
    out.write_text(body + "\n", encoding="utf-8")
    users = sum(1 for role, _ in turns if role == "user")
    print(f"extract: {out}")
    print(f"format: {fmt}")
    print(f"cwd: {cwd}")
    print(f"turns: {len(turns)} ({users} user), chars: {len(body)}, source bytes: {source.stat().st_size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
