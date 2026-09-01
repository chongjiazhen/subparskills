# Changelog

## Unreleased

- Rigor audit vs upstream pins (`docs/migration/rigor-audit-2026-09-01.md`): reinstated the pressure-resistance and authorization gates the merge had stripped - rationalization/red-flag content (`tdd/PRESSURE.md`, diagnose and verify rules), grill's confirm-before-acting gate and exhaustive stop bar, mandatory per-task review and ledger discipline in `implement`, review round cap with no silent discards, worker status contract in `parallel-execution`, redact-secrets in `handoff` and `diagnose`, worktree gitignore check, base-branch confirmation in `finish`, cross-task interface consistency in `plan`, ticket durability and triage verification in the tracker pack, and matching-form-to-failure plus reference mechanics in `writing-for-agents`. Corrected two provenance rows (`brainstorming`, `to-spec`). Red-green revalidation of the reinstated wording is deferred; the wording compresses upstream text that was pressure-tested upstream.

- Ported the remaining promoted upstream capabilities: `wayfinder` (tracker pack), `prototype`, `wizard`, `teach`, and `to-questionnaire` (delivery pack); the catalog now covers the full mattpocock promoted set and the superpowers set, with only experimental and repo-policy capabilities excluded.
- Added public `choose-skill` as the manual router over the portable catalog.
- Added public `writing-for-agents` and `wait-what` productivity skills to the canonical catalog.
- Merged portable skill-authoring guidance into `writing-for-agents` instead of shipping a separate `writing-skills` skill.
- Deepened public `diagnose` and `grill` with pointed reference files so richer rigor stays available without bloating the always-loaded skill body.
- Added `curate-sources.py` and `verify-release.py` to keep upstream curation and release verification explicit, testable, and non-publishing by default.

## 0.2.0 - 2026-08-31

- Clarified the public-to-private overlay boundary for downstream repositories.
- Documented the `v0.2.0` release line for the consolidated canonical catalog.
- Recorded the release date for the Task 2 migration checkpoint.
