# Provenance

Retrieved 2026-08-31T00:00:00Z. Pins re-verified at upstream HEAD 2026-09-01 (no drift). `sources.lock.yml` contains immutable pins: `obra/superpowers` `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`; `mattpocock/skills` `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`. Each upstream capability is represented below. `exclude` means intentionally unavailable in v0.1.0. `wrapper` means command only; `adapter-only` means harness metadata only.

| Source capability | Revision | Decision | Canonical target | Local delta |
| --- | --- | --- | --- | --- |
| obra/superpowers: brainstorming | b36e0829 | merge | grill | Decision interrogation only; no harness gate. 2026-09-01 audit: upstream's confirm-before-acting approval gate had not landed; restored to grill step 5. |
| obra/superpowers: dispatching-parallel-agents | b36e0829 | merge | parallel-execution | Portable worker contract. |
| obra/superpowers: executing-plans | b36e0829 | merge | implement | Compact task loop. |
| obra/superpowers: finishing-a-development-branch | b36e0829 | merge | finish | No default branch policy. |
| obra/superpowers: receiving-code-review | b36e0829 | merge | review | Consolidated review flow. |
| obra/superpowers: requesting-code-review | b36e0829 | merge | review | Consolidated review flow. |
| obra/superpowers: subagent-driven-development | b36e0829 | merge | parallel-execution | Harness-neutral dispatch. |
| obra/superpowers: systematic-debugging | b36e0829 | merge | diagnose | Feedback-loop-first diagnosis. |
| obra/superpowers: test-driven-development | b36e0829 | merge | tdd | Real-behavior red-green gate. |
| obra/superpowers: using-git-worktrees | b36e0829 | adopt | worktrees | Generic Git only. |
| obra/superpowers: using-superpowers | b36e0829 | merge | choose-skill | Stripped to manual routing over public skills; no universal bootstrap. |
| obra/superpowers: verification-before-completion | b36e0829 | adopt | verify | Evidence before claims. |
| obra/superpowers: writing-plans | b36e0829 | merge | plan | No required artifact path. |
| obra/superpowers: writing-skills | b36e0829 | merge | writing-for-agents | Folded portable skill-authoring guidance into the public writing discipline. |
| mattpocock/skills: ask-matt | 6654f6b6 | merge | choose-skill | Public router over the portable catalog only. |
| mattpocock/skills: code-review | 6654f6b6 | merge | review | One canonical review discipline. |
| mattpocock/skills: codebase-design | 6654f6b6 | merge | deep-modules | Deep-module design. |
| mattpocock/skills: diagnosing-bugs | 6654f6b6 | merge | diagnose | Feedback-loop diagnosis. |
| mattpocock/skills: domain-modeling | 6654f6b6 | merge | domain-model | Portable vocabulary discovery. |
| mattpocock/skills: grill-with-docs | 6654f6b6 | merge | grill | No artifact prescription. |
| mattpocock/skills: implement | 6654f6b6 | merge | implement | TDD-managed execution. |
| mattpocock/skills: improve-codebase-architecture | 6654f6b6 | merge | architecture-improvement | Scoped deepening scan. |
| mattpocock/skills: prototype | 6654f6b6 | merge | prototype | Throwaway question-answering artifact; UI-stack specifics dropped. |
| mattpocock/skills: research | 6654f6b6 | merge | research | Primary-source evidence, direct citations, and decision-ready findings; no required background agent or artifact path. |
| mattpocock/skills: resolving-merge-conflicts | 6654f6b6 | merge | merge-conflicts | Intent-first resolution, checks before continuation, explicit authorization before abandon. |
| mattpocock/skills: setup-matt-pocock-skills | 6654f6b6 | adapter-only | adapters | Replaced by native discovery manifests. |
| mattpocock/skills: tdd | 6654f6b6 | merge | tdd | Real-behavior red-green gate. |
| mattpocock/skills: to-spec | 6654f6b6 | wrapper | commands/plan.md | Explicit plan entry point. 2026-09-01 audit: wrapper had absorbed no content; seam-minimization rule folded into `plan` step 2. Conversation-to-spec synthesis remains unported. |
| mattpocock/skills: to-tickets | 6654f6b6 | merge | to-tickets | GitHub tracker backend is opt-in; local Markdown remains default. |
| mattpocock/skills: triage | 6654f6b6 | merge | triage | GitHub tracker backend is opt-in; local Markdown remains default. |
| mattpocock/skills: wayfinder | 6654f6b6 | merge | wayfinder | Backend-neutral decision-ticket mapping over the tracker pack. |
| mattpocock/skills: wizard | 6654f6b6 | merge | wizard | Human-only manual procedures; template library vendored verbatim. |
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
| mattpocock/skills: teach | 6654f6b6 | merge | teach | Stateful teaching workspace; lazy file creation. |
| mattpocock/skills: to-questionnaire | 6654f6b6 | merge | to-questionnaire | Grill the send, not the subject; portable Markdown handoff. |
| mattpocock/skills: wait-what | 6654f6b6 | adopt | wait-what | Portable re-pitch prompt with glossary-aware wording. |
| mattpocock/skills: writing-for-agents | 6654f6b6 | merge | writing-for-agents | Portable agent-document guidance plus merged skill-authoring reference. |

Upstream PR mattpocock/skills#876 (open as of 2026-09-01) renames `CONTEXT.md`/`CONTEXT-MAP.md` to `GLOSSARY.md`/`GLOSSARY-MAP.md` across ten skills. The catalog already uses the `GLOSSARY.md` name where a vocabulary doc is mentioned (`wait-what`, `writing-for-agents`), aligned with the PR; `domain-model` prescribes no filename ("No artifact prescription"). Nothing to apply on a future refresh whichever way the PR lands.
