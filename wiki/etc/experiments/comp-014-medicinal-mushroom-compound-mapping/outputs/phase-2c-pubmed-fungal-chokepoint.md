---
title: "Phase 2c — PubMed fungal × chokepoint literature scan"
date: 2026-05-06
phase: 2c
experiment: comp-014-medicinal-mushroom-compound-mapping
method: PubMed via NCBI E-utilities (mcp plugin), 17 searches across 3 axes, 92 abstracts read
---

# Phase 2c — PubMed Scan: Fungal Compounds × Open Enzyme Chokepoints

**Source:** PubMed via NCBI E-utilities. All findings cited by PMID with DOI where available. According to PubMed.

## Method

Three-axis search, 17 queries total, 92 article abstracts fetched:

- **Axis 1 (chokepoint × fungus):** XO, URAT1, NLRP3, ABCG2, complement/C5aR1, hyperuricemia/gout, Lp-PLA2, HDAC6, PPARγ, ergothioneine/thioredoxin/TXNIP. 10 searches.
- **Axis 2 (species × indication):** Ganoderma lucidum, Cordyceps militaris/sinensis, Trametes versicolor/PSK, Pleurotus ostreatus, Inonotus obliquus. 5 searches.
- **Axis 3 (multilingual catch-net):** TCM × mushroom × gout; Kampo × mushroom × inflammation. 2 searches.

Breadth-pass approach: titles + abstracts only, no full-text reads — Phase 5 will deep-dive top candidates.

## Top findings (high signal)

### Dual-chokepoint hit (single compound, in vivo)

