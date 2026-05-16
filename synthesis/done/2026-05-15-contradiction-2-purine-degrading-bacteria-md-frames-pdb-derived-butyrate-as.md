---
type: contradiction
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 2
global_index: 6
pass3_verdict: Augment
overlap_tag: EXTENSION
---

# `purine-degrading-bacteria.md` frames PDB-derived butyrate as a "natural genotype-targeted therapy" for Q141K via HDAC inhibition, while `abcg2-modulators.md` §6 frames butyrate's Q141K rescue as an orthogonal mechanism to the androgen question, but neither page addresses the quantitative question of whether *endogenous* PDB-derived butyrate concentrations in the colonic crypt reach the HDAC-inhibition threshold documented in Basseville 2012 (1 mM in vitro).

2. **`purine-degrading-bacteria.md` frames PDB-derived butyrate as a "natural genotype-targeted therapy" for Q141K via HDAC inhibition, while `abcg2-modulators.md` §6 frames butyrate's Q141K rescue as an orthogonal mechanism to the androgen question, but neither page addresses the quantitative question of whether *endogenous* PDB-derived butyrate concentrations in the colonic crypt reach the HDAC-inhibition threshold documented in Basseville 2012 (1 mM in vitro).** *Locations:* `purine-degrading-bacteria.md` §"Q141K + PDB-butyrate + HDAC: a natural genotype-targeted therapy" and `abcg2-modulators.md` §6 "The Q141K rescue mechanism — a separate axis." *Analysis:* Both pages cite Basseville 2012 (PMID 22472121) for the mechanism and Li 2023 (PMID 36948133) for butyrate's in vivo ABCG2 restoration, but neither addresses the concentration gap. Basseville 2012 used 1–5 mM butyrate in cell culture; physiological colonic butyrate concentrations in humans on a high-fiber diet are ~5–20 mM in the lumen but drop steeply across the mucus layer and epithelial surface, with crypt-base concentrations potentially an order of magnitude lower. Whether endogenous PDB flux can achieve HDAC-inhibitory concentrations at the enterocyte nucleus — where HDAC1/2/3 reside — is unresolved. The "natural genotype-targeted therapy" framing in `purine-degrading-bacteria.md` is mechanistically elegant but quantitatively unanchored. This is not a contradiction between pages — it's a shared blind spot. *Suggested resolution:* Add a "Concentration gap" subsection to `purine-degrading-bacteria.md` §"Q141K + PDB-butyrate + HDAC" that explicitly names the in vitro vs. in vivo concentration uncertainty and proposes a Caco-2 transwell experiment (butyrate dose-response at the basolateral side, measuring ABCG2 surface expression in Q141K-transfected cells) to determine the minimum colonic butyrate concentration needed for HDAC-mediated trafficking rescue. Cross-reference the existing `validation-experiments.md` §1.14 (Caco-2 ABCG2 suppression/rescue assay) which could accommodate a butyrate dose-response arm at marginal cost.

> **Pass 3 review — Augment.** `[OVERLAP: EXTENSION]` The concentration-gap critique is valid: `purine-degrading-bacteria.md` strongly frames PDB-butyrate as Q141K-targeted rescue, while the page does not currently quantify whether endogenous colonic/crypt butyrate reaches the HDAC-rescue range established in the ABCG2 Q141K literature. Tighten the proposed experiment around the specific mechanism: wild-type butyrate induction is PPARγ-mediated per `abcg2-modulators.md`, whereas Q141K rescue is HDAC-mediated, so the dose-response should measure both ABCG2 surface trafficking and urate efflux in Q141K cells.

---

## ✓ Actioned 2026-05-16

Pass 3 tightening (dual readouts in Q141K-vs-WT) baked into the wet-lab arm. Three edits, closing Items 12 + 14 + 22 together:

- [`wiki/purine-degrading-bacteria.md`](../../wiki/purine-degrading-bacteria.md) — added "#### Concentration gap" subsection inside §"Q141K + PDB-butyrate + HDAC" naming the in vitro vs in vivo concentration uncertainty explicitly (Basseville 2012 1–5 mM in cell culture vs ~5–20 mM luminal but order-of-magnitude lower at crypt base / enterocyte nucleus where HDAC1/2/3 act). Frames the PDB-butyrate-Q141K stack as "mechanistically supported but quantitatively unverified" until dose-response runs.
- [`wiki/validation-experiments.md §1.14`](../../wiki/validation-experiments.md) — added "Butyrate dose-response arm — Q141K concentration-gap resolution" bullet to Treatment arms. Five concentrations (0.05, 0.2, 1, 2, 5 mM) basolateral, both WT and Q141K-transfected Caco-2 monolayers. Dual readouts (ABCG2 apical-membrane Western + transwell urate efflux) per Pass 3 tightening — disentangles WT PPARγ-mediated transcriptional induction from Q141K HDAC-mediated trafficking restoration. Marginal cost +$500–1,500; total §1.14 cost updated to $2,300–4,300. Affected-wiki list extended to include `purine-degrading-bacteria.md`.
- [`wiki/abcg2-modulators.md §6`](../../wiki/abcg2-modulators.md) "Q141K rescue mechanism" — added concentration-gap caveat paragraph cross-linking the purine-degrading-bacteria §"Concentration gap" and the §1.14 dose-response arm. Frames in vivo Q141K rescue magnitude as "mechanistically supported, quantitatively unverified" until dose-response runs.

Cluster-closure: Items 12 (this), 14 (Experiment 2 — same dose-response wet-lab work), 22 (Priority Action 3 — same wet-lab addition) all close together via the same edit set. Pointer maintained in each.
