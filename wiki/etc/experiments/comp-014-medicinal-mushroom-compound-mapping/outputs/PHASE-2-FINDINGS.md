# comp-014 Phase 2 — Headline findings (2026-05-06)

Phase 2 ran three parallel passes against the chokepoint inventory. Each pass produced its own structured output; this file is the human-facing synthesis.

## What ran

| Pass | Source | Method | Status |
|---|---|---|---|
| 2a | ChEMBL | MCP bioactivity sweep across 19 chokepoint targets, filter to fungal-source compounds | ✅ |
| 2b | LOTUS | REST API iterated across 56 fungal genera/species, deduplicated by InChIKey | ✅ partial (LOTUS only; KNApSAcK + NPASS + TCMSP + HIT pending) |
| 2c | PubMed | 17 searches across 3 axes (chokepoint × fungus, species × indication, multilingual catch-net) | ✅ |

## Top-line numbers

- **6,798 unique fungal compounds** (LOTUS, deduped by InChIKey)
- **55 fungal genera/species** with compound attributions
- **9,409 raw compound-source pairs** seen
- **14 high-signal PubMed papers** with primary-literature evidence at chokepoint targets
- **1 ChEMBL hit** with empirical sub-μM bioactivity (Fumitremorgin C → ABCG2)

## Highest-leverage individual findings

### Dual-chokepoint hit — Ganoderma applanatum 2,4-DAE
PubMed PMID 35750011 (Fitoterapia 2022). 2,4-dihydroxyacetophenone derivatives from *Ganoderma applanatum* show in vivo SUA reduction from 407 → 134 µmol/L in murine hyperuricemia model. Hits **both XO and URAT1** by mechanism. Strongest single-compound finding of the breadth pass.

### URAT1 direct modulator — cordycepin (Cordyceps militaris)
PubMed PMID 29422889. Mouse dose-response, mechanism proven. Cordycepin is a 3'-deoxyadenosine purine analog — structurally adjacent to the nucleotide salvage / XO substrate axis we'd predicted from the candidate-species file.

### Clinical-grade evidence — Cordyceps × hyperuricemia
- Cochrane review of 5 RCTs (PMID 26457607)
- 9-RCT meta-analysis (PMID 28137532)
Both Chinese-source data — confirms multilingual ingestion is load-bearing for capturing this evidence quality. PubMed indexed only English abstracts; full RCT data is in CNKI/Wanfang.

### ABCG2 — Fumitremorgin C (Aspergillus fumigatus)
ChEMBL CHEMBL1232 (or similar, full ID in JSON). IC50 800 nM, pChEMBL 6.10. The canonical ABCG2/BCRP discriminator tool compound from Western pharma curation. Fungal source: *A. fumigatus* — which is on the WHO Fungal Priority Pathogens list and EXCLUDED by the toxicity filter. So this hit is **chemistry-relevant but producer-organism-excluded**: the compound has chokepoint relevance but cannot use *A. fumigatus* as the production chassis. Synthetic / heterologous expression route required for downstream use.

### Multi-chokepoint extract — AMC-BFE
2026 paper, PMID 41905012. *Cordyceps × Astragalus* solid-state co-fermentation extract hitting URAT1 + GLUT9 + ABCG2 + PPARα. Adjacent to the engineered-koji co-culture thesis.

## Strategic findings (negatives + reframings)

### C5aR1 platform-gap (validation-experiments §1.21) confirmed empirically
Both Phase 2a (ChEMBL) and Phase 2c (PubMed) returned ZERO direct fungal-source C5aR1 antagonists. ChEMBL has only 2 named C5aR1 compounds total, neither fungal. PubMed surfaced that mushroom β-glucans actually ACTIVATE complement via CR3/iC3b — opposite-sign to what the platform gap needs. **Implication: the avacopan-dependence gap will not be closed by mushroom-extract programs.** Phase 5 C5aR1 work needs synthetic / non-fungal source.

