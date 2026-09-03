---
name: plan
description: Use when an approved design or spec needs breaking into small implementation tasks with acceptance evidence, before multi-task execution starts.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Plan

## Procedure

1. Search the spec for `[NEEDS CLARIFICATION` first. Any hit returns to `grill` before task one - a plan cannot settle what the spec left open, and a task written over a marker encodes a guess.
2. State goal, constraints, files, and verification for each task, plus its interfaces: what it consumes from earlier tasks and produces for later ones, exact names and signatures.
3. Keep each task independently reviewable: failing test, minimal implementation, focused verification. Prefer the highest, fewest test seams - ideally one; confirm seam choice with the user.
4. When a task retires a persisted shape, a wire field, or an interface whose consumers deploy separately, the removal is its own last task, gated on evidence that the old shape has no live reader; `implement` stops on it as destructive. The task before it names as acceptance a re-run that leaves state unchanged and a read that serves both shapes.
5. Write the plan in the shape of [TEMPLATE.md](TEMPLATE.md): the spec path in the header, a Global Constraints block copied verbatim from the spec, and each task ending in a commit step. Name exact commands and expected result. Remove placeholders and ambiguous steps.
6. Before execution: check every design requirement maps to a task, names and signatures agree across tasks, and every task pair sharing a file or interface is contradiction-free. Rule on conflicts before dispatching task one.
7. When execution crosses a process boundary - a separate worker session, a headless agent, or fan-out to another harness - persist the plan before dispatch; a worker in a fresh process cannot read a plan that lives only in this context. Write a dated file `docs/plans/YYYY-MM-DD-<feature>.md`, or route parallel claimable slices through `to-tickets`. Persist the contract concretely: file paths, interface signatures, acceptance command, expected output per task. Solo in-context execution needs no file.
8. Hand off: solo in-context execution to `implement`; across a process boundary to `parallel-execution` with the persisted file.
