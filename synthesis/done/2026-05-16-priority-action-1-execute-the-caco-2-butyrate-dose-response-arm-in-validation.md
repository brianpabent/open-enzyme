---
type: priority-action
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 1
global_index: 14
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# Execute the Caco-2 butyrate dose-response arm in `validation-experiments.md` §1.14.

1. **Execute the Caco-2 butyrate dose-response arm in `validation-experiments.md` §1.14.** This is the single experiment that gates the endogenous-PDB-butyrate-Q141K triple-mechanism thesis. It was added to §1.14 on 2026-05-16 with explicit dual readouts (ABCG2 surface expression + functional urate efflux) and a 5-concentration range bracketing 0.05–5 mM. It resolves the concentration-gap question that `purine-degrading-bacteria.md` names as open. Cost ~$500–1,500 as an add-on to the existing §1.14 factorial. No new infrastructure required. This should be the highest-priority wet-lab spend in the current queue.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` This is the same correct wet-lab priority as above and is already encoded in `validation-experiments.md` §1.14. The value is practical: the 0.05–5 mM dose-response with trafficking plus urate-efflux readouts is the single cheapest experiment that separates “endogenous PDB/fiber is enough” from “engineered butyrate-producing LBP is required.”

---

**WALKED 2026-05-19 — Closed (already specified in §1.14; awaits wet-lab budget).**

Actioned:
- ✓ Verified `validation-experiments.md` §1.14 already fully specifies the Caco-2 butyrate dose-response: WT + Q141K, 0.05/0.2/1/2/5 mM butyrate, dual readout (ABCG2 apical-membrane expression + functional urate efflux). No wiki work needed at synthesis-walkthrough layer.
- ✓ Verified `purine-degrading-bacteria.md` line 221 already carries the canonical thesis framing (“endogenous gut bacteria producing the molecule that fixes their genetic variant... genotype-targeted gene-trafficking rescue for the #1 gout GWAS variant”). No tagline extraction needed — the wiki's framing is more precise than the daemon's “gene-therapy-by-microbiome” coinage.
- ✓ Status: experiment fully specified; gates on wet-lab budget allocation (~$500–1,500 add-on to §1.14 factorial). Tracked in §1.14 prioritization, not in the synthesis queue.

Canonical entry for the 5-item Q141K-butyrate-§1.14 duplicate cluster (Cluster A1 in the 2026-05-19 walkthrough). Also closes:
- 2026-05-16 connection-1 (PDB-butyrate-Q141K triple-mechanism stack — Pass 3 already pushed back on the novelty claim)
- 2026-05-16 connection-2 (concentration-gap reframe — Pass 3 already confirmed the reframe is in the wiki)
- 2026-05-16 experiment-1 (Caco-2 dose-response — same experiment, restated)
- 2026-05-16 most-curious-thread-1 (PDB-butyrate-Q141K — restatement, all 139 sourced wiki pages already cited)

5-item duplicate density traced to Pass 2's deliberate “bias toward inclusion” + Pass 3 under-deduping in practice. Flagged for end-of-session daemon-prompt-tightening pass.
