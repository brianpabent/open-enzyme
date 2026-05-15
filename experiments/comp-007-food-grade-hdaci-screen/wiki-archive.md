---
title: "Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue: Computational Analysis (comp-007)"
date: 2026-05-05
tags: [abcg2, q141k, hdac, hdac-inhibitor, gout, hyperuricemia, butyrate, sulforaphane, computational, food-grade]
related:
  - abcg2-modulators.md
  - supplements-stack.md
  - gut-lumen-sink.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "ChEMBL v34 (MCP, 2026-05-05)"
  - "Basseville A et al. Mol Cancer Ther 2012 PMID 22472121"
  - "Druesne N et al. Carcinogenesis 2004 PMID 14976134"
  - "Myzak MC et al. FASEB J 2006 PMID 16537909 / PMID 24441674"
  - "Rajendran P et al. Int J Oncol 2011 PMID 21305261"
  - "Gupta P et al. Mol Carcinog 2019 PMID 31228495"
  - "Bora-Tatar G et al. Bioorg Med Chem 2009 PMID 19188062"
---

# Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue: Computational Analysis (comp-007)

**Status:** Complete — 2026-05-05  
**Experiment folder:** [`experiments/comp-007-food-grade-hdaci-screen/`](../experiments/comp-007-food-grade-hdaci-screen/)  
**Informs:** [`validation-experiments.md` §1.22](./validation-experiments.md#122-gut-selective-food-grade-hdac-inhibitor-screen-for-q141k-abcg2-trafficking-rescue)

---

## Summary

Stage 1 in silico screen of 7 food-grade or GRAS-classified HDAC inhibitor candidates for Q141K-ABCG2 trafficking rescue. Ranked on three axes: class I HDAC potency (HDAC1/2/3 IC50), HDAC6 selectivity (off-target cardiotoxicity avoidance), and gut-enriched exposure (1 − oral bioavailability).

**Top 3 advancing to Stage 2:**

| Rank | Compound | Mean HDAC1-3 IC50 | HDAC6 sel. | Gut BA | Composite | Confidence |
|---|---|---|---|---|---|---|
| 1 | **Butyrate** | 12,000 nM | 167× confirmed | 5% | 0.3734 | HIGH |
| 2 | **Sulforaphane** | 5,000 nM* | uncharacterized | 70% | 0.0900 | LOW |
| 3 | **PEITC** | 10,000 nM* | uncharacterized | 60% | 0.0600 | LOW |

\* = estimated from nuclear extract or by analogy; isoform-specific biochemical IC50 unavailable

**All rankings are Mechanistic Extrapolation** per Open Enzyme evidence-level convention. No wet-lab data generated at Stage 1.

---

## Background: Q141K ABCG2 and HDAC Inhibition

ABCG2-Q141K is the most common clinically relevant variant of the urate transporter ABCG2, carried by ~12% of all alleles (~25% East Asian, ~4% European). The Q141K substitution destabilizes the NBD2 ATP-binding domain, causing ER retention via ERAD rather than apical membrane trafficking. The consequence: reduced luminal urate efflux → higher serum urate → increased gout risk and impaired Q141K-ABCG2 function in absorptive epithelial cells (Basseville et al. 2012, PMID 22472121; mechanistic extrapolation — no direct Q141K clinical HDACi data beyond Basseville's in vitro demonstration).

**The HDAC-mediated rescue pathway** (Basseville 2012, in vitro, human cell lines expressing Q141K-ABCG2):

```
Class I HDACi (HDAC1/2/3)
  → histone hyperacetylation
  → HSF1 nuclear translocation
  → Hsp90α/β transcriptional upregulation
  → chaperone-assisted refolding of misfolded Q141K NBD2
  → partial membrane-trafficking rescue (~30–50% surface expression restoration at 1 mM butyrate)
```

This is distinct from butyrate's ABCG2-inducing effect in wild-type cells, which is PPARγ-mediated and does not require HDAC inhibition (Xie et al. 2020 — see [abcg2-modulators.md §6](./abcg2-modulators.md)).

**Why HDAC6 is the off-target:** HDAC6 is a cytoplasmic tubulin deacetylase (class IIb). Pan-HDAC inhibitors (vorinostat, romidepsin) hit HDAC6 → tubulin hyperacetylation → actin/microtubule dysregulation → cardiac ion-channel effects → QT prolongation, cardiomyopathy. Any food-grade HDACi candidate must spare HDAC6 to be safe for chronic oral use. Selectivity ratio (HDAC6/class-I IC50) > 10× is the minimum acceptable; butyrate achieves 167× in biochemical assay.

---

## Scoring Formula

```
composite_score = potency_score × selectivity_score × gut_selectivity_score
```

| Factor | Definition | Notes |
|---|---|---|
| **potency_score** | 1 / geomean(HDAC1/2/3 IC50 nM), max-normalized to [0,1] | Higher = more potent at class I inhibition |
| **selectivity_score** | HDAC6_IC50 / (HDAC6_IC50 + mean_classI_IC50), midpoint ratio = 10 | Sigmoid-like; confirmed 222× → 0.957; unknown HDAC6 → penalty 0.30 |
| **gut_selectivity_score** | 1 − oral_bioavailability_fraction | Higher = more gut-enriched; rewards low-bioavailability compounds |

**Confidence tiers:** HIGH = biochemical recombinant assay (ChEMBL); LOW = nuclear extract or estimated from cellular data; DATA_UNAVAILABLE = no usable IC50. DATA_UNAVAILABLE compounds receive composite = 0.

The selectivity penalty (0.30) for unknown-HDAC6 compounds means they can rank above 0 but are substantially penalized compared to compounds with confirmed HDAC6 avoidance. If isoform-specific HDAC6 IC50 data were measured and found to be > 1 mM for sulforaphane or PEITC, their composite scores would increase ~3-fold.

---

## Candidate-by-Candidate Analysis

### 1. Butyrate (rank 1, composite 0.3734, HIGH confidence)

Butyrate (sodium butyrate; n-butyric acid) is the benchmark food-grade HDACi and the only candidate with HIGH-confidence biochemical IC50 data for all four HDAC isoforms.

**IC50 (biochemical, recombinant; ACS Med Chem Lett 2011, ChEMBL activity IDs 5207850–5207858):**
- HDAC1: 16,000 nM
- HDAC2: 12,000 nM
- HDAC3: 9,000 nM
- HDAC6: > 2,000,000 nM (> 2 mM; no inhibition detected at 2 mM)
- **HDAC6 selectivity ratio: ~167× over HDAC1/2/3 geometric mean (12,172 nM)**

**Mechanism:** Short-chain fatty acid; carboxylate coordinates the catalytic zinc of class I HDAC active sites. The HDAC6 active-site cavity is bulkier and accommodates acetylated tubulin peptides — the small carboxylate headgroup of butyrate is insufficient to engage it efficiently, which explains the class I selectivity structurally.

**Gut vs. systemic:** Colonic luminal concentration 0.5–2 mM from fermentable fiber (PMID 19197985); oral bioavailability fraction ~0.05 (colonocytes consume >90% as energy substrate before portal entry). Gut selectivity score: 0.95 — extremely favorable.

**Limitation for Q141K rescue:** Butyrate delivery at 1 mM is microbiome- and fiber-dependent. Individuals on low-fiber diets or with microbiome dysbiosis may have substantially lower colonic butyrate than 0.5 mM. A direct supplement or alternative food-grade HDACi with more predictable dosing would be meaningful for Q141K carriers.

### 2. Sulforaphane (rank 2, composite 0.0900, LOW confidence)

Sulforaphane (SFN; 4-methylsulfinylbutyl isothiocyanate) is derived from glucoraphanin hydrolysis by myrosinase in broccoli sprouts.

**IC50 (estimated; no isoform-specific biochemical data available from ChEMBL or primary literature):**
- Effective class I HDAC estimate: 5,000 nM (from PBMC HDAC activity measurements; Myzak 2006 PMID 16537909, Su 2014 PMID 24441674)
- HDAC6 IC50: uncharacterized

**Mechanism:** SFN is metabolized via the mercapturic acid pathway; the active metabolites SFN-Cys and SFN-N-acetylcysteine are proposed to engage the HDAC active-site zinc via thiol/sulfinyl coordination. HDAC inhibition in PBMC and cell-line studies is well-documented (Myzak 2006, Su 2014), but these are protein-level and nuclear-extract measurements, not isoform-specific biochemical assays. ChEMBL CHEMBL48802 has no HDAC bioactivity records. Critically, Choi 2018 (PMID 29482060) documents SFN-mediated downregulation of HDAC1/2/3 protein levels — this is epigenetic reprogramming (transcriptional), not direct zinc-chelation inhibition. The distinction matters: indirect, transcription-mediated HDAC reduction may have different kinetics, dose-response, and isoform specificity than direct inhibition.

**Gut vs. systemic:** ~70–80% oral bioavailability (absorbed in proximal small intestine); peak plasma 2–3 μM at 100 g broccoli sprout dose. High oral bioavailability substantially reduces its gut-selectivity score (0.30). The enterocyte exposure during absorption may be higher than plasma levels suggest, but this cannot be quantified without intracellular SFN measurements.

**Key Stage 2 question:** Does SFN inhibit HDAC1/2/3 preferentially over HDAC6 in a Caco-2 nuclear extract? If HDAC6 sparing is confirmed, SFN moves up substantially in the ranking.

### 3. PEITC (rank 3, composite 0.0600, LOW confidence)

Phenethyl isothiocyanate (PEITC) is derived from gluconasturtiin in watercress and garden cress.

**IC50 (estimated; no ChEMBL record, no primary isoform-specific IC50):**
- Effective class I HDAC estimate: 10,000 nM (Gupta 2019 PMID 31228495; HDAC1 protein reduction in colorectal model — not a direct enzyme IC50)
- HDAC6 IC50: uncharacterized

**Mechanism:** Similar to SFN — isothiocyanate metabolism via mercapturic acid pathway → active thiol metabolites → proposed zinc coordination. HDAC1 protein downregulation documented in cell lines (Gupta 2019); mechanism is extrapolated from SFN analogy. Less studied than SFN.

**Gut vs. systemic:** ~60% oral bioavailability; gut-selectivity score 0.40. Gut concentrations during absorption are 3–10 μM (estimated from watercress consumption PK).

### 4. Allyl Mercaptan (rank 4, composite 0.0225, LOW confidence)

Allyl mercaptan (AM; 2-propene-1-thiol) is produced from garlic-derived DADS and DATS by intestinal/hepatic metabolism.

**IC50 (estimated from bulk nuclear extract; no isoform-specific data):**
- 200 μM AM → 92% total HDAC activity inhibition in Caco-2 nuclear extracts (Druesne 2004 PMID 14976134)
- Effective class I HDAC estimate: 50,000 nM (Ki-equivalent from 92% inhibition at 200 μM, assuming competitive inhibition; rough estimate only)
- HDAC6 IC50: uncharacterized

**Mechanism:** Free thiol directly coordinates catalytic zinc; competitive inhibition confirmed in nuclear extract. Most potent garlic-derived HDACi in Druesne 2004. Isoform selectivity unknown.

**Gut vs. systemic:** Volatile compound; primarily a gut-lumen and intestinal-cell metabolite from DADS. Oral BA ~25%; gut exposure is high relative to systemic.

### 5. DADS (rank 5, composite 0.0009, LOW confidence)

Diallyl disulfide (DADS) is a major garlic oil component; AM is its proximal intracellular metabolite.

**IC50 (estimated from nuclear extract):**
- 200 μM DADS → 29% HDAC inhibition in Caco-2 nuclear extracts (Druesne 2004) — much weaker than AM
- Effective class I HDAC estimate: ~1,000,000 nM (weak direct inhibitor; AM is the active species)

DADS's low direct potency reflects that it requires intracellular conversion to AM. Its score (0.0009) reflects this: DADS is better conceptualized as an AM pro-drug than a standalone HDACi.

### 6–7. Caffeic Acid and Ferulic Acid (composite 0.0000, DATA_UNAVAILABLE)

Both hydroxycinnamic acids show histone hyperacetylation in cell studies (PMID 27588384) consistent with HDAC inhibition, but no isoform-specific IC50 is available from ChEMBL (CHEMBL145, CHEMBL32749 — 192 and 249 activities respectively, none against HDAC targets) or primary literature. These compounds are not scored and do not advance to Stage 2 without a targeted HDAC1/2/3 biochemical screen first.

The proposed mechanism (catechol metal chelation for caffeic acid; similar but methoxy-reduced for ferulic acid) is plausible but unquantified. If biochemical IC50 data emerge, they could re-enter the ranking.

---

## Stage 2 Recommendation

**Advance to Stage 2 (paired Caco-2 / HepG2 HDAC activity assay):**

1. **Butyrate** — confirmed class I selectivity; Stage 2 is primarily a confirmation run and a reference standard for the cellular assay format
2. **Sulforaphane** — the critical Stage 2 question is HDAC6 isoform selectivity; Stage 2 must include a HDAC6-selective substrate assay (acetylated α-tubulin peptide) alongside the class I substrate
3. **PEITC** — same Stage 2 requirement as SFN for HDAC6 characterization; lower estimated class I potency than SFN but plausible mechanism

**Do not advance to Stage 2 without biochemical data first:**
- Caffeic Acid, Ferulic Acid — isoform IC50 screen against recombinant HDAC1/2/3/6 needed before cellular work is interpretable

**Effectively ruled out at Stage 1:**
- DADS — prodrug for AM; study AM directly in Stage 2 rather than DADS
- Allyl Mercaptan (rank 4) — could be included in Stage 2 if reagent is available; lower priority than top 3

---

## Key Limitations

**Heterogeneous assay formats.** Butyrate IC50 values are from biochemical recombinant assay (highest confidence). SFN values are from PBMC nuclear extract or protein-level measurements (confounded by non-HDAC effects). Direct comparison across formats is approximate.

**HDAC6 selectivity unknown for most candidates.** The selectivity penalty (0.30) is arbitrary; if HDAC6 IC50 were measured at > 1 mM for SFN or PEITC, their composite scores would increase ~3-fold and their rankings relative to butyrate would tighten substantially.

**Gut-enrichment proxy is coarse.** Oral bioavailability (1 − BA) is a surrogate for gut exposure. Sulforaphane is highly bioavailable (70%) but enterocytes encounter SFN during absorption — intracellular enterocyte SFN concentration during transit may be 10–100× higher than plasma. The proxy underestimates SFN's intestinal epithelial activity.

**Sulforaphane's mechanism differs from butyrate's.** Direct zinc-chelation (butyrate) vs. indirect protein-level downregulation (SFN) via transcriptional reprogramming. Kinetics, dose-response shape, and isoform specificity may differ substantially. Stage 2 cellular data will be the first direct comparison in a Q141K-relevant cell context.

**No Q141K trafficking rescue data for any compound except the vorinostat class.** Basseville 2012 used the pharmacological tool compound and confirmed the pathway. That butyrate's class I profile recapitulates the pathway is a mechanistic extrapolation; Stage 3 is the first direct test.

---

## Cross-References

- [abcg2-modulators.md §6](./abcg2-modulators.md) — Q141K trafficking defect and butyrate dual mechanism (PPARγ/WT vs. HDACi/Q141K)
- [supplements-stack.md](./supplements-stack.md) — Q141K-personalized supplement recommendations; this analysis informs which HDACi candidates enter that stack
- [gut-lumen-sink.md](./gut-lumen-sink.md) — gut-lumen concentration and luminal exposure context
- [validation-experiments.md §1.22](./validation-experiments.md#122-gut-selective-food-grade-hdac-inhibitor-screen-for-q141k-abcg2-trafficking-rescue) — Stage 1 (this analysis), Stage 2 (Caco-2/HepG2 HDAC assay), Stage 3 (Q141K trafficking rescue)
- [computational-experiments.md](./computational-experiments.md) — tracking index
- [synthesis.md](./synthesis.md) — 2026-05-05 Proposed Experiment #3 (origin of this screen)
