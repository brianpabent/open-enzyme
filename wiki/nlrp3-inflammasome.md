---
title: NLRP3 Inflammasome
aliases:
  - NLRP3
  - NOD-like receptor protein 3
  - inflammasome
  - IL-1β pathway
  - ASC speck
related:
  - uricase
  - gout
  - bpc-157
  - blood-barrier
  - complement-c5a-gout
  - spm-resolution-pathway
  - tnfsf14-gout-target
sources:
  - nlrp3-exploit-map.md
  - gout-deep-dive.md
  - peptide-gout-addendum.md
  - complement-c5a-gout.md
  - spm-resolution-pathway.md
  - tnfsf14-gout-target.md
  - etc/chembl-cross-check.md
  - theaflavins.md
  - zileuton.md
  - nlrp3-inhibitor-screen.md
---

# NLRP3 Inflammasome

## Overview

The NLRP3 inflammasome is a multi-protein intracellular complex that acts as a master trigger for the acute inflammatory response in gout. It is composed of three core proteins: NLRP3 (the sensor), ASC (the adaptor), and pro-caspase-1 (the executioner). When activated, it cleaves pro-IL-1β into active interleukin-1β (IL-1β), a potent pro-inflammatory cytokine that drives the explosive pain and swelling of a gout flare. (Source: gout-deep-dive.md, nlrp3-exploit-map.md)

The inflammasome is not unique to gout—it evolved to respond to pathogenic danger signals. However, monosodium urate (MSU) crystals, which deposit in joints during hyperuricemia, directly trigger NLRP3 assembly through lysosomal rupture, potassium efflux, and reactive oxygen species (ROS) generation. In gout, the innate immune system mistakes metabolic crystals for microbial threats, producing an outsized inflammatory cascade. (Source: gout-deep-dive.md)

## The NLRP3 Activation Cascade: Seven Chokepoints (with Sub-Branches)

The NLRP3 inflammasome pathway operates as a sequential cascade with seven primary vulnerability points (chokepoints), several with mechanistically distinct sub-branches. Each is a potential therapeutic target — gout can be attacked at multiple nodes simultaneously rather than through a single intervention. The CP0–CP6b vocabulary below is referenced throughout the corpus; the [NLRP3 Exploit Map](./nlrp3-exploit-map.md) owns the full per-chokepoint catalog.

The v1.2 restructure (April 2026) added CP0 (complement priming, C5a-dominant, upstream of NF-κB), sub-branches CP1a (TNFSF14/LIGHT priming amplifier) and CP1b (C5a→ROS), CP5b (active resolution via ALX/FPR2 SPMs, alongside CP5a receptor blockade), and promoted 5-LOX/LTB4 neutrophil chemotaxis to a first-class CP6a chokepoint. (source: nlrp3-exploit-map.md)

| Chokepoint | The step | Canonical exploit |
|---|---|---|
| **CP0** — Complement priming (C5a-dominant) | MSU activates complement → C5a→C5aR1 → ROS primes NLRP3, upstream of NF-κB | Avacopan (oral C5aR1 antagonist; platform gap — no fermentable modulator) |
| **CP1 (CP1a/CP1b)** — NF-κB priming | TLR/LPS → NF-κB transcribes NLRP3, pro-IL-1β, pro-IL-18, ASC. CP1a = TNFSF14/LIGHT amplifier; CP1b = C5a→ROS | Sulforaphane (Nrf2); also berberine, curcumin, KPV, EGCG, TNFSF14 blockade |
| **CP2** — NLRP3 activation / ASC assembly | K⁺ efflux + mtROS drive NLRP3 oligomerization and ASC nucleation | BHB (direct oligomerization block); also oridonin, tranilast, theaflavins, NAC |
| **CP3** — ASC speck assembly / caspase-1 recruitment | Microtubule transport assembles ASC specks → recruits pro-caspase-1 | Colchicine (microtubule depolymerization) |
| **CP4** — Caspase-1 activation / substrate cleavage | Active caspase-1 cleaves pro-IL-1β and GSDMD (the executioner step) | VX-765/belnacasan (selective caspase-1 inhibitor) |
| **CP5a** — IL-1β/IL-18 secretion and signaling | Mature IL-1β binds IL-1R1 → neutrophil recruitment, pain, systemic flare | Anakinra (IL-1R1 antagonist); canakinumab; inhaled mRNA-IL-1RA (chassis-pending) |
| **CP5b** — Active resolution via ALX/FPR2 | SPMs (resolvins, protectins, maresins) signal neutrophil withdrawal + efferocytosis | Omega-3 EPA/DHA precursors → RvD1/MaR1 (Animal Model gout evidence) |
| **CP6a** — Neutrophil amplification via 5-LOX/LTB4 | 5-LOX produces LTB4 → neutrophil chemotaxis sustains the flare | Zileuton (5-LOX inhibitor); quercetin (5-LOX IC50 300 nM); AKBA |
| **CP6b** — GSDMD pore / pyroptotic amplification | Caspase-1-cleaved GSDMD-N oligomerizes into pores → pyroptosis releases IL-1β + alarmins | Disulfiram (Cys191 covalent block); DMF |

