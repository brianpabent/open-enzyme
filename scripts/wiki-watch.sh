#!/usr/bin/env bash
# wiki-watch.sh — watch wiki/ for human edits and trigger the two-pass doc
# sweep (wiki-update.sh → sweep-prompt.md).
#
# wiki/ is the primary research layer (docs/ was merged in April 2026, and
# the ai-analysis/ staging directory was curated into wiki/ alongside it).
#
# Cycles are prevented two ways: (1) the daemon commits at the end of each
# sweep, so self-writes during Pass 1 match HEAD by the time queued fswatch
# events fire; (2) the git-diff-HEAD filter below skips any path that already
# matches HEAD.
#
# Filters out changes that came from git (pull, checkout, reset, stash pop,
# merge, rebase, cherry-pick). Anything already in git history is assumed to
# have been synced by whoever committed it.
#
# Serializes concurrent syncs with flock so rapid-fire edits queue up instead
# of racing each other over git and the wiki/ tree.
#
# Usage:
#   ./scripts/wiki-watch.sh            # foreground (Ctrl+C to stop)
#   ./scripts/wiki-watch.sh --no-commit
#
# Typical deployment: installed as a launchd agent via install-watcher.sh so
# it runs at login.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

NO_COMMIT_FLAG=""
[[ "${1:-}" == "--no-commit" ]] && NO_COMMIT_FLAG="--no-commit"

LOCK_DIR="/tmp/open-enzyme-wiki-sync.lock.d"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

# Portable mutex using mkdir (atomic on POSIX). macOS doesn't ship flock.
# Waits up to $2 seconds (default 300) for the lock, retrying every 0.2s.
acquire_lock() {
  local dir="$1"
  local timeout="${2:-300}"
  local elapsed=0
  while ! mkdir "$dir" 2>/dev/null; do
    # Stale lock recovery: if holder PID no longer exists, remove the lock.
    if [[ -f "$dir/pid" ]]; then
      local holder
      holder="$(cat "$dir/pid" 2>/dev/null || true)"
      if [[ -n "$holder" ]] && ! kill -0 "$holder" 2>/dev/null; then
        log "removing stale lock (holder PID $holder no longer running)"
        rm -rf "$dir"
        continue
      fi
    fi
    sleep 0.2
    elapsed=$((elapsed + 1))
    if (( elapsed > timeout * 5 )); then
      log "lock acquisition timed out after ${timeout}s"
      return 1
    fi
  done
  echo "$$" > "$dir/pid"
}

release_lock() {
  rm -rf "$1"
}

if ! command -v fswatch &>/dev/null; then
  log "error: fswatch not found. install with: brew install fswatch"
  exit 1
fi

if ! command -v claude &>/dev/null; then
  log "error: claude CLI not found in PATH."
  exit 1
fi

log "watching wiki/ — human edits trigger two-pass sweep; git-driven changes are skipped"
log "  repo:    $REPO_ROOT"
log "  lock:    $LOCK_DIR"
[[ -n "$NO_COMMIT_FLAG" ]] && log "  mode:    --no-commit"

# Debounce state
LAST_PATH=""
LAST_TIME=0

# Only spin up fswatch on directories that exist
WATCH_DIRS=()
[[ -d "$REPO_ROOT/wiki" ]] && WATCH_DIRS+=("$REPO_ROOT/wiki")

if [[ ${#WATCH_DIRS[@]} -eq 0 ]]; then
  log "error: wiki/ does not exist under $REPO_ROOT"
  exit 1
fi

fswatch -r -e ".*" -i "\.md$" "${WATCH_DIRS[@]}" | while IFS= read -r CHANGED_PATH; do
  # Deletion or other non-file event → skip
  if [[ ! -f "$CHANGED_PATH" ]]; then
    continue
  fi

  REL_PATH="${CHANGED_PATH#"$REPO_ROOT/"}"

  # Debounce: same file within 5s → skip (editors often fire multiple events per save)
  NOW=$(date +%s)
  if [[ "$REL_PATH" == "$LAST_PATH" && $((NOW - LAST_TIME)) -lt 5 ]]; then
    continue
  fi
  LAST_PATH="$REL_PATH"
  LAST_TIME=$NOW

  # Skip if a git operation is in progress — we don't want to sync mid-conflict
  if [[ -f "$REPO_ROOT/.git/MERGE_HEAD" ]] \
     || [[ -f "$REPO_ROOT/.git/REBASE_HEAD" ]] \
     || [[ -d "$REPO_ROOT/.git/rebase-merge" ]] \
     || [[ -d "$REPO_ROOT/.git/rebase-apply" ]] \
     || [[ -f "$REPO_ROOT/.git/CHERRY_PICK_HEAD" ]]; then
    log "skip: $REL_PATH (git merge/rebase/cherry-pick in progress)"
    continue
  fi

  # Skip if the file matches HEAD. That means the change came from git itself
  # (pull, checkout, reset, stash pop) — not a human edit. Already-in-git
  # content is assumed to have been synced by whoever committed it.
  if git -C "$REPO_ROOT" diff --quiet HEAD -- "$REL_PATH" 2>/dev/null; then
    log "skip: $REL_PATH (matches HEAD — git operation, not a human edit)"
    continue
  fi

  log "sync: $REL_PATH"

  # Serialize via mkdir-based mutex (portable; macOS has no flock by default).
  # Blocking acquire with stale-lock recovery — if another sync is running, wait.
  if ! acquire_lock "$LOCK_DIR"; then
    log "sync SKIPPED for $REL_PATH (could not acquire lock)"
    continue
  fi
  trap 'release_lock "$LOCK_DIR"' EXIT INT TERM
  if "$REPO_ROOT/scripts/wiki-update.sh" "$REL_PATH" $NO_COMMIT_FLAG; then
    log "sync done: $REL_PATH"
  else
    log "sync FAILED for $REL_PATH (exit $?)"
  fi
  release_lock "$LOCK_DIR"
  trap - EXIT INT TERM
done
