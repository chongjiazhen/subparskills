"""Summarise one stream.jsonl cell: top-level Agent dispatches, their briefs, final text."""
import json, sys, io, os
sys.stdout.reconfigure(encoding="utf-8")

for path in sys.argv[1:]:
    print("#####", os.path.basename(path))
    dispatches, tools, final, sub_tools = [], {}, "", {}
    for line in io.open(path, encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = ev.get("type")
        if t == "assistant":
            parent = ev.get("parent_tool_use_id")
            for blk in ev.get("message", {}).get("content", []):
                if blk.get("type") != "tool_use":
                    continue
                name = blk.get("name")
                if parent:
                    sub_tools[name] = sub_tools.get(name, 0) + 1
                    continue
                tools[name] = tools.get(name, 0) + 1
                if name in ("Agent", "Task"):
                    inp = blk.get("input", {})
                    dispatches.append((inp.get("description", ""), inp.get("subagent_type", ""),
                                       (inp.get("prompt", "") or "")[:300].replace("\n", " ")))
        elif t == "result":
            final = ev.get("result", "") or ""
            print("cost_usd", ev.get("total_cost_usd"), "turns", ev.get("num_turns"),
                  "duration_ms", ev.get("duration_ms"), "subtype", ev.get("subtype"))
    print("top-level tools:", tools)
    print("subagent tools:", sub_tools)
    print("AGENT DISPATCHES:", len(dispatches))
    for i, (d, st, p) in enumerate(dispatches, 1):
        print(f"  {i}. [{st}] {d} :: {p}")
    print("--- final text ---")
    print(final[:3000])
    print()
