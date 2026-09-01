---
name: grill
description: Surface expensive-to-reverse decisions before implementation starts.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Grill

Surface expensive-to-reverse decisions before implementation starts. Keep the always-loaded path on the live interview; branch to pointed references for decision categories and written-artifact review.

Use [DECISION-TREE.md](DECISION-TREE.md) to choose which branches deserve questions. Use [GAP-REVIEW.md](GAP-REVIEW.md) when the user already has a written proposal and wants holes, not an interview.

## Procedure

1. Read the stated goal and nearby code first. If the terrain is unknown, survey constraints and seams before asking the user for answers the repository can already provide.
2. Identify the costly implicit decisions and ask one branch question at a time.
3. Recommend an answer with a concise reason before asking for confirmation or override.
4. Skip cheap-to-reverse bikesheds unless they block a real branch. Stop when the remaining questions are low leverage or the user is ready to move into implementation.
5. End with confirmed decisions, deferred branches with reasons, and the safest next concrete step.
