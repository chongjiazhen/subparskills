# Intermittent Failures

The target is not a perfect repro. The target is a reproduction rate high enough to debug against.

## Raise The Rate

- Run the trigger in a loop instead of waiting for one-off failure.
- Parallelize or stress the trigger when the bug depends on load or timing.
- Narrow the timing window with sleeps, retries, ordering controls, or fixture reduction.
- Capture enough metadata per run to separate true failures from lookalikes.

## Use Rate As The Signal

When the bug is probabilistic, compare failure rates before and after each probe or fix. A change that moves the rate in the predicted direction is evidence; a single passing run is not.

## Stop Condition

Do not move into root-cause guessing while the failure rate is too low to learn from. Keep working on the loop until the rate is materially higher or explain exactly what external artifact is still missing.
