---
name: plan
description: Turn approved design into small implementation tasks with acceptance evidence.
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
