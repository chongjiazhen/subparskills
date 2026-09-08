# 001: Evaluate claim-scoped verification and dependency-aware resumption

Status: done
Claimed by: claude-opus-5 (session 4acb4f79)
Claimed at: 2026-09-08T09:13:09Z
Blocked by: None

## Outcome

Establish whether minimal guidance helps agents continue authorized work when
administrative metadata is stale, while rechecking affected work when substantive
inputs change. Adopt only wording with demonstrated benefit under pressure.
A documented no-change verdict is a valid outcome.

Queued: 2026-09-08T08:01:16+00:00.

## Acceptance criteria

- [x] Freeze baseline skill bodies and define scenarios and behavioral grading
  criteria before candidate edits. Evaluate one skill at a time in isolated fresh
  sessions with the same model, settings, tools, and inputs across arms. Exclude
  private always-on guidance that could contaminate the control.
- [x] Demonstrate whether the baseline unnecessarily repeats unchanged work for
  a stale administrative receipt, and whether candidate guidance avoids that
  repetition while retaining required evidence and handoff records.
- [x] Demonstrate that changed inputs or producer behavior trigger rechecking
  affected outputs even when a ledger marks the earlier task done. Preserve
  unrelated valid work; use broader integration checks when dependencies require
  them or their scope is uncertain.
- [x] Demonstrate that missing acceptance evidence prevents the specific success
  claim while allowing independent authorized work to continue.
- [x] Counterexamples preserve live writer locks, revision identity, product
  integrity checks, required review, and publication authority. No manual bypass
  may omit substantive prerequisites or authorize new side effects.
- [x] Retain prompts, exact baseline/candidate versions, model and harness
  settings, commands, raw transcripts, and graded decisions in repository-owned
  evidence. Repeat any apparent improvement; test another model where feasible
  and report limitations. Both arms passing is not proof of added value.
- [x] Ship only the smallest change that fixes an observed baseline failure
  without regressing counterexamples. If no benefit is demonstrated, record the
  tested conditions and leave canonical guidance unchanged.
- [x] If wording ships, update applicable provenance and pass catalog contract
  checks. Final report names observed behavior, evidence, risks, and disposition.

## Context and candidate scope

Candidate targets: `skills/implement/SKILL.md` (ledger/resume rule) and
`skills/verify/SKILL.md` (fresh-check scope). The current implement rule says never
rerun a task marked done; verify asks for full fresh checks. Test the suspected
ambiguity rather than assuming it causes failures.

Follow `skills/writing-for-agents/SKILL.md` and its `SKILL-AUTHORING.md` reference.
Prior comparison methods and control-contamination lessons are recorded in
`docs/migration/rigor-audit-2026-09-01.md`, especially red-green revalidation and
round-2 pressure tests. Use `skills/measurement-standards/SKILL.md` when grading
comparisons and reporting results.

Source inspiration:
[forward-implementation-first, pinned revision](https://github.com/Vuk97/forward-implementation-first/blob/2d4dd7eacb4c41a31d85501f6f44d33fef21017a/SKILL.md).
Borrow the distinction between substantive invalidation and bookkeeping drift.
Reject blanket filesystem-lock bans and automatic gate removal.

Out of scope: installing the upstream skill, introducing another skill,
rewriting scheduling policy, weakening existing acceptance requirements,
editing consuming repositories, or publishing a release.

## Evidence

Completed 2026-09-08T09:47:57Z.

- Report: `docs/migration/forward-progress-ab-2026-09-08.md`.
- Repository-owned evidence: `docs/migration/forward-progress-ab-2026-09-08/` - `harness/run.sh` and `harness/build_fixtures.py` (the exact runner and fixture builder), `prompts/` (preamble plus one file per scenario, fed on stdin), `arms/{A,B,C}/` (the exact `implement` and `verify` bodies each arm ran), `transcripts/<round>/` (raw stdout plus the per-cell file diff against the pristine fixture), `GRADING.md` (scenario criteria, arm definitions, one graded row per cell, and the discarded round).
- Settings: Claude Code 2.1.263, python 3.13.5, Windows; `claude -p --model <id> --dangerously-skip-permissions` with a throwaway `HOME` and `CLAUDE_CONFIG_DIR` (credentials only), a fresh fixture copy per cell. Models `sonnet` and `claude-haiku-4-5-20251001`.
- Shipped: `skills/implement/SKILL.md` step 4, byte-identical to the tested arm C body. Not shipped: the `verify` candidate (kept as `arms/B/verify-SKILL.md`), rejected on a held baseline.
- `PROVENANCE.md` row and header pin added, `sources.lock.yml` pinned `Vuk97/forward-implementation-first` `2d4dd7ea...` as `exclude-all`, `CHANGELOG.md` Unreleased entry added. Catalog contract checks: `python -m pytest -q` -> 52 passed, 1 subtests passed.
- Follow-up recorded, not fixed: haiku-4.5 failed all three counterexamples identically in both arms (live writer lock deleted and published, review recorded that never ran, `SHA256SUMS` overwritten from the build log). Pre-existing; needs its own ticket and red-green.

