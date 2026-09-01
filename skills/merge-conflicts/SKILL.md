---
name: merge-conflicts
description: Use when an in-progress Git merge or rebase has unresolved conflicts and intent must be preserved safely.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Merge Conflicts

## Procedure

1. Confirm merge or rebase state and list unresolved paths. Preserve unrelated work.
2. For every conflict, read common ancestor, each side, surrounding code, commit messages, tests, and linked requirements. Identify each change's intent before editing.
3. Preserve compatible intents. When intents conflict, choose only behavior supported by merge goal and primary sources; record trade-off. Do not invent behavior.
4. Remove markers, stage resolved paths, and run relevant checks. Resolve failures caused by integration before continuing.
5. Continue merge or rebase only after all current conflicts are resolved and verified. Finish only when repository reports no integration state.

Stop for user direction when resolution changes product behavior, security posture, secrets, deployment configuration, data meaning, or cannot be proved by sources and checks. Do not abandon merge or rebase without explicit user approval.
