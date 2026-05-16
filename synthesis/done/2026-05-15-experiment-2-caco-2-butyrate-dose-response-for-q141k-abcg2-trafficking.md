---
type: experiment
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 2
global_index: 8
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Caco-2 butyrate dose-response for Q141K ABCG2 trafficking rescue at physiologically relevant concentrations.

2. **Caco-2 butyrate dose-response for Q141K ABCG2 trafficking rescue at physiologically relevant concentrations.** *Cost: $2,000–4,000. Time: 4–6 weeks. Decides:* Whether endogenous PDB-derived colonic butyrate concentrations (estimated 0.5–5 mM at the crypt base) are sufficient to rescue Q141K trafficking via HDAC inhibition, closing the concentration gap identified in Contradiction 2. Protocol: Caco-2 cells transfected with ABCG2-Q141K-GFP, treated with sodium butyrate at 0.1, 0.5, 1, 5, 10 mM basolaterally for 48h; measure surface ABCG2 expression by flow cytometry and urate efflux by transwell assay. This directly tests the load-bearing quantitative assumption in `purine-degrading-bacteria.md`'s "natural genotype-targeted therapy" framing.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the right cheap experiment: `validation-experiments.md` §1.14 already contains a single butyrate rescue arm at 1 mM, and the proposed 0.1–10 mM dose-response directly addresses the concentration uncertainty in the PDB/Q141K framing. The readouts should include Q141K surface ABCG2 and functional urate efflux, not just GFP localization, because `abcg2-modulators.md` separates trafficking rescue from transporter function.

---

## ✓ Actioned 2026-05-16 — via Item 12 (Contradiction 2) closure

Same wet-lab work as Items 12 and 22; closed together via the §1.14 dose-response arm addition. Concentrations 0.05, 0.2, 1, 2, 5 mM (close to the proposed 0.1–10 mM range; lower bound shifted down to 0.05 mM to better bracket crypt-base concentrations after the mucus-layer gradient drop; upper bound 5 mM matches Basseville 2012's in vitro ceiling). Dual readouts (Q141K surface ABCG2 Western + transwell urate efflux) per Pass 3 tightening. Marginal cost +$500–1,500 on §1.14. Full detail in Item 12 closure annotation at [`synthesis/done/2026-05-15-contradiction-2-purine-degrading-bacteria-md-frames-pdb-derived-butyrate-as.md`](./2026-05-15-contradiction-2-purine-degrading-bacteria-md-frames-pdb-derived-butyrate-as.md).
