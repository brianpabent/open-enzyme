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

**Oridonin** is an ent-kaurane diterpenoid isolated from *Rabdosia rubescens*, a plant used in traditional Chinese medicine. Its gout-relevant hypothesis is direct, covalent interruption of NLRP3–NEK7 assembly at Cys279. That mechanism is established in preclinical systems, including a human THP-1 assay, but has not been tested clinically in gout.

> **Species-gap caveat:** Rodent NLRP3 potency does not establish human-cell potency; apply the cross-species standard in [`chembl-cross-check.md`](./etc/chembl-cross-check.md) before making dose claims.

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

The 0.5–2 μM figure from the 2018 *Nature Communications* paper reflects cell-free and mouse-derived covalent-binding assays; it does not translate 1:1 to the 5.18 μM human cellular IC50. MCC950's 7.5 nM figure is likewise cell-free and is not directly comparable without a head-to-head cellular assay. (source: nlrp3-inhibitor-screen.md)

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

These secondary effects could broaden target engagement beyond NLRP3 assembly, but they do not establish greater potency or clinical benefit.

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

*Rabdosia rubescens* (also called *Isodon rubescens*) is a plant used in traditional Chinese medicine for inflammatory conditions, clearing heat, and removing toxins (冬凌草 Dong Ling Cao — "heat-clearing detoxification" category in TCM materia medica). The plant has been used for centuries in Asian herbal medicine, though oridonin specifically was only isolated and characterized in modern times.

Apply the chokepoint, ChEMBL, bioavailability, and formula-decomposition standards in [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md) when evaluating this TCM-lineage candidate. (source: tcm-modern-rigor-intersection.md)

### Modern Extraction & Standardization

Commercial preparations typically contain:
- Crude Rabdosia extracts (standardized to oridonin content by HPLC)
- Isolated oridonin powder (higher concentration, more expensive)
- Combination formulas blending Rabdosia with other anti-inflammatory herbs

### Bioavailability Considerations

Natural plant extracts vary significantly in bioavailability. Oridonin-specific extracts are more consistent than whole-plant preparations. Oral supplementation of isolated oridonin or standardized extracts (50–200 mg/day) achieves active serum concentrations.

## Translation boundary

Oridonin's curated human cellular IC50 is 5.18 μM, versus 1.0 μM for dapansutrile in human MDM. Dapansutrile's mouse cellular IC50 is 1,000× lower than its human result, illustrating why rodent potency cannot stand in for human-cell exposure. Oridonin has no gout-specific study and no human clinical trial. (source: nlrp3-inhibitor-screen.md)

## Derivative Development

Recent research (2025) has focused on **synthetic analogs of oridonin** with higher NLRP3 potency:

**(Source: nlrp3-exploit-map.md)** — "recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives."

Whether those analogs retain an acceptable off-target and safety profile remains a separate question.

## Contraindications, Drug Interactions, and Dose-Dependent Risk

**Contraindications:**
- Pregnancy (insufficient data; covalent-binding mechanism warrants caution)
- Pediatric use (insufficient data)
- Active hepatic disease (some Rabdosia preparations have hepatotoxicity case reports at high TCM-formula doses)
- Combination with other covalent-mechanism drugs without spacing (theoretical concern)

**Drug interactions:**
- **CYP3A4 substrates:** preliminary in vitro data suggests modest CYP3A4 inhibition by oridonin — relevant for tacrolimus, cyclosporine, simvastatin, some calcium channel blockers, and direct oral anticoagulants.
- **Omeprazole, PPIs:** mechanistic-extrapolation concern only; no clinical data.
- **Covalent-mechanism drugs (clopidogrel, prasugrel, aspirin at antiplatelet dose):** theoretical compounding of covalent off-target effects; no clinical signal.

**Dose-dependent risk profile:**
- 50–100 mg/day purified oridonin: tolerated in published TCM and supplement dosing; main risk is sourcing-quality and standardization.
- 200–500 mg/day high-dose extracts: case reports of transient ALT elevation; not common but flagged.
- Sourcing variability: Rabdosia rubescens whole-extract preparations contain other diterpenoids with unclear safety profiles. Purified oridonin from research chemical suppliers is more characterizable.

**Stack interactions:**
- **Synergy with sulforaphane, quercetin (Nrf2 axis):** all three are Nrf2 activators; cumulative effect with diminishing returns.
- **Mechanistic complementarity with BCP, BHB, dapansutrile (CP2):** these candidates touch NLRP3 through different mechanisms, but additivity has not been established.
- **No documented ABCG2 interaction.**

(source: supplements-stack.md)

---

## Sources and delivery

- **Whole-plant and standardized extracts:** *R. rubescens* preparations vary in diterpenoid composition; HPLC-standardized oridonin content improves characterization.
- **Isolated compound:** Higher-purity material is available from specialty suppliers, but human oral pharmacokinetics and gout target engagement remain unresolved.
- **Formulation question:** Extract consistency, systemic exposure, and covalent off-target reactivity need to be measured together; traditional use does not answer those questions.

Oridonin + beta-caryophyllene is a third mechanistically distinct combination worth testing. Oridonin acts covalently at NLRP3 Cys279 (NACHT domain); beta-caryophyllene acts via CB2 agonism upstream (TLR4/MyD88/NF-κB suppression in MSU-stimulated synovium, animal model). No direct combination studies are published, but the mechanisms are non-overlapping, and a combination may allow dose reduction of oridonin — reducing any off-target covalent reactivity risk from chronic dosing. See [Cannabinoids & Terpenes](./cannabinoids-terpenes.md#experiments-that-would-move-the-needle) for the proposed MSU-model combination experiment. (source: cannabinoids-terpenes.md)

## Related Concepts

- [[nlrp3-inflammasome|NLRP3 Inflammasome]] — The target pathway
- [[gout|Gout Flare Cascade]] — The disease mechanism
- [[sulforaphane|Sulforaphane and Nrf2 Activation]] — Another Nrf2-activating anti-inflammatory
- [[dapansutrile|Dapansutrile]] — Pharmaceutical NLRP3 inhibitor in clinical trials
- [[bhb-ketones|Beta-Hydroxybutyrate]] — Complementary NLRP3 mechanism

## Falsification tests

1. Establish oral pharmacokinetics for a characterized preparation and compare achieved free concentration with the human THP-1 IC50.
2. In human macrophages, verify Cys279 engagement, NLRP3–NEK7 disruption, and preservation of AIM2/NLRC4 signaling at the same exposure.
3. In an MSU model, test whether target engagement changes flare readouts without unacceptable hepatic or covalent off-target signals.
