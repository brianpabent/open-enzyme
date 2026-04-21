#!/usr/bin/env bash
# wiki-update.sh — run a two-pass doc sweep for a changed file.
#
# Pass 1 propagates the change into affected docs/wiki pages.
# Pass 2 synthesizes new connections across the whole corpus and writes
# ai-analysis/SYNTHESIS-[date].md. The daemon commits once at the end.
#
# The actual sweep logic lives in scripts/sweep-prompt.md. This script just
# concatenates that prompt with trigger metadata and hands it to claude.
#
# Usage:
#   ./scripts/wiki-update.sh docs/some-doc.md
#   ./scripts/wiki-update.sh ai-analysis/SYNTHESIS-2026-04-21.md
#   ./scripts/wiki-update.sh docs/some-doc.md --no-commit
#
# Requires: claude CLI (Claude Code) in PATH

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PROMPT_FILE="$REPO_ROOT/scripts/sweep-prompt.md"

# ── Args ──────────────────────────────────────────────────────────────────────
DOC=""
NO_COMMIT=false
for arg in "$@"; do
  case "$arg" in
    --no-commit) NO_COMMIT=true ;;
    -*)          echo "unknown flag: $arg" >&2; exit 2 ;;
    *)           [[ -z "$DOC" ]] && DOC="$arg" ;;
  esac
done

if [[ -z "$DOC" ]]; then
  echo "Usage: $0 <path> [--no-commit]" >&2
  echo "  e.g. $0 docs/new-compound.md" >&2
  exit 1
fi

# Normalize path (strip leading ./ and repo prefix)
DOC="${DOC#./}"
DOC="${DOC#"$REPO_ROOT/"}"

if [[ ! -f "$DOC" ]]; then
  echo "error: '$DOC' not found (repo root: $REPO_ROOT)" >&2
  exit 1
fi

# Only accept files under the knowledge-base roots
case "$DOC" in
  docs/*|wiki/*|ai-analysis/*) ;;
  *)
    echo "error: path must be under docs/, wiki/, or ai-analysis/ — got: $DOC" >&2
    exit 1
    ;;
esac

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "error: prompt template not found: $PROMPT_FILE" >&2
  exit 1
fi

# ── Build prompt ──────────────────────────────────────────────────────────────
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
COMMIT_FLAG="yes"
[[ "$NO_COMMIT" == true ]] && COMMIT_FLAG="no"

echo "Open Enzyme doc sweep"
echo "  file:   $DOC"
echo "  time:   $TIMESTAMP"
echo "  commit: $COMMIT_FLAG"
echo ""

# Concatenate sweep-prompt.md with trigger metadata the prompt reads at the end.
PROMPT="$(cat "$PROMPT_FILE")

---

TRIGGER: File changed: $DOC at $TIMESTAMP
commit=$COMMIT_FLAG"

# ── Run ───────────────────────────────────────────────────────────────────────
exec claude -p "$PROMPT"
