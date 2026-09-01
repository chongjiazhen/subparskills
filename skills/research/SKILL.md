---
name: research
description: Use when a decision needs current external facts, API or library guidance, source verification, or a cited research brief.
license: MIT
compatibility: Any Agent Skills-compatible harness.
metadata: { pack: research, source: merge }
---

# Research

## Procedure

1. State decision question, scope, target versions or dates, evidence needed, and meaning of “current” before searching.
2. Prefer primary sources: official documentation, specifications, source code, release notes, package metadata, and first-party advisories. Use secondary sources only for discovery or clearly labeled context.
3. Record each material claim with direct source, retrieval time, source version or date, and confidence. Separate source fact from inference.
4. Save one UTC-dated Markdown brief in repository research-notes convention. If none exists, use `docs/research/YYYY-MM-DD-<topic>.md`.
5. End with decision-relevant findings, open questions, assumptions, and validation needed. Research does not authorize code, configuration, or external state changes.
