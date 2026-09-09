# 006: A/B - does an edit-radius cap in the brief contract reduce over-editing

Status: ready-for-human
Claimed by: -
Claimed at: -
Blocked by: None

## Outcome

A verdict on whether naming the in-scope files and an "unrelated style stays
as found" line in the `parallel-execution` brief contract measurably shrinks a
worker's diff on code it did not write, without costing correctness.

The prior is arXiv 2609.03894 (Crocodil): four open-weight models edited their
own implementations up to 14% less than each other's, on 14 of 16 pairings.
The paper's mitigation is post-training (GRPO + LoRA on Olmo3 7B) and does not
transfer to a catalog of prose skills. The open question is whether the prose
half of the same idea - a scope cap in the brief - buys any of it.

The effect did NOT hold for the one closed model tested: Haiku 4.5's minimum
edit distance fell on GPT-OSS 20B's code, not its own. The authors flag this
as unexplained and note GPT-5 and Claude Opus were not evaluated. So the cell
that matters here is the local-transport worker, not a Claude subagent, and a
null result on sonnet is not evidence of absence on qwen.

The atelier private half of this line already shipped 2026-09-09 in
`guidelines/delegation.md` §2 - that surface is operator-register and owes no
A/B. This ticket covers only the portable half, which would change a skill
body every harness loads.

Queued: 2026-09-09T15:40:48+00:00.

## Decisions needed from the operator

- Whether a null result on Claude models is enough to drop the line, or
  whether it ships on the qwen-adapter evidence alone.
- Whether the cap belongs in `parallel-execution` (every brief pays it) or
  only in the code-change template, given the resident-body cost.

## Acceptance criteria

- [ ] A fixture where the implementation under edit was written by a
      DIFFERENT model than the editor - that cross-model pairing is the whole
      effect, and a same-model fixture cannot measure it. Generate the
      implementation arm-blind, before either brief body is chosen.
- [ ] Two arms: current `parallel-execution` body, and that body plus the
      edit-radius clause. N=2 per differentiating cell, isolated fresh
      sessions, same fixture copy per cell.
- [ ] At least one local-transport model through the qwen adapter, since that
      is the measured cell. A Claude arm is a control, not the result.
- [ ] Primary metric is diff size against the pre-edit tree, graded from disk
      (`git diff --stat`), never from the worker's own summary. Secondary
      metric is the fixture's test suite - a smaller diff that breaks tests is
      a fail, not a win.
- [ ] Report the correctness metric even when the diff metric wins. A scope
      cap that buys a smaller diff by skipping required work is the failure
      mode this ticket is most likely to produce.
- [ ] Raw transcripts, per-cell disk state and graded decisions retained under
      `docs/migration/`.
- [ ] Out of scope: changing any skill body on a null result, per-model prompt
      tuning, and the post-training half of the paper.

## Evidence
