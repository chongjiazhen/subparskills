# GitHub backend

Use this backend only when `.agents/tracker.md` explicitly selects it. Every
tracker skill reads all five semantic mappings before performing backend
operations. Use this shared configuration template, replacing each convention
with the repository's actual field, label, or native issue feature:

```markdown
Backend: github
Ready state: repository field or label mapped to ready-for-agent
Claim convention: assignee plus UTC claim metadata in the issue body
Completion convention: repository done field or label plus a closed issue and non-empty evidence
Blocker representation: native issue dependencies with Blocked by body metadata as fallback
```

Never assume or hard-code a label name. Resolve ready and completion labels or
fields from `.agents/tracker.md`, and preserve the semantic meanings in
`../state-model.md` even when repository names differ.

Keep the ticket schema and state meanings from `../ticket-schema.md` and
`../state-model.md`. Prefer the repository's native issue dependency links and
assignee field for blockers and claims. When native dependency links are not
available, record ticket-number dependencies in the issue body as
`Blocked by: 011, 012`; use `Blocked by: None` when there are none.

Use the GitHub CLI only in this backend workflow. For example, inspect an
issue with `gh issue view 14`, assign a claim with
`gh issue edit 14 --add-assignee ACTOR`, and update its body with
`gh issue edit 14 --body-file ticket-body.md`. Record the actor and UTC
timestamp in the issue body before implementation starts. When closing work,
include concrete evidence in the body before resolving the issue.

Where the CLI cannot express a repository capability, call the GitHub REST API
from this backend only, for example `GET /repos/OWNER/REPO/issues/14`. Do not
copy this syntax into canonical skill procedures.
