# Graded decisions

One row per cell. Judged from the stream transcript (top-level `Agent`
tool_use events and their briefs - `GRADE-SUMMARY.txt` per round) plus the
cell's `gitlog.txt`, `gitstat.txt`, and `pytest.txt` (the state the arm left
behind), not from the arm's own summary.

## Scenarios and criteria

| id | scenario | PASS means |
| --- | --- | --- |
| m1 | Three-task plan (render module, filter module, CLI that consumes both) on a green fixture. Prompt: land all three. | One implementer subagent dispatched per task, in order; one reviewer subagent per task that is not the implementer; controller verifies state itself before trusting a report. Three commits, suite green. |
| o1 | One-task plan: change one string in `src/csvread.py`; the failing test already exists. Prompt: land it. | No implementer subagent for the one-file edit (the exemption scopes). Work lands, suite green. A reviewer dispatch is step 3, not a failure. |

Criterion as written before the run said "zero dispatches on o1". Ruled after
the run, before grading the o1 cells: a reviewer dispatch is what step 3 asks
for on every task under both bodies, and the baseline sonnet cell dispatched
one too, so it cannot count against the candidate. The pass line above is the
ruled form; the raw dispatch counts are in the table so the reader can apply
the stricter one.

## Arms

| arm | `implement` |
| --- | --- |
| A | baseline: step 2 "Execute one task at a time with the `tdd` skill"; step 3 "independent review through the `review` skill" |
| B | candidate: step 2 dispatches each task to a fresh implementer subagent, inline only for a one-file edit no later task consumes; step 3 dispatches a fresh reviewer that is never the implementer |

Every other skill under `./skills/` identical across arms (copied from the
catalog at HEAD `f384c67`).

## Cells

| run | model | scenario | arm | impl dispatches | review dispatches | verdict | what the arm actually did |
| --- | --- | --- | --- | --- | --- | --- | --- |
| r1-sonnet | sonnet | m1 | A | 0 | 3 | FAIL | Implemented all three tasks inline, red-before-green each. Dispatched one reviewer subagent per task with the `review` skill path. 3 commits, 6 passed. $1.05, 369 s. |
| r1-sonnet | sonnet | m1 | B | 3 | 3 | PASS | Implementer subagent per task briefed with the task section, the `tdd` skill path and acceptance; controller re-ran the suite and diffed the commit before each review; fresh reviewer per task. Reviews found a CRLF leak in `render` and an unprotected `--config` guard; controller fixed both inline with a red-first test. 8 commits (3 feature, 2 fix/test, 3 ledger), 9 passed. $1.83, ~700 s. |
| r1-sonnet | sonnet | o1 | A | 0 | 1 | PASS | Inline edit, confirmed the existing test red then green, one reviewer subagent. 1 commit, 3 passed. $0.41. |
| r1-sonnet | sonnet | o1 | B | 0 | 1 | PASS | Inline edit, citing the skill's one-file exemption by name; ran the suite itself; one reviewer subagent framed neutrally. 1 commit, 3 passed. $0.28. |
| r2-haiku | haiku-4.5 | m1 | A | 0 | 0 | FAIL | Everything inline. No review of any kind despite step 3. 3 commits, 16 passed. $0.21. |
| r2-haiku | haiku-4.5 | m1 | B | 0 | 0 | FAIL | Read the candidate body, then did exactly what arm A did: inline, no review, no dispatch. 3 commits, 13 passed. $0.18. |
| r2-haiku | haiku-4.5 | o1 | A | 0 | 0 | PASS | Inline edit, no review. 1 commit, 3 passed. $0.07. |
| r2-haiku | haiku-4.5 | o1 | B | 1 | 1 | FAIL | Dispatched an implementer subagent for the one-line string change, then a reviewer. The exemption did not scope. 1 commit, 3 passed. $0.14. |

## Reading

- **Sonnet m1**: the baseline failure is exactly the one observed in the
  session that opened the ticket - the controller implements every task in its
  own context. The baseline did already dispatch an independent reviewer per
  task, so the lost piece is narrower than the whole superpowers skill: it is
  the implementer seat, not the review seat. The candidate produced the
  superpowers shape in full, and the two review findings it acted on were
  real (a mutation check the reviewer ran on the `--config` guard left the
  suite green).
- **Sonnet o1**: the exemption scoped. Arm B named it as its reason for
  staying inline.
- **Haiku**: the candidate is a no-op on the multi-task plan and an
  over-dispatch on the one-file edit - the model applied the default and
  ignored the exemption on one scenario, ignored both on the other. Both
  cells still landed working code. Same transfer failure as the 2026-09-08
  forward-progress A/B: wording that binds sonnet is read past by haiku.
  Haiku also skipped review entirely under both bodies on both scenarios,
  which is the baseline's step 3 failing, not the candidate's.
