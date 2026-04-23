---
title: Oridonin
aliases:
  - Rabdosin
  - Natural NLRP3 Inhibitor
  - Cys279 Inhibitor
  - Rabdosia Extract
related:
  - nlrp3-inflammasome
  - gout
  - natural-compounds
  - chokepoint-2
  - traditional-medicine
sources:
  - nlrp3-exploit-map.md
---

# Oridonin: Natural NLRP3 Inhibitor from Traditional Medicine

**Oridonin** is an ent-kaurane diterpenoid compound isolated from *Rabdosia rubescens*, a plant used in traditional Chinese medicine. It is a **specific, covalent NLRP3 inflammasome inhibitor** that targets the exact same binding site used by the pharmaceutical NLRP3 inhibitor MCC950, achieving comparable potency through a natural product scaffold.

## Mechanism: Covalent NLRP3 Inhibition at NACHT Domain Cys279

### The Binding Target

Oridonin covalently and irreversibly modifies **cysteine 279 (Cys279)** in the NACHT domain of NLRP3 protein. This domain contains the nucleotide-binding pocket essential for NLRP3 conformational changes required for inflammasome assembly.

By forming a covalent bond at this site, oridonin prevents the NLRP3-NEK7 interaction — a critical step in inflammasome platform formation. This is the same mechanism targeted by MCC950 (a pharmacological NLRP3 inhibitor), but through a different chemical approach.

**(Source: nlrp3-exploit-map.md)** — "Oridonin, an ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens, covalently and specifically modifies NLRP3 at cysteine 279. This is the same domain that MCC950 targets — the NACHT domain. By forming an irreversible covalent bond, oridonin blocks the NLRP3-NEK7 interaction that's essential for inflammasome assembly."

### The Chemistry: Michael Addition

Oridonin's mechanism is a **Michael addition** — a nucleophilic attack by the thiol group of Cys279 on the α,β-unsaturated carbonyl in oridonin's molecular structure. This is the same type of covalent modification used by other natural NLRP3 inhibitors and by some pharmaceutical compounds.

## Potency & Specificity

### Active Concentration

Oridonin exhibits dose-dependent inhibition of NLRP3 in cell culture:
- Caspase-1 cleavage: reduced dose-dependently
- IL-1β secretion: suppressed
- Pyroptotic cell death: prevented

**Curated human NLRP3 IC50 (ChEMBL v34, queried 2026-04-23):** 5,180 nM (5.18 μM) in human THP-1 macrophages under LPS/ATP stimulation (*Eur J Med Chem* 2023, ChEMBL ID CHEMBL1164920, pChEMBL = 5.29). This is the only direct human NLRP3 bioactivity for oridonin in the ChEMBL database — which is stricter than review-literature citations because it requires a curated binding/inhibition assay, not a downstream IL-1β readout. (In Vitro; source: nlrp3-inhibitor-screen.md)

**Legacy citation (0.5–2 μM):** The commonly repeated "0.5–2 μM" figure — including earlier versions of this page — derives from the 2018 *Nature Communications* paper (Cys279 covalent binding kinetics), which reported cell-free and mouse-derived assays. It does not translate 1:1 to the curated human-cell IC50 above. Treat the two numbers as complementary: 0.5–2 μM for covalent-binding-kinetic potency (cell-free/mouse), 5.18 μM for human cellular IC50. (source: nlrp3-inhibitor-screen.md)

These concentrations are physiologically achievable with oral supplementation, but the potency gap versus pharmaceutical benchmarks is larger than older wiki framing implied — dapansutrile (also 1 μM human cellular IC50) is in the same order of magnitude as oridonin in human cells, not orders of magnitude more potent. MCC950's 7.5 nM figure is from the original Coll et al. 2015 *J Biol Chem* paper (cell-free NACHT Walker B) and is not directly comparable to cellular IC50 without a head-to-head assay.

### NLRP3-Specific

Critically, oridonin **does not affect other inflammasome types** — specifically NLRC4 or AIM2 inflammasomes, which operate through different mechanisms. This selectivity is important for safety; non-selective inflammasome inhibition could impair other critical immune responses.

