---
type: connection
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 2
global_index: 2
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# The PDB-butyrate → Q141K rescue concentration gap is not a contradiction — it's a well-scoped empirical question with a concrete wet-lab resolution path that re-frames from "uncertainty" to "testable prediction."

2. **The PDB-butyrate → Q141K rescue concentration gap is not a contradiction — it's a well-scoped empirical question with a concrete wet-lab resolution path that re-frames from "uncertainty" to "testable prediction."** *Supported*. `[REFRAME]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `purine-degrading-bacteria.md`, `abcg2-modulators.md`, `validation-experiments.md`, `chassis-pending-interventions.md`

   - *Page-pair linkage:* **Strong.** These pages already cross-reference each other heavily. The butyrate dual-action (PPARγ + HDAC) and the Basseville 2012 in vitro anchor are documented in all of them. The concentration-gap caveat was added to `abcg2-modulators.md` on 2026-05-16 and flagged as a contradiction (contradiction-2) in the 2026-05-15 sweep.

   - *Why It Matters:* The 2026-05-15 sweep framed this as a contradiction between the PDB-butyrate-Q141K mechanism story and the unresolved in vivo concentration question. That framing implies a problem with the thesis. The re-frame is: this is a **measurement-design question**, not a thesis flaw. The mechanism is coherent (Basseville 2012 shows Q141K rescue at 1–5 mM butyrate in vitro; PDB produce butyrate in the colon; the unknown is whether endogenous colonic butyrate concentrations at the enterocyte nucleus reach the HDAC-inhibitory threshold). This is a tractable wet-lab question: Caco-2 transwell, butyrate applied basolaterally at five concentrations (0.05–5 mM), in both WT and Q141K-transfected cells, with dual readouts (ABCG2 surface expression + functional urate efflux). The §1.14 butyrate dose-response arm — added 2026-05-16 during the walkthrough that closed contradiction-2 — is exactly this experiment.

     The re-frame has operational consequences: it converts the gap from a "risk to the PDB thesis" into a "gate that decides how strongly the PDB thesis should be asserted," and it surfaces that the §1.14 arm's dual readout (WT PPARγ induction vs Q141K HDAC rescue) is non-optional — measuring only ABCG2 expression conflates two different mechanisms with different dose-response shapes.

   - *Suggested Action:* No new action — the §1.14 butyrate dose-response arm already added on 2026-05-16 directly resolves this. The re-frame changes how the corpus *describes* the gap: move from "concentration gap — contradiction" language to "concentration-gap — testable prediction with a defined wet-lab resolution path" in `purine-degrading-bacteria.md` §"Concentration gap" and `abcg2-modulators.md` §6. The dual-readout discipline (WT PPARγ vs Q141K HDAC) should propagate to both pages when the butyrate dose-response arm is described.

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` The reframe is correct, but it is now already first-class in the corpus: `purine-degrading-bacteria.md` names the “Concentration gap,” cites Basseville 2012’s 1–5 mM butyrate rescue anchor, and points to `validation-experiments.md` §1.14 with WT/Q141K dual readouts to disentangle PPARγ induction from HDAC-mediated trafficking rescue. `abcg2-modulators.md` carries the same concentration-gap caveat and resolution path. The finding is therefore a valid restatement of the current wiki position rather than a new contradiction resolution.
