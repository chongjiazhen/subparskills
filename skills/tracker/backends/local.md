# Local Markdown backend

This is the default backend. If `.agents/tracker.md` is absent, use local
Markdown tickets. If it exists without a `Backend:` field, use the same
default. A configuration that explicitly selects a different backend overrides
this default.

Store tickets at `.agents/tickets/NNN-slug.md`, using the schema in
`../ticket-schema.md` and states in `../state-model.md`. Give each ticket a
unique zero-padded numeric prefix and keep its heading number identical to the
filename number.

To list the available frontier, select only tickets whose status is
`ready-for-agent`, whose claim fields are unclaimed, and whose listed blockers
are all `done`. Before editing implementation files, write the claim actor and
UTC timestamp, then set the ticket status to `claimed`. Before setting status
to `done`, fill `## Evidence` with the verification command, observed result,
and changed behavior.
