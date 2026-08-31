---
name: work-frontier
description: List tickets safe for an agent to claim.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# Work frontier

## Procedure

1. Read the configured backend and ticket records using
   `../tracker/ticket-schema.md` and `../tracker/state-model.md`.
2. Include a ticket only when its status is `ready-for-agent`, both claim
   fields are unclaimed, and every ticket in `Blocked by` is `done`.
3. Exclude tickets in all other triage or execution states, tickets with an
   active claim, and tickets with any unfinished or unresolved blocker.
4. Report each available ticket with its number, title, outcome, acceptance
   criteria, and blocker status. Do not claim or edit tickets while reporting.
