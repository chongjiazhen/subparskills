# Integration Contract

Generated 2026-08-31T12:30:45.6448053Z.

This directory is opt-in only. Subparskills ships no default hooks, no background scripts, and no harness-specific mutation outside the documented adapters.

An integration belongs here only if all of the following stay true:

- it exposes the canonical skill body without forking procedure prose
- it is reversible by deleting the installed surface and re-running the documented installer
- it solves a real harness gap that adapters and native discovery cannot cover cleanly
- it can be verified with a repository test or fixture gate

Required boundaries:

- keep canonical skill text in `skills/`; integration files point at it, never copy-edit it
- prefer installer metadata and explicit commands over auto-run hooks
- no default hooks means a fresh install must stay inert until the operator chooses the integration
- install and uninstall steps must be documented in the integration itself and remain reversible

If a future integration needs scripts or hooks, add only the minimal surface required for that harness and prove the gap in tests before widening the contract.
