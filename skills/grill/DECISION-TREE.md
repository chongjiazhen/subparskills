# Decision Tree

Prioritize branches where being wrong will cost a migration, a data repair, or a hard-to-explain rollback.

## High-Leverage Branches

- Boundary behavior: startup, shutdown, retries, reconnects, partial failure, duplicate input.
- Ownership: which unit owns validation, coordination, and rollback.
- Identifier semantics: canonical IDs, joins, equality, and deduplication rules.
- Concurrency posture: what can run in parallel, what must serialize, and where recovery begins after interruption.
- Reversibility: code revert, config revert, data repair, or irreversible external effect.
- Done-when: the observable condition that proves the change is complete.

## Question Discipline

- Ask one branch at a time.
- Recommend the default answer before asking for confirmation.
- Read code, tests, and recent changes before asking questions the codebase can settle.
- Move on once a branch is confirmed or consciously deferred.
