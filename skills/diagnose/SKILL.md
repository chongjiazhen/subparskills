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

1. Build the smallest repeatable loop for the reported symptom. Make the signal specific enough to distinguish the real bug from nearby failures.
2. Run the loop until you can reproduce the exact reported behavior with enough confidence to debug against it.
3. Write 3-5 ranked falsifiable hypotheses. Each hypothesis must predict an observable change in the loop.
4. Probe one prediction at a time with debugger-first or targeted tagged instrumentation. For performance work, measure baseline before changing code.
5. Turn the real repro into a regression test at the correct seam. Watch it fail, apply the smallest fix, then re-run the regression and the original loop.
6. Remove temporary probes, state the confirmed hypothesis, and record missing seam or architecture findings separately.

Stop if no trustworthy loop. State attempts and request reproduction artifact or access.
