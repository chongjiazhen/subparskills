# Audit: tdd / verify / implement rigor loss

Scope: superpowers {test-driven-development/SKILL.md+writing-good-tests.md, verification-before-completion/SKILL.md, executing-plans/SKILL.md} and mattpocock-skills {engineering/tdd/SKILL.md+mocking.md+tests.md, engineering/implement/SKILL.md, in-progress/implement-spec/SKILL.md} vs subparskills skills/{tdd,verify,implement,review}/SKILL.md.

Merged files are ~4-18 lines each (compressed procedure only). No mocking.md, tests.md, or writing-good-tests.md counterpart exists anywhere in the catalog (confirmed via full file listing) - every mechanism below not literally inlined into the 4 merged SKILL.md files is gone, not relocated.

## LOST-LOAD-BEARING

### HIGH

1. **TDD Common Rationalizations table** - superpowers `test-driven-development/SKILL.md` section Common Rationalizations (10-row excuse->reality table: "too simple to test", "I'll test after", "tests after achieve same goals", "already manually tested", "deleting X hours wasteful", "keep as reference", "need to explore first", "test hard = design unclear", "TDD will slow me down", "existing code has no tests"). Defends against: agent rationalizing a skip of test-first under time/sunk-cost pressure. Merged `tdd/SKILL.md` has zero rationalization counters.
   Reinstatement: `Common excuses ("too simple", "I'll test after", "already manual-tested", "keep old code as reference") are the rule breaking, not an exception to it.`

