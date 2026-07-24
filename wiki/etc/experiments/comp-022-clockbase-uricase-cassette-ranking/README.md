# comp-022: ClockBase-style Combinatorial Ranking of A. oryzae Uricase Expression Cassettes

**Question:** Across the ~43,200 *A. oryzae* uricase expression cassette design space (promoter × signal peptide × codon variant × secretion scaffold), which sequence-level candidates survive a multi-model concordance gate and warrant promotion into the §1.33 physiological topology screen?

**Verdict:** **501 unique cassettes (collapsed across propeptide / N-glyc modifiers) pass N-of-4 ≥ 3 concordance; 195 of 43,200 candidates (0.45%) pass N-of-4 = 4 (all four models in top quintile). The headline cluster converges on PamyB + 5'-softened-codon-optimization + direct-secretion + PTS1-blocked C-terminal tag + native-glyc-ablated. This is a candidate cluster, not a topology verdict.**

Comp-022 adds three sequence-level refinements to the direct-secretion candidate: (1) prefer the **5'-softened codon variant** (low-GC head + max-CAI body) over pure max-CAI; (2) **block the PTS1 signal** explicitly with 3xAla or His6 C-terminal tag rather than leaving native SKL intact; (3) **ablate the N191 glycosylation sequon** (N191Q) to remove the one predicted occupancy site uricase carries. These refinements can enter §1.33 at gene-synthesis time, but comp-022 cannot establish product formation at physiological substrate, oxygen dependence, peroxide safety, or the topology to carry into §1.9B.

**Informs:** [`validation-experiments.md` §1.33 and §1.9B](../../../validation-experiments.md); replaces literature-precedent one-at-a-time selection with a composite-ranked candidate shortlist before gene-synthesis dollars commit. §1.33, not comp-022, selects topology; §1.9B then tests the selected implementation in solid-state koji.

**Interpretive wiki page:** [`wiki/uricase-cassette-ranking-computational.md`](../../../uricase-cassette-ranking-computational.md)

**Related experiments:** [comp-010 (invalidated cassette model)](../comp-010-cassette-compatibility/) | [comp-011 (invalidated *C. utilis* cassette model)](../comp-011-c-utilis-uricase-cassette-compatibility/) | [comp-001 (uricase protease-site proxy; empirical risk unresolved)](../comp-001-uricase-shio-koji-protease-stability/)

---

## How to reproduce

**v1 (stdlib-only):**

```bash
cd wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking
python3 analyze.py
```

Stdlib-only Python 3 (no external packages). All inputs are committed in `inputs/`. Outputs land in `outputs/` and are committed as peer-reviewable artifacts.

**v2 (canonical writer = `v2/analyze_v2.py`):**

```bash
cd wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2
python3 analyze_v2.py   # regenerates outputs/v2_shortlist.csv, v2_summary.json
```

`v2/analyze_v2.py` is the **canonical** v2 script — it produced the committed `v2/outputs/`. `v2/rerank_v2.py` is a DEPRECATED earlier writer that emits the same filenames with an incompatible column schema; do not run it to regenerate the committed outputs (see its header). The upstream ESM2 pseudo-likelihood and ViennaRNA MFE scores (`v2/run_esm2_pseudo_likelihood.py`, `v2/run_viennarna_mfe.py`) require a non-stdlib environment (torch, ViennaRNA); their outputs are committed under `v2/outputs/` so `analyze_v2.py` reproduces the ranking from committed intermediate scores without re-running those models. *(Marked 2026-07-14, independent comp review.)*

---

## File index

```
comp-022-clockbase-uricase-cassette-ranking/
  analyze.py                       ← analysis script (run this)
  inputs/
    parts_list.json                ← enumerated 6 promoters x 12 SPs x 10 codons x 60 scaffolds
    a_oryzae_codon_usage.json      ← fixed Kazusa RIB40 codon table
    Q00511.fasta                   ← A. flavus uricase, 302 aa (UniProt Q00511)
    provenance.md                  ← source-by-source citations + verification table
  outputs/
    report.json                    ← machine-readable full report (top 25 + distributions)
    full_ranking_top1000.csv       ← top 1000 of 43,200 by concordance + composite
    unique_cassette_shortlist.csv  ← 501 unique (promoter, sp, codon, scaffold_base) combos in shortlist
    top25.md                       ← human-readable top-25 cassette table
    codon_variant_scores.md        ← per-codon-variant Tier 1 score table (10 rows)
    scaffold_chaperone_loads.md    ← per-scaffold chaperone-load table (10 base scaffolds)
  provenance.md                    ← verification-agent pass per CLAUDE.md Rule 4 + comp-NNN verification proposal
  README.md                        ← this file
```

