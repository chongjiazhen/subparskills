---
name: finish
description: Use when verified work on a branch is ready for integration - merge, pull request, keep, or discard decisions and branch cleanup.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Finish

## Procedure

1. Confirm workspace status and run full named verification.
2. Inspect diff against acceptance criteria and review findings.
3. Confirm the base branch the work forked from - merging into the wrong base is expensive to undo. Present integration choices: merge, pull request, retain branch, or discard with explicit authorization.
4. Never delete branches or worktrees without confirmation.
