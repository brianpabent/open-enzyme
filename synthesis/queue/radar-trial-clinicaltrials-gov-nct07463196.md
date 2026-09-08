---
type: evidence-radar
feed: clinical_trials
source_ids: ["NCT07463196"]
source_snapshot: {"clinicaltrials_gov": {"api_version": null, "data_timestamp": "2026-09-08T09:00:04", "record_count": 1058}, "who_ictrp": {"record_count": 1008, "registry_imports": {"lblAustralia": "Australian New Zealand Clinical Trials Registry,|31 August 2026", "lblChinese": "Chinese Clinical Trial Registry,|31 August 2026", "lblClinical": "ClinicalTrials.gov,|31 August 2026", "lblCtis": "Clinical Trials Information System (CTIS),|31 August 2026", "lblCuba": "Cuban Public Registry of Clinical Trials,|10 August 2026", "lblEUClinical": "EU Clinical Trials Register (EU-CTR),|31 August 2026", "lblEvery4Weeks": "Brazilian Clinical Trials Registry (ReBec),|3 August 2026", "lblGerman": "German Clinical Trials Register,|3 August 2026", "lblISRCTN": "ISRCTN,|31 August 2026", "lblIndia": "Clinical Trials Registry - India,|3 August 2026", "lblIran": "Iranian Registry of Clinical Trials,|1 June 2026", "lblJapan": "Japan Registry of Clinical Trials (jRCT),|29 June 2026", "lblKorea": "Clinical Research Information Service - Republic of Korea,|31 August 2026", "lblLebanon": "Lebanese Clinical Trials Registry (LBCTR),|2 February 2026", "lblNetherland": "The Netherlands National Trial Register,|31 August 2026", "lblPanafrica": "Pan African Clinical Trial Registry,|3 August 2026", "lblPeru": "Peruvian Clinical Trials Registry (REPEC),|30 March 2026", "lblSriLanka": "Sri Lanka Clinical Trials Registry,|3 August 2026", "lblThai": "Thai Clinical Trials Registry (TCTR),|3 August 2026", "lblTrad": "International Traditional Medicine Clinical Trial Registry (ITMCTR),|3 August 2026"}, "registry_imports_sha256": "06f44a4ca6050f63784fcc803b9100c0324b419bc0f183f7c15cf3357e7748a7"}}
reviewed_packet_sha256: ef00572294950f1bb0aa71ebca90fc4480245cb6183bf552cc014ddc5b1e9215
review_sha256: f5810163aad58b4f55bdd3d712b2e0a64a7ef66cb68b9c71691c3878d0832dd1
canonical_owner: wiki/gout-clinical-pipeline.md
---

# Verify ACI-19764 as a gout-relevant NLRP3/immune pharmacology lead

## Why action remains open

The registry expansion adds higher-inflammatory-risk cohorts and immune-effect language; confirming target and PD endpoints could define a bounded NLRP3 research conjecture rather than a generic adjacent-disease listing.

## Source delta

- Registry: `NCT07463196` (clinicaltrials.gov)
- Change: changed — completion, conditions, enrollment, interventions, last_update_posted, primary_completion, title
- Reported status: RECRUITING
- Title: A Study Investigating the Safety, Absorption, Elimination, and the Effect on the Immune System of ACI-19764 in Healthy Participants and in Participants With Cardiovascular Risk Factors
- Intervention(s): ACI-19764 at dose A1, ACI-19764 at dose A2, ACI-19764 at dose A3, ACI-19764 at dose A4, ACI-19764 at dose A5, ACI-19764 at dose A6, ACI-19764 at dose B1, ACI-19764 at dose B2, ACI-19764 at dose B3, ACI-19764 at dose C1, Placebo
- Results posted: no
- Source: https://clinicaltrials.gov/study/NCT07463196

## Required action

Reopen ClinicalTrials.gov NCT07463196 and any linked sponsor/protocol materials; advance only if the primary record or sponsor source identifies ACI-19764 as an NLRP3/inflammasome-pathway modulator with interpretable IL-1β/IL-18, ex vivo inflammasome, or related PD endpoints that could bridge to MSU biology; redirect if the target is different, and kill if it is only nonspecific safety/PK without immune PD detail.

## Evidence boundary

Registry protocol/status metadata only; not evidence of efficacy, gout benefit, or causal NLRP3 modulation until primary-source pharmacology/results are verified.

Apply any supported change in [wiki/gout-clinical-pipeline.md](../../wiki/gout-clinical-pipeline.md) and delete this queue file in the same commit. Git is the archive.