---

## Four-model scoring pipeline

| Model | Tier | Score direction | Method |
|---|---|---|---|
| Codon Adaptation Index (CAI) | 1 | Higher better | Sharp & Li 1987 PMID 3547335 over A. oryzae table |
| mRNA 5' structure proxy | 1 | Higher better | GC-content + GC-clamp + palindromic-4mer count over first 120 nt; ViennaRNA proxy (Kudla 2009 PMID 19359587) |
| Architecture-adjusted chaperone load | 2 | Lower better | Σ (disulfide_count × α) per chaperone-orthogonal-stacking.md §3.5 formula |
| Promoter × SP prior | 4 | Higher better | Literature-derived bounded multiplier per promoter and SP |

Concordance gate: a candidate passes if it falls in the top quintile (top 20%) of N-of-4 models. Threshold for the sequence-level shortlist: **N-of-4 ≥ 3 (75% concordance)**, chosen a priori from ClockBase 30/40 precedent (no retrospective calibration possible against comp-001..comp-014 since those were not cassette-ranking experiments).

---

## V1 simplifications (owned per parent brief)

1. **Cascading-filter not strictly needed.** Tier 1 (CAI + mRNA-5') is per-codon-variant only (10 evaluations, not 43,200), and Tier 2 (chaperone-load) is per-scaffold-base-only (10 evaluations, not 43,200). So evaluation of all 43,200 candidates is O(1) per candidate after the per-variant and per-scaffold pre-computations. Cascading-filter language in the brief was for a model where Tier 2/3 required per-candidate compute; here it does not.

2. **Tier 3 fold-quality model (ESMFold / AlphaFold pLDDT) DEFERRED.** No GPU access, no ColabFold API access from this subagent. Brief authorized this; we replace it with a sequence-preservation tie-breaker that is effectively redundant with Tier 1 (since all candidates share the same uricase AA sequence). Functional topology is deferred to §1.33, followed by solid-state confirmation in §1.9B.

3. **N-of-M threshold = 3 of 4 (75%), not 4 of 5 (80%).** Because fold-quality is deferred, M=4 not 5. The 75% concordance fraction matches ClockBase precedent. A priori choice, no retrospective calibration.

4. **Promoter strengths + SP efficiencies are bounded estimates**, not measured in NSlD-ΔP10. They are priors and should be read as ordinal multipliers, not absolute predicted titer ratios.

5. **mRNA 5' structure proxy** is a GC-content + GC-clamp + palindromic-4mer count instead of true ViennaRNA MFE. Defensible per Kudla 2009 (5' GC dominates translation initiation), but a true MFE pass on the surviving shortlist would refine the ranking.

See `provenance.md` for the full verification-agent pass and the explicit "items not verified" section.

---

## Headline numbers

- Design space: **43,200 candidates** (matches brief's Pass-2 estimate exactly).
- N-of-4 = 4 (all four models top quintile): **195 candidates (0.45%)**.
- N-of-4 ≥ 3 (75% concordance): **2,421 candidates (5.6%)** → **501 unique cassettes** after collapsing propeptide/nglyc modifier degeneracy.
- Top cluster: **PamyB + SPamyB_pro + 5'-softened codon variant + direct-secretion + 3xAla or His6 C-terminal tag + N191Q glyc-ablation + no propeptide**.
- §1.33 candidate list: direct-secretion arm refined in three gene-synthesis-time details (codon variant, C-terminal tag, glycosylation sequon); architecture remains unresolved until the physiological-system readout.

---

## Disagreement protocol

If you reproduce the outputs and disagree with the methods or numbers, file a GitHub issue referencing this folder (`comp-022-clockbase-uricase-cassette-ranking`). Primary candidates for revision: (1) promoter relative-strength values; (2) SP_BASE_EFFICIENCY values; (3) glucoamylase carrier glyc-load (3 N-glyc sites vs the 2.5 heuristic we used); (4) KEX2_PENALTIES values; (5) lack of ViennaRNA MFE; would substantively change the mRNA-5' ranking column.
