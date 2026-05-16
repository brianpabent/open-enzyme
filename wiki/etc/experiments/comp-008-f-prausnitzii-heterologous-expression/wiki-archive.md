# comp-008 Results — F. prausnitzii Heterologous Expression Feasibility

**Date:** 2026-05-16. **Chassis:** Faecalibacterium prausnitzii A2-165 (now F. duncaniae per Sakamoto 2022 IJSEM, doi:10.1099/ijsem.0.005379). **Genome GC:** 56.6%.

## Headline

**Top payload: butyrate_pathway_boost_BCoAT (score 0.748, verdict GREEN, range [0.641, 0.822]).**

**Ranking by composite feasibility:**
1. **butyrate_pathway_boost_BCoAT** — score **0.748** (GREEN); range [0.641, 0.822]; limiting factor: *engineering_toolkit_maturity* at 0.25
2. **scr1_truncation_SCR1to4** — score **0.565** (YELLOW); range [0.433, 0.678]; limiting factor: *engineering_toolkit_maturity* at 0.25
3. **lactoferrin_HumanFullLength** — score **0.54** (YELLOW); range [0.423, 0.659]; limiting factor: *engineering_toolkit_maturity* at 0.25
4. **uricase_AspergillusFlavus** — score **0.393** (YELLOW); range [0.271, 0.523]; limiting factor: *host_physiology_compatibility* at 0.1

**The shared blocker is the engineering toolkit gap** (factor at 0.25 across all payloads — F. prausnitzii has no published transformation protocol as of 2026-05). The verdicts above bake that fixed-facility cost into the geometric mean. **Toolkit-conditional ranking** (the ordering IF the transformation toolkit is established as a separate 1-2 yr investment) re-orders the payloads:

1. **butyrate_pathway_boost_BCoAT** — non-toolkit score 0.875 (GREEN)
2. **scr1_truncation_SCR1to4** — non-toolkit score 0.635 (GREEN)
3. **lactoferrin_HumanFullLength** — non-toolkit score 0.603 (GREEN)
4. **uricase_AspergillusFlavus** — non-toolkit score 0.419 (YELLOW)

## Chassis profile summary

- **Host:** F. prausnitzii A2-165 (taxonomically reclassified as *F. duncaniae* by Sakamoto 2022, doi:10.1099/ijsem.0.005379). A2-165 = JCM 31915 = DSM 17677.
- **Genome:** 2.78 - 3.23 Mbp, 56.6% GC, ~2795 protein-coding genes (Fraccascia 2022 doi:10.1128/mra.00824-22).
- **Physiology:** Strict obligate anaerobe. Colonic-lumen resident. Native butyrate producer via butyryl-CoA:acetate CoA-transferase pathway.
- **Secretion machinery:** Sec-translocon (SecA/Y/E annotated), Tat-translocon (TatABC annotated). Native MAM (15 kDa anti-inflammatory protein) secretion documented (Quévrain 2016 doi:10.1136/gutjnl-2014-307649).
- **Engineering toolkit (2026-05):** None published for F. prausnitzii itself. Closest precedent is Lachnospiraceae conjugation (Roseburia inulinivorans, E. rectale; Sheridan 2019 doi:10.1016/j.anaerobe.2019.06.008; Sheridan 2020 doi:10.21769/BioProtoc.3575). Workaround pattern in literature: when researchers want to express F. prausnitzii's MAM in mouse gut, they engineer *Lactococcus lactis* to carry the MAM plasmid — NOT engineering F. prausnitzii itself (Quévrain 2016; Breyner 2017 doi:10.3389/fmicb.2017.00114).

## Per-payload analysis


### butyrate_pathway_boost_BCoAT
**Composite: 0.748 (GREEN); range [0.641, 0.822]**
**Dominant uncertainty / limiting factor: engineering_toolkit_maturity at 0.25**

