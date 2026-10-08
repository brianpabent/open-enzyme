---
type: evidence-radar
feed: clinical_trials
source_ids: ["NCT07824895"]
source_snapshot: {"clinicaltrials_gov": {"api_version": null, "data_timestamp": "2026-10-08T09:00:05", "record_count": 1069}, "who_ictrp": {"record_count": 1033, "registry_imports": {"lblAustralia": "Australian New Zealand Clinical Trials Registry,|5 October 2026", "lblChinese": "Chinese Clinical Trial Registry,|5 October 2026", "lblClinical": "ClinicalTrials.gov,|5 October 2026", "lblCtis": "Clinical Trials Information System (CTIS),|5 October 2026", "lblCuba": "Cuban Public Registry of Clinical Trials,|14 September 2026", "lblEUClinical": "EU Clinical Trials Register (EU-CTR),|5 October 2026", "lblEvery4Weeks": "Brazilian Clinical Trials Registry (ReBec),|14 September 2026", "lblGerman": "German Clinical Trials Register,|14 September 2026", "lblISRCTN": "ISRCTN,|5 October 2026", "lblIndia": "Clinical Trials Registry - India,|14 September 2026", "lblIran": "Iranian Registry of Clinical Trials,|1 June 2026", "lblJapan": "Japan Registry of Clinical Trials (jRCT),|14 September 2026", "lblKorea": "Clinical Research Information Service - Republic of Korea,|5 October 2026", "lblLebanon": "Lebanese Clinical Trials Registry (LBCTR),|2 February 2026", "lblNetherland": "The Netherlands National Trial Register,|5 October 2026", "lblPanafrica": "Pan African Clinical Trial Registry,|14 September 2026", "lblPeru": "Peruvian Clinical Trials Registry (REPEC),|30 March 2026", "lblSriLanka": "Sri Lanka Clinical Trials Registry,|14 September 2026", "lblThai": "Thai Clinical Trials Registry (TCTR),|3 August 2026", "lblTrad": "International Traditional Medicine Clinical Trial Registry (ITMCTR),|3 August 2026"}, "registry_imports_sha256": "e77b3a4aeaa1840c2463b3822bc67ded718c95d4442575bb62516f690bb047b4"}}
reviewed_packet_sha256: 284eee8ac2996d670f875a22c4a319ce91a29f34308c29a5542caea0e561d4ca
review_sha256: 4b25262c097a23c90ed6f85836632661041f0ce26fb82492da6a09e9d98e9837
canonical_owner: wiki/gout-clinical-pipeline.md
---

# Mazdutide gout/hyperuricemia phase 4 registration (NCT07824895) joins a second incretin-gout record

## Why action remains open

Two new registrations in one window test a GLP-1/glucagon agonist in obese gout (NCT07824895 and ChiCTR2600131243), suggesting incretin-mediated urate or flare effects are being probed. The pipeline page has no coverage of this class.

## Source delta

- Registry: `NCT07824895` (clinicaltrials.gov)
- Change: new — new_record
- Reported status: NOT_YET_RECRUITING
- Title: Mazdutide for Weight Management and Gout in Adults With Obesity
- Intervention(s): Mazdutide
- Results posted: no
- Source: https://clinicaltrials.gov/study/NCT07824895

## Required action

Reopen NCT07824895 and ChiCTR2600131243 and extract primary and secondary outcomes (serum urate, flare rate), comparators, the ULT background and enrollment. Advance as a pipeline-page entry if urate or flare endpoints are prespecified; close if the endpoints are weight or metabolic only. Check for any related ChiCTR2600130538 SUA-on-glucose-lowering-drug design overlap.

## Evidence boundary

Registrations only; no data. Weight-loss-associated urate changes cannot be separated from drug-specific effects from registry metadata. No efficacy implied.

Apply any supported change in [wiki/gout-clinical-pipeline.md](../../wiki/gout-clinical-pipeline.md) and delete this queue file in the same commit. Git is the archive.
