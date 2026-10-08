---
type: evidence-radar
feed: clinical_trials
source_ids: ["NCT06771115"]
source_snapshot: {"clinicaltrials_gov": {"api_version": null, "data_timestamp": "2026-10-08T09:00:05", "record_count": 1069}, "who_ictrp": {"record_count": 1033, "registry_imports": {"lblAustralia": "Australian New Zealand Clinical Trials Registry,|5 October 2026", "lblChinese": "Chinese Clinical Trial Registry,|5 October 2026", "lblClinical": "ClinicalTrials.gov,|5 October 2026", "lblCtis": "Clinical Trials Information System (CTIS),|5 October 2026", "lblCuba": "Cuban Public Registry of Clinical Trials,|14 September 2026", "lblEUClinical": "EU Clinical Trials Register (EU-CTR),|5 October 2026", "lblEvery4Weeks": "Brazilian Clinical Trials Registry (ReBec),|14 September 2026", "lblGerman": "German Clinical Trials Register,|14 September 2026", "lblISRCTN": "ISRCTN,|5 October 2026", "lblIndia": "Clinical Trials Registry - India,|14 September 2026", "lblIran": "Iranian Registry of Clinical Trials,|1 June 2026", "lblJapan": "Japan Registry of Clinical Trials (jRCT),|14 September 2026", "lblKorea": "Clinical Research Information Service - Republic of Korea,|5 October 2026", "lblLebanon": "Lebanese Clinical Trials Registry (LBCTR),|2 February 2026", "lblNetherland": "The Netherlands National Trial Register,|5 October 2026", "lblPanafrica": "Pan African Clinical Trial Registry,|14 September 2026", "lblPeru": "Peruvian Clinical Trials Registry (REPEC),|30 March 2026", "lblSriLanka": "Sri Lanka Clinical Trials Registry,|14 September 2026", "lblThai": "Thai Clinical Trials Registry (TCTR),|3 August 2026", "lblTrad": "International Traditional Medicine Clinical Trial Registry (ITMCTR),|3 August 2026"}, "registry_imports_sha256": "e77b3a4aeaa1840c2463b3822bc67ded718c95d4442575bb62516f690bb047b4"}}
reviewed_packet_sha256: 284eee8ac2996d670f875a22c4a319ce91a29f34308c29a5542caea0e561d4ca
review_sha256: 4b25262c097a23c90ed6f85836632661041f0ce26fb82492da6a09e9d98e9837
canonical_owner: wiki/gout-clinical-pipeline.md
---

# VTX3232 (NLRP3 inhibitor) phase 2a obesity results posted (NCT06771115)

## Why action remains open

has_results flipped to true. Posted human safety and inflammatory-biomarker data for an oral NLRP3 inhibitor can inform NLRP3 target-engagement and safety priors for the pipeline page.

## Source delta

- Registry: `NCT06771115` (clinicaltrials.gov)
- Change: changed — enrollment, has_results, interventions, last_update_posted
- Reported status: COMPLETED
- Title: Phase 2a Placebo-Controlled Study of VTX3232 Alone or in Combination With Semaglutide in Obesity
- Intervention(s): Placebo, Placebo in combination with semaglutide, VTX3232 30 mg, VTX3232 30 mg in combination with semaglutide
- Results posted: yes
- Source: https://clinicaltrials.gov/study/NCT06771115

## Required action

Reopen the NCT06771115 results record. Extract the safety and adverse-event tables and any hs-CRP, IL-6 or other inflammatory biomarker outcomes by arm, and note the dose labels now revealed (30 mg vs the earlier 'Dose A'). Advance as a pipeline-page note if biomarker or safety data are interpretable; close if only weight endpoints or sparse safety data are posted.

## Evidence boundary

Registry results in obesity, not gout. Not validated efficacy; do not infer gout flare or urate benefit from an adjacent disease.

Apply any supported change in [wiki/gout-clinical-pipeline.md](../../wiki/gout-clinical-pipeline.md) and delete this queue file in the same commit. Git is the archive.
