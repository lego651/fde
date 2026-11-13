#!/bin/bash
# Claude Code Stop hook: block "I'm done" while the FDE doc center is out of sync.
# Wired in ~/.claude/settings.json. Only acts in sessions that touched this repo.
# Exit 2 + stderr = Claude must keep working and sees the message.
REPO="$(cd "$(dirname "$0")/.." && pwd)"
INPUT="$(cat)"
field() { printf '%s' "$INPUT" | /usr/bin/python3 -c "import json,sys; print(json.load(sys.stdin).get('$1') or '')" 2>/dev/null; }

[ "$(field stop_hook_active)" = "True" ] && exit 0          # already blocked once this turn; don't loop
CWD="$(field cwd)"; TRANSCRIPT="$(field transcript_path)"
case "$CWD" in "$REPO"*) ;; *)
  [ -n "$TRANSCRIPT" ] && grep -qF "$REPO/" "$TRANSCRIPT" 2>/dev/null || exit 0 ;;
esac

cd "$REPO" || exit 0
PROBLEMS=""
CHECK="$(/usr/bin/python3 scripts/build_docs.py --all --check 2>&1 >/dev/null)" || PROBLEMS+="$CHECK"$'\n'

# Uncommitted work in client folders and tooling (root *-preview.html files are scratch and ignored)
DIRTY="$(git status --porcelain -- $(for f in */docs.json; do dirname "$f"; done) scripts .claude CLAUDE.md _config.yml index.html 2>/dev/null)"
[ -n "$DIRTY" ] && PROBLEMS+="not committed:"$'\n'"$DIRTY"$'\n'

git fetch -q origin main 2>/dev/null
AHEAD="$(git rev-list --count origin/main..main 2>/dev/null || echo 0)"
[ "$AHEAD" != "0" ] && PROBLEMS+="main is $AHEAD commit(s) ahead of origin/main (not pushed)"$'\n'

[ -z "$PROBLEMS" ] && exit 0
cat >&2 <<MSG
FDE doc center rule (skill: fde-docs) is not satisfied:
$PROBLEMS
Fix it before finishing: register client docs in <Client>/docs.json, run
  python3 scripts/build_docs.py <Client>
then commit and push main, and confirm the live URL returns 200.
If the user explicitly said not to publish yet, tell them what is unpublished and stop.
MSG
exit 2
