---
name: prototype
description: Use when a design question needs a throwaway artifact to answer - whether a state model or logic feels right, or what an interface should look like.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Prototype

A prototype is throwaway code that answers a question. The question decides the shape: a logic question gets a runnable demo that pushes the state model through hard-to-reason cases and surfaces full state after every action; an interface question gets several radically different variations, switchable in one place. If the question is ambiguous and the user is unreachable, match the surrounding code (backend module: logic; page or component: interface) and state the assumption at the top of the prototype.

## Rules

1. Throwaway from day one, marked as such. Place it near the code it prototypes for; name it so a casual reader sees prototype, not production. Follow existing project conventions; invent no new top-level structure.
2. Trivial to run: one command in the project's task runner, or a single file the user opens directly.
3. No persistence by default. State lives in memory; persistence is what the prototype checks, not what it depends on. If the question involves a database, use a scratch target with a clear wipe-me name.
4. Skip polish. No tests, no abstractions, no error handling beyond runnable.
5. Surface the state. After every action or variant switch, show the full relevant state so the user sees what changed.
6. Keep the logic under test in a pure module - no page, DOM, or handler coupling. The page is a thin shell over it, so the validated logic lifts into the real codebase.
7. Capture when done. Fold the validated decision into real code; keep the prototype off the main branch with a pointer from the tracking artifact; record the verdict and the question it settled in the shape of [NOTE.md](NOTE.md) - even when the prototype is abandoned, the note is the value. The main branch keeps only the validated decision.