For the full per-chokepoint exploit catalog (mechanism detail, all compound entries, dosing, ChEMBL cross-check verdicts, coverage audit), see [NLRP3 Exploit Map](./nlrp3-exploit-map.md). Compound-specific dossiers: [colchicine](./colchicine.md), [oridonin](./oridonin.md), [BHB/ketones](./bhb-ketones.md), [theaflavins](./theaflavins.md), [zileuton](./zileuton.md), [disulfiram](./disulfiram.md), [complement C5a](./complement-c5a-gout.md), [SPM resolution pathway](./spm-resolution-pathway.md), [cannabinoids & terpenes](./cannabinoids-terpenes.md).

## Endogenous and Protein-Protein Interface (PPI) Regulatory Checkpoints

Recent programmatic mapping of the Reactome database (`R-HSA-844456`) coupled with a comprehensive literature review has identified four high-resolution, biophysical regulatory interfaces within the NLRP3 pathway. These represent novel strategic entry points for engineered therapeutics and natural-product stack designs:

### 1. Pyrin as a Competitive ASC Decoy (CP3 Sequestration)
*   **Mechanism:** Trimeric Pyrin (encoded by *MEFV*) acts as a molecular sink or competitive decoy, binding to the adaptor protein **ASC (PYCARD)** via homotypic PYD-PYD interactions to physically prevent ASC from forming high-molecular-weight specks with NLRP3 (source: Molecular Cell 2003, PMID: 12718875).
*   **Structural Details:** 
    *   **ASC PYD Interface:** Electrostatic bipolar interaction. The positively charged surface involves **Lys21** and **Arg41** (helices α2/α3); the negatively charged surface involves **Glu13**, **Asp48**, and **Asp51** (helices α1/α4).
    *   **Pyrin PYD Interface:** Mediated by three distinct sites: Leu10/Glu14 (Site 1), Lys25/Arg42 (Site 2), and Leu71/Arg75/Arg80 (Site 3). The FMF-associated **R42W** mutation severely disrupts this binding loop.
*   **Biophysical Affinities ($K_d$):**
    *   *NLRP3-ASC PYD:* Moderate affinity ($K_d \approx 22 \ \mu\text{M}$); relies on highly cooperative, nucleation-controlled filament polymerization.
    *   *POP1-ASC Decoy (Benchmark):* High affinity ($K_d \approx 4.08 \pm 0.52 \ \mu\text{M}$); POP1-ASC successfully outcompetes basal NLRP3-ASC interaction (**In Vitro**).
*   **Evidence Level:** **Animal Model** (heightened endotoxin sensitivity and caspase-1 activation in $Mefv^{-/-}$ mice) and **In Vitro** (NMR/SPR interface mapping).

### 2. HMOX1 NACHT-Domain Shielding (CP2 Oligomerization Arrest)
*   **Mechanism:** Soluble cytosolic Heme Oxygenase 1 (HMOX1/HO-1) interacts directly with the **NACHT domain** of NLRP3, physically masking the Walker motifs to block the self-association required for oligomerization (source: J. Biol. Chem. 2018, PMID: 30121650).
*   **Enzymatic Independence:** This structural shielding occurs in an **enzymatic activity-independent manner**. Inhibition of HO-1 catalytic activity (via SnPP) does not impair its binding to NLRP3 or its cytoprotective properties.
*   **Therapeutic Translation:** This interface provides an ideal template for de novo peptide mimics. Hydrocarbon-stapled peptides derived from the 12–15 amino acid HO-1 binding loop can be designed to selectively shield the NLRP3 NACHT domain.
*   **Evidence Level:** **Animal Model** (epithelial-specific HO-1 overexpression mitigates NLRP3-driven injury in murine models) and **In Vitro** (Co-IP and GST pull-down assays).

