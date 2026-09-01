---
name: claim-ticket
description: Use when about to start tracker work - claim exactly one available ticket first so parallel agents never collide on the same work.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# Claim ticket

## Procedure

1. Read `.agents/tracker.md` and the selected guide in
   `../tracker/backends/` before any backend operation. If configuration is
   absent, use every default in the local backend guide. Also read the ticket
   schema in `../tracker/ticket-schema.md` and state rules in
   `../tracker/state-model.md`.
2. Confirm the ticket is in the configured ready state, unclaimed, and every
   blocker satisfies the configured completion convention with evidence.
3. Refuse the claim if the configured claim representation already records an
   actor or timestamp.
   Do not replace, steal, or silently clear another actor's claim.
4. Before making implementation edits, persist the claim actor and current
   ISO-8601 UTC timestamp using the configured claim convention.
5. Record the resulting claimed state in the selected backend before
   proceeding.
