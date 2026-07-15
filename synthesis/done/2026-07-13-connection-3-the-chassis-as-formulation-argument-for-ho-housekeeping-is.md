---
type: connection
sweep_date: 2026-07-13
sweep_sha: fae0e36
section_index: 3
global_index: 3
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# The "chassis-as-formulation" argument for H₂O₂ housekeeping is now quantitatively resolved across all three intra-articular uricase architectures, but it is driven by total catalase capacity at the joint scale, not by residue-level proximity.

3. **The "chassis-as-formulation" argument for H₂O₂ housekeeping is now quantitatively resolved across all three intra-articular uricase architectures, but it is driven by total catalase capacity at the joint scale, not by residue-level proximity.** *Supported.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `chassis-pending-interventions.md`, `gout-kill-chain-delivery-routes.md`, `delivery-route-matrix.md`, `intra-articular-uricase-h2o2-reaction-diffusion-computational.md` (comp-035), `engineered-koji-protocol.md`, `complement-c5a-gout.md`
   - *Page-pair linkage:* Weakly-connected pair. `chassis-pending-interventions.md` and `delivery-route-matrix.md` both discuss the intra-articular uricase + catalase route and the H₂O₂ housekeeping issue, but neither links the resolution to the reaction-diffusion analysis that quantitatively closes it. The specific finding that FRET-confirmed <10 nm proximity is *not* the safety mechanism (Da_shell ~5×10^{-3}, escape fraction ~0.998, bulk-phase catalase scavenging dominates) is named only in comp-035.
   - *Why It Matters:* The H₂O₂ housekeeping risk was the single load-bearing safety question for the chassis-pending intra-articular uricase route. comp-035's Damköhler-number analysis across three architectures (Pickering emulsion, fusion protein, free co-formulated catalase) closes it as GREEN under reference dosing. The finding is load-bearing for chassis selection: Pickering and fusion fix stoichiometry by construction; free co-formulated fails at YELLOW only when the URI:CAT ratio is mis-engineered (high URI, low CAT). Catalase (kcat/Km) is the dominant sensitivity driver (Spearman r = −0.95 to −0.97). This reframes the previous qualitative "H₂O₂ diffuses faster than catalase can scavenge it" critique in `delivery-route-matrix.md` §"Why SC uricase doesn't work" as correct for SC depots but not for IA at typical dosing. The chassis-as-formulation argument for oral whole-cell uricase (peroxisomal co-localization) is now quantitatively corroborated by the IA bulk-catalase scavenging result. The two routes solve the same biochemistry problem through different mechanisms; both depend on the same load-bearing variable (total catalase capacity at the reaction site).
   - *Suggested Action:* Update `chassis-pending-interventions.md` §6 to reflect the comp-035 verdict (all three architectures GREEN under reference dosing; catalase capacity is the dominant driver). Add the reaction-diffusion result to `delivery-route-matrix.md` §"Catalase capacity principle" as the quantitative anchor. The IA uricase route is now mechanistically defensible and should be promoted from "candidate for traditional-name re-scan" to "active exploration vector" in the modality matrix. Run the Amplex Red microelectrode H₂O₂ measurement in synovial-fluid mimic as the first wet-lab confirmation (estimated $2–5K, already scoped in comp-035 handoff).

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` This item is an exact duplicate of New Connections #2 — identical title, body, document list, `[CHAIN-DEPTH: 3+]` tag, and suggested action. The synthesis run inserted the same finding twice. The content is correct (comp-035's Damköhler analysis is accurately relayed, and `chassis-pending-interventions.md` §6 does contain the comp-035 summary), but the duplication is a synthesis error that wastes a queue slot. The emitter should deduplicate: retain one instance (New Connections #2) and drop this one. If the intent was to surface the Liu 2025 FRET-claim vs. comp-035 Damköhler tension as a contradiction, that belongs in the Contradictions Found section, not as a duplicate New Connection.

---

## ✓ Actioned 2026-07-14 — dedup

Exact duplicate of connection-2 (same comp-035 H₂O₂ finding; Pass 3: "drop this one"). Closed as part of the queue-items-2–4 dedup cluster — see connection-2's closure annotation for the substantive action (caveat propagation to the two downstream pages; no IA promotion). No separate wiki work.
