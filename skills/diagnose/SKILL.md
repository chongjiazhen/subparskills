---
name: diagnose
description: Build evidence loop before fixing bugs, regressions, or incidents.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: merge }
---

# Diagnose

## Procedure

1. Build smallest repeatable feedback loop for reported symptom. Prefer failing test, fixture command, replay, then targeted instrumentation.
2. Run loop. Confirm exact reported failure, not adjacent error.
3. Write 3-5 ranked falsifiable hypotheses. Probe one prediction at time.
4. Turn real repro into regression test at correct seam. Watch test fail.
5. Fix minimum cause. Re-run regression, original loop, and cleanup temporary probes.

Stop if no trustworthy loop. State attempts and request reproduction artifact or access.
