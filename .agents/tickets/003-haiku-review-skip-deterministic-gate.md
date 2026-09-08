# 003: A weaker model cannot skip `implement`'s per-task review

Status: ready-for-agent
Claimed by: -
Claimed at: -
Blocked by: None

## Outcome

An `implement` run on haiku-4.5 (or any model that reads past prose gates)
cannot mark a task done without an independent review having run. Today the
review requirement lives in a sentence; the fix moves the guarantee into a
step the workflow executes, per `writing-for-agents` SKILL-AUTHORING, the
guarantees-in-a-script rule.

Observed 2026-09-08 (`docs/migration/implement-dispatch-ab-2026-09-08.md`):
on haiku-4.5, under both the pre- and post-change `implement` bodies, on
both a three-task plan and a one-file fix, the controller implemented
everything inline, dispatched no reviewer, and reported done. Sonnet under
the same bodies dispatched a reviewer per task every time. The
forward-progress A/B on the same day recorded the sibling failure: haiku
wrote `reviewed (independent)` into a ledger for a review that never ran.
Two A/Bs, same shape: a discipline rule that binds sonnet is a no-op on
haiku.

Queued: 2026-09-08T13:59:32+00:00.

## Acceptance criteria

- [ ] Freeze the current `implement` body as baseline. Reproduce the skip on
  haiku-4.5 in an isolated fresh session on the existing three-task fixture
  before any candidate is written; record the baseline transcript.
- [ ] The candidate is a deterministic layer, not more prose: a ledger-write
  or done-marking step that refuses when no review record for the task
  exists, a bundled check the body runs, or an equivalent the harness
  executes. Prose-only candidates (rationalization tables, STOP lists) may be
  tested as a comparison arm but do not satisfy this criterion on their own.
- [ ] On haiku-4.5 under the candidate, every task in the three-task plan
  has a review that ran in a separate context before the task is recorded
  done, or the run stops and says so. N=2 per differentiating cell.
- [ ] Sonnet under the candidate is unchanged in shape: still one implementer
  and one reviewer dispatch per task, still inline on the one-file fix.
- [ ] Both models still land working code: commits per task, suite green.
- [ ] Prompts, both bodies, harness settings, runner, raw transcripts, and
  graded decisions retained under `docs/migration/`. The
  `implement-dispatch-ab-2026-09-08/harness/` runner and fixture builder
  are reusable as-is.
- [ ] Out of scope: the haiku over-dispatch on the one-file fix, and haiku's
  counterexample failures from the forward-progress A/B (lock deletion,
  checksum overwrite). Record if observed, do not fix here.

## Evidence

