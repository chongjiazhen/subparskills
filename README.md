# Subparskills

Portable, curated Agent Skills framework. Canonical skills contain reusable engineering discipline. Harness and personal policy stay outside this repository.

## Install

Primary:

```sh
npx skills add chongjiazhen/subparskills
```

Manual fallback:

```sh
git clone https://github.com/chongjiazhen/subparskills.git
```

`npx skills` discovers canonical `skills/` directly. For a native project-local harness layout, run:

```sh
python scripts/install_adapter.py --harness codex --pack core --destination .
```

Replace `codex` with `claude-code`, `pi`, `opencode`, or `qwen`; omit `--pack` for full catalog. Claude Code can also load this repository as plugin through `.claude-plugin/plugin.json`.

## Packs

- `core`: `diagnose`, `tdd`, `verify`, `review`.
- `delivery`: deliberate workflow skills, operator commands, a manual router, and opt-in productivity disciplines such as prompt repair and agent-facing writing.
- `architecture`: domain modeling and module depth.
- `research`: source-grounded decision research, opt-in.
- `tracker`: opt-in ticket workflow, separate from `delivery`.

The tracker pack needs zero setup: tickets are local Markdown files at
`.agents/tickets/`, committed with the project so claims and history survive
sessions and sync across machines. No configuration file is required - absent
config, every skill uses the local backend defaults. Hosted backends are a
power-user opt-in with no setup flow: create `.agents/tracker.md` containing
`Backend: github` and the mappings described in
`skills/tracker/backends/github.md`.

Install the tracker pack into a project-local Codex layout with:

```sh
python scripts/install_adapter.py --harness codex --pack tracker --destination .
```

Commands are explicit operator entry points. Skills contain canonical procedure bodies. Adapters must reference canonical skills and must not fork prose.

## Harnesses

Claude Code, Codex, Pi, OpenCode, and Qwen catalogs live under `adapters/`. Installer copies canonical bodies unchanged to documented native project paths. OpenCode additionally receives explicit `commands/` wrappers; commands are operator-invoked, not autoinvoked. Qwen receives `.qwen/skills` layout.

## Updating sources

`sources.lock.yml` pins upstream URL, commit, license, and retrieval date. Upstream updates are manual diff-and-curate changes: update lock, update provenance, change canonical text deliberately, run tests. Never auto-sync.

Two helper gates support that manual flow:

- `python scripts/curate-sources.py --upstream obra-superpowers=/path/to/superpowers --upstream mattpocock-skills=/path/to/skills --check` reports upstream capability deltas against the pinned commits and fails if provenance decisions are still missing.
- `python scripts/verify-release.py --evidence .scratch/release-verification.md` runs the release gate, writes dated evidence only at that explicit path, and leaves publishing as a separate explicit step.

## Release

Use SemVer tags. Current release line: `v0.2.0`. Test in clean harness fixtures beside stock installs before publishing. Migrate repositories one at time; remove stock installs only after recorded migration evidence.

Portable procedure prose ends at the public catalog boundary. Repository-specific facts, paths, policy, and operator routes belong in a private overlay maintained by the consuming repository after it selects the matching public skill ID. Public updates stay curated; this repository does not auto-sync private overlays. Before removing stock skill sets, run and retain [Codex and Claude migration evidence](docs/migration/codex-claude-smoke-test.md).

MIT. See [NOTICE](NOTICE) and [PROVENANCE.md](PROVENANCE.md).
