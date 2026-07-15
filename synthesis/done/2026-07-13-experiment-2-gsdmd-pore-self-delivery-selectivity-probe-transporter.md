---
type: experiment
sweep_date: 2026-07-13
sweep_sha: fae0e36
section_index: 2
global_index: 6
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# GSDMD-Pore Self-Delivery — Selectivity Probe (transporter-orphan tracer ± PepT1 blockade).

2. **GSDMD-Pore Self-Delivery — Selectivity Probe (transporter-orphan tracer ± PepT1 blockade).** Cost: ~$2,000–5,000. Time: 4–6 weeks. Decides: Whether a membrane-impermeant payload is selectively concentrated in pyroptotic (GSDMD-pore-forming) macrophages versus intact-membrane cells — the load-bearing selectivity claim of the pore self-delivery paradox. The transport model (comp-042) returned YELLOW (provisional) — the flux physics is sound (a ~20 nm pore equilibrates the cell interior to the extracellular concentration in ~2 s; lifetime not limiting), but selectivity is the real decision variable and it is falsified for KPV specifically: KPV already enters cells via PepT1 (Dalmasso 2008, PMID 18061177), and as an upstream inhibitor it arrives downstream of inflammasome firing. This reframes the experiment — a fluorescent-KPV uptake assay is PepT1-confounded and tests the wrong molecule. The clean test uses a transporter-orphan tracer. (source: gsdmd-pore-delivery-paradox.md, kpv-gsdmd-pore-influx-computational.md, kpv-peptide.md, disulfiram.md)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The proposal correctly reframes the GSDMD-pore experiment around comp-042's key finding: KPV is the wrong payload to demonstrate pore-selectivity because it already enters cells via PepT1 (Dalmasso 2008, PMID 18061177). The comp-042 outputs confirm that the PepT1 baseline makes A2 selectivity unquantifiable for KPV, and that a transporter-orphan tracer is the clean test. The cost estimate ($2,000–5,000) and timeline (4–6 weeks) are reasonable for a custom fluorescent tracer synthesis + macrophage uptake assay. The connection to `gsdmd-pore-delivery-paradox.md` and `disulfiram.md` is correctly cited. One sharpening: the proposal could explicitly name a candidate transporter-orphan payload class (e.g., a charged, membrane-impermeant fluorophore or a small cyclic peptide with no known SLC transporter) to accelerate wet-lab scoping, but the conceptual reframe is sound as-is.

---

## ✓ Actioned 2026-07-14 — already fully actioned

**Closed as already-done.** The experiment is registered as validation-experiments.md **§1.32** "GSDMD-Pore Self-Delivery — Selectivity Probe (transporter-orphan tracer ± PepT1 blockade)" (added 2026-07-13) — thorough: THP-1 macrophages, transporter-orphan tracer primary probe, PepT1-confounder control arm (fluorescent-KPV ± PepT1 inhibitor), disulfiram as GSDMD-pore-blocker control, GREEN/RED criteria. Pass 3's "name a candidate payload" sharpening is already in §1.32 (charged fluorescent dextran / calcein derivative, no peptide-transporter route). comp-042 (kpv-gsdmd-pore-influx-computational.md) is complete + peer-reviewed (YELLOW-provisional; KPV-as-selective-payload effectively falsified, the transporter-orphan platform thesis genuinely open), and gsdmd-pore-delivery-paradox.md already carries the comp-042 caveat + reframe.

**Micro-cleanup done:** added a pointer at gsdmd-pore-delivery-paradox.md §"Open questions" Tier-1 precursor (line ~176) marking §1.32 as the canonical sharpened design of record, so the earlier precursor note and §1.32 don't read as competing designs.
