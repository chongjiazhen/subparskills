# <Feature> Implementation Plan

Spec: docs/specs/YYYY-MM-DD-<feature>.md
Goal: one sentence.

## Global Constraints

Exact values copied verbatim from the spec: names, limits, formats. Every task's requirements include this block.

## Task N: <component>

Files: create / modify / test paths.
Consumes: exact names and signatures from earlier tasks.
Produces: exact names and signatures for later tasks.

- [ ] Failing test `<name>` pins <behavior>. Run: `<command>`. Expected: FAIL because <reason>.
- [ ] Minimal implementation. Run: `<command>`. Expected: PASS, suite green, output clean.
- [ ] Commit: `git commit -m "<type>(<scope>): <description>" -- <paths>`
