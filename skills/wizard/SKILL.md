---
name: wizard
description: Use when a human must perform manual steps only they can do - provisioning, credentials, third-party dashboards, one-off migrations - and needs a generated step-by-step interactive script.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: delivery, source: merge }
---

# Wizard

A wizard is a bash script that walks a human through a manual procedure: it opens each URL, says exactly what to click and copy, captures values, writes them where they belong, confirms at every stage, and shows stages remaining. Generate one only for steps the agent cannot perform itself. When the procedure will repeat and is worth keeping as a document, write the runbook first in the shape of [RUNBOOK.md](RUNBOOK.md) and generate the wizard from it.

The UX is solved by [template.sh](template.sh): stage progress, confirmation gates, cross-platform URL opening, hidden secret entry, idempotent env-file upserts, CI secret writes, closing summary. Author only the stages below the STAGES marker; never hand-edit the library above it.

A wizard is ephemeral by default: built for one run, kept in a scratch or scripts path, deleted when done. Commit it only when the user wants a repeatable setup path in the repo.

## Procedure

1. Scope: enumerate every manual step and captured value by reading the repo first (env examples, README, CI workflow secret references, or current vs target state for a migration). Confirm the ordered stage list with the user. Done when every captured value has a source, a destination, and a secret-or-public marking.
2. Map each stage: the precise human path - URL, actions, where the value appears, which variable it fills. Where the current UI or command is unknown, say so and ask; never invent steps.
3. Author: copy `template.sh` to the target path, one `stage` per step in dependency order, set `TOTAL_STAGES`. Open the URL before asking for its value, use hidden entry for secrets, persist every value the plan named, and gate irreversible actions behind `confirm`.
4. Verify statically and hand off: syntax-check, make executable, trace that every planned value lands where planned and every CI secret name matches its workflow reference. Do not run it end-to-end yourself - it blocks on human input. Tell the user how to run it.
