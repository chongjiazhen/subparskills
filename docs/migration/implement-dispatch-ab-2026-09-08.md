# Implement-dispatch A/B: a fresh subagent per task as the `implement` default

Run 2026-09-08. Ticket `.agents/tickets/002-implement-dispatch-ab-evaluation.md`.
Evidence: [`implement-dispatch-ab-2026-09-08/`](implement-dispatch-ab-2026-09-08/) -
prompts, both `implement` bodies, the fixture builder, runner, grader, raw
stream-json transcripts, per-cell git log, diff stat and pytest tail, and
[`GRADING.md`](implement-dispatch-ab-2026-09-08/GRADING.md).

Source: obra/superpowers `subagent-driven-development` at `b36e0829`, already
pinned. No text copied; the borrowed idea is the dispatch model - controller
holds the plan, each task runs in a fresh implementer subagent, a separate
fresh subagent reviews it, the controller verifies before trusting either.

## Verdict

**Shipped** - `implement` steps 2 and 3. The baseline body never names a
subagent, and sonnet read it as it is written: on a three-task plan it
implemented every task in its own context. It did dispatch an independent
reviewer per task, so what the merge lost is the implementer seat, not the
review seat. The candidate makes dispatch the default and keys the inline
exemption to one edit in one file that no later task consumes. Sonnet under
the candidate produced the full shape (3 implementer + 3 reviewer dispatches,
controller re-ran the suite and diffed each commit before review) and stayed
inline on the one-file scenario, citing the exemption. 0/1 baseline cells
dispatched an implementer on the multi-task plan; 1/1 candidate cells did.
The shipped wording is byte-identical to the arm B body that was tested.

**Shipped untested** - `plan` step 8's hand-off sentence, which called
`implement` "solo in-context execution". That description is now false; the
edit is routing prose brought into line with the tested body, not a behavior
change with its own scenario.

## Method

Two scenarios over one fixture project, two arms, fresh session per cell.

- **m1** three-task plan with interfaces between tasks. **o1** one-task plan,
  a single string change in one file, the failing test already present.
- **A** baseline `implement`. **B** candidate. Every other skill identical.
- Cells isolated as in the forward-progress A/B: throwaway `HOME` and
  `CLAUDE_CONFIG_DIR` (credentials copied in, nothing else), a fresh copy of the
  fixture per cell on a `feat/v2` branch, prompt on stdin, `claude -p
  --dangerously-skip-permissions --output-format stream-json --verbose` so
  subagent dispatches are visible as top-level `Agent` tool_use events.
- Claude Code 2.1.263, python 3.13, Windows. Models: `sonnet` (primary),
  `claude-haiku-4-5-20251001` (second model).
- Graded from the dispatch events plus what reached disk - commits, diff stat,
  pytest tail - not from the arm's summary. `GRADING.md` records one criterion
  ruling made after the run and before grading the affected cells.

Same managed-policy confound as the earlier run: `C:\Program Files\ClaudeCode\CLAUDE.md`
still loads with `HOME` overridden. It carries repo maps and Windows traps, no
guidance about dispatch or review, identical across arms.

## What the baseline actually failed at

Not "no subagents". Sonnet baseline dispatched three reviewer subagents with
the `review` skill path and framed them neutrally. The failure is that step 2
("Execute one task at a time with the `tdd` skill") reads as an instruction to
the controller, and the controller obeyed it - the implementation of every
task, and the context it consumed, stayed in the one session that holds the
plan. Superpowers' whole argument for the model is that this is the context
that must survive to the last task.

## Haiku - not fixed, worth its own ticket

The candidate does not transfer. On m1 haiku read the candidate body and then
did what it did under baseline: everything inline, no review, no dispatch. On
o1 it did the opposite - dispatched an implementer and a reviewer for a
one-line string change, ignoring the exemption. Both cells landed working
code, so this is a cost failure on the small case and a no-op on the large
one. Haiku also skipped step 3's review entirely under both bodies on both
scenarios. This is the same shape the forward-progress A/B recorded: prose
gates that bind sonnet are read past by haiku. A deterministic step is the
remediation pattern; it is a separate change with its own red-green.

## Cost

Sonnet m1: $1.05 baseline, $1.83 candidate, roughly twice the wall clock. The
candidate's extra commits were two real review findings (a CRLF leak in
`render` on Windows, a `--config required=True` guard whose removal left the
suite green) plus ledger commits. Whether the seat is worth the spend on a
three-task plan is the operator's call; the catalog's position after this
change is that it is the default and the one-file case is the exemption.

## Limits

N=1 per differentiating cell on one model, one fixture, one scenario per
criterion. The candidate is demonstrated to produce the dispatch shape on
sonnet and demonstrated not to on haiku. Not tested: a plan whose tasks share
a file (the candidate says "in plan order", it does not say what to do when
an implementer's diff collides with the next brief); a harness with no
subagent tool (the exemption's first clause). Trigger to revisit: any live
`implement` session on a frontier model that stays inline across a multi-task
plan, or one that dispatches for a change the exemption names.
