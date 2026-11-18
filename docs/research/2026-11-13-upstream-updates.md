# Upstream updates

Retrieved 2026-11-13, 08:03-08:07 UTC through live GitHub API; commander spot-checks followed. Source facts below have high confidence. Recommendations are judgment; no upstream code was executed or behavior benchmarked.

## Question and scope

What changed in obra/superpowers and mattpocock/skills since this repository's pinned sources, and what merits selective curation? Current means live default-branch HEAD and latest published release, not search-index freshness. Both pinned commits resolve and precede their recorded August 31 retrieval date.

## Current versions

| Source | Pinned commit | Current main | Latest release |
|---|---|---|---|
| obra/superpowers | b36e0829c6d0140e93cfef2ca599b1b07d4a7797, v6.3.0 | 22f0b463e7a5e579904dd6211a520321035526f7, November 3 | [v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2), November 3 |
| mattpocock/skills | 6654f6b60cd9d5be8b54c6fafe44346dabeb3b76 | 5863806dd4e15c63174bee4e7515a4256792ecfa, November 12 | [v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2), October 29; main has subsequent changes |

Exact comparisons: [Superpowers](https://github.com/obra/superpowers/compare/b36e0829c6d0140e93cfef2ca599b1b07d4a7797...22f0b463e7a5e579904dd6211a520321035526f7), [Matt Pocock](https://github.com/mattpocock/skills/compare/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76...5863806dd4e15c63174bee4e7515a4256792ecfa).

## Superpowers

- **Native execution:** inline plan execution with persistent ledger and final independent review replaces periodic checkpoints in `executing-plans`. [September 19 source](https://github.com/obra/superpowers/commit/5bf4e78011075bcfc0dc295f0724994cd123ee71). Recommendation: evaluate only as an opt-in; do not replace this repository's fresh-worker/per-task-review default on unreplicated cost claims.
- **Leaner plans and Review Focus:** exact interfaces, assertions and verification commands instead of routine implementation bodies; implied input/failure cases must be connected to task tests. [September 25 source](https://github.com/obra/superpowers/commit/8ca22dba9a94f28898bbce59f2537ff4d87c747d), [current planning procedure](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md). Recommendation: curate coverage and proportion checks into `plan`.
- **Brainstorming retuned:** inspect context, establish motivation, ask build-changing questions, recommend concrete choices, and bind approval to the actual design. [v7.0.0](https://github.com/obra/superpowers/commit/bb92a77741419a4ab5f06e711a283343f1ada0c3), [v7.0.1](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b). Recommendation: borrow question-quality rules while preserving `grill`'s bounded path.
- **Skill layout and helper hardening:** conditional procedures move to explicitly loaded references; entrypoint-size and installed-layout tests; repository-aware helpers; task IDs and unclosed fences handled more carefully. [v7.0.1](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b), [v7.0.2](https://github.com/obra/superpowers/commit/22f0b463e7a5e579904dd6211a520321035526f7). Recommendation: use these as acceptance cases where equivalent tooling exists, not a reason to import the helper suite.
- **Verification/privacy:** explicit project-suite verification and unrelated-failure disclosure, secret-safe debugging examples, development prompts outside installed skills, and transcript-grounded session diagnosis with approval/redaction boundaries. [Current TDD](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md), [session diagnosis](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md). Recommendation: audit local equivalents; defer the specialized diagnosis workflow.

## Matt Pocock

- **Wizard correctness fixes:** EOF handling, Readline editing, quoted environment values, restrictive initial permissions, symlink/existing-mode preservation, visible opener failures, terminal-clear fallback and function-wrapped stages. [October 6](https://github.com/mattpocock/skills/commit/868c4cf20cb7e08bc805c388ff1f305dbedd261a), [October 9](https://github.com/mattpocock/skills/commit/49dd158d1076134a641b33efb035946536778336). Highest-priority candidate: local template retains older behavior. Validate shell and dotenv consumers separately rather than assuming quoting is portable.
- **Verification improvements:** prove a forced mutation landed before accepting the failing test; explain what proposed TDD seams catch and miss. [Diagnosis](https://github.com/mattpocock/skills/commit/f3fc5632f401156837ee3872f14fe33ccf1024ea), [TDD](https://github.com/mattpocock/skills/commit/3f599139104dfceabc7754eeb91319802f85e042). Recommendation: selective additions to existing procedures.
- **Router reads the selected skill before claiming its behavior or skipping steps.** [October 6](https://github.com/mattpocock/skills/commit/954ee7fd7f1911b79bfa82589b4d35ab6c4b13b8). Recommendation: consider this explicit boundary in `choose-skill`.
- **PR, retro and implement-spec graduate into engineering.** [September 24](https://github.com/mattpocock/skills/commit/a7d038f6bf7f01b516408e95e2fb56e0b338fa6f), [implement-spec](https://github.com/mattpocock/skills/commit/24f41cc26d34ffd688e9105b43798a4b446e267d). Recommendation: reconsider retro's experimental exclusion; fold useful PR evidence/reversibility checks into existing skills rather than add overlap. Preserve applicable Humanlayer attribution if copying PR visuals.
- **Fresh-context workers and fresh implementer per ticket.** [October 29](https://github.com/mattpocock/skills/commit/7739eaed7f8f3915437a8def198a6d0d7206dbc7), [per-ticket implementers](https://github.com/mattpocock/skills/commit/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa). Already overlaps local `implement`; no duplicate port needed.
- **Glossary rename merged; merge-conflict skill retired.** [Rename](https://github.com/mattpocock/skills/commit/e484a8095543718ced436b9b49a8160ed4554000), [retirement](https://github.com/mattpocock/skills/commit/daa01d8aa68ad5c61b68970ec2018d0ce9567be6). Update stale provenance wording during curation; upstream retirement alone does not justify deleting local safeguards.
- **Experimental orchestration evolves:** shared dated/commit-cited memory in chief-of-staff, bounded automation and review/deduplication questions in software-factory. [Chief-of-staff](https://github.com/mattpocock/skills/commit/5ae481693d13b37d4d2c2c92d0b66d299c93e695), [software-factory](https://github.com/mattpocock/skills/commit/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d). Keep deferred; broader than this portable catalog.

## Decision and validation

Prioritize wizard regression tests and fixes, then planning failure-case coverage and small diagnosis/TDD/router improvements. Evaluate execution-mode changes independently. Do not wholesale-sync or advance source pins before curation and verification.

Open questions: which wizard consumers must parse generated environment files; whether Native execution improves this repository's workload without weakening review; which installation safeguards are already covered locally. Performance and universal harness truncation claims remain unverified.

Evidence: independent repository research used GitHub API and source diffs. Commander rechecked Matt Pocock HEAD and the October 6 wizard patch, plus Superpowers latest release/HEAD and current planning Review Focus guidance. No fetched code executed. Cross-agent memory index was absent. No skills, configuration or pins changed; this brief is the only intended repository addition.
