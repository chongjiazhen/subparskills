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
| mattpocock/skills: to-spec | 6654f6b6 | merge | to-spec | Conversation-to-spec synthesis with seam confirmation; tracker publish opt-in, no setup-skill dependency. Ported 2026-09-01 after the audit found the original `wrapper -> commands/plan.md` decision had absorbed no content. |
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
| mattpocock/skills: zoom-out | pre-pin (removed e112a6b0) | exclude | - | Historical capability, deleted upstream before the 6654f6b6 pin with no stated rationale. Excluded 2026-09-01, mirroring the upstream removal; private-layer's adapted copy retired the same day. Recorded so refreshes don't re-litigate. |

2026-09-01: original curation from the maintainer's private harness (MIT, no pinned upstream - nothing to diff on a source refresh), pressure-tested red-green per SKILL-AUTHORING (`docs/migration/pressure-test/run3.sh` / `results3.txt`, isolated config, sonnet, N=1 per cell). Landed: `review` anti-anchoring rule for requesting review of one's own changes (old body leaked the author's diagnosis and framing; new body stayed neutral); `parallel-execution` shared-checkout pathspec-commit step (old body ran a bare `git commit`); SKILL-AUTHORING `Guarantees` section (old body housed always-save/always-validate guarantees in prose; new body routed them through a bundled script). Rejected on a held baseline: a `handoff` reconcile-against-git step (reverted same day - the old body verified against git unprompted at two pressure levels) and candidate one-skill-per-process and codify-on-inconsistency bullets (baseline already chose correctly). Also rejected on held baselines (`results5.txt`): update-not-sibling and evidence-splits-from-principle bullets for `writing-for-agents` Pruning - both arms edited the family rule in place and split incident narrative from the always-loaded rule unprompted, deriving the behavior from the existing single-source, co-location, and Two Loads wording.

2026-09-01: `measurement-standards` added to the core pack - original curation from the maintainer's private harness (MIT, no pinned upstream), converting its measurement-validity discipline: condition tracing, positive and negative instrument controls, comparison isolation, re-run before generalizing, the best-of-N under-null floor, and six untrustworthy-provenance shapes. Pressure evidence (`docs/migration/pressure-test/results4.txt`, isolated config, sonnet, unnamed-skill prompts proving description-routing): the best-of-N cell differentiated on mechanism (green invoked the selection-bias floor; red's round-1 remedy re-ran only the winners, re-conditioning on the max), the sweep cell held in both arms at two pressure levels - same keep-with-caveat standard the rigor audit applied to reinstated gates.

Upstream PR mattpocock/skills#876 (open as of 2026-09-01) renames `CONTEXT.md`/`CONTEXT-MAP.md` to `GLOSSARY.md`/`GLOSSARY-MAP.md` across ten skills. The catalog uses the `GLOSSARY.md` name wherever a vocabulary doc is mentioned (`wait-what`, `writing-for-agents`, and since 2026-09-01 `domain-model` as its default output name, with `to-tickets` and `triage` as consumers), aligned with the PR. Nothing to apply on a future refresh whichever way the PR lands.
