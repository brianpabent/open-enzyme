---
type: connection
sweep_date: 2026-07-13
sweep_sha: fae0e36
section_index: 2
global_index: 2
pass3_verdict: Augment
overlap_tag: EXTENSION
---

# The "chassis-as-formulation" argument for H₂O₂ housekeeping is now quantitatively resolved across all three intra-articular uricase architectures, but it is driven by total catalase capacity at the joint scale, not by residue-level proximity.

2. **The "chassis-as-formulation" argument for H₂O₂ housekeeping is now quantitatively resolved across all three intra-articular uricase architectures, but it is driven by total catalase capacity at the joint scale, not by residue-level proximity.** *Supported.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `chassis-pending-interventions.md`, `gout-kill-chain-delivery-routes.md`, `delivery-route-matrix.md`, `intra-articular-uricase-h2o2-reaction-diffusion-computational.md` (comp-035), `engineered-koji-protocol.md`, `complement-c5a-gout.md`
   - *Page-pair linkage:* Weakly-connected pair. `chassis-pending-interventions.md` and `delivery-route-matrix.md` both discuss the intra-articular uricase + catalase route and the H₂O₂ housekeeping issue, but neither links the resolution to the reaction-diffusion analysis that quantitatively closes it. The specific finding that FRET-confirmed <10 nm proximity is *not* the safety mechanism (Da_shell ~5×10^{-3}, escape fraction ~0.998, bulk-phase catalase scavenging dominates) is named only in comp-035.
   - *Why It Matters:* The H₂O₂ housekeeping risk was the single load-bearing safety question for the chassis-pending intra-articular uricase route. comp-035's Damköhler-number analysis across three architectures (Pickering emulsion, uricase-catalase fusion, free co-formulated catalase) closes it as GREEN under reference dosing. The finding is load-bearing for chassis selection: Pickering and fusion fix stoichiometry by construction; free co-formulated only works when URI:CAT ratio is engineered correctly. Catalase (kcat/Km) is the dominant sensitivity driver (Spearman r = −0.95 to −0.97). The architecture-distinguishing edge case is the free co-formulated YELLOW outcome at uneven URI:CAT ratio (31.6 µM H₂O₂). This reframes the previous qualitative "H₂O₂ diffuses faster than catalase can scavenge it" critique in `delivery-route-matrix.md` §"Why SC uricase doesn't work" as correct for SC depots but not for IA at typical dosing. The chassis-as-formulation argument for oral whole-cell uricase (peroxisomal co-localization) is now quantitatively corroborated by the IA bulk-catalase scavenging result. The two routes solve the same biochemistry problem through different mechanisms; both depend on the same load-bearing variable (total catalase capacity at the reaction site).
   - *Suggested Action:* Update `chassis-pending-interventions.md` §6 to reflect the comp-035 verdict (all three architectures GREEN under reference dosing; catalase capacity is the dominant driver). Add the reaction-diffusion result to `delivery-route-matrix.md` §"Catalase capacity principle" as the quantitative anchor. The IA uricase route is now mechanistically defensible and should be promoted from "candidate for traditional-name re-scan" to "active exploration vector" in the modality matrix. Run the Amplex Red microelectrode H₂O₂ measurement in synovial-fluid mimic as the first wet-lab confirmation (estimated $2–5K, already scoped in comp-035 handoff).

> **Pass 3 review — Augment.** `[OVERLAP: EXTENSION]` The content correctly relays comp-035's finding that bulk-phase catalase scavenging, not FRET-confirmed <10 nm proximity, is the safety mechanism for IA uricase architectures. The `chassis-pending-interventions.md` §6 does contain the comp-035 summary (verified via file read), and `delivery-route-matrix.md` does not yet link to the reaction-diffusion resolution. The factual claims are sound. **However, this item is an exact duplicate of New Connections #3 below — same title, same body, same `[CHAIN-DEPTH: 3+]` tag, same suggested action.** The synthesis contains a duplicate insertion. The downstream emitter should deduplicate: keep one instance, merge the other into the "Contradictions Found" section if the Liu 2025 FRET-claim-vs-Damköhler tension is the intended contradiction, or drop. The content itself is load-bearing for chassis selection and warrants the suggested `chassis-pending-interventions.md` §6 and `delivery-route-matrix.md` updates.

---

## ✓ Actioned 2026-07-14

**Dedup cluster (queue items 2–4) closed as one; this is the retained instance.** connection-3 and contradiction-1 are the same comp-035 H₂O₂ finding inserted two more times — Pass 3 flagged both as duplicates to drop.

The comp-035 reaction-diffusion finding (bulk-phase catalase scavenging, **not** FRET <10 nm proximity, is the IA-uricase H₂O₂ safety mechanism) was **already integrated** into both target pages before this walk: `chassis-pending-interventions.md §6` carries the full proximity-claim reframe, and `delivery-route-matrix.md` §"Catalase capacity principle" already links comp-035. The suggested integration action was already done.

**What this walk added:** propagated the comp-035 **"GREEN not decision-grade" audit caveat** (comp-review 2026-07-14) to the two downstream pages, which still presented it as "resolved / GREEN / independently validated" — the same loose end as comp-027 (source page caveated, downstream sites not). `chassis-pending §6` and `delivery-route-matrix` now carry the caveat + the "do not promote the IA uricase route on this alone; gated on Amplex Red" gate. The suggested promotion ("candidate → active exploration vector") was **NOT** done — the audit caveat blocks it.