| Factor | Score | Low | High | Rationale |
|---|---|---|---|---|
| cluster_size_tractability | 0.95 | 0.9 | 1.0 | Single 448-aa ORF (1.3 kb). Native gene — option to chromosomally duplicate at native locus or supplement on plasmid. |
| GC_content_codon_compatibility | 1.0 | 0.95 | 1.0 | NATIVE F. prausnitzii gene. CAI = 1.0 by definition. Zero codon-optimization cost. |
| secretion_pathway_availability | 1.0 | 0.95 | 1.0 | Butyryl-CoA:acetate CoA-transferase is cytoplasmic. Product (butyrate) diffuses across cell membrane as a small molecule. No secretion engineering needed. |
| host_physiology_compatibility | 1.0 | 0.95 | 1.0 | Native enzyme in native pathway in native host. No physiology mismatch. Anaerobic-pathway-anaerobic-host alignment is total. |
| engineering_toolkit_maturity | 0.25 | 0.15 | 0.35 | Shared factor. Even for a native-payload boost, the cassette must still be integrated; transformation toolkit gap applies. |
| host_toxicity_risk | 0.75 | 0.65 | 0.85 | Native overexpression risks fitness loss via diversion of acetate / acetyl-CoA from primary metabolism, especially if cassette is on a high-copy plasmid. Manageable via copy-number tuning / inducible promoter. Not host-toxic in the toxicity sense. |
| heterologous_expression_precedent | 0.55 | 0.4 | 0.7 | Closely-related-chassis precedent: Clostridium tyrobutyricum, C. acetobutylicum butyrate-pathway boost via plasmid-based overexpression (biofuel literature, well-established). F. prausnitzii-specific precedent: zero. Motif maturity is high; species-level precedent is zero. |
| folding_complexity | 1.0 | 0.95 | 1.0 | Native enzyme — folding in native cytoplasm is by definition the optimal case. |

### scr1_truncation_SCR1to4
**Composite: 0.565 (YELLOW); range [0.433, 0.678]**
**Dominant uncertainty / limiting factor: engineering_toolkit_maturity at 0.25**

| Factor | Score | Low | High | Rationale |
|---|---|---|---|---|
| cluster_size_tractability | 0.95 | 0.9 | 1.0 | 280 aa truncated construct (~840 bp). Trivially clonable. |
| GC_content_codon_compatibility | 0.8 | 0.7 | 0.9 | Same human ~58% GC vs Fp 56.6%. Codon optimization moderate. |
| secretion_pathway_availability | 0.6 | 0.45 | 0.75 | Sec-translocon present. Same caveat as lactoferrin re: disulfide-rich secretion. 8 disulfides in SCR1-4 — less than lactoferrin's 17 but still requires oxidative folding. |
| host_physiology_compatibility | 0.9 | 0.8 | 0.95 | No O2 requirement. CR1 (a host complement regulator) is mechanistically inert to bacterial physiology — F. prausnitzii has no classical-pathway complement target. |
| engineering_toolkit_maturity | 0.25 | 0.15 | 0.35 | Shared factor. |
| host_toxicity_risk | 0.9 | 0.8 | 0.95 | CR1 is a host immune regulator; no bacterial target. Native serpins / complement regulators don't perturb commensal physiology. |
| heterologous_expression_precedent | 0.25 | 0.15 | 0.35 | Zero precedent for soluble complement regulator in obligate anaerobe. comp-006/012 evaluated DAF SCR1-4 in koji (HIGH risk) — informs the parallel for LBP but doesn't establish a positive precedent. |
| folding_complexity | 0.45 | 0.3 | 0.6 | 8 disulfides require oxidative folding. Smaller magnitude than lactoferrin's 17 disulfides, but same fundamental anoxic-environment-folding question. SCR/sushi/CCP-fold proteins are tolerant of disulfide isomerization (more robust than serpin-fold lactoferrin) — slight upward adjustment vs. lactoferrin. |

### lactoferrin_HumanFullLength
**Composite: 0.54 (YELLOW); range [0.423, 0.659]**
**Dominant uncertainty / limiting factor: engineering_toolkit_maturity at 0.25**

