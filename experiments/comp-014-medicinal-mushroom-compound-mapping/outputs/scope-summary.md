# comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping

**Status:** Phase 1 (scope) — execution pending Brian sign-off.

## Phase 1 inventory

- **Candidate fungal species:** 18
- **Open Enzyme chokepoint targets:** 19 (1 proposed, not-yet-canonical)
- **Compound databases planned:** 14
- **Bioactivity / target databases planned:** 6
- **Multilingual literature corpora planned:** 7

## Candidate species (Phase 2 expansion may extend)

- *Ganoderma lucidum* (reishi / lingzhi)
- *Cordyceps militaris* (cordyceps (cultivated))
- *Ophiocordyceps sinensis* (caterpillar fungus (wild-harvested))
- *Hericium erinaceus* (lion's mane)
- *Trametes versicolor (Coriolus versicolor)* (turkey tail / yun zhi)
- *Inonotus obliquus* (chaga)
- *Grifola frondosa* (maitake)
- *Lentinula edodes* (shiitake)
- *Pleurotus ostreatus* (oyster mushroom) — **redox chokepoint primary**
- *Agaricus blazei (A. subrufescens)* (almond mushroom)
- *Antrodia camphorata (Taiwanofungus camphoratus)* (antrodia / niu zhang zhi)
- *Phellinus linteus* (phellinus / sang hwang)
- *Wolfiporia cocos (Poria cocos)* (fu ling / poria)
- *Polyporus umbellatus* (zhu ling)
- *Tremella fuciformis* (tremella / yin er)
- *Auricularia auricula-judae* (wood ear / mu er)
- *Aspergillus oryzae* (koji (Open Enzyme chassis)) — redox chokepoint secondary
- *Aspergillus terreus* (Aspergillus terreus (lovastatin-original producer))

## Chokepoint targets

| Chokepoint | UniProt | Site | Priority signal |
|---|---|---|---|
| uricase_substrate | — | gut lumen | Not a protein target — substrate degradation. |
| URAT1 | Q96S37 | renal tubule | Validated drug target (probenecid, benzbromarone, lesinurad, dotinurad). |
| GLUT9 | Q9NRM0 | renal tubule + gut epithelium | Less drugged than URAT1 but mechanistically validated. |
| ABCG2 | Q9UNQ0 | gut epithelium + renal tubule | comp-004 supplement screen validated this target. |
| Xanthine_Oxidase | P47989 | systemic + gut + liver | Allopurinol, febuxostat target. |
| NLRP3 | Q96P20 | macrophages (gut + synovial + vessel-wall) | Central gout-flare driver. |
| ASC | Q9ULZ3 | — | Oridonin and related natural products block ASC oligomerization. |
| Caspase_1 | P29466 | — | Downstream of NLRP3+ASC; pharmacological inhibition is a separate intervention class. |
| IL_1B | P01584 | — | Canakinumab/anakinra target. |
| TNFA | P01375 | — | Gut-barrier and vessel-wall inflammation cycle. |
| DAF_CD55 | P08174 | engineered chassis output, not target | Open Enzyme is engineering CD55 SCR1-4 itself (comp-006/comp-012). |
| C5aR1 | P21730 | — | validation-experiments. |
| Lp_PLA2 | Q13093 | — | Brian's persistent elevation across panels. |
| HDAC6 | Q9UBN7 | — | comp-007 ran the supplement-grade HDACi screen. |
| PPARG | P37231 | — | Fungal triterpenoids (esp. |
| NRF2_KEAP1 | Q14145 / Q16236 | — | Sulforaphane axis; fungal compounds (esp. |
| OAT1_OAT3 | Q4U2R8 / Q8TCC7 | — | Off-target risk profile for any URAT1-targeted compound — needs counter-screen. |
| OAT4 | Q9NS40 | — | Apical urate exchanger; benzbromarone hits this alongside URAT1. |

**Proposed (not-yet-canonical):**

- **Redox/disulfide chemistry (PROPOSED — not yet a wiki chokepoint)** — PROPOSED 2026-05-06 by comp-014 scope. Not yet added to wiki/modality-chokepoint-matrix.md or wiki/nlrp3-exploit-map.md. Phase 5 deliverable: confirm or reject the chokepoint-warrant claim based on what fungal-compound coverage actually surfaces.

## Phase plan

- **phase_1_scope**: This commit. Inventory sources, candidate species, chokepoint targets. No DB queries executed.
- **phase_2_breadth_aggregation**: Pull LOTUS + NPAtlas + KNApSAcK + NPASS + TCMSP + COCONUT. Dedup by InChIKey. Output: unified fungal compound × species table.
- **phase_3_target_mapping**: Empirical (ChEMBL + HIT + PubChem) → SwissTargetPrediction for orphans. Output: compound × target table with empirical/predicted flag.
- **phase_4_chokepoint_intersection**: Join compound × target × Open Enzyme chokepoints (chokepoint-targets.json). Output: ranked candidate list.
- **phase_5_multilingual_deep_dive**: For top 3-5 species flagged by Phase 4: ingest CNKI + J-STAGE primary literature with two-model translation cross-check. Compare Asian clinical evidence against the breadth-pass mechanism map.
- **phase_6_per_compound_triage**: comp-013-style IC50 occupancy analysis for top candidates. Verdicts: GUT-LUMINAL VIABLE / SYSTEMIC VIABLE / MECHANISM UNCLEAR / NON-VIABLE. Subset gets shio-koji protease stability comp-NNN follow-ups.

## Data sources (Phase 2-5 access plan)

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
cd experiments/comp-014-medicinal-mushroom-compound-mapping
python3 scripts/scope_validate.py
```

Phase 2+ will add per-phase scripts. This Phase 1 script validates inputs and emits this summary.
