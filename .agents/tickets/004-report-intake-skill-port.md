# 004: Port the `report` intake skill into the tracker pack

Status: ready-for-agent
Claimed by: -
Claimed at: -
Blocked by: None

## Outcome

One observation - a bug hit mid-task, a freeform idea, a commit ref - becomes
one deduped ticket in the configured tracker backend, filed only after the
user confirms the drafted title and body. Today the catalog has `to-tickets`
(splits approved work) and `triage` (classifies tickets already filed) and no
intake step; ticket 003 on 2026-09-08 was written by hand for lack of one.

Source: the operator's private `report` skill (atelier `skills/report/SKILL.md`,
Claude Code adapter of soluterminal RFC #43). Roughly a third of it is
portable. Port only that: gather from the session, classify to one type and
scope and never file a question, three-axis dedup (symptom, mechanism,
identifier - a sweep on one axis is not coverage), draft in the ticket
schema, confirm gate, file through the configured backend (`gh issue` for
github, `.agents/tickets/` for local). Everything else stays out of the
catalog: default repo and account token, an org-specific triage audience and
its granularity rule, upstream-worthiness by ancestor commit, roadmap rows,
teammate-repo restraint, voice and attribution rules. Those move to the
operator's work layer as a section the catalog skill can be pointed at via
`.agents/tracker.md`.

Queued: 2026-09-08T14:12:00+00:00.

## Acceptance criteria

- [ ] Red-green before the body is written, per `writing-for-agents`
  SKILL-AUTHORING. The scenario under test is the dedup rule: a local
  tracker seeded with an open ticket whose title names the mechanism
  (`unique constraint`, `race`) while the prompt reports the symptom
  (`duplicate rows`, `stale`) under mild time pressure. Baseline is the
  catalog with no intake skill, prompted to file a ticket; record whether it
  finds the near-match. Candidate must find it and propose commenting
  instead of filing. Both recorded misses behind the source rule were
  single-axis sweeps; the fixture reproduces that shape.
- [ ] A second scenario where no near-match exists: the candidate files one
  ticket in the schema, with a specific outcome and observable criteria,
  and only after the confirm gate. A run that files without showing title
  and body first fails.
- [ ] A third scenario where the report is a question, not a defect: the
  candidate does not file.
- [ ] Both tracker backends exercised at least once, or the github backend
  cell explicitly recorded as not run and why.
- [ ] Sonnet primary, a second model where feasible; N=2 per differentiating
  cell; isolated fresh sessions; prompts, bodies, runner, raw transcripts and
  graded decisions retained under `docs/migration/`. The
  `implement-dispatch-ab-2026-09-08/harness/` runner is reusable.
- [ ] No org-specific default, account, repo path, or audience rule in the
  catalog body. PROVENANCE row added for the source with what was excluded.
- [ ] On landing, the operator's private copy is retired the way `diagnose`
  and `grill` were on 2026-09-01 (parked, manifest and setup script
  migration entry), and the excluded parts land in the work layer the same
  batch so nothing is lost between the two. This half is out of the
  catalog's tree but blocks closing the ticket.

## Evidence

