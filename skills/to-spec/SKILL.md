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
3. Write the spec with these sections: Problem Statement and Solution (both from the user's perspective); User Stories (numbered, "As an actor, I want a feature, so that benefit", covering every aspect, each with an Independent Test - the observable check that proves this story alone); Implementation Decisions; Testing Decisions (external behavior only, which modules, prior art in the codebase); Out of Scope; Further Notes.
4. Mark what the discussion left open instead of guessing: write `[NEEDS CLARIFICATION: <question>]` inline at the sentence it blocks. A quality word (fast, secure, scalable, robust, intuitive) carries a measurable criterion or a marker. Three or more markers means the design has not settled - return to `grill` with the list rather than writing around it.
5. Record decisions as interfaces and behavior. The test for a line belonging in the spec: the implementation cannot change without changing what it describes. Inline a code snippet only where it encodes a decision more precisely than prose (a state machine, schema, or type shape); inline the decision-rich part and note its origin. Leave out file paths and illustrative code - they go stale fast.
6. Self-review before handoff: read the sections against each other for contradiction, and check the spec still describes one plan's worth of work - split into sub-specs when it does not. Fix inline.
7. Hand the spec to `plan` or `to-tickets`, or store it where the project keeps specs. When the tracker pack is in use, publish it `ready-for-agent`.
