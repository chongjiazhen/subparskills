# Provenance

Retrieved 2026-08-31T00:00:00Z. `sources.lock.yml` contains immutable pins: `obra/superpowers` `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`; `mattpocock/skills` `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`. Each upstream capability is represented below. `exclude` means intentionally unavailable in v0.1.0. `wrapper` means command only; `adapter-only` means harness metadata only.

| Source capability | Revision | Decision | Canonical target | Local delta |
| --- | --- | --- | --- | --- |
| obra/superpowers: brainstorming | b36e0829 | merge | grill | Decision interrogation only; no harness gate. |
| obra/superpowers: dispatching-parallel-agents | b36e0829 | merge | parallel-execution | Portable worker contract. |
| obra/superpowers: executing-plans | b36e0829 | merge | implement | Compact task loop. |
| obra/superpowers: finishing-a-development-branch | b36e0829 | merge | finish | No default branch policy. |
| obra/superpowers: receiving-code-review | b36e0829 | merge | review | Consolidated review flow. |
| obra/superpowers: requesting-code-review | b36e0829 | merge | review | Consolidated review flow. |
| obra/superpowers: subagent-driven-development | b36e0829 | merge | parallel-execution | Harness-neutral dispatch. |
| obra/superpowers: systematic-debugging | b36e0829 | merge | diagnose | Feedback-loop-first diagnosis. |
| obra/superpowers: test-driven-development | b36e0829 | merge | tdd | Real-behavior red-green gate. |
| obra/superpowers: using-git-worktrees | b36e0829 | adopt | worktrees | Generic Git only. |
| obra/superpowers: using-superpowers | b36e0829 | exclude | - | Universal bootstrap is not portable. |
| obra/superpowers: verification-before-completion | b36e0829 | adopt | verify | Evidence before claims. |
| obra/superpowers: writing-plans | b36e0829 | merge | plan | No required artifact path. |
| obra/superpowers: writing-skills | b36e0829 | exclude | - | Out of v0.1.0 scope. |
| mattpocock/skills: ask-matt | 6654f6b6 | exclude | - | Persona-specific. |
| mattpocock/skills: code-review | 6654f6b6 | merge | review | One canonical review discipline. |
| mattpocock/skills: codebase-design | 6654f6b6 | merge | deep-modules | Deep-module design. |
| mattpocock/skills: diagnosing-bugs | 6654f6b6 | merge | diagnose | Feedback-loop diagnosis. |
| mattpocock/skills: domain-modeling | 6654f6b6 | merge | domain-model | Portable vocabulary discovery. |
| mattpocock/skills: grill-with-docs | 6654f6b6 | merge | grill | No artifact prescription. |
| mattpocock/skills: implement | 6654f6b6 | merge | implement | TDD-managed execution. |
| mattpocock/skills: improve-codebase-architecture | 6654f6b6 | merge | architecture-improvement | Scoped deepening scan. |
| mattpocock/skills: prototype | 6654f6b6 | exclude | - | UI-specific, deferred. |
| mattpocock/skills: research | 6654f6b6 | exclude | - | Source-specific research workflow deferred. |
| mattpocock/skills: resolving-merge-conflicts | 6654f6b6 | exclude | - | Narrow Git workflow deferred. |
| mattpocock/skills: setup-matt-pocock-skills | 6654f6b6 | adapter-only | adapters | Replaced by native discovery manifests. |
| mattpocock/skills: tdd | 6654f6b6 | merge | tdd | Real-behavior red-green gate. |
| mattpocock/skills: to-spec | 6654f6b6 | wrapper | commands/plan.md | Explicit plan entry point. |
| mattpocock/skills: to-tickets | 6654f6b6 | exclude | - | Tracker integration deferred. |
| mattpocock/skills: triage | 6654f6b6 | exclude | - | Issue-tracker workflow deferred. |
| mattpocock/skills: wayfinder | 6654f6b6 | exclude | - | Exploration-specific workflow deferred. |
| mattpocock/skills: wizard | 6654f6b6 | exclude | - | UI flow-specific workflow deferred. |
| mattpocock/skills: claude-handoff | 6654f6b6 | merge | handoff | Harness-specific wording removed. |
| mattpocock/skills: implement-spec | 6654f6b6 | merge | implement | One execution procedure. |
| mattpocock/skills: loop-me | 6654f6b6 | exclude | - | Experimental upstream capability. |
| mattpocock/skills: retro | 6654f6b6 | exclude | - | Experimental upstream capability. |
| mattpocock/skills: setup-ts-deep-modules | 6654f6b6 | merge | deep-modules | Language-specific setup removed. |
| mattpocock/skills: writing-beats | 6654f6b6 | exclude | - | Experimental upstream capability. |
| mattpocock/skills: writing-fragments | 6654f6b6 | exclude | - | Experimental upstream capability. |
| mattpocock/skills: writing-shape | 6654f6b6 | exclude | - | Experimental upstream capability. |
| mattpocock/skills: git-guardrails-claude-code | 6654f6b6 | adapter-only | adapters/claude-code | Harness policy stays adapter-local. |
| mattpocock/skills: migrate-to-shoehorn | 6654f6b6 | exclude | - | Migration-specific workflow deferred. |
| mattpocock/skills: scaffold-exercises | 6654f6b6 | exclude | - | Teaching tooling deferred. |
| mattpocock/skills: setup-pre-commit | 6654f6b6 | exclude | - | Repository policy, not skill discipline. |
| mattpocock/skills: grill-me | 6654f6b6 | merge | grill | One decision procedure. |
| mattpocock/skills: grilling | 6654f6b6 | merge | grill | One decision procedure. |
| mattpocock/skills: handoff | 6654f6b6 | adopt | handoff | Portable structured handoff. |
| mattpocock/skills: teach | 6654f6b6 | exclude | - | Learning workflow deferred. |
| mattpocock/skills: to-questionnaire | 6654f6b6 | exclude | - | Questionnaire workflow deferred. |
| mattpocock/skills: wait-what | 6654f6b6 | exclude | - | Prompt-only capability deferred. |
| mattpocock/skills: writing-for-agents | 6654f6b6 | exclude | - | Writing workflow deferred. |
