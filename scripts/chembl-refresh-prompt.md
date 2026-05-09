# ChEMBL Quarterly Refresh — Agent Brief

You are running a quarterly ChEMBL v3x cross-check refresh for the Open Enzyme research library. **Read `CLAUDE.md` first** for evidence-level standards, cross-referencing rules, and the Doc Sweep Rule. The TRIGGER block at the end of this prompt names the timestamp, trigger event, and any manual dispatch context.

## Your job

Re-query ChEMBL for every compound listed in `wiki/chembl-cross-check.md`, diff against the recorded baseline, and surface any new bioactivities or discrepancies. Also catch compounds newly added to the Open Enzyme stack since the last refresh.

---

## Knowledge-base layout

Two kinds of content: **living** (the refresh reads AND writes) and **canonical** (read-only).

### Living — read and write

- `wiki/chembl-cross-check.md` — the ChEMBL cross-check baseline. This is the primary file you are updating.
- `synthesis/queue/` — action queue. Prepend a new section if Pass 1 or Pass 2 surface meaningful discrepancies (see Pass 4). Never delete or modify existing sections.
- `logs/chembl-refresh-log.md` — this workflow's own log (see Pass 5; create with an H1 heading if it doesn't exist).

### Read-only for this workflow

- `wiki/*.md` (other than `chembl-cross-check.md`) — read to discover newly-added stack compounds in Pass 2, but **do not modify**. The wiki-sweep workflow owns edits to other wiki pages. Surface findings through `synthesis/queue/` files (Pass 4) and let Brian (or a subsequent sweep) propagate.
- `reference/*`, `*.html`, `CLAUDE.md`, `README.md`, `scripts/*`, `.claude/*`, `.obsidian/*`, `.git/*` — never modify.

The only files the refresh writes: `wiki/chembl-cross-check.md`, `synthesis/queue/`, `logs/chembl-refresh-log.md`.

---

## PASS 1 — Re-query baseline compounds

Read `wiki/chembl-cross-check.md`. Extract the list of stack compounds already cross-checked (from the summary table and per-compound sections).

For each compound:

1. Call `mcp__plugin_chembl_ChEMBL__compound_search` by name to confirm the ChEMBL ID. ChEMBL IDs can occasionally be re-indexed, merged, or withdrawn between releases.
2. Call `mcp__plugin_chembl_ChEMBL__get_bioactivity` with the (confirmed) ChEMBL ID to fetch the current curated bioactivity profile.
3. Compare against the baseline recorded in `wiki/chembl-cross-check.md`. Flag any of:
   - **New targets** — bioactivity entries against targets not previously recorded.
   - **Changed IC50/EC50/Ki** — values that moved by >2× from the previous record (in either direction).
   - **Newly potent** — sub-μM activities against targets previously recorded as ~μM or weaker.
   - **Withdrawn / merged** — ChEMBL IDs that changed, disappeared, or were merged into another entry.
   - **New assay types** — e.g., a target that previously had only binding data now has functional data (or vice versa).
4. Capture the diff for each compound in a working list (compound → list of findings, or "unchanged").

---

## PASS 2 — Add new compounds to the baseline

Since the last refresh, new compounds may have been added to the Open Enzyme stack. Scan these files for compound names not yet in the cross-check baseline:

- `wiki/supplements-stack.md`
- `wiki/nlrp3-inhibitor-screen.md`
- Any other `wiki/*.md` file that lists concrete small-molecule interventions (e.g., new per-compound pages).

For each new compound:

1. Call `mcp__plugin_chembl_ChEMBL__compound_search` to resolve its ChEMBL ID.
2. Call `mcp__plugin_chembl_ChEMBL__get_bioactivity` to pull the curated bioactivity profile.
3. Optionally call `mcp__plugin_chembl_ChEMBL__get_mechanism` if the compound has an approved-drug or clinical-candidate mechanism entry — this is the most valuable signal for cross-checking claimed MoA.
4. Add a new row to the summary table and a full per-compound section to `wiki/chembl-cross-check.md`, matching the format of entries already in that file.

If a compound has no ChEMBL entry (e.g., a complex botanical extract or a novel food ingredient), note that explicitly in the table with `no ChEMBL record` and move on. Don't fabricate entries.

---

## PASS 3 — Update `wiki/chembl-cross-check.md`

For every change surfaced in Pass 1 or Pass 2:

- Update the summary table at the top of the file — last-refreshed date, top target, IC50, any newly added compounds.
- Add or expand a per-compound discrepancy block when a genuinely new top-target or newly-potent activity surfaces. Preserve prior discrepancy narratives — append "As of <YYYY-MM-DD> refresh: ..." rather than overwriting.
- Update the per-compound "last refreshed" date (or equivalent) for every compound you re-queried, even when data is unchanged — so Brian can see the baseline is current.
- Update the page-level refresh date / header at the top of the file (e.g., `date:` in frontmatter, or a "Last refreshed" line in the body — match whatever format is already in use).
- Tag every new or revised claim with its evidence level: `(Clinical Trial)`, `(Animal Model)`, `(In Vitro)`, or `(Mechanistic Extrapolation)`. ChEMBL bioactivity records are `(In Vitro)` by default unless the underlying reference is explicitly clinical.
- Add inline provenance on new content: `(source: ChEMBL v3X refresh <YYYY-MM-DD>)`. Use the ChEMBL version string the API returns if available; otherwise use the date alone.

If every compound is unchanged: update only the per-compound refresh dates and the page-level refresh date. Do not add empty "no change" sections.

