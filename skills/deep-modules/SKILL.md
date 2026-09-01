---
name: deep-modules
description: Use when designing or reshaping a module boundary - the interface feels wide, callers leak internals, or an abstraction spreads complexity instead of hiding it.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: architecture, source: adopt }
---

# Deep Modules

## Procedure

1. Identify caller knowledge required by current interface.
2. Move incidental coordination, invariants, and representation behind module seam.
3. Keep interface behavior-focused, stable, and directly testable.
4. Reject extraction that only moves complexity across callers.
