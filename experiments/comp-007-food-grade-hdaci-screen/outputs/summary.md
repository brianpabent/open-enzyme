# comp-007: Food-Grade HDAC Inhibitor Screen — Summary

**Date:** 2026-05-05
**Experiment:** Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue
**Informs:** [`validation-experiments.md` §1.22](../../wiki/validation-experiments.md#122-gut-selective-food-grade-hdac-inhibitor-screen-for-q141k-abcg2-trafficking-rescue)
**Interpretive wiki page:** [`wiki/food-grade-hdaci-screen-computational.md`](../../wiki/food-grade-hdaci-screen-computational.md)

## Scoring formula

```
composite_score = potency_score × selectivity_score × gut_selectivity_score
```

| Factor | Definition | Range |
|---|---|---|
| **potency_score** | 1/mean(HDAC1/2/3 geometric-mean IC50 nM), max-normalized | 0–1 |
| **selectivity_score** | HDAC6_IC50 / (HDAC6_IC50 + mean_class_I_IC50), normalized at midpoint ratio=10 | 0–1 |
| **gut_selectivity_score** | 1 − oral bioavailability fraction | 0–1 |

Compounds with DATA_UNAVAILABLE confidence (no usable IC50 or estimate) receive composite_score = 0.
Compounds with unknown HDAC6 selectivity receive selectivity_score = 0.30 (penalty vs butyrate's confirmed 222× selectivity).

## Ranking table

| Rank | Compound | Mean HDAC1-3 IC50 (nM) | HDAC6 IC50 (nM) | Sel. ratio | Oral BA | Potency (norm) | Sel. score | Gut score | Composite | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Butyrate** | 12,000 | 2,000,000 | 167× | 5% | 0.417 | 0.943 | 0.950 | **0.3734** | HIGH |
| 2 | **Sulforaphane** | 5,000* | N/A | unknown | 70% | 1.000 | 0.300 | 0.300 | **0.0900** | LOW |
| 3 | **PEITC** | 10,000* | N/A | unknown | 60% | 0.500 | 0.300 | 0.400 | **0.0600** | LOW |
| 4 | **Allyl Mercaptan** | 50,000* | N/A | unknown | 25% | 0.100 | 0.300 | 0.750 | **0.0225** | LOW |
| 5 | **DADS** | 1,000,000* | N/A | unknown | 40% | 0.005 | 0.300 | 0.600 | **0.0009** | LOW |
| 6 | **Caffeic Acid** | N/A | N/A | unknown | 33% | 0.000 | 0.000 | 0.670 | **0.0000** | DATA_UNAVAILABLE |
| 7 | **Ferulic Acid** | N/A | N/A | unknown | 30% | 0.000 | 0.000 | 0.700 | **0.0000** | DATA_UNAVAILABLE |

\* = estimated value (see `inputs/provenance.md`); actual IC50 unavailable from ChEMBL or primary literature

## Top candidates and Stage 2 recommendation

### Rank 1: Butyrate (composite 0.3734)

- **Mean HDAC1/2/3 IC50:** 12,000 nM (confidence: HIGH)
- **HDAC6 IC50:** 2,000,000 nM
- **HDAC6 selectivity ratio:** 167×
- **Oral bioavailability:** 5%
- **Food source:** Colonic fermentation of dietary fiber (gut-derived); also butter, ghee
- **HDAC mechanism:** Zinc-chelating short-chain fatty acid; direct active-site inhibitor of class I and class II HDACs via carboxylate coordination of catalytic zinc...

### Rank 2: Sulforaphane (composite 0.0900)

- **Mean HDAC1/2/3 IC50:** estimated 5,000 nM
- **HDAC6 selectivity ratio:** Unknown (penalty score 0.30 applied)
- **Oral bioavailability:** 70%
- **Food source:** Broccoli sprouts (highest: ~73 mg/100 g fresh), broccoli, cauliflower, Brussels sprouts

### Rank 3: PEITC (composite 0.0600)

- **Mean HDAC1/2/3 IC50:** estimated 10,000 nM
- **HDAC6 selectivity ratio:** Unknown (penalty score 0.30 applied)
- **Oral bioavailability:** 60%
- **Food source:** Watercress, garden cress, papaya seeds — gluconasturtiin hydrolysis product

### Rank 4: Allyl Mercaptan (composite 0.0225)

- **Mean HDAC1/2/3 IC50:** estimated 50,000 nM
- **HDAC6 selectivity ratio:** Unknown (penalty score 0.30 applied)
- **Oral bioavailability:** 25%
- **Food source:** Garlic metabolite — produced from DADS and DATS by intestinal and hepatic metabolism

### Rank 5: DADS (composite 0.0009)

- **Mean HDAC1/2/3 IC50:** estimated 1,000,000 nM
- **HDAC6 selectivity ratio:** Unknown (penalty score 0.30 applied)
- **Oral bioavailability:** 40%
- **Food source:** Garlic oil (major component: ~60% of garlic oil organosulfur compounds)

### Compounds scored 0 (DATA_UNAVAILABLE — Stage 1 gap)

The following candidates have no usable isoform-specific IC50 data from ChEMBL or primary literature.
They are not ranked but are not excluded — they require a targeted biochemical screen at Stage 2 to obtain scoreable data.

- **Caffeic Acid** — Coffee (major polyphenol), blueberries, apples, eggplant, red wine, olive oil. Hydroxycinnamic acid with catechol moiety; HDAC inhibition proposed via catechol-metal chelation but no isoform-specific...
- **Ferulic Acid** — Wheat bran (major source: ~0.4-0.8 mg/g), rice bran, corn, oats, tomatoes. Hydroxycinnamic acid; shows histone H3 hyperacetylation in MCF-7 and HeLa cells (PMID 27588384), consistent with HDAC in...

## Stage 2 advancement decision

**Advance to Stage 2 (paired Caco-2 / HepG2 HDAC activity assay):**

- **Butyrate** (rank 1, score 0.3734) — Confirmed class-I selectivity (167×). IC50 from biochemical assay (high confidence).
- **Sulforaphane** (rank 2, score 0.0900) — HDAC6 selectivity unconfirmed — Stage 2 must include HDAC6 isoform-selective substrate assay. IC50 is estimated (Stage 2 will confirm or falsify the ranking position).
- **PEITC** (rank 3, score 0.0600) — HDAC6 selectivity unconfirmed — Stage 2 must include HDAC6 isoform-selective substrate assay. IC50 is estimated (Stage 2 will confirm or falsify the ranking position).

**Drop from Stage 2 (DATA_UNAVAILABLE — redirect to biochemical IC50 screen first):**

- **Caffeic Acid** — no isoform-specific IC50 data available. Recommend targeted HDAC1/2/3 biochemical assay before Stage 2 cellular work.
- **Ferulic Acid** — no isoform-specific IC50 data available. Recommend targeted HDAC1/2/3 biochemical assay before Stage 2 cellular work.

## Data gaps materially affecting the ranking

- Sulforaphane: no isoform-specific IC50; effective estimate used (LOW confidence); HDAC6 selectivity unknown (penalty applied)
- Allyl Mercaptan: no ChEMBL entry; estimated from bulk nuclear extract (LOW confidence); HDAC6 selectivity unknown
- DADS: no ChEMBL entry; estimated from bulk nuclear extract (LOW confidence); HDAC6 selectivity unknown
- PEITC: no ChEMBL entry; estimated by analogy with sulforaphane (LOW confidence); HDAC6 selectivity unknown
- Caffeic Acid: no isoform IC50 available in ChEMBL or primary literature; scored 0 (DATA_UNAVAILABLE)
- Ferulic Acid: no isoform IC50 available in ChEMBL or primary literature; scored 0 (DATA_UNAVAILABLE)

## Limitations

- Heterogeneous assay formats: butyrate IC50 values from biochemical recombinant assay (highest confidence); sulforaphane/AM/DADS from nuclear extract or cellular protein level (lower confidence). Direct comparison is approximate.
- HDAC6 selectivity data absent for sulforaphane, AM, DADS, PEITC. Unknown penalty (0.30) penalizes these compounds vs butyrate (confirmed 222x selectivity). If HDAC6 IC50 were measured and found to be >1 mM for these compounds, their scores would increase substantially.
- Gut-vs-systemic proxy (1 - oral BA) is a coarse surrogate. High oral BA (sulforaphane) reduces gut-selectivity score, but SFN reaches enterocytes before portal absorption — the gut mucosal cell may still have substantial SFN exposure. This proxy underestimates SFN's enterocyte-level activity.
- Oral bioavailability values are estimates from literature rather than direct human PK measurements at food-achievable doses.
- Q141K trafficking rescue (the key outcome) has not been tested for any compound except the vorinostat class-I reference compound (Basseville 2012). Butyrate's class-I selectivity and IC50 predict rescue, but direct demonstration is Stage 3.
- Evidence level: all analyses are Mechanistic Extrapolation per Open Enzyme wiki evidence-level convention. No wet-lab confirmation at Stage 1.

## Provenance

All source data, ChEMBL activity IDs, and PubMed citations: [`inputs/provenance.md`](../inputs/provenance.md)

**Evidence level:** Mechanistic Extrapolation (per Open Enzyme wiki evidence-level convention). No wet-lab data has been generated for comp-007. Rankings reflect published biochemical and cellular IC50 data plus literature-derived estimates where primary IC50 data is absent.