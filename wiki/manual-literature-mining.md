---
title: "Manual Literature Mining Protocol — Paperclip MCP Discipline"
date: 2026-05-05
tags:
  - methodology
  - literature-mining
  - paperclip
  - verification-discipline
  - epistemic-rigor
  - global-multilingual
related:
  - paperclip-deep-dive.md
  - bio-ai-tools.md
  - open-source-platform.md
  - chembl-cross-check.md
  - CLAUDE.md
sources:
  - "feedback memory `feedback_paperclip_map_unreliable.md` — documented hallucination of organisms and fabricated kinetic numbers by the `map` operator (2026-05-05)"
  - "paperclip-deep-dive.md — full Paperclip MCP capability + limitation audit"
status: published
---

# Manual Literature Mining Protocol — Paperclip MCP Discipline

A small but load-bearing methodology page. Codifies the verification discipline for using Paperclip MCP (the full-text PubMed / bioRxiv / medRxiv / arXiv corpus) safely in this project — surfaced 2026-05-05 by the wiki sweep daemon (Pass 2 Connection #3 + Priority Action #1). The motivation: Paperclip's index of ~11M full-text papers is genuinely valuable for deep-dive questions, but the `map` operator (the convenience-aggregation primitive) hallucinates — wrong organisms, fabricated kinetic numbers, made-up author affiliations — making automated unverified use unsafe. This page defines the safe-use workflow.

## Why this protocol exists

Specific failure mode documented 2026-05-05: a Paperclip `map` query against a multi-paper question returned organism names not present in the source papers AND specific kinetic numbers (Km, IC50) that did not appear in any of the cited sources when grep-verified. The `map` primitive appears to do model-side aggregation of partial extracts, which the underlying model fills in plausibly but not faithfully. (Memory record: `feedback_paperclip_map_unreliable.md`, decided 2026-05-05.)

`search`, `cat`, `head`, `grep`, `scan` primitives DON'T exhibit this failure mode — they return raw paper content, line-anchored, verifiable. The protocol below confines automated use to those safe primitives and requires explicit verification before any quantitative claim derived from Paperclip enters the wiki.

## The five-rule discipline

### 1. Use safe primitives only

**Allowed:** `search`, `cat`, `head`, `grep`, `scan`.
**Forbidden in any automated workflow:** `map`, `reduce`, or any aggregation primitive that produces synthesized output rather than raw paper content.

If a finding requires aggregation across multiple papers (e.g., "summarize the IC50 range for compound X across all NLRP3-relevant studies"), do the aggregation in two stages: (1) `search` + `grep` to surface the specific lines containing IC50 values; (2) human-verify each value against `cat` of the source paper; (3) the synthesis happens in the wiki page, not in Paperclip's primitive call.

### 2. Anchor identity to `meta.json`

Every paper Paperclip returns has a `/papers/<id>/meta.json` file with: title, authors, journal, year, PMID, doi. **Cite from `meta.json`, not from inferred metadata in the paper body.** A common failure mode is misattributing a paper based on a title-like string in the body that turns out to be a citation TO another paper, not the paper's own title.

Workflow: `cat /papers/<id>/meta.json | jq .title` (or read directly) before quoting a paper.

### 3. Grep-verify all numbers before they enter the wiki

For any quantitative claim sourced from Paperclip — IC50, Km, dose, sample size, percent change, p-value, cohort n — `grep` for the specific number in the source paper's `content.lines` file BEFORE writing the number into the wiki. The verification step takes ~30 seconds and catches the `map`-class hallucination directly.

```bash
# Example: verify a claimed IC50
grep -i "IC50" /papers/<id>/content.lines
grep "5\.18\|5.18 μM" /papers/<id>/content.lines
```

If the number doesn't appear in the source, it didn't come from the source. Do not propagate.

### 4. Never propagate `map`/`reduce` summaries

If you find yourself looking at output from Paperclip's `map` or `reduce` primitives (e.g., from a prior session, from a logged subagent task, from the daemon's intermediate state) — **treat that output as un-validated and re-derive from the safe primitives.** A `map` summary that LOOKS reasonable cannot be assumed reasonable.

This applies even when the `map` output is convenient. Convenience is the failure-mode signal — `map` is fast precisely because it skips verification.

### 5. Cite line-anchored, with the project's citation format

