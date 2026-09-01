---
name: to-tickets
description: Use when approved work is too big for one sitting and needs splitting into independently verifiable tracker tickets with explicit blocker edges.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# To tickets

## Procedure

1. Read `.agents/tracker.md` and the selected guide in
   `../tracker/backends/` before any backend operation. If configuration is
   absent, use every default in the local backend guide.
2. Start only from approved work. State the user-visible outcome and the
   constraints that tickets must preserve. Read `GLOSSARY.md` and any recorded
   architecture decisions if present; use their vocabulary, and flag a conflict
   rather than silently overriding it.
3. Divide the work into small vertical slices. Each ticket must deliver an
   end-to-end behavior that a user or verifier can observe independently.
4. For every ticket, use the shared template in `../tracker/ticket-schema.md`.
   Write a specific outcome and observable acceptance criteria.
5. Record directed blocker edges in `Blocked by`; do not hide ordering in prose.
   Keep unrelated work independent and avoid tickets that are only layers or
   implementation phases. Exception: a mechanical, blast-radius-wide change
   (rename, retype) is not a vertical slice - ticket it as expand, then batched
   migrate, then contract, staying green between tickets.
6. Show the proposed ticket set, acceptance criteria, and blockers to the user.
   Obtain approval before publishing tickets.
7. After approval, publish using the configured ready, claim, completion, and
   blocker mappings. Follow the selected guide in `../tracker/backends/`.
   Publish only new tickets; never close or edit the issue or spec the work
   originated from.
