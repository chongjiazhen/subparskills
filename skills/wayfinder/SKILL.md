---
name: wayfinder
description: Use when work is too big for one session and wrapped in fog - chart it as a map of decision tickets on the tracker, then resolve one per session until the way is clear.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: tracker, source: merge, invocation: user }
---

# Wayfinder

Wayfinding is planning, not doing: each ticket resolves a decision, and the map is done when nothing is left to decide before someone executes. The pull to just do the work signals the edge of the map - time to hand off. Read `.agents/tracker.md` and the selected guide in `../tracker/backends/` before any backend operation; defaults come from the local backend guide.

## The map

One tracker ticket, tagged as the wayfinder map, is the canonical artifact; decision tickets are its children using the shared template in `../tracker/ticket-schema.md`, each sized to one session and carrying one question whose resolution is a decision. The map is an index, never a store: a decision lives in exactly one place - its ticket - and the map gists and links it. Map body sections:

- Destination: what reaching the end looks like (a spec, a locked decision, a change made in place). One or two lines; every session orients to it first. The destination fixes the scope.
- Notes: domain, skills every session should consult, standing preferences.
- Decisions so far: one line per closed ticket - title, link, one-line gist of the answer.
- Not yet specified: the fog of war - decisions you can tell are coming but cannot yet phrase sharply. Ticket when the question is precise now, even if blocked; fog when it is not. Never pre-slice fog into ticket-sized pieces.
- Out of scope: work consciously ruled beyond the destination, with why. It never graduates; a mis-scoped ticket gets closed and one line here, not a resolution.

Blocker edges use the tracker's mapping from `Blocked by`; the frontier is the open, unblocked, unclaimed children. In everything the human reads, refer to tickets by title, never bare identifiers.

## Ticket types

Each ticket is human-in-the-loop (resolved only by live exchange - never answer the human's side yourself) or agent-driven:

- research (agent-driven): surface a fact a decision waits on, via the research skill; link findings from the ticket.
- prototype (human-in-the-loop): raise discussion fidelity with a cheap concrete artifact, via the prototype skill; link it as an asset.
- grilling (human-in-the-loop, the default): conversation, via the grill and domain-model skills.
- task: manual work that must happen before a decision can be made - provisioning, access, moving data so its shape can be seen. The one type that does rather than decides; it earns its place by unblocking a decision. Resolution records what was done and the facts later tickets depend on.

## Chart the map

1. Name the destination first (grill plus domain-model): the spec, decision, or change this effort finds its way to.
2. Grill again breadth-first across the whole space, surfacing open decisions and first takeable steps. No fog surfaced means no map needed - stop and ask the user.
3. Create the map: destination and notes filled, decisions empty, fog sketched into Not yet specified.
4. Create the tickets you can specify now, then wire blocker edges in a second pass.
5. Dispatch workers for research tickets; charting hand-resolves nothing else. Stop.

## Work the map

Never resolve more than one non-research ticket per session.

1. Load the map body, not every ticket.
2. Choose the ticket the user named, else the first frontier ticket. Claim it before any work - other sessions may work the tracker concurrently, and the claim is what makes them skip it.
3. Resolve it, zooming into related or closed tickets on demand and invoking whatever skills the map's Notes name (default: grill plus domain-model).
4. Record: post the answer as a resolution comment, close the ticket, append the one-line gist to Decisions so far.
5. Update the map: create newly surfaced tickets and wire their edges; graduate fog the answer made specifiable, clearing it from Not yet specified; rule out-of-scope what the answer exposed as past the destination; fix or drop tickets the decision invalidated.
