# State model

Triage uses these mutually exclusive states:

- `needs-triage`: incoming work that has not yet been classified.
- `needs-info`: work that cannot be prepared until missing information arrives.
- `ready-for-agent`: a sufficiently specified ticket that an agent may claim
  when its blockers are done.
- `ready-for-human`: work requiring a human decision or action.
- `wontfix`: work intentionally not pursued.

Execution uses two additional states:

- `claimed`: active work owned by a recorded actor.
- `done`: completed work with concrete verification evidence.

Triage moves work from `needs-triage` to one of the other triage states. Add
or resolve information and blockers before moving work to `ready-for-agent`.
Only a ready, unclaimed, unblocked ticket may become `claimed`. Persist both
the actor and an ISO-8601 UTC timestamp before starting work. Move a claimed
ticket to `done` only after its acceptance criteria are met and its `Evidence`
section is non-empty. Re-triage a ticket if its assumptions or scope change.
