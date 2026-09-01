# Codex and Claude Migration Smoke Test

Created: 2026-09-01T01:55:18.7273035Z

Run this once per target repository after installing Subparskills and before removing stock skill sets. Use two separate disposable branches or worktrees. Do not remove stock skills during this test.

## Fresh session

Start a fresh Codex session and a fresh Claude Code session in separate test worktrees. Record harness version, repository commit, install command, install path, selected packs, and stock installs still present.

## Skill discovery

Confirm each harness discovers selected canonical IDs and no duplicate stock IDs. Record visible skill list or screenshot. Required core IDs: `diagnose`, `tdd`, `verify`, `review`.

## Bug diagnosis prompt

Use a reproducible bug prompt. Confirm `diagnose` builds a symptom-specific feedback loop before proposing a fix. Record prompt, selected skill, loop command, and observed result.

## Feature delivery prompt

Use a bounded feature prompt. Confirm selected delivery skills establish intent before implementation, use test-first behavior where code changes, and finish with verification. Record prompt, selected skills, tests, and observed result.

## Stock absence

After positive results, remove stock installs only from a disposable test environment, restart both harnesses, and repeat discovery plus both prompts. Record exact removal commands, remaining installed locations, and any duplicate or missing triggers. Restore stock installs if either result is inconclusive.

## Evidence record

| UTC time | Harness | Version | Repository and commit | Packs | Discovery evidence | Diagnosis result | Delivery result | Stock absence result | Operator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |

Cut over one production repository only after both harness rows are complete and no stock-trigger collision remains.
