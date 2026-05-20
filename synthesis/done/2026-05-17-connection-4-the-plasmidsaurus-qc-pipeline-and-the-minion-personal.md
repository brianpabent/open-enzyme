---
type: connection
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 4
global_index: 4
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# The Plasmidsaurus QC pipeline and the MinION personal-genome buildout answer overlapping questions via different instruments — a "dual-platform verification" pattern that is implicit but unnamed.

4. **The Plasmidsaurus QC pipeline and the MinION personal-genome buildout answer overlapping questions via different instruments — a "dual-platform verification" pattern that is implicit but unnamed.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `engineered-koji-protocol.md`, `personal-genome-protocol.md`
   - *Page-pair linkage:* `engineered-koji-protocol.md` and `personal-genome-protocol.md` are **not directly cross-referenced**. The Plasmidsaurus QC pipeline (§05, canonical pricing table added 2026-05-17) and the MinION genome protocol both address the same verification question ("does the DNA say what I designed?") but via different instruments and at different cost points.
   - *Why It Matters:* `engineered-koji-protocol.md` §05 now states the same MinION + Dorado + Flye/Clair3 pipeline for strain genome verification is already specified in `personal-genome-protocol.md` for personal pharmacogenomics. The pipeline pages note this dual-use property ("One amortized hardware investment, two outputs"), but the Plasmidsaurus section doesn't map which QC questions are better answered by which platform under which cost structure. Specifically: (a) Plasmidsaurus wins on pre-transformation plasmid verification ($15, next-day) — no MinION equivalent at that price point; (b) Plasmidsaurus wins on transformant clone screening via Genotyping Analysis ($30, 1-2 days) — MinION would need a full library prep per clone; (c) MinION wins on cost-per-genome at N > 12 strains (flow cell can multiplex ~12-24 microbial genomes per run); (d) Plasmidsaurus wins on turnaround for plasmid + amplicon reads. The two platforms are complementary, not competing — each answers a different subset of the same "DNA verification" question at a different cost-time tradeoff. This is a **platform infrastructure design pattern** — not a research finding, but a load-bearing operational insight for anyone building Phase 1+ strain pipelines.
   - *Suggested Action:* Add a "Plasmidsaurus vs. MinION — per-question platform selection" table to `engineered-koji-protocol.md` §05, cross-referencing `personal-genome-protocol.md` for the MinION buildout. The table maps each QC question (plasmid verification, junction PCR, transformant screening, final genome release) to the preferred platform with cost and turnaround.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The dual-platform verification pattern is supported: `engineered-koji-protocol.md` now has the Plasmidsaurus table for whole plasmid sequencing ($15), amplicon sequencing ($15), genotyping analysis ($30), and *A. oryzae* WGS ($250 + extraction), and it explicitly compares this outsourced Phase 0 default against the `personal-genome-protocol.md` MinION/Dorado/Flye/Clair3 buildout. The suggested per-question selection table is an incremental operational refinement because the current protocol already gives the ingredients but does not present a single "which tool for which QC question" decision matrix.

---

**WALKED 2026-05-19 — Closed (per-question platform selection matrix added to engineered-koji-protocol.md §05).**

Actioned:
- ✓ Added "Per-question platform selection — Plasmidsaurus vs MinION decision matrix" subsection to `engineered-koji-protocol.md` §05 (after the existing in-house MinION cost-note paragraph, before "How Much Uricase Per Gram of Koji?"). Maps 6 QC questions (pre-transformation plasmid verification, junction PCR amplicon, transformant clone screening, multi-strain WGS, final genome release, personal-genome dual-use) to preferred platform with cost + turnaround + reasoning.
- ✓ Operational pattern encoded: Phase 0 (N=1-5/year) all-outsource Plasmidsaurus; Phase 1+ (N≥12/year OR contributor donates MinION time) hybrid pattern; dual-use unlock when MinION buildout exists for personal-genome use.
- ✓ Cross-references to `personal-genome-protocol.md` (Tier 5 MinION buildout) + `validation-experiments.md` §1.9/1.10/1.25 (per-experiment Plasmidsaurus adds) + `etc/open-source-platform.md` (platform-infrastructure-sharing pattern).

This is the same architectural-surfacing pattern as B3 (closed-loop pharmacogenomics pipeline naming) and other clusters that turned implicit decision criteria into explicit decision matrices.
