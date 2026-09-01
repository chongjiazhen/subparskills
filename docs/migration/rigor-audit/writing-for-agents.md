# Audit: writing-for-agents merge (subparskills) vs upstream

Upstream read in full: superpowers/skills/writing-skills/{SKILL.md, anthropic-best-practices.md,
persuasion-principles.md, testing-skills-with-subagents.md}; mattpocock-skills/skills/productivity/
writing-for-agents/{SKILL.md, SKILL-MECHANICS.md}.
Merged: subparskills/skills/writing-for-agents/{SKILL.md, SKILL-AUTHORING.md}.
Operator deepened: private skills/writing-for-agents/{SKILL.md, SKILL-MECHANICS.md}.

## Verdict summary

mattpocock/skills writing-for-agents content (context pointers, two loads, information hierarchy,
completion criteria, leading words, pruning, invocation/router mechanics) survived the merge
almost isomorphically - compressed prose, same substance. KEPT in full.

superpowers' writing-skills content is where the rigor loss concentrates. The merge kept the
RED-GREEN-REFACTOR *label* (as "Red-Green Validation," 4 lines) but dropped essentially every
mechanism that made superpowers' skill-testing regime actually bite: the anti-rationalization
scaffolding, the persuasion-principles wording technique, the per-skill-type testing taxonomy,
the deployment checklist, and several concrete technical gotchas from anthropic-best-practices.
persuasion-principles.md (a whole file, cited research, N=28,000) is not referenced anywhere.

## LOST-LOAD-BEARING (detailed)

