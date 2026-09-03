# Skill Authoring

This is the skill-specific branch of [writing-for-agents](SKILL.md): what changes when the document is a skill rather than a general agent-facing document.

## Red-Green Validation

Create and edit skills with the same red-green discipline used for code:

1. Write or update the pressure scenario first.
2. Run the scenario without the new skill guidance and record the baseline failure or rationalization.
3. Add the smallest wording that fixes the observed failure.
4. Re-run the scenario until the behavior holds under pressure.

If you did not watch the baseline fail, you do not know whether the skill teaches the right behavior.

Test shape follows skill type: discipline rule - pressure scenario; technique - apply to a new case plus edge cases; pattern - recognize when it applies plus a counter-example; reference - can it be found, plus a gap check. One skill at a time: test each before starting the next - batch-authoring untested skills is the same violation as batching untested code.

## Matching Form To Failure

Classify the baseline failure before choosing wording:

- Skips a step under pressure: prohibition plus a rationalization table (excuse - reality) and a red-flags self-check naming the workarounds you observed. A bare rule restatement folds under pressure.
- Wrong output shape: a positive recipe. Prohibition here measurably produces more of the unwanted content, not less.
- Omitted element: a required field or slot.
- Conditional behavior: a keyed conditional, never an unconditional rule with exemption clauses - exemptions do not scope.

Wording that must survive pressure reads imperative and immediate, with explicit no-exceptions; soft or deferred phrasing measurably loses compliance.

## Reference Mechanics

Keep every disclosed reference one hop from the entry file - a reference chained through another reference gets partially read. Give any reference file past ~100 lines a table of contents so a partial read still shows scope. Cross-reference another skill by its plain name; some harnesses force-load `@`-style file references immediately, defeating the pointer. File paths use forward slashes even when authored on Windows.

## Discovery And Frontmatter

Every skill needs frontmatter that matches the catalog contract:

- `name`: stable skill identifier, usually the folder name
- `description`: trigger-oriented "Use when..." text that helps the agent decide whether to load the skill
- `license`
- `compatibility`
- `metadata`

Descriptions should describe when to use the skill, not summarize the full procedure. Keep keywords for symptoms, tool names, and failure modes that an agent would search for.

## Invocation

Two choices trade the two loads:

- A discoverable skill keeps a trigger-oriented `description`, so the agent can find it autonomously and other skills can point at it.
- A user-invoked skill relies on the human to remember it, saving context load and spending cognitive load instead.

Choose autonomous discovery only when the agent must reach the skill on its own, or when another skill must be able to point at it.

## Shared Reference

Shared reference used by several discoverable skills can live in one skill-level reference file. Shared reference that should stay outside discovery can live in a plain document such as `GLOSSARY.md`, then any skill or instructions file can point at it without turning it into another skill.

## Guarantees

A guarantee the skill must always uphold - persistence, validation, naming, idempotency - lives in a bundled script the skill runs, never in body prose. Prose like "always write X to Y" or "always validate Z first" is a guarantee mis-housed in wording that drifts; move it into a script step the body calls.

Match specificity to fragility. Many valid paths: text heuristics. A preferred pattern with acceptable variation: parameterized pseudocode. One exact sequence that fails when varied: a fixed script with nothing to negotiate.

A bundled script handles its own errors and justifies every constant; the body says whether the agent runs it or reads it as reference. A batch or destructive operation validates a plan file before executing it. An MCP tool is named `ServerName:tool_name`.

## Before Shipping

A skill is done when every item holds, checked against the file rather than recalled:

- Frontmatter complete per the catalog contract, description trigger-oriented.
- Every dependency the body assumes (a script, a sibling file, a tool) is named and present.
- Every disclosed reference is one hop away and linked relatively.
- No hardcoded per-model, per-run, or per-machine constant in the body.
- The red-green scenario for this edit passed, on more than one model where feasible.

## Router Skills

When the number of user-invoked skills grows past easy recall, create one router skill that names the others and states when to reach for each. The router lowers human indexing cost without forcing every downstream skill into autonomous discovery.
