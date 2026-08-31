# Deepening

Classify dependency before deepening module:

1. **In-process**: merge and test through new interface.
2. **Local-substitutable**: use local stand-in behind internal seam.
3. **Owned remote**: define port at seam; inject production and in-memory adapters.
4. **External**: inject narrow port; test against mock adapter.

Tests cross module interface and assert observable outcomes. Delete shallow
module tests once interface tests cover behavior; do not expose internal seam
only to make tests convenient.
