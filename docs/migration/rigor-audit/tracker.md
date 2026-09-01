# Audit: mattpocock tracker-family skills -> subparskills tracker pack

Scope: to-tickets, triage(+AGENT-BRIEF+OUT-OF-SCOPE), wayfinder, to-spec, setup-matt-pocock-skills(+its 4 seed docs)
vs merged: to-tickets, triage, claim-ticket, wayfinder, work-frontier, tracker/* (backends, state-model,
ticket-schema), plan, and all six commands.

Context checked: PROVENANCE.md and docs/specs/2026-08-31-tracker-pack-design.md record the merge as a
deliberate redesign (not a lossy compression pass), with named deltas. Findings below judge against those deltas
where they exist; anything dropped with NO recorded delta is flagged.

## LOST-LOAD-BEARING

### 1. Agent-brief writing discipline entirely absent (HIGH)
Upstream: `triage/AGENT-BRIEF.md`, referenced from `triage/SKILL.md` step 5 (`ready-for-agent`).
Content: "Durability over precision" (describe interfaces/behavior, never file paths or line numbers - they go
stale before an AFK agent picks the ticket up), "Behavioral, not procedural" (what, not how), "Explicit scope
boundaries" (an `Out of scope` list to stop gold-plating), plus full good/bad worked examples.
Merged: no file in the repo teaches this at all (grepped `durab|file path|line number|stale` across `skills/` -
only hit is unrelated wayfinder prose). `tracker/ticket-schema.md` gives a structural template (Outcome/Acceptance
criteria/Evidence) but never warns against embedding file paths/line numbers or writing procedural steps, and
`to-tickets/SKILL.md` dropped the equivalent line upstream to-tickets carried ("avoid specific file paths or code
snippets: they go stale fast"). Failure mode: agents (both the one filing the ticket and the one filling
`Claimed by`) will naturally write "open src/x.ts line 42" style tickets, which then go stale exactly as upstream
warns, wasting a downstream AFK session that can't find the referenced code.
Reinstatement (terse, fits `ticket-schema.md` as a "Writing outcomes" note): "Outcome/Acceptance criteria: describe
interfaces and behavior, not file paths or line numbers - they go stale before claim. Say what, not how."

### 2. Triage verification-before-decision step dropped (HIGH)
Upstream: `triage/SKILL.md` step 3, "Verify the claim" - reproduce a bug from the reporter's steps, or check out a
PR diff and run it, *before* grilling or deciding a state. "A confirmed verification makes a much stronger agent
brief."
Merged: `triage/SKILL.md` has no verification step at all; it goes straight from "read the ticket" to "choose a
state" to "set ready-for-agent only when adequately specific." Specificity of wording is checked; truth of the
claim never is. Failure mode: a ticket can be marked `ready-for-agent` and handed to an AFK worker on an
unreproduced bug report, burning a full session chasing nothing.
Reinstatement: add a step 2.5 to `triage/SKILL.md`: "Before choosing a state, verify the claim where possible
(reproduce a bug, run/check a proposed diff). Record confirmed/failed/insufficient-detail; insufficient detail is
a `needs-info` signal."

### 3. Redundancy check dropped (MED-HIGH)
Upstream: `triage/SKILL.md` step 1(a) - before triaging, search the codebase by domain concept for an existing
implementation of the request; if found, it's `wontfix` (already implemented), not new work.
Merged: no such check anywhere in `triage/SKILL.md` or `to-tickets/SKILL.md`. Failure mode: duplicate tickets for
already-built behavior, discovered only after an agent starts implementing.
Reinstatement: one line in `triage/SKILL.md` step 2: "Before classifying, check whether the outcome already
exists in the codebase; if so, state `wontfix` (implemented) with the location, not a new ticket."

### 4. Domain glossary / ADR consumer rules have no home (MED)
Upstream: wired into to-tickets step 2, triage step 1, to-spec step 1, and centrally defined in
`setup-matt-pocock-skills/domain.md` ("read CONTEXT.md/CONTEXT-MAP.md and relevant ADRs before exploring," "use
the glossary's vocabulary," "flag ADR conflicts explicitly rather than silently overriding").
Merged: `domain-model/SKILL.md` deliberately "prescribes no filename" (per its own PROVENANCE.md delta), and none
of `to-tickets`, `triage`, `wayfinder`, `work-frontier`, or `claim-ticket` mention consulting domain docs or ADRs
at all (grepped `domain glossary|ADR` across `skills/` - only wayfinder's generic "Notes: domain..." line hits).
Failure mode: a ticket or triage decision can silently contradict a recorded architectural decision with nothing
in the flow prompting a check.
Reinstatement: in `to-tickets/SKILL.md` step 2 and `triage/SKILL.md` step 2, add: "Check project domain docs/ADRs
if present; flag rather than silently override a conflict."

### 5. Wide-refactor / expand-contract exception missing from to-tickets (MED)
Upstream: `to-tickets/SKILL.md`, the `<vertical-slice-rules>` section's "Wide refactors are the exception" block -
explicit guidance to *not* force a mechanical, blast-radius-fanned change (rename a column, retype a shared
symbol) into a tracer-bullet slice, and instead sequence expand -> batched migrate -> contract, each its own
ticket, keeping CI green batch to batch.
Merged: `to-tickets/SKILL.md` step 3 only says "Divide the work into small vertical slices... avoid tickets that
are only layers or implementation phases" - with no exception carved out. Applied literally to a wide refactor,
this rule is actively wrong (it says avoid phased tickets, which is exactly what expand-contract needs).
Failure mode: an agent following the merged rule verbatim either forces an unshippable single slice for a
codebase-wide rename, or breaks the "no implementation-phase tickets" rule with no license to do so.
Reinstatement: add to `to-tickets/SKILL.md` step 3: "Exception: a mechanical, blast-radius-wide change (rename,
retype) is not a vertical slice - ticket it as expand, then batched migrate, then contract, staying green between
tickets."

### 6. "Do not touch the parent issue" guard dropped, with nothing replacing it (MED)
Upstream: `to-tickets/SKILL.md` step 5, "Do NOT close or modify any parent issue." A specific scope-control rule
protecting the source issue/spec a ticket set was generated from.
Merged: no equivalent anywhere in `to-tickets/SKILL.md`, `tracker/ticket-schema.md`, or either backend guide.
Failure mode: an agent publishing child tickets could plausibly "clean up" or close the originating issue/spec as
part of the same pass; nothing in the merged text forbids it.
Reinstatement: `to-tickets/SKILL.md` step 7: "Publish only new tickets; never close or edit the ticket or spec the
work originated from."

### 7. Triage state-transition guard rails dropped (MED)
Upstream: `triage/SKILL.md` - explicit transition graph (unlabeled -> `needs-triage`; `needs-info` -> `needs-triage`
once reporter replies), "every triaged issue carries exactly one category and one state role; if state roles
conflict, flag it and ask before doing anything else," and "flag transitions that look unusual and ask." These are
rationalization counters: they stop an agent from silently applying a second, conflicting state label or making an
odd jump (e.g. `wontfix` straight to `ready-for-agent`).
Merged: `tracker/state-model.md` documents the state *meanings* but no transition rules or conflict guard, and
`triage/SKILL.md` step 3 says "choose exactly one triage state" (no-conflict is implied by the field being
singular) but never says to flag an unusual transition or resurface a `needs-info` ticket once new info lands.
Failure mode: stale `needs-info` tickets never get automatically re-surfaced for re-triage (no mechanism says to
check reporter activity since notes), and no guard catches an agent making a surprising jump.
Reinstatement: `tracker/state-model.md`: "An unusual transition (e.g. `wontfix`->`ready-for-agent`) should be
flagged to the maintainer before applying. Re-triage a `needs-info` ticket once new information arrives."
(Partially already true - "Re-triage a ticket if its assumptions or scope change" exists - but the *unusual
transition* flag and the *needs-info resurfacing trigger* are both new asks, not covered by that sentence.)

### 8. to-spec's content has no surviving home (MED)
Upstream: `to-spec/SKILL.md` - synthesize-don't-interview spec writing, explicit seam-identification step ("use
the highest seam possible... the fewer seams across the codebase, the better - the ideal number is one," confirmed
with the user), and the full spec template (Problem Statement / Solution / User Stories / Implementation Decisions
/ Testing Decisions / Out of Scope / Further Notes), published with `ready-for-agent`.
Merged: PROVENANCE.md records this as `wrapper -> commands/plan.md`, but `commands/plan.md` just invokes the
generic `plan` skill ("Turn approved design into small implementation tasks with acceptance evidence") - a
different skill entirely (implementation task breakdown, not spec synthesis from conversation). None of: the
no-interview synthesis instruction, the seam-minimization rule, or the User Stories / Out of Scope spec template
survive anywhere in the catalog. This is a bigger gap than the "wrapper" provenance label suggests - a wrapper
implies the target skill absorbed the content; `plan` did not.
Reinstatement: either fold the seam-identification rule into `plan/SKILL.md` step 1 ("prefer the highest, fewest
test seams; ideally one"), or restore a thin `to-spec`-equivalent skill for conversation-to-spec synthesis.

## PRUNED-OK (deliberate, recorded, judged sound)

- `.out-of-scope/` rejected-feature knowledge base (triage/OUT-OF-SCOPE.md) - explicit non-goal in
  `docs/specs/2026-08-31-tracker-pack-design.md` ("Full historical out-of-scope knowledge base... "
  non-goal). Losing the dedup/institutional-memory mechanism is a real capability drop but a *named* one.
- Category roles `bug`/`enhancement` and the wontfix-by-reason branching (already-implemented / rejected-bug /
  rejected-enhancement) - collapses cleanly once out-of-scope KB is gone, since that branching existed mainly to
  route into it.
- PR-as-issue triage surface, AI-disclaimer comment requirement, `gh`/`glab` CLI specifics - GitHub-specific
  mechanics, correctly backend-scoped per PROVENANCE ("GitHub tracker backend is opt-in").
- setup-matt-pocock-skills interactive scaffolding - recorded `adapter-only`, replaced by static
  `.agents/tracker.md` + backend-guide templates. Reasonable given the harness-portable design.
- Quick state override shortcut ("if maintainer says move to X, trust and act, skip grilling") - a convenience
  escape valve, not a guard; its absence just means the full procedure always runs. LOW-severity even if counted
  as lost.
- Resuming-a-previous-session logic (don't re-ask resolved questions) - genuinely useful but LOW severity, folds
  into general "read the ticket" step; flagged only as a minor quality loss, not scored as a finding above.
- Literal Markdown map-body template in wayfinder - merged replaced the copy-paste block with equivalent prose
  sections; content preserved, just reformatted.
- gitlab.md backend - not requested by this audit's merged-file list; present in repo (`tracker/backends/` only
  ships github.md/local.md per design non-goals: "Linear or other hosted trackers" - gitlab was ported anyway per
  earlier commits, out of scope for this pass).

## KEPT (tallies, no detail needed)

- Vertical-slice / tracer-bullet definition, blocking edges, frontier concept, quiz-and-approve-before-publish gate
  (to-tickets).
- Full wayfinder mechanism: map-as-index, decision tickets sized to one session, HITL vs AFK ticket types
  (research/prototype/grilling/task) with the "grilling agent must not answer its own questions" guard, fog-of-war
  vs ticket sharpness test, out-of-scope-as-scoping-act, refer-by-name rule, one-ticket-per-session limit
  (exception: research), claim-before-work. This is the most faithfully preserved of the five upstream files, and
  is *more* thorough than to-tickets/triage in the merge (backend guides carry explicit "Wayfinding operations"
  sections mirroring upstream's tracker-specific mechanics almost verbatim).
- State model core: 5 triage states + claimed/done, evidence-required-before-done - and this is enforced
  *mechanically* now (`scripts/tracker_local.py` raises on missing/malformed claim or evidence fields), which is
  stronger than upstream's prose-only rule.
- Ticket schema fields (Status/Claimed by/Claimed at/Blocked by/Outcome/Acceptance criteria/Evidence) - a clean
  superset merge of upstream's local-file and GitHub-issue templates.
- Backend-neutrality discipline: no `gh`/API syntax leaks into canonical skill files (verified structurally by
  `test_contracts.py` per the plan doc).

## Skills with no upstream source (per-instruction note)

`claim-ticket` and `work-frontier` have no directly corresponding upstream `SKILL.md` among the five audited files.
They decompose logic that upstream left embedded in prose (to-tickets' "Work the frontier: any ticket whose
blockers are all done" line, and the general claim/frontier mechanics upstream only spells out inside wayfinder and
the tracker doc's "Wayfinding operations" sections). Treat them as original additions that generalize a pattern
upstream only instantiated for wayfinder - not a loss, but worth knowing they're not ports.

## Severity summary

- HIGH: 2 (agent-brief writing discipline gone; triage verification-before-decision step gone)
- MED-HIGH: 1 (redundancy check gone)
- MED: 5 (domain/ADR consumer rules; wide-refactor exception; parent-issue guard; triage transition guard rails;
  to-spec content orphaned)
- LOW / PRUNED-OK: recorded above, mostly deliberate and defensible.
