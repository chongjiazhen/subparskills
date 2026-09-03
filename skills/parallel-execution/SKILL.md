---
name: parallel-execution
description: Use when work splits into independent bounded tasks that could run as concurrent workers or subagents - briefing, dispatching, and verifying delegated work.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Parallel Execution

## Procedure

1. Split only independent work with no shared-file or ordering dependency.
2. Give each worker goal, scope, acceptance, and report format, including a status vocabulary: done, done-with-concerns, blocked, needs-context. Escalating uncertainty is never penalized; silently shipping unsure work is.
3. When workers write production code, dispatch in two phases: each worker reports its first failing test and the failure reason; the commander runs that test and confirms the failure before authorizing implementation. Name an integration test at every touchpoint between workers - it is the contract.
4. Keep integration, risk judgment, and final verification with commander. Workers never dispatch their own reviewers or helpers - review comes from the commander after the report.
5. Inspect each result independently before combining changes. A worker's report is a claim, not evidence - check the state it says it changed.
6. When workers commit to one shared checkout: commit by pathspec (`git commit -m "msg" -- <your paths>`) after `git diff --cached --stat` shows only your files. A bare `git commit` commits the whole index and sweeps whatever a sibling has staged into your commit.