### NLRP3 directionality is structure-dependent and OPPOSITE-SIGN across fungal compounds
Phase 2c surfaced this clearly: *Ganoderma lucidum* exopolysaccharides ACTIVATE NLRP3 (cryptococcosis defense, beneficial in that context); spore powder + GLP β-glucan INHIBIT NLRP3 (CNS contexts). **Phase 5 cannot claim "fungal β-glucan inhibits NLRP3" without specifying triple-helix conformation, MW, branching, sulfation.** Methodology constraint for Phase 6 triage.

### ChEMBL coverage is severely Western-pharma-biased for fungal compounds
Phase 2a found ChEMBL has **none** of the canonical mushroom compound classes by name — ganoderic acids, ergosterol, hericenones, erinacines, inotodiol, pachymic acid, eburicoic acid, eritadenine, PSK. The CLAUDE.md global-multilingual research warning is empirically validated. LOTUS captured 6,798 unique compounds; ChEMBL captured handful of fungal compounds. The breadth signal is in LOTUS + East-Asian DBs (still pending) + multilingual literature.

### Two new chokepoint candidates surfaced
Phase 2c found primary-literature evidence at chokepoints not currently in our inventory:
1. **ADA (adenosine deaminase)** — *Ganoderma lucidum* GLPP, PMID 36385640. Mechanism: ADA is upstream of xanthine oxidase in purine catabolism. Plausibly a fourth front in the urate-axis chokepoint map.
2. **Mitophagy / PINK1** — *Cordyceps cicadae*, PMID 40334761. Adjacent to NLRP3 priming via mitochondrial dysfunction-induced ROS.

Both warrant addition to `chokepoint-targets.json` (Phase 4 follow-up) and possibly the canonical wiki chokepoint inventory.

## Per-species breadth ranking (top from LOTUS)

| Rank | Genus/species | LOTUS compound count |
|---:|---|---:|
| 1 | Ganoderma (genus, summed) | 1,938 |
| 2 | Aspergillus terreus | 457 |
| 3 | Lactarius | 380 |
| 4 | Aspergillus niger | 302 |
| 5 | Phellinus | 292 |
| 6 | Cordyceps (genus, summed) | 283 |
| 7 | Fomitopsis | 282 |
| 8 | Penicillium chrysogenum | 240 |

The Phase 5 anchor list (18 well-studied medicinal fungi) all appear in the LOTUS pull — sanity-check passed.

## Methodology gaps (deferred to Phase 2 follow-up runs)

1. **East-Asian-hosted DBs not yet pulled.** KNApSAcK (Japanese), NPASS (Chinese), TCMSP (Chinese), HIT (TCM ingredient targets), BATMAN-TCM. Together likely surface another 1,000-3,000 unique compounds. None of these have public REST APIs comparable to LOTUS — scraping or bulk download required.
2. **LOTUS organism-attribution is via query-hint, not per-record metadata.** The `search/simple` endpoint returns compound metadata but not organism per record; we attribute by query name. To upgrade, hit the per-compound LOTUS endpoint or use the Zenodo bulk dump.
3. **200-records-per-LOTUS-query truncation.** Ganoderma lucidum returned 28MB of data suggesting we hit the limit. Re-run with limit=2000+ for top-10 species to expand coverage.
4. **Toxicity filter not yet applied at the species level.** All compounds pulled were retained — the filter logic in `toxicity-filter.json` needs to be applied as a post-processing step before Phase 4 chokepoint intersection. *A. fumigatus* example (Fumitremorgin C → ABCG2) is the canonical case where filter matters.
5. **MIBiG + antiSMASH-DB BGC pull not run.** Genomic-encoded compound space — for compounds we don't yet have isolation data for. Phase 2c (genome-upstream) deferred.

## Next concrete step (Phase 3)

Phase 3 = target mapping. For each of the 6,798 LOTUS compounds, look up known bioactivity. Three sources in cascade:

1. **ChEMBL by InChIKey** (highest curation, lowest fungal coverage) — already partially run via Phase 2a; intersect that data with the LOTUS InChIKey list to find any cross-source hits.
2. **HIT (Herb Ingredient Targets)** — TCM-curated target hypotheses for compounds with TCM literature.
3. **SwissTargetPrediction** for orphan compounds (no empirical target) — flagged as predicted-not-empirical in the output.

Then Phase 4 intersects with `chokepoint-targets.json` to produce the ranked candidate list — the answer to Brian's original question.
