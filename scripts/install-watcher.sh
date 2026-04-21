#!/usr/bin/env bash
# install-watcher.sh — install wiki-watch as a launchd agent (macOS).
#
# After install, the watcher runs at login, restarts on crash, and logs to
# scripts/wiki-watch.log.
#
# Usage:
#   ./scripts/install-watcher.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLIST_LABEL="com.openenzyme.wiki-watch"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_LABEL}.plist"
WATCH_SCRIPT="$REPO_ROOT/scripts/wiki-watch.sh"
LOG_FILE="$REPO_ROOT/scripts/wiki-watch.log"

# ── Preflight ─────────────────────────────────────────────────────────────────
if [[ "$(uname)" != "Darwin" ]]; then
  echo "error: launchd is macOS-only. this install script only works on macOS."
  echo "on linux, run wiki-watch.sh under systemd user or tmux/screen."
  exit 1
fi

if ! command -v fswatch &>/dev/null; then
  echo "error: fswatch not found."
  echo "install with: brew install fswatch"
  exit 1
fi

CLAUDE_BIN="$(command -v claude || true)"
if [[ -z "$CLAUDE_BIN" ]]; then
  echo "error: claude CLI not found in PATH."
  echo "install Claude Code first (https://docs.claude.com/claude-code)."
  exit 1
fi

if [[ ! -x "$WATCH_SCRIPT" ]]; then
  echo "error: $WATCH_SCRIPT is not executable."
  exit 1
fi

# Build PATH for the launchd job. launchd starts with a minimal PATH, so we
# have to include everywhere the required binaries live.
FSWATCH_BIN="$(command -v fswatch)"
GIT_BIN="$(command -v git)"
LAUNCH_PATH="$(dirname "$CLAUDE_BIN"):$(dirname "$FSWATCH_BIN"):$(dirname "$GIT_BIN"):/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin"

mkdir -p "$HOME/Library/LaunchAgents"

# ── Write plist ───────────────────────────────────────────────────────────────
cat > "$PLIST_PATH" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_LABEL}</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${WATCH_SCRIPT}</string>
    </array>

    <key>WorkingDirectory</key>
    <string>${REPO_ROOT}</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>${LAUNCH_PATH}</string>
        <key>HOME</key>
        <string>${HOME}</string>
    </dict>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>${LOG_FILE}</string>

    <key>StandardErrorPath</key>
    <string>${LOG_FILE}</string>
</dict>
</plist>
EOF

# ── Load (idempotent) ─────────────────────────────────────────────────────────
# Unload first in case it was already loaded with an older plist
launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH"

echo "wiki-watch launchd agent installed."
echo "  label:  $PLIST_LABEL"
echo "  plist:  $PLIST_PATH"
echo "  log:    $LOG_FILE"
echo ""
echo "status:"
launchctl list | grep "$PLIST_LABEL" || echo "  (not visible in launchctl list — check $LOG_FILE)"
echo ""
echo "useful commands:"
echo "  tail -f $LOG_FILE                      # watch activity"
echo "  launchctl list | grep $PLIST_LABEL     # check status"
echo "  ./scripts/uninstall-watcher.sh         # stop and remove"
