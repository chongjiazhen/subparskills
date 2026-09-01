# Grill/wait-what/to-questionnaire merge audit

Scope: mattpocock-skills {grilling, grill-me, grill-with-docs, wait-what, to-questionnaire}
+ superpowers brainstorming (read for cross-reference, has no direct merge counterpart -
excluded from tallies) -> subparskills {skills/grill/*, skills/wait-what, skills/to-questionnaire,
commands/grill.md}. Second pass: subparskills vs operator's personal deepened versions
(private skills/{grill,wait-what}).

## Part A - upstream -> merged

### LOST-LOAD-BEARING

**1. HIGH - No explicit "wait for confirmation before acting" terminal gate.**
Upstream `grilling/SKILL.md` line 28: "The session is done when the frontier is empty:
every branch of the design tree visited, nothing left silently assumed. **Do not act on
it until the user confirms you have reached a shared understanding.**" This is a hard
stop between "interview looks done" and "start implementing" - it requires an explicit
user confirmation, not just the agent's own judgment that decisions are settled.
Merged `skills/grill/SKILL.md` step 5 ends with "confirmed decisions, deferred branches
with reasons, and the safest next concrete step" - a report, not a gate. Nothing in
`commands/grill.md` or `DECISION-TREE.md` requires waiting for an explicit yes before
moving to implementation. Failure mode defended against: the agent treats its own
summary as sufficient authorization and starts coding off a self-graded "shared
understanding" the user never actually confirmed.
Reinstatement (terse register): add to grill/SKILL.md step 5 - "Wait for the user to
confirm the summary before treating any deferred item as settled or starting
implementation."

**2. MED - Completion criterion weakened from exhaustive to satisficing.**
Upstream: "done when frontier is empty... nothing left silently assumed" - an
exhaustiveness bar. Merged `skills/grill/SKILL.md` step 4: "Stop when the remaining
questions are low leverage **or the user is ready to move into implementation**." The
"user is ready" disjunct lets the session end with unvisited high-leverage branches if
the user simply signals impatience - exactly the case the upstream gate exists to catch.
`DECISION-TREE.md`'s "confirmed or consciously deferred" partially compensates (a
branch can't be silently skipped, only consciously deferred) but the SKILL.md-level exit
condition undercuts it.
Reinstatement: change grill/SKILL.md step 4 to "Stop when every high-leverage branch is
confirmed or consciously deferred with a stated reason - not merely when the user seems
ready to move on."

**3. MED - Fact-finding delegation (subagent dispatch, non-blocking parallelism) dropped.**
Upstream: "Finding facts is your job, never the user's... dispatch a sub-agent to find
it; don't ask the user for anything you could look up yourself. Don't block on it: a
running exploration is an unsettled prerequisite, so only the questions downstream of it
wait... ask the rest of the frontier now." Two distinct rules bundled: (a) never ask the
user a fact-question you could resolve yourself - KEPT in merged (`DECISION-TREE.md`:
"Read code, tests, and recent changes before asking questions the codebase can settle").
(b) for research that needs real digging, spin it off and keep interviewing everything
not downstream of it - LOST. Merged's procedure gives no guidance for the case where
settling a branch needs more than a quick read; nothing stops the agent from serially
blocking the whole interview on its own investigation instead of parallelizing.
Reinstatement: add to grill/SKILL.md step 1 or DECISION-TREE.md - "A branch needing real
investigation, not a quick read: dispatch it and keep asking branches that don't depend
on it; don't block the whole interview on your own research."

### PRUNED-OK (tally)

- grill-me's pure delegate-stub shape - collapsed into one skill. Correct consolidation.
- grill-with-docs's paired invocation of domain-modeling (ADR/glossary generation) -
  dropped; domain-model exists as its own skill in the catalog, just no longer
  auto-chained. Matches the task's "deliberately dropped artifact prescription" carve-out.
- Round/frontier **batching format** (numbered Q, ➡️ recommended-answer emoji block,
  whole-frontier-per-round) - replaced by one-branch-at-a-time in both merged and the
  operator's own deepened version, so this is a considered design choice on both sides,
  not an accidental drop. Presentational, not a gate.
- wait-what's `CONTEXT-MAP.md` multi-glossary routing (repo has more than one glossary) -
  dropped in favor of a flat "GLOSSARY.md when one exists." Edge-case file-routing
  mechanic, not a gate or rationalization-counter. LOW-severity omission if it matters
  at all.
- ASD-STE100 Simplified Technical English framing - present verbatim in both upstream
  and merged wait-what actually (kept, not pruned - noted only to confirm it survived).
- to-questionnaire: fully preserved (all 3 steps, document structure, all fields) in
  compressed prose. No loss.
- brainstorming's HARD-GATE / Red Flags anti-rationalization table has no counterpart in
  either mattpocock grilling or merged grill - it was never in this merge's scope
  (brainstorming wasn't ported as a skill at all), so not gradable as a merge loss here.
  Flagged only as a note: if brainstorming's approval-gate machinery was meant to inform
  grill's design, the "don't act without confirmation" bar in Finding 1 above is the same
  bar and is missing.

### KEPT (tally)

- Core interview posture: identify implicit decisions, recommend-then-confirm per
  question, skip cheap-to-reverse bikesheds - present in grill/SKILL.md + DECISION-TREE.md.
- "Read code before asking questions the codebase can settle" - kept.
- One-branch-at-a-time discipline - kept (in different form than upstream's round-batch,
  see PRUNED-OK).
- to-questionnaire: full fidelity.
- wait-what: stop-and-restate, minimum missing context, ubiquitous-language lookup,
  fallback to one concrete check question - all kept.
- GAP-REVIEW.md as new branch for "already-written artifact" case - present, addresses
  the same use case grill-with-docs implicitly covered.

## Part B - merged vs operator's personal deepened version

### (a) Load-bearing in operator's version, missing from merged

**HIGH - GAP-REVIEW: merged reintroduces fix-proposing that operator's version explicitly
bans.** Operator's GAP-REVIEW.md: "Do not rewrite, do not propose fixes... Diagnosis and
treatment are separate jobs; merging them lets the author accept a patch instead of
seeing the hole." Merged catalog's GAP-REVIEW.md step 5: "End with the smallest revision
that would make the artifact implementation-ready" - this is a fix proposal, the exact
thing the operator's version forbids and names a specific failure mode for (author patches
over the hole instead of confronting it). Not a case of the merge losing upstream content
(neither mattpocock file contains gap-review material at all - this branch has no
upstream source in scope) but it is a real, reasoned rigor loss relative to the more
developed reference design.
Reinstatement: replace merged GAP-REVIEW.md step 5 with "End with the gap list only - no
proposed fixes or rewrite. The user asks for fixes separately, once the holes are seen."

**MED - GAP-REVIEW: missing "perspectives/stakeholders absent" gap class and the
silent-omission completion check.** Operator's version names 5 gap classes including
"Perspectives or stakeholders absent from it" (merged's 4 - omissions, contradictions,
unowned decisions, unproven claims - has no equivalent) and closes with "A gap list that
skips a class silently reads the same as one where the class was clean" - an explicit
anti-silent-omission bar mirroring Finding 2 above. Merged has neither.
Reinstatement: add a "missing stakeholder/perspective" bullet to merged GAP-REVIEW.md
step 2, and close with "treat a skipped category as unchecked, not clean."

**MED - grill: pushback-handling rule absent.** Operator's SKILL.md step 2: "If the user
pushes back with a reason, accept it and move on - don't re-litigate. If they push back
without a reason, ask for the reason once, then accept." Nothing in merged grill/SKILL.md
governs what happens when the user disagrees with a recommended answer - a real gap in
question-discipline coverage (re-litigating settled ground vs. capitulating to unreasoned
pushback are both named agent failure modes the operator's version explicitly guards).
Reinstatement: add to grill/SKILL.md step 3 - "Pushback with a reason: accept, move on.
Pushback without one: ask once for the reason, then accept."

**LOW/MED - grill: no tone/pressure-resistance directive.** Operator's Step 3: "Be
critical, not pleasant... don't pander." Merged grill has zero tone guidance, so without
a catalog-wide disposition layer loaded, a portable-harness agent defaults to soft
"have you considered X?" framing rather than stating the hole. This is squarely
pressure-resistance content per the audit's own definition, and it is absent.
Reinstatement: one line in grill/SKILL.md - "State the hole directly ('this breaks at X'),
not as a soft question."

### (b) Bloat in operator's version (accretion the merge correctly left out)

- Provenance/changelog prose: wait-what's HTML comment block (upstream commit hash,
  adaptation notes) and GAP-REVIEW.md's closing paragraph ("Template 08b... cribbed
  2026-07-27. Split out of SKILL.md 2026-08-06...") - session/edit history, not runtime
  instruction. Correctly absent from the portable catalog.
- Step 0's citation ("Origin: Thariq Shihipar's field guide, unknown-unknowns quadrant")
  - name-drop with no operational content.
  add. Correctly absent.
- Repo-specific pointers (`guidelines/identifier-canonicalization.md`,
  `guidelines/lightweight-spec.md`, `rules/disposition.md`) - would not resolve in a portable
  catalog; the merge correctly generalized these into inline, self-contained bullets
  (DECISION-TREE.md's "Identifier semantics" line stands alone; grill/SKILL.md has no
  disposition.md dependency, unresolved above as a genuine gap, not this one).
- Operator's Step 0 "blindspot pass" is a fuller, more ceremonious restatement of what
  merged compresses into one clause in step 1 ("If the terrain is unknown, survey
  constraints and seams..."). The extra structure (named Step 0, propose-and-confirm a
  sharper plan paragraph before restarting from Step 1) is defensible depth, not pure
  bloat, but it is heavier than the merge's version needs to be for the same behavior.

## Summary

3 upstream findings (1 HIGH, 2 MED) - all cluster around one theme: the merge kept the
interview MECHANICS (recommend-then-confirm, read-before-ask) but weakened the
COMPLETION/AUTHORIZATION gate (exhaustiveness bar, explicit confirm-before-acting) and
dropped the parallel-research nuance.

4 operator-vs-merged findings (1 HIGH, 2 MED, 1 LOW/MED) - GAP-REVIEW's fix-proposing
regression is the standout: it is a direct, named contradiction of a documented rationale
("diagnosis and treatment are separate jobs"), not an ambiguous prune.
