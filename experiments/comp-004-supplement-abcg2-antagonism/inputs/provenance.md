# Provenance — comp-004 inputs

All inputs documented with sources, fetch dates, and versions.

## ic50_data.json

### ABCG2 target identification
- **Source:** ChEMBL MCP query, 2026-05-05
- **Target:** CHEMBL5393 (ABCG2/BCRP, *Homo sapiens*)
- **UniProt:** Q9UNQ0
- **GO term confirmed:** GO:0015143 "urate transmembrane transporter activity" — verified via UniProt Q9UNQ0 GO annotations

### Quercetin IC50 vs ABCG2
- **ChEMBL compound ID:** CHEMBL50
- **Fetch date:** 2026-05-05
- **Fetch method:** ChEMBL MCP `get_bioactivity` query (standard_type=IC50, target=CHEMBL5393)
- **Values retrieved:** 6900 nM and 7600 nM (two activities)
- **Used:** 7250 nM (arithmetic mean)
- **Assay:** Hoechst 33342 efflux, MCF7 cells expressing ABCG2
- **Source paper:** Bioorg Med Chem 2011 (ChEMBL document reference)

### EGCG (mechanism, no IC50)
- **ChEMBL compound ID:** CHEMBL297453
- **Fetch date:** 2026-05-05
- **Fetch method:** ChEMBL MCP (no transport inhibition IC50 found for ABCG2); PubMed literature search
- **Finding:** EGCG modulates ABCG2 via expression downregulation, not acute transport inhibition
- **PubMed sources:** Multiple papers on EGCG-mediated ABCG2 mRNA/protein reduction in cancer cell lines; Yu 2024 in vivo gout study (net urate direction favorable, likely anti-inflammatory rather than ABCG2 transport block)

### Curcumin IC50 vs ABCG2
- **ChEMBL compound ID:** CHEMBL140
- **Fetch date:** 2026-05-05
- **Fetch method:** ChEMBL MCP `get_bioactivity` query (standard_type=IC50, target=CHEMBL5393)
- **Value retrieved:** 1630 nM
- **Used:** 1630 nM
- **Assay:** Mitoxantrone efflux, MCF7-VP cells (ABCG2-overexpressing)
- **Source paper:** Eur J Med Chem 2022 (ChEMBL document reference)

---

## compounds.json

### Quercetin bioavailability (~17%)
- **Source:** Manach C et al. "Quercetin is recovered in human plasma as conjugated derivatives which retain antioxidant properties." Am J Clin Nutr 2005;81(1 Suppl):230S-242S.
- **PMID:** 15640486
- **DOI:** 10.1093/ajcn/81.1.230S

### Quercetin aqueous solubility (7 mg/L)
- **Source:** Literature consensus; see Merkle HP et al. studies on quercetin biopharmaceutics; FaSSIF solubility estimates

### Curcumin bioavailability (<1%)
- **Source:** Metzler M et al. "Curcumin uptake and metabolism." Biofactors 2013;39(1):14-20.
- **PMID:** 22996406
- **DOI:** 10.1002/biof.1042
- **Note:** Essentially all oral dose remains in gut lumen; <1% reaches systemic circulation

### Curcumin intestinal solubility (5 mg/L estimate)
- **Source:** Estimate from literature range 0.6-8 mg/L depending on formulation and intestinal conditions (bile salt content, lipid content, pH). Standard unformulated curcumin 0.6 mg/L aqueous; with intestinal bile salts ~2-8 mg/L. Conservative midpoint 5 mg/L used.

### EGCG bioavailability (~2%)
- **Source:** Literature consensus across multiple PK studies; EGCG is among least-absorbed flavonoids despite high water solubility

---

## gut_model.json
- **Small intestine volume 250 mL:** Johnson LR (ed.) *Physiology of the Gastrointestinal Tract*; commonly cited fasted SI fluid volume
- **pH 6.5–7.0:** Standard reference for proximal SI; relevant for ABCG2 expression zone (duodenum/jejunum)
