from __future__ import annotations

import importlib.util
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "skills" / "handoff"
SCRIPT = SKILL / "extract_transcript.py"
EXPECTED = [("user", "fix the parser"), ("assistant", "Reading it.\n\nFixed."), ("user", "commit it")]


def load_extractor():
    spec = importlib.util.spec_from_file_location("extract_transcript", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    # No __pycache__ inside the skill dir: the installer copies every file there.
    previous, sys.dont_write_bytecode = sys.dont_write_bytecode, True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


EXTRACTOR = load_extractor()


def write_jsonl(directory: str, entries: list[dict], name: str = "s.jsonl") -> Path:
    path = Path(directory) / name
    path.write_text("\n".join(json.dumps(e) for e in entries) + "\n{torn", encoding="utf-8")
    return path


def claude_entries() -> list[dict]:
    def user(content, **extra):
        return {"type": "user", "cwd": "/repo", "message": {"role": "user", "content": content}, **extra}

    def assistant(*blocks, **extra):
        return {"type": "assistant", "cwd": "/repo", "message": {"role": "assistant", "content": list(blocks)}, **extra}

    return [
        {"type": "attachment"},
        user("<system-reminder>injected</system-reminder>fix the parser"),
        user("<local-command-caveat>noise</local-command-caveat>"),
        user("meta prompt", isMeta=True),
        assistant({"type": "thinking", "thinking": "SECRET"}, {"type": "text", "text": "Reading it."}),
        assistant({"type": "tool_use", "name": "Bash", "input": {"command": "TOOL-CALL"}}),
        user([{"type": "tool_result", "content": "TOOL-OUTPUT"}]),
        assistant({"type": "text", "text": "Fixed."}),
        assistant({"type": "text", "text": "SIDECHAIN"}, isSidechain=True),
        user([{"type": "text", "text": "commit it"}]),
    ]


def codex_entries() -> list[dict]:
    def item(role, kind, text):
        return {"type": "response_item", "payload": {"type": "message", "role": role, "content": [{"type": kind, "text": text}]}}

    return [
        {"type": "session_meta", "payload": {"id": "abc", "cwd": "/repo"}},
        item("developer", "input_text", "DEVELOPER-PROMPT"),
        item("user", "input_text", "# AGENTS.md instructions for /repo\n<INSTRUCTIONS>x"),
        item("user", "input_text", "<environment_context>x</environment_context>"),
        item("user", "input_text", "fix the parser"),
        {"type": "response_item", "payload": {"type": "reasoning", "summary": [{"text": "SECRET"}]}},
        item("assistant", "output_text", "Reading it."),
        {"type": "response_item", "payload": {"type": "custom_tool_call", "input": "TOOL-CALL"}},
        {"type": "response_item", "payload": {"type": "custom_tool_call_output", "output": "TOOL-OUTPUT"}},
        item("assistant", "output_text", "Fixed."),
        {"type": "event_msg", "payload": {"type": "user_message", "message": "DUPLICATE"}},
        item("user", "input_text", "commit it"),
    ]


def pi_entries() -> list[dict]:
    def message(role, *blocks):
        return {"type": "message", "message": {"role": role, "content": list(blocks)}}

    return [
        {"type": "session", "version": 3, "id": "abc", "cwd": "/repo"},
        {"type": "model_change", "modelId": "m"},
        message("system", {"type": "text", "text": "SYSTEM"}),
        message("user", {"type": "text", "text": "fix the parser"}),
        message("assistant", {"type": "thinking", "thinking": "SECRET"}, {"type": "text", "text": "Reading it."},
                {"type": "toolCall", "name": "bash"}),
        message("toolResult", {"type": "text", "text": "TOOL-OUTPUT"}),
        {"type": "custom_message", "customType": "subagent-notify", "content": "NOTICE"},
        message("assistant", {"type": "text", "text": "Fixed."}),
        message("user", {"type": "text", "text": "commit it"}),
    ]


def qwen_entries() -> list[dict]:
    def entry(kind, role, *parts, **extra):
        return {"type": kind, "cwd": "/repo", "message": {"role": role, "parts": list(parts)}, **extra}

    return [
        entry("user", "user", {"text": "fix the parser"}),
        {"type": "system", "cwd": "/repo", "subtype": "ui_telemetry", "systemPayload": {}},
        entry("assistant", "model", {"text": "SECRET", "thought": True}, {"text": "Reading it."},
              {"functionCall": {"name": "shell"}}),
        entry("tool_result", "user", {"functionResponse": {"response": "TOOL-OUTPUT"}}),
        entry("assistant", "model", {"text": "Fixed."}),
        entry("user", "user", {"text": "commit it"}),
    ]


def opencode_db(directory: str, updated_ms: int = 0) -> Path:
    path = Path(directory) / "opencode.db"
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.executescript(
        "CREATE TABLE session (id text PRIMARY KEY, directory text, time_updated integer);"
        "CREATE TABLE message (id text PRIMARY KEY, session_id text, time_created integer, data text);"
        "CREATE TABLE part (id text PRIMARY KEY, message_id text, session_id text, time_created integer, data text);"
        "CREATE TABLE account (id text PRIMARY KEY, access_token text);"
    )
    conn.execute("INSERT INTO session VALUES ('ses_a', '/repo', ?), ('ses_other', '/elsewhere', ?)",
                 (updated_ms, updated_ms + 60_000))
    conn.execute("INSERT INTO account VALUES ('acc', 'TOKEN')")
    messages = [("m1", "ses_a", 1, "user"), ("m2", "ses_a", 2, "assistant"), ("m3", "ses_a", 3, "user"),
                ("m9", "ses_other", 0, "user")]
    for mid, sid, t, role in messages:
        conn.execute("INSERT INTO message VALUES (?, ?, ?, ?)", (mid, sid, t, json.dumps({"role": role})))
    parts = [
        ("p1", "m1", 1, {"type": "text", "text": "fix the parser"}),
        ("p2", "m1", 2, {"type": "text", "text": "SYNTHETIC", "synthetic": True}),
        ("p3", "m2", 1, {"type": "reasoning", "text": "SECRET"}),
        ("p4", "m2", 2, {"type": "text", "text": "Reading it."}),
        ("p5", "m2", 3, {"type": "tool", "state": {"output": "TOOL-OUTPUT"}}),
        ("p6", "m2", 4, {"type": "text", "text": "Fixed."}),
        ("p7", "m3", 1, {"type": "text", "text": "commit it"}),
        ("p9", "m9", 1, {"type": "text", "text": "OTHER-SESSION"}),
    ]
    for pid, mid, t, data in parts:
        sid = "ses_other" if mid == "m9" else "ses_a"
        conn.execute("INSERT INTO part VALUES (?, ?, ?, ?, ?)", (pid, mid, sid, t, json.dumps(data)))
    conn.commit()
    conn.close()
    return path


class HandoffExtractTest(unittest.TestCase):
    def test_skill_links_bundled_extractor(self) -> None:
        body = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("[extract_transcript.py](extract_transcript.py)", body)

    def test_each_jsonl_format_keeps_only_conversation_text(self) -> None:
        for fmt, entries in (("claude", claude_entries()), ("codex", codex_entries()),
                             ("pi", pi_entries()), ("qwen", qwen_entries())):
            with self.subTest(fmt), tempfile.TemporaryDirectory() as tmp:
                turns, cwd, detected = EXTRACTOR.extract(write_jsonl(tmp, entries))
                self.assertEqual((detected, cwd, turns), (fmt, "/repo", EXPECTED))

    def test_opencode_reads_one_session_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            turns, cwd, fmt = EXTRACTOR.extract(opencode_db(tmp), "ses_a")
        self.assertEqual((fmt, cwd, turns), ("opencode", "/repo", EXPECTED))

    def test_pi_compaction_summary_is_kept(self) -> None:
        entries = pi_entries()[:1] + [{"type": "compaction", "summary": "## Goal\nship it"}]
        with tempfile.TemporaryDirectory() as tmp:
            turns, _, _ = EXTRACTOR.extract(write_jsonl(tmp, entries))
        self.assertEqual(turns, [("summary", "## Goal\nship it")])

    def test_unknown_format_and_empty_extract_fail_loud(self) -> None:
        cases = {
            "unknown": [{"event": "something", "data": 1}],
            "empty": [{"type": "session", "version": 3, "cwd": "/repo"}, {"type": "model_change"}],
        }
        for name, entries in cases.items():
            with self.subTest(name), tempfile.TemporaryDirectory() as tmp:
                path = write_jsonl(tmp, entries)
                with self.assertRaises(EXTRACTOR.FormatError):
                    EXTRACTOR.extract(path)
                result = subprocess.run(
                    [sys.executable, "-B", str(SCRIPT), str(path), "--out", str(Path(tmp) / "x.md")],
                    capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 3, result.stderr)
                self.assertFalse((Path(tmp) / "x.md").exists())

    def test_opencode_unknown_session_fails_loud(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(EXTRACTOR.FormatError):
                EXTRACTOR.extract(opencode_db(tmp), "ses_missing")

    def test_latest_picks_newest_idle_session_for_cwd_across_harnesses(self) -> None:
        now = time.time()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def session(rel: str, entries: list[dict], age: float) -> Path:
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8")
                os.utime(path, (now - age, now - age))
                return path

            session(".claude/projects/r/old.jsonl", claude_entries(), 3600)
            session(".claude/projects/r/current.jsonl", claude_entries(), 10)  # the running session
            elsewhere = [dict(e, cwd="/elsewhere") for e in qwen_entries()]
            session(".qwen/projects/e/chats/q.jsonl", elsewhere, 400)  # newest idle, wrong cwd
            pi_path = session(".pi/agent/sessions/--repo--/2026-01-01T00-00-00-000Z_p.jsonl", pi_entries(), 600)
            db = opencode_db(str(root / "share" / "opencode"), int((now - 1200) * 1000))
            env = {"XDG_DATA_HOME": str(root / "share"), "CODEX_HOME": str(root / ".codex")}
            with mock.patch.object(EXTRACTOR, "home", lambda: root), mock.patch.dict(os.environ, env):
                self.assertEqual(EXTRACTOR.find_latest("/repo", now), (pi_path, None))
                os.utime(pi_path, (now - 7200, now - 7200))
                self.assertEqual(EXTRACTOR.find_latest("/repo/", now), (db, "ses_a"))
                with sqlite3.connect(db) as conn:  # a warm OpenCode session is skipped too
                    conn.execute("UPDATE session SET time_updated = ?", (int((now - 10) * 1000),))
                conn.close()
                self.assertEqual(EXTRACTOR.find_latest("/repo", now)[0].name, "old.jsonl")
                self.assertIsNone(EXTRACTOR.find_latest("/nowhere", now))


if __name__ == "__main__":
    unittest.main()
