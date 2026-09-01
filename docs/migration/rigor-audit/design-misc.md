# Audit: design/misc skill cluster - mattpocock-skills to subparskills

Scope: codebase-design, domain-modeling, improve-codebase-architecture, setup-ts-deep-modules,
research, prototype, resolving-merge-conflicts, wizard, teach.

## LOST-LOAD-BEARING

### 1. MED - ADR-gating test dropped entirely (domain-modeling to domain-model)
Upstream `engineering/domain-modeling/SKILL.md` section "Offer ADRs sparingly" gates ADR creation on
a 3-part test (hard to reverse AND surprising without context AND result of a real trade-off,
skip if any is missing), with the full rationale and qualifying-examples list in
`ADR-FORMAT.md` section "When to offer an ADR"/"What qualifies". This is a rationalization-counter: it
stops the agent from either never writing ADRs (losing decisions) or writing one for every
trivial choice (drowning the log). `skills/domain-model/SKILL.md` in the merge has zero mention
of ADR, `docs/adr/`, or any gating test - confirmed via grep, no file in the merged catalog
references ADRs at all. The numbering scheme, template, and "Considered Options"/"Consequences"
optional-sections guidance (`ADR-FORMAT.md`) are also gone, but those are template mechanics
(PRUNED-OK); the 3-part gate is the load-bearing part.
Reinstate (terse): `domain-model/SKILL.md` step 4 -> "Offer an ADR only when reversal cost is
real AND the choice will look surprising later AND a genuine alternative was rejected; skip
otherwise."

### 2. MED - CONTEXT.md file-structure and scope discipline dropped (domain-modeling to domain-model)
Upstream `SKILL.md` section "File structure" defines lazy-create `CONTEXT.md` at repo root, and a
`CONTEXT-MAP.md` fan-out for multi-context repos (with per-context `CONTEXT.md` + `docs/adr/`).
`CONTEXT-FORMAT.md` adds the hard rule: "`CONTEXT.md` should be totally devoid of implementation
details. Do not treat it as a spec, a scratch pad, or a repository for implementation
decisions." That rule prevents scope creep in a document other skills (`architecture-improvement`)
read as ground truth for domain vocabulary; if it silently fills with implementation notes, the
vocabulary contract degrades and downstream design work inherits bad terms. None of this survived:
`domain-model/SKILL.md` never names `CONTEXT.md`, `CONTEXT-MAP.md`, or a scope rule.
Reinstate (terse): domain-model/SKILL.md -> "Record vocabulary in CONTEXT.md (or per-context under
CONTEXT-MAP.md); glossary only, no implementation detail."

### 3. MED - Design-It-Twice parallel sub-agent mechanism dropped (codebase-design to architecture-improvement/INTERFACE-DESIGN.md)
Upstream `DESIGN-IT-TWICE.md` is a full process: frame the problem space for the user first, then
spawn 3+ sub-agents in parallel, each given a distinct hard constraint (minimize interface,
maximize flexibility, optimize common caller, ports-and-adapters), each required to return a
structured brief (interface, usage example, what's hidden, dependency/adapter strategy,
trade-offs); then present sequentially, compare on depth/locality/seam placement, and give an
opinionated recommendation ("the user wants a strong read, not a menu"). The merged
`INTERFACE-DESIGN.md` collapses this to "Sketch at least two materially different interfaces...
Compare depth, locality, and migration cost. Recommend one." The parallel-fan-out mechanism (which
is what makes the alternatives *radically* different rather than variations the same author drifts
into) is gone; this is explicitly the kind of design-discipline-that-changes-outcomes example
named in the audit brief itself.
Reinstate (terse): INTERFACE-DESIGN.md step 2 -> "Fan out 3+ parallel agents, each under one hard
constraint (minimal surface / max flexibility / common-case-trivial / ports-and-adapters); each
returns interface + usage + hidden impl + adapters + trade-offs. Don't design serially."

### 4. MED - ADR-conflict handling gate dropped (improve-codebase-architecture to architecture-improvement)
Upstream `SKILL.md` section 3 "Grilling loop": "if a candidate contradicts an existing ADR, only surface
it when the friction is real enough to warrant revisiting the ADR... Don't list every theoretical
refactor an ADR forbids." This stops the tool from re-litigating settled architecture decisions on
a whim. `architecture-improvement/SKILL.md` has no mention of ADRs at all (consistent with finding
#1, the concept was dropped catalog-wide), so a deepening proposal can now silently contradict a
recorded decision with no flag and no bar for reopening it.
Reinstate (terse): architecture-improvement/SKILL.md step 4 -> "If a proposal contradicts a
recorded ADR, only surface it when the friction is real enough to justify reopening the ADR."

### 5. MED - Pure-module isolation discipline dropped from logic prototyping (prototype/LOGIC.md to prototype/SKILL.md)
Upstream `LOGIC.md` section 2 "Isolate the logic in a portable module": the actual state
machine/reducer/pure-functions must be written with zero DOM/`document`/button-handler coupling,
specifically so it "could be lifted out and dropped into the real codebase later"; this is what
makes step 5 ("Capture the answer") actually work. Reinforced by its own anti-pattern: "Don't blur
the logic and the page together... Keep the page as a thin shell over a pure module." The merged
`prototype/SKILL.md` describes only the demo's external behavior ("a runnable demo that pushes the
state model through hard-to-reason cases") with no isolation requirement; a prototype built under
the merged instructions can end up with logic wired straight into DOM handlers, making step 6
("fold the validated decision into real code") much harder than the upstream design intended.
Reinstate (terse): prototype/SKILL.md rule 2 -> "Keep the logic under test in a pure module (no
DOM/document/handlers); the page is a thin shell over it, liftable into the real codebase later."

