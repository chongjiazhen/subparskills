---
name: architecture-improvement
description: Find high-value seams where a deeper module improves locality and testability.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: architecture, source: merge }
---

# Architecture Improvement

## Procedure

1. Scope scan to active change area. Read domain vocabulary and tests first.
2. Locate shallow seams, duplicated coordination, hidden coupling, and poor test surfaces.
3. Apply deletion test: remove candidate mentally; see whether complexity disappears or spreads.
4. Propose smallest deepening change with locality, leverage, migration, and test impact.

Do not refactor unrelated areas.
