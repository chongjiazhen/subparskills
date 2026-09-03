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

1. State completed goal and scope.
2. List files changed and reason for each.
3. Record commands, observed results, risks, and unverified areas.
4. Redact secrets, credentials, and PII - the handoff may become another agent's literal prompt.
5. State exact next action and prerequisite context. Reference specs, plans, decision records, issues, and commits by path or URL; restate nothing they already hold.
6. Write the brief to a file in the receiving directory and report the path. Prefer the live-state file the repo already names; absent one, create one at its root.
