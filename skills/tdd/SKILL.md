---
name: tdd
description: Use red-green-refactor for features and bug fixes.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: merge }
---

# Test-Driven Development

Read [PRESSURE.md](PRESSURE.md) when tempted to skip, reorder, or backfill a step.

## Procedure

1. Name one observable behavior and production change test must catch.
2. Write smallest real-behavior test. Run it; confirm it fails for the missing behavior - a pass means it tests existing behavior (fix test); an error means broken setup, not a valid red (fix, re-run).
3. Write minimum production code. Run focused test; confirm pass, rest of relevant suite green, output clean.
4. Refactor only while full relevant suite stays green.
5. Repeat one behavior at a time - never a batch of tests before any implementation.

## Rules

- No production code before observed failing test. Code already written before its test: delete it - do not adapt it or keep it as reference; rewrite from the test.
- Bug fix follows the same law: failing test reproducing the bug first.
- Derive expected values independently (hand literal, not the code's own helper) - a test that recomputes what the code computes passes by construction.
- Mock only external boundaries, never own modules. An assertion whose target is a mock: unmock it or delete the assertion.
- Before calling a test done, mentally mutate the code it protects (wrong branch, dropped side effect, empty return) - if no test would fail, the behavior is unprotected.
- Ask user before exempting generated code or throwaway probe.
