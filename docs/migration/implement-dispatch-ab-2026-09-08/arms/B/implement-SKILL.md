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
2. Dispatch each task, in plan order, to a fresh implementer subagent. Brief it with the task text, the interfaces it consumes and produces, the acceptance command and expected result, and the path of the `tdd` skill it must follow. It reports done, done-with-concerns, blocked, or needs-context; it never dispatches its own reviewers or helpers. Implement inline only when the harness exposes no subagent tool, or the task is one edit to one file that no later task consumes. Keep unrelated changes untouched.
3. Run task verification and inspect state yourself - the implementer's report is a claim, not evidence. Then dispatch a fresh reviewer subagent, never the implementer, with the `review` skill path, the task text, and the diff, before the next task starts. The implementer's self-review and the controller's own read never substitute.
4. Record each completed task with its evidence in a durable ledger file. On resume, trust the ledger over recollection. Re-run a task the ledger marks done only when one of these holds: its inputs changed in meaning, its pinned target or revision moved, its output is malformed or inconsistent with a consumer, or an observed run disproves the recorded result. A missing, stale, or mismatched ledger receipt is none of these - reuse the work, repair the record, and continue. Replay only the changed producer's dependents, not the whole task range.
5. After the last task passes review, invoke the `finish` skill for the integration decision.

## Rules

- Decide routine ambiguities yourself and log the ruling (what, why, cost if wrong). Stop and ask only for: an irreversible or destructive operation, a security-sensitive action, a side effect outside the workspace, a missing dependency, contradictory acceptance criteria, or verification failing repeatedly.
- A worker may report blocked or needs-context instead of guessing. Escalating uncertainty is never penalized; silently shipping unsure work is.
