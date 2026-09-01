---
name: review
description: Review changes against requirements, correctness, tests, and regressions.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: merge }
---

# Review

## Procedure

1. Read stated requirements and changed diff before judging implementation.
2. Find correctness, security, compatibility, test, and maintainability defects. Cite file and line.
3. Classify findings by severity. Verify disputed claims with source or test.
4. Recheck critical and important fixes before approval. Cap fix/re-review rounds; at the cap, adjudicate every open finding explicitly and log the ruling - never drop one silently.

## Rules

- Review is read-only on the checkout: never move HEAD or mutate tree, index, or branch. Inspect another revision in a separate worktree.
- The implementer's own report or self-review never downgrades a finding or replaces review.
- Receiving review: verify each finding against the codebase before implementing it; if any item is unclear, clarify all unclear items before implementing any. Push back with technical reasoning where a finding is wrong - do not comply performatively.
