# 007: Record eli5 and i-have-adhd as excluded neighbors of `wait-what`

Status: ready-for-agent
Claimed by: -
Claimed at: -
Blocked by: None

## Outcome

`PROVENANCE.md` records that two public skills near `wait-what` were scanned
and excluded, so a later source refresh does not rediscover and re-evaluate
them. Housekeeping with no deadline: nothing in the catalog depends on it.

The scan is done. Sources, comparison, verdicts and the two drafted rows are
in `docs/research/2026-11-18-wait-what-adjacent-skills.md`:

- `DreambigOu/ELI5: eli5` at a766623b - audience-calibrated explanation.
  Adjacent to `wait-what`, but swaps project vocabulary for analogy and
  accepts reduced accuracy.
- `ayghri/i-have-adhd: i-have-adhd` at 1ecea199 - session-persistent response
  style for one reader profile. Personal and harness policy, not a portable
  procedure.

Both MIT. No upstream text was copied.

Queued: 2026-11-18T12:44:30+00:00.

## Acceptance criteria

- [ ] The two `exclude` rows from the brief are added to the decision table in
      `PROVENANCE.md`, in the format of the existing
      `ucsandman/claude-skills` exclude row.
- [ ] The brief is committed alongside, since the rows cite its crib
      candidates.
- [ ] `python -m pytest -q` passes after the edit.
- [ ] Out of scope: any change to `skills/wait-what/SKILL.md`. The three crib
      candidates in the brief (purpose before mechanism, first-line/last-line
      check, restated position) are untested; shipping one needs its own
      ticket and a red-green pressure test showing a baseline gap first.

## Evidence
