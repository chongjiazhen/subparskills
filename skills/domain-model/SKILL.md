---
name: domain-model
description: Discover domain language, invariants, and bounded concepts before changing behavior.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: architecture, source: merge }
---

# Domain Model

## Procedure

1. Read code, tests, docs, and examples around requested behavior.
2. Name concepts, relationships, invariants, lifecycle states, and ownership in user language.
3. Challenge terms that combine different concepts or hide ambiguity.
4. Record agreed vocabulary and use it in design, interfaces, tests, and handoff. Keep the vocabulary record free of implementation detail - it is a glossary, not a spec or scratch pad.
5. Offer a decision record only when reversal cost is real AND the choice will look surprising later AND a genuine alternative was rejected; skip otherwise.
