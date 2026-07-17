---
type: evidence-radar
feed: faers
source_ids: ["23339186", "26232487", "26251913", "26264173", "26264179", "26363665"]
source_snapshot: {"api_last_updated": "2026-04-28", "download_export_date": "2026-07-13", "latest_available_quarter": "2026Q1", "queried_quarters": ["2026Q1"]}
reviewed_packet_sha256: d4c2bad69e3c8468f12207e12f72836e1c174018b3c4995ef8bface4c56bd162
review_sha256: 0a489cb4b8221300cc102533761f5cf0cde0f0429bfe15b9f00c0c99f70b8da3
canonical_owner: wiki/open-questions.md
---

# Tolvaptan urate-increase co-reports are a renal water-handling lead

## Why action remains open

Most reports use blood-uric-acid-increased/hyperuricemia terms, and an aquaretic kidney/cardiac drug offers a concrete route to test dehydration/osmolality effects on urate handling.

## Source delta

- Drug identity: TOLVAPTAN
- Released reporting window: 2026Q1
- Unique reports: 6
- Deduplicated case keys: 6
- Suspect / concomitant / interacting: 5 / 1 / 0
- Informative suspect / sole suspect / high-polypharmacy: 5 / 5 / 0
- Positive rechallenge fields: 0
- Event terms: {"BLOOD URIC ACID INCREASED": 5, "GOUT": 1, "HYPERURICAEMIA": 1}
- Indication interpretation: no matching gout/hyperuricemia indication was recorded in captured fields; missing or blank fields remain unknown
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen the Samsca/Jynarque labels and TEMPO/REPRISE safety sources; documented serum-urate/gout excess with aquaresis or dehydration context advances a hydration-osmolality/urate thread, ADPKD/CKD-only confounding redirects, and no controlled imbalance kills the lead.

## Evidence boundary

FAERS co-reporting only; does not establish causality, incidence, risk, or chronology.

Apply any supported change in [wiki/open-questions.md](../../wiki/open-questions.md) and delete this queue file in the same commit. Git is the archive.
