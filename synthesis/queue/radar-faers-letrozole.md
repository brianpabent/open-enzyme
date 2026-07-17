---
type: evidence-radar
feed: faers
source_ids: ["19642475", "20405369", "21408087", "22000822", "26210661", "26348202", "26381023", "26410521", "26411645", "26440127", "26452161", "26525115"]
source_snapshot: {"api_last_updated": "2026-04-28", "download_export_date": "2026-07-13", "latest_available_quarter": "2026Q1", "queried_quarters": ["2026Q1"]}
reviewed_packet_sha256: 004c74f2ec37bfff57d1b914ac6f77950ee25a25bca23ed8dd1f8d74d8e21379
review_sha256: cbcacc1a2a13edf5f4b013851cc0b9ecc159755baf50636ea2ab305f626cae4c
canonical_owner: wiki/androgen-urate-axis.md
---

# Check whether letrozole/aromatase-inhibitor urate reports reflect a real androgen-urate-axis liability

## Why action remains open

Aromatase inhibition is already an OE urate-axis subject; this new FAERS cluster is not efficacy evidence but is specific enough to justify checking primary safety sources and class recurrence before the signal is forgotten.

## Source delta

- Drug identity: LETROZOLE
- Released reporting window: 2026Q1
- Unique reports: 12
- Deduplicated case keys: 10
- Suspect / concomitant / interacting: 4 / 6 / 0
- Informative suspect / sole suspect / high-polypharmacy: 2 / 1 / 0
- Positive rechallenge fields: 0
- Event terms: {"BLOOD URIC ACID INCREASED": 7, "GOUT": 2, "HYPERURICAEMIA": 1}
- Indication fields captured: 8 of 10 deduplicated drug-case rows
- Matching gout/hyperuricemia indication recorded: false (missing or blank indication fields remain unknown)
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen the openFDA/FAERS 2026Q1 letrozole case set and primary aromatase-inhibitor sources: FDA/EMA labels plus trial safety tables for letrozole, anastrozole, and exemestane. Advance if urate/gout terms recur across the class or primary safety tables show urate/gout imbalance; redirect if confined to cancer co-therapy, renal dysfunction, or tumor-lysis context; kill if no class or primary-source support is found.

## Evidence boundary

Unvalidated spontaneous-report association; not causality, incidence, or risk, and breast-cancer therapy context may confound reports.

Apply any supported change in [wiki/androgen-urate-axis.md](../../wiki/androgen-urate-axis.md) and delete this queue file in the same commit. Git is the archive.
