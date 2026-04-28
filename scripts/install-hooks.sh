#!/usr/bin/env bash
#
# scripts/install-hooks.sh — point git at .githooks/ for this clone.
#
# Run once after cloning. Idempotent: re-running just re-applies the
# config and chmods. The hooks themselves are tracked in .githooks/
# under version control; this script only wires git's hook lookup.
#
# Hooks installed:
#   commit-msg   — enforces sweep-automation commit-message conventions
#                  (see scripts/SWEEP-ARCHITECTURE.md §"Hooks for
#                  enforcement"). Refuses [skip-wiki-sweep] on hand
#                  authored wiki commits and refuses sweep-N-... prefix
#                  on commits authored by anyone other than
#                  github-actions[bot].
#

set -euo pipefail

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

if [[ ! -d .githooks ]]; then
  echo "ERROR: .githooks/ not found in $ROOT" >&2
  exit 1
fi

git config core.hooksPath .githooks
chmod +x .githooks/commit-msg

echo "✓ Hooks installed."
echo "  core.hooksPath = $(git config core.hooksPath)"
echo "  Active hooks:"
ls -1 .githooks/ | grep -v '\.md$' | sed 's/^/    /'
echo ""
echo "  To uninstall: git config --unset core.hooksPath"
