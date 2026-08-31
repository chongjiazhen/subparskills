# Ticket schema

Every tracker ticket has a title and these metadata fields immediately after its
heading. For the local backend, store it at `.agents/tickets/NNN-slug.md`.

```markdown
# 014: Outcome title

Status: ready-for-agent
Claimed by: —
Claimed at: —
Blocked by: None

## Outcome

End-to-end behavior visible to user or verifier.

## Acceptance criteria

- [ ] Observable criterion

## Evidence

Required before `Status: done`: command, observed result, and changed behavior.
```

`Status` is the current triage or execution state. `Claimed by` and `Claimed
at` are either both populated or both unclaimed markers (`—`, `-`, or empty).
`Claimed at` uses an ISO-8601 UTC timestamp ending in `Z`. `Blocked by` is
`None` when there are no dependencies, otherwise a comma-separated list of
ticket numbers. `Outcome` states the delivered behavior, acceptance criteria
make it observable, and evidence records how completion was verified.
