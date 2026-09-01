---
name: handoff
description: Use when a session ends with work unfinished, another operator or agent must continue, or context must move to a different harness, directory, or owner.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: adopt }
---

# Handoff

Continue in-session by default - it costs nothing and loses nothing. Hand off only when context must change harness, directory, or owner.

## Procedure

1. Reconcile claims against version control: enumerate changed files from fresh `git status` and `git log` output, never from recall. Flag any completion claim the history does not confirm; record uncommitted work and its disposition.
2. State completed goal and scope.
3. List files changed and reason for each.
4. Record commands, observed results, risks, and unverified areas.
5. Redact secrets, credentials, and PII - the handoff may become another agent's literal prompt.
6. State exact next action and prerequisite context.
