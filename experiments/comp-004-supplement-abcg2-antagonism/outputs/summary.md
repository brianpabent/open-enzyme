# comp-004: Supplement ABCG2 Antagonism — Risk Assessment Summary

**Target:** ABCG2 (Breast Cancer Resistance Protein / BCRP) (CHEMBL5393)
**Function:** ATP-driven urate efflux transporter; apical surface of enterocytes exports uric acid from blood into gut lumen. Accounts for ~33% of total gut urate secretion. Loss-of-function Q141K variant (rs2231142) reduces surface expression ~50% and is enriched in East Asian populations.
**Gut volume model:** 0.25 L (small intestine lumen, fasted estimate)

## Risk ratio table

Risk ratio = effective gut-lumen dissolved concentration ÷ ABCG2 IC50
Predicted inhibition from Hill equation (n=1): ratio / (ratio + 1)

| Compound | Dose (mg) | Gut conc (µM) | Solubility-capped? | IC50 (nM) | Risk ratio | Pred. inhibition | Risk level |
|---|---|---|---|---|---|---|---|
| Quercetin | 500 | 49.6 | Yes | 7250 | 6.8× | 87% | **VERY_HIGH** |
| EGCG | 400 | 1090.8 | Yes | N/A (expression mechanism) | N/A | N/A | **NOT_APPLICABLE** |
| Curcumin | 1000 | 13.6 | Yes | 1630 | 8.3× | 89% | **VERY_HIGH** |

## Per-compound breakdown

### Quercetin (CHEMBL50)
- Dose: 500 mg | Bioavailability: 17% | MW: 302.24 g/mol
- Gut mass (unabsorbed): 415.0 mg
- Dose-limited concentration: 1660.0 mg/L
- Intestinal solubility: 15.0 mg/L
- Solubility cap applied: Yes → effective concentration = 15.0 mg/L
- Effective dissolved: **49.6 µM** (49629 nM)
- ABCG2 IC50: 7250 nM | Assay: Hoechst 33342 efflux assay (cell-based)
- Risk ratio: 6.85× | Predicted inhibition: 87%
- **Risk level: VERY_HIGH**
- Data note: Hoechst 33342 is a fluorescent ABCG2 substrate; assay measures inhibition of its efflux. MCF7 cells overexpress ABCG2 vs enterocytes — functional inhibition in primary enterocytes may differ.
- IC50 source: Bioorg Med Chem 2011

### EGCG (CHEMBL297453)
- Dose: 400 mg | Bioavailability: 2% | MW: 458.37 g/mol
- Gut mass (unabsorbed): 392.0 mg
- Dose-limited concentration: 1568.0 mg/L
- Intestinal solubility: 500.0 mg/L
- Solubility cap applied: Yes → effective concentration = 500.0 mg/L
- Effective dissolved: **1090.8 µM** (1090822 nM)
- ABCG2 IC50: None nM | Assay: N/A (expression mechanism)
- Risk ratio: N/A | Framework not applicable
- **Risk level: NOT_APPLICABLE**
- Mechanism: EGCG downregulates ABCG2 mRNA and protein expression over 24-72h in cell culture. Effect is transcriptional/post-transcriptional, not acute transport inhibition. No kinetic IC50 for direct transport block exists in ChEMBL.
- Data note: The §1.14 Caco-2 transwell assay (48h, acute urate flux) will not detect EGCG's mechanism. A separate longer-treatment arm (72h) with ABCG2 Western blot is needed to quantify EGCG's expression effect.
- IC50 source: PubMed search 2026-05-05; Yu 2024 in vivo gout study showed net-favorable urate direction (likely indirect anti-inflammatory effects dominating over ABCG2 expression changes)

### Curcumin (CHEMBL140)
- Dose: 1000 mg | Bioavailability: 1% | MW: 368.38 g/mol
- Gut mass (unabsorbed): 990.0 mg
- Dose-limited concentration: 3960.0 mg/L
- Intestinal solubility: 5.0 mg/L
- Solubility cap applied: Yes → effective concentration = 5.0 mg/L
- Effective dissolved: **13.6 µM** (13573 nM)
- ABCG2 IC50: 1630 nM | Assay: Mitoxantrone efflux assay (cell-based)
- Risk ratio: 8.33× | Predicted inhibition: 89%
- **Risk level: VERY_HIGH**
- Data note: Mitoxantrone is a high-affinity ABCG2 substrate; assay measures inhibition of its efflux. MCF7-VP cells overexpress ABCG2. Single value — no replication across labs in ChEMBL for this specific assay.
- IC50 source: Eur J Med Chem 2022

