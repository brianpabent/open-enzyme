---
type: riskiest-assumption
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 1
global_index: 12
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# The single load-bearing belief in the current platform thesis that is least supported by the corpus is that home-fermented engineered koji can reliably deliver therapeutic doses of multiple heterologous proteins with batch-to-batch consistency sufficient for a chronic disease intervention.

The single load-bearing belief in the current platform thesis that is least supported by the corpus is **that home-fermented engineered koji can reliably deliver therapeutic doses of multiple heterologous proteins with batch-to-batch consistency sufficient for a chronic disease intervention.** The `open-source-platform.md` §“Open Questions — Reliability of Community Fermentation” explicitly flags strain stability across generations, reproducibility across users, and contamination as unresolved risks, with mitigations described as “engineering sketches, not SOPs.” The `ginkgo-cloud-lab-evaluation.md` reinforces the gap: even a commercial cloud lab optimized for microtiter-plate screening cannot answer the question “does this construct secrete from a fungal host in a real solid-state fermentation context?” — that question requires a community-college or academic collaborator running actual koji trays. The `cross-validation.md` rates home production feasibility at 3/10 as originally stated and 6/10 under the reframed “Community BioLab + Home Fermentation” model, but even the reframed model has not been tested with an engineered strain. The platform’s entire accessibility thesis — “grow it at home like sourdough” — rests on this assumption, and the corpus currently offers no direct evidence that it holds for a multi-cassette engineered *A. oryzae* strain. The Ward 1995 §1.9 dual-cassette feasibility test is the first experimental gate that begins to address it, but even a positive §1.9 result only validates expression in a controlled lab setting, not home-fermentation reliability. (Anchor: `open-source-platform.md` §“Open Questions — Reliability of Community Fermentation”; `ginkgo-cloud-lab-evaluation.md` §“Where this fits the OE wet-lab plan”; `cross-validation.md` Claim 5.)

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` The central risk is correct — `open-source-platform.md` explicitly says home/community fermentation has unresolved strain-stability, reproducibility, contamination, and regulatory problems, and calls the mitigations "engineering sketches, not SOPs"; `ginkgo-cloud-lab-evaluation.md` also says the $39 cell-free gate cannot answer fungal secretion or real fermentation-context behavior. But the synthesis overclaims its support: I read `cross-validation.md` and could not find the cited 3/10 vs. 6/10 home-production feasibility ratings or a "Claim 5" anchor, and the cited `wiki/ward-1995-lab-access.md` path is wrong in this repo (`operations/ward-1995-lab-access.md` exists). Keep the riskiest-assumption conclusion, but remove or repair those specific citations before emitting it as a queue item.

---

## ✓ Actioned 2026-05-15

Pass 3 was partially right (one citation path was wrong) and partially wrong (the cross-validation.md Claim 5 + 3/10/6/10 ratings DO exist — I verified directly):

- ✓ `cross-validation.md` line 319 has `### Claim 5: "As Easy as Sourdough" — Home Production`
- ✓ Line 365 has the **3/10 → 6/10 reframe** ("Entirely Home-Based" → "Community BioLab + Home Fermentation")
- ✓ Line 377 in the cross-validation summary table: Home Production rated **3/10** with mitigation "Pivot to hybrid model"
- ✗ Pass 3 was right that `ward-1995-lab-access.md` is at `operations/`, not `wiki/` — Pass 2's path was wrong; corrected in the H09 cross-references below.

The substantive riskiest-assumption claim was well-grounded.

**Committed H09 — Community Fermentation Reliability** as a stub-level falsification card to register the platform's #2 load-bearing scientific bet (production/delivery side, paired with H08 on the mechanism side). Mirror of the H08 pattern shipped earlier in this walk (Item 2). Together H08 + H09 give a complete picture of the platform's two load-bearing risks — both must survive for the accessibility thesis to hold.

**Files shipped:**

- **`wiki/hypotheses/H09-community-fermentation-reliability.md`** — new stub. Pre-commits the magnitude band (CV < 30% cross-user / strain retention ≥ 95% at gen 5 / contamination < 5% per batch / drying activity retention ≥ 80% / smartphone-colorimetric QC feasible) as the alive/killed threshold anchor. Provisional killshot menu: industrial-koji lit scan, multi-user community-fermentation pilot, 50-passage strain stability test, drying-method activity-retention comparison, contamination-spike test, smartphone colorimetric assay validation, regulatory framework scoping pass. Cross-references corrected on `ward-1995-lab-access.md` path (now at `operations/`, not `wiki/`).
- **`wiki/hypotheses/README.md`** — H09 row added to the Current Hypotheses table; H08's row updated to clarify "#1 riskiest assumption (mechanism)" framing now that H09 is the "#2 (production/delivery)" sister.
- **`wiki/cross-validation.md` §Claim 5 verdict** — appended H09 falsification-card pointer; existing 3/10 → 6/10 framing preserved.
- **`wiki/open-source-platform.md` §"Open Questions — Reliability of Community Fermentation"** — H09 callout added directly under the section heading, with read-H09-before-extending-strong-claims guidance.
- **`index.md`** — Riskiest-assumption anchor extended from one (H08-only) to two (H08 + H09). Both H-cards now surfaced from the dashboard with their distinct mechanism-vs-production framing.
- **`wiki/open-questions.md` §Platform/Strategic** — new "Riskiest assumption #2" section added above the existing H08 section (now renamed "Riskiest assumption #1"); mirrors the H09 Phase 2 follow-up table.

**Six-surface tracking (per walk-synthesis skill §5):**
1. H09 page's own Open Follow-Ups (P2-1 through P2-11)
2. `wiki/open-questions.md` §Platform/Strategic — new "Riskiest assumption #2" entry
3. `wiki/computational-experiments.md` — no comp-NNN assigned for H09 follow-ups (production reliability is primarily wet-lab + behavioral, not in-silico)
4. H09 itself = the falsification card
5. `index.md` — two-anchor riskiest-assumption surface
6. This closure annotation + the queue→done move

**Phase 3 reflection (content-triggered):** the existing `synthesis/strategic-reflections/platform-framing-reframe.md` covers the broader "OE is the mission, not the koji chassis" framing — which intersects with H09 if the community-fermentation reliability question reshapes the platform's positioning (e.g., if H09 dies and OE pivots to centralized manufacturing, the multi-track framing strengthens; if H09 holds, the open-source-accessibility framing strengthens). No new strategic-reflection file needed yet — H09's Phase 2 results will inform the existing reflection.

Pass 3's "Push back" verdict was procedurally right (citation path fix needed) and substantively conservative (the riskiest-assumption conclusion should ship, not be re-questioned). Both honored in this closure.