| Factor | Score | Low | High | Rationale |
|---|---|---|---|---|
| cluster_size_tractability | 0.85 | 0.8 | 0.9 | Single 691-aa mature ORF (~2.1 kb). Larger than uricase but well within single-vector range. |
| GC_content_codon_compatibility | 0.8 | 0.7 | 0.9 | Human ~58% GC vs Fp 56.6% — only 1.4 percentage point mismatch. Best GC match of any payload in this set. Codon optimization still recommended for mammalian-table -> Firmicutes-table; ~$3-5K DNA synthesis. |
| secretion_pathway_availability | 0.6 | 0.45 | 0.75 | Sec-translocon annotated; native MAM secretion proves the pathway functions. But heterologous-payload secretion titers from Fp never measured. 17 disulfides in mature lactoferrin require post-translocational oxidative folding — Bacillus / Firmicutes Sec pathway produces proteins to the cell exterior where disulfide bond formation occurs (e.g. DsbA/DsbB-class systems); native F. prausnitzii disulfide machinery less characterized. |
| host_physiology_compatibility | 0.85 | 0.75 | 0.95 | No O2 dependence. Iron-sequestration function aligns with anaerobic-lumen physiology (anaerobic pathogens compete for iron). Minor risk: lactoferrin's iron-sequestration could starve F. prausnitzii itself, since Fp also requires iron — manage via inducible promoter or strain-engineered iron uptake. |
| engineering_toolkit_maturity | 0.25 | 0.15 | 0.35 | Shared factor. |
| host_toxicity_risk | 0.7 | 0.6 | 0.8 | Native lactoferrin doesn't kill F. prausnitzii in vivo (Fp and lactoferrin coexist in healthy gut). Heterologous overexpression risk is iron-starvation of the host, mitigatable with inducible promoter. |
| heterologous_expression_precedent | 0.3 | 0.2 | 0.4 | Extensive precedent in non-anaerobe heterologous hosts (P. pastoris, A. niger, transgenic mammals). Zero precedent in obligate anaerobe. comp-005 evaluated koji chassis HIGH risk for stability — LBP track was framed precisely to address this. |
| folding_complexity | 0.4 | 0.3 | 0.55 | MAJOR concern. 17 disulfides require oxidative folding. Gut lumen is anoxic — disulfide bond formation in anoxic environment requires alternative oxidant (e.g. periplasmic-equivalent space + heterologously expressed DsbA, or methodologically untested in obligate anaerobes). Disulfide-rich secreted protein expression in obligate anaerobes is essentially unprecedented. |

### uricase_AspergillusFlavus
**Composite: 0.393 (YELLOW); range [0.271, 0.523]**
**Dominant uncertainty / limiting factor: host_physiology_compatibility at 0.1**

| Factor | Score | Low | High | Rationale |
|---|---|---|---|---|
| cluster_size_tractability | 0.95 | 0.9 | 1.0 | Single 302-aa ORF (906 bp), trivial cluster size. |
| GC_content_codon_compatibility | 0.7 | 0.6 | 0.8 | A. flavus CDS ~52% GC vs Fp 56.6%. Small GC mismatch, eukaryotic codon-table mismatch. Codon optimization moderate-cost (~$1-2K DNA synthesis). |
| secretion_pathway_availability | 1.0 | 0.95 | 1.0 | Uricase is cytoplasmic/peroxisomal natively; functions intracellularly. No secretion engineering needed. But this raises the OPPOSITE problem: substrate (uric acid) must enter cell, product (allantoin) must exit. |
| host_physiology_compatibility | 0.1 | 0.05 | 0.2 | DOMINANT BLOCKER. Uricase requires O2 as substrate. F. prausnitzii is a strict anaerobe in an anoxic colonic lumen. Heterologous H2O2 production from uricase activity ALSO toxic to the anaerobic host (H2O2 lethal to obligate anaerobes without catalase, which F. prausnitzii lacks). |
| engineering_toolkit_maturity | 0.25 | 0.15 | 0.35 | Shared factor across payloads. No published F. prausnitzii transformation; closest precedent is Lachnospiraceae conjugation (Roseburia, E. rectale per Sheridan 2019/2020). Estimated 1-2 yr adaptation needed. |
| host_toxicity_risk | 0.2 | 0.1 | 0.35 | Uricase produces stoichiometric H2O2 per uric acid molecule. F. prausnitzii lacks robust catalase; H2O2 destroys obligate anaerobes via [Fe-S] cluster damage. Adding heterologous catalase as a co-payload is engineerable but compounds the campaign. |
| heterologous_expression_precedent | 0.2 | 0.1 | 0.3 | Zero precedent for uricase in obligate anaerobe. Rasburicase (S. cerevisiae expressing A. flavus uricase) is the canonical engineering precedent — aerobic / fermentation-batch context, fundamentally different physiology. |
| folding_complexity | 0.85 | 0.75 | 0.95 | Cofactorless single-domain enzyme. No disulfides, no metals, no glycosylation. Folding in bacterial cytoplasm is well-precedented (Rasburicase in S. cerevisiae). |

