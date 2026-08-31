# Language

Use these terms consistently.

- **Module**: unit with interface and implementation.
- **Interface**: all caller knowledge, including invariants, ordering, errors, configuration, and performance behavior.
- **Seam**: place behavior can change without editing callers.
- **Adapter**: concrete implementation at seam.
- **Depth**: leverage delivered through interface.
- **Locality**: change and knowledge concentrated in one place.

Depth belongs to interface, not implementation size. Deletion test asks whether
removing module deletes complexity or redistributes it across callers. One
adapter is hypothetical seam; two justified adapters make seam real.
