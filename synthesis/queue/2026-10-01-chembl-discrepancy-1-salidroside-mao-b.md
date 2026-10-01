---
type: chembl-discrepancy
quarter: 2026-Q4
sweep_date: 2026-10-01
compound: Salidroside
chembl_id: CHEMBL465208
wiki_claim: "Salidroside is cited as an MSU animal-study retrieval lead (PMID 30265377); the primary study is not rehydrated; no mechanism is attributed in the wiki."
chembl_curated: "Top annotated protein target is MAO-B (IC50 pChEMBL 6.09; Ki 6.04), both from CHEMBL4706619. 211 total records; 8 with pChEMBL values."
epistemic_status: evidence-update
---

# ChEMBL discrepancy — Salidroside at MAO-B

Salidroside (p-hydroxyphenethyl-β-D-glucopyranoside, CHEMBL465208) was added to the Open Enzyme candidate screen in `wiki/nlrp3-inhibitor-screen.md` after the 2026-Q3 refresh. Its wiki entry describes a single bibliographic retrieval lead — one MSU animal study (PMID 30265377) — with an explicit note that the primary study has not been rehydrated and no evidence tier has been assigned. The ChEMBL bioactivity profile (211 records, 8 with converted pChEMBL values) shows monoamine oxidase B (MAO-B) as the top annotated protein target, with an IC50 of pChEMBL 6.09 (~810 nM) and a Ki of pChEMBL 6.04 (~910 nM), both from document CHEMBL4706619. MAO-B inhibition is not mentioned in the current wiki entry for salidroside. The remaining five quantified records include PC-12 cell-line functional assays (EC50 6.68, neuroprotection context) and one PEPT2 (SLC15A2) EC50 of 4.55.

This is not a contradiction of the MSU animal claim — MAO-B inhibition and NLRP3/urate-pathway activity are not mutually exclusive, and the animal study result stands on its own evidence. However, MAO-B inhibition at sub-μM concentrations is a mechanistically distinct finding that the wiki does not capture, and it could confound attribution of any anti-inflammatory effect observed in an in vivo salidroside experiment if MAO-B contributes to the inflammatory readout. Before advancing salidroside to a human-cell MSU assay, the primary source for the MAO-B record (CHEMBL4706619) should be rehydrated: confirm compound identity, assay format, cell system, and whether the IC50 translates to a concentration achievable at the relevant compartment.

## Suggested action

1. Verify CHEMBL4706619 against its primary paper: confirm that the salidroside MAO-B IC50 of ~810 nM was measured in a direct biochemical assay, identify the species and assay format, and assess whether it is achievable at relevant exposure.
2. If confirmed, add a brief note to `wiki/nlrp3-inhibitor-screen.md` under the salidroside row (or to the salidroside evidence home once the primary MSU study is rehydrated) flagging MAO-B as a co-occurring target at measured concentrations — **(In Vitro)** evidence, primary-source verified.
3. If the MAO-B IC50 is not reproduced in the primary paper or belongs to a different compound lot, note the retrieval failure and omit.
4. Do not assign a gout-specific evidence tier to salidroside until the MSU animal study (PMID 30265377) itself is rehydrated and the model, material, and endpoint are verified.
