# subparskills rigor audit

Scope: superpowers (writing-plans, requesting-code-review + code-reviewer.md,
receiving-code-review, dispatching-parallel-agents, subagent-driven-development
+ 3 prompt templates, finishing-a-development-branch, using-git-worktrees,
using-superpowers) and mattpocock-skills (engineering/code-review,
productivity/handoff, in-progress/claude-handoff, engineering/ask-matt +
PHASE-BOUNDARIES.md) against merged skills/plan, review, parallel-execution,
finish, worktrees, handoff, choose-skill and commands/{plan,finish,handoff,implement}.md.

## LOST-LOAD-BEARING

### 1. Workers must never spawn their own reviewer/helper subagents - HIGH
Upstream: `requesting-code-review/code-reviewer.md` section "You Do Not Dispatch
Subagents"; `subagent-driven-development/implementer-prompt.md` and
`task-reviewer-prompt.md`, same section, verbatim in three places. Also named
in subagent-driven-development's Common Rationalizations: "The implementer
spawned its own reviewer, free extra assurance" versus reality: "It's a duplicate
seat reviewing the same diff... a defect to flag, not rigor."
Failure defended against: recursive/runaway subagent spawning, and a
worker-spawned reviewer that looks like extra assurance but actually
duplicates the one review seat the process already grants at full cost,
diluting or masking the real gate.
Merged catalog has no such constraint anywhere (review, parallel-execution,
implement all silent on it).
Reinstatement (implement / parallel-execution / review, terse register):
"Worker never dispatches its own reviewer or helper subagents; review comes
only from the commander after the worker reports."

### 2. Durable progress ledger across context loss - HIGH
Upstream: `subagent-driven-development/SKILL.md` section Setup: "Conversation memory
does not survive compaction. In real sessions, controllers that lost their
place have re-dispatched entire completed task sequences, the single most
expensive failure observed. Track progress in a ledger file, not only in
todos." Ledger is also where every autonomous ruling must be recorded and
surfaced before cleanup.
Failure defended against: after context loss/compaction, blind re-execution
of already-completed (possibly destructive/committing) work.
Merged `implement` has no persistence/resume discipline at all (4 lines,
no mention of tracking completed tasks against context loss).
Reinstatement (implement): "Record each completed task in a durable ledger
file; on resume, trust the ledger over recollection, never re-dispatch a
task the ledger marks done."

