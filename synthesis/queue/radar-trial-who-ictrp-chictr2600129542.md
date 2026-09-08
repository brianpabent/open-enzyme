---
type: evidence-radar
feed: clinical_trials
source_ids: ["ChiCTR2600129542"]
source_snapshot: {"clinicaltrials_gov": {"api_version": null, "data_timestamp": "2026-09-08T09:00:04", "record_count": 1058}, "who_ictrp": {"record_count": 1008, "registry_imports": {"lblAustralia": "Australian New Zealand Clinical Trials Registry,|31 August 2026", "lblChinese": "Chinese Clinical Trial Registry,|31 August 2026", "lblClinical": "ClinicalTrials.gov,|31 August 2026", "lblCtis": "Clinical Trials Information System (CTIS),|31 August 2026", "lblCuba": "Cuban Public Registry of Clinical Trials,|10 August 2026", "lblEUClinical": "EU Clinical Trials Register (EU-CTR),|31 August 2026", "lblEvery4Weeks": "Brazilian Clinical Trials Registry (ReBec),|3 August 2026", "lblGerman": "German Clinical Trials Register,|3 August 2026", "lblISRCTN": "ISRCTN,|31 August 2026", "lblIndia": "Clinical Trials Registry - India,|3 August 2026", "lblIran": "Iranian Registry of Clinical Trials,|1 June 2026", "lblJapan": "Japan Registry of Clinical Trials (jRCT),|29 June 2026", "lblKorea": "Clinical Research Information Service - Republic of Korea,|31 August 2026", "lblLebanon": "Lebanese Clinical Trials Registry (LBCTR),|2 February 2026", "lblNetherland": "The Netherlands National Trial Register,|31 August 2026", "lblPanafrica": "Pan African Clinical Trial Registry,|3 August 2026", "lblPeru": "Peruvian Clinical Trials Registry (REPEC),|30 March 2026", "lblSriLanka": "Sri Lanka Clinical Trials Registry,|3 August 2026", "lblThai": "Thai Clinical Trials Registry (TCTR),|3 August 2026", "lblTrad": "International Traditional Medicine Clinical Trial Registry (ITMCTR),|3 August 2026"}, "registry_imports_sha256": "06f44a4ca6050f63784fcc803b9100c0324b419bc0f183f7c15cf3357e7748a7"}}
reviewed_packet_sha256: ef00572294950f1bb0aa71ebca90fc4480245cb6183bf552cc014ddc5b1e9215
review_sha256: f5810163aad58b4f55bdd3d712b2e0a64a7ef66cb68b9c71691c3878d0832dd1
canonical_owner: wiki/gout-clinical-pipeline.md
---

# Verify tininurad food-effect PK registration and gout/hyperuricemia development relevance

## Why action remains open

A new uricosuric/urate-lowering asset entering human PK work could alter the gout clinical-pipeline map if the primary ChiCTR record confirms mechanism, sponsor, and development context.

## Source delta

- Registry: `ChiCTR2600129542` (who-ictrp)
- Change: new — new_record
- Reported status: Not Recruiting
- Title: A Phase I Study to Evaluate the Effect of Food on the Pharmacokinetics of Tininurad Tablets in Healthy Chinese Subjects
- Intervention(s): not supplied in the compact record
- Results posted: no
- Source: https://trialsearch.who.int/Trial2.aspx?TrialID=ChiCTR2600129542

## Required action

Reopen WHO ICTRP ChiCTR2600129542 and, if accessible, the ChiCTR primary record; advance if it confirms tininurad tablets as a gout/hyperuricemia urate-lowering candidate with food-effect PK details and identifiable sponsor/program, redirect if it is a non-gout pharmacology record, and kill if primary details cannot verify the compound or indication context.

## Evidence boundary

Registry metadata only; a food-effect PK registration is not efficacy evidence and does not establish clinical benefit or safety in gout.

Apply any supported change in [wiki/gout-clinical-pipeline.md](../../wiki/gout-clinical-pipeline.md) and delete this queue file in the same commit. Git is the archive.
