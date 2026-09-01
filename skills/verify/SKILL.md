---
name: verify
description: Use when about to claim done, passing, fixed, complete, or ready to merge or release - every completion claim needs fresh evidence first.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: adopt }
---

# Verify

## Procedure

1. Map each acceptance claim to command, fixture, or read-back that proves it.
2. Run full checks fresh. Read output and inspect changed state, not only exit status.
3. Report exact evidence and remaining gaps. Do not claim pass without evidence.

## Rules

- A subagent, teammate, or prior run reporting "done" is not evidence - inspect the diff or state it claims to have changed.
- Hedge words ("should work", "probably fine") or satisfaction before running the check mark an unmet claim - run the proving command now, or report the claim as unverified.
- A linter, a compile, or one earlier green run is not evidence of the specific claim being made.
