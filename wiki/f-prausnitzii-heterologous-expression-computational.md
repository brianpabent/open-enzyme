---
title: "F. prausnitzii Heterologous Expression Feasibility (comp-008)"
date: 2026-05-16
tags:
  - computational-experiment
  - engineered-lbp-chassis
  - faecalibacterium-prausnitzii
  - faecalibacterium-duncaniae
  - heterologous-expression
  - butyrate
  - payload-feasibility
related:
  - engineered-lbp-chassis.md
  - hypotheses/H02-engineered-lbp-thesis.md
  - uricase.md
  - lactoferrin.md
  - complement-c5a-gout.md
  - dual-chassis-ecn-pdb-uricase-computational.md
sources:
  - "Fraccascia 2022 Microbiol Resour Announc doi:10.1128/mra.00824-22 — Fp genome 2.78-3.23 Mbp, 56.6% GC"
  - "Sheridan 2023 Microbiome Research Reports doi:10.20517/mrr.2022.13 — gut-bacteria genetic-manipulation review"
  - "Martín 2023 FEMS Microbiol Rev doi:10.1093/femsre/fuad039 — Faecalibacterium NGP/LBP review"
  - "Quévrain 2016 Gut doi:10.1136/gutjnl-2014-307649 + Breyner 2017 Front Microbiol doi:10.3389/fmicb.2017.00114 — MAM L. lactis delivery (workaround for missing Fp toolkit)"
  - "Sakamoto 2022 IJSEM doi:10.1099/ijsem.0.005379 — A2-165 reclassified as F. duncaniae"
status: complete
---

# F. prausnitzii Heterologous Expression Feasibility (comp-008)

> **Frozen analysis archived at [`experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md`](../experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md). Reproducible artifact: `python3 experiments/comp-008-f-prausnitzii-heterologous-expression/analyze.py`.**

## Headline ranking

| Rank | Payload | Composite (base) | Range | Verdict | Limiting factor |
|---|---|---|---|---|---|
| 1 | Butyrate-pathway boost (native BCoAT, UniProt C7H5K4) | **0.748** | [0.641, 0.822] | **GREEN** | engineering toolkit maturity |
| 2 | sCR1 SCR1-4 truncation (UniProt P17927) | 0.565 | [0.433, 0.678] | YELLOW | engineering toolkit maturity |
| 3 | Human lactoferrin (UniProt P02788) | 0.540 | [0.423, 0.659] | YELLOW | engineering toolkit maturity |
| 4 | *A. flavus* uricase (UniProt Q00511) | 0.393 | [0.271, 0.523] | YELLOW (toward RED) | **host physiology (O2 substrate vs strict anaerobe)** |

## Key findings

1. **Butyrate-pathway boost wins decisively.** It is the only GREEN payload at the base score and remains GREEN with the engineering-toolkit gap excluded (toolkit-conditional score 0.875). CAI=1.0 (native gene), no secretion, no folding burden, native pathway alignment.
2. **Uricase is the wrong payload for this chassis.** Uricase catalyzes uric acid + O2 → 5-hydroxyisourate + H2O2 ([UniProt Q00511](https://www.uniprot.org/uniprotkb/Q00511); verified 2026-05-16). F. prausnitzii is a strict obligate anaerobe in an anoxic colonic lumen. Even with a perfect engineering toolkit, the chemistry can't run. **Strategic reclassification:** uricase belongs on koji or *E. coli* Nissle (facultative anaerobe), not F. prausnitzii.
3. **Lactoferrin and sCR1 are conditional-GREEN candidates.** Both have favorable host-physiology fit, both bottleneck on the same anoxic-environment-disulfide-folding question (lactoferrin 17 disulfides, sCR1 SCR1-4 8 disulfides). Mitigatable via heterologous DsbA/DsbB co-expression but not yet validated experimentally.
4. **The engineering-toolkit gap (0.25 across all payloads) is the gating factor.** As of 2026-05, **F. prausnitzii has no published transformation protocol.** The 2023 [Sheridan review of gut-bacteria genetic manipulation](https://doi.org/10.20517/mrr.2022.13) covers Bifidobacterium, Bacteroides, Roseburia, E. rectale — not F. prausnitzii. The literature workaround: MAM (F. prausnitzii's anti-inflammatory effector protein) is delivered to mouse gut via *Lactococcus lactis* carrying the plasmid ([Quévrain 2016](https://doi.org/10.1136/gutjnl-2014-307649); [Breyner 2017](https://doi.org/10.3389/fmicb.2017.00114)) — researchers engineered *L. lactis*, not F. prausnitzii. Closest engineering precedent for adapting a toolkit: Roseburia inulinivorans conjugation ([Sheridan 2019 Anaerobe doi:10.1016/j.anaerobe.2019.06.008](https://doi.org/10.1016/j.anaerobe.2019.06.008); [Sheridan 2020 Bio Protoc doi:10.21769/BioProtoc.3575](https://doi.org/10.21769/BioProtoc.3575)) — Lachnospiraceae phylogenetic neighbor, conjugative-transposon-based, 10⁻⁴ to 10⁻⁶ transconjugants/recipient. Estimated 1-2 yr to adapt to F. prausnitzii A2-165.

## Codon / GC / secretion summary

- **Genome:** 2.78-3.23 Mbp, **56.6% GC** ([Fraccascia 2022 doi:10.1128/mra.00824-22](https://doi.org/10.1128/mra.00824-22)). A2-165 = JCM 31915 = DSM 17677, reclassified as *F. duncaniae* by [Sakamoto 2022](https://doi.org/10.1099/ijsem.0.005379).
- **GC match:** human payloads ~58% GC ↔ Fp 56.6% — only 1.4 pp mismatch, **best of any chassis in the LBP track** (vs Bacteroides 43%, EcN 51%). A. flavus uricase ~52% GC, 4-5 pp mismatch. Codon-optimization low-cost ($1-5K/cassette).
- **Secretion:** Sec-translocon (SecA/Y/E) + Tat-translocon (TatABC) both annotated. Native MAM secretion documented ([Quévrain 2016](https://doi.org/10.1136/gutjnl-2014-307649)). Heterologous-payload secretion titers never measured.

## Cross-reference for engineered-lbp-chassis Phase 2

This comp informs / decides:

- **P2-4 (this comp):** complete; Fp engineering-naive as of 2026-05; Phase 2 should prioritize toolkit development BEFORE payload selection. **P2-6 (chassis matrix):** uricase belongs on EcN or koji; butyrate-boost belongs on Fp; lactoferrin / sCR1 routable to Fp or Bacteroides pending disulfide-folding investigation.
- **Wet-lab sequence (if committed):** (1) adapt Sheridan 2019 Lachnospiraceae conjugation toolkit, (2) chromosomally boost native BCoAT, (3) heterologously secrete a small reporter (e.g. NanoLuc) via Sec, (4) only then attempt lactoferrin / sCR1.
- **comp-007 cross-link:** butyrate was the top food-grade HDAC inhibitor by isoform selectivity (167× class-I over HDAC6). Continuous gut-luminal butyrate from engineered Fp solves oral bioavailability — comp-008 says it's the FIRST plausible engineering campaign in this chassis.
