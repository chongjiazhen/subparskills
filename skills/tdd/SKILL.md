---
name: tdd
description: Use red-green-refactor for features and bug fixes.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: core, source: merge }
---

# Test-Driven Development

## Procedure

1. Name one observable behavior and production change test must catch.
2. Write smallest real-behavior test. Run it; confirm expected failure caused by missing behavior.
3. Write minimum production code. Run focused test; confirm pass.
4. Refactor only while full relevant suite stays green.

No production code before observed failing test. Ask user before exempting generated code or throwaway probe.
