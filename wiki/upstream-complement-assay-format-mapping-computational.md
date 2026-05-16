---
title: "Upstream-Complement Compound × Assay-Format × IC50 Mapping (Computational, comp-021)"
date: 2026-05-16
tags:
  - computational
  - comp-021
  - complement
  - CP0
  - assay-format
  - rosmarinic-acid
  - heparin
  - bupleurum
  - ic50-spread
related:
  - complement-c5a-gout.md
  - upstream-complement-modulator-sweep-computational.md
  - upstream-complement-verification-rerun-computational.md
  - combined-cp0-systems-model-computational.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "Zhang T, Chen D 2008 J Ethnopharmacol 117(2):351-61 (PMC7126446); luteolin H-CP/H-AP grep-verified"
  - "Wu M et al. 2015 Acta Pharm Sin B 5(4):316-22 (PMC4629277); suramin H-CP 100 vs ELISA-CP 89 µg/mL within-paper anchor"
  - "Yin X et al. 2016 Molecules 21(11):1506 (PMC6273495); Helicteres lignan H-CP/H-AP grep-verified"
  - "Jin W et al. 2015 Mar Drugs 14(1):2 (PMC4728500); marine polysaccharide H-CP grep-verified"
  - "Talsma DT et al. 2020 Front Immunol 11:732 (PMC7212410); heparin 5-format spread grep-verified"
  - "Sahu A, Rawal N, Pangburn MK 1999 Biochem Pharmacol 57(12):1439-46 (PMID 10353266); RA 4-format spread WebSearch-snippet-tier"
status: complete (Phase 1)
---

# Upstream-Complement Compound × Assay-Format × IC50 Mapping (Computational, comp-021)

> **Frozen analysis at [`./etc/experiments/comp-021-upstream-complement-assay-format-mapping/`](./etc/experiments/comp-021-upstream-complement-assay-format-mapping/) — README + analyze.py + inputs/ + outputs/ committed for reproducibility.** Wiki page is the interpretive layer.

## Headline

comp-020 documented a **44× IC50 spread** for rosmarinic acid that drove [comp-029](./combined-cp0-systems-model-computational.md) to YELLOW. comp-021 stratified every published IC50 in the upstream-complement natural-product corpus by **assay format** (6 canonical formats from hemolytic CP/AP through ELISA WieLISA / C3c-ELISA through cell-based C3b deposition through purified convertase enzymatic) and scored each format 0-3 for gut-luminal mechanistic relevance.

**Result: the 44× RA spread is mostly assay-format spread.** Restricted to gut-luminal-relevant formats (CELL-C3b + H-CP + ELISA-CP — assays measuring C3b-deposition / C3-convertase-formation on cellular or hemolytic substrates), RA IC50 collapses from 200× full-range to **5.3×** (34-180 µM, median 160 µM, n=3). The 1500 µM number is orthogonal-step (RA doesn't act on assembled C5 convertase); the 5-10 µM Englberger optimal is a purified-enzymatic lower-bound that doesn't translate to whole-cascade biology.

## Cross-format anchors (validate the stratification logic)

- **Heparin** (5 formats, 2 labs): H-CP 38.5 µg/mL ≈ ELISA-CP-WieLISA 39 µg/mL within 1.5% (same pathway, different labs/format = consistent). BUT WieLISA-LP 2 vs C4-cleavage 102 µg/mL = 51× **real-biology spread** within Talsma 2020 (different cascade steps). Confirms format spread can be intrinsic.
- **Suramin** within Wu 2015: H-CP 100 vs ELISA-CP 89 µg/mL within 12%. Rules out "hemolytic-vs-ELISA artifact" as the RA discrepancy mechanism.

## comp-029 implications

Narrowing RA prior from log-uniform [5, 180] µM (36×) to [34, 180] µM (5.3×) tightens RA's singleton CI. Per comp-029 §6 dominant uncertainty driver is DAF α (Spearman r = +0.480) not RA IC50 (r = -0.658, now narrowed). **YELLOW verdict holds** — combined ratio at α=0.20 likely improves from 1.10× to ~1.12-1.15×, still below 1.5× GREEN threshold. Gating wet-lab unknown remains [§1.25 DAF MSU-surface engagement](./validation-experiments.md).

## Uncertainty-collapse vs replication-imperative buckets

- **Collapsed (now tight)**: rosmarinic acid (5.3× gut-relevant), Bupleurum chinense PS (3.6× across H-CP/H-AP/ELISA-LP — LP selectivity is real biology, not artifact).
- **Still wide**: heparin (19.5× even within gut-relevant subset — real multi-step biology); heparin tetrasaccharide (16.3× across WieLISA-LP vs C4-cleavage vs Ficolin3-LP — real cross-step heterogeneity).
- **Insufficient cross-format coverage** (13 compounds, single primary anchor at single format): Helicteres compounds 4 + 5 (the highest-potency lignans in scope), tiliroside, falcarindiol, ganoderic acid Sz, ergosterol, ANW/SC/SJW marine polysaccharides, luteolin, 3,5-diCQA. **Replication imperative sharpened:** the right test isn't "reproduce the published IC50" but "measure it at a DIFFERENT assay format that hits a different cascade step."

## Multilingual coverage

This run did not execute new CNKI / WanFang / J-STAGE direct queries; comp-020's partial-execution disclosure (§4.3) applies. The Wu 2015 + Zhang & Chen 2008 + Yin 2016 papers — Daofeng Chen Fudan group, English-language journals — are the canonical TCM-anti-complement primary literature in scope here. CNKI substantive follow-up remains queued per comp-020 §5.4.

## Where the analysis lives

- Per-IC50 grep-verification: [`./etc/experiments/comp-021-upstream-complement-assay-format-mapping/inputs/provenance.md`](./etc/experiments/comp-021-upstream-complement-assay-format-mapping/inputs/provenance.md)
- Compound × format × IC50 matrix: [`./etc/experiments/comp-021-upstream-complement-assay-format-mapping/outputs/matrix.json`](./etc/experiments/comp-021-upstream-complement-assay-format-mapping/outputs/matrix.json)
- Summary with per-compound spread analysis: [`./etc/experiments/comp-021-upstream-complement-assay-format-mapping/outputs/summary.md`](./etc/experiments/comp-021-upstream-complement-assay-format-mapping/outputs/summary.md)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
