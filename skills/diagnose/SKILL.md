---
name: diagnose
description: Build evidence loop before fixing bugs, regressions, or incidents.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: merge }
---

# Diagnose

## Procedure

1. Build smallest repeatable feedback loop for reported symptom. Prefer failing test, fixture command, replay, then targeted instrumentation. Make signal fast, deterministic, and specific.
2. Run loop repeatedly. Confirm exact reported failure, not adjacent error; raise reproduction rate for intermittent failures before diagnosis.
3. Write 3-5 ranked falsifiable hypotheses. Each states prediction. Probe one prediction at time with debugger or targeted tagged instrumentation.
4. Turn real repro into regression test at correct seam. Watch test fail; record missing seam as architectural finding.
5. Fix minimum cause. Re-run regression and original loop. Remove temporary probes and state confirmed hypothesis.

Stop if no trustworthy loop. State attempts and request reproduction artifact or access.
