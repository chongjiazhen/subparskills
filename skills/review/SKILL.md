---
name: review
description: Use when changes need review before integration, when asked to review a diff or pull request, or when acting on review feedback received on your own changes.
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
- Requesting review of your own changes: state subject and scope neutrally. Including your diagnosis, what you already fixed, or "confirm this is correct" framing anchors the reviewer toward agreement and forfeits the independent read. Frame around specific prior changes only when a verify-my-fix or regression pass is explicitly the request.
- Receiving review: verify each finding against the codebase before implementing it; if any item is unclear, clarify all unclear items before implementing any. Push back with technical reasoning where a finding is wrong - do not comply performatively.
