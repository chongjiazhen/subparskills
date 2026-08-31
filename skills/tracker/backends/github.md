# GitHub backend

Use this backend only when `.agents/tracker.md` explicitly contains:

```markdown
Backend: github
```

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
