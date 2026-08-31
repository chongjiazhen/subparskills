# Interface Design

## Procedure

1. State constraints, dependency category, caller needs, and invariants.
2. Sketch at least two materially different interfaces: minimum surface and common-caller surface. Add extensible alternative only when real variation needs it.
3. For each, show caller usage, hidden implementation, adapters, error modes, and ordering rules.
4. Compare depth, locality, and migration cost. Recommend one interface and record rejected trade-offs.