1. **Bulletproofing skills against rationalization** (superpowers SKILL.md "Bulletproofing
   Skills Against Rationalization", lines 476-543; reinforced in testing-skills-with-subagents.md
   REFACTOR phase, lines 163-237) - Defends against: an agent that *knows* the discipline rule
   and rationalizes past it under pressure ("spirit not letter," "keep as reference," "this case
   is different"). Mechanism: explicit negation of each workaround, a foundational "violating the
   letter is violating the spirit" line, a per-skill rationalization table (excuse -> reality), a
   red-flags self-check list. None of this survives in the merge - SKILL-AUTHORING.md's
   Red-Green Validation section states only "add the smallest wording that fixes the observed
   failure," with no guidance on the *shape* that wording must take to resist rationalization.
   Severity: HIGH - a discipline skill authored under the merged catalog's process can pass its
   own baseline test once and still fold under real pressure, with no prompt in the catalog to
   close the loophole.
   Reinstatement: "Discipline rule surviving pressure needs 3 things: an explicit no-exceptions
   list naming the specific workarounds you saw in testing, a rationalization table (excuse ->
   reality), and a red-flags self-check list - a bare rule restatement is not enough."

2. **persuasion-principles.md - entire file** - Defends against: discipline skills that are
   technically correct but wordy/soft, which measurably fail to survive pressure. Concrete,
   cited technique (Cialdini's principles; Meincke et al. 2025, N=28,000 AI conversations,
   compliance 33%->72% with authority/commitment/scarcity framing) mapped to skill-type ("use
   Authority+Commitment+Social Proof for discipline skills, avoid Liking/Reciprocity"), with an
   ethics gate ("would this serve the user's genuine interest"). Zero trace in the merge - not
   summarized, not linked, not folded into any other section. Severity: HIGH - this is the one
   piece of upstream content backed by an actual measured effect size, and it is the mechanism
   the rest of superpowers' bulletproofing techniques (no-exceptions lists, foundational
   principles) are instances of. Losing it strips the *why* and the *how to extend it* from every
   other surviving discipline-skill guidance.
   Reinstatement: "Wording that must survive pressure: imperative + no-exceptions (authority),
   forced explicit choice (commitment), immediate not deferred (scarcity) - avoid liking/
   reciprocity framing for compliance. Cialdini 2021; Meincke et al. 2025 measured 33%->72%."

3. **Match the Form to the Failure** (superpowers SKILL.md, lines 459-474) - Defends against:
   applying the wrong intervention type to a failure (prohibition lists for a *shaping* problem -
   wrong output shape, not rule-skipping). Cites a measured result: in head-to-head wording
   tests, prohibition-based guidance on a shaping problem produced *more* of the unwanted content
   than a positive recipe, and trended worse than no guidance at all. Also states "no nuance
   clauses" and "exemption clauses don't scope" as general rules for whichever form is chosen.
   The merge's "Negation" aside (folded into Leading Words) keeps only the narrowest slice -
   don't over-rely on prohibition - and drops the 4-row failure-type taxonomy (skip-under-
   pressure / wrong-shape / omitted-element / conditional-behavior) entirely, along with the
   measured backfire finding and the nuance/exemption-clause traps. Severity: HIGH - without the
   taxonomy an author has no way to tell which of the four failure types they're facing, and the
   dropped backfire finding is the strongest evidence in the corpus for why the choice matters.
   Reinstatement: "Classify the baseline failure before choosing a form: skip-under-pressure ->
   prohibition + rationalization table; wrong-shape output -> positive recipe (a prohibition here
   measurably produces MORE of the unwanted content); omitted element -> required field/slot;
   conditional behavior -> keyed conditional, never an unconditional rule + exemptions (exemption
   clauses don't scope)."

4. **Per-skill-type testing taxonomy** (superpowers SKILL.md "Testing All Skill Types," lines
   395-442) - Defends against: applying pressure-scenario testing (built for discipline skills)
   to a reference or pattern skill, where it's the wrong tool, or skipping testing on a technique
   skill because it "isn't a discipline skill." Gives per-type test design and success criteria
   (discipline: pressure scenarios; technique: application/variation/gap tests; pattern:
   recognition/counter-example tests; reference: retrieval/gap tests). Not present in merge at
   any granularity - SKILL-AUTHORING.md's Red-Green Validation reads as one-size-fits-all.
   Severity: MED.
   Reinstatement: "Test shape follows skill type: discipline -> pressure scenario; technique ->
   apply-to-new-case + edge cases; pattern -> recognize-when-it-applies + counter-example;
   reference -> can-it-be-found + gap check."

5. **Micro-test wording before full pressure scenarios** (superpowers SKILL.md lines 575-586) -
   Defends against: shipping guidance validated only by a single expensive pressure-scenario run,
   or never validated at all because full runs are "too slow." Concrete cheap-validation protocol:
   one fresh-context sample per call, a no-guidance control mandatory before authoring anything,
   5+ reps, manual read of every flagged match (automated counts overstate both directions),
   variance-across-reps as its own metric. Not in merge. Severity: MED - this is the affordable
   on-ramp to the testing discipline; without it, "test before shipping" (already weakened per
   item 1) has a higher activation cost and is more likely skipped outright.
   Reinstatement: "Before a full pressure-scenario run: 1 fresh-context sample per wording
   variant incl. a no-guidance control (skip authoring if the control doesn't fail), 5+ reps,
   read every flagged match by hand, treat reply variance itself as a signal the wording isn't
   binding."

6. **Skill Creation / deployment checklist** (superpowers SKILL.md lines 614-667, "STOP: Before
   Moving to Next Skill" + "Skill Creation Checklist") + **anthropic-best-practices.md
   "Checklist for effective Skills"** (lines 1101-1134) - Defends against: batch-authoring
   several skills without testing each one ("batching is more efficient"), and shipping a skill
   missing a required element (frontmatter shape, packages listed, error handling explicit, no
   voodoo constants, tested on multiple models). Two separate concrete checklists upstream; zero
   consolidated checklist in the merge. Severity: MED-HIGH - this is the closest thing upstream
   has to a hard "ready to ship" gate, and the merged catalog has none at all beyond the 4-line
   Red-Green Validation paragraph.
   Reinstatement: "One skill at a time: test and verify each skill before starting the next -
   batching authoring across untested skills is the same violation as batching untested code."

7. **Meta-testing when a skill "should have worked" but didn't**
   (testing-skills-with-subagents.md lines 240-266) - Defends against: an author giving up or
   over-correcting when a pressure test fails, without diagnosing *why*. Concrete 3-way
   diagnostic: ask the failing agent how the skill could have been written to make the correct
   option unmistakable, and sort the answer into "skill was clear, I chose to ignore it"
   (need a stronger foundational principle) / "skill should have said X" (add verbatim) /
   "I didn't see section Y" (organization problem, promote it). Not in merge. Severity: MED.
   Reinstatement: "Skill failed pressure test? Ask the failing agent how the skill should have
   been worded to make the correct choice unmistakable - the answer sorts into ignored-it
   (need a stronger foundational rule), missing-content (add verbatim), or buried (promote it)."

8. **Degrees of freedom (narrow-bridge vs open-field)**
   (anthropic-best-practices.md lines 59-131) - Defends against: over-specifying a judgment-call
   task (kills adaptability) or under-specifying a fragile, must-follow-exact-sequence task
   (invites drift/error). Concrete 3-tier framework - high freedom (text heuristics) / medium
   (parameterized pseudocode) / low (exact script, no deviation) - keyed to task fragility, with
   a memorable analogy. Not present anywhere in the merge (Information Hierarchy covers *where*
   content sits, not *how much latitude* to give the agent executing it - a different axis).
   Severity: MED - this is a distinct authoring decision the merge's ladder doesn't cover at all.
   Reinstatement: "Match specificity to fragility: many valid paths -> text heuristics (high
   freedom); a preferred pattern with acceptable variation -> parameterized pseudocode (medium);
   one exact sequence, error-prone if varied -> a fixed script, no parameters to negotiate (low)."

9. **Deep-nesting partial-read failure mode**
   (anthropic-best-practices.md lines 353-406, "Avoid deeply nested references" +
   "Structure longer reference files with table of contents") - Defends against: an agent
   previewing a reference chain with `head -100`-style partial reads when references are nested
   more than one level from SKILL.md, silently working from incomplete information; and a >100
   line reference file with no table of contents suffering the same partial-read blindness.
   Concrete rule: keep every reference file one hop from SKILL.md, and put a TOC at the top of
   anything past 100 lines. Not in merge - Information Hierarchy states the 3-tier ladder but
   never states the one-hop-deep rule or the TOC requirement. Severity: MED-HIGH - this is a
   specific, previously-observed failure mode (silent incomplete read, not an error), not just
   a style preference.
   Reinstatement: "Keep every disclosed-reference link one hop from the entry file - a reference
   chained through another reference gets partially read via head-style previews. Any reference
   file over ~100 lines gets a table of contents at the top so a partial read still shows scope."

10. **Windows-style path prohibition**
    (anthropic-best-practices.md lines 825-832, 1125) - Defends against: a skill authored with
    backslash paths (`scripts\helper.py`) breaking on any Unix-based runtime. Concrete, checkable
    rule (forward slashes always, checklist item). Not in merge at all. Severity: MED - a real,
    previously-seen correctness bug, not a style nit; and notably this exact trap is invisible to
    an author working on a Windows box (this very session), which is the population most likely
    to reproduce it.
    Reinstatement: "Skill file paths: forward slashes only, even when authored on Windows -
    backslash paths break on Unix runtimes."

11. **Script-bundling discipline** (anthropic-best-practices.md "Solve, don't punt" lines 855-906,
    "Provide utility scripts" + execute-vs-read-as-reference distinction lines 908-961,
    "Create verifiable intermediate outputs" / plan-validate-execute lines 985-1002,
    and MCP fully-qualified tool names lines 1053-1071) - Defends against 4 distinct failure
    modes for skills that bundle executable code: (a) a script that punts error handling back to
    the agent instead of solving it, or leaves unjustified "voodoo constants"; (b) ambiguity over
    whether a referenced script should be *run* or *read as reference*, which either wastes
    tokens loading it or causes the agent to skip execution; (c) no intermediate
    validation step on a batch/destructive operation, catching errors only after they're applied;
    (d) an MCP tool referenced without its `ServerName:` prefix, causing "tool not found" when
    multiple servers are present. None of these four appear anywhere in the merge - the merged
    catalog has no section on skills that bundle scripts/tools at all. Severity: MED (narrower
    scope - only bites skills with executable code - but each is a concrete, previously-observed
    bug class).
    Reinstatement: "Bundled script: handle its own errors, justify every constant, and state
    explicitly whether the agent should run it or read it as reference. Batch/destructive
    operation: validate a plan file before executing it. MCP tool: always `ServerName:tool_name`."

12. **Cross-reference `@` force-load gotcha**
    (superpowers SKILL.md lines 278-289) - Defends against: writing `@skills/x/SKILL.md` style
    references between skills, which force-loads the target file's full content immediately
    (200k+ context) rather than deferring it behind a pointer - defeating progressive disclosure
    from inside the skill body itself. Concrete rule: use a named requirement marker
    (`**REQUIRED SUB-SKILL:** skill-name`) instead of an `@`-link. Not in merge - the merge's
    Context Pointers section explains pointer *wording* generally but never flags this specific
    Claude-Code-specific syntax trap. Severity: MED - a real technical footgun that silently
    defeats the merge's own stated goal (progressive disclosure / minimizing context load).
    Reinstatement: "Cross-referencing another skill: name it plainly (`REQUIRED: skill-name`),
    never `@skill/path` - `@` force-loads the target immediately, burning the context budget the
    pointer model exists to save."

## KEPT (tally)

- RED-GREEN-REFACTOR framing, retitled "Red-Green Validation" (compressed but structurally intact)
- Frontmatter contract (name/description/trigger-oriented "Use when")
- Description-is-triggers-not-workflow-summary rule (worked example dropped, rule kept - see PRUNED-OK)
- Keyword coverage in descriptions
- Evaluation-driven-development spirit (baseline before writing docs)
- All of mattpocock/skills writing-for-agents: context pointers, two loads, information hierarchy,
  progressive disclosure, co-location, sprawl, completion criteria (clarity/demand), splitting
  by sequence, leading words, negation-as-failure-mode (narrow slice), pruning (single source of
  truth, environment-as-cache, relevance, no-ops)
- Invocation trade-off (model-invoked vs user-invoked), router skills, shared-reference placement

## PRUNED-OK (tally)

- SDO worked-example narrative (the "one review vs two" incident) - rule survives, anecdote cut
- Flowchart-usage style guidance, code-example style guidance, file-organization patterns -
  redundant with progressive-disclosure content kept elsewhere
- Anti-patterns gallery (narrative example, multi-language dilution, generic labels)
- Descriptive/gerund naming convention - style, not a behavior gate
- Third-person voice rule for descriptions - minor, no clear failure mode tied to it
- Numeric token-budget targets (<150/<200/<500 words) - superseded by general "concise is key"
  principle; losing the exact numbers is a minor completeness gap, not a gate loss
- Time-sensitive-info / "old patterns" `<details>` pattern, consistent-terminology reminder
- Template/examples/conditional-workflow "common patterns" gallery - mostly redundant illustration
- Agent-A/Agent-B iterative development narrative, "observe how agents navigate" checklist -
  advisory, not gating
- Package-dependency platform notes (claude.ai vs API) - deployment-target-specific, not general

## Operator deepened version vs merged (both directions)

**(a) Load-bearing in operator version, missing from merged:**
- `!` splice mechanism (operator SKILL-MECHANICS.md, "`!` splice - the deterministic lane inside
  a skill body," verified on CLI 2.1.227): a body line `` !`<shell>` `` executes at invoke time
  and its stdout replaces the line before the model reads it - the mechanism for making a
  guarantee (repo bindings, git ground truth, a checker's verdict) un-skippable rather than
  prose the model can skip/mistype/reconstruct from memory. This is the concrete implementation
  of "Where guarantees live -> deterministic layer" (the operator's code-modification rules) *inside* a
  skill file, and it is entirely absent from the merged catalog, which has no mechanism at all
  for making any part of a skill body deterministic rather than advisory. Caveat: this is Claude
  Code-specific (the merged frontmatter declares `compatibility: Any Agent Skills-compatible
  harness`), so its absence may be a deliberate portability cut rather than an oversight - flag,
  don't auto-port, if the merged catalog targets multiple harnesses.

**(b) Bloat in operator version:**
- Minimal. The operator file carries a 5-line HTML-comment provenance header (upstream commit
  hash, license, local-adaptation notes) that costs tokens on every load and has no effect on
  agent behavior - the one clear candidate for trimming if this file is ever promoted somewhere
  context-sensitive. Otherwise the operator version is not bloated relative to the merge; it is
  the fuller (uncompressed) restatement of the same content the merge already compressed, not an
  expansion beyond it.

## Severity rollup

HIGH: bulletproofing/rationalization-table technique (1), persuasion-principles.md entire file (2),
Match-the-Form taxonomy (3).
MED-HIGH: deployment checklist (6), deep-nesting/TOC partial-read failure mode (9).
MED: per-skill-type testing taxonomy (4), micro-test protocol (5), meta-testing diagnostic (7),
degrees-of-freedom framework (8), Windows-path rule (10), script-bundling discipline (11),
`@`-force-load gotcha (12).