Paperclip provides line-anchored URLs of the form `https://citations.gxl.ai/papers/<doc_id>#L<n>`. **Always cite at the line-anchor level**, never just at the paper level. This makes verification trivial for a future reader (or for the sweep daemon's Pass 3 reviewer) and forces the citation to point at a specific claim, not a generalized invocation of "the paper."

Citation discipline (from existing wiki convention):
- Inline: `[1]`, `[2]`
- References block at end of page:
  ```
  --------
  REFERENCES
  [1] Authors. "Title." *Journal* vol, pages (year). doi:XX
      https://citations.gxl.ai/papers/<doc_id>#L<n>
  ```
- Never expose Paperclip's internal `doc_id` in prose (only in the URL).

## Specific OE questions worth Paperclip search-and-verify time

These are questions whose primary-literature grounding would meaningfully advance the platform but require non-trivial scanning. Listed here so they're discoverable as a queue (anyone reading this page can pick one up):

1. **Does *Candida utilis* uricase have published KEX2-site / cassette-compatibility data?** — supports comp-011 (the *C. utilis* uricase compatibility analysis). Search: `Candida utilis uricase Aspergillus` + grep KEX2, signal peptide, secretion.
2. ***Aspergillus oryzae* heterologous expression precedents** beyond what comp-010 + Killshot #1 already surfaced — particularly any solid-state-format dual-protein work. Search: `Aspergillus oryzae solid-state heterologous protein` + grep dual cassette, multi-cassette, two genes.
3. **ABCG2-probiotic intersections** — does any published probiotic strain (engineered or natural) modulate intestinal ABCG2 expression in vivo? Informs the LBP track's butyrate-via-*F. prausnitzii* thesis. Search: `ABCG2 probiotic` + grep intestinal expression, fold-change.
4. **GRAS-host complement-regulator expression** — has anyone published heterologous expression of soluble complement regulators (sCR1, Factor H, DAF/CD55) in any GRAS organism? Informs comp-006 / comp-012 platform implications. Search: `complement regulator heterologous expression yeast Aspergillus` + grep specific protein names.
5. **Si Miao San and related TCM gout formulas** — modern Chinese clinical evidence. Per the global-multilingual default ([CLAUDE.md](../CLAUDE.md) §"Global-multilingual research by default"), search Chinese-language sources directly via CNKI / WanFang / ChiCTR, not just PubMed-indexed translations. Informs the TCM × rigor track ([tcm-modern-rigor-intersection.md](./tcm-modern-rigor-intersection.md)) Phase 2 P2-1.
6. **NSlD-ΔP10 strain availability outside the Maruyama lab** — verify the `operations/ward-1995-lab-access.md` finding that the strain isn't in any public repository by direct catalog query at JCM, NBRC, CGMCC, CBS-KNAW, ATCC, FGSC.

## When Paperclip is the wrong tool

- **For ChEMBL bioactivity data** — use the ChEMBL MCP directly. Paperclip's index is paper-level; ChEMBL is target-and-compound-level with curated quantitative bioactivity. See [`chembl-cross-check.md`](./chembl-cross-check.md) for the cross-check discipline.
- **For patents** — Paperclip indexes academic literature, not patent literature. Use Google Patents, Espacenet, Lens.org, JPlatPat, CNIPA directly via WebFetch.
- **For non-English-language clinical trial registries** — ChiCTR (Chinese), JPRN (Japanese), KISS (Korean) registries are not in Paperclip's index. Direct WebFetch of those registries is the right tool.
- **For real-time updates** — Paperclip's index has an indexing lag. For the very most recent findings (within the last 1–4 weeks), the journal websites or PubMed direct may have content Paperclip doesn't yet have.

## Cross-references

- [`paperclip-deep-dive.md`](./paperclip-deep-dive.md) — full Paperclip MCP capability + limitation audit (the upstream documentation this page operationalizes for OE)
- [`bio-ai-tools.md`](./bio-ai-tools.md) — broader AI-tool landscape for biology research
- [`chembl-cross-check.md`](./chembl-cross-check.md) — sister discipline for ChEMBL bioactivity verification
- [`open-source-platform.md`](./open-source-platform.md) §"Multi-model synthesis as guard against epistemic homogenization" — the broader epistemic-rigor framework this protocol fits within
- [`CLAUDE.md`](../CLAUDE.md) §"Global-multilingual research by default" + §"Translation protocol" — the multilingual + cross-vendor disciplines that combine with this protocol for non-English Paperclip-adjacent work
