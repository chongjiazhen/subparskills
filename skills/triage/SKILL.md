---
name: triage
description: Classify incoming tracker work into a compact state machine.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# Triage

## Procedure

1. Read the ticket, its outcome, acceptance criteria, blocker edges, and
   current evidence using `../tracker/ticket-schema.md`.
2. Choose exactly one triage state from `needs-triage`, `needs-info`,
   `ready-for-agent`, `ready-for-human`, or `wontfix` as defined in
   `../tracker/state-model.md`.
3. Use `needs-info` for a concrete missing fact, `ready-for-human` for a human
   decision or action, and `wontfix` for intentionally declined work.
4. Set `ready-for-agent` only when the outcome and acceptance criteria are
   specific enough to execute and blocker edges are recorded.
5. Persist the chosen state through the configured backend. Do not claim or
   complete work while triaging it.
