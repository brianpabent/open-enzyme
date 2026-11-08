---
type: evidence-radar
feed: faers
source_ids: ["23201171", "23218844", "23448615", "23580228", "24380751", "24555295", "24621082", "24861797", "24973726", "25380653", "25829665", "25984959", "26056289", "26193288", "26218063", "26694670", "26697348", "26699978", "26812708", "26939172", "27324680", "27330108"]
source_snapshot: {"api_last_updated": "2026-10-28", "download_export_date": "2026-11-02", "latest_available_quarter": "2026Q3", "queried_quarters": ["2026Q2", "2026Q3"]}
reviewed_packet_sha256: d92c502a4db98b3878cda81a8033e01f121dea241fd76bfd087b8edaba942046
review_sha256: 2f3940796ec55746dae97c47537d8adc319539a7d354d444ddb917f4fd5d75d3
canonical_owner: wiki/open-questions.md
---

# Verify whether sparsentan trials or label show gout/urate worsening

## Why action remains open

The repeated renal-drug cluster is confounded by CKD/IgA nephropathy/FSGS, but the low polypharmacy and many sole-suspect reports make a targeted primary-source safety check reasonable.

## Source delta

- Drug identity: SPARSENTAN
- Released reporting window: 2026Q2, 2026Q3
- Unique reports: 22
- Deduplicated case keys: 22
- Suspect / concomitant / interacting: 22 / 0 / 0
- Informative suspect / sole suspect / high-polypharmacy: 22 / 20 / 0
- Positive rechallenge fields: 0
- Event terms: {"BLOOD URIC ACID INCREASED": 4, "GOUT": 18}
- Indication fields captured: 22 of 22 deduplicated drug-case rows
- Matching gout/hyperuricemia indication recorded: false (missing or blank indication fields remain unknown)
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen FILSPARI label, FDA review, and PROTECT/DUPLEX safety/lab appendices; look for gout, hyperuricemia, serum-urate changes, diuretic background, and renal-function stratification versus control. Advance only if controlled/regulatory sources show a urate or gout imbalance; redirect to renal-hemodynamic/transport conjecture if grounded but untested; kill if no controlled imbalance is present.

## Evidence boundary

FAERS lead only; renal disease, background therapies, missing chronology, and reporting bias prevent causal or risk inference.

Apply any supported change in [wiki/open-questions.md](../../wiki/open-questions.md) and delete this queue file in the same commit. Git is the archive.
