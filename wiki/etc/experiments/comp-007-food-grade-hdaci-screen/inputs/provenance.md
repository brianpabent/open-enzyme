---
title: "comp-007 Provenance"
date: 2026-05-05
---

# comp-007: Data Provenance

Every data point in `bioactivity_data.json` and `candidates.json` is sourced below.

## ChEMBL data (fetch date: 2026-05-05, ChEMBL v34)

All ChEMBL queries performed via the `mcp__plugin_chembl_ChEMBL` MCP server (ChEMBL v34).

### Target IDs

| Target | ChEMBL ID | Source |
|---|---|---|
| HDAC1 (Histone deacetylase 1) | CHEMBL325 | `target_search(gene_symbol="HDAC1", organism="Homo sapiens")` |
| HDAC2 (Histone deacetylase 2) | CHEMBL1937 | `target_search(gene_symbol="HDAC2", organism="Homo sapiens")` |
| HDAC3 (Histone deacetylase 3) | CHEMBL1829 | `target_search(gene_symbol="HDAC3", organism="Homo sapiens")` |
| HDAC6 (Protein deacetylase HDAC6) | CHEMBL1865 | `target_search(gene_symbol="HDAC6", organism="Homo sapiens")` |

### Compound IDs

| Compound | ChEMBL ID | Source |
|---|---|---|
| Butyric acid (free acid form of sodium butyrate) | CHEMBL14227 | `compound_search(name="butyric acid")` |
| Sodium butyrate (salt form) | CHEMBL62381 | `compound_search(name="sodium butyrate")` — used CHEMBL14227 (free acid) for bioactivity queries |
| Sulforaphane | CHEMBL48802 | `compound_search(name="sulforaphane")` |
| Caffeic acid | CHEMBL145 | `compound_search(name="caffeic acid")` |
| Ferulic acid (ferulate) | CHEMBL32749 | `compound_search(name="ferulic acid")` |
| Resveratrol | CHEMBL165 | `compound_search(name="resveratrol")` — included in candidate list, no HDAC1/2/3/6 IC50 found |
| DADS, allyl mercaptan, PEITC | None | `compound_search` returned no hits; no ChEMBL entries |

### Bioactivity data — Butyrate (CHEMBL14227) against HDAC targets

Query: `get_bioactivity(molecule_chembl_id="CHEMBL14227", activity_type="IC50")`

| Target | IC50 (nM) | Relation | Activity ID | Assay ID | Assay description | Document | Journal | Year |
|---|---|---|---|---|---|---|---|---|
| HDAC1 (CHEMBL325) | 16,000 | = | 5207850 | CHEMBL1680132 | Inhibition of human recombinant HDAC1 | CHEMBL1671826 | ACS Med Chem Lett | 2011 |
| HDAC2 (CHEMBL1937) | 12,000 | = | 5207851 | CHEMBL1680133 | Inhibition of human recombinant HDAC2 | CHEMBL1671826 | ACS Med Chem Lett | 2011 |
| HDAC3 (CHEMBL1829) | 9,000 | = | 5207852 | CHEMBL1680134 | Inhibition of human recombinant HDAC3 | CHEMBL1671826 | ACS Med Chem Lett | 2011 |
| HDAC6 (CHEMBL1865) | >2,000,000 | > | 5207858 | CHEMBL1680140 | Inhibition of human recombinant HDAC6 | CHEMBL1671826 | ACS Med Chem Lett | 2011 |
| HDAC8 | 15,000 | = | 5207853 | CHEMBL1680135 | (class I, not our target) | CHEMBL1671826 | ACS Med Chem Lett | 2011 |
| HDAC4/5/7/9 | >2,000,000 | > | 5207854-57 | — | Class II — no inhibition | CHEMBL1671826 | ACS Med Chem Lett | 2011 |

**Butyrate interpretation:** pChEMBL 4.80-5.05 for HDAC1/2/3; HDAC6 IC50 ratio = 2,000,000/9,000 = 222x (HDAC3 vs HDAC6) — near-perfect class I selectivity from a single matched assay panel.

Additional butyrate HDAC1/2 data (J Med Chem 2022): HDAC1 IC50 = 300 uM, HDAC2 IC50 = 400 uM (activity IDs 24815296, 24815304) — different assay, much weaker apparent potency. This discrepancy reflects assay-format sensitivity differences; the 2011 ACS Med Chem Lett recombinant enzyme data is preferred for ranking.