### 3. Stop conditions plus rulings-not-stalls doctrine - HIGH
Upstream: `subagent-driven-development/SKILL.md` top section: "A running plan does
not wait on a human... Four things stop you, and only these: an irreversible
or destructive operation; a security-sensitive action; a side effect outside
this worktree... a plan so broken that every path forward is a guess."
Everything else gets decided and logged as `Ruling: <what> - <why> - <cost if
wrong>`.
Failure defended against: two opposite failure modes, stalling on routine
ambiguity (wastes the user's day for nothing), and barreling through
irreversible/destructive/security-sensitive/external side-effect actions
without asking.
Merged `implement`/`parallel-execution` say nothing about when autonomous
judgment is allowed vs. when to stop.
Reinstatement (implement): "Decide ambiguities yourself and log the ruling.
Stop only for an irreversible/destructive op, a security-sensitive action, a
side effect outside the workspace, or a plan broken beyond guessing."

### 4. Fix-loop round cap, escalation, and breaker adjudication - HIGH
Upstream: `subagent-driven-development/SKILL.md` section 4 "The fix loop": 5 rounds
max, rounds 4-5 escalate to a fresh implementer on a stronger model, a scoped
re-review only verifies the named findings, and at the cap every open finding
is adjudicated and logged, "Silent discards are forbidden." Common
Rationalizations: "Close enough on spec compliance" and "This finding is
obviously wrong, I'll drop it" are both named and refuted.
Failure defended against: an unresolved review loop that either never
converges, or gets abandoned by the agent quietly deciding a finding doesn't
matter and moving on unrecorded.
Merged `review` only has "Recheck critical and important fixes before
approval", no bound, no escalation, no adjudicate-and-log-at-cap step.
Reinstatement (review): "Cap fix/re-review rounds; past the cap, adjudicate
every remaining open finding explicitly and log the ruling, never drop one
silently."

### 5. Task review is mandatory, not risk-discretionary - HIGH
Upstream: `subagent-driven-development/SKILL.md` section 3: "Never skip the task
review... Implementer self-review never replaces the task review; both are
needed."
Failure defended against: agent judges its own risk as low and skips
independent review, the exact self-assessment the rule exists to prevent.
Merged `implement` step 3: "request independent review when risk warrants",
converts a hard per-task gate into a discretionary call the same agent makes.
Reinstatement (implement): "Every task gets an independent review before the
next task starts; self-review never substitutes for it."

### 6. Explicit worker status contract plus permission to refuse/escalate - HIGH
Upstream: `subagent-driven-development/implementer-prompt.md` section "When You're in
Over Your Head": "It is always OK to stop and say 'this is too hard for me.'
Bad work is worse than no work. You will not be penalized for escalating,"
plus the required status vocabulary DONE / DONE_WITH_CONCERNS / BLOCKED /
NEEDS_CONTEXT and "Never silently produce work you're unsure about."
Failure defended against: pressure to report false completion rather than
surface uncertainty, the core false-completion failure mode.
Merged catalog has no status contract or escalation permission anywhere
(implement, parallel-execution both silent).
Reinstatement (implement / parallel-execution): "Worker may report
blocked/needs-context instead of guessing; escalating uncertainty is never
penalized, silently shipping unsure work is."

### 7. Redact secrets/PII before writing a handoff artifact - HIGH
Upstream: `mattpocock-skills/productivity/handoff/SKILL.md` and
`in-progress/claude-handoff/SKILL.md`, both: "Redact any sensitive
information, such as API keys, passwords, or personally identifiable
information", for claude-handoff explicitly because "the summary becomes
the agent's prompt."
Failure defended against: a handoff document (which may be pasted into a
fresh session, sent to a colleague, or become another agent's literal prompt)
forwarding live credentials or PII with nothing gating it.
Merged `handoff` (4 lines) has no redaction step at all.
Reinstatement (handoff): "Redact secrets, credentials, and PII before
writing the handoff."

## LOST-LOAD-BEARING (MED)

### 8. Receiving-feedback discipline is entirely absent
Upstream: `receiving-code-review/SKILL.md`, whole skill, verify against the
codebase before implementing, clarify every unclear item before
implementing any of them (explicitly ruled out: "implement what's clear,
ask about the rest later"), YAGNI-check a reviewer's "do it properly"
suggestion by grepping for actual usage, push back with technical reasoning
rather than complying automatically.
Failure defended against: performative/blind implementation of feedback, and
partial implementation of multi-item feedback that leaves an inconsistent
state because later items were related to the skipped ones.
Merged `review` only covers the reviewer's side (findings, severity,
re-verification); nothing in the catalog addresses how a worker or commander
receiving review feedback should act on it.
Reinstatement (review): "On received feedback: verify against the codebase
before implementing; if any item is unclear, clarify all unclear items
before implementing any of them."

### 9. Reviewer must not mutate the checkout - MED
Upstream: `requesting-code-review/code-reviewer.md` section "Read-Only Review" and
`subagent-driven-development/task-reviewer-prompt.md`, same rule: never move
HEAD, checkout, or otherwise mutate the working tree/index/branch; use a
separate worktree to inspect another revision.
Failure defended against: a review subagent corrupting the user's live
working tree while merely trying to inspect a diff or another commit.
Merged `review` has no isolation/mutation constraint.
Reinstatement (review): "Review is read-only on the checkout, never move
HEAD or otherwise mutate tree/index/branch state; inspect another revision
in a separate worktree."

### 10. Preflight cross-task conflict scan before execution starts
Upstream: `subagent-driven-development/SKILL.md` section Setup: before dispatching
Task 1, build a table of every task-pair sharing a file or interface (what
one produces vs. what the other consumes) and every task's internal
self-consistency, rule on every conflict found, and write the table to the
ledger, "'The scan is clean' without those rows is not a scan you ran."
Failure defended against: two tasks with contradictory specs or interfaces
both get built before the contradiction surfaces, since each fresh
implementer subagent sees only its own task.
Merged `plan` step 4 only checks spec-to-task coverage, not inter-task
consistency; merged `implement` has no preflight scan step either.
Reinstatement (plan): "Before execution, check every pair of tasks sharing a
file or interface for contradiction; rule on conflicts found before
dispatching task 1."

### 11. Task interface contract plus cross-task type-consistency check
Upstream: `writing-plans/SKILL.md` section Task Structure ("Interfaces: Consumes /
Produces, exact function names, parameter and return types... this block is
how [the implementer] learns the names and types neighboring tasks use") and
section Self-Review #3 "Type consistency": "A function called `clearLayers()` in
Task 3 but `clearFullLayers()` in Task 7 is a bug."
Failure defended against: a later task assumes a name/signature the earlier
task didn't actually produce, undetectable to a fresh subagent that only
ever reads its own task.
Merged `plan` has no Interfaces block and no signature-consistency check
(step 4 is spec-coverage only).
Reinstatement (plan): "Each task states what it consumes from earlier tasks
and produces for later ones, exact names and types; recheck those names and
signatures agree across tasks before execution."

### 12. Worktree directory must be verified gitignored before creation
Upstream: `using-git-worktrees/SKILL.md` section Safety Verification: "MUST verify
directory is ignored before creating worktree... Why critical: Prevents
accidentally committing worktree contents to repository."
Failure defended against: an entire worktree's contents (including another
branch's checked-out files) getting committed into the repo by accident.
Merged `worktrees` has no gitignore check (step 1 only inspects status,
step 2 creates the worktree).
Reinstatement (worktrees): "Verify the worktree directory is gitignored
before creating it; add and commit the ignore first if not."

### 13. Phase-boundary decision procedure (continue / clear / handoff / subagent / compact)
Upstream: `ask-matt/PHASE-BOUNDARIES.md`, whole file: an ordered five-option
tree, "Continue costs nothing and loses nothing... rule it out first,"
`/compact` is explicitly "the default, not the first reach" because it is
the lossiest option and "the failure mode when people start here is a fresh
session that is confidently wrong about a decision the summary flattened."
Failure defended against: premature/needless compaction or handoff losing
context that continuing would have kept for free, or the inverse, grinding
on past the point continuing still pays off.
No merged skill addresses when to hand off/compact/subagent vs. simply
continue; `handoff` only describes what goes in a handoff once the
decision to write one is already made.
Reinstatement (handoff): "Continue in-session by default, it costs nothing.
Reach for handoff only when context must move harness, directory, or owner;
compaction is lossier still and a last resort."

## LOST-LOAD-BEARING (LOW)

### 14. Confirm the base branch before merging
Upstream: `finishing-a-development-branch/SKILL.md` section Step 3: "Confirm before
merging: merging into the wrong base is expensive to undo."
Merged `finish` never mentions identifying/confirming the base branch.
Reinstatement (finish): "Confirm the base branch this work forked from
before merging, the wrong base is expensive to undo."

## KEPT (compressed, tally)

- Task right-sizing to `plan` #2
- No-placeholder discipline to `plan` #3
- Spec-coverage self-review to `plan` #4 (partial: coverage kept, type-consistency lost, see #11)
- Independent-vs-sequential dispatch decision to `parallel-execution` #1
- Focused/self-contained/output-spec'd worker prompts to `parallel-execution` #2
- Commander keeps integration/verification, inspects each result to `parallel-execution` #3-4
- Verify-then-menu, exactly-as-written options, discard only on explicit request to `finish` #1, #3-4
- Worktree detection-first, native-tool preference, clean-scope-before-edit to `worktrees` #1, #3
- Both spec-compliance and code-quality checked (architecture of running them as separate sub-agents dropped, but the content itself survives) to `review` #1-2
- Do-not-blindly-trust-implementer's-report to `review` #3 (partial; the "stated rationale never downgrades severity" nuance is dropped, folded into #4/#9 above rather than a separate line item)

## PRUNED-OK (tally, not detailed)

Plan Document Header template; bite-sized-step granularity; "Execution
Handoff" menu ceremony; git-SHA capture and dispatch mechanics; all Output
Format templates (code-reviewer.md, task-reviewer-prompt.md,
plan-document-reviewer-prompt.md); Common Rationalizations / Common Mistakes
/ Red Flags tables that restate a gate already counted above rather than
adding a new one; model-selection cost tiers; same-shape-work batching
guidance; bounded-wait/poll mechanics; the 42k-char pasted-history anecdote;
git-worktree Detect-Environment / cleanup-ownership mechanics; native
worktree tool preference; sandbox fallback; "type the literal word discard"
ceremony; Fowler smell baseline list; spec-source discovery order;
two-axis-review's parallel-subagent execution mechanism (the checks
themselves survive, only the isolation mechanism is dropped); ask-matt's
"smart zone" token-budget specifics and its own flow/route map (superseded
adequately by `choose-skill`'s route map); using-superpowers' mandatory
skill-invocation enforcement ceremony and platform-adapter references;
"suggested skills" section in a handoff doc; do-not-duplicate-other-artifacts
guidance in handoff; GitHub inline-thread reply mechanics; forbidden-phrase
social-performance list ("You're absolutely right!" etc.) and
acknowledging-correct-feedback tone examples.
