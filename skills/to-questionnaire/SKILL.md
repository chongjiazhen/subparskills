---
name: to-questionnaire
description: Use when a decision needs knowledge someone else holds - turn the gap into a Markdown questionnaire the user hands off to fill in async.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge, invocation: user }
---

# To Questionnaire

The recipient holds knowledge the user lacks; the questionnaire pulls it out. Interview the user only about the send - which they can always answer - never about the subject itself.

## Procedure

1. Who is it going to? One exchange: recipient's role, expertise, relationship. This fixes tone and how much context the document carries.
2. What do you need back? One exchange: the specific decisions or facts the user cannot resolve alone. Done when you have a concrete list of what the user must walk away able to decide.
3. Write it. Questions target the gap between what the recipient knows and what the user needs, most-important-first (async may get one pass), grouped by theme past a handful. Save as `to-questionnaire-<slug>.md` in the current directory and report the path. Done when every item from step 2 is covered by a question.

## Document structure

- Purpose, from/to, and how answers will be used, up top.
- One orienting context paragraph - enough to answer well, not a page.
- How to answer: deadline, rough effort, and that partial answers and "I don't know" beat skipped questions.
- One idea per question, never compound, with an answer stub beneath and a one-line why-this-matters only where the question could be misread or invite a throwaway answer.
- Closing catch-all: anything we did not ask that we should know?
