---
title: "Houttuynia cordata Polysaccharides"
date: 2026-07-23
tags: [houttuynia, polysaccharide, complement, nlrp3, tlr4, cp0, cp1, gut-delivery]
related:
  - complement-c5a-gout.md
  - nlrp3-exploit-map.md
  - validation-experiments.md
  - cfh-mechanism-dissociation-cp0-candidates.md
  - supplements-stack.md
sources:
  - "Zhou et al. Int J Biol Macromol 2022;222:2414–2425 (PMID 36252625; DOI 10.1016/j.ijbiomac.2022.10.027)"
  - "Li et al. Acta Pharm Sin B 2025;15(6):3073–3091 (PMID 40654358; PMCID PMC12254813; DOI 10.1016/j.apsb.2025.04.008)"
  - "Cheng et al. Carbohydr Polym 2014;103:244–249 (PMID 24528726; PMCID PMC7112369; DOI 10.1016/j.carbpol.2013.12.048)"
  - "Lu et al. Acta Pharm Sin B 2018;8(2):218–227 (PMID 29719782; PMCID PMC5925397; DOI 10.1016/j.apsb.2017.11.003)"
status: research-stage
---

# Houttuynia cordata Polysaccharides

*Houttuynia cordata* polysaccharides are a material-defined research track with two separable gout-relevant hypotheses:

1. **CP0 — complement:** an exact polysaccharide material may reduce complement activation around MSU crystals.
2. **CP1 — inflammatory direction:** an exact material may suppress or amplify macrophage priming and IL-1β release, depending on structure, context, and contamination controls.

Evidence for one route does not establish the other. Neither route has direct human gout evidence.

## Evidence

| Material | Reported result | Evidence boundary |
|---|---|---|
| **CHCP, crude polysaccharides** | Inhibited classical and alternative complement in vitro; depleted-serum experiments implicated C3 and C4, with a partial C5 effect. Oral CHCP also reduced complement-associated injury in rat lung-injury and fever models ([Lu 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5925397/)). | **In Vitro + Animal Model.** Not an MSU-crystal or gout experiment. |
| **HCPM, 19.1 kDa acidic heteropolysaccharide** | Sequential ultrafiltration produced a defined material with CH50 = 254.1 ± 7.8 µg/mL; HCPM reduced complement activation and injury in an H1N1 mouse model ([Zhou 2022](https://doi.org/10.1016/j.ijbiomac.2022.10.027)). | **In Vitro + Animal Model.** The hemolysis assay and infection model do not establish gout efficacy. |
| **HCPM and crude HCP** | Both materials reduced intestinal C3a/C5a, NLRP3, cleaved caspase-1, IL-1β, and IL-18 in H1N1–MRSA coinfection mice ([Li 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12254813/)). | **Animal Model.** The experiment cannot distinguish a direct macrophage effect from a complement-mediated or intestinal-system effect. |
| **HCP-2, 60 kDa pectic homogalacturonan** | Increased IL-1β and other inflammatory mediators in naïve human PBMCs; a TLR4 antagonist reduced HCP-2-induced IL-1β ([Cheng 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC7112369/)). | **In Vitro.** Supports TLR4 involvement, not direct TLR4/MD-2 binding or a gout effect. |

The bounded multilingual scan completed on 2026-07-14 identified no study testing an isolated *H. cordata* polysaccharide in an MSU, urate, hyperuricemia, or gout model. That is a searched-corpus result, not a universal absence claim. See the [structure–activity scan](../logs/houttuynia-polysaccharide-structure-activity-lit-scan-2026-07-14.md).

## Sourcing and material identity

The biologically relevant unit is an exact material, not the species name or a capsule label.

- **HCPM reference:** obtain material from the originating group or reproduce the sequential-ultrafiltration preparation reported by Zhou et al. Confirm molecular-weight distribution, carbohydrate and uronic-acid content, monosaccharide profile, and batch identity before biological testing.
- **Crude HCP:** record plant part, voucher or identity method, extraction, precipitation, deproteinization, drying, and lot.
- **Independent extracts:** test only lots with documented identity, composition, contaminants, and extraction method. A retail label cannot establish equivalence to HCPM.
- **TLR4-sensitive assays:** qualify endotoxin and recovery controls before interpreting priming or suppression. Endotoxin contamination could otherwise be mistaken for material-specific TLR4 activity.

## Delivery and exposure

Li et al. frame HCPM as a gastrointestinally poorly absorbed macromolecule and report that intestinal improvement preceded lung improvement in the mouse coinfection model (**Animal Model**). The working oral-delivery hypothesis is therefore intestinal exposure, not direct delivery to synovial macrophages.

A positive result from directly bathing THP-1 macrophages in HCPM would establish only an in-vitro directionality signal. It would not establish that oral HCPM reaches joint macrophages, that an independent extract reproduces the material, or that intestinal complement modulation changes gout.

The delivery gate is to measure an exact material or validated structural markers along the intestinal tract after controlled oral exposure, then pair exposure with ex-vivo complement activity and tissue-safety readouts. Systemic and synovial exposure remain unestablished.

> **Research conjecture — Exact Houttuynia fractions may expose two independent gout weaknesses**{ .research-conjecture-label }
>
> **Grounded premises:** Defined HCPM inhibits complement and changes inflammatory outcomes in vitro and in infection-model mice (**In Vitro + Animal Model**; PMID 36252625, PMID 40654358). Crude CHCP affects C3/C4-centered complement activity (**In Vitro + Animal Model**; PMID 29719782). HCP-2 can instead raise IL-1β through a TLR4-sensitive response in naïve PBMCs (**In Vitro**; PMID 24528726).
>
> **Novel leap:** A qualified HCPM or related material may reduce MSU-driven inflammation through complement suppression, complement-independent macrophage modulation, or both. No direct evidence from an MSU or gout model exists.
>
> **Why it matters:** Two independent routes could make the material useful even if one route fails, while material-dependent sign reversal makes identity a decisive engineering variable.
>
> **Discriminating observation:** Test exact materials separately in an MSU–serum complement assay and a controlled macrophage priming/activation matrix. A negative result closes only the route and material actually tested.

## Experimental gates

1. **Direct macrophage directionality — [validation §1.30](./validation-experiments.md#130-houttuynia-cordata-polysaccharide-fraction-comparison-in-msu-stimulated-thp-1-macrophages--prioritization-screen).** Determine whether qualified materials suppress, amplify, or do not change LPS/MSU-driven IL-1β under contamination, viability, and priming controls.
2. **Complement route — [COMP-040](./computational-experiments.md).** Test MSU-crystal complement activation in CFH-replete and CFH-depleted serum. This route is independent of the macrophage result.
3. **Exposure and safety.** Only after an exact material produces a reproducible signal, measure intestinal persistence, complement activity, barrier effects, and systemic exposure before selecting a delivery strategy.

Failure in one assay does not retire the other route. Failure of both biological routes for qualified materials would deprioritize this intervention while leaving the wider complement and NLRP3 chokepoints open.
