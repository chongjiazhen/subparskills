# Feedback Loops

The loop is the skill. Everything else depends on having a fast pass-fail signal you can rerun without reinterpretation.

## Loop Ladder

Try the cheapest loop that still exercises the real bug pattern:

1. Failing test at the closest real seam.
2. Fixture command or CLI invocation with stable input and asserted output.
3. Replay of captured payload, event, or trace through the isolated path.
4. Small harness that boots only the necessary subsystem.
5. Differential or bisection loop across versions, configs, or datasets.
6. Human-assisted script only when the trigger cannot be automated.

## Sharpening

- Faster: cache setup, skip unrelated startup, narrow fixtures.
- More specific: assert on the exact wrong value, error, or timing symptom.
- More deterministic: pin time, seed randomness, isolate filesystem, freeze network, reduce concurrency noise.

## Escalate

If you cannot build a trustworthy loop, stop and say so explicitly. List what you tried, then request the missing artifact, access, or permission for temporary instrumentation.
