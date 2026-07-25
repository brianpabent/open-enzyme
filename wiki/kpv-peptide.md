---
title: KPV Tripeptide
aliases:
  - Lys-Pro-Val
  - Alpha-MSH C-terminal tripeptide
tags:
  - kpv
  - peptide
  - pept1
  - nf-kb
  - delivery
related:
  - nlrp3-exploit-map.md
  - gsdmd-pore-delivery-paradox.md
  - kpv-gsdmd-pore-influx-computational.md
  - validation-experiments.md
sources:
  - "Dalmasso G et al. Gastroenterology 2008;134(1):166-178 (PMID 18061177; DOI 10.1053/j.gastro.2007.10.026)"
---

# KPV Tripeptide

KPV (Lys-Pro-Val) is the C-terminal tripeptide of α-melanocyte-stimulating hormone. Its qualified Open Enzyme evidence supports PepT1-mediated uptake and an NF-κB assay response in specific cell systems; it does not establish gout efficacy, synovial exposure, or a clinical delivery route.

## Evidence relevant to gout

Dalmasso et al. measured KPV transport through human PepT1 in Caco2-BBE intestinal epithelial cells and Jurkat T cells. The reported KPV transport constants were approximately 160 µM in the epithelial system and 700 µM in Jurkat cells. In the Caco2-BBE assay, extracellular KPV concentrations in the nanomolar range reduced IL-1β-induced NF-κB reporter activation; 10 nM was the lowest tested effective concentration used as the engineering proxy in [COMP-042](./kpv-gsdmd-pore-influx-computational.md). These are **In Vitro** observations in the named models ([PMID 18061177](https://pubmed.ncbi.nlm.nih.gov/18061177/)); 10 nM is not an intracellular IC50, target-engagement threshold, or gout-effective concentration.

NF-κB contributes to inflammatory priming in the gout cascade, so a PepT1-dependent KPV effect in a gout-relevant macrophage is plausible but remains a **Mechanistic Extrapolation**. The qualified evidence on this page does not establish direct NLRP3-assembly inhibition by KPV, activity against monosodium urate crystals, or an effect in human gout. See the [NLRP3 exploit map](./nlrp3-exploit-map.md) for the pathway context.

## Sourcing and delivery

For research use, the material must be a chemically defined KPV preparation with its sequence or chemical form, counterion, purity, identity, endotoxin burden, solvent, and stability recorded. These are experimental-material requirements, not consumer-sourcing guidance.

Delivery remains unresolved:

- **PepT1 uptake:** demonstrated in Caco2-BBE and Jurkat systems (**In Vitro**); functional uptake in resting or MSU-activated synovial macrophages is unmeasured.
- **Joint exposure:** no qualified route-specific KPV pharmacokinetic measurement establishes useful extracellular or intracellular exposure in a human joint.
- **COMP-042 route spaces:** the intra-articular range is arithmetic from declared dose and compartment-volume assumptions; subcutaneous and oral values are named pharmacokinetic design spaces. They are not observed synovial concentrations or route qualifications.
- **Intracellular stability:** uncharacterized in the relevant cells and not modeled by COMP-042.
- **Clinical safety:** no route-specific clinical safety package is cited here. This page is a research record, not a dosing or treatment protocol.

## GSDMD pore entry

[COMP-042](./kpv-gsdmd-pore-influx-computational.md) estimates the passive GSDMD-pore contribution relative to the 10 nM extracellular cell-assay proxy; it does not model intracellular efficacy. Under the declared route spaces, A1 is GREEN for intra-articular, YELLOW for subcutaneous, and RED for oral delivery. The full A2 grid retains favorable heuristic corners—including two of nine moderate-PepT1 and one of nine high-PepT1 intra-articular combinations—but healthy-cell uptake, synovial-macrophage PepT1 activity, and concurrent PepT1 transport in pore-forming cells remain unmeasured or unmodeled.

Because KPV is framed as acting upstream of pore formation, the useful intervention window is uncertain; pathway order alone does not prove that pore-mediated entry is too late. KPV is therefore a confounded probe of pore selectivity. A prequalified transporter-orphan payload with a downstream intracellular target would isolate the pore contribution more directly. **Mechanistic Extrapolation.**

> **Research conjecture — KPV could modify gout-relevant inflammatory priming before pore formation**{ .research-conjecture-label }
>
> **Grounded premises:** KPV enters the epithelial and Jurkat cell systems studied through PepT1 and reduces IL-1β-induced NF-κB reporter activation at extracellular nanomolar concentrations (**In Vitro**; [Dalmasso et al.](https://pubmed.ncbi.nlm.nih.gov/18061177/)). NF-κB is part of gout-relevant inflammatory priming (**Mechanistic Extrapolation**; [NLRP3 exploit map](./nlrp3-exploit-map.md)).
>
> **Novel leap:** If a gout-relevant macrophage admits KPV through PepT1 at a useful exposure before or during priming, KPV might reduce later inflammasome output. No direct evidence tests this sequence in gout or synovial macrophages.
>
> **Why it matters:** This would define a KPV opportunity independent of the more weakly constrained pore-selectivity hypothesis.
>
> **Discriminating observation:** In a prespecified MSU-relevant macrophage system, cross KPV timing and concentration with PepT1-on/off conditions; measure intracellular KPV, NF-κB priming, pro-IL-1β, inflammasome/caspase/GSDMD outputs, viability, and washout controls.

## Falsification path

Two questions should be tested separately:

1. **KPV biology:** Does exact KPV produce a reproducible, PepT1-dependent change in gout-relevant priming at a measured intracellular exposure? A result that lacks uptake, concentration response, or mechanism-proximal change does not advance the conjecture.
2. **Pore-delivery physics:** [Validation §1.32](./validation-experiments.md#132-gsdmd-pore-self-delivery--matched-uptake-and-selectivity-probe) uses a prequalified transporter-orphan tracer for the primary pore-on/off test and KPV only as a pore-on/off × PepT1-on/off uptake comparator. It has no KPV efficacy endpoint.

A negative result kills only the tested material, exposure, timing, cell system, and mechanism claim. It does not decide every α-MSH-derived peptide or the wider transporter-orphan pore-delivery hypothesis.

## Related

- [NLRP3 exploit map](./nlrp3-exploit-map.md) — gout-relevant inflammatory chokepoints
- [GSDMD pore-delivery hypothesis](./gsdmd-pore-delivery-paradox.md) — the wider physical-delivery conjecture
- [COMP-042](./kpv-gsdmd-pore-influx-computational.md) — model, assumptions, results, and limits
- [Validation experiments](./validation-experiments.md#132-gsdmd-pore-self-delivery--matched-uptake-and-selectivity-probe) — matched empirical gate