### 3. SGT1 (SUGT1) Chaperone Chokepoint (CP2 Stabilisation)
*   **Mechanism:** In resting cells, the specialized co-chaperone SGT1 (encoded by *SUGT1*) complexes with HSP90 to bind and stabilize the **Leucine-Rich Repeat (LRR) domain** of NLRP3, keeping it in an inactive but signaling-competent primed state (source: Nat. Immunol. 2007, PMID: 17401368).
*   **Disruption Outcome:** Pharmacological disruption of the SGT1-HSP90 interface causes the rapid routing of NLRP3 to the ubiquitin-proteasome system and autophagic degradation. 
*   **Natural Product Synergy (Echinatin):** Echinatin, a retrochalcone isolated from Licorice (*Glycyrrhiza inflata*, Gancao), acts as a selective HSP90 ATPase inhibitor, driving **dissociation of SGT1** from the HSP90-NLRP3 complex and triggering selective NLRP3 degradation (**Animal Model**, JCI Insight 2021).
*   **Evidence Level:** **Animal Model** (Echinatin protects against colitis and NASH pathology in vivo) and **In Vitro** (BMDMs and PBMC chaperone dissociation kinetics).

### 4. P2X7/Pannexin-1 Macropore & Ionic Collapse (CP2 Activation Trigger)
*   **Mechanism:** Low-level extracellular ATP triggers the trimeric P2X7 receptor to act as a standard small-cation channel ($K^+$ efflux, $Na^+$/$Ca^{2+}$ influx). Under sustained high extracellular ATP levels, P2X7 recruits the hemichannel **Pannexin-1 (Panx1)** to form a giant non-selective **macropore** permeable to large molecules up to 800–900 Da (source: EMBO J. 2006, PMID: 17036048). This drives a catastrophic cytosolic potassium ($K^+$) depletion ("ionic collapse"), the universal biophysical switch for NLRP3 oligomerization.
*   **Structural Regulation:** 
    *   **P2X7 C-Terminal Tail:** Contains a proline-rich domain (residues 450–456) with SH3-binding motifs that recruits Src tyrosine kinase to phosphorylate and activate adjacent Pannexin-1 channels.
    *   **CRR Palmitoylation:** The juxtamembrane cysteine-rich region is palmitoylated at residues **C362, C363, C374, and C377** (rat numbering), which prevents channel desensitization. Truncation or cysteine mutations completely abolish macropore formation.
*   **Inhibitory Modulators:**
    *   **10Panx1 Peptide:** A synthetic 10-amino acid mimetic (**WRQAAFVDSY**) derived from the ECL1 loop of Pannexin-1 that sterically blocks the macropore and suppresses mature IL-1β release without affecting baseline P2X7 small-cation currents (**In Vitro**).
    *   **Emodin (TCM/Kampo Antagonist):** Emodin, an anthraquinone from Rhubarb (*Rheum officinale*, Dahuang), acts as a selective P2X7 antagonist with an $IC_{50} \approx 3 \ \mu\text{M}$ for human P2X7 and $0.2 - 0.5 \ \mu\text{M}$ for macrophage death/pore blockade (**Animal Model**).
*   **Evidence Level:** **Animal Model** (Panx1 and P2X7 knockouts display profound protection against gouty arthritis flares in vivo) and **In Vitro** (electrophysiology and BzATP-evoked dye uptake).

### Chokepoint 5 — endogenous IL-1Ra biology (anakinra is not a foreign molecule)

