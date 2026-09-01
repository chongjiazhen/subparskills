---
name: to-spec
description: Use when a design conversation has settled enough to write down - synthesize the discussion into a spec without re-interviewing, before planning or ticketing starts.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge, invocation: user }
---

# To Spec

Turn the current conversation and codebase understanding into a spec. Do not interview the user - the questions were grill's job; this is synthesis of what is already discussed. A gap too large to synthesize past goes back to `grill`, not into a guess.

## Procedure

1. Explore the repository state if you have not already. Use `GLOSSARY.md` vocabulary throughout, and respect recorded architecture decisions in the touched area.
2. Sketch the seams where the work will be tested. Prefer existing seams; propose new ones at the highest point possible - the fewer seams, the better, and the ideal number is one. Confirm the seams with the user before writing.
3. Write the spec with these sections: Problem Statement and Solution (both from the user's perspective); User Stories (numbered, "As an actor, I want a feature, so that benefit", covering every aspect); Implementation Decisions; Testing Decisions (external behavior only, which modules, prior art in the codebase); Out of Scope; Further Notes.
4. Record decisions as interfaces and behavior, never file paths or code snippets - they go stale fast. Exception: a prototype snippet that encodes a decision more precisely than prose (state machine, schema, type shape) - inline the decision-rich part and note its origin.
5. Hand the spec to `plan` or `to-tickets`, or store it where the project keeps specs. When the tracker pack is in use, publish it `ready-for-agent`.
