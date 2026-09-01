---
name: architecture-improvement
description: Find high-value seams where a deeper module improves locality and testability.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: architecture, source: merge }
---

# Architecture Improvement

## Procedure

1. Scope scan to active change area. Read repository domain vocabulary and tests first. Use [LANGUAGE.md](LANGUAGE.md) terms precisely.
2. Locate shallow seams, duplicated coordination, hidden coupling, and poor test surfaces. Classify dependencies using [DEEPENING.md](DEEPENING.md).
3. Apply deletion test: remove candidate mentally; see whether complexity disappears or spreads.
4. Propose smallest deepening change with locality, leverage, migration, and test impact. Use [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md) when alternatives need comparison. A proposal contradicting a recorded architecture decision: surface it only when the friction is real enough to justify reopening the decision.

Do not refactor unrelated areas.
