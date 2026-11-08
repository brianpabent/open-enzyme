---
type: evidence-radar
feed: faers
source_ids: ["21144605", "21374384", "21398287", "21808283", "23249633", "23277389", "23597920", "23996706", "24010448", "24092081", "24672038", "24982181", "25875919", "26459105", "26593323", "26625058", "26657591", "26683629", "26692283", "26693065", "26774425", "26821072", "26917814", "27136166"]
source_snapshot: {"api_last_updated": "2026-10-28", "download_export_date": "2026-11-02", "latest_available_quarter": "2026Q3", "queried_quarters": ["2026Q2", "2026Q3"]}
reviewed_packet_sha256: d92c502a4db98b3878cda81a8033e01f121dea241fd76bfd087b8edaba942046
review_sha256: 2f3940796ec55746dae97c47537d8adc319539a7d354d444ddb917f4fd5d75d3
canonical_owner: wiki/sirna-urat1-modality.md
---

# Verify whether inclisiran or PCSK9 silencing has a controlled urate/gout safety signal

## Why action remains open

Inclisiran is used in the repo as an RNAi-delivery precedent; a repeated gout/urate FAERS signal could affect how the siRNA-URAT1 precedent is framed, but must be checked against primary controlled sources.

## Source delta

- Drug identity: INCLISIRAN
- Released reporting window: 2026Q2, 2026Q3
- Unique reports: 24
- Deduplicated case keys: 24
- Suspect / concomitant / interacting: 24 / 0 / 0
- Informative suspect / sole suspect / high-polypharmacy: 24 / 24 / 0
- Positive rechallenge fields: 0
- Event terms: {"BLOOD URIC ACID INCREASED": 18, "GOUT": 7}
- Indication fields captured: 24 of 24 deduplicated drug-case rows
- Matching gout/hyperuricemia indication recorded: false (missing or blank indication fields remain unknown)
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen LEQVIO/inclisiran label, FDA/EMA review documents, ORION trial safety tables, and PCSK9 comparator safety context where available; look for gout, hyperuricemia, or serum-urate lab imbalance versus placebo/standard care. Advance to a compact Research Conjecture only if controlled/regulatory sources show a consistent signal; redirect toward PCSK9 biology if evolocumab/alirocumab share it; kill if the signal is absent or clearly reporting-context noise.

## Evidence boundary

FAERS is an unvalidated lead and cannot establish causality, incidence, or risk; preserve indication, chronology, reporting bias, and comparator limitations.

Apply any supported change in [wiki/sirna-urat1-modality.md](../../wiki/sirna-urat1-modality.md) and delete this queue file in the same commit. Git is the archive.
