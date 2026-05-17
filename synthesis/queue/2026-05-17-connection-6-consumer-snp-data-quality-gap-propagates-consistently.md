---
type: connection
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 6
global_index: 6
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Consumer SNP data-quality gap propagates consistently across three pages — a quality-discipline pattern that the platform should name rather than repeat.

6. **Consumer SNP data-quality gap propagates consistently across three pages — a quality-discipline pattern that the platform should name rather than repeat.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `gout-action-guide.md`, `personal-genome-protocol.md`, `gout-genetic-variants.md`
   - *Page-pair linkage:* `gout-action-guide.md` → `personal-genome-protocol.md` is linked (action guide routes through personal-genome for variant-informed selection). `gout-action-guide.md` → `gout-genetic-variants.md` is linked. `personal-genome-protocol.md` → `gout-genetic-variants.md` is linked in the variant index's cross-references.
   - *Why It Matters:* All three pages now independently carry the same warning: consumer SNP arrays (23andMe, AncestryDNA) are NOT recommended for gout-relevant variant typing because (a) raw SNP data quality is uneven for the specific variants gout stack design depends on, (b) the chips are optimized for common-variant GWAS imputation, not precision pharmacogenetics, and (c) a clinical-grade CLIA PCR or WGS is the right tool. This is a **quality-discipline pattern** — the same warning propagated consistently across three pages that serve different audiences (patient-facing action guide, protocol-level sequencing guide, variant-index reference). Rather than repeating the warning in each page, the platform should name it as a standing quality discipline and link to a single canonical statement.
   - *Suggested Action:* Add a "Consumer SNP data-quality caveat" section to `gout-genetic-variants.md` §"How to test — testing tiers at a glance" and replace the per-page warnings in `gout-action-guide.md` and `personal-genome-protocol.md` with a one-line cross-reference. The canonical statement lives in the variant index; the other pages link to it.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The warning is genuinely repeated across surfaces: `gout-action-guide.md` says consumer panels are not recommended for gout stack design, `personal-genome-protocol.md` names the data-quality gap for ABCG2 Q141K, SLC2A9, SLC22A12, and HLA-B*58:01, and `gout-genetic-variants.md` says consumer SNP arrays are personal-exploration only and not clinical-grade. Promoting a single canonical caveat in `gout-genetic-variants.md` is a maintenance improvement and a clearer quality-discipline pattern.
