---
type: open-question
sweep_date: 2026-05-14
sweep_sha: 81e6264
section_index: 1
global_index: 8
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# Can the quantification ladder’s Tier 2 assays (cordycepin, rosmarinic acid, ergothioneine) achieve the ±15% inter-operator reproducibility target required by H06 Dimension 2?

1. **Can the quantification ladder’s Tier 2 assays (cordycepin, rosmarinic acid, ergothioneine) achieve the ±15% inter-operator reproducibility target required by H06 Dimension 2?** The ladder framework is specified but no multi-operator validation has been performed. Without reproducibility data, the “calibrate once, track batches cheap” operational pattern remains unproven for the medicinal-mushroom track. (context: `quantification-ladder.md`, `medicinal-mushroom-extract-sops.md`, `hypotheses/H06-medicinal-mushroom-complement-track.md`)

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` The central factual framing is wrong: H06 Dimension 2 does **not** require Tier 2 cordycepin/rosmarinic-acid/ergothioneine assays to hit ±15% inter-operator reproducibility. `hypotheses/H06-medicinal-mushroom-complement-track.md` Dimension 2 specifies ±15% for Open Enzyme HPLC/MS characterization protocols on mushroom-track targets, and `quantification-ladder.md` / `medicinal-mushroom-extract-sops.md` use Tier 2 for cheaper batch tracking against a Tier 3 anchor, with a ±20% accept/escalate pattern; rosmarinic acid is also not an H06 medicinal-mushroom target. The useful open question is narrower: can Tier 2 assays stay within a pre-registered tracking tolerance after Tier 3 calibration, and for cordycepin specifically does any validated colorimetric method exist at all?

---

## ✓ Actioned 2026-05-15

Pass 3 caught three factual errors in Pass 2's framing:

1. H06 Dimension 2 specifies ±15% for **Tier 3 HPLC/MS protocols**, not Tier 2 batch-tracking
2. The actual Tier 2 tolerance per `quantification-ladder.md` + `medicinal-mushroom-extract-sops.md` is **±20% accept/escalate**, not ±15%
3. **Rosmarinic acid is not an H06 medicinal-mushroom target** — it's a TCM / CP0-dietary compound; Pass 2 conflated tracks

Two pieces of the corrected question are now in place across the wiki:

- **The cordycepin-validity arm** — "does any validated colorimetric method exist at all?" — is structurally answered by Item 22's [`validation-experiments.md` §1.28](../../wiki/validation-experiments.md) (shipped earlier in this walk, commit `8e7f87b`). GREEN/YELLOW/RED verdict from §1.28 resolves the cordycepin-specific arm.
- **The inter-operator reproducibility arm** — "can Tier 2 assays stay within ±20% across multiple operators after a shared Tier 3 calibration?" — surfaced in [`wiki/open-questions.md` §"Compound-Specific Questions"](../../wiki/open-questions.md) as a new "Quantification methodology — Tier 2 inter-operator reproducibility" subsection. Explicit "Fires when" trigger (≥3 independent operators in practice; structurally prerequisite for H09's CV < 30% cross-user batch claim). Applies to ergothioneine, GLPP, cordycepin (if §1.28 returns GREEN), and uricase activity. Resolution work scoped as a small multi-operator round-robin (~$500-1,000 + 4-6 weeks).

**No new comp-NNN / validation-experiments entry beyond §1.28** — the open question is methodological (multi-operator reproducibility) and fires only when there's an operator network to test, which is downstream of current Phase 0. Surfacing in `open-questions.md` with the explicit trigger is sufficient.

**No correction to H06 Dimension 2** — Pass 3 correctly noted H06's ±15% is for Tier 3 protocols and does NOT need updating to apply to Tier 2. The error was in Pass 2's reading; H06 itself is fine.

Pass 3's "Push back" verdict honored. Closing.
