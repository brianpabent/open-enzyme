---
type: connection
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 2
global_index: 2
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Colchicine (CP2/CP3 tubulin) + topical CBD:THC (CB2 → NLRP3) as a dual-receptor, dual-route acute-flare stack — mechanism composed but never named as a combination protocol.

2. **Colchicine (CP2/CP3 tubulin) + topical CBD:THC (CB2 → NLRP3) as a dual-receptor, dual-route acute-flare stack — mechanism composed but never named as a combination protocol.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `colchicine.md`, `cannabinoids-terpenes.md`, `gout-action-guide.md`
   - *Page-pair linkage:* `colchicine.md` and `cannabinoids-terpenes.md` have **no direct cross-reference** to each other. `gout-action-guide.md` §"Active flare" now names both (colchicine as standard, topical CBD:THC as adjunct). `colchicine.md` §4.3 comparison table lists topical CBD+THC as an adjunct option.
   - *Why It Matters:* Colchicine blocks NLRP3 at CP2 (P2X7 pore) and CP3 (microtubule-mediated ASC transport). Topical CBD:THC at a 1:1 ratio blocks NLRP3 at CP2 via CB2 receptor activation on synovial macrophages — a completely different receptor pathway reaching the same chokepoint. The two interventions are **mechanism-non-redundant**: colchicine acts via β-tubulin binding (intracellular, cytoskeleton-level); CBD:THC acts via CB2 GPCR signaling (plasma-membrane-level, Gαi-coupled). `cannabinoids-terpenes.md` §4a now specifies a concrete protocol (ice 10–15 min → apply topical → ice again 30–60 min later). The combination — oral colchicine 1.2 mg + 0.6 mg at 1 hour (systemic CP2/CP3) PLUS topical CBD:THC on the affected joint (local CB2 → CP2) — hits the same chokepoints via **two independent receptor mechanisms and two independent delivery compartments** (systemic oral + local transdermal). This is the acute-flare equivalent of the multi-chokepoint stacking logic the platform already applies to chronic prophylaxis, but transposed to the acute window. No wiki page names this combination as a deliberate protocol.
   - *Suggested Action:* Add a "Combined acute-flare protocol: colchicine + topical CBD:THC" subsection to `gout-action-guide.md` §"Active flare" that explicitly names the dual-receptor, dual-route logic. The evidence base is In Vitro / Animal Model for each arm individually; the combination is Speculative and should be tagged as such.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The combination protocol is correctly identified as an unnamed composition: `colchicine.md` documents low-dose colchicine's CP3 microtubule/ASC-speck blockade plus CP2 P2X7 pore inhibition, while `cannabinoids-terpenes.md` and `gout-action-guide.md` document topical 1:1 CBD:THC + ice as an acute-flare adjunct via CB2/NLRP3 and TRPV1/cooling analgesia. The evidence tiers also match the corpus: colchicine is clinical-standard for acute gout, while topical cannabinoid use remains In Vitro / Animal Model plus mechanistic extrapolation, not human gout RCT evidence.

---

**WALKED 2026-05-19 — Closed (TWO combined-route protocols named, with Brian's n=1 anchor on Protocol B).**

Brian's 2026-05-19 walkthrough context: he doesn't use colchicine (so the daemon's colchicine + topical CBD:THC framing fits some users but not him), but he DOES use a four-route layered protocol (prednisone + topical CBD:THC + inhaled cannabis + ice) and has a documented n=1 observation supporting it. The closure formalizes BOTH protocols.

Actioned:
- ✓ Added new "Combined-route flare protocols — mechanism-non-redundant stacking" subsection to `gout-action-guide.md` §"Active flare" naming TWO protocols:
  - **Protocol A** — Colchicine + topical CBD:THC (for users on colchicine). Two independent receptor pathways (tubulin/P2X7 intracellular vs CB2 GPCR plasma-membrane) reaching the same CP2 chokepoint via two delivery compartments.
  - **Protocol B** — Prednisone + topical CBD:THC + inhaled cannabinoid + ice (four-route layered, n=1-supported). Mechanism layering documented including GR-after-LPS-priming timing alignment per H2 lit scan.
- ✓ Added cross-reference from `colchicine.md` §3.3.1 to `cannabinoids-terpenes.md` documenting the dual-receptor adjunct logic with explicit mechanism-non-redundancy framing.
- ✓ Added Brian's n=1 observation as new "Brian's n=1 observation — four-route layered flare-interrupt" subsection in `cannabinoids-terpenes.md` §4a. Documented with explicit epistemic-tier tags (n=1, uncontrolled, single observation, multi-intervention) per `self-experiment-protocol.md` discipline. Mechanism interpretation cross-references the H2 lit scan's GR-after-LPS-priming timing-dependence finding.

Also closes:
- 2026-05-17 most-curious-thread-1 (same dual-receptor mechanism-composition pick).
