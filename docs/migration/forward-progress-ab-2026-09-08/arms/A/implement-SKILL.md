---
name: implement
description: Use when executing an approved plan or task list - small verified increments, per-task review, and a ledger that survives context loss.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Implement

## Procedure

1. Read plan and current workspace. Confirm a work branch, not the default branch, before the first edit; on the default branch or a shared checkout, invoke the `worktrees` skill first.
2. Execute one task at a time with the `tdd` skill. Keep unrelated changes untouched.
3. Run task verification and inspect state. Every task gets independent review through the `review` skill before the next starts; self-review never substitutes.
4. Record each completed task with its evidence in a durable ledger file. On resume, trust the ledger over recollection - never re-run a task the ledger marks done.
5. After the last task passes review, invoke the `finish` skill for the integration decision.

## Rules

- Decide routine ambiguities yourself and log the ruling (what, why, cost if wrong). Stop and ask only for: an irreversible or destructive operation, a security-sensitive action, a side effect outside the workspace, a missing dependency, contradictory acceptance criteria, or verification failing repeatedly.
- A worker may report blocked or needs-context instead of guessing. Escalating uncertainty is never penalized; silently shipping unsure work is.
