# Skill Authoring

This is the skill-specific branch of [writing-for-agents](SKILL.md): what changes when the document is a skill rather than a general agent-facing document.

## Red-Green Validation

Create and edit skills with the same red-green discipline used for code:

1. Write or update the pressure scenario first.
2. Run the scenario without the new skill guidance and record the baseline failure or rationalization.
3. Add the smallest wording that fixes the observed failure.
4. Re-run the scenario until the behavior holds under pressure.

If you did not watch the baseline fail, you do not know whether the skill teaches the right behavior.

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

## Router Skills

When the number of user-invoked skills grows past easy recall, create one router skill that names the others and states when to reach for each. The router lowers human indexing cost without forcing every downstream skill into autonomous discovery.
