You are running **Pass 1** of the Open Enzyme sweep — propagation only. The TRIGGER block at the end of this prompt names the changed file(s).

**Read `CLAUDE.md` first** for evidence-level standards, cross-referencing rules, and the Doc Sweep Rule.

**Pass 1 only.** Propagate findings from the trigger files across the wiki. Do NOT do Pass 2 (synthesis) — DeepSeek V4-Pro does that in the next job. Do NOT modify `wiki/synthesis.md`. Do NOT log to `logs/sweep-log.md`.

---

## Knowledge-base layout (read-and-write)

- `wiki/*.md` — research library. Edit these.
- `wiki/GRAPH.md` — Mermaid concept graph. Update when concepts/relationships change.
- `wiki/hypotheses/*.md` — committed hypothesis cards (see `wiki/linter-design.md`). Read for context; don't edit unless trigger explicitly affects a hypothesis card.
- `index.md` (repo root) — dashboard. Update when new wiki page is created or thesis shifts.
- `mkdocs.yml` — published-site nav. Update when a new wiki page is created (per Pass 1 step 4 below).

## Read-only

- `wiki/synthesis.md` — Pass 3 (Claude review) writes to it. Hands off.
- `reference/*`, `*.html`, `CLAUDE.md`, `README.md`, `scripts/*`, `.claude/*`, `.obsidian/*`, `.git/*`, `abent-family-health/*` — never modify.

---

## Pass 1 protocol

1. **Read the trigger file(s).** Extract findings, claims, concepts, evidence levels. When multiple trigger files are present, treat them as a single batch.

2. **Build an impact list.** Grep across `wiki/` for the concept names, compounds, organisms, and mechanisms in the trigger file(s). List every affected page before editing.

3. **Update each affected `wiki/*.md` page:**
   - Inline rewrite of contradicted claims; don't append "see also" footnotes
   - Tag every new or revised claim with evidence level: `(Clinical Trial)`, `(Animal Model)`, `(In Vitro)`, `(Mechanistic Extrapolation)`
   - Inline provenance: `(source: <trigger-filename>)`
   - If the trigger contradicts existing content and resolution is ambiguous, flag inline — do NOT silently overwrite:
     `> ⚠️ CONTRADICTION: <page A says X; trigger says Y — needs resolution>`
   - Standard markdown links `[text](./path.md)`, not `[[wiki-links]]`

4. **Create new wiki pages** if a trigger file introduces a concept not yet in `wiki/`:
   - YAML frontmatter (`title`, `date`, `tags`, optionally `related`, `sources`)
   - Add an entry under the most appropriate section in `mkdocs.yml` (Vision & Strategy / Gout & Uricase / NLRP3 & Inflammation / Koji & Digestive Enzymes / Organisms & Engineering / Delivery & Barrier / Compounds & Peptides / Self-Experiment & Validation / Tools & Reference). Format: `    - <Display Title>: <filename>.md`
   - Add an entry to `index.md` under the corresponding section
   - Without these two, the page renders as orphaned

5. **Update `wiki/GRAPH.md`** for new concepts/relationships. Add Mermaid nodes/edges; label edge types (produces / inhibits / activates / requires / synergizes / degrades). **No HTML in node labels** (breaks Obsidian).

6. **Update `index.md`** if a new wiki page was created or if a meaningful status shift happened (platform thesis, cheapest-experiments). Conservative — don't rewrite the dashboard for small changes. `index.md` is the in-repo dashboard; `mkdocs.yml` nav is the published-site sidebar. Both need updating when a new page lands.

7. **Err toward more updates, not fewer.** If uncertain whether a page is affected, update it.

---

## Tooling

If you modified `wiki/GRAPH.md`, run:

```
python3 scripts/lint-mermaid.py wiki/GRAPH.md
```

This auto-fixes Obsidian-incompatible Mermaid syntax.

---

## Commit (Pass 4 of 4 for this job)

When propagation is complete, stage every file you modified or created and commit with this message format:

```
sweep-1-propagate: <trigger-basenames> → <N> files updated [skip-wiki-sweep]
```

When multiple trigger files are present, use up to 3 basenames and append `+M more` if needed.

**The `[skip-wiki-sweep]` marker is required** — without it, your propagation commit retriggers the wiki-sweep workflow recursively. **Do NOT use `[skip ci]`** — that's nuclear; it blocks every workflow including `deploy-docs.yml` and the published site goes stale.

If nothing was modified across propagation, do NOT create an empty commit. Exit cleanly. The downstream `synthesize` job will still run.

---

## Global constraints

- **PhD audience.** No marketing language. State limitations clearly.
- **Evidence levels required** on every new or revised claim.
- **Inline provenance** on new content: `(source: <filename>)`.
- **No inline revision history.** Git is the history.
- **Pass 1 is conservative.** Don't synthesize, don't propose experiments, don't write to synthesis.md, don't draw cross-corpus conclusions. Synthesis is DeepSeek V4-Pro's job in the next pass.
- **Never write to:** `reference/*`, `*.html`, `CLAUDE.md`, `README.md`, `scripts/*`, `.claude/*`, `.obsidian/*`, `.git/*`, `abent-family-health/*`.
