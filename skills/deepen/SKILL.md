---
name: deepen
description: Use when the user explicitly asks for a deeper task or a higher standard of inquiry without expanding its scope, before planning or execution.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: original, invocation: user, status: dogfood }
---

# Deepen

Raise the method and evidence standard while holding the task's scope fixed. This is task reframing, not execution or an expert persona.

## Procedure

1. Identify the task's objective, deliverable, constraints, and budget from the conversation. Preserve them. If no task is available, ask for it and stop.
2. Give four short, task-specific answers:
   - **Expert practice:** what consequential step would a practitioner take that the current request omits? Explain which uncertainty it resolves; avoid prestige claims and imagined consensus.
   - **Primary material:** name the least-processed useful inputs they would inspect instead of summaries, and where those inputs can be obtained. Rawer is useful only when it improves the decision.
   - **Methods and tools:** name concrete methods and tools, why they fit, and any required access. Distinguish verified availability from proposed access; never invent sources or capabilities.
   - **Independent evidence:** name an observable test, external record, or outcome that could establish correctness, plus what would falsify the result. Another model agreeing is not independent evidence. For judgment tasks without a definitive test, state the limit and the strongest available check.
3. Rewrite the user's prompt in one copyable fenced block. Include the four improvements, preserve the original objective and constraints, and make unavailable inputs or tools explicit prerequisites rather than assumed capabilities. Choose the smallest sufficient method; do not add new deliverables or promise an expanded investigation.
4. Stop after the rewritten prompt. The user decides whether to execute it. If the original task already meets the standard, say so and keep the rewrite minimal.

## Source

Original procedure inspired by Felix Rieseberg's [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/), specifically the depth prompt. Opt-in dogfood skill; behavioral validation is pending.
