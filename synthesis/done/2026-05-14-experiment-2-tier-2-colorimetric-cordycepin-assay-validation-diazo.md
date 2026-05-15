---
type: experiment
sweep_date: 2026-05-14
sweep_sha: 81e6264
section_index: 2
global_index: 7
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Tier 2 colorimetric cordycepin assay validation (diazo-coupling or alternative).

2. **Tier 2 colorimetric cordycepin assay validation (diazo-coupling or alternative).** Cost: ~$200 (reagents + reference standard). Time: 2 weeks. Decides: whether the speculative diazo-coupling assay proposed in `medicinal-mushroom-extract-sops.md` SOP-6 is viable, or whether an alternative (UV 260 nm) must be used. This is the gating experiment for home quantification of cordycepin, which is load-bearing for the genotype-informed n=1 workflow (Connection 2).

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is actionable and correctly grounded: `medicinal-mushroom-extract-sops.md` SOP-6 explicitly marks cordycepin Tier 2 diazo-coupling as speculative and says not to commit until primary-literature confirmation, with UV 260 nm as the fallback. A cheap validation against a cordycepin reference standard is therefore the right next gate before any home-quantification workflow depends on Tier 2 cordycepin numbers.

---

## ✓ Actioned 2026-05-15

**Files shipped:**

- **`wiki/validation-experiments.md` §1.28 (new)** — "Tier 2 Colorimetric Cordycepin Assay Validation." Two-arm protocol (diazo-coupling per SOP-6 vs. UV 260 nm fallback), Tier 3 anchor cross-validation via HPLC-UV ($150 of the $200 budget), explicit adenosine cross-reactivity specificity check at 100 µg/mL (the most likely failure mode given crude *Cordyceps* extracts are orders-of-magnitude more adenosine than cordycepin by mass). GREEN/YELLOW/RED decision rule with concrete numeric thresholds (R² ≥ 0.98, LoD ≤ 2 µg/mL, < 20% adenosine cross-reactivity, ≤ 20% Tier 2-vs-Tier 3 disagreement). RED → fallback to UV 260 nm + downgrade diazo to "experimental." Pre-execution literature-check note included per `Open Enzyme/CLAUDE.md` §"Global-multilingual research by default" (PubMed + CNKI + J-STAGE before running).

- **`wiki/medicinal-mushroom-extract-sops.md` SOP-6 cordycepin row** — extended the Tier 2 cell with explicit cross-link to `validation-experiments.md` §1.28 noting that the GREEN verdict promotes the SOP entry from Speculative to Validated. Preserves the existing "do NOT commit until primary-literature confirmation" caveat; surfaces the experiment that produces that confirmation.

**Cross-linkage already in place via §1.28's own cross-references:**
- `quantification-ladder.md` (Tier-2 framework anchor)
- `self-experiment-protocol.md` §12 (genotype-informed-supplement-quantification workflow — Item 17 — depends on Tier 2 cordycepin)
- `cordycepin-cassette-burden-computational.md` (comp-023 engineering thread)
- `medicinal-mushroom-complement-track.md` (cordycepin-bearing co-products including the Item 19 cross-chassis pairing)
- §2.7 (sister Tier 2 assay — the ADA-challenge stability test from Item 19 shares Tier-2 home-assay infrastructure with §1.28)

**Six-surface tracking:**
1. `wiki/validation-experiments.md` §1.28 (canonical wet-lab home)
2. `wiki/medicinal-mushroom-extract-sops.md` SOP-6 cordycepin row (the SOP this validates)
3. `wiki/quantification-ladder.md` (Tier-2 framework — already references SOP-6; §1.28 inherits via SOP-6 link)
4. `wiki/self-experiment-protocol.md` §12 (the workflow this gates — bidirectional link present)
5. `wiki/cordycepin-cassette-burden-computational.md` (engineering thread — already cross-linked via Item 19's edits)
6. This closure annotation + queue→done move

Pass 3 verdict honored. Closing.
