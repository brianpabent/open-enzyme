# comp-020: Upstream Complement Modulator Sweep (Brief-Scrubbed Verification Re-Run)

**Date:** 2026-05-08
**Status:** Phase 1 complete. Re-run executed against the upstream complement cascade (C1q / MBL-MASP / C3 tickover; convertases; soluble factors; membrane regulators; residual C5/C5aR1 axis) anchored only to TARGET NODES — no compound names supplied, no prior comp-018 findings consulted.

## Purpose

Independent verification re-run of an earlier breadth scan. Per CLAUDE.md §Multi-model synthesis as guard against epistemic homogenization, the same heterogeneity-guard discipline applied to translation and to the wiki sweep daemon's three-pass output is here applied to a literature-mining scan: a brief-scrubbed re-run from a single agent produces a second-opinion data point that can be compared against the predecessor scan to surface narrative-cohesion bias, missed candidates, and assay-format inconsistencies.

## Question

Across all known upstream complement cascade nodes — C1q/MBL/MASP-2 (initiation); C3/C5 convertases; Factor B/D/H/I, properdin, clusterin (soluble); CD55/CD59/CR1 (membrane); residual C5/C5aR1 — which compounds have documented direct modulator activity (CH50, AP50, IC50, EC50, Ki, hemolytic, ELISA-deposition, or convertase-enzymatic assay) at IC50 / EC50 ≤ 100 μM-equivalent in matched-format assays, and across what compound classes (fungal / plant / bacterial / marine / dietary / FDA / TCM / Kampo / Ayurvedic) does the evidence cluster?

## Independence statement

- No prior comp-018 outputs consulted during this run.
- Compound names were NOT supplied in the brief; all hits emerged from target-anchored literature mining.
- Multilingual default applied (CNKI / WanFang / J-STAGE direct queries scoped; partially executed in time budget).
- ChEMBL coverage gap analysis included as a methodological output.

## Methodology

1. Target node list constructed from the brief's upstream-complement scope. See [`inputs/target-nodes.json`](inputs/target-nodes.json).
2. Per-node anchor queries via Paperclip MCP (PMC + bioRxiv + medRxiv full-text). See [`inputs/query-strategy.md`](inputs/query-strategy.md).
3. Returned primary-paper records inspected for IC50/CH50/AP50 values; values cited line-anchored where the source paper is in the Paperclip corpus.
4. Targeted WebSearch supplements for non-corpus PubMed records (notably rosmarinic acid PMID 10353266 / 1761351 / 3198307 — three primary papers documenting C3 convertase / C5 convertase IC50 values).
5. ChEMBL coverage spot-check for tabulated compounds. ChEMBL anti-complement assay coverage gaps documented as a methodological output.
6. CNKI / WanFang / J-STAGE multilingual scope scoped but only partially executed in 60-min time budget — Phase 2 follow-up explicitly flagged.
7. Compound × target × IC50 × assay format × evidence tier × source language × primary citation table assembled per node. See [`outputs/per-node-findings.md`](outputs/per-node-findings.md).

## Tool discipline

- Paperclip MCP: `search` / `grep` / `cat` / `head` only. **`map` operator NOT used** per `memory/feedback_paperclip_map_unreliable.md`.
- WebSearch: PubMed PMID anchors for rosmarinic acid 1988/1991/1999 papers.
- WebFetch: NOT used (sandbox-blocked behavior anticipated; not load-bearing for this scan).

## Time budget

Target 30-60 min. Actual: ~50 min.

## Output

- [`outputs/per-node-findings.md`](outputs/per-node-findings.md) — per-target-node compound × evidence tier × source language tables; assay-format heterogeneity log; ChEMBL coverage gap analysis; multilingual coverage analysis; unranked discriminating follow-ups.
- Wiki page: [`wiki/upstream-complement-verification-rerun-computational.md`](../../../upstream-complement-verification-rerun-computational.md) — interpretive plain-English-summary-first synthesis.

## Reproducibility

```bash
cd experiments/comp-020-upstream-complement-verification-rerun
# Inputs are JSON + markdown — no scripts to run for the literature mining itself.
# Each finding cites a primary source with PMC/PMID anchor; reproducing means re-querying the
# named source.
```

The Paperclip MCP queries used are documented in `outputs/per-node-findings.md` per finding's primary-citation row. Re-running the queries should reproduce the hits modulo MCP corpus updates.

## Comparison with predecessor (queued)

After both this re-run and the predecessor scan are complete, Brian compares:
1. **Compound list overlap** — which source records appear in both, and which appear in only one?
2. **Headline-bias check** — does the predecessor promote one result beyond what its source record supports, or does the re-run reveal narrative-cohesion bias?
3. **Assay-format discipline** — does either scan flag the rosmarinic-acid 44× IC50 spread or the heparin 50× pathway-stratified spread?
4. **Multilingual coverage** — does either scan show evidence of CNKI/WanFang/J-STAGE deep work?
5. **ChEMBL coverage gap** — do both surfaces flag the structural coverage gap?

This re-run supplies an assay-specific source inventory, not a headline compound, tier, comparative potency verdict, or platform priority. Candidate routing requires independent evidence verification, exact-material qualification, exposure and safety assessment, and a prespecified experiment.

## File index

```
comp-020-upstream-complement-verification-rerun/
├── README.md                                  ← this file
├── inputs/
│   ├── target-nodes.json                      ← upstream complement cascade target list
│   ├── query-strategy.md                      ← per-node anchor query patterns + tool order
│   └── provenance.md                          ← provenance + methodology notes
├── outputs/
│   ├── per-node-findings.md                   ← compound × node × IC50 × assay × evidence × source citation tables
│   └── search-log.md                          ← Paperclip queries run + result counts (audit trail)
└── scripts/                                   ← (empty — this is a literature-mining experiment, not a computational analysis)
```
