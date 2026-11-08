---
type: evidence-radar
feed: faers
source_ids: ["25506889", "26840971", "26917150", "26939591", "26939592", "26941032", "26941502", "26946281", "26946653", "26950369", "26950975"]
source_snapshot: {"api_last_updated": "2026-10-28", "download_export_date": "2026-11-02", "latest_available_quarter": "2026Q3", "queried_quarters": ["2026Q2", "2026Q3"]}
reviewed_packet_sha256: d92c502a4db98b3878cda81a8033e01f121dea241fd76bfd087b8edaba942046
review_sha256: 2f3940796ec55746dae97c47537d8adc319539a7d354d444ddb917f4fd5d75d3
canonical_owner: wiki/abcg2-modulators.md
---

# Recheck abaloparatide gout boundary against current regulatory sources

## Why action remains open

The repo already states abaloparatide raises serum urate without demonstrated gout excess; the new FAERS cluster is not proof, but it is directly relevant to that boundary and has a concrete regulatory-source verification path.

## Source delta

- Drug identity: ABALOPARATIDE
- Released reporting window: 2026Q2, 2026Q3
- Unique reports: 11
- Deduplicated case keys: 11
- Suspect / concomitant / interacting: 11 / 0 / 0
- Informative suspect / sole suspect / high-polypharmacy: 11 / 11 / 0
- Positive rechallenge fields: 0
- Event terms: {"BLOOD URIC ACID INCREASED": 4, "GOUT": 6, "HYPERURICAEMIA": 1}
- Indication fields captured: 11 of 11 deduplicated drug-case rows
- Matching gout/hyperuricemia indication recorded: false (missing or blank indication fields remain unknown)
- Known gout-treatment identity: false
- Source: https://open.fda.gov/apis/drug/event/

## Required action

Reopen current TYMLOS/Ostabalo labels, FDA/PMDA review materials, and available postmarketing safety updates; determine whether gout has appeared as a labeled/postmarketing event or whether trial extensions show a gout imbalance. Advance by revising the existing ABCG2/PTH1R Research Conjecture only if primary sources change the gout boundary; kill if the label and controlled sources remain limited to urate rise without gout excess.

## Evidence boundary

FAERS reports are unvalidated and cannot establish causality, incidence, or risk; preserve osteoporosis indication, age/comorbidity, missing chronology, and reporting-bias limitations.

Apply any supported change in [wiki/abcg2-modulators.md](../../wiki/abcg2-modulators.md) and delete this queue file in the same commit. Git is the archive.
