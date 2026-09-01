---
name: writing-for-agents
description: Use when creating or editing skills, always-on agent instructions, or pointed reference files that agents must read predictably.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Writing For Agents

Reference for writing any document an agent consumes: a skill, an instructions file, or a document reached through a pointer. The packaging differs; the writing does not. Shape the agent's process, not one canned output.

When the document is a skill, read [SKILL-AUTHORING.md](SKILL-AUTHORING.md) for frontmatter, discovery, and red-green validation.

## Context Pointers

A context pointer is text already in context that names out-of-context material and encodes when to reach it. A skill description is one. A line in `AGENTS.md` that points to `GLOSSARY.md`, `STATUS.md`, or another reference is the same object. The pointer wording, not the target, decides when the agent loads the material - and how reliably.

A good pointer does two jobs:

- state what the material is
- list the distinct branches that should trigger it

Every always-loaded pointer costs tokens on every turn, so prune them harder than the body:

- front-load the leading word that should trigger the lookup
- keep one trigger per real branch
- cut identity the target document already carries

## The Two Loads

Every document and pointer spends one of two budgets:

- Context load: always-loaded material in the working window, such as an instructions line or skill description.
- Cognitive load: the human effort of knowing which documents exist and when they matter.

Material reached only through a pointer escapes most context load but still spends the pointer line. Material with no pointer spends only cognitive load.

## Information Hierarchy

Documents are built from steps and reference. The core decision is where each piece sits on the hierarchy:

1. In-file step: the primary ordered actions.
2. In-file reference: definitions, rules, and facts consulted on demand.
3. Disclosed reference: separate files reached by pointer only when needed.

Push too little down and the top bloats. Push too much down and you hide material the agent actually needs. Use progressive disclosure to keep every branch carrying only the reference it needs.

Co-locate definitions, rules, and caveats for the same concept under one heading. Split only when the cut earns its own load.

## Steps And Completion Criteria

Every step ends on a completion criterion: the condition that tells the agent the work is done. Strong criteria are both checkable and exhaustive.

- Clarity prevents premature completion. Sharpen the bound before splitting the sequence.
- Demand sets how much legwork the agent must do. "Every changed rule accounted for" is stronger than "summarize changes."

If later visible steps tempt the agent to rush the current one, split by sequence so the later steps leave view at a real handoff boundary.

## Leading Words

A leading word is a compact concept the model already thinks with, reused as a token so it anchors a whole behavior region. Prefer existing terms with strong priors over invented jargon. Repeating one sharp word is cheaper and more reliable than restating the same idea in full sentences.

Negation is the nearby failure mode. Do not steer mainly with prohibition when a positive target will do. State the wanted behavior so attention lands there first.

## Pruning

- Keep each meaning in one source of truth.
- Let the environment hold cheap lookups such as scripts, config, and directory layout unless the lookup is expensive or the reason behind it is not visible.
- Check every line for present relevance, not just historical truth.
- Delete sentence-level no-ops that do not change behavior from the default.