**Ganoderma applanatum 2,4-DAE** [(PMID 35750011)](https://doi.org/10.1016/j.fitote.2022.105202) — 2,4-dihydroxybenzoic acid methyl ester inhibits BOTH xanthine oxidase AND down-regulates URAT1 in hyperuricemic mice. SUA reduced from 407 to 134 µmol/L. Computationally allopurinol-like; binds XO active site. **Strongest single-compound finding from the scan.**

### Direct URAT1 modulator (compound-level)

**Cordyceps militaris cordycepin** [(PMID 29422889)](https://pubmed.ncbi.nlm.nih.gov/29422889) — 3'-deoxyadenosine, dose-response in mice (15/30/60 mg/kg → SUA 216/210/203 µmol/L vs control 337). ELISA/RT-PCR/WB confirms URAT1 mechanism. Already pharmacologically characterized — top Phase 5 candidate.

### Clinical-grade evidence

**Cordyceps sinensis** has two systematic reviews / meta-analyses of RCTs:
- [(PMID 26457607)](https://doi.org/10.1002/14651858.CD009698.pub2) Cochrane review of 5 RCTs (n=447) in kidney transplant recipients — Cordyceps reduces hyperuricemia, hyperlipidemia, hyperglycemia, liver injury vs azathioprine.
- [(PMID 28137532)](https://doi.org/10.1016/j.ctim.2016.12.007) Meta-analysis of 9 RCTs — Cordyceps + cyclosporine A reduces hyperuricemia and CNI nephrotoxicity.

This is the highest evidence tier in the entire scan. Most of the source data is from Chinese clinical trials (CNKI). Confirms multilingual ingestion is load-bearing.

### Multi-chokepoint extract

**AMC-BFE (Cordyceps militaris × Astragalus biotransformation)** [(PMID 41905012)](https://doi.org/10.1016/j.bioorg.2026.109806) — 2026 paper — bidirectional fermentation produces extract that hits URAT1 + GLUT9 + ABCG2 + PPARα simultaneously. Isoflavone aglycones, nucleosides, polyols. Koji-relevant biotransformation comparator.

### ABCG2 + NLRP3 simultaneous hit

**Poria cocos in Fuling-Zexie formula** [(PMID 37788785)](https://doi.org/10.1016/j.jep.2023.117262) — TCM formula modulates ABCG2/GLUT9/OAT1 + suppresses NLRP3/ASC/cleaved-caspase-1. Poria is the only fungal ingredient; needs deconvolution to identify driver compound.

## Critical caveats

### Polysaccharide directionality problem

Ganoderma lucidum NLRP3 effects are **structure-dependent and opposite-direction**:

| Preparation | Effect on NLRP3 | Context |
|---|---|---|
| Exopolysaccharides (EPS) | **Activates** | Cryptococcus protection [(PMID 40450627)](https://doi.org/10.1007/s11046-025-00950-w) |
| Sporoderm-removed spore powder | **Inhibits** | Alzheimer model [(PMID 41378217)](https://doi.org/10.3389/fphar.2025.1690192) |
| GLP β-glucan | **Inhibits** | Cognitive dysfunction [(PMID 39522844)](https://doi.org/10.1016/j.jep.2024.119065) |
| GLPS polysaccharides | **Inhibits** | Liver injury [(PMID 30673679)](https://doi.org/10.1159/000493896) |

Triple-helix β-glucan conformation, MW, branching, and sulfation determine directionality [(PMID 40592243 review)](https://doi.org/10.1016/j.carres.2025.109591). **Phase 5 must specify polysaccharide structure** before claiming NLRP3 modulation. "Mushroom β-glucan inhibits NLRP3" without structural detail is not a defensible claim.

### C5aR1 platform gap (per validation-experiments.md §1.21)

**No direct fungal antagonist of C5aR1 surfaced in the PubMed scan.** Mushroom β-glucans **activate** complement via CR3/iC3b opsonization [(PMID 17895634)](https://pubmed.ncbi.nlm.nih.gov/17895634) — opposite of inhibition. Complement-inflammasome crosstalk review [(PMID 41983141)](https://doi.org/10.3389/fimmu.2026.1778759) confirms mechanistic synergy rationale (C3a/C5a/MAC prime NLRP3) but identifies no natural fungal small-molecule antagonist. **Phase 5 C5aR1 work will need synthetic-derivative or non-fungal source.** Whole-mushroom polysaccharide programs will not fill this gap.

## Novel chokepoints surfaced (not in current Open Enzyme map)

- **Mitophagy / PINK1** — Cordyceps cicadae [(PMID 40334761)](https://doi.org/10.1016/j.jep.2025.119926). Recommend adding to validation-experiments.md.
- **Adenosine deaminase (ADA)** — Ganoderma lucidum GLPP polysaccharide-peptide [(PMID 36385640)](https://doi.org/10.1039/d2fo02431d). Upstream of XO — earlier intervention point. Recommend adding to chokepoint map.

## Empty / thin chokepoints

- **Lp-PLA2:** 15 total hits, no direct fungal × Lp-PLA2 primary studies.
- **HDAC6:** 155 hits, no direct fungal antagonist papers.
- **Trametes versicolor / PSK × NLRP3:** only 2 hits total, neither directly relevant.
- **Pleurotus ostreatus:** 189 hits dominated by lovastatin/cholesterol — off-target for our XO/URAT1/NLRP3/C5aR1 frame.

## By-species summary

| Species | Strongest finding | Evidence |
|---|---|---|
| Ganoderma applanatum | 2,4-DAE dual XO+URAT1 | animal IN VIVO |
| Ganoderma lucidum | GLPP triple ADA+GLUT9+OAT1; multiple NLRP3 prep-dependent effects | animal |
| Cordyceps militaris | cordycepin URAT1 modulator | animal |
| Cordyceps sinensis | hyperuricemia reduction in transplant | CLINICAL meta-analysis |
| Cordyceps chanhua | XOD + chronic gout protection | animal (chronic rat) |
| Cordyceps cicadae | mitophagy / renal fibrosis | animal |
| Sanghuangporus vaninii | davallialactone XO IC50 = 90 µM | in vitro |
| Poria cocos | ABCG2 + NLRP3 (in TCM formula) | animal |
| Inonotus obliquus (chaga) | anticancer triterpenes; no direct gout chokepoint hit | in vitro |
| Trametes versicolor | thin (2 hits) | n/a |
| Pleurotus ostreatus | lovastatin/cholesterol axis; off-target | n/a |

## Phase 5 recommendations

1. **Top 3 single compounds for deep-dive:** Ganoderma applanatum 2,4-DAE; Cordyceps militaris cordycepin; Sanghuangporus vaninii davallialactone.
2. **Top extract for whole-organism modeling:** AMC-BFE (solid-state fermentation Cordyceps × Astragalus) — concrete koji-comparable workflow.
3. **Polysaccharide work demands structural specification** — don't claim NLRP3 modulation without naming the β-glucan conformation, MW, and branching.
4. **Add ADA + mitophagy to chokepoint map** in validation-experiments.md.
5. **C5aR1:** accept the platform gap or pivot to non-fungal/synthetic source. Don't waste Phase 5 cycles searching mushroom polysaccharides for C5aR1 antagonism.

## Counts

- Searches run: 17 (Axis 1: 10, Axis 2: 5, Axis 3: 2)
- Article metadata fetched: 92
- High-signal hits surfaced: 14
- Total PubMed results estimated across all axes: >8000 (most off-target)
- Output JSON: `outputs/phase-2c-pubmed-fungal-chokepoint.json`
