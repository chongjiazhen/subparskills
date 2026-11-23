---
name: handoff
description: Use when a session ends with work unfinished, another operator or agent must continue, context must move to a different harness, directory, or owner, or an old or stale session must be resumed by its session id.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: adopt }
---

# Handoff

Continue in-session while the prompt cache is warm - it costs nothing and loses nothing. Hand off when context must change harness, directory, or owner. Past cache expiry, a retroactive handoff is cheaper than resume: resume reloads the whole context at full price and every later turn carries it.

## Procedure

1. State completed goal and scope.
2. List files changed and reason for each.
3. Record commands, observed results, risks, and unverified areas.
4. Redact secrets, credentials, and PII - the handoff may become another agent's literal prompt.
5. State exact next action and prerequisite context. Reference specs, plans, decision records, issues, and commits by path or URL; restate nothing they already hold.
6. Write the brief to a file in the receiving directory and report the path. Prefer the live-state file the repo already names; absent one, create one at its root.

## Retroactive Handoff

Use when resuming a session whose prompt cache has expired, or one too large to reload. Input: a session id. Same brief; the input is the dead session's transcript instead of live context.

1. Run [extract_transcript.py](extract_transcript.py) with the session id. It finds and reads Claude Code, Codex, pi, Qwen Code, and OpenCode sessions, keeps only user and assistant text, and prints the extract path and the session's working directory. Done when both print. Exit 2 (not found): pass the transcript path, or for OpenCode the database path plus `--session`. Exit 3 (unknown format or no text): stop and report it - never brief from an empty or guessed extract.
2. Dispatch one subagent, rooted in the printed working directory, to read the whole extract and write Procedure steps 1-5 to `.resume-<session-id>.md` at the repo root, plus Decisions (each with the options rejected) and the last 3 user messages verbatim. 60 lines maximum. It replies with one word.
3. Read only the brief, never the extract or transcript. Check every claim against the disk - `git status`, `git log`, each named file - and list each contradiction.
4. Report the summary, contradictions, and next action. Wait for a go before acting.
