---
name: to-tickets
description: Split approved work into independently verifiable tracker tickets.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# To tickets

## Procedure

1. Start only from approved work. State the user-visible outcome and the
   constraints that tickets must preserve.
2. Divide the work into small vertical slices. Each ticket must deliver an
   end-to-end behavior that a user or verifier can observe independently.
3. For every ticket, use the shared template in `../tracker/ticket-schema.md`.
   Write a specific outcome and observable acceptance criteria.
4. Record directed blocker edges in `Blocked by`; do not hide ordering in prose.
   Keep unrelated work independent and avoid tickets that are only layers or
   implementation phases.
5. Show the proposed ticket set, acceptance criteria, and blockers to the user.
   Obtain approval before publishing tickets.
6. After approval, publish through the backend selected by the tracker
   configuration. Follow the corresponding guide in `../tracker/backends/`.
