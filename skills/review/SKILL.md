---
name: review
description: Use when changes need review before integration, when asked to review a diff or pull request, or when acting on review feedback received on your own changes.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: merge }
---

# Review

## Procedure

1. Confirm the target ref resolves and the diff is non-empty. A bad ref or an empty diff ends the review here, with that message.
2. Read stated requirements and changed diff before judging implementation.
3. Find correctness, security, compatibility, test, and maintainability defects. Cite file and line.
4. Admit a finding only when it names the affected code and the input or state that triggers it, and the author would fix it on being told. A defect in a touched function that predates the change is in scope, labelled pre-existing. Prefer no findings to a padded list.
5. Classify findings by severity. Verify disputed claims with source or test.
6. Recheck critical and important fixes before approval. Cap fix/re-review rounds; at the cap, adjudicate every open finding explicitly and log the ruling - never drop one silently.

## Rules

- Review is read-only on the checkout: never move HEAD or mutate tree, index, or branch. Inspect another revision in a separate worktree.
- The implementer's own report or self-review never downgrades a finding or replaces review.
- Requesting review of your own changes: state subject and scope neutrally. Including your diagnosis, what you already fixed, or "confirm this is correct" framing anchors the reviewer toward agreement and forfeits the independent read. Frame around specific prior changes only when a verify-my-fix or regression pass is explicitly the request.
- Receiving review: verify each finding against the codebase before implementing it; if any item is unclear, clarify all unclear items before implementing any. Push back with technical reasoning where a finding is wrong - do not comply performatively.
- Every new defensive branch (guard, early return, fallback, `except`) gets a mutation check in a scratch copy or worktree: break the branch, run the suite, confirm a test fails by name, restore. A green suite with the branch broken means the branch is unprotected - report it as a missing test. A branch with no observable effect gets a docstring saying why; leave the test suite alone.
