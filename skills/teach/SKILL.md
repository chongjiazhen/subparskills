---
name: teach
description: Use when the user asks to be taught a skill or concept over multiple sessions - runs a stateful teaching workspace in the current directory.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge, invocation: user }
---

# Teach

A stateful request: the user learns the topic over multiple sessions, with state captured in the current directory. Create files lazily, as each earns its place.

## Workspace

- `MISSION.md` - why the user wants this; grounds all teaching. If missing or unclear, questioning the user on it is the first job: without the mission, lessons float abstract and there is no way to judge what comes next. Missions may shift; confirm before updating, and record the change as a learning record.
- `RESOURCES.md` - high-quality external resources found for the topic. Populate this before teaching from it; never trust parametric knowledge alone, and cite resources inside lessons.
- `lessons/NNNN-<dash-case-name>.html` - the unit of teaching: one self-contained page teaching one tightly-scoped thing tied to the mission, short enough to complete quickly, readable enough to revisit. Open it for the user when possible.
- `reference/*.html` - the compressed essence of lessons, built for quick lookup: syntax sheets, algorithms, routines, and above all a glossary, which every later lesson adheres to. Lessons are rarely revisited; reference documents are.
- `learning-records/NNNN-<dash-case-name>.md` - what the user actually learned: non-obvious lessons and key insights, used to place the next session.
- `assets/*` - components shared across lessons (stylesheet first, then quiz widgets, simulators). Read it before authoring a lesson; reuse is the default, and anything a second lesson could use goes here, never inlined.
- `NOTES.md` - the user's teaching preferences and working notes.

## Method

- Pick each lesson from the zone of proximal development: challenged just enough, judged from the learning records and the mission, unless the user names the topic.
- Split knowledge from skills. Knowledge is acquired from trusted resources, and difficulty there is the enemy - keep working memory free for understanding. Skills make it stick, and difficulty there is the tool: retrieval practice, spacing, and interleaving build storage strength over the illusory fluency of in-the-moment recall.
- Every skill exercise runs on the tightest feedback loop available - immediate, ideally automatic. Quiz answer options carry no formatting clues (same length where possible).
- Wisdom comes from real-world interaction. When a question needs it, answer, then point at a high-reputation community where the user can test the skill - respecting a stated preference not to join one.
