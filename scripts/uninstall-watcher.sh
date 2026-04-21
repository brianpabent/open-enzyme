#!/usr/bin/env bash
# uninstall-watcher.sh — stop and remove the wiki-watch launchd agent.

set -euo pipefail

PLIST_LABEL="com.openenzyme.wiki-watch"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_LABEL}.plist"

if [[ ! -f "$PLIST_PATH" ]]; then
  echo "not installed (no plist at $PLIST_PATH)"
  exit 0
fi

launchctl unload "$PLIST_PATH" 2>/dev/null || true
rm "$PLIST_PATH"

echo "wiki-watch launchd agent uninstalled."
echo "(logs preserved at scripts/wiki-watch.log — delete manually if desired)"
