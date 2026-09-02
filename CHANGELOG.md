# Changelog

## Unreleased

## 0.3.0 - 2026-09-02

- `review` gains two cribs from a side-by-side of the harness-native reviewers (Claude Code bundled `code-review` 2.1.258, Codex 0.149.0 `review` rubric) and the two upstream pins: a ref-resolves and non-empty-diff precheck (mattpocock), and a finding-admissibility step (Codex: affected code plus triggering input named, author would fix it, no padding; pre-existing defects in a touched function in scope and labelled). Two more were drafted and rejected on a held baseline: Claude's three finder angles and mattpocock's spec axis. Provenance rows added for the two harness sources. Red-green: `.scratch/pressure-test/run6.sh` / `results8.txt`, `results8b.txt`.

- Ceremony edges, from the 2026-09-02 comparison against the upstream pins and issue #1: `implement` names the `worktrees`, `tdd`, `review`, and `finish` skills at the points it reaches them (the bare phrase "using TDD" never fired the skill); `review` gains an executed mutation check for every new defensive branch; `plan` gains `TEMPLATE.md` (spec path in the header, Global Constraints block, commit step per task) and an explicit hand-off to `implement` or `parallel-execution`; `grill` classifies the path aloud (spike, bounded, architectural) with the artifact scaling and the approval gate fixed, and hands off by path to `prototype`, `implement`, or `to-spec`; `choose-skill` routes any starting feature to `grill`. Every delta red-green tested (`docs/migration/pressure-test/run5.sh`, `run5b.sh`, `results7.txt`, `results7b.txt`): all four differentiated, the bounded-ask grill cell held in both arms and the architectural-ask cell differentiated.

- Added `measurement-standards` (core pack): earn belief in a number before it decides anything - condition tracing, both instrument controls, comparison isolation, re-run before generalizing, best-of-N selection-bias floor, and six untrustworthy-provenance shapes. Original curation from the maintainer's private harness (MIT, no pinned upstream); pressure evidence in `docs/migration/pressure-test/results4.txt`. Catalog is now 30 skills.

- Ported `to-spec` (delivery pack): conversation-to-spec synthesis without re-interviewing - seam sketch confirmed with the user, full spec template, no-file-paths rule with the prototype-snippet exception. Closes the audit's orphaned-wrapper finding; catalog is now 29 skills.

- Rewrote 18 procedure-summary skill descriptions trigger-oriented ("Use when..." with symptoms and keywords) so agent-invoked discovery works without a router or bootstrap, per the catalog's own SKILL-AUTHORING rule.
- Named `GLOSSARY.md` as `domain-model`'s default output and wired `to-tickets` and `triage` to consume it and flag architecture-decision conflicts.
- Documented the tracker pack's zero-setup default (committed local Markdown tickets in `.agents/tickets/`, no config file needed); hosted backends are a power-user opt-in via `.agents/tracker.md` only.
- Renamed `docs/{plans,specs}` to `docs/{plans,specs}` - the directory convention is generic, not brand-named.

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
