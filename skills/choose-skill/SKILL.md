---
name: choose-skill
description: Use when the next step is unclear and you need to choose which public skill or workflow should start the task.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge, invocation: user }
---

# Choose Skill

Use this when you are unsure which public skill fits. Route first, then invoke the chosen skill. Do not try to run a universal bootstrap or the full lifecycle by default.

## Routing Rules

1. Name the immediate problem, not the whole project.
2. Pick one starting skill whose scope matches that immediate problem.
3. If two skills are close, choose the narrower one and say why the other is not first.
4. Stop after naming the route unless the operator also asked you to execute it.

## Route Map

- Prior explanation did not land: `wait-what`
- Need to write or edit agent-facing docs or skills: `writing-for-agents`
- Work starting on a feature, behavior change, or fix with design room: `grill` (classifies spike, bounded, or architectural, then hands off by path)
- Approved design needs task breakdown: `plan`
- Approved plan needs execution in verified increments: `implement`
- Bug, regression, or incident cause is unclear: `diagnose`
- Feature or bugfix work needs red-green discipline: `tdd`
- Completion, merge, or release claim needs fresh evidence: `verify`
- Need findings on correctness, regressions, or missing tests: `review`
- Need to hand work to another operator with context and evidence: `handoff`
- Need isolated branch ownership or parallel workspaces: `worktrees`
- Independent bounded tasks can run concurrently: `parallel-execution`
- Verified work is ready for integration choices: `finish`
- Domain language, invariants, or bounded concepts are unclear: `domain-model`
- Need module/interface design principles for a focused change: `deep-modules`
- Need to scan for high-value refactor seams in an active area: `architecture-improvement`
- Design question needs a throwaway artifact to answer: `prototype`
- Human-only manual steps need a guided interactive script: `wizard`
- Decision needs knowledge someone else holds, async: `to-questionnaire`
- User wants to learn a topic over multiple sessions: `teach`
- Work too big for one session and the route is foggy: `wayfinder`
