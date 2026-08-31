# Tracker Pack Design

Created: 2026-08-31T13:28:07Z

## Goal

Add an opt-in `tracker` pack that coordinates multi-session and multi-agent work through small vertical-slice tickets, explicit blocker edges, claims, and proof-backed completion.

`delivery` remains tracker-agnostic. Repositories may continue to use direct planning and implementation workflows without configuring a tracker.

## Scope

Add these canonical skills:

- `to-tickets`: turn approved work into independently verifiable vertical slices with acceptance criteria and blocker edges.
- `triage`: move incoming work through a compact, evidence-aware state model.
- `claim-ticket`: claim only an available frontier ticket before implementation begins.
- `work-frontier`: report open tickets that are ready, unclaimed, and unblocked.

Add matching explicit operator command wrappers, pack manifest entries, adapter catalog entries, install-fixture coverage, and contract tests.

## Configuration and Backends

Each consuming repository configures tracker behavior in `.agents/tracker.md`.

The file selects one backend and maps semantic roles to repository-specific labels or fields. Omitted configuration means the local backend. Configuration fields include backend, ready state, claim convention, completion convention, and blocker representation.

Two backends ship initially:

- Local Markdown: default backend. Tickets live in `.agents/tickets/` so they are durable, reviewable, and optionally committed.
- GitHub: opt-in backend. Native issue dependencies and assignee claims are used when available; documented body-field fallback applies otherwise.

Canonical skills describe semantic operations only. Backend guides own command syntax and storage representation. No canonical procedure contains GitHub CLI or API commands.

## Ticket Model

Every ticket contains a title, status, owner/claim field, blockers, outcome, acceptance criteria, and evidence.

Tickets are vertical slices: each completed ticket delivers an end-to-end behavior that can be demonstrated or verified independently. Wide refactors use explicit expand, migrate, and contract tickets instead of artificial vertical slices.

Blockers are directed edges. A ticket belongs to the frontier only when every blocker is complete, its state is `ready-for-agent`, and it has no active claim.

## State Model

Triage states are `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`.

Execution states are `claimed` and `done`. A claim records actor and UTC timestamp before work starts. Completion records concrete verification evidence before resolving or closing the ticket. Backend state mappings may combine these fields with labels, assignees, or issue state, but must preserve these meanings.

## Package Layout

```text
packs/tracker.yml
skills/
  to-tickets/SKILL.md
  triage/SKILL.md
  claim-ticket/SKILL.md
  work-frontier/SKILL.md
  tracker/
    ticket-schema.md
    state-model.md
    backends/local.md
    backends/github.md
commands/
  to-tickets.md
  triage.md
  claim-ticket.md
  work-frontier.md
```

## Verification

Tests prove that tracker pack declares intended skills, every adapter includes canonical sources, installer produces matching native layouts, and canonical skill files do not embed backend-specific `gh` or GitHub API commands.

Behavioral acceptance tests validate local ticket parsing for state, blockers, claims, and frontier selection. GitHub behavior remains guide-driven and is tested structurally without network credentials.

## Non-goals

- Linear or other hosted trackers.
- Automated tracker synchronization.
- A mandatory tracker for normal single-session work.
- Full historical out-of-scope knowledge base or wayfinding map workflow.
