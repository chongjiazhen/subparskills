---
name: claim-ticket
description: Claim a single available tracker ticket before implementation.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# Claim ticket

## Procedure

1. Read the ticket schema in `../tracker/ticket-schema.md` and state rules in
   `../tracker/state-model.md`.
2. Confirm the ticket is in the frontier: it is `ready-for-agent`, unclaimed,
   and every blocker is `done`.
3. Refuse the claim if either claim field already records an actor or timestamp.
   Do not replace, steal, or silently clear another actor's claim.
4. Before making implementation edits, persist the claim actor and current
   ISO-8601 UTC timestamp, then set the ticket state to `claimed`.
5. Use the backend selected by tracker configuration and record the result in
   that backend before proceeding.
