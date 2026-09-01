---
name: worktrees
description: Use when parallel tasks would fight over one checkout, a build or review needs another branch without moving HEAD, or an experiment needs an isolated workspace.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: adopt }
---

# Worktrees

## Procedure

1. Inspect repository status and target branch. Preserve existing work.
2. Verify the worktree directory is gitignored before creating it; add and commit the ignore first if not. Create one named worktree and branch per isolated task.
3. Verify correct worktree, branch, and clean task scope before edits.
4. Remove worktree only after integration and explicit confirmation.
