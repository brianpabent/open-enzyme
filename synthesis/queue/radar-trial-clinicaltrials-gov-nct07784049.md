---
type: evidence-radar
feed: clinical_trials
source_ids: ["NCT07784049"]
source_snapshot: {"clinicaltrials_gov": {"api_version": null, "data_timestamp": "2026-09-08T09:00:04", "record_count": 1058}, "who_ictrp": {"record_count": 1008, "registry_imports": {"lblAustralia": "Australian New Zealand Clinical Trials Registry,|31 August 2026", "lblChinese": "Chinese Clinical Trial Registry,|31 August 2026", "lblClinical": "ClinicalTrials.gov,|31 August 2026", "lblCtis": "Clinical Trials Information System (CTIS),|31 August 2026", "lblCuba": "Cuban Public Registry of Clinical Trials,|10 August 2026", "lblEUClinical": "EU Clinical Trials Register (EU-CTR),|31 August 2026", "lblEvery4Weeks": "Brazilian Clinical Trials Registry (ReBec),|3 August 2026", "lblGerman": "German Clinical Trials Register,|3 August 2026", "lblISRCTN": "ISRCTN,|31 August 2026", "lblIndia": "Clinical Trials Registry - India,|3 August 2026", "lblIran": "Iranian Registry of Clinical Trials,|1 June 2026", "lblJapan": "Japan Registry of Clinical Trials (jRCT),|29 June 2026", "lblKorea": "Clinical Research Information Service - Republic of Korea,|31 August 2026", "lblLebanon": "Lebanese Clinical Trials Registry (LBCTR),|2 February 2026", "lblNetherland": "The Netherlands National Trial Register,|31 August 2026", "lblPanafrica": "Pan African Clinical Trial Registry,|3 August 2026", "lblPeru": "Peruvian Clinical Trials Registry (REPEC),|30 March 2026", "lblSriLanka": "Sri Lanka Clinical Trials Registry,|3 August 2026", "lblThai": "Thai Clinical Trials Registry (TCTR),|3 August 2026", "lblTrad": "International Traditional Medicine Clinical Trial Registry (ITMCTR),|3 August 2026"}, "registry_imports_sha256": "06f44a4ca6050f63784fcc803b9100c0324b419bc0f183f7c15cf3357e7748a7"}}
reviewed_packet_sha256: ef00572294950f1bb0aa71ebca90fc4480245cb6183bf552cc014ddc5b1e9215
review_sha256: f5810163aad58b4f55bdd3d712b2e0a64a7ef66cb68b9c71691c3878d0832dd1
canonical_owner: wiki/gout-clinical-pipeline.md
---

# Verify DECT foot MSU burden versus CCTA coronary atheroma protocol

## Why action remains open

If the primary record specifies quantitative DECT MSU deposition and CCTA plaque endpoints with relevant covariates, it could ground a research conjecture about gout crystal burden and cardiovascular imaging phenotypes.

## Source delta

- Registry: `NCT07784049` (clinicaltrials.gov)
- Change: new — new_record
- Reported status: NOT_YET_RECRUITING
- Title: The Correlation Between Sodium Urate (MSU) Deposition and Coronary Atherosclerosis in Patients With Foot Gout
- Intervention(s): DECT;CCTA
- Results posted: no
- Source: https://clinicaltrials.gov/study/NCT07784049

## Required action

Reopen ClinicalTrials.gov NCT07784049; advance if the protocol defines quantitative MSU deposition and coronary plaque/atheroma measures plus planned adjustment for serum urate, urate-lowering therapy, kidney function, and cardiovascular risk factors; redirect to general gout comorbidity tracking if endpoints are descriptive only, and kill if imaging or covariate detail is too vague to interpret.

## Evidence boundary

Registry registration only; any future association would be observational correlation, not evidence that MSU deposition causes coronary atherosclerosis or that treating gout changes coronary outcomes.

Apply any supported change in [wiki/gout-clinical-pipeline.md](../../wiki/gout-clinical-pipeline.md) and delete this queue file in the same commit. Git is the archive.
