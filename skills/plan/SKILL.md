---
name: plan
description: Use when an approved design or spec needs breaking into small implementation tasks with acceptance evidence, before multi-task execution starts.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Plan

## Procedure

1. State goal, constraints, files, and verification for each task, plus its interfaces: what it consumes from earlier tasks and produces for later ones, exact names and signatures.
2. Keep each task independently reviewable: failing test, minimal implementation, focused verification. Prefer the highest, fewest test seams - ideally one; confirm seam choice with the user.
3. Name exact commands and expected result. Remove placeholders and ambiguous steps.
4. Before execution: check every design requirement maps to a task, names and signatures agree across tasks, and every task pair sharing a file or interface is contradiction-free. Rule on conflicts before dispatching task one.
5. When execution crosses a process boundary - a separate worker session, a headless agent, or fan-out to another harness - persist the plan before dispatch; a worker in a fresh process cannot read a plan that lives only in this context. Write a dated file `docs/plans/YYYY-MM-DD-<feature>.md`, or route parallel claimable slices through `to-tickets`. Persist the contract concretely: file paths, interface signatures, acceptance command, expected output per task. Solo in-context execution needs no file.
