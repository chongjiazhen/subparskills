---
name: triage
description: Classify incoming tracker work into a compact state machine.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge }
---

# Triage

## Procedure

1. Read `.agents/tracker.md` and the selected guide in
   `../tracker/backends/` before any backend operation. If configuration is
   absent, use every default in the local backend guide.
2. Read the ticket, its outcome, acceptance criteria, blocker edges, and
   current evidence using `../tracker/ticket-schema.md`.
3. Choose exactly one triage state from `needs-triage`, `needs-info`,
   `ready-for-agent`, `ready-for-human`, or `wontfix` as defined in
   `../tracker/state-model.md`.
4. Use `needs-info` for a concrete missing fact, `ready-for-human` for a human
   decision or action, and `wontfix` for intentionally declined work.
5. Set `ready-for-agent` only when the outcome and acceptance criteria are
   adequately specific to execute and blocker edges are recorded.
6. Persist the chosen state via the configured backend's semantic mappings.
   Do not claim or complete work while triaging it.
