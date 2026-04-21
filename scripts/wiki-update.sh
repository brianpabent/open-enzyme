#!/usr/bin/env bash
# wiki-update.sh — LLM-driven wiki sync for a new or changed doc
#
# Usage:
#   ./scripts/wiki-update.sh docs/some-doc.md
#   ./scripts/wiki-update.sh docs/some-doc.md --no-commit
#
# Requires: claude CLI (Claude Code) in PATH

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# ── Args ──────────────────────────────────────────────────────────────────────
DOC="${1:-}"
NO_COMMIT=false
for arg in "$@"; do
  [[ "$arg" == "--no-commit" ]] && NO_COMMIT=true
done

if [[ -z "$DOC" ]]; then
  echo "Usage: $0 <doc-path> [--no-commit]"
  echo "  e.g. $0 docs/new-compound.md"
  exit 1
fi

# Normalize: strip leading ./ and repo root prefix
DOC="${DOC#./}"
DOC="${DOC#"$REPO_ROOT/"}"

if [[ ! -f "$DOC" ]]; then
  echo "Error: '$DOC' not found (working dir: $REPO_ROOT)"
  exit 1
fi

if [[ "$DOC" != docs/* ]]; then
  echo "Error: path must be under docs/ — got: $DOC"
  exit 1
fi

DOC_BASENAME="$(basename "$DOC")"
echo "Open Enzyme wiki sync"
echo "  doc:  $DOC"
echo "  root: $REPO_ROOT"
[[ "$NO_COMMIT" == true ]] && echo "  mode: --no-commit (review before committing)"
echo ""

# ── Commit instructions ───────────────────────────────────────────────────────
if [[ "$NO_COMMIT" == true ]]; then
  COMMIT_INSTRUCTIONS="Do NOT commit. Leave all changes staged/unstaged for human review."
else
  COMMIT_INSTRUCTIONS="After all wiki edits are complete, commit with:
  - If \`$DOC\` is new (untracked by git): \`git add \"$DOC\" wiki/ && git commit -m \"docs+wiki: add $DOC_BASENAME and sync wiki\"\`
  - If \`$DOC\` already exists in git: \`git add wiki/ && git commit -m \"wiki: sync after $DOC_BASENAME update\"\`"
fi

# ── Prompt ────────────────────────────────────────────────────────────────────
PROMPT="You are performing an automated wiki sync for the Open Enzyme research project.

A doc was just created or significantly updated: \`$DOC\`

Your job is to propagate changes from this doc into the wiki/ folder, following the Doc Sweep Rule in CLAUDE.md exactly. Work through these steps in order:

---

## Step 1 — Read the changed doc

Read \`$DOC\` in full. Note:
- The YAML frontmatter \`related:\` field
- All concepts, compounds, organisms, mechanisms, and disease areas mentioned
- All new claims and their evidence levels

---

## Step 2 — Inventory the current wiki

Read \`wiki/INDEX.md\` — all existing concept pages.
Read \`wiki/GRAPH.md\` — current concept relationships.

---

## Step 3 — Identify affected wiki pages

A wiki page is affected if it:
a) Is named in the doc's YAML \`related:\` field
b) Covers a concept, organism, compound, mechanism, or disease mentioned in the doc

List every affected page before proceeding.

---

## Step 4 — Update each affected wiki page

For each page identified above:
1. Read its current content
2. Add any information from \`$DOC\` that is missing or underdeveloped
3. After each new sentence or claim you add, append \`(source: $DOC_BASENAME)\` inline
4. If you find a contradiction between the new doc and existing wiki content, add:
   \`> ⚠️ CONTRADICTION: [describe — doc A says X; doc B says Y — needs resolution]\`
5. Do NOT remove existing content unless it is directly contradicted and provably wrong

---

## Step 5 — Create new concept pages (if needed)

If \`$DOC\` introduces concepts not yet covered in the wiki:
- Create \`wiki/[concept-slug].md\`
- Follow the format of existing wiki pages: no frontmatter, short intro paragraph, H2 sections, [[wiki-links]]
- Append \`(source: $DOC_BASENAME)\` after all new claims
- Add [[wiki-links]] back to related existing pages

---

## Step 6 — Update wiki/INDEX.md

Add any new concept pages under the appropriate category section.
Format: \`- [[concept-slug]] — one-line description\`

---

## Step 7 — Update wiki/GRAPH.md

- Add Mermaid nodes for any new concepts
- Add edges for new relationships found in \`$DOC\`
- Label edges with type: produces, inhibits, activates, requires, synergizes, degrades, etc.
- Ensure all new nodes appear in at least one subgraph

---

## Step 8 — Commit

$COMMIT_INSTRUCTIONS

---

## Standards (from CLAUDE.md — non-negotiable)

- Audience is PhD scientists. No marketing language, no overselling.
- Always tag evidence: (Clinical Trial), (Animal Model), (In Vitro), (Mechanistic Extrapolation)
- Use [[wiki-links]] for all cross-references between concept pages
- Cross-references must be bidirectional: if page A links to B, then B should link back to A
- Err toward MORE updates, not fewer — if uncertain whether a page is affected, update it

Begin with Step 1 now."

# ── Run ───────────────────────────────────────────────────────────────────────
exec claude -p "$PROMPT"