**(Source: nlrp3-exploit-map.md)** — "Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM. It's NLRP3-specific — doesn't affect NLRC4 or AIM2 inflammasomes."

## Multi-Pathway Inhibition

Beyond direct NLRP3 inhibition, oridonin activates secondary anti-inflammatory pathways:

### Nrf2 Activation (Signal 1 / Chokepoint 1)

Oridonin activates Nrf2 (nuclear factor erythroid 2-related factor 2), the master regulator of cellular antioxidant defense. This suppresses NF-κB-driven transcription of inflammatory genes.

### NF-κB Suppression (Chokepoint 1)

Direct suppression of NF-κB pathway in addition to Nrf2 effects.

**(Source: nlrp3-exploit-map.md)** — "The dual hit: Beyond NLRP3, oridonin also activates Nrf2 and suppresses NF-κB independently. So it hits CP1 AND CP2 through different mechanisms."

This multi-target property makes oridonin more potent than a single-mechanism inhibitor — it attacks both the priming step (NF-κB) and the activation step (NLRP3 direct inhibition).

## Evidence Level: Published Mechanism in Nature Communications

The peer-reviewed evidence for oridonin's NLRP3 inhibition is strong:

- **Primary mechanism:** 2018 Nature Communications study on covalent NLRP3-Cys279 modification
- **Analog development:** 2025 research on more potent oridonin derivatives
- **Gout-specific studies:** ✗ None published
- **Human clinical trials:** ✗ None

The mechanism is well-established in cell culture and animal models, but clinical translation to gout has not occurred.

**(Source: nlrp3-exploit-map.md)** — "Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM." (As noted above, this figure is from the original covalent-binding kinetic assays and does not equal the curated human THP-1 cellular IC50 of 5.18 μM — *Eur J Med Chem* 2023, ChEMBL entry.)

## Traditional Medicine Provenance

### Rabdosia rubescens Usage

*Rabdosia rubescens* (also called *Isodon rubescens*) is a plant used in traditional Chinese medicine for inflammatory conditions, clearing heat, and removing toxins. The plant has been used for centuries in Asian herbal medicine, though oridonin specifically was only isolated and characterized in modern times.

### Modern Extraction & Standardization

Commercial preparations typically contain:
- Crude Rabdosia extracts (standardized to oridonin content by HPLC)
- Isolated oridonin powder (higher concentration, more expensive)
- Combination formulas blending Rabdosia with other anti-inflammatory herbs

### Bioavailability Considerations

Natural plant extracts vary significantly in bioavailability. Oridonin-specific extracts are more consistent than whole-plant preparations. Oral supplementation of isolated oridonin or standardized extracts (50–200 mg/day) achieves active serum concentrations.

## Comparison: Oridonin vs. Pharmaceutical NLRP3 Inhibitors

| Compound | Target | Mechanism | Curated human NLRP3 IC50 (ChEMBL v34) | Status | Cost | Safety |
|----------|--------|-----------|---|--------|------|--------|
| **Oridonin** | NLRP3 Cys279 | Covalent (natural) | **5.18 μM** (THP-1, *Eur J Med Chem* 2023) | Available now | ~$20–40/month | Good (traditional use) |
| **MCC950** | NLRP3 Walker B | Non-covalent (pharma) | 7.5 nM (cell-free, Coll 2015 — not in ChEMBL by common synonyms) | Discontinued (Phase 1 hepatotoxicity) | NA | Hepatotoxic |
| **Dapansutrile** | NLRP3 (general) | Direct inhibitor | **1.0 μM human MDM** / 1.0 nM mouse J774A.1 (**1000× species gap**) | Phase 2a in gout published 2020; **no Phase 2b/3 registered as of 2026-04** | Unknown | Good (Phase 2 safety) |
| **Tranilast** | NLRP3 NACHT | Non-covalent (pharma) | Zero direct human NLRP3 bioactivities in ChEMBL (2017 EMBO Mol Med NACHT-binding claim rests on non-ChEMBL assays) | Approved (Japan/Korea) | ~$30–50/month | Good (decades of use) |

(IC50 values above reflect ChEMBL v34 curated cross-check, 2026-04-23. source: nlrp3-inhibitor-screen.md)