This is the canonical explainer for why recombinant IL-1Ra has such a clean safety profile — referenced from [`chassis-pending-interventions.md` §4](./chassis-pending-interventions.md). The acute-flare anakinra protocol (100 mg SC daily × 3 days, ~$900/flare, cumulative-steroid-burden framing) and the inhaled mRNA-IL-1RA pulse comparator live canonically in [gout-action-guide.md §"Active flare"](./gout-action-guide.md) and [chassis-pending-interventions.md §4](./chassis-pending-interventions.md) respectively; the [exploit map's CP5a section](./nlrp3-exploit-map.md) carries the full mechanism entries.

Humans naturally produce IL-1Ra (~17 kDa, encoded by IL1RN, secreted primarily by macrophages and neutrophils as a feedback brake on IL-1 signaling). Endogenous IL-1Ra competes with IL-1α and IL-1β for the same IL-1R1 receptor — when bound, it occupies the receptor without triggering downstream signaling. The IL-1β / IL-1Ra ratio determines net signaling: at homeostatic baseline, endogenous IL-1Ra is in ~100× molar excess over IL-1β, keeping signaling damped. Inflammatory states (gout flare, autoimmune, sepsis) tip the ratio by driving IL-1β production faster than IL-1Ra, exceeding the endogenous brake. **Therapeutic anakinra is the same protein the body makes, just at supplemental dose** — which is why the safety profile is so clean (essentially zero immunogenicity, no ADCC/CDC off-target effects, simple competitive-antagonism mechanism). The same "endogenous brake" framing is why mRNA-encoded IL-1Ra is a cleaner payload than an mRNA-encoded anti-IL-1β monoclonal: IL-1Ra is small (no glycosylation, no disulfides, no heavy/light chain assembly), broader-mechanism (blocks IL-1α AND IL-1β at the same receptor), and immunogenicity-free as a recombinant version of an endogenous protein. (source: chassis-pending-interventions.md, gout-action-guide.md, nlrp3-exploit-map.md)

## Multi-Chokepoint Compounds

The most efficient exploits hit three or more chokepoints — BHB (CP1+CP2+CP3), berberine (CP1+CP4), oridonin (CP1+CP2), DMF (CP1+CP2+CP6b), EGCG (CP1+CP4+CP5). See the [NLRP3 Exploit Map "Multi-Chokepoint Compounds" section](./nlrp3-exploit-map.md) for the per-compound chokepoint breakdown. (source: nlrp3-exploit-map.md)

## Pharmaceutical NLRP3 Inhibitors

### Approved or In Clinical Development

- **Canakinumab (Ilaris)**: IL-1β monoclonal antibody. **FDA approved for gout in August 2023** — the first biologic ever formally indicated for gout in the US, 12 years after its initial 2011 rejection. Originally approved for CAPS/JIA. Very effective but expensive (~$300,000/year). Systemic immunosuppression risk. (Clinical Trial; *J Inflamm Res* 2026;19, PMID: 41867470. source: gout-clinical-pipeline.md)

- **Genakumab (Firsekibart)**: Chinese canakinumab competitor (GeneScience). Phase 3 NCT05983445 (313 patients) completed April 2024. Same anti-IL-1β mechanism. (Clinical Trial; source: gout-clinical-pipeline.md)

- **Anakinra (Kineret)**: IL-1 receptor antagonist. FDA-approved for RA and CAPS. Off-label for refractory gout. Less expensive than canakinumab but requires daily injection.

- **Rilonacept (Arcalyst)**: IL-1 trap. **Rejected by FDA for gout in 2012** despite a 1,315-patient Phase 3 (NCT00856206) demonstrating efficacy. Not currently in active gout development. (Clinical Trial; source: gout-clinical-pipeline.md)

- **Dapansutrile (OLT1177)**: Oral NLRP3 inhibitor. Phase 2a in gout (N=34, *Lancet Rheumatol* 2020, PMID: 33005902) showed 52–68% target joint pain reduction at day 3 across four dose levels. **However, no Phase 2b or Phase 3 trial in gout is registered on ClinicalTrials.gov as of April 2026.** Olatec's subsequent active programs moved to heart failure (Phase 1b NCT03534297, completed 2019) and COVID-19 (Phase 2 NCT04540120, terminated 2022). Dapansutrile in gout appears stalled, not advancing. (Clinical Trial; source: gout-clinical-pipeline.md) **Species-gap caveat (ChEMBL v34, 2026-04-23):** Dapansutrile's curated cellular IC50 is **1.0 nM in mouse J774A.1 cells but 1.0 μM in human MDM cells — a 1,000× species gap** (*Eur J Med Chem* 2020/2023, *Bioorg Med Chem Lett* 2021). The Phase 2a efficacy at 100–2,000 mg/day is consistent with human-cell μM potency at high oral doses, not with the sub-nanomolar mouse-cell potency. This reframes translational expectations for the entire oral-NLRP3-inhibitor class. (In Vitro; source: nlrp3-inhibitor-screen.md)

- **MCC950 (CRID3)**: The first specific NLRP3 inhibitor. Binds the Walker B motif in the NACHT domain, blocking ATP hydrolysis required for oligomerization. Clinical development terminated due to hepatotoxicity in Phase 1 RA trial, but it defined the druggable target and validated the mechanism. **ChEMBL cross-check (2026-04-23):** MCC950 / CRID3 / CP-456773 are not retrievable by common synonyms in ChEMBL v34's name search; the cited 7.5 nM IC50 (Coll et al. 2015 *J Biol Chem*, cell-free Walker B) has not been independently re-indexed by the MCP cross-check. Benchmark status unchanged, but the IC50 is not verified via ChEMBL. (source: nlrp3-inhibitor-screen.md)

### Two-Tier Labeling: Direct Inhibitors vs. Pathway Modulators (2026-04-23)

The 2026-04-23 ChEMBL v34 cross-check (see [nlrp3-inhibitor-screen.md](nlrp3-inhibitor-screen.md) appendix) surfaced a labeling rigor issue. Only two compounds in the wiki's broader NLRP3 discussion have a curated direct human NLRP3 IC50 in ChEMBL:

- **Dapansutrile:** 1.0 μM (human MDM, *Eur J Med Chem* 2023) — but 1 nM in mouse J774A.1 (1,000× species gap)
- **Oridonin:** 5.18 μM (human THP-1, *Eur J Med Chem* 2023)

MCC950 and tranilast have published direct NLRP3 assays in the primary literature but are not retrievable via ChEMBL's curated target-bound bioactivity table for human NLRP3 (CHEMBL1741208) by common synonyms.

**Compounds with zero curated direct human NLRP3 entries in ChEMBL:** quercetin, ursolic acid, tranilast, beta-caryophyllene. Their "NLRP3 inhibitor" status rests on functional IL-1β readouts in macrophage assays or upstream pathway effects (NF-κB priming, ROS, K⁺ efflux) — not direct NLRP3 binding/inhibition measurements.

**Going-forward convention:** Distinguish "direct NLRP3 inhibitor" (binding/inhibition IC50 measured against NLRP3 protein) from "NLRP3 pathway modulator" (functional IL-1β reduction, mechanism inferred). Both are clinically relevant — Open Enzyme ultimately cares about IL-1β output, not NLRP3 biochemistry per se — but the distinction sharpens how claims are written. (In Vitro; source: nlrp3-inhibitor-screen.md)

### NLRP3 Pipeline Has Drifted Out of Gout

The broader NLRP3 inhibitor pipeline has moved to other indications where the biology has wider therapeutic appeal: DFV890 (Novartis, knee osteoarthritis Phase 2 completed Dec 2024), NT-0796 (NodThera, obesity + semaglutide Phase 2a active), VTX3232 (Zomagen, Parkinson's Phase 2a completed April 2025), VENT-02 (Ventus, Parkinson's Phase 1b **terminated Oct 2025**), Inzomelid (Inflazome/Roche, CAPS Phase 1 completed), ZYIL1 (Zydus, Phase 1 completed). **No NLRP3-specific compound is in active gout-indicated trials as of April 2026.** This is a strategic data point for Open Enzyme's "food-derived NLRP3 adjunct" positioning — the prescription pipeline isn't delivering for gout. (source: gout-clinical-pipeline.md)

### Emerging Target: TNFSF14 (LIGHT) — CP1a Priming Amplifier

A 2024 *Annals of the Rheumatic Diseases* study (Ea et al., DOI: 10.1136/ard-2023-225305, PMID: 38373842) used the Olink 92-protein inflammation panel on gout flare vs. intercritical vs. treat-to-target patients. **TNFSF14 (TNF superfamily 14, also called LIGHT) was the second-highest fold-change gout-flare biomarker after IL-6.** LIGHT signals via HVEM and LTβR receptors on fibroblast-like synoviocytes, B cells, monocytes, and myeloid cells, activating NF-κB and AP-1 — a priming amplifier parallel to LPS/TLR4 (classified as CP1a in the exploit map v1.2). Ex vivo TNFSF14 blockade reduced LPS+MSU cytokine production; SNPs in TNFSF14 modulate myeloid cytokine output. CERC-002 (anti-LIGHT mAb) showed positive Phase 2 data in COVID ARDS — potential repurposing candidate. Safety caveat: LIGHT has dual roles (LIGHT-null mice have worse colitis) — episodic or LTβR-selective blockade is safer than total suppression. Natural compounds: EGCG suppresses TNFSF14-induced IL-6 and downregulates HVEM receptor expression (In Vitro); DHA shows inverse genetic association with circulating LIGHT. (Clinical Trial + In Vitro; source: gout-clinical-pipeline.md, tnfsf14-gout-target.md) See [TNFSF14 Gout Target](./tnfsf14-gout-target.md) for the dedicated analysis.

## Engineered Koji & Production Candidates

*A. oryzae* could be engineered to overproduce food-derived NLRP3-suppressing compounds (procyanidin/EGCG-like polyphenols), and several stack compounds have established microbial titers — ursolic acid (8.59 g/L in *S. cerevisiae*), quercetin (930 mg/L), carnosine (the only candidate with dual hyperuricemia + NLRP3 rat data), and native kojic acid (3–5 g/L, NLRP3 mechanism unscreened). The full production-candidate analysis (titers, potency rankings, bioavailability, stacking strategy) lives in the [NLRP3 Exploit Map "AI Analysis — Microbial Production Candidates" section](./nlrp3-exploit-map.md) and [07 — NLRP3 Inhibitor Screen](../ai-analysis/07-nlrp3-inhibitor-screen.md). (source: nlrp3-exploit-map.md)

## The SIBO–Gout–Lynn Connection

NLRP3 activation is a shared driver of both gout and SIBO-driven intestinal inflammation, so several stack compounds (berberine, KPV, omega-3 SPMs, BHB/fasting, spermidine+trehalose) suppress both conditions through the same mechanism. See the [NLRP3 Exploit Map "SIBO–Gout–Lynn Connection" section](./nlrp3-exploit-map.md) for the full per-compound dual-indication mapping. (source: nlrp3-exploit-map.md)

---

## Key Insights

**The Crystal Dissolution Danger Window:** When urate-lowering therapy (including [[uricase|koji-uricase]]) begins dissolving existing MSU crystal deposits, crystals temporarily become smaller with more surface area. Crystal shedding from tophi can trigger acute flares. The NLRP3 stack is essential during this phase—it prevents dissolution-triggered flares while the uricase handles the underlying uric acid problem. Both strategies must run simultaneously. (Source: nlrp3-exploit-map.md, gout-deep-dive.md)

**Disulfiram is Underrated:** An FDA-approved drug with 70 years of safety data, costing ~$30/month, that blocks the final step of IL-1β release and prevents pyroptotic amplification. Few rheumatologists discuss it because it was discovered by immunologists studying sepsis—a market inefficiency in medical knowledge. (Source: nlrp3-exploit-map.md)

**Ketosis Paradox Resolved:** The conventional wisdom that ketosis is bad for gout (ketones compete with urate for renal excretion) misses that BHB simultaneously and potently suppresses NLRP3 inflammasome activation. With [[uricase|koji-uricase]] handling uric acid clearance, ketosis becomes purely beneficial—all inflammasome suppression, no uric acid penalty. (Source: nlrp3-exploit-map.md)

## References

- Source: nlrp3-exploit-map.md — Systematic black hat pen-testing of NLRP3 inflammasome pathway; v1.2 restructure (April 2026) adds CP0, CP1a/1b, CP5a/5b, CP6a/6b — seven primary chokepoints
- Source: gout-deep-dive.md — Comprehensive gout pathophysiology including NLRP3 inflammasome overview and crystal-driven activation
- Source: peptide-gout-addendum.md — Deep dive into peptide mechanisms including BPC-157 and TB-500 NLRP3 interactions
- Source: complement-c5a-gout.md — Complement C5a as dominant NLRP3 priming signal (CP0); avacopan repurposing candidate
- Source: spm-resolution-pathway.md — Active resolution via ALX/FPR2 SPMs (CP5b); RvD1 and MaR1 gout animal model evidence
- Source: tnfsf14-gout-target.md — TNFSF14/LIGHT as second-highest gout-flare biomarker (CP1a); EGCG and DHA natural activity; CERC-002 clinical precedent
- Source: chembl-cross-check.md — ChEMBL v34 curated cross-check of stack compounds; curcumin 24.2 μM NLRP3 IC50, berberine TDO top target, resveratrol DPP-4 top target, EGCG proteasome 86 nM
- Source: theaflavins.md — Theaflavins (black-tea polyphenols): NLRP3-NEK7 disruption (CP2/CP3), direct MSU peritonitis Animal Model, URAT1/GLUT9 downregulation, TF3 TNFSF14/HVEM modulation (CP1a); Tier 2 supplement candidate added 2026-05-05
- Source: zileuton.md — Zileuton (FDA-approved 5-LOX inhibitor, asthma): CP6a repurposing candidate; zero gout trials registered; hepatotoxicity monitoring required; n=1 protocol design
- Source: nlrp3-inhibitor-screen.md — 2026-05-05 audit: sulforaphane upgraded to Tier 2 (Yang 2018 PMID 29340626 direct MSU gout; Greaney 2015 PMID 26269198 Nrf2-independent inflammasome inhibition); theaflavins added as Tier 2
