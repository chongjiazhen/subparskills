---
name: measurement-standards
description: Use when about to produce, trust, or compare a number - a benchmark, rate, count, sweep result, pass/fail matrix, sweep winner, or a figure inherited from an earlier session, report, or handoff.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: original }
---

# Measurement Standards

Earn belief in a number before it decides anything. The failure this defends against is a vacuous measurement: a figure that reads as proof while proving nothing - and nothing in the output says so.

## Procedure

1. State what the number must support (a threshold, a comparison, a verdict) and what it actually measured: conditions, command, inputs. A figure whose conditions you cannot state supports nothing - re-derive it under known conditions, or say you cannot.
2. Validate the instrument with both controls before believing its output. Positive control: a known-good input of the same kind returns a hit through the same command - a zero-match sweep can mean the tool never saw the data (wrong encoding, wrong directory, wrong flag). Negative control: a deliberately wrong input returns a miss - an instrument that answers the same on fabricated input is agreeing, not discriminating. Both, or the sweep is vacuous in one direction and you will not know which.
3. Isolate the comparison. Pin exactly what served each arm before an A/B - an auto-routing layer picks a different backend per request, so an unpinned comparison measures the routing. Run arms in blocks, never interleaved (interleaving makes every run pay the previous run's cache miss), and keep contended resources out of the frame: latency or peak-memory measured while something else shares the machine is not comparable to anything, including a later run of itself.
4. Re-run before generalizing. One positive proves a mechanism possible, not reliable; a control validates the instrument, not the behavior's consistency. Merged, closed, or code-reviewed is not delivered - confirm the effect live.
5. For a sweep winner, discount selection luck before reporting "candidate K wins by D": the max of N candidates beats the field partly by chance, so establish the best-of-N-under-null floor (re-run the identical condition, or bootstrap it), confirm the metric covers the failure mode you care about, and correct the floor family-wise across K comparisons. Direction across all candidates is the honest signal, never the max.

## Provenance shapes

Where an untrustworthy number comes from - check the matching shape before resting a decision on it:

- **Inherited figure** - a past session's number did not record its conditions. Step 1 applies in full.
- **Invented fixture** - a parser or selector tested only on hand-written samples validates a shape the real system may never emit. Capture one real sample and assert on that.
- **Derived artifact** - a generated or ignored file is a cache of its generator. Re-run the generator and cite the command; read the field you mean, since a summary stat is not the log's last row.
- **Over-wide pull** - a per-entity query carries the entity's whole history, so a derived series can pair the wrong rows with every individual value real. Sanity-check derived counts against the window they should cover.
- **Misattributed guard** - a test cited as guarding a fix may be unreachable (an earlier gate means the fix never runs - revert the fix and the guard still passes), undiscriminable (the fix replaced an equivalent guard, so a fault trips both), or floating (baselines moved - pin both comparison points to the same parent). Read the fix's diff before crediting the test.
- **Order-dependent failure** - a defect attributed to a test's position in a sequence is usually shared state. Reorder the cases; if the failure moves, give each case its own fixture and assert the precondition directly.