## Key findings

**Curcumin is the highest-risk compound** despite being perceived as systemically safe.
Its extreme insolubility (< 1% bioavailability) concentrates effectively all oral dose in the
gut lumen, where it reaches the solubility ceiling at ~13.6 µM — 8.3× its ABCG2 IC50 (1630 nM).
Predicted inhibition: ~89% of maximal ABCG2 activity.

**Quercetin** is moderately-to-highly risk at standard 500 mg doses. Gut-lumen concentration
is solubility-limited at ~49.6 µM, which is ~6.8× its ABCG2 IC50 (7250 nM).
Predicted inhibition: ~87% of maximal ABCG2 activity.

**EGCG** cannot be scored by this framework. Its ABCG2 modulation is transcriptional
(mRNA/protein downregulation over 24-72h), not acute transport inhibition.
The §1.14 48h transwell assay would miss this mechanism; a 72h arm with Western blot is needed.

## Impact on §1.14 experimental framing

Before comp-004: supplement arms in §1.14 were purely screening for whether an effect exists.
After comp-004: IC50 occupancy strongly predicts substantial inhibition for quercetin and curcumin.
§1.14 supplement arms now test a pharmacologically-predicted effect — the question shifts from
'is there an effect?' to 'how large is it and does it match predictions?' The IC50 translation
uncertainties (cell line vs. enterocyte, substrate dependence, self-aggregation) mean the Caco-2
arm remains genuinely informative rather than a foregone conclusion.

The strategic implication: gout patients taking curcumin or quercetin supplements may
paradoxically worsen their condition by inhibiting gut ABCG2-mediated urate excretion,
even if these compounds have anti-inflammatory effects on other pathways.

## Limitations

- Solubility values are estimates; actual intestinal solubility varies with meal fat content,
  bile salt concentration, and supplement formulation (phospholipid complexes, nanoparticles,
  piperine co-administration). Enhanced-bioavailability curcumin formulations (Meriva, BCM-95)
  increase intestinal solubility 5-20×, potentially raising curcumin risk ratio to 40-160×.
- IC50 values from cancer cell lines (MCF7, MCF7-VP) overexpressing ABCG2 at 10-100× enterocyte
  levels. Substrate-to-transporter stoichiometry affects apparent IC50; functional inhibition in
  primary enterocytes may differ quantitatively from cell-line data.
- Substrate-dependent IC50: quercetin IC50 was measured with Hoechst 33342; curcumin with
  mitoxantrone. Both are high-affinity ABCG2 substrates. ABCG2 displays substrate-dependent
  inhibitor binding — IC50 against urate transport specifically may differ; urate is a
  lower-affinity physiological substrate handled via a different binding mode.
- Quercetin self-aggregation: quercetin forms colloidal aggregates above ~10 µM in aqueous
  solution. Effective free monomeric concentration may be lower than the 49.6 µM nominal gut
  concentration — aggregates may not inhibit ABCG2 and can produce artifactual inhibition in
  cell-based assays. True free inhibitor concentration is uncertain.
- Single-dose reporting: one representative supplement dose used per compound. At 1-3 g
  quercetin (commercially available), risk ratio is identical (solubility-capped). For curcumin,
  enhanced-solubility formulations are the variable to watch, not dose.
- Gut volume model (250 mL whole SI) overestimates dilution relative to the proximal
  small intestine where ABCG2 is most expressed — concentrations in duodenum/jejunum
  may be 2-3× higher than reported, pushing risk ratios further into VERY_HIGH.
- Hill equation n=1 assumes simple 1:1 competitive inhibition. ABCG2 inhibitor
  mechanisms vary (ATP hydrolysis interference, substrate competition, conformational locking);
  true dose-response curves may be steeper (n > 1) or shallower.
- Q141K (rs2231142) amplified risk subgroup: Q141K carriers have ~50% reduced ABCG2 surface
  expression at baseline, reducing gut urate secretion capacity before any supplement exposure.
  Pharmacological inhibition on top of genetically-reduced ABCG2 drives total gut urate
  excretion toward zero — this is an amplified-risk subgroup, not just a variant of interest.
  ~27% of East Asian-ancestry individuals carry this variant.
- EGCG cannot be assessed by this framework; a 72h treatment arm with ABCG2 Western blot
  is needed in §1.14 to detect expression-level changes.
- Transit dynamics not modelled: peak concentration window in proximal SI may be
  shorter than total transit time, limiting total exposure.