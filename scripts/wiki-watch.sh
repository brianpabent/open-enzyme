#!/usr/bin/env bash
# wiki-watch.sh — continuous file watcher that triggers wiki-update.sh
#
# Watches docs/ for .md file changes and auto-runs the wiki sync.
# Requires: fswatch (brew install fswatch)
#
# Usage:
#   ./scripts/wiki-watch.sh           # watch docs/, auto-commit
#   ./scripts/wiki-watch.sh --no-commit

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

NO_COMMIT_FLAG=""
[[ "${1:-}" == "--no-commit" ]] && NO_COMMIT_FLAG="--no-commit"

if ! command -v fswatch &>/dev/null; then
  echo "Error: fswatch not found. Install with: brew install fswatch"
  exit 1
fi

if ! command -v claude &>/dev/null; then
  echo "Error: claude CLI not found. Install Claude Code first."
  exit 1
fi

echo "Watching docs/ for changes. Press Ctrl+C to stop."
echo ""

# Track recent updates to avoid double-firing on rapid saves
LAST_PATH=""
LAST_TIME=0

fswatch -r -e ".*" -i "\.md$" "$REPO_ROOT/docs/" | while IFS= read -r CHANGED_PATH; do
  # Debounce: ignore if same file within 5 seconds
  NOW=$(date +%s)
  if [[ "$CHANGED_PATH" == "$LAST_PATH" && $((NOW - LAST_TIME)) -lt 5 ]]; then
    continue
  fi
  LAST_PATH="$CHANGED_PATH"
  LAST_TIME=$NOW

  # Get path relative to repo root
  REL_PATH="${CHANGED_PATH#"$REPO_ROOT/"}"

  echo "[$(date '+%H:%M:%S')] Change detected: $REL_PATH"
  echo "  Starting wiki sync..."

  # Run sync (foreground so output is visible; Ctrl+C will interrupt it)
  if "$REPO_ROOT/scripts/wiki-update.sh" "$REL_PATH" $NO_COMMIT_FLAG; then
    echo "  Wiki sync complete."
  else
    echo "  Wiki sync failed (exit $?). Check output above."
  fi
  echo ""
done
