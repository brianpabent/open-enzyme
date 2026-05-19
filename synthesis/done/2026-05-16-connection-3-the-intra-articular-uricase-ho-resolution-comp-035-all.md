---
type: connection
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 3
global_index: 3
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The intra-articular uricase H₂O₂ resolution (comp-035, all GREEN) surfaces a load-bearing architectural reframe: FRET-proximity is NOT the safety mechanism in Pickering emulsion IA uricase; bulk-phase catalase scavenging dominates all three architectures.

3. **The intra-articular uricase H₂O₂ resolution (comp-035, all GREEN) surfaces a load-bearing architectural reframe: FRET-proximity is NOT the safety mechanism in Pickering emulsion IA uricase; bulk-phase catalase scavenging dominates all three architectures.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `intra-articular-uricase-h2o2-reaction-diffusion-computational.md`, `chassis-pending-interventions.md`, `gout-kill-chain-delivery-routes.md`, `delivery-route-matrix.md`, `engineered-koji-protocol.md`

   - *Page-pair linkage:* **Weak.** `chassis-pending-interventions.md` §6 (IA uricase) was updated 2026-05-16 to reference comp-035, but the architectural reframe (FRET proximity ≠ safety mechanism) has not propagated to `gout-kill-chain-delivery-routes.md` or `delivery-route-matrix.md`, both of which describe the IA uricase route in qualitative terms without the Damköhler-number analysis comp-035 provides.

   - *Why It Matters:* comp-035's core finding — that the Damköhler number for the Pickering emulsion's 5 nm catalase shell is ~5 × 10⁻³ (far below 1, meaning the shell is too thin to scavenge H₂O₂ in transit), and that the escape fraction is ~0.998 — reframes what makes IA uricase safe. It is NOT the FRET-confirmed <10 nm proximity advertised by Liu 2025. It is **bulk-phase catalase scavenging** from catalase distributed across all dispersed droplets in the joint volume. The Pickering architecture is mathematically equivalent to free co-formulated catalase at the same total dose — the same outcome, a different reason.

     This reframe has direct chassis-selection implications. If proximity doesn't matter, then **catalase preparation quality + in vivo stability + proportional dosing** are the first-order chassis-selection variables across all three architectures (Pickering, fusion protein, free co-formulated). Catalase (kcat/Km) is the dominant load-bearing input across all architectures (Spearman r = −0.95 to −0.97). The fusion protein architecture has the most robust safety margin (both intramolecular Smoluchowski capture AND bulk scavenging contribute), but all three architectures are safe under reference dosing.

     The reframe also connects to the koji chassis thesis: koji's peroxisomal co-localization of uricase + catalase is solving at the cell-biology layer what IA delivery has to solve at the formulation-engineering layer. This isn't just "the chassis solves it for free" — it's that the chassis has an intrinsic advantage that scales across any oxidase payload the platform might add. The IA uricase math independently corroborates the chassis-as-formulation argument.

   - *Suggested Action:* Propagate the architectural reframe (Damköhler numbers + bulk-phase dominance) into `gout-kill-chain-delivery-routes.md` IA uricase row and `delivery-route-matrix.md` §"Open exploration questions" #1 (IA uricase + catalase). Update the IA uricase entry in `chassis-pending-interventions.md` §6 to reflect that chassis selection should be driven by production economics + regulatory pathway + in vivo retention + immunogenicity, NOT by advertised proximity claims. The cheapest wet-lab next step is Amplex Red microelectrode H₂O₂ measurement in synovial-fluid mimic with dispersed architecture + 0.5 mM urate substrate (~$2–5K per architecture) — this directly measures the predicted bulk-phase steady-state [H₂O₂] and resolves the absolute-magnitude uncertainty.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The architectural reframe is exactly what comp-035 says: Pickering Da_shell is ~4.55e-03 with escape fraction ~0.998, so FRET-confirmed <10 nm proximity is not the H₂O₂ safety mechanism; bulk catalase capacity dominates, and catalase kcat/Km is the top sensitivity driver for Pickering and fusion (r = −0.972 and −0.954 in the summary). This should change route-selection behavior: compare architectures by catalase preparation quality, stoichiometry, retention, immunogenicity, regulatory path, and manufacturing economics, not by advertised proximity claims. The suggested Amplex Red synovial-mimic handoff matches the comp-035 wet-lab recommendation.

---

**WALKED 2026-05-19 — Closed (Damköhler reframe was already propagated by the 2026-05-16 sweep; verified via grep across all three target pages).**

The daemon Pass 2's claim that "the architectural reframe... has not propagated to gout-kill-chain-delivery-routes.md or delivery-route-matrix.md" was based on a stale file state. 2026-05-19 walkthrough verification:

- ✓ `chassis-pending-interventions.md` §6 (line 194): full reframe present — Da_shell ~5×10⁻³, bulk-phase catalase dominance, FRET-proximity ≠ safety mechanism, Schiavon class precedent, updated chassis-selection criteria (production economics + regulatory + retention + immunogenicity, NOT proximity claims), Amplex Red wet-lab handoff documented.
- ✓ `gout-kill-chain-delivery-routes.md` (line 173): "H₂O₂ safety gate resolved by comp-035 2026-05-16: GREEN across all three architectures... Catalase (kcat/Km) is the dominant safety-margin driver; FRET-proximity claims are NOT the safety mechanism — bulk-phase catalase scavenging dominates."
- ✓ `delivery-route-matrix.md` §"Open exploration questions" #1 (line 208): same reframe text.

**The cross-chassis architectural principle that *was* missing got promoted to its own named platform discipline** via F3 (closed in companion item connection-6): "Catalase capacity principle" subsection added to `delivery-route-matrix.md` §"Chassis-as-formulation". That's the architecturally-load-bearing addition this cluster surfaced; the per-page reframe was already in.