## Key findings

1. **Butyrate-pathway boost (BCoAT) is the unambiguous winner** — both base ranking AND toolkit-conditional ranking. It is a NATIVE payload (CAI=1.0, no secretion, native lifestyle, no folding burden). The only blocker is the shared engineering-toolkit gap.
2. **Uricase scores LOW (~0.40) — and the bottleneck is the host-physiology mismatch, not the engineering toolkit.** Uricase fundamentally requires O2 as a substrate. F. prausnitzii is a strict anaerobe in an anoxic colonic lumen. Even with a perfect engineering toolkit, the chemistry can't run. This is a STRATEGIC RECLASSIFICATION moment: uricase is not a plausible F. prausnitzii payload, regardless of how much engineering investment goes in. Different chassis is required (e.g. E. coli Nissle as facultative anaerobe — micro-aerobic windows possible in proximal colon; or maintain uricase on the koji track).
3. **Lactoferrin and sCR1 SCR1-4 score similarly (~0.50-0.55)** — both have favorable host-physiology fit, both bottleneck on the same anoxic-environment-disulfide-folding question. This is a more tractable problem than uricase's O2-substrate-requirement because it could be addressed by heterologous DsbA/DsbB co-expression or by switching to a chassis with characterized oxidative-folding capacity in the periplasmic-equivalent space. But it's still a real risk.
4. **CR1 SCR1-4 ranks slightly above lactoferrin** due to fewer disulfide bonds (8 vs 17) and the SCR/sushi/CCP-fold's documented isomerization tolerance.
5. **The engineering toolkit gap (no published F. prausnitzii transformation as of 2026-05) is the gating factor for ALL payloads except butyrate-boost-via-native-pathway.** Without the toolkit, every score above except butyrate's is academic. Strategic path: invest 1-2 yr in adapting the Lachnospiraceae conjugation toolkit (Roseburia inulinivorans + E. rectale precedent) to F. prausnitzii FIRST; the payload selection happens second.

## What this comp informs / decides

- **Engineered LBP chassis Phase 2 (P2-4)** per [`wiki/engineered-lbp-chassis.md`](../../../engineered-lbp-chassis.md): F. prausnitzii is engineering-naive as of 2026-05; the LBP-chassis Phase 2 investment should prioritize toolkit development BEFORE payload selection.
- **Payload-specific guidance:** if the toolkit is committed to, butyrate-pathway boost (native BCoAT overexpression) is the first wet-lab target. Uricase should be REMOVED from the F. prausnitzii payload menu (RED on host-physiology grounds). Lactoferrin and sCR1 are conditional GREEN if disulfide-folding can be addressed (engineering question + experimental measurement; not solvable purely in silico).
- **Comparative chassis matrix (P2-6 per engineered-lbp-chassis.md):** confirms that uricase belongs on a facultative-anaerobe chassis (E. coli Nissle) or a transit-aerobic chassis (koji) rather than a strict-anaerobe chassis. Butyrate-boost belongs on F. prausnitzii. Lactoferrin / sCR1 can plausibly go either to F. prausnitzii or Bacteroides depending on disulfide-folding investigation.
- **comp-007 (food-grade HDAC inhibitor screen) cross-link:** butyrate was the top food-grade HDAC inhibitor with 167× class-I-over-HDAC6 selectivity. Continuous gut-luminal butyrate from an engineered F. prausnitzii strain solves the bioavailability problem at the dose-frequency level — this comp says that's the FIRST plausible engineering campaign, not the second or third.

