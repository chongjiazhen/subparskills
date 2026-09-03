# Runbook

A wizard is generated from a runbook: the document a human or an agent follows when a known procedure repeats and forgetting a step is costly (a migration, a deploy, a recovery, scheduled maintenance). Write the runbook when the procedure will repeat and its steps are verifiable; skip it for a one-off job or a pure judgment call. Imperative present, as long as the procedure needs.

```md
# <Procedure>

Preconditions: <what must be true before step 1; how to check>
Rollback: <how to undo, or "none - forward-only">

## 1. <Step>

Run:      <the actual command, never "the usual cleanup">
Expect:   <the observable post-state that proves the step landed>
If not:   <the failure branch - what to check, and whether to stop>

## 2. <Step>
...
```

Rules: every step is cold-readable by someone with zero context; every step has a verify gate stated as a post-state, not as the command having exited 0; every failure mode the author has seen gets its own branch. It is a living document - refine it each time it is used.