---

## PASS 4 — Surface findings to `synthesis/queue/`

(Updated 2026-05-08 per [migration spec](../operations/specs/2026-05-08-synthesis-filesystem-migration.md) §4.3 N1 — was previously "prepend to `wiki/synthesis.md`"; that file no longer exists post-migration.)

If Pass 1 or Pass 2 found **meaningful** discrepancies (new potent targets, changed framings, newly-indexed compounds, withdrawn/merged IDs), **write one file per discrepancy directly to `synthesis/queue/`** following the naming convention `<YYYY-MM-DD>-chembl-discrepancy-<N>-<slug>.md` where `<N>` is the discrepancy index (1, 2, 3...) and `<slug>` is a kebab-case slug derived from the compound name + change description.

Each file follows the synthesis queue format per [migration spec §5.4](../operations/specs/2026-05-08-synthesis-filesystem-migration.md):

```markdown
---
type: chembl-discrepancy
quarter: <YYYY-Q[1-4]>
sweep_date: <YYYY-MM-DD>
compound: <compound-name>
chembl_id: <CHEMBL-id>
wiki_claim: <one-line summary of what the wiki currently says>
chembl_curated: <one-line summary of what ChEMBL now reports>
evidence_tier: Supported | Speculative
---

# ChEMBL discrepancy — <compound> at <target>

[1-2 paragraph plain-English description of the discrepancy. What the wiki says
vs. what ChEMBL now reports. Why it matters for the Open Enzyme thesis (gout /
NLRP3 / EPI / stack interactions). Any contradictions with specific wiki claims
flagged explicitly.]

## Suggested action

[One of: verify against primary source / drop the wiki claim / add to
`wiki/chembl-cross-check.md` / propose an experiment / queue for next sweep
walkthrough.]
```

Files in `synthesis/queue/` are picked up by the next walk-synthesis discipline (`.claude/skills/walk-synthesis/SKILL.md`) — either actioned (closure note appended + `git mv` to `synthesis/done/`) or addressed via wiki-page edits.

**Skip Pass 4 entirely** if no meaningful discrepancies surfaced — e.g., only refresh dates changed, or deltas are below the >2× threshold. Record "no new findings" in the Pass 5 log instead. Low-signal queue entries pollute the walkthrough.

**Do not edit any other wiki page.** If a new potent target contradicts a claim in (say) `wiki/nlrp3-inflammasome.md`, note it in the queue file's "Suggested action" section for a subsequent walkthrough to propagate. The chembl-refresh workflow must not race the wiki-sweep workflow.

**Recursion-protection rationale (post-migration):** chembl-refresh writes to `synthesis/**`, which the wiki-sweep daemon's path filter (`wiki/**.md`) does not match. The `[skip-wiki-sweep]` commit-msg marker is still applied to chembl-refresh's commits as belt-and-suspenders per [migration spec §5.9](../operations/specs/2026-05-08-synthesis-filesystem-migration.md).

---

## PASS 5 — Log

Append to `logs/chembl-refresh-log.md` (create it with an H1 heading `# ChEMBL Refresh Log` if it doesn't exist):

```markdown
## Refresh: <YYYY-MM-DD HH:MM UTC>

**Trigger:** scheduled (cron) | manual (workflow_dispatch)
**Note:** <value from TRIGGER block's `note=` field, or "—" if absent>
**Compounds queried:** <count re-queried in Pass 1> baseline + <count added in Pass 2> new = <total>
**Discrepancies surfaced:** <count — "none" if zero meaningful diffs>
**Summary:** <one-line top finding, or "all baselines current">
```

---

## PASS 6 — Commit

Read the TRIGGER block's `commit=` directive.

- **`commit=yes`** — stage every file you modified or created and commit with this message format:

  ```
  chembl-refresh: quarterly sweep <YYYY-MM-DD> — <N> compounds, <M> discrepancies [skip-chembl-refresh] [skip-wiki-sweep]
  ```

  Where `<N>` is the total number of compounds queried (baseline + new) and `<M>` is the count of meaningful discrepancies from Pass 4 ("0" if none). **Both markers are required**: `[skip-chembl-refresh]` prevents this workflow from re-triggering itself; `[skip-wiki-sweep]` prevents `wiki-sweep.yml` from firing on the `wiki/chembl-cross-check.md` change (which would be redundant since the refresh already synthesized into synthesis.md). **Do NOT use `[skip ci]`** — that's nuclear; it blocks every workflow including `deploy-docs.yml`, and the published site would go stale after every quarterly refresh. The workflow-specific markers are surgical.

  If nothing was modified across any pass, **do not create an empty commit.** Exit cleanly and let the "Push refresh output" step no-op.

- **`commit=no`** — leave all changes unstaged. Brian will review and commit manually.

---

## Global constraints

- **PhD audience.** No marketing language. State limitations clearly.
- **Evidence levels required** on every new or revised claim.
- **Inline provenance** on new content: `(source: ChEMBL v3X refresh <date>)`.
- **No inline revision history.** Git is the history.
- **Never write to:** `reference/*`, `*.html`, `CLAUDE.md`, `README.md`, `scripts/*`, `.claude/*`, `.obsidian/*`, `.git/*`, or any `wiki/*.md` other than `chembl-cross-check.md` and `synthesis.md`.
- **Do not race the wiki-sweep workflow.** This refresh writes to a narrow set of files by design; cross-wiki propagation happens through `synthesis.md` and subsequent wiki-sweep runs.
