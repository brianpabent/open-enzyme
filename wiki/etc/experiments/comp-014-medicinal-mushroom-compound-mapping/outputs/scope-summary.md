# comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping

**Status:** Breadth aggregation and target mapping are retained as a lead inventory. Historical rank and priority fields have no current decision authority; the former Phase 6 occupancy/feasibility triage is retired.

## Inventory

- **Phase 5 anchor species (sanity-check):** 18
- **Rendered historical target entries:** 19
- **Compound databases recorded:** 14
- **Bioactivity / target databases recorded:** 6
- **Multilingual literature corpora recorded:** 7

## Historical anchor species (sanity-check set, not priorities)

- *Ganoderma lucidum* (reishi / lingzhi)
- *Cordyceps militaris* (cordyceps (cultivated))
- *Ophiocordyceps sinensis* (caterpillar fungus (wild-harvested))
- *Hericium erinaceus* (lion's mane)
- *Trametes versicolor (Coriolus versicolor)* (turkey tail / yun zhi)
- *Inonotus obliquus* (chaga)
- *Grifola frondosa* (maitake)
- *Lentinula edodes* (shiitake)
- *Pleurotus ostreatus* (oyster mushroom)
- *Agaricus blazei (A. subrufescens)* (almond mushroom)
- *Antrodia camphorata (Taiwanofungus camphoratus)* (antrodia / niu zhang zhi)
- *Phellinus linteus* (phellinus / sang hwang)
- *Wolfiporia cocos (Poria cocos)* (fu ling / poria)
- *Polyporus umbellatus* (zhu ling)
- *Tremella fuciformis* (tremella / yin er)
- *Auricularia auricula-judae* (wood ear / mu er)
- *Aspergillus oryzae* (koji (Open Enzyme chassis))
- *Aspergillus terreus* (Aspergillus terreus (lovastatin-original producer))

## Chokepoint targets

| Chokepoint | UniProt | Site | Scope rationale |
|---|---|---|---|
| uricase_substrate | — | gut lumen | Historical uricase-substrate search node. Rehydrate source, substrate, compartment, material identity, and direct degradation function. |
| URAT1 | Q96S37 | renal tubule | Historical URAT1 search node. Rehydrate target attribution, effect polarity, substrate, compartment, relevant exposure, and mechanism-matched function. |
| GLUT9 | Q9NRM0 | renal tubule + gut epithelium | Historical GLUT9 search node. Rehydrate target attribution, effect polarity, substrate, compartment, relevant exposure, and direct function. |
| ABCG2 | Q9UNQ0 | gut epithelium + renal tubule | Historical ABCG2 search node. Rehydrate source, interaction type, effect polarity, substrate, compartment, and direct urate-flux function before any current use. |
| Xanthine_Oxidase | P47989 | systemic + gut + liver | Historical xanthine-oxidase search node. Rehydrate fungal provenance, assay context, effect polarity, exposure, and mechanism-matched function. |
| NLRP3 | Q96P20 | macrophages (gut + synovial + vessel-wall) | Historical NLRP3 search node. Rehydrate exact material, assay layer, effect polarity, attribution, relevant exposure, and mechanism-matched function. |
| ASC | Q9ULZ3 | — | Historical ASC search node. Rehydrate exact material, binding or oligomerization endpoint, effect polarity, attribution, exposure, and direct function. |
| Caspase_1 | P29466 | — | Historical caspase-1 search node. Rehydrate material identity, assay type, effect polarity, attribution, and direct function. |
| IL_1B | P01584 | — | Historical IL-1β search node. Rehydrate whether each record measures transcription, processing, release, receptor signaling, or another endpoint. |
| TNFA | P01375 | — | Historical TNF search node. Rehydrate the material, endpoint, effect polarity, pathway attribution, compartment, and direct function. |
| DAF_CD55 | P08174 | engineered chassis output, not target | Historical CD55 context node, not evidence of a fungal-compound target or a current production decision. |
| C5aR1 | P21730 | — | Historical C5aR1 search node. Database non-retrieval does not establish universal absence; rehydrate source, material, effect polarity, exposure, and direct receptor function. |
| Lp_PLA2 | Q13093 | — | Historical Lp-PLA2 search node. Rehydrate source, assay type, effect polarity, relevant exposure, and direct function without inferring personal relevance. |
| HDAC6 | Q9UBN7 | — | Historical HDAC6 search node. Rehydrate direct activity, selectivity, material provenance, relevant exposure, and function. |
| PPARG | P37231 | — | Historical PPARγ search node. Rehydrate exact compound and fungal provenance, assay type, agonist/antagonist polarity, concentration, and direct function. |
| NRF2_KEAP1 | Q14145 / Q16236 | — | Historical Nrf2/KEAP1 search node. Rehydrate exact material, direct target or reporter endpoint, effect polarity, exposure, and downstream function. |
| OAT1_OAT3 | Q4U2R8 / Q8TCC7 | — | Historical OAT1/OAT3 counter-screen node. Rehydrate substrate, assay system, effect polarity, concentration, and transporter function. |
| OAT4 | Q9NS40 | — | Historical OAT4 search node. Rehydrate substrate, assay system, effect polarity, concentration, and transporter function. |
| ADA | P00813 | systemic + liver + kidney | Historical ADA search node. Rehydrate exact composition, assay type, direct ADA function, effect polarity, exposure, and attribution controls. |

## Recorded phase scope

- **phase_1_scope**: Historical source, species, toxicity, and target inventory; no database calls were part of this step.
- **phase_2_breadth_aggregation**: Historical aggregation plan and retained outputs. The former pull/aggregation scripts are removed; rows are source leads only.
- **phase_3_target_mapping**: Historical target-mapping plan and retained outputs. The former mapper is removed; empirical/predicted labels require source rehydration.
- **phase_4_chokepoint_intersection**: Join compound × target × Open Enzyme chokepoints (chokepoint-targets.json). Retained rows are an unranked lead inventory; historical rank fields are invalid for decision use.
- **phase_5_multilingual_deep_dive**: Rehydrate nominated rows in relevant multilingual primary literature with the required two-model translation cross-check. Do not cap the search by a historical rank.
- **phase_6_per_compound_triage**: RETIRED. The former comp-013-style occupancy and composite-score triage is invalid for candidate ranking. Any successor must preserve target-effect polarity and require measured or justified free exposure plus mechanism-matched function.

## Historical data-source inventory

### Compound databases
- **LOTUS** — Open natural products with species-of-origin links. ~750K compound-organism pairs across all kingdoms. Filter to fungi (Kingdom=Fungi).
- **NPAtlas** — Microbial natural products (bacteria + fungi) with strong provenance. ~33K curated entries.
- **KNApSAcK** — Japanese-hosted comprehensive species-metabolite database. ~50K species, ~100K metabolites. Strong East-Asian-traditional-medicine coverage including fungi.
- **NPASS** — Natural Product Activity & Species Source DB. ~30K natural products with bioactivity data. China-hosted (NUS / Bidd group).
- **TCMSP** — Traditional Chinese Medicine Systems Pharmacology DB. ~30K compounds from Chinese herbs/fungi with predicted targets and ADME.
- **TCMID** — Traditional Chinese Medicine Integrated Database. Compound-disease-target relations.
- **TCM_Database_Taiwan** — ~32K compounds from Chinese herbs (China Medical University, Taiwan).
- **HIT** — Herb Ingredient Targets database. Curated TCM ingredient → protein target mappings.
- **BATMAN-TCM** — Bioinformatics Analysis Tool for Molecular mechANism of TCM. Predicts targets via similarity to known drugs.
- **COCONUT** — Aggregator of open natural product DBs (~700K compounds). Includes upstream LOTUS, NPAtlas, others.
- **MIBiG** — Minimum Information about a Biosynthetic Gene cluster. Curated BGC → product links. ~2.5K entries, fungal subset ~400.
- **antiSMASH-DB** — Predicted BGCs from sequenced genomes including fungi. ~150K fungal BGCs.
- **MycoCosm_JGI** — JGI MycoCosm — canonical fungal genomes portal. ~2,000+ assembled fungal genomes with annotated secondary metabolism.
- **NCBI_RefSeq_Fungi** — NCBI RefSeq fungal genomes — backup genomic source for any candidate species not in MycoCosm.

### Bioactivity / target databases
- **ChEMBL** — European-hosted manually curated bioactivity DB. ~2M compounds, 1.5M assays. Western pharma-skewed.
- **PubChem_BioAssay** — NIH bioassay corpus, broader than ChEMBL but less curated.
- **HIT** — see compound_databases — also a target source
- **BATMAN-TCM** — see compound_databases — also a target predictor
- **SwissTargetPrediction** — Similarity-based target prediction for compounds with known structure but no empirical target.
- **STITCH** — Chemical-protein interactions, integrates multiple sources.

### Multilingual literature corpora
- **PubMed** — English-indexed biomedical literature, includes English-translated abstracts of many Asian papers.
- **CNKI** — China National Knowledge Infrastructure. Canonical Chinese-language clinical and pharmacology corpus. The decades of Chinese-medicine clinical experience that ChEMBL/PubMed never see.
- **Wanfang** — Major Chinese academic database, complementary to CNKI.
- **J-STAGE** — Japanese scientific journals — Kampo medicine, mycology, fungal natural products research.
- **CiNii** — Japanese academic database, includes fungal/Kampo research.
- **KISS** — Korean Studies Information Service System. Korean-language pharmacology and ethnomycology.
- **RISS** — Research Information Sharing Service (Korea).

## Reproducibility

```bash
cd wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping
python3 scripts/scope_validate.py
```

This scope validator checks the current input structure and emits this summary. It does not reproduce the database pulls, later joins, historical rankings, or retired Phase 6.
