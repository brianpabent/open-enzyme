# Legacy upstream-complement literature inventory (formerly COMP-020)

**Date:** 2026-05-08
**Status:** Quarantined legacy literature provenance. This was not an executable computational experiment, and its quantitative verdict is invalid. Raw queries and source observations are retained for audit and possible re-verification; generated outputs are not authoritative for a threshold-qualified hit set, potency ranking, ChEMBL coverage rate, exhaustive absence, gout-compartment activity, dietary efficacy, CFH independence, or genotype response.

## Purpose

This directory preserves a target-anchored literature scan that was originally framed as an independent verification re-run. Its useful output is an audit trail of searches and assay-specific source leads. It does not satisfy the current COMP lifecycle or reproducibility standard.

## Historical question — unresolved

Across all known upstream complement cascade nodes — C1q/MBL/MASP-2 (initiation); C3/C5 convertases; Factor B/D/H/I, properdin, clusterin (soluble); CD55/CD59/CR1 (membrane); residual C5/C5aR1 — which compounds have documented direct modulator activity (CH50, AP50, IC50, EC50, Ki, hemolytic, ELISA-deposition, or convertase-enzymatic assay) at IC50 / EC50 ≤ 100 μM-equivalent in matched-format assays, and across what compound classes (fungal / plant / bacterial / marine / dietary / FDA / TCM / Kampo / Ayurvedic) does the evidence cluster?

## Independence defect

- The agent did not directly read prior comp-018/019 output files.
- The brief nevertheless supplied named comparators, prior exclusions, and an
  empty-class conclusion through `inputs/target-nodes.json`.
- This was therefore not a context-isolated independent replication. The
  artifact cannot support an independence or confirmation claim.
- Multilingual sources were scoped but not executed deeply enough to support a
  multilingual coverage claim.
- The ChEMBL notes were an unsnapshotted spot-check and support no coverage
  analysis.

## Methodology

1. Target node list constructed from the brief's upstream-complement scope. See [`inputs/target-nodes.json`](inputs/target-nodes.json).
2. Per-node anchor queries via Paperclip MCP (PMC + bioRxiv + medRxiv full-text). See [`inputs/query-strategy.md`](inputs/query-strategy.md).
3. Returned primary-paper records inspected for IC50/CH50/AP50 values; values cited line-anchored where the source paper is in the Paperclip corpus.
4. Targeted WebSearch supplements recorded PubMed and search-snippet leads,
   including rosmarinic-acid records. The full text was not verified for every
   value.
5. An unsnapshotted ChEMBL spot-check recorded identifiers as future query
   seeds only.
6. CNKI / WanFang / J-STAGE multilingual work was scoped but only partially
   executed within the approximately 50-minute run.
7. Compound × target × IC50 × assay format × evidence tier × source language × primary citation table assembled per node. See [`outputs/per-node-findings.md`](outputs/per-node-findings.md).

## Tool discipline

- Paperclip MCP: `search` / `grep` / `cat` / `head` only. **`map` operator NOT used** per `memory/feedback_paperclip_map_unreliable.md`.
- WebSearch: PubMed PMID anchors for rosmarinic acid 1988/1991/1999 papers.
- WebFetch: NOT used (sandbox-blocked behavior anticipated; not load-bearing for this scan).

## Time budget

Target 30-60 min. Actual: ~50 min.

## Output

- [`outputs/per-node-findings.md`](outputs/per-node-findings.md) — quarantined
  source leads and the conditions required before any can be reused.
- Wiki page: [`wiki/upstream-complement-verification-rerun-computational.md`](../../../upstream-complement-verification-rerun-computational.md) — interpretive plain-English-summary-first synthesis.

## Method receipt

```bash
cd wiki/etc/experiments/comp-020-upstream-complement-verification-rerun
# Inspect the recorded queries, sources, and raw findings.
```

There is no executable decision function or immutable source snapshot. Re-querying evolving databases may recover different records and does not exactly reproduce the original scan. Any source observation reused in current work must be reverified at the exact material, assay, unit, and primary-source tier.

## Historical comparison intent

After both this re-run and the predecessor scan are complete, Brian compares:
1. **Compound list overlap** — which source records appear in both, and which appear in only one?
2. **Headline-bias check** — does the predecessor promote one result beyond what its source record supports, or does the re-run reveal narrative-cohesion bias?
3. **Assay-format discipline** — does either scan improperly compare records
   from different materials, pathways, or assay conditions?
4. **Multilingual execution** — which exact regional databases, queries, and
   primary records were actually inspected?
5. **Registry reproducibility** — was a dated, query-defined snapshot retained,
   or only informal identifier notes?

This inventory supplies no headline compound, tier, comparative potency verdict, platform priority, or completed quantitative result. Candidate routing requires independent evidence verification, exact-material qualification, exposure and safety assessment, and a prespecified experiment.

## File index

```
comp-020-upstream-complement-verification-rerun/
├── README.md                                  ← this file
├── inputs/
│   ├── target-nodes.json                      ← upstream complement cascade target list
│   ├── query-strategy.md                      ← per-node anchor query patterns + tool order
│   └── provenance.md                          ← provenance + methodology notes
├── outputs/
│   ├── per-node-findings.md                   ← quarantined source-lead tables
│   └── search-log.md                          ← Paperclip queries run + result counts (audit trail)
└── reviews/                                   ← exact-snapshot review receipts
```
