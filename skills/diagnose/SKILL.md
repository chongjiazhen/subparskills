---
name: diagnose
description: Build evidence loop before fixing bugs, regressions, or incidents.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: merge }
---

# Diagnose

Build a trustworthy evidence loop before fixing anything. The top-level procedure stays short; branch to the pointed references when the loop itself or the reproduction mode is the hard part.

Use [FEEDBACK-LOOPS.md](FEEDBACK-LOOPS.md) when the hard part is constructing or sharpening the repro loop. Use [INTERMITTENT-FAILURES.md](INTERMITTENT-FAILURES.md) when the bug is flaky or rate-based.

## Procedure

1. Build the smallest repeatable loop for the reported symptom. Make the signal specific enough to distinguish the real bug from nearby failures. The loop counts only once run: name the command and show output from a run you already did.
2. Run the loop until you can reproduce the exact reported behavior with enough confidence to debug against it. Shrink the repro one element at a time until everything left is load-bearing - cutting it flips the loop green.
3. Write 3-5 ranked falsifiable hypotheses. Each hypothesis must predict an observable change in the loop.
4. Probe one prediction at a time with debugger-first or targeted tagged instrumentation. An error surfacing deep in a call chain: trace backward to the originating call before fixing at the surfacing point. For performance work, measure baseline before changing code.
5. Turn the real repro into a regression test at the correct seam. Watch it fail, apply the smallest fix, then re-run the regression and the original loop.
6. Remove temporary probes, state the confirmed hypothesis, and record missing seam or architecture findings separately. Close by asking what would have prevented this bug; record the recommendation now, while the information is fresh.

Stop if no trustworthy loop. State attempts and request reproduction artifact or access.

## Rules

- Redact secrets in any shown command or output (`<REDACTED>`); build loops against env vars, not inline credentials.
- Catch yourself proposing a fix before the loop reproduces the bug: stop, return to step 1. "It's probably X, let me fix that" is the process breaking, not a shortcut through it.
- 3+ fixes failed at the same seam: stop - that is an architecture problem, not another hypothesis. Say so before attempting a fourth.
