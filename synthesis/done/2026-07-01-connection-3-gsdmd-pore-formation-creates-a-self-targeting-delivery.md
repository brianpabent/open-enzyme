---
type: connection
sweep_date: 2026-07-01
sweep_sha: 18d3696
section_index: 3
global_index: 3
pass3_verdict: Confirmed
overlap_tag: NOVEL
---

# GSDMD pore formation creates a self-targeting delivery route for KPV peptide into pyroptotic cells.

3. **GSDMD pore formation creates a self-targeting delivery route for KPV peptide into pyroptotic cells.** *Speculative*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `gsdmd-pore-delivery-paradox.md`, `kpv-peptide.md`, `gout-kill-chain-delivery-routes.md`
   - *Page-pair linkage:* No prior linkage exists between the GSDMD pore delivery mechanism and KPV peptide as a therapeutic payload.
   - *Why It Matters:* `gsdmd-pore-delivery-paradox.md` describes how GSDMD pores (10-20 nm) in pyroptotic cells allow entry of otherwise membrane-impermeant molecules. `kpv-peptide.md` identifies KPV as a small (tripeptide), hydrophilic molecule that inhibits intracellular NLRP3 and NF-κB. This connection proposes that KPV is an ideal payload for the GSDMD self-delivery mechanism. During a gout flare, macrophages undergo pyroptosis, opening GSDMD pores. KPV present in the synovial fluid would selectively enter these "leaky" pyroptotic cells, concentrating the anti-inflammatory agent precisely where it's needed most. This provides a new, highly targeted delivery rationale for using KPV (systemically or via intra-articular injection) for acute flare management, enhancing its therapeutic window.
   - *Suggested Action:* Propose a wet-lab experiment: stimulate THP-1 macrophages with MSU to induce pyroptosis, then add fluorescently-labeled KPV. Use confocal microscopy or flow cytometry to demonstrate increased intracellular KPV accumulation in GSDMD-pore-forming cells compared to non-pyroptotic controls. This would be a direct validation of the proposed delivery synergy.

> **Pass 3 review — Confirmed.** `[OVERLAP: NOVEL]` The mechanism is solid. `gsdmd-pore-delivery-paradox.md` documents GSDMD pores at 10–20 nm inner diameter — KPV (tripeptide, Lys-Pro-Val, ~360 Da) is trivially small for these pores. `kpv-peptide.md` confirms KPV's intracellular targets are NLRP3 inflammasome assembly and NF-κB, both active in pyroptotic macrophages during a gout flare. The size match is compelling (KPV is ~1–2 orders of magnitude below the pore's demonstrated permissivity range), the target match is exact, and the proposed wet-lab experiment (fluorescent-KPV + MSU-stimulated THP-1 ± GSDMD inhibitor) is the right first move. One refinement from the corpus: `gsdmd-pore-delivery-paradox.md` §"Open questions" #4 flags that pore lifetime is minutes to tens of minutes before ESCRT repair or lysis — so the delivery window is brief, and KPV must already be present in extracellular fluid when pores open. This shifts the clinical framing from "systemic KPV anytime" to "KPV present in synovial fluid at flare onset," which favors intra-articular or early-oral dosing. Worth noting in the experimental design.

---

## ✓ Actioned 2026-07-13

Ran **comp-042** ([`kpv-gsdmd-pore-influx-computational.md`](../../wiki/kpv-gsdmd-pore-influx-computational.md)) as a $0 computational prior before any wet-lab commit. Result reframes this connection: the pore transport physics is sound (intracellular [KPV] equilibrates to synovial concentration in ~2 s — answers the paradox page's Open Question #4), but KPV-*selective* self-delivery is **falsified** for two independent reasons — (1) KPV already enters cells via PepT1 ([Dalmasso 2008, PMID 18061177](https://doi.org/10.1053/j.gastro.2007.10.026); grep-verified against PubMed), so healthy cells admit it too and may concentrate it *more*; (2) PD timing mismatch — KPV is an upstream NLRP3/NF-κB inhibitor, but pores open downstream of inflammasome firing, so it arrives too late. The *general* pore-delivery thesis survives with a sharpened payload spec (transporter-orphan + downstream-acting + intracellularly-labile); Ac-FLTD-CMK fits better than KPV. Documented in [`gsdmd-pore-delivery-paradox.md`](../../wiki/gsdmd-pore-delivery-paradox.md) §"Computational stress-test" + [`kpv-peptide.md`](../../wiki/kpv-peptide.md) §"GSDMD Pore Self-Delivery — Evaluated, Not Selective for KPV". No H-card (not thesis-ready).
