---
name: work-frontier
description: List tickets safe for an agent to claim.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# Work frontier

## Procedure

1. Read `.agents/tracker.md` and the selected guide in
   `../tracker/backends/` before any backend operation. If configuration is
   absent, use every default in the local backend guide. Read ticket records
   using `../tracker/ticket-schema.md` and `../tracker/state-model.md`.
2. Include a ticket only when it matches the configured ready state, its
   configured claim representation is empty, and every configured blocker
   satisfies the completion convention with non-empty evidence.
3. Exclude tickets in all other triage or execution states, tickets with an
   active claim, and tickets with any unfinished or unresolved blocker.
4. Report each available ticket with its number, title, outcome, acceptance
   criteria, and blocker status. Do not claim or edit tickets while reporting.