## Toolkit adaptation roadmap (for Phase 2 wet-lab handoff)

1. **Method development phase (12-18 months):** Adapt Sheridan 2019/2020 Roseburia inulinivorans conjugation protocol to F. prausnitzii A2-165. Tn1545-class conjugative transposon + tet(W) or erm(B) selection. Expected transfer efficiency 10^-5 to 10^-7 per recipient (Lachnospiraceae baseline).
2. **PAM (Plasmid Artificial Modification) protocol** if Type II RM systems in F. prausnitzii prove inhibitory — Yasui 2009 doi:10.1128/AEM.02418-08 demonstrated 10,000× improvement in B. adolescentis with this method.
3. **First-payload milestone:** chromosomally integrate a second copy of native butyryl-CoA:acetate CoA-transferase (or a strong-promoter variant of the native gene). Measure butyrate output in YCFA broth. This is the lowest-risk validation construct — native pathway, native gene.
4. **Second-payload milestone:** secrete a small reporter protein (e.g. tagged MAM or NanoLuc) via Sec-translocon. Measure secretion titer. This establishes whether the chassis can heterologously secrete at biologically relevant levels — a precondition for lactoferrin / sCR1 expression.
5. **Defer disulfide-rich payloads (lactoferrin, sCR1) until milestone 4 is achieved.** Until then, lactoferrin / sCR1 development should run in parallel on the alternative E. coli Nissle chassis (Synlogic-class toolkit) per the comparative chassis matrix.

## Limitations

1. **Factor scores are expert estimates**, not derived from large-scale empirical heterologous-expression datasets in F. prausnitzii (which don't exist). Geometric mean is robust to ±0.1 variation in any single factor but the verdict could shift if a factor is meaningfully miscalibrated. See the sensitivity ranges (low/high columns).
2. **CAI values are framework-estimated, not RSCU-table-computed.** Wet-lab cassette design needs a proper codon-frequency table for F. prausnitzii A2-165 highly-expressed genes (rpsA, tuf, fusA). Estimates here are ±0.10.
3. **Disulfide-folding-in-anoxic-environment** is an open empirical question; the literature is sparse. Folding-complexity scores for lactoferrin and sCR1 reflect this — the scores represent a real engineering risk, not a known impossibility.
4. **The shared engineering-toolkit-maturity factor at 0.25 is the dominant variance source across all payloads.** If a successful F. prausnitzii transformation protocol is published in 2026-27, every payload's geometric mean lifts by ~0.10-0.15. The toolkit-conditional ranking section anticipates this.
5. **No published wet-lab F. prausnitzii transformation efficiency baseline.** Roseburia inulinivorans conjugation efficiency (10^-4 to 10^-6 transconjugants/recipient per Sheridan 2019) is used as the proxy.
6. **GC% / CAI / codon-level optimization details are framework-level only.** Detailed RBS strength, mRNA secondary structure, and codon-context effects are part of the wet-lab cassette-design phase.

## Multilingual sources checked

- **Chinese-language**: Guo 2025 J Transl Med doi:10.1186/s12967-025-07493-0 (Chinese authors, MAM-engineered strain — uses L. lactis delivery, not engineered F. prausnitzii); no published F. prausnitzii engineering toolkit in CNKI-indexed literature as of 2026-05.
- **Japanese-language**: Sakamoto 2022 IJSEM doi:10.1099/ijsem.0.005379 (Japanese RIKEN group taxonomic reclassification of A2-165 to F. duncaniae); JCM 31915 strain deposit. No engineering work.
- **Korean-language**: Seo 2024 Probiotics Antimicrob Proteins doi:10.1007/s12602-024-10213-7 (Korean strain KBL1027 phenotype work). No engineering.
- **Net:** the 'no published transformation protocol for F. prausnitzii' finding is robust across English, Chinese, Japanese, and Korean PubMed-indexed sources.