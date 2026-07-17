---
type: evidence-radar
feed: faers
source_ids: ["23121792", "23911603", "23945019", "24999531", "25546018", "25585736", "25629113", "25661138", "26116499", "26172490", "26189384", "26290957", "26309292", "26339940", "26340036", "26347260", "26400476", "26410618", "26438944", "26537127", "26548723"]
source_snapshot: {"api_last_updated": "2026-04-28", "download_export_date": "2026-07-13", "latest_available_quarter": "2026Q1", "queried_quarters": ["2026Q1"]}
reviewed_packet_sha256: d4c2bad69e3c8468f12207e12f72836e1c174018b3c4995ef8bface4c56bd162
review_sha256: 0a489cb4b8221300cc102533761f5cf0cde0f0429bfe15b9f00c0c99f70b8da3
canonical_owner: wiki/open-questions.md
---

# Dupilumab gout co-reports may be an immunology-gating lead

## Why action remains open

Twenty-one 2026Q1 FAERS cases, mostly sole/informative suspect, are enough to check whether IL-4/IL-13 blockade has any primary-source gout, hyperuricemia, or inflammatory-arthritis signal. No matching gout indication was recorded in the captured fields, but missing or blank indication fields remain unknown.

## Source delta

- Drug identity: DUPILUMAB
- Released reporting window: 2026Q1
- Unique reports: 21
- Deduplicated case keys: 21
- Suspect / concomitant / interacting: 20 / 1 / 0
- Informative suspect / sole suspect / high-polypharmacy: 19 / 19 / 0
- Positive rechallenge fields: 0
- Event terms: {"GOUT": 21}
- Indication interpretation: no matching gout/hyperuricemia indication was recorded in captured fields; missing or blank fields remain unknown
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen the Dupixent US label/EMA EPAR and pivotal/extension safety tables; a reproducible gout/hyperuricemia imbalance or clear chronology would advance to an IL-4/IL-13–MSU/IL-1 mechanism scan, competing indication/comedication would redirect, and absence from controlled/label sources would kill the thread.

## Evidence boundary

FAERS co-reporting only; does not establish causality, incidence, risk, or chronology.

Apply any supported change in [wiki/open-questions.md](../../wiki/open-questions.md) and delete this queue file in the same commit. Git is the archive.
