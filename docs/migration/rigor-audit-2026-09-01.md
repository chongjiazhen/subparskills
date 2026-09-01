# Rigor audit: merge execution vs upstream

Created 2026-09-01T03:02:20Z. Audits the Codex-executed merge (subparskills fe70af3) against
upstream pins `obra/superpowers` b36e0829 and `mattpocock/skills` 6654f6b6 (re-cloned, pins
verified), plus the operator's `the maintainer's private skills` deepened set. Method: seven
parallel per-cluster reviews grading every upstream mechanism KEPT / PRUNED-OK /
LOST-LOAD-BEARING; key claims re-verified against source by the commander.

## Verdict

The merge is structurally faithful and procedurally complete - every phase skeleton, schema,
and ordering constraint survived, several skills came through strengthened (merge-conflicts,
research, wayfinder, wizard, teach), and the tracker redesign is honest about its named
deltas. But it systematically stripped one entire genre: **pressure-resistance and
authorization-gate content**. 10 of 14 superpowers skills carry a `Red Flags` or `Common
Rationalizations` section (excuse -> reality tables, STOP self-checks, confirm-before-acting
gates); the merged catalog contains zero. That is an editorial stance ("procedure only"),
not random loss - and it discards the thing superpowers exists for: wording that holds when
an agent is tempted to shortcut. The tell is reflexive: the merged `writing-for-agents`
itself lost the bulletproofing-against-rationalization and match-form-to-failure guidance
that would have identified these sections as load-bearing rather than prunable.

The catalog claims `compatibility: Any Agent Skills-compatible harness`. On the operator's
own boxes some losses are backstopped by the maintainer's private rules layer (verification, disposition);
on the portable harness the catalog advertises, they are not backstopped by anything.

## HIGH findings (false completion, unauthorized action, or data exposure possible)

Grouped; per-item reinstatement one-liners are in the cluster tables below.

1. **Rationalization/red-flag machinery absent catalog-wide.** tdd, verify, diagnose, grill,
   finish, worktrees, review all lost their excuse->reality tables and STOP lists. Includes
   verify's "trusting a subagent's own success report is not evidence" row and tdd's
   "delete code written before its test - don't adapt it" rule.
2. **Authorization gates dropped.** grill lost "do not act until the user confirms shared
   understanding" and gained a "user seems ready" exit hatch; per-task independent review
   became discretionary ("when risk warrants" - the agent grades its own risk); no
   stop-conditions doctrine (irreversible / security-sensitive / out-of-worktree side effect
   / broken plan) survives anywhere; superpowers brainstorming's approval-gate Red Flags
   table reached nothing despite PROVENANCE recording "merge -> grill".
3. **Safety rules dropped.** Redact-secrets is gone from both places upstream carried it:
   diagnose (redact shown command output, loop against env vars) and handoff (redact
   keys/PII before the doc becomes another agent's prompt). Worktrees lost the
   verify-directory-gitignored-before-create check; finish lost confirm-the-base-branch.
4. **Verification specifics weakened to vacuity.** Verify-RED trichotomy (fails-for-missing-
   behavior vs errors vs passes), suite-wide green + pristine output, the mutation check,
   the tautological/change-detector test rule, mock discipline (boundary-only, mock earns no
   assertions), diagnose's proof-of-loop (show the command you already ran), triage's
   verify-the-claim-before-deciding step - all gone.
5. **Orchestration rigor gone.** Durable progress ledger against compaction (upstream calls
   blind re-dispatch "the single most expensive failure observed"); fix-loop round cap with
   adjudicate-and-log, "silent discards forbidden"; worker status contract
   (DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT) with explicit permission to escalate;
   workers-never-spawn-their-own-reviewers; preflight cross-task conflict scan; task
   interface (Consumes/Produces) contracts.
6. **Tracker: agent-brief durability discipline gone** (no file paths / line numbers in
   tickets - they go stale before an AFK claim; behavioral not procedural; explicit
   out-of-scope list). Nothing in ticket-schema.md or to-tickets carries it.
7. **writing-for-agents lost its own enforcement layer**: bulletproofing-against-
   rationalization, the entire persuasion-principles file (the one upstream item with a
   measured effect size, 33%->72%), match-form-to-failure taxonomy (with the measured
   prohibition-backfire finding), both ship checklists, one-hop reference depth + TOC rule,
   the `@`-force-load trap.

## Provenance drift (record does not match execution)

- `to-spec` recorded as `wrapper -> commands/plan.md`, but `plan` absorbed none of it: the
  seam-minimization rule ("ideal number of seams is one") and conversation-to-spec synthesis
  do not exist anywhere in the catalog. The wrapper label overstates coverage.
- `brainstorming` recorded as `merge -> grill`, but its gate machinery (the actual substance
  beyond interview mechanics grill already had from mattpocock) did not land.

## MED findings (compressed)

ADR concept dropped catalog-wide (offer-an-ADR 3-part gate, ADR-conflict bar in
architecture-improvement, CONTEXT.md scope discipline); design-it-twice's parallel
constrained fan-out collapsed to "sketch two interfaces"; prototype lost pure-module
isolation (logic liftable into real code); diagnose lost the Minimise phase, backward
root-cause tracing, pattern-analysis-vs-working-example, and 3-failed-fixes ->
question-architecture; receiving-review discipline absent entirely (verify feedback against
codebase, clarify-all-before-implementing-any, YAGNI-check reviewer suggestions); reviewer
read-only-on-checkout rule; phase-boundary decision tree (continue > handoff > compact);
to-tickets lost the wide-refactor expand/contract exception (the surviving rule is actively
wrong for that case) and the never-touch-the-parent-issue guard; triage lost the
redundancy check and transition guard rails; grill lost non-blocking fact-finding dispatch;
skill-testing lost the per-type taxonomy, micro-test protocol, and meta-testing diagnostic;
degrees-of-freedom (specificity matched to fragility), forward-slash paths, and
script-bundling discipline from anthropic-best-practices.

## Correctly pruned (merge got these right)

Harness-specific mechanics and ceremony (superpowers announce-lines, plugin bootstrap,
adapter references, output-format templates, model-cost tiers); brand/persona content;
worked-example galleries and anecdotes; artifact templates where the catalog deliberately
dropped prescription (teach formats, HTML report, wizard kept template.sh byte-identical);
GitHub specifics behind the backend split; setup-* skills; the out-of-scope knowledge base
(a recorded non-goal). Local tracker backend now enforces evidence-before-done mechanically
via `scripts/tracker_local.py` - stronger than upstream prose.

## Operator `.scratch/skills` verdict: not bloated

All three graded copies (diagnose, grill+GAP-REVIEW, wait-what, writing-for-agents) came
back leaner than feared: the only trims worth making are provenance/changelog comment
blocks, one citation name-drop, and a slightly ceremonious grill Step 0. They are fuller
restatements, not accretion. They also carry unique load-bearing content the merge lacks:

- GAP-REVIEW: the no-fix-proposing rule ("diagnosis and treatment are separate jobs") -
  which the merged GAP-REVIEW directly violates (its step 5 ends with a proposed revision);
  the missing-stakeholder gap class; the skipped-class-reads-as-clean completion check.
- grill: pushback-handling (reasoned pushback -> accept and move on; unreasoned -> ask once);
  state-the-hole-directly tone rule.
- diagnose: post-fix "what would have prevented this" reflection step.
- writing-for-agents: the `!` splice mechanism (Claude-Code-specific; flag, don't port to
  the portable catalog).

Note: the `.scratch` set did NOT restore upstream's dropped rigor either - the same losses
hold there.

## Remediation applied 2026-09-01 - and what was deliberately not applied

Commits 1eae846 and 1b1890d applied every HIGH finding and the one-line MED findings.
Deliberately skipped, with reasons - revisit only if the trigger fires:

- **defense-in-depth** (diagnose, LOW/MED): validate-at-every-layer sits in tension with the
  least-code-that-works posture and was upstream's weakest gate. Trigger to revisit: the same
  bad value reaching a fixed failure point through a second path.
- **wait-what multi-glossary routing** (CONTEXT-MAP fan-out, LOW): edge-case file routing;
  the flat "GLOSSARY.md when one exists" rule covers the common case. Trigger: a repo with
  more than one glossary actually in use.
- **`!` splice mechanism** (operator writing-for-agents): Claude-Code-specific; the catalog
  declares harness-neutral compatibility. Stays in the operator's private layer.
- **Full re-import of upstream bodies** (200-600 lines each): the catalog's lean-body,
  pointed-reference architecture is the design, not the defect; reinstatement was
  gate-by-gate, table-by-table.
- **persuasion-principles citations** (Cialdini; Meincke et al. 2025): the operative wording
  rule survives compressed in SKILL-AUTHORING's Matching Form To Failure; the study citations
  and effect sizes stay in the upstream file and the writing-for-agents cluster report.
- **Red-green revalidation of the reinstated wording**: deferred (also noted in CHANGELOG).
  The wording compresses upstream text pressure-tested upstream - evidence, not proof.
  Trigger: any reinstated gate observed failing under pressure in a live session.
- **Remaining MED items not applied**: diagnose condition-based-waiting (test-authoring
  technique, not a diagnostic gate); micro-test protocol and meta-testing diagnostic
  (skill-authoring depth beyond the catalog's current ambition); phase-boundary five-option
  tree beyond the one-line continue-by-default rule in handoff; to-spec conversation-to-spec
  synthesis (recorded as unported in its PROVENANCE row).

## Recommended remediation shape

Do not re-import the 200-600-line upstream bodies. The catalog's own architecture already
has the right slot: pointed reference files per skill (the grill/DECISION-TREE.md pattern).
Concretely: one `PRESSURE.md`-style reference per discipline skill (tdd, verify, diagnose,
grill, review, implement) carrying the compressed rationalization table + STOP list; restore
the dropped one-line gates directly into skill bodies where they are gates, not reference
(confirm-before-acting, redact, gitignore check, mandatory task review, base-branch
confirm); fix the two provenance rows; port the four operator-unique items above into the
canonical bodies. Per-item terse reinstatement wording for every finding is in the seven
cluster reports (session artifacts); the HIGH-tier wording is short enough to apply from
this document alone.
