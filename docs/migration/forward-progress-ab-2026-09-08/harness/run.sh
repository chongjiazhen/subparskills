#!/usr/bin/env bash
# A/B harness for ticket 001. Usage: run.sh <model-id> <round-tag> [scenario...]
set -u
S="$(cd "$(dirname "$0")" && pwd)"
MODEL="$1"; ROUND="$2"; shift 2
SCEN=("$@"); [ ${#SCEN[@]} -eq 0 ] && SCEN=(s1 s2 s3 c1 c2 c3)
OUT="$S/results/$ROUND"; mkdir -p "$OUT"
for sc in "${SCEN[@]}"; do
  for arm in ${ARMS:-A B}; do
    CELL="$S/cells/$ROUND/$sc-$arm"
    rm -rf "$CELL"; mkdir -p "$CELL"
    cp -r "$S/fixtures/$sc/." "$CELL/"
    cp -r "$S/arms/$arm/skills" "$CELL/skills"
    P="$OUT/$sc-$arm.prompt.txt"
    cat "$S/prompts/preamble.txt" "$S/prompts/$sc.txt" > "$P"
    echo "=== $ROUND $sc arm $arm ($MODEL) start $(date -u +%FT%TZ)"
    ( cd "$CELL" && HOME="$S/home" USERPROFILE="$(cygpath -w "$S/home")" \
        CLAUDE_CONFIG_DIR="$S/cfg" \
        timeout 900 claude -p --model "$MODEL" --dangerously-skip-permissions \
        < "$P" ) > "$OUT/$sc-$arm.transcript.txt" 2>&1
    echo "   rc=$? bytes=$(wc -c < "$OUT/$sc-$arm.transcript.txt")"
    ( cd "$CELL" && git init -q . 2>/dev/null ) >/dev/null 2>&1
    diff -ru "$S/fixtures/$sc" "$CELL" --exclude=skills --exclude=.git \
      > "$OUT/$sc-$arm.filediff.txt" 2>&1
  done
done
echo "done $(date -u +%FT%TZ)"
