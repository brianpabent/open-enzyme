---
type: evidence-radar
feed: faers
source_ids: ["24911892", "25829665", "26307872", "26508673", "26568533", "26609024", "26727397", "26750462", "26750908", "26762485", "26764905", "26772380", "26786756", "26824843", "26913823", "26915700", "26922332", "26928194", "26928379", "26938691", "26939172", "26994445", "26999978", "27053151", "27090669"]
source_snapshot: {"api_last_updated": "2026-10-28", "download_export_date": "2026-11-02", "latest_available_quarter": "2026Q3", "queried_quarters": ["2026Q2", "2026Q3"]}
reviewed_packet_sha256: d92c502a4db98b3878cda81a8033e01f121dea241fd76bfd087b8edaba942046
review_sha256: 2f3940796ec55746dae97c47537d8adc319539a7d354d444ddb917f4fd5d75d3
canonical_owner: wiki/open-questions.md
---

# Check whether GLP-1/GIP weight-loss agents show a controlled gout/urate imbalance

## Why action remains open

The repeated tirzepatide signal plus semaglutide product signals may reflect diabetes/obesity/weight-change confounding, but it is now concrete enough to verify against trial and label safety sources.

## Source delta

- Drug identity: TIRZEPATIDE
- Released reporting window: 2026Q2, 2026Q3
- Unique reports: 31
- Deduplicated case keys: 31
- Suspect / concomitant / interacting: 25 / 6 / 0
- Informative suspect / sole suspect / high-polypharmacy: 25 / 21 / 0
- Positive rechallenge fields: 0
- Event terms: {"BLOOD URIC ACID INCREASED": 7, "GOUT": 21, "HYPERURICAEMIA": 4}
- Indication fields captured: 26 of 31 deduplicated drug-case rows
- Matching gout/hyperuricemia indication recorded: false (missing or blank indication fields remain unknown)
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen MOUNJARO/ZEPBOUND labels, FDA clinical reviews, SURPASS/SURMOUNT adverse-event and lab tables, and compare with semaglutide product safety tables; look for gout, hyperuricemia, or serum-urate changes versus comparator and for timing around rapid weight loss. Advance only if controlled data show an imbalance or a clear urate-lab pattern; redirect to a metabolic/weight-loss flare conjecture if grounded but untested; kill if trial/regulatory sources do not corroborate.

## Evidence boundary

Unvalidated spontaneous reports only; diabetes, obesity, weight change, renal disease, concomitant drugs, and reporting bias remain major alternative explanations.

Apply any supported change in [wiki/open-questions.md](../../wiki/open-questions.md) and delete this queue file in the same commit. Git is the archive.
