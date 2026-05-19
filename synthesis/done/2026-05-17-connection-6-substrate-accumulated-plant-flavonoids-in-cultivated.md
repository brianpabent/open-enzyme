---
type: connection
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 6
global_index: 6
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Substrate-accumulated plant flavonoids in cultivated mushrooms create a "substrate engineering" quality-control axis for the medicinal-mushroom-complement track that is mechanistically distinct from "strain engineering" — and currently unaddressed by the extract characterization SOPs.

6. **Substrate-accumulated plant flavonoids in cultivated mushrooms create a "substrate engineering" quality-control axis for the medicinal-mushroom-complement track that is mechanistically distinct from "strain engineering" — and currently unaddressed by the extract characterization SOPs.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `medicinal-mushroom-compound-mapping-computational.md` (Phase 3), `medicinal-mushroom-complement-track.md`, `medicinal-mushroom-extract-sops.md`
   - *Page-pair linkage:* The Phase 3 target mapping found multi-chokepoint compounds — morin (4 chokepoints: ABCG2, CASP1, URAT1, XO), genistein (4: ABCG2, CASP1, PPARG, XO), quercetin (2: ABCG2, XO), daidzein (2: NRF2, XO) — all annotated as "plant-origin flavonoids that accumulate in mushroom substrates rather than being biosynthesized by the fungi." The medicinal-mushroom-extract-sops.md SOP-6 tiered framework treats compound quantification as a per-compound analytical question without distinguishing biosynthesized vs. substrate-accumulated origin. The medicinal-mushroom-complement-track.md cultivation SOPs focus on strain selection + growth conditions, not substrate flavonoid content. This is a quality-control blind spot.
   - *Why It Matters:* If a mushroom's quercetin content comes from its substrate (e.g., oak sawdust containing quercetin from the wood) rather than from its own biosynthesis, then substrate lot variation — not strain genetics — is the dominant source of batch-to-batch compound variability. The current SOP framework (SOP-6 Tier 2 colorimetry) would detect a shifted quercetin batch but wouldn't distinguish "strain drift" from "substrate lot change" as the root cause. For the H06 falsification-card Dimension 2 (characterization protocol robustness, ±15% inter-operator), substrate source needs to be a documented variable, not an invisible confound. This is a tractable methodological refinement: add "document substrate source + lot" to the cultivation data sheet and flag plant-flavonoid-accumulating compounds as substrate-sensitive in the per-compound SOP entries.
   - *Suggested Action:* Add a "Substrate-accumulated vs. biosynthesized" annotation column to the medicinal-mushroom-extract-sops.md SOP-6 tier table. For quercetin, genistein, daidzein, morin entries: note "substrate-accumulated — substrate lot documentation required for batch QC." Add "substrate source + lot" as a required field in the cultivation data sheet (analogous to the "extract source, batch ID, lot" fields already in SOP-6's operational pattern). No new assay needed — this is documentation discipline, not analytical chemistry.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` comp-014 Phase 3 explicitly flags quercetin, genistein, daidzein, and morin as plant-origin flavonoids attributed to fungi through substrate accumulation rather than fungal biosynthesis, and `medicinal-mushroom-extract-sops.md` currently treats SOP-6 quantification as compound-specific without a substrate-origin field. The QC implication follows: if the analyte is substrate-accumulated, substrate lot and source can dominate batch variance even when the fungal strain is unchanged. Add the annotation column and substrate-lot field; this is low-cost documentation discipline with real falsification-card relevance.

---

**WALKED 2026-05-19 — Closed (substrate-origin discipline encoded + platform-level question elevated to first-principles investigation).**

**Brian's 2026-05-19 walkthrough reframe** flipped this from a documentation-QC problem to a first-principles question worth investigating: *if we're growing something, can we get more or better compounds by changing the substrate?* The daemon stopped at "substrate is a confound to document"; Brian's framing names the inverse — substrate as a deliberate engineering lever. This was the noteworthy insight of the walkthrough.

Actioned:
- ✓ Added "Substrate-accumulated vs biosynthesized — origin-of-compound discipline" subsection to `medicinal-mushroom-extract-sops.md` (after SOP-6). Documents the origin distinction per-compound (cordycepin/EGT/GLPP/kojic acid biosynthesized vs quercetin/genistein/daidzein/morin substrate-accumulated), QC implications, and required cultivation-data-sheet fields (substrate species/source/lot/composition).
- ✓ Added new "Open Questions — Substrate as Engineering Lever (queued 2026-05-19)" section to `etc/open-source-platform.md`. Documents the four production mechanisms substrate engineering can exploit (passive accumulation, biotransformation, substrate induction of silent BGCs, precursor feeding), why this is platform-level (universal to mushroom/koji/future LBP tracks), and the elevation-to-named-principle decision gate (≥2× yield effects OR new-compound-class effects in ≥2 candidate species).
- 🔄 Substrate-engineering lit-scan subagent firing in background. Targets: cordycepin × substrate, ganoderic acid × substrate, ergothioneine × substrate sulfur/methionine, lentinan × substrate, hericenones × substrate, PSK/PSP × substrate, Penicillium metabolites × cheese substrate. Multilingual scope (J-STAGE, CNKI). Output → `logs/substrate-engineering-mushroom-cultivation-lit-scan-2026-05-19.md`.

The documentation discipline (per Pass 3) is the prerequisite QC anchor for any substrate-engineering experiment. Both directions are now active: substrate-as-documentation discipline encoded in the SOP page; substrate-as-engineering-lever queued for investigation in the platform page.

Also closes:
- 2026-05-17 priority-action-3 (Add substrate-accumulated vs biosynthesized annotation to SOP-6).
