# 002: Evaluate subagent-per-task dispatch as the `implement` default

Status: done
Claimed by: claude-fable-5-1 (session 75a52d74)
Claimed at: 2026-09-08T13:15:00Z
Blocked by: None

## Outcome

Establish whether `implement` should default to dispatching each plan task to a
fresh implementer subagent with a separate fresh reviewer subagent, as
obra/superpowers `subagent-driven-development` did, and whether the wording
that says so also holds the inline exemption for a one-file edit. Adopt only
wording with demonstrated benefit. A documented no-change verdict is valid.

Observation that opened the ticket (2026-09-08): the merged catalog routes solo
in-context execution to `implement`, which never names a subagent, and reserves
`parallel-execution` for independent slices. Sequential one-subagent-per-task
with the controller holding the plan has no home. PROVENANCE maps
`subagent-driven-development` to `parallel-execution`; the 2026-09-01 rigor
audit reinstated three rules from that skill but never flagged the dispatch
model itself as lost.

## Acceptance criteria

- [x] Freeze the baseline `implement` body and the candidate before any cell
  runs; scenarios and grading criteria defined first. Isolated fresh session per
  cell, same model, settings, tools, and inputs across arms.
- [x] Multi-task plan: does the baseline dispatch an implementer per task and a
  reviewer that is not the implementer? Does the candidate?
- [x] One-file plan: does the candidate spawn subagents for a change the
  exemption names as inline?
- [x] Work still lands under both arms: commits per task, suite green, no
  regression in what reached disk.
- [x] Retain prompts, both skill bodies, model and harness settings, the runner,
  raw stream transcripts, per-cell git and pytest state, and graded decisions in
  repository-owned evidence. Second model where feasible.
- [x] Ship only the smallest change that fixes an observed baseline failure
  without regressing the counter-case.

## Result (2026-09-08)

Shipped `implement` steps 2-3 (arm B, byte-identical) and the matching `plan`
step 8 sentence. Write-up: `docs/migration/implement-dispatch-ab-2026-09-08.md`.
Sonnet: baseline 0/1 implementer dispatches on m1, candidate 1/1; exemption
held on o1 under both. Haiku: candidate no-op on m1, over-dispatch on o1,
no review under either body - recorded, owes its own ticket.
