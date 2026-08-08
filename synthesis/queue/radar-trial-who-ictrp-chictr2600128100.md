---
type: evidence-radar
feed: clinical_trials
source_ids: ["ChiCTR2600128100"]
source_snapshot: {"clinicaltrials_gov": {"api_version": null, "data_timestamp": "2026-08-07T09:00:05", "record_count": 1053}, "who_ictrp": {"record_count": 1011, "registry_imports": {"lblAustralia": "Australian New Zealand Clinical Trials Registry,|3 August 2026", "lblChinese": "Chinese Clinical Trial Registry,|3 August 2026", "lblClinical": "ClinicalTrials.gov,|3 August 2026", "lblCtis": "Clinical Trials Information System (CTIS),|3 August 2026", "lblCuba": "Cuban Public Registry of Clinical Trials,|22 June 2026", "lblEUClinical": "EU Clinical Trials Register (EU-CTR),|3 August 2026", "lblEvery4Weeks": "Brazilian Clinical Trials Registry (ReBec),|3 August 2026", "lblGerman": "German Clinical Trials Register,|3 August 2026", "lblISRCTN": "ISRCTN,|3 August 2026", "lblIndia": "Clinical Trials Registry - India,|3 August 2026", "lblIran": "Iranian Registry of Clinical Trials,|1 June 2026", "lblJapan": "Japan Registry of Clinical Trials (jRCT),|29 June 2026", "lblKorea": "Clinical Research Information Service - Republic of Korea,|3 August 2026", "lblLebanon": "Lebanese Clinical Trials Registry (LBCTR),|2 February 2026", "lblNetherland": "The Netherlands National Trial Register,|3 August 2026", "lblPanafrica": "Pan African Clinical Trial Registry,|3 August 2026", "lblPeru": "Peruvian Clinical Trials Registry (REPEC),|30 March 2026", "lblSriLanka": "Sri Lanka Clinical Trials Registry,|3 August 2026", "lblThai": "Thai Clinical Trials Registry (TCTR),|3 August 2026", "lblTrad": "International Traditional Medicine Clinical Trial Registry (ITMCTR),|3 August 2026"}, "registry_imports_sha256": "99a4658aa18b8839721930990a84484a03a7652382c70a8e951f2a0973caf16c"}}
reviewed_packet_sha256: fe025c08068c15838ae382ee509707525e7413280a5be4a0fa78661eb95f658b
review_sha256: 71672fc779f18c9e52790dd86016bdaf5eb3bc9701fb39473c60693544eb2e50
canonical_owner: wiki/gout-clinical-pipeline.md
---

# New registered probiotic-strain RCT for hyperuricemia

## Why action remains open

WHO ICTRP surfaced a multicenter randomized double-blind placebo-controlled hyperuricemia study naming Bifidobacterium longum subsp. longum BL-G301 and Lactobacillus acidophilus LA-G80, a specific intestinal-urate intervention that can be verified at the primary registry.

## Source delta

- Registry: `ChiCTR2600128100` (who-ictrp)
- Change: new — new_record
- Reported status: Not Recruiting
- Title: A multicenter randomized double-blind placebo-controlled study of combined intervention with Bifidobacterium longum subsp. longum BL-G301 and Lactobacillus acidophilus LA-G80 for hyperuricemia
- Intervention(s): not supplied in the compact record
- Results posted: no
- Source: https://trialsearch.who.int/Trial2.aspx?TrialID=ChiCTR2600128100

## Required action

Reopen ChiCTR2600128100 and the primary ChiCTR record; capture eligibility, endpoints, strain identity/doses, comparator, status, and planned urate readouts. Advance if serum urate/gout-relevant outcomes and strain details are present; redirect to a compact Research Conjecture if only a plausible untested intestinal-urate mechanism remains; kill if no primary record/details can be verified.

## Evidence boundary

WHO/ChiCTR registration only; not evidence of efficacy, causality, or a strain effect.

Apply any supported change in [wiki/gout-clinical-pipeline.md](../../wiki/gout-clinical-pipeline.md) and delete this queue file in the same commit. Git is the archive.
