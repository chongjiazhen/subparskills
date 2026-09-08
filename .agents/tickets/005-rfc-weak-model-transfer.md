# 005: RFC - which skills survive on a 27B local model and a free-tier cloud model

Status: ready-for-human
Claimed by: -
Claimed at: -
Blocked by: None

## Outcome

A per-skill transfer verdict for the harnesses the catalog ships adapters
for but has never been tested on. Every skill carries `compatibility: Any
Agent Skills-compatible harness`; every A/B so far ran on `claude -p` with
sonnet as primary. The weakest model tested, haiku-4.5, read past the prose
gates in both 2026-09-08 A/Bs: skipped review under every body, deleted a
live writer lock and published, recorded a review that never ran, and
applied the dispatch default backwards. A 27B local model through the qwen
adapter and a free-tier cloud model through opencode or pi are the workers
the catalog will mostly run on, and the prior from haiku is that they do no
better.

The question is therefore not "do weak models benefit" but, per skill:
holds, holds only behind a deterministic gate, or does not transfer. That
verdict replaces the blanket compatibility line with a table, and tells
ticket 003 which shape of gate to build.

Why an RFC and not a ready ticket: the runner does not transfer. Dispatch,
skill loading and tool naming differ per harness, so a per-harness runner
is most of the cost, and the model roster, GPU time on a shared card, and
the cloud tier are the operator's call.

Queued: 2026-09-08T14:07:27+00:00.

## Decisions needed from the operator

- Roster: which 27B-class local model and serving path, which free-tier
  cloud model and through which adapter.
- Budget: phase 1 as bounded below, or narrower.
- Whether a failing verdict on a skill changes its body, its frontmatter,
  or only the README table.

## Acceptance criteria - phase 1, bounded

- [ ] Three scenarios that already discriminate on Claude models, reused
  as-is from `docs/migration/`: substantive invalidation (forward-progress
  s2), the live-lock counterexample (forward-progress c1), and the
  multi-task dispatch (implement-dispatch m1). Two arms each: the catalog
  body and no skill. N=2 per differentiating cell.
- [ ] One 27B-class local model through the qwen adapter and one free-tier
  cloud model through opencode or pi. Isolated fresh sessions; the same
  fixture copy per cell; the runner, prompts, raw transcripts, per-cell disk
  state and graded decisions retained under `docs/migration/`.
- [ ] Per scenario and model, one verdict from: holds, holds only behind a
  deterministic gate (name the gate), does not transfer. Graded from what
  reached disk, not the model's summary.
- [ ] A compatibility table in the README for the skills covered, replacing
  the blanket line for those rows only. Rows not covered keep the line and
  say so.
- [ ] A harness gap is a finding, not a blocker: if an adapter cannot load
  the skill or dispatch a subagent, record it against the adapter and grade
  the cell as not run.
- [ ] Out of scope for phase 1: the rest of the catalog, more than two
  models, per-model prompt tuning, and fixing anything found - each fix owes
  its own red-green.

## Evidence

