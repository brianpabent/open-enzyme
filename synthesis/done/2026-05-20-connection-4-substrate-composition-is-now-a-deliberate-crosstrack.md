---
type: connection
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 4
global_index: 4
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# Substrate composition is now a deliberate, cross‑track engineering variable — it modulates cordycepin:pentostatin ratios in *Cordyceps militaris*, ergothioneine yields in *Pleurotus* and koji, and the protease environment affecting heterologous protein stability in solid‑state fermentation — yet no platform‑level document treats substrate as a unified engineering lever across tracks.

4. **Substrate composition is now a deliberate, cross‑track engineering variable — it modulates cordycepin:pentostatin ratios in *Cordyceps militaris*, ergothioneine yields in *Pleurotus* and koji, and the protease environment affecting heterologous protein stability in solid‑state fermentation — yet no platform‑level document treats substrate as a unified engineering lever across tracks.**  
   *Supported (by the substrate‑engineering lit scan and SOP‑7).* `[CHAIN-DEPTH: 2]` `[REFRAME]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `medicinal-mushroom-complement-track.md` (substrate‑engineering findings, Platform Principle 9), `medicinal-mushroom-extract-sops.md` (SOP‑7 protocol matrix), `koji-home-fermentation.md` (substrate discussion, methionine supplementation for ergothioneine), `engineered-koji-protocol.md` (substrate effects on native metabolite profile), `validation-experiments.md` §1.29 (cordycepin‑×‑substrate‑matrix experiment).  
   - *Page‑pair linkage:* **Weak across tracks.** `medicinal-mushroom‑complement‑track.md` treats substrate engineering as a cultivation‑track lever; `koji‑home‑fermentation.md` discusses rice bran vs white rice yield but does not frame it as an *engineering* variable. The substrate‑engineering lit scan that produced SOP‑7 explicitly cross‑applied the mechanisms to *A. oryzae* (methionine → ergothioneine via Lee 2009, carbon‑source modulation of secondary metabolites), but this cross‑track implication is stated only in the scan log, not in a permanent wiki page.  
   - *Why It Matters:* Substrate engineering is the **lightest‑effort, highest‑leverage lever** in the platform — every reagent in SOP‑7 is GRAS food‑grade, available at consumer retail, and requires no genetic modification. Yet the platform currently treats substrate as a “documentation discipline” (batch‑QC context) rather than an “engineering discipline” (deliberate yield‑optimisation and compound‑profile tuning). Elevating substrate to a named cross‑track engineering principle would give every distributed contributor a lever they can pull without a lab, and would connect the koji and mushroom tracks at a practical operations layer.  
   - *Suggested Action:* Codify “Substrate composition as a cross‑track engineering variable” as a permanent section in `etc/open-source-platform.md` (promote Platform Principle 9 from the scope page to the platform‑principles document). Cross‑link the SOP‑7 protocol matrix, the methionine‑for‑ergothioneine finding, and the cordycepin‑×‑pentostatin‑ratio experiment as canonical examples.

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The claim that “no platform-level document treats substrate as a unified engineering lever” is wrong. Tool-verified `etc/open-source-platform.md` already contains Platform Principle 9, “Substrate Engineering as a First-Class Engineering Variable,” and `medicinal-mushroom-extract-sops.md` already has SOP-7 with the substrate-intervention matrix; `koji-home-fermentation.md` also cross-applies the substrate-engineering mechanisms to *A. oryzae*. The underlying substrate-engineering thesis is correct, but the proposed codification has already happened.

---

## ✓ Actioned 2026-05-21 (closure note)

Already canonical in [`wiki/etc/open-source-platform.md`](../../wiki/etc/open-source-platform.md) §"9. Substrate Engineering as a First-Class Engineering Variable (added 2026-05-19, promoted from queued open question)" (line 210). Three intervention classes documented with primary-literature effect sizes: precursor feeding (Lee 2009 methionine → 1.7–3.1× ergothioneine PMC3749454, Yu 2024 alanine → 3× cordycepin PMC11698586, Lou 2021 oleic acid → 8.57× betulinic acid PMC8066064), BGC induction signals (Hu 2017 microcrystalline cellulose 1.5% → +85.96% ganoderic acids PMC5395960, D-galactose), and biotransformation.

Cross-link hygiene already in place: [`medicinal-mushroom-extract-sops.md`](../../wiki/medicinal-mushroom-extract-sops.md) §SOP-7 (line 147) cross-links to Platform Principle 9; [`koji-home-fermentation.md`](../../wiki/koji-home-fermentation.md) (line 64) cross-applies the substrate-engineering mechanisms to *A. oryzae* and cross-links to Platform Principle 9 + SOP-7. The cross-track lever framing Pass 2 wanted is the explicit framing of Platform Principle 9.

No new wiki work needed. Pass 2 misread the corpus state; the codification already happened during the 2026-05-19 sweep walkthrough.
