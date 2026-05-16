---
type: priority-action
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 3
global_index: 15
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Resolve the PDB butyrate concentration gap (Contradiction 2) by adding a butyrate dose-response arm to the existing `validation-experiments.md` §1.14 Caco-2 ABCG2 assay.

3. **Resolve the PDB butyrate concentration gap (Contradiction 2) by adding a butyrate dose-response arm to the existing `validation-experiments.md` §1.14 Caco-2 ABCG2 assay.** The §1.14 assay already includes a butyrate rescue arm at a single concentration (1 mM); extending it to a 5-point dose-response (0.1–10 mM) with Q141K-transfected cells directly tests the quantitative assumption underlying `purine-degrading-bacteria.md`'s "natural genotype-targeted therapy" framing. Marginal cost: ~$500–1,000. This is the cheapest experiment that can anchor the PDB mechanism to physiologically relevant concentrations.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The butyrate dose-response arm is the cheapest decisive way to resolve the PDB/Q141K concentration gap. `validation-experiments.md` §1.14 already gives the Caco-2 infrastructure and a 1 mM butyrate rescue arm; extending to 0.1, 0.5, 1, 5, and 10 mM directly tests whether physiologically plausible colonic exposure can rescue Q141K trafficking and urate efflux.

---

## ✓ Actioned 2026-05-16 — via Item 12 (Contradiction 2) closure

Same wet-lab addition as Items 12 and 14; closed together via the §1.14 dose-response arm. Concentrations finalized at 0.05, 0.2, 1, 2, 5 mM (lower bound shifted down to 0.05 mM to bracket crypt-base concentrations after mucus-layer + epithelial-surface gradient drop). Dual readouts (ABCG2 surface trafficking + urate efflux) in both WT and Q141K-transfected cells per Pass 3 tightening. Full detail in Item 12 closure annotation at [`synthesis/done/2026-05-15-contradiction-2-purine-degrading-bacteria-md-frames-pdb-derived-butyrate-as.md`](./2026-05-15-contradiction-2-purine-degrading-bacteria-md-frames-pdb-derived-butyrate-as.md).
