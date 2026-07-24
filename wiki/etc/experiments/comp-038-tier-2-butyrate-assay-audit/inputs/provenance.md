# COMP-038 provenance

## 2026-05-20 discovery run

The original run queried PubMed E-utilities using the 27 exact searches in
[`query-strategy.json`](./query-strategy.json). It captured 74 title/abstract
records at `2026-05-20T15:06:05+00:00` in
[`../outputs/pubmed-snapshot.json`](../outputs/pubmed-snapshot.json).
Codex/GPT-5.5 performed five in-session synthesis trajectories and wrote the
first result at `2026-05-20T15:09:12+00:00`. No OpenRouter calls were made.

That run was a discovery scan. PubMed abstracts were not full-text method
verification, and the absence of a qualifying assay from that bounded search
was not proof that none existed.

The original scan did not cover regional non-English databases. This is a
frozen historical limitation, not an acceptable design for a future refreshed
search. A future landscape update must follow the repository's current
global-multilingual literature workflow.

## 2026-07-15 manual addendum

Git commit `db5d674f43d4668983b73db8c6852868251e2133` appended a section headed
“Full-text verification addendum (2026-07-14)” to `outputs/summary.md`.
Neither that commit nor reachable prior history contains a July 14 full-text
retrieval, extracted protocol, bounded source read, or verification receipt.
`results.json` and this provenance file also remained unchanged.

The addendum therefore has no authority as proof that a July 14 full-text
verification occurred. Its scientific details must be retained only when a
newly dated source read supports them.

## 2026-07-24 corrective source read

The approved repair is limited to the two primary papers named by the
addendum:

| Source | Identity | Access used | Permitted evidence scope |
|---|---|---|---|
| De Baere et al. 2013 | PMID 23542733; DOI `10.1016/j.jpba.2013.02.032` | PubMed-indexed primary abstract reproduced by the U.S. EPA HERO record | Abstract-level method fields only. Do not label this source full-text verified. |
| Gu et al. 2026 | PMID 42041444; PMCID PMC13114974; DOI `10.3390/bios16040223` | NCBI PMC full text and article tables/supplement index | Full-text method and within-study test-cohort fields. Do not relabel the source study as external independent replication. |

This is targeted identifier-based verification, not a refreshed literature
search. No non-English text is involved, so the two-model translation protocol
is not triggered. The output must record access scope, exact supported fields,
section or table location, reviewer date, and retractions. Any field that
cannot be reconstructed from these sources is omitted.

The compact method receipt belongs at
`logs/lit-scans/comp-038-primary-source-verification-2026-07-24.json`.
Scientific interpretation remains in the canonical wiki pages.

## Evidence boundaries

- De Baere supports a published HPLC-UV method in bacterial culture
  supernatants. It does not qualify that method for an Open Enzyme strain or
  medium.
- Gu supports performance in an independent test cohort within the same
  source study. It does not supply independent external replication or an
  adopted Open Enzyme implementation.
- The original scan's SCFA/ELISA outcome remains RED-provisional: no qualifying
  primary comparison surfaced in the documented bounded search. This is not an
  exhaustive absence claim.
- HPLC-UV and GC-MS are Tier 3 when run in-house under the current
  quantification ladder; outsourced qualified testing is Tier 4.
