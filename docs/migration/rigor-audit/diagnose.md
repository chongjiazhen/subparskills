# Audit: diagnose merge vs upstream (systematic-debugging + diagnosing-bugs)

Merged counterpart audited: `skills/diagnose/{SKILL.md,FEEDBACK-LOOPS.md,INTERMITTENT-FAILURES.md}`.
Merge is structurally the upstream `diagnosing-bugs` (loop -> reproduce -> hypothesise -> instrument
-> fix+test -> cleanup). None of superpowers `systematic-debugging`'s distinct machinery
(Iron Law, Red Flags, Rationalizations table, 3-fixes-architecture rule, Pattern Analysis phase,
root-cause-tracing, defense-in-depth) survived into any catalog skill - grepped the whole
`skills/` tree for `root cause|defense-in-depth|condition-based|Iron Law|rationalization|red flag`,
zero hits outside diagnose's own files.

## LOST-LOAD-BEARING

### 1. Common Rationalizations table - HIGH
Upstream: `systematic-debugging/SKILL.md` "## Common Rationalizations" (8-row excuse->reality
table: "Issue is simple", "Emergency, no time", "I'll write test after confirming fix works",
"Multiple fixes at once saves time", "I see the problem, let me fix it", etc.)
Failure mode defended: agent talks itself out of the process under time pressure or false
confidence - exactly the "if you think X / actually Y" pattern this audit targets. Nothing in
`diagnose/SKILL.md` counters a specific rationalization; it only states the procedure.
Reinstatement (terse register): add to `diagnose/SKILL.md` a short "## Rationalizations" table,
3-4 rows max: simple-issue, emergency, "I'll test after", "one more fix" (folds in #3 below).

### 2. Iron Law + Red Flags stop-list - HIGH
Upstream: `systematic-debugging/SKILL.md` "The Iron Law" (`NO FIXES WITHOUT ROOT CAUSE
INVESTIGATION FIRST`) and "## Red Flags - STOP and Follow Process" (verbatim self-talk triggers:
"Quick fix for now, investigate later", "Just try changing X and see if it works", "It's
probably X, let me fix that", "Here are the main problems: [lists fixes without investigation]").
Failure mode defended: agent proposes a fix before establishing repro/hypothesis - the merged
skill's numbered steps imply order but never says "catching yourself here means stop."
Upstream's own weaker version of this ("if you catch yourself reading code to build a theory
before this command exists, stop") was also dropped from the merge, compounding the loss.
Reinstatement: one line under Step 1 - "Catch yourself proposing a fix before Step 2 finishes -> stop, return to Step 1."

### 3. 3+ failed fixes -> question architecture - HIGH
Upstream: `systematic-debugging/SKILL.md` Phase 4 step 5 ("If 3+ Fixes Failed: Question
Architecture" - each fix revealing new coupling elsewhere, "massive refactoring" needed, is not
a failed hypothesis, it's a wrong architecture; discuss before attempting more fixes).
Failure mode defended: unbounded fix-thrash - agent keeps patching symptoms in different spots
instead of recognizing a structural problem. Merged `diagnose` has no fix-attempt counter or
architecture-question trigger at all.
Reinstatement: append to Step 5 - "3+ fixes failed at the same seam without resolving it: stop: this is an architecture problem, not another hypothesis. Say so before attempting a 4th."

### 4. Redact secrets in captured diagnostic output - HIGH
Upstream: `diagnosing-bugs/SKILL.md` "## Redact" (write `<REDACTED>` over secrets before showing
commands/output; build loops against env vars so credentials stay in the environment, not in
what's displayed; quote only signal-bearing lines from artifacts carrying auth headers).
Failure mode defended: an agent diagnosing a bug involving curl/HTTP/logs pastes an
Authorization header or API key straight into chat/commit/report. This is a hard safety rule,
not debugging style, and it is entirely absent - grepped `REDACTED|redact|secret` across all of
`skills/`, zero hits. It also does not survive into the operator's deepened version.
Reinstatement: new line, top of `diagnose/SKILL.md` procedure - "Redact secrets in any shown command/output (`<REDACTED>`); build loops against env vars, not inline credentials."

### 5. Minimise phase - MED/HIGH
Upstream: `diagnosing-bugs/SKILL.md` Phase 2 "### Minimise" - once red, shrink the repro to the
smallest scenario that still fails, cutting inputs/callers/config one at a time, re-running
after each cut; done when every remaining element is load-bearing (removing it goes green).
Failure mode defended: debugging against a bloated, confounded repro inflates the hypothesis
space in Step 3 and produces a noisy, over-broad regression test in Step 5. Completely absent
from merged Step 2 ("Reproduce") - the word "minimise" does not appear anywhere in `diagnose/`.
Reinstatement: add to Step 2 - "Shrink the repro one element at a time until everything left is load-bearing (cutting it flips the loop green) - this is what Step 3-5 will actually debug against."

### 6. Backward root-cause tracing technique - MED
Upstream: `systematic-debugging/root-cause-tracing.md` - explicit algorithm (observe symptom ->
find immediate cause -> ask "what called this?" -> keep tracing up -> find original trigger;
never fix just where the error surfaces) plus the instrumentation tip (log before the dangerous
op, `console.error` not logger in tests, capture `new Error().stack`).
Failure mode defended: fixing at the point an error becomes visible (e.g. patching a null-check
deep in a call chain) instead of the actual originating call site. Merged Step 4 ("Instrument")
covers probing generically but never states the backward-tracing method or "never fix just the
symptom point" rule explicitly.
Reinstatement: one line in Step 4 - "Error surfaces deep in a call chain? Trace backward call-by-call to the original trigger before instrumenting there - don't fix at the surfacing point."

### 7. Proof-of-loop before proceeding - MED
Upstream: `diagnosing-bugs/SKILL.md` "### Completion criterion" - Phase 1 is done only when you
can name one command **already run at least once**, with its invocation and output shown
(redacted), satisfying explicit checkboxes (red-capable / deterministic / fast / agent-runnable).
Failure mode defended: agent claims "I have a repro loop" without ever having executed it -
unverifiable, fabrication-shaped completion claim. Merged Step 1/2 describes loop qualities in
prose but drops the "show the command you already ran + its output" evidence requirement.
Reinstatement: append to Step 1 - "Name the command and show its output from a run you already did - a loop you haven't executed yet doesn't count."

### 8. Pattern Analysis phase (compare against working/reference code) - MED
Upstream: `systematic-debugging/SKILL.md` Phase 2 "Pattern Analysis" - find a working example in
the same codebase, read any reference implementation COMPLETELY (not skimmed), list every
difference between working and broken however small, understand what the pattern depends on.
Failure mode defended: "reference too long, I'll adapt the pattern" / partial-understanding
implementation, called out explicitly in that skill's own rationalizations table. No equivalent
step exists anywhere in merged `diagnose` - hypothesis generation (Step 3) jumps straight from
symptom to guesses without a compare-to-working-example step.
Reinstatement: fold into Step 3 - "Before ranking hypotheses, diff against a working example or the reference implementation you're matching, read it in full, and list every difference."

### 9. Defense-in-depth after root cause found - LOW/MED
Upstream: `defense-in-depth.md` - validate at every layer data passes through (entry, business
logic, environment guard, debug instrumentation), because a single validation point gets
bypassed by a different code path, a mock, or a refactor; "single validation: we fixed the bug;
multiple layers: we made the bug impossible."
Failure mode defended: complacency after one fix - "one check is enough" - when the same bad
value can reach the failure point through another path. Weaker than items 1-7 since it's a
completeness technique rather than a hard gate, and it sits in some tension with the catalog's
"smallest fix" ethos (disposition.md "least code that works") - plausible this was pruned on
purpose. Still, nothing in merged Step 5 mentions checking for other paths to the same failure.
Reinstatement (optional, low priority): append to Step 5 - "Check whether the bad value can reach the failure point through another caller/path before calling the fix complete."

## PRUNED-OK (tally)

- Multi-component evidence-gathering example (Phase 1.4 CI->build->signing bash block) - redundant with Step 4 instrument guidance, one example beyond the pattern.
- "your human partner's Signals You're Doing It Wrong" - soft/branded persona content, redundant with Red Flags (which is itself lost, but this variant is the weaker one).
- Real-World-Impact stats blocks ("1847 tests passed", "60%->100% pass rate") - session-log fixtures, not generalizable rules.
- `find-polluter.sh` bisection script pointer, dot-graph diagrams in root-cause-tracing.md - formatting/tooling, substance covered in prose.
- `condition-based-waiting.md` (arbitrary sleep -> poll-for-condition in tests) - narrow test-authoring technique, not a diagnostic gate; no catalog skill (tdd/verify) covers it either, but it's implementation-style guidance rather than agent-behavior-gating. Judgment call - could be reinstated as one line in `tdd` if flaky tests recur, not urgent.
- `hitl-loop.template.sh` - reusable script; the technique ("drive a human with a structured capture script") is already named in FEEDBACK-LOOPS.md's loop ladder item 6.
- Headless-browser-script loop-ladder item (pocock #4) - one example among many equivalent loop types, condensed away, substance ("build the cheapest loop that exercises the real pattern") retained.

## KEPT (tally)

- Overall phase skeleton: loop -> reproduce -> hypothesise -> instrument -> fix+regression-test -> cleanup.
- 3-5 ranked falsifiable hypotheses requirement, with the "if you can't state the prediction it's a vibe" framing.
- Tagged debug-log convention (`[DEBUG-xxxx]`) and grep-to-clean requirement.
- Perf-branch "measure baseline before bisecting" rule.
- Seam-conditional regression test (no correct seam = note the gap, don't fake a shallow test).
- Cleanup checklist (repro re-run, regression passes, debug tags removed, hypothesis recorded).
- Non-deterministic-bug rate-raising ladder (loop the trigger, stress, narrow timing) - preserved almost verbatim in `INTERMITTENT-FAILURES.md`.
- Loop ladder ordering (test > CLI/fixture > replay > harness > differential/bisection > human-assisted).

## Operator deepened version (private) vs merged

Single-file monolith (no split FEEDBACK-LOOPS/INTERMITTENT-FAILURES); content is the upstream
skill re-stepped to match the merged catalog's 6-step shape, plus repo-specific pointers
(factlog domain check, a repo-specific evidence guide for live-incident gathering).

**(a) Load-bearing in operator, missing from merged:**
- Post-mortem reflection at Step 6 close: "ask what would have prevented this bug... hand off to `/improve` with specifics, make the recommendation after the fix is in (more information than at the start)." Merged Step 6 stops at the cleanup checklist and never closes the loop into architecture follow-up. Minor but real: it's the only place in either version that captures anything like upstream's "3+ fixes -> question architecture" spirit (post-hoc rather than as a stop-gate). Worth porting into merged Step 6 as a closing line.
- That's the only substantive addition. Everything else upstream flagged as lost above (Redact, Minimise, Iron Law/Red Flags, rationalizations table, root-cause-tracing, defense-in-depth, pattern-analysis, proof-of-loop) is **also missing from the operator version** - the personal deepening did not restore any of it.

**(b) Bloat in operator vs merged:**
- None substantial. It's roughly the same length/density as merged's SKILL.md+FEEDBACK-LOOPS.md combined, just not split into reference files - a structural inconsistency with the rest of the catalog's split-on-demand pattern, not padding.
- The factlog/evidence-guide pointers are appropriate single-line personalization (repo-specific routing), not restatement of another layer.
- No redundant restatement or over-specification found worth flagging.