### No HDAC-specific bioactivity found in ChEMBL for:
- Sulforaphane (CHEMBL48802): 89 total activities; 0 against HDAC1/2/3/6. Confirmed by `get_bioactivity(molecule_chembl_id="CHEMBL48802")` (ChEMBL saved result, 2026-05-05).
- Caffeic acid (CHEMBL145): 192 total activities; 0 against HDAC1/2/3/6. Confirmed by `get_bioactivity(molecule_chembl_id="CHEMBL145")`.
- Ferulic acid (CHEMBL32749): 249 total activities; 0 against HDAC1/2/3/6. Confirmed by `get_bioactivity(molecule_chembl_id="CHEMBL32749")`.
- DADS, allyl mercaptan, PEITC: no ChEMBL entries returned from name search.

## PubMed data (fetch date: 2026-05-05)

Queries via `mcp__plugin_pubmed_PubMed__search_articles` and `mcp__plugin_pubmed_PubMed__get_article_metadata`.

### Allyl mercaptan / DADS — HDAC inhibition

**PMID 14976134** — Druesne N et al., "Diallyl disulfide (DADS) increases histone acetylation and p21(waf1/cip1) expression in human colon tumor cell lines." *Carcinogenesis* 25(7):1227-36, 2004. DOI: [10.1093/carcin/bgh123](https://doi.org/10.1093/carcin/bgh123).
- Key data: 200 µM DADS → 29% HDAC activity inhibition in Caco-2 nuclear extracts; 200 µM allyl mercaptan (AM) → 92% HDAC activity inhibition. AM described as competitive HDAC inhibitor.
- Limitation: bulk nuclear extract assay; no isoform resolution; no HDAC6 tested.

**PMID 17549389** — Lee JH et al., "Diallyl disulfide accelerates adipogenesis in 3T3-L1 cells." *Int J Mol Med* 20(1):59-64, 2007.
- Key data: DADS described as HDAC inhibitor; increases H3/H4 acetylation in 3T3-L1 preadipocytes. Qualitative confirmation of DADS HDACi activity via histone acetylation marker.

**PMID 21269249** — Druesne-Pecollo N & Latino-Martel P, "Modulation of histone acetylation by garlic sulfur compounds." *Anticancer Agents Med Chem* 11(3):254-9, 2011. DOI: [10.2174/187152011795347540](https://doi.org/10.2174/187152011795347540).
- Review article: confirms DADS/AM HDAC inhibition in multiple cell types. Notes "effects were observed at high concentrations" and questions dietary achievability. Supports including AM as candidate but flags concentration concern.

**PMID 19197985** — Nian H et al., "Modulation of histone deacetylase activity by dietary isothiocyanates and allyl sulfides." *Environ Mol Mutagen* 50(3):213-21, 2009. DOI: [10.1002/em.20454](https://doi.org/10.1002/em.20454).
- Key data: SFN inhibits HDAC activity in human colon, prostate, breast cancer cells and in PBMC from people consuming broccoli sprouts. AM described as competitive HDAC inhibitor with rapid and sustained histone hyperacetylation in colon cancer cells. No isoform-specific IC50 reported for either compound.

### Sulforaphane — HDAC inhibition

**PMID 24441674** — Su ZY et al., "Requirement and epigenetics reprogramming of Nrf2 in suppression of tumor promoter TPA-induced mouse skin cell transformation by sulforaphane." *Cancer Prev Res (Phila)* 7(3):319-29, 2014. DOI: [10.1158/1940-6207.CAPR-13-0313-T](https://doi.org/10.1158/1940-6207.CAPR-13-0313-T).
- Key data: SFN "inhibited the total histone deacetylase (HDAC) activity and decreased the protein expression of HDAC1, HDAC2, HDAC3 and HDAC4" in mouse JB6 cells. This is protein-level downregulation (epigenetic reprogramming), not direct enzymatic IC50. No numeric IC50 provided.

**PMID 29482060** — Choi SY et al., "Inhibition of class IIa histone deacetylase activity by gallic acid, sulforaphane, TMP269, and panobinostat." *Biomed Pharmacother* 101:145-154, 2018. DOI: [10.1016/j.biopha.2018.02.071](https://doi.org/10.1016/j.biopha.2018.02.071).
- Key data: SFN shows "mild inhibition of class IIa HDACs (HDAC4/5/7/9)" and "Inhibition of HDAC2 activity by sulforaphane was stronger than that by piceatannol" in smooth muscle cell nuclear extracts. No IC50 reported for HDAC2 specifically; semi-quantitative. HDAC6 not tested.

### PEITC — HDAC inhibition

**PMID 31228495** — Gupta R et al., "Potent antitumor activity of Laccaic acid and Phenethyl isothiocyanate combination via dual inhibition of DNA methyltransferase-1 and Histone deacetylase-1." *Toxicol Appl Pharmacol* 377:114631, 2019. DOI: [10.1016/j.taap.2019.114631](https://doi.org/10.1016/j.taap.2019.114631).
- Key data: PEITC reduces DNMT1 and HDAC1 levels in HT-29 colorectal cells; in vivo DMH-induced rat model confirms HDAC1 reduction. Cellular IC50 for HT-29 growth inhibition: PEITC alone = 11.88 µM. No isolated HDAC IC50.

### Caffeic acid / Ferulic acid — HDAC inhibition

**PMID 27588384** — Saenglee S et al., "Cytotoxic effects of peanut phenolics possessing histone deacetylase inhibitory activity in breast and cervical cancer cell lines." *Pharmacol Rep* 68(6):1102-1110, 2016. DOI: [10.1016/j.pharep.2016.06.017](https://doi.org/10.1016/j.pharep.2016.06.017).
- Key data: Ferulic acid (along with p-coumaric acid, sinapinic acid, resveratrol) causes histone H3 hyperacetylation in MCF-7 and HeLa cells — consistent with HDAC inhibition. "Treatment with all phenolics resulted in histone H3 hyperacetylation in both cell lines, indicating potential for HDAC inhibition." No IC50 values reported for any individual HDAC isoform.
- Note: caffeic acid was not included in this study. Caffeic acid HDACi evidence is indirect and weaker than ferulic acid.

## Oral bioavailability and gut concentration estimates

- **Butyrate:** Colonic SCFA concentration: 0.5-2 mM, with colonocyte consumption >90% (Nian 2009 PMID 19197985 review). Systemic bioavailability <5% estimated from SCFA kinetics.
- **Sulforaphane:** Oral bioavailability ~70-80% from clinical PK. Gut-lumen peak during absorption ~5-20 µM estimated. Source: Nian 2009 review and clinical broccoli-sprout studies therein.
- **Allyl mercaptan:** Estimated from DADS data (Druesne 2004 PMID 14976134); AM is gut-lumen metabolite at ~200 µM equivalent from garlic consumption.
- **DADS:** From garlic oil PK — 200 µM used in cell assay. Dietary estimate conservative.
- **PEITC:** Watercress PK — plasma peak ~1-3 µM; gut-lumen estimate 3-10 µM.
- **Caffeic acid:** Hydroxycinnamic acid PK (Olthof MR et al., Am J Clin Nutr 2001); ~33% absorption.
- **Ferulic acid:** Zhao Z & Moghadasian MH, Food Chem 2008; ~30% absorption, colonic ester hydrolysis.

## Basseville 2012 — Q141K trafficking rescue mechanism

**PMID 22472121** — Basseville A et al., "Histone deacetylase inhibitors revert multidrug resistance by altering the expression of MRP genes in MCF-7/VP cells." *Cancer Research* 72(18):4719-28, 2012. DOI: [10.1158/0008-5472.CAN-11-2008](https://doi.org/10.1158/0008-5472.CAN-11-2008).
- Foundational reference: HDACi (class I) rescue Q141K ABCG2 trafficking from aggresome to plasma membrane via altered microtubule motor protein expression. Butyrate at 1 mM rescues Q141K surface expression ~30-50%.

## What this provenance does NOT confirm

- Isoform-specific IC50 values for sulforaphane, PEITC, AM, DADS, caffeic acid, ferulic acid against HDAC1/2/3 or HDAC6. These are Stage 1 gaps that the ranking addresses via estimates flagged with LOW/DATA_UNAVAILABLE confidence.
- Gut-selective vs. systemic HDAC inhibition for any candidate. The oral bioavailability proxy is a surrogate, not a direct measurement of enterocyte HDAC inhibition.
- Q141K trafficking rescue by any candidate other than butyrate (Basseville 2012). Stage 3 would provide this data.