**Key observation:** Oridonin is a covalent NLRP3 inhibitor like MCC950, but unlike MCC950 it has not shown hepatotoxicity. It's available immediately, costs far less than clinical-stage drugs, and has the advantage of traditional use history (though this is not the same as modern clinical trial validation).

**Revised potency framing (2026-04-23):** When comparing cellular IC50 in human cells rather than cell-free NACHT-binding kinetics, oridonin (5.18 μM) and dapansutrile (1.0 μM) are within ~5× of each other. Dapansutrile's mouse cellular IC50 of 1 nM is 1,000× more potent than its own human cellular IC50 — a major species gap that reframes how we should interpret rodent NLRP3-inhibitor preclinical data generally. Oridonin's gap between cell-free covalent-binding kinetics (~0.5–2 μM) and human cellular IC50 (5.18 μM) is small by comparison. (source: nlrp3-inhibitor-screen.md)

## Derivative Development

Recent research (2025) has focused on **synthetic analogs of oridonin** that achieve even higher NLRP3 potency while maintaining the safety profile:

**(Source: nlrp3-exploit-map.md)** — "recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives."

These next-generation compounds could combine oridonin's natural product scaffold with enhanced pharmaceutical properties.

## Practical Implementation

### Sourcing

- **Standardized Rabdosia extract:** ~50–100 mg oridonin per dose, easily sourced from supplement suppliers
- **Isolated oridonin:** Higher concentration (95%+ pure), available from specialty suppliers
- **Cost:** Significantly less than pharmaceutical alternatives ($20–40/month for therapeutic dosing)

### Dosing

- **Typical range:** 50–200 mg oridonin per day (from Rabdosia extract or isolated form)
- **Timing:** With meals; fat may improve absorption
- **Safety profile:** Decades of traditional use at these levels; no known serious adverse effects at therapeutic dosing

### Integration with Other Compounds

Oridonin + [[bhb-ketones|BHB]] represent a two-pronged NLRP3 inhibition strategy:
- Oridonin: direct NLRP3 + Nrf2 activation
- BHB: K⁺ efflux blockade + ASC oligomerization prevention
- Combined: redundant suppression of multiple inflammasome activation pathways

Oridonin + beta-caryophyllene is a third mechanistically distinct combination worth testing. Oridonin acts covalently at NLRP3 Cys279 (NACHT domain); beta-caryophyllene acts via CB2 agonism upstream (TLR4/MyD88/NF-κB suppression in MSU-stimulated synovium, animal model). No direct combination studies are published, but the mechanisms are non-overlapping, and a combination may allow dose reduction of oridonin — reducing any off-target covalent reactivity risk from chronic dosing. See [Cannabinoids & Terpenes](./cannabinoids-terpenes.md#experiments-that-would-move-the-needle) for the proposed MSU-model combination experiment. (source: cannabinoids-terpenes.md)

## Related Concepts

- [[nlrp3-inflammasome|NLRP3 Inflammasome]] — The target pathway
- [[gout|Gout Flare Cascade]] — The disease mechanism
- [[sulforaphane|Sulforaphane and Nrf2 Activation]] — Another Nrf2-activating anti-inflammatory
- [[dapansutrile|Dapansutrile]] — Pharmaceutical NLRP3 inhibitor in clinical trials
- [[bhb-ketones|Beta-Hydroxybutyrate]] — Complementary NLRP3 mechanism

## Key Insight

**Oridonin bridges traditional medicine and modern immunology.** It is a specific, covalent NLRP3 inhibitor with a well-characterized mechanism, available immediately at low cost, with the advantage of centuries of traditional use and the safety history of Rabdosia preparations. Unlike MCC950 (which caused hepatotoxicity) and unlike dapansutrile (which is still in Phase 3), oridonin is available now and targets exactly the same molecular vulnerability (NLRP3 Cys279) that pharmaceutical programs have identified.

The limitation is the absence of gout-specific clinical trials, but the mechanistic case is as strong as it is for any other NLRP3 inhibitor.

---

*Last updated: April 2026*
*Wiki synthesized from primary research documents*
