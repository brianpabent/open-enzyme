---
type: open-question
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 2
global_index: 11
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# Is there a Tier 2 butyrate assay — colorimetric, enzymatic, or breath‑hydrogen proxy — that can be validated against Tier 3 GC‑MS to close the microbiome‑metabolite quantification gap?

2. **Is there a Tier 2 butyrate assay — colorimetric, enzymatic, or breath‑hydrogen proxy — that can be validated against Tier 3 GC‑MS to close the microbiome‑metabolite quantification gap?** Without it, every future microbiome‑derived intervention (engineered LBP butyrate‑boost, bile‑acid modulators, indole‑based AhR agonists) will face the same QC blind spot. A desk audit of existing assay literature is the $0 first step.  

   

---

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` The butyrate Tier 2 assay question is already named in `genotype-informed-supplement-workflow.md`, including the three candidate paths and the warning that stool SCFA is exposure proxy rather than direct potency measurement. The synthesis correctly elevates it as a quantification-ladder bottleneck rather than a Q141K-only inconvenience. A $0 desk audit before wet-lab development is the right next action.

---

## ✓ Actioned 2026-05-21 (answered by comp-038)

**The desk audit Pass 2 asked for already shipped as [comp-038](../../wiki/tier-2-butyrate-assay-audit-computational.md) on 2026-05-20.**

**Verdict: YELLOW.** No ready-to-adopt simple/home colorimetric or breath-based butyrate Tier 2 assay surfaced. Two plausible Tier 2-lab candidates require full-text protocol review + paired GC-MS validation before adoption:

| Candidate | Matrix fit | Verdict |
|---|---|---|
| HPLC-UV SCFA + lactate (PMID 23542733) | Culture supernatant / engineered-strain work | YELLOW — full text + OE spike-recovery required |
| Electrochemical fecal SCFA + ANN deconvolution (PMID 42041444) | Stool / fecal SCFA profiling | YELLOW — full-text butyrate-specific performance + external validation required |
| Butyric-acid / SCFA ELISA kits | Serum/plasma/vendor-claimed | RED-provisional — no PubMed/GC-MS validation; small-molecule specificity concern |
| Breath H₂/CH₄ | Breath | RED — broad fermentation proxy, not butyrate-specific |
| Generic free-fatty-acid colorimetric | Vendor-dependent | RED — representative FFA kit excludes SCFAs including butyric acid |

**Operational state:** GC-MS remains the Tier 3 anchor. HPLC-UV is the most plausible Tier 2-lab path for culture supernatants (engineered-strain / fermentation work). Stool/serum/home Tier 2 has no ready-to-adopt method.

**comp-038 Next Step (open follow-up, not actioned this walk):** Focused full-text/protocol verification pass on PMID 23542733 + PMID 42041444 + vendor protocol audit for SCFA ELISA claims. If one candidate survives, design a small paired validation with sodium-butyrate spike/recovery and 10–20 real samples measured by the candidate Tier 2 method + GC-MS in parallel.

The "structural gap" extension to other microbiome-derived metabolites (SCFAs, secondary bile acids, indoles, TMAO) was added to [`quantification-ladder.md`](../../wiki/quantification-ladder.md) line 46 in this walkthrough — see [Item 5 closure](./2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md).