2. **TDD Red Flags - STOP and Start Over** - superpowers `test-driven-development/SKILL.md` section Red Flags (code before test, test passes immediately, can't explain why test failed, "already manually tested it", "it's about spirit not ritual", "already spent X hours"). Defends against: agent noticing its own violation mid-stream and rationalizing past it instead of restarting. No equivalent in merged `tdd/SKILL.md`.
   Reinstatement: `Wrote code before the test, or test passed on first run? Delete the code (or the false-positive test) and restart the cycle - do not adapt it in place.`

3. **"Delete means delete" - no salvage of pre-test code** - superpowers `test-driven-development/SKILL.md` section The Iron Law: "Write code before the test? Delete it... Don't keep it as reference. Don't adapt it while writing tests. Don't look at it." Defends against: agent writing implementation first, then backfilling a test that was silently shaped by the code it's supposed to specify. Merged step 1 only says "no production code before observed failing test" - no instruction on what to do when that's already been violated.
   Reinstatement: `Code already written before its test? Delete it - don't adapt or reference it. Rewrite from the test.`

4. **Verify-RED specificity** - superpowers section Verify RED: confirm the test fails "because feature missing (not typos)"; "Test passes? You're testing existing behavior, fix test. Test errors? Fix error, re-run until it fails correctly." Merged step 2 says only "confirm expected failure caused by missing behavior" - drops the errors-vs-fails-vs-passes trichotomy that catches an agent mistaking a broken test harness for a valid red.
   Reinstatement: `Confirm the test fails for the missing behavior, not a typo or errored setup - a passing or errored "red" invalidates the cycle.`

5. **Tautological / change-detector tests** - mattpocock `tdd/SKILL.md` section Anti-patterns "Tautological", `tests.md` (calculateTotal example), superpowers `writing-good-tests.md` section Principle 1 "No change detectors" plus Gate Function ("Confirm the expected value is derived without the code under test... replace it with a literal"). Defends against: an agent writing a test whose expected value is computed by the same code/helper under test, which passes by construction and proves nothing - a specific false-verification pattern, not covered by anything in merged catalog.
   Reinstatement: `Derive the expected value independently (hand literal, not the code's own helper) - a test that recomputes what the code computes passes by construction.`

6. **Mutation check before finishing a test** - superpowers `writing-good-tests.md` section The Mutation Check ("mentally mutate the production code; at least one test should fail for each realistic mutation"). Defends against: false completion - a green suite that doesn't actually cover the branch/edge case being claimed as done. Not referenced anywhere in merged `tdd` or `verify`.
   Reinstatement: `Before calling a test done, mutate the code it targets (wrong branch, dropped side effect, empty return) - if nothing fails, the behavior is unprotected.`

7. **verification-before-completion Red Flags - STOP list** - superpowers `verification-before-completion/SKILL.md` section Red Flags ("should"/"probably"/"seems to", expressing satisfaction before verification, trusting agent success reports, "just this once", "tired and wanting work over"). Defends against the exact failure mode this audit is checking for: an agent claiming done without fresh evidence, especially trusting a subagent's own success report. Merged `verify/SKILL.md` (18 lines total) has no rationalization/red-flag content at all.
   Reinstatement: `Hedge words ("should work", "probably fine"), satisfaction before running the check, or trusting a subagent's own "done" report - treat each as an unmet claim, not a claim.`

8. **verification-before-completion Rationalization Prevention table** - same file, section Rationalization Prevention (8-row: "Should work now"->RUN it, "I'm confident"->confidence is not evidence, "Agent said success"->verify independently, "Linter passed"->linter is not compiler, etc.). Same defense as item 7, complementary. Entirely absent from merged.
   Reinstatement: `Confidence, a prior run, a subagent's report, or a passing linter are not evidence of the specific claim being made - run the command that proves it, now.`

9. **Common Failures mapping table** - superpowers `verification-before-completion/SKILL.md` section Common Failures, specifically rows "Agent completed -> VCS diff shows changes, not agent reports success" and "Regression test works -> red-green cycle verified, not test passes once". Defends against trusting delegated/subagent work and against a regression test that was never proven to fail pre-fix. Given this catalog runs in a multi-agent orchestration context (per `implement-spec`/`parallel-execution`/`handoff` skills present in the same catalog), the delegated-work-verification gap is directly exercised territory. Merged `verify/SKILL.md` step 2 ("inspect changed state, not only exit status") is a much weaker generic hint with no subagent-specific instance.
   Reinstatement: `A subagent or teammate reporting "done" is not evidence - check the diff/state it claims to have changed, not its report.`

### MED

10. **Horizontal slicing anti-pattern** - mattpocock `tdd/SKILL.md` section Anti-patterns "Horizontal slicing" (write all tests, then all implementation, is banned; work in vertical slices, one test -> one implementation -> repeat). Defends against: an agent front-loading a batch of tests against imagined behavior instead of letting each cycle inform the next. Merged `tdd/SKILL.md` procedure is written as if only one cycle exists; nothing forbids batching.
    Reinstatement: `One test, one minimal implementation, repeat - do not write a batch of tests before any implementation.`

11. **Seams: test only at pre-agreed, user-confirmed boundaries** - mattpocock `tdd/SKILL.md` section Seams ("No test is written at an unconfirmed seam... confirm them with the user"). Defends against scope creep / testing-everything or testing the wrong layer without a checkpoint. No equivalent gate in merged tdd/implement.
    Reinstatement: `Confirm the seam (public interface under test) before writing the test - don't test at an interface no one agreed to.`

12. **Mock discipline: boundary-only, unmock-or-delete** - mattpocock `mocking.md` (mock external boundaries only, never own modules/internal collaborators; SDK-style per-endpoint mocks) plus superpowers `writing-good-tests.md` section Principle 2 ("The mock earns no assertions" - unmock it or delete the assertion; mirror full real structure; production classes carry production methods only). Defends against tests that pass by asserting on the mock rather than real behavior - a specific false-verification pattern (matches the audit's "verification requirements" category) with zero coverage in merged catalog.
    Reinstatement: `Mock only external/slow boundaries, never your own code. Assertion targets a mock's existence? Unmock it or delete the assertion.`

13. **TDD Verification Checklist (pre-completion)** - superpowers `test-driven-development/SKILL.md` section Verification Checklist (8-item: every function has a test, watched each fail, failed for expected reason, minimal code, all pass, pristine output, real code not mocks, edge cases covered - "Can't check all boxes? You skipped TDD, start over"). Overlaps with but is more specific than merged `verify/SKILL.md`; nothing TDD-specific survives in merged `tdd/SKILL.md`.
    Reinstatement: `Before marking a TDD task done: every changed function has a test, you watched each fail first, output is pristine, edge/error cases covered - any box unchecked means restart, not ship.`

14. **Verify-GREEN "other tests still pass, pristine output"** - superpowers section Verify GREEN. Merged step 3 ("Run focused test; confirm pass") only checks the one test, dropping the requirement to confirm the rest of the suite didn't regress and that output has no stray errors/warnings.
    Reinstatement: `Confirm pass on focused test AND no regression in the rest of the suite; output must be clean, not just non-failing.`

15. **executing-plans explicit STOP conditions** - superpowers `executing-plans/SKILL.md` section When to Stop and Ask for Help (missing dependency, unclear instruction, repeated verification failure - not just "contradictory acceptance criteria"). Merged `implement/SKILL.md` step 1 only stops on "contradictory or missing acceptance criteria," narrower than the upstream list; an agent hitting an unclear instruction or a verification that keeps failing has no explicit stop instruction and may push through.
    Reinstatement: `Stop and ask (don't guess) on: missing dependency, unclear instruction, or verification failing repeatedly - not only on contradictory acceptance criteria.`

16. **"Never start implementation on main/master without explicit consent"** - superpowers `executing-plans/SKILL.md` section Remember, last bullet. Concrete, checkable safety gate against an irreversible-ish mistake; no analog anywhere in merged implement/tdd/verify.
    Reinstatement: `Confirm you're on a feature branch, not main/master, before the first implementation edit - ask if not.`

### LOW

17. **"Never fix bugs without a test" (debugging integration)** - superpowers `test-driven-development/SKILL.md` section Debugging Integration. Narrow restatement of the Iron Law for the bug-fix case; the Iron Law itself is kept, so this is mostly redundant, but the explicit bug-fix framing is gone.
    Reinstatement: `Bug fix: write the failing test that reproduces the bug first - same Iron Law, no bug-shaped exception.`

18. **When Stuck table** (superpowers) - advice for four stuck-states (don't know how to test, test too complicated, must mock everything, huge setup). Genuinely advisory, not a gate; fine to drop.

## PRUNED-OK (tallied)

- superpowers TDD: Red-Green-Refactor dot-diagram, Good/Bad code examples, worked bug-fix example, Final Rule restatement - redundant with kept procedure.
- superpowers `verification-before-completion`: Key Patterns checkmark examples, "When To Apply" enumeration - redundant with description/frontmatter trigger and kept gate function.
- superpowers `executing-plans`: "Announce at start" branding line, superpowers-specific sub-skill cross-references (`finishing-a-development-branch`, `subagent-driven-development`, `using-git-worktrees`), "tell your human partner Superpowers works better with subagents" - harness/persona-specific.
- mattpocock `tdd/SKILL.md`: CONTEXT.md/ADR domain-vocabulary note, `codebase-design` skill cross-reference - harness-specific pointers, not gates.
- mattpocock `mocking.md`/`tests.md`: code examples (good/bad TypeScript snippets) beyond the one-per-pattern the merged catalog already keeps in spirit - acceptable example pruning, though the underlying *rules* they illustrate (items 5, 12 above) were also dropped, not just the examples.
- mattpocock `implement/SKILL.md`: reasonably captured by merged `implement/SKILL.md`; only loses "run typechecking regularly" and "use /code-review once done," both minor process hints, not gates.
- mattpocock `implement-spec/SKILL.md`: entire multi-agent task-graph/PR/worktree orchestration content (frontier of tickets, implementer/merger subagents, draft-PR-per-spec workflow) - this is a specific parallel-delivery workflow, not a completion/rigor gate; the catalog's `parallel-execution`, `worktrees`, `to-tickets`, and `tracker` skills appear to cover this ground separately. Correctly out of scope for tdd/verify/implement.
- "Refactoring is not part of the loop, belongs to code-review stage" - process-sequencing note, effectively preserved by the catalog having a separate `review` skill.

## KEPT (tallied)

- TDD Iron Law (no production code before failing test).
- Name-the-behavior-first step (compressed form of writing-good-tests Gate Function 1).
- Verify-RED / verify-GREEN as a concept (though weakened, see items 4/14).
- Refactor-only-while-green.
- Verify skill's core "evidence before claim" Iron Law and its 3-step gate (identify->run->report), map-claim-to-command instruction.
- Implement skill's stop-on-missing-criteria, one-task-at-a-time, TDD-per-task, review-when-risk-warrants, evidence-recording.
