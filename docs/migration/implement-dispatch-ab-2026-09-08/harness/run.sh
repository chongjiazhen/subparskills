#!/usr/bin/env bash
# A/B harness: implement-dispatch. Usage: run.sh <model-id> <round-tag> [scenario...]
set -u
S="$(cd "$(dirname "$0")" && pwd)"
MODEL="$1"; ROUND="$2"; shift 2
SCEN=("$@"); [ ${#SCEN[@]} -eq 0 ] && SCEN=(m1 o1)
OUT="$S/results/$ROUND"; mkdir -p "$OUT"
for sc in "${SCEN[@]}"; do
  for arm in ${ARMS:-A B}; do
    CELL="$S/cells/$ROUND/$sc-$arm"
    rm -rf "$CELL"; mkdir -p "$CELL"
    cp -a "$S/fixtures/$sc/." "$CELL/"
    cp -r "$S/arms/$arm/skills" "$CELL/skills"
    P="$OUT/$sc-$arm.prompt.txt"
    cat "$S/prompts/preamble.txt" "$S/prompts/$sc.txt" > "$P"
    echo "=== $ROUND $sc arm $arm ($MODEL) start $(date -u +%FT%TZ)"
    ( cd "$CELL" && HOME="$S/home" USERPROFILE="$(cygpath -w "$S/home")" \
        CLAUDE_CONFIG_DIR="$S/cfg" \
        timeout 1500 claude -p --model "$MODEL" --dangerously-skip-permissions \
        --output-format stream-json --verbose \
        < "$P" ) > "$OUT/$sc-$arm.stream.jsonl" 2>"$OUT/$sc-$arm.stderr.txt"
    echo "   rc=$? lines=$(wc -l < "$OUT/$sc-$arm.stream.jsonl") end $(date -u +%FT%TZ)"
    ( cd "$CELL" && git log --oneline feat/v2 ) > "$OUT/$sc-$arm.gitlog.txt" 2>&1
    ( cd "$CELL" && git diff --stat main..feat/v2 && git status -s ) > "$OUT/$sc-$arm.gitstat.txt" 2>&1
    ( cd "$CELL" && python -m pytest -q 2>&1 | tail -3 ) > "$OUT/$sc-$arm.pytest.txt"
  done
done
echo "done $(date -u +%FT%TZ)"
