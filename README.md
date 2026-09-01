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
- `delivery`: deliberate workflow skills and operator commands.
- `architecture`: domain modeling and module depth.
- `research`: source-grounded decision research, opt-in.
- `tracker`: opt-in ticket workflow, separate from `delivery`.

The tracker pack uses local Markdown tickets by default. Configure tracker
behavior in `.agents/tracker.md`; local tickets live in `.agents/tickets/` and
can be committed with the project. Use the GitHub backend only when
`.agents/tracker.md` explicitly contains `Backend: github`.

Install the tracker pack into a project-local Codex layout with:

```sh
python scripts/install_adapter.py --harness codex --pack tracker --destination .
```

Commands are explicit operator entry points. Skills contain canonical procedure bodies. Adapters must reference canonical skills and must not fork prose.

## Harnesses

Claude Code, Codex, Pi, OpenCode, and Qwen catalogs live under `adapters/`. Installer copies canonical bodies unchanged to documented native project paths. OpenCode additionally receives explicit `commands/` wrappers; commands are operator-invoked, not autoinvoked. Qwen receives `.qwen/skills` layout.

## Updating sources

`sources.lock.yml` pins upstream URL, commit, license, and retrieval date. Upstream updates are manual diff-and-curate changes: update lock, update provenance, change canonical text deliberately, run tests. Never auto-sync.

## Release

Use SemVer tags. Current release line: `v0.2.0`. Test in clean harness fixtures beside stock installs before publishing. Migrate repositories one at time; remove stock installs only after recorded migration evidence.

Portable procedure prose ends at the public catalog boundary. Repository-specific facts, paths, policy, and operator routes belong in a private overlay maintained by the consuming repository after it selects the matching public skill ID. Public updates stay curated; this repository does not auto-sync private overlays. Before removing stock skill sets, run and retain [Codex and Claude migration evidence](docs/migration/codex-claude-smoke-test.md).

MIT. See [NOTICE](NOTICE) and [PROVENANCE.md](PROVENANCE.md).
