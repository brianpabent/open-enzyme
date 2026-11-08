---
type: evidence-radar
feed: faers
source_ids: ["22597333", "23854945", "24447500", "24831433", "25295436", "25897193", "26172417", "26172490", "26201024", "26410618", "26495812", "26591608", "26623331", "26625085", "26638993", "26655507", "26681834", "26686996", "26708818", "26737947", "26752056", "26758224", "26835728", "26842447", "26863314"]
source_snapshot: {"api_last_updated": "2026-10-28", "download_export_date": "2026-11-02", "latest_available_quarter": "2026Q3", "queried_quarters": ["2026Q2", "2026Q3"]}
reviewed_packet_sha256: d92c502a4db98b3878cda81a8033e01f121dea241fd76bfd087b8edaba942046
review_sha256: 2f3940796ec55746dae97c47537d8adc319539a7d354d444ddb917f4fd5d75d3
canonical_owner: wiki/open-questions.md
---

# Check whether dupilumab has any controlled gout or urate safety imbalance

## Why action remains open

The Q2-Q3 FAERS cluster is sizable for a non-gout biologic and mostly sole-suspect, making it a concrete lead for a bounded label/clinical-review verification task rather than a causal claim.

## Source delta

- Drug identity: DUPILUMAB
- Released reporting window: 2026Q2, 2026Q3
- Unique reports: 47
- Deduplicated case keys: 47
- Suspect / concomitant / interacting: 44 / 3 / 0
- Informative suspect / sole suspect / high-polypharmacy: 43 / 42 / 1
- Positive rechallenge fields: 0
- Event terms: {"BLOOD URIC ACID INCREASED": 3, "GOUT": 40, "GOUTY ARTHRITIS": 2, "HYPERURICAEMIA": 3}
- Indication fields captured: 46 of 47 deduplicated drug-case rows
- Matching gout/hyperuricemia indication recorded: false (missing or blank indication fields remain unknown)
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen the current DUPIXENT label, FDA/EMA clinical review materials, and pivotal/extension safety tables; look specifically for gout, hyperuricemia, or serum-urate lab imbalance versus comparator. Advance only if a controlled or regulatory source shows a reproducible imbalance; redirect to an immune-axis Research Conjecture if grounded but untested; kill if absent or explained by indication/comorbidity/reporting artifacts.

## Evidence boundary

Unvalidated spontaneous-report association; not causality, incidence, or risk. Captured indication fields are incomplete and reporting bias, concomitant drugs, chronology, and duplicate limits remain.

Apply any supported change in [wiki/open-questions.md](../../wiki/open-questions.md) and delete this queue file in the same commit. Git is the archive.
