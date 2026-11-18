# Skills adjacent to `wait-what`: eli5 and i-have-adhd

Retrieved 2026-11-18, 12:40-12:45 UTC, through the live GitHub API (repo
metadata, file trees, and the skill bodies at default-branch HEAD). The
skills.sh listing pages were fetched as discovery only. Source facts below
have high confidence unless marked. Verdicts are judgment. No upstream code
was executed and no upstream text was copied into this repository.

## Question and scope

Are `dreambigou/eli5` and `ayghri/i-have-adhd` adjacent to this catalog's
`wait-what`, were they already recorded, and should `PROVENANCE.md` record
them? "Current" means default-branch HEAD at retrieval. Out of scope: running
either skill, reproducing their evals.

Already recorded: no. Neither skill, repo, nor author appears anywhere in this
repository before this note (case-insensitive search of the tree, 2026-11-18).

## Sources

| Skill | Repo | HEAD | Last commit | License | Stars (API) |
|---|---|---|---|---|---|
| eli5 | [DreambigOu/ELI5](https://github.com/DreambigOu/ELI5), `skills/eli5/SKILL.md` | a766623b | 2026-03-18 | MIT | 2,001 |
| i-have-adhd | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd), `skills/i-have-adhd/SKILL.md` | 1ecea199 | 2026-10-11 | MIT | 61,582 |

Listings: [skills.sh eli5](https://www.skills.sh/dreambigou/eli5/eli5),
[skills.sh i-have-adhd](https://www.skills.sh/ayghri/i-have-adhd/i-have-adhd).
Install counts and audit badges were not recoverable from the fetched pages
(low confidence that none exist).

## What each one is

**eli5** (about 8 KB, model-invoked). Triggers on "ELI5", "explain this to my
...", "dumb it down". Three steps: identify the audience from four fixed
tables (ages, grade levels, job roles, relationships; default "Age 5"), read
the source material, then explain as what -> analogy -> details -> "so what".
Language and tone are calibrated per audience class. It states that for a
very non-technical audience "getting the core idea across at 80% accuracy is
better" than a fully accurate explanation that loses them. Self-reported
eval: three cases, one run each with and without the skill, graded on
per-case assertions.

**i-have-adhd** (about 7 KB, user-invoked, `disable-model-invocation: true`).
A persistent response style, on until the reader says "stop adhd mode". Ten
rules: lead with the next action, number multi-step work, end on one concrete
next action, suppress tangents, restate state every turn, give specific time
estimates, make completed work visible, matter-of-fact errors, cap lists at
five, no preamble or recap. Six override cases (explain requests, destructive
actions, debug spirals, real ambiguity, rule-versus-task, rule-versus-harness)
and a pre-send check ending in a first-line/last-line test. The repo also
ships a `SessionStart` hook for an always-on flag and adapters for several
harnesses. Self-reported eval (2026-08-02, `claude-opus-4-8`, 14 cases x 3
trials, same-model blind judge): weighted score 4.045 baseline to 4.473 with
the skill; its own release gate is recorded as FAILED on three blocking
findings.

## Adjacency to `wait-what`

`wait-what` is a four-step, user-invoked re-pitch for one moment: the prior
explanation did not land. It restates the topic, restores the minimum missing
context, re-pitches in short sentences using `GLOSSARY.md` vocabulary, and
asks one check question if ambiguity remains.

| | wait-what | eli5 | i-have-adhd |
|---|---|---|---|
| Trigger | explanation just failed | explicit audience request | user switches a mode on |
| Lifetime | one response | one response | whole session |
| Reader model | same reader, missing context | a named audience class | one reader profile, fixed |
| Vocabulary | the project's own terms | replaced with analogy | unchanged |
| Accuracy | unchanged | may be traded for reach | unchanged |

- **eli5 is adjacent** (inference). Same job family, simplifying an
  explanation, with a different cause assumed: `wait-what` treats the miss as
  missing context and keeps project vocabulary; eli5 treats it as the wrong
  register and swaps vocabulary for analogy. They would answer the same
  request differently.
- **i-have-adhd is a neighbor of a different kind** (inference). It is an
  output style, not a re-pitch. Its overlap with `wait-what` is narrow: the
  debug-spiral override (stop, name the assumption, ask one diagnostic
  question) mirrors `wait-what` step 4, and "restate state every turn"
  resembles steps 1-2.

## Crib candidates for `wait-what` (ideas, not text)

1. From eli5: purpose before mechanism - say why the thing exists before how
   it works. `wait-what` step 2 says "minimum missing context" without saying
   which context comes first.
2. From i-have-adhd: the first-line/last-line test as a self-check on the
   re-pitch (does the reader know what just happened and what to do next).
3. From i-have-adhd: restating position ("step 3 of 5") as one concrete form
   of step 1's one-sentence restatement.

None is tested. Per this catalog's authoring rule, a crib ships only after a
red-green pressure test shows a baseline gap; a four-step skill that grows a
fifth step for an unmeasured gain is the failure to avoid.

## Findings

- Record both in `PROVENANCE.md` as `exclude`. The precedent is the
  `ucsandman/claude-skills` row: scanned, license noted, no text copied, crib
  candidates named.
- eli5: exclude. The audience tables are content a model already has, and the
  stated accuracy trade conflicts with this catalog's verification
  disciplines.
- i-have-adhd: exclude. A persistent response style for one reader profile is
  personal and harness policy, which the README places outside the public
  catalog; the always-on hook is adapter territory.
- Proposed rows (not applied):

```
| DreambigOu/ELI5: eli5 | a766623b (2026-03-18) | exclude | - | Scanned 2026-11-18, MIT, no text copied. Audience-calibrated explanation; adjacent to `wait-what` but swaps project vocabulary for analogy and accepts reduced accuracy. One crib candidate recorded (purpose before mechanism), untested. |
| ayghri/i-have-adhd: i-have-adhd | 1ecea199 (2026-10-11) | exclude | - | Scanned 2026-11-18, MIT, no text copied. Session-persistent response style for one reader profile; personal and harness policy, not a portable procedure. Two crib candidates for `wait-what` recorded (first-line/last-line check, restated position), untested. |
```

## Open questions, assumptions, validation needed

- Assumed the skills.sh listings resolve to the GitHub repos above; the slugs
  match and GitHub redirects `dreambigou/eli5` to `DreambigOu/ELI5`, but the
  listing pages were not read in full.
- Both upstream evals are self-reported and were not reproduced. The
  i-have-adhd judge is the same model as the generator.
- Whether `wait-what` has a baseline gap any of the three cribs would close is
  unmeasured. A pressure test on a failed-explanation fixture would answer it.
- Star counts are the API's values at retrieval and say nothing about quality.
