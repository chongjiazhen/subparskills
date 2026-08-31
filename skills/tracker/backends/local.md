# Local Markdown backend

This is the default backend. Every tracker skill reads the semantic mapping in
`.agents/tracker.md` before performing backend operations. If the file is
absent, use these exact defaults:

```markdown
Backend: local
Ready state: Status metadata equals ready-for-agent
Claim convention: Claimed by and Claimed at metadata are populated, then Status is claimed
Completion convention: Evidence is non-empty, then Status is done
Blocker representation: Blocked by metadata contains ticket numbers or None
```

The same five fields form the shared tracker configuration template for every
backend. If `.agents/tracker.md` exists but omits a local field, use that
field's default above. A configuration that explicitly selects another backend
uses that backend guide's mappings instead.

Store tickets at `.agents/tickets/NNN-slug.md`, using the schema in
`../ticket-schema.md` and states in `../state-model.md`. Give each ticket a
unique zero-padded numeric prefix and keep its heading number identical to the
filename number.

To list the available frontier, select only tickets whose status is
`ready-for-agent`, whose claim fields are unclaimed, and whose listed blockers
are all `done` with non-empty evidence. Before editing implementation files,
write the claim actor and UTC timestamp, then set the ticket status to
`claimed`. Before setting status to `done`, fill `## Evidence` with the
verification command, observed result, and changed behavior.