## PRUNED-OK (tally)

- `codebase-design` ASCII deep/shallow diagrams, "Rejected framings" section - illustrative/pedagogical, no behavior change.
- `codebase-design` "Designing for testability" code-example triad (accept deps, return not side-effect, small surface) - LOW-severity trim; general spirit survives via "interface is the test surface" / deletion-test carried in DEEPENING.md and LANGUAGE.md. Worth a one-line reinstatement if budget allows, not flagged as a full finding.
- `codebase-design` glossary terms "Implementation" (vs Adapter) and formal "Leverage" definition - dropped from LANGUAGE.md; term "leverage" still used operationally in architecture-improvement/SKILL.md step 4, just undefined. LOW.
- `improve-codebase-architecture` step-1 exploration heuristics (walk `git log` for hotspots, spawn a sub-agent to explore organically, the specific friction-question checklist) - compressed to "scope scan to active change area; read domain vocab and tests first." Real thoroughness loss but prose-level, not a gate. LOW.
- `improve-codebase-architecture` HTML-REPORT.md scaffold/styling - explicitly out of scope per audit brief (artifact template).
- `setup-ts-deep-modules` - entire skill dropped. Correctly pruned: it's a TS/dependency-cruiser-specific setup skill (stack-specific tooling, matches the audit's own non-load-bearing example). Its one generic technique, "prove the rules bite" (pass, break, fail, revert, pass), is a specific instance of the catalog's generic `verify/SKILL.md` ("run full checks fresh... do not claim pass without evidence"), so the discipline isn't actually lost catalog-wide, only its worked example.
- `research` - background/async-agent dispatch mechanism dropped, but the merged `research/SKILL.md` is a strict superset in rigor (decision framing, primary-source priority, per-claim source+timestamp+confidence, UTC-dated brief, explicit "does not authorize changes" boundary). Net gain, not a loss.
- `resolving-merge-conflicts` to `merge-conflicts` - fully preserved (primary-source resolution, no invented behavior, run checks, finish/stage/commit) and actually strengthened: merged version adds an explicit stop-for-user-approval gate (security posture, secrets, deployment config, data meaning) not present upstream.
- `wizard` - `template.sh` is byte-identical to upstream (diffed by inspection, no differences). `SKILL.md` preserves every gate: open URL before asking, hidden entry for secrets, `confirm` before irreversible actions, never run end-to-end, static trace of every captured value and CI secret name. Fully KEPT.
- `teach` - the four `*-FORMAT.md` template files (MISSION-FORMAT, RESOURCES-FORMAT, LEARNING-RECORD-FORMAT, and implied lesson format) are dropped in favor of inline description; matches the audit's own "canned artifact template" exclusion. Substance (mission-grounding, fluency-vs-storage-strength, zone-of-proximal-development, tight feedback loops, community-for-wisdom) fully retained in `teach/SKILL.md`.

## KEPT (tally)

- Deletion test - present in both `deep-modules/SKILL.md` ("reject extraction that only moves complexity across callers") and `architecture-improvement/LANGUAGE.md`.
- "One adapter = hypothetical seam, two = real" - `architecture-improvement/LANGUAGE.md`.
- Dependency-category classification (in-process / local-substitutable / owned-remote ports-and-adapters / true-external mock) - `architecture-improvement/DEEPENING.md`, compressed but complete, including "don't expose internal seam only to make tests convenient."
- "Tests cross module interface, assert observable outcomes, delete shallow-module tests once interface tests exist" - `architecture-improvement/DEEPENING.md`.
- Merge-conflict resolution procedure - `merge-conflicts/SKILL.md`, preserved and strengthened (see PRUNED-OK).
- Wizard mechanics and template - fully preserved, see above.
- Research rigor - preserved and strengthened, see above.
- Teach workspace model (MISSION/RESOURCES/lessons/reference/learning-records/assets/NOTES, ZPD, fluency-vs-storage) - fully preserved in `teach/SKILL.md`.
- Prototype's general throwaway-artifact rules (marked as prototype, trivial to run, no persistence, skip polish, surface state, capture-when-done) - preserved in `prototype/SKILL.md`, apart from finding #5 above.
