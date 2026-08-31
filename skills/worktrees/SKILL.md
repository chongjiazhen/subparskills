---
name: worktrees
description: Isolate concurrent feature work with Git worktrees and explicit branch ownership.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: adopt }
---

# Worktrees

## Procedure

1. Inspect repository status and target branch. Preserve existing work.
2. Create one named worktree and branch per isolated task.
3. Verify correct worktree, branch, and clean task scope before edits.
4. Remove worktree only after integration and explicit confirmation.
