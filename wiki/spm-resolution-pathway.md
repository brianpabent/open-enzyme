---
title: "SPM Resolution Pathway — ALX/FPR2 Agonism as a Gout Target (CP5b)"
date: 2026-04-24
tags:
  - spm
  - resolution
  - alx-fpr2
  - fpr2
  - rvd1
  - rvd2
  - mar1
  - maresin
  - resolvin
  - protectin
  - lipoxin
  - omega-3
  - dha
  - epa
  - gout
  - nlrp3
  - chokepoint-5b
  - aggnet
related:
  - nlrp3-exploit-map.md
  - nlrp3-inflammasome.md
  - gout-pathophysiology.md
  - gout-deep-dive.md
  - complement-c5a-gout.md
  - supplements-stack.md
  - lactoferrin.md
  - self-experiment-protocol.md
  - open-questions.md
  - open-enzyme-vision.md
sources:
  - "Zaninelli TH, Fattori V, Saraiva-Santos T, et al. Br J Pharmacol 2022;179(18):4500-4515 (PMID: 35716378)"
  - "Jiang H, Song D, Zhou X, et al. Mol Med 2023;29(1):158 (PMID: 37996809)"
  - "Zaninelli TH, Martelossi-Cebinelli G, Saraiva-Santos T, et al. Expert Opin Ther Targets 2023;27(8):679-703 (PMID: 37651647)"
  - "Schauer C, Janko C, Munoz LE, et al. Nat Med 2014;20(5):511-7 (PMID: 24784231)"
  - "Lopategi A, Flores-Costa R, Rius B, et al. J Leukoc Biol 2018;105(1):25-36 (PMID: 29601102)"
  - "Caron JP, Gandy JC, Brown JL, Sordillo LM. Prostaglandins Other Lipid Mediat 2019;142:1-8 (PMID: 30836143)"
  - "Serhan CN. Nature 2014;510(7503):92-101 (SPM review, foundational)"
status: published
---

# SPM Resolution Pathway — ALX/FPR2 Agonism as a Gout Target

**Chokepoint 5b** in the [NLRP3 exploit map](./nlrp3-exploit-map.md). CP5a handles receptor blockade (anakinra, canakinumab, rilonacept — the "off switch" for IL-1 signaling); CP5b is **active resolution via ALX/FPR2** and related GPCRs — fundamentally different in kind, not just degree. Most anti-inflammatory drugs *suppress*; SPMs *command resolution*.

**Scope:** mechanism primer (what resolution actually is, biosynthesis), individual SPM families (structures, receptors, effector profiles), receptor biology (ALX/FPR2, GPR32, GPR18, ChemR23/CMKLR1, LGR6, GPR37), functional effects on leukocytes, gout-specific evidence (direct MSU models), the complement → aggNET → resolution loop, kinetics of resolution, therapeutic landscape (precursors, direct SPMs, aspirin-triggered series, pharma pipeline), engineered-production feasibility, clinical biomarkers, and open research questions.

---

## 1. Overview — Resolution as Active Signaling, Not Passive Subsidence

### 1.1 The classical view and why it was wrong

The textbook view of acute inflammation through ~1995 was that inflammation "runs down" — once the provoking stimulus is cleared, signaling fuel (cytokines, leukocytes, lipid mediators) depletes and homeostasis is restored by default. Resolution was framed as the *absence* of ongoing inflammation rather than a positively-executed program.

The reframe, initiated by Charles Serhan's group at Brigham and Women's Hospital beginning with the 1999 lipoxin papers, is this: resolution is an **active, biosynthetic, receptor-mediated program** driven by a distinct class of lipid mediators — **specialized pro-resolving mediators (SPMs)** — that switch on in the resolution phase of inflammation, engage their own receptors, and command neutrophils to stop infiltrating and macrophages to start clearing debris and switch to the M2 phenotype. (Evidence level: In Vitro + Animal Model — decades of Serhan-lab and subsequent work, reviewed in [Serhan *Nature* 2014 510:92-101](https://doi.org/10.1038/nature13479).)

### 1.2 The COX-2 enzymatic paradox — where the whole field started

Aspirin was known to acetylate COX-2 and block prostaglandin synthesis. But aspirin-treated COX-2 was not simply "inactivated" — it kept producing lipid products, just *different* ones: 15R-hydroxyeicosatetraenoate from arachidonate, leading to 15-epi-lipoxin A4 ("aspirin-triggered lipoxin"). This was the foundational observation: a drug considered purely inhibitory was, at the enzyme level, **repurposing** the enzyme to produce a pro-resolution mediator instead of a pro-inflammatory one. The Serhan lab's systematic follow-up identified resolvins (2002), protectins (2004), and maresins (2009) as endogenous human mediators made through analogous biosynthetic rerouting from EPA and DHA. (Evidence level: In Vitro, biochemistry.)

### 1.3 Why this matters for gout

Gout flares are famously self-limiting — a typical flare peaks in 24-48 h and resolves spontaneously in 7-14 days even without treatment. The classical view would attribute this to crystal-load depletion (clearance + phagocytosis) and cytokine decay. The SPM view reframes it: **the flare resolves because resolution actively switches on**, and when it does not (or switches on insufficiently) the flare becomes chronic — tophaceous gout, chronic gouty arthritis. This predicts a therapeutic class that is orthogonal to suppression: drugs that *accelerate or enforce* resolution rather than blocking upstream cascade steps. At CP5b this class is the SPMs and SPM-mimetic receptor agonists.

---

## 2. Biosynthesis — How SPMs Are Made

SPMs are enzymatic products of polyunsaturated fatty acids (PUFAs) released from membrane phospholipids by cPLA2α and iPLA2. The precursor pool and enzyme set determine the product class.

### 2.1 Substrates

| Substrate | Carbon:double bonds | Dietary source | Downstream SPM class |
|---|---|---|---|
| **Arachidonic acid (AA)** | 20:4 ω-6 | Meat, eggs, vegetable oils (inflammatory bulk) | Lipoxins (LXA4, LXB4); also pro-inflammatory LTB4, PGE2 — shared pool |
| **EPA (eicosapentaenoic acid)** | 20:5 ω-3 | Fatty fish, algae oil, krill | E-series resolvins (RvE1, RvE2, RvE3) |
| **DHA (docosahexaenoic acid)** | 22:6 ω-3 | Fatty fish, algae oil | D-series resolvins (RvD1-D5), Protectins (PD1/NPD1, PDX), Maresins (MaR1, MaR2) |
| **n-3 DPA (docosapentaenoic)** | 22:5 ω-3 | Fish, intermediate metabolite | RvD_n-3DPA, MaR_n-3DPA, PD_n-3DPA series (parallel family) |

Key tension: AA and EPA compete for the same 5-LOX / COX / CYP enzymes. Dietary ω-3 loading shifts substrate occupancy *away from* AA-derived pro-inflammatory products (LTB4, PGE2) and *toward* EPA-derived resolution products (RvE1) — a substrate-competition mechanism independent of the pathway switch. This is the CP6a ↔ CP5b bridge: omega-3 acts twice, once by diverting 5-LOX away from LTB4 (CP6a — see [nlrp3-exploit-map.md §CP6a](./nlrp3-exploit-map.md)), and once by supplying SPM substrate (CP5b here).

### 2.2 Enzymes and intermediates

The SPM biosynthetic map (simplified — actual tissue biology has more branching and cell-type-specific handoffs):

```text
EPA (20:5) ──5-LOX/CYP450──▶ 18-HEPE ──5-LOX──▶ 5S,12R,18R-trihydroxy-EPA = RvE1
                                    └──15-LOX──▶ RvE2, RvE3

DHA (22:6) ──15-LOX──▶ 17S-HpDHA ──5-LOX──▶ RvD1, RvD2, RvD3, RvD4, RvD5
                    └─(aspirin-COX-2)──▶ 17R-HpDHA ──▶ 17R-RvD (AT-RvD) series
                    ──12-LOX──▶ 14-HpDHA ──▶ MaR1 (7,14-diHDHA), MaR2
                    ──epoxide hydrolase──▶ PD1/NPD1, PDX (protectins)

AA (20:4) ──15-LOX/5-LOX──▶ LXA4, LXB4 (lipoxins)
        ──(aspirin-COX-2)──▶ 15R-HETE ──5-LOX──▶ 15-epi-LXA4 (aspirin-triggered lipoxin)
```

Key enzymes and rate-limiting steps:

- **5-lipoxygenase (5-LOX, gene ALOX5):** Catalyzes 5-H(p)ETE from AA and 5-HpEPE from EPA. Also catalyzes trans-cell handoff to neighboring 15-LOX-expressing cells (endothelium, epithelium) in the classic "transcellular biosynthesis" mechanism for lipoxins and E-series resolvins.
- **12-lipoxygenase (12-LOX, gene ALOX12):** Platelet-type; catalyzes 14-HpDHA from DHA — the maresin precursor. Macrophages upregulate a functional 12-LOX-like activity during the resolution phase.
- **15-lipoxygenase (15-LOX, gene ALOX15):** Reticulocyte/eosinophil/macrophage-expressed; catalyzes 17-HpDHA from DHA (D-resolvin/protectin precursor) and 15-HpETE from AA (lipoxin precursor). ALOX15 expression is induced by IL-4/IL-13 on M2-polarized macrophages — a built-in positive feedback that reinforces the resolution program once it switches on.
- **CYP450 (especially CYP1A1, CYP2C/J isoforms):** Aspirin-acetylated COX-2 and various CYP450s generate 18R-HEPE from EPA (→ RvE1) and 17R-HpDHA from DHA (→ 17R-RvD series). These are the "R-epimer" or "aspirin-triggered" SPMs.
- **COX-2 (PTGS2):** Normally produces pro-inflammatory prostaglandins; **when acetylated by aspirin**, its catalytic pocket is modified to produce 15R-HETE instead of PGH2. This is the enzymatic basis for aspirin-triggered lipoxin / resolvin production.
- **Soluble epoxide hydrolase and other hydrolases:** Open epoxide intermediates (e.g., 17,18-epoxy-EPA, 13,14-epoxy-DHA) to form the dihydroxy and trihydroxy products that are the stable SPMs.

### 2.3 Intermediates as biomarkers

The stable mono- and di-hydroxy intermediates (17-HDHA, 18-HEPE, 14-HDHA) are the forms quantified in LC-MS/MS lipidomic panels and in commercial SPM precursor supplements. They are measurable at pg/mL levels in human plasma and shift reliably with fish-oil loading (Evidence level: In Vitro / Clinical — multiple supplementation trials, e.g., the "fish oil supplementation SPM plasma levels" literature). The fully-formed trihydroxy SPMs (RvD1, RvD2, MaR1) are lower-abundance, less stable, and more technically challenging to quantify.

### 2.4 Biosynthetic choreography across cells

A characteristic feature of SPM biosynthesis is **transcellular biosynthesis** — intermediates produced in one cell (e.g., 15-HpETE from endothelial 15-LOX) are transferred to a neighboring cell (e.g., 5-LOX in neutrophils) to complete the synthesis. This couples SPM production to tissue context (presence of the right cell partners) and is one reason why pharmacologic reconstitution with exogenous SPMs is not a perfect substitute for endogenous production — the signal is already spatially pre-positioned at the site of inflammation.

(Evidence level: In Vitro — characterized primarily in Serhan-lab lipidomic studies; textbook biochemistry.)

---

## 3. Individual SPM Families

### 3.1 E-series resolvins (EPA-derived)

**Members:** RvE1 (5S,12R,18R-trihydroxy-EPA), RvE2 (5S,18-dihydroxy-EPA), RvE3 (17R,18R-dihydroxy-EPA).

**Primary receptors:** **ChemR23 (CMKLR1)** — agonist; **BLT1** — partial antagonist (RvE1 displaces LTB4 from BLT1, effectively pushing the neutrophil away from the chemotactic gradient).

**Cell types:** Neutrophils (BLT1 expression), monocytes/macrophages (CMKLR1), dendritic cells.

**Effector profile:**
- Stops neutrophil chemotaxis and transmigration (BLT1 antagonism + CMKLR1 agonism)
- Promotes macrophage phagocytosis of apoptotic neutrophils (efferocytosis)
- Reduces IL-12 from dendritic cells — dampens adaptive inflammatory amplification

**Half-life:** Short (minutes to low hours in tissue; inactivated by ω-oxidation and dehydrogenation).

**Structure sketch:** Conjugated triene in the middle of a 20-carbon chain with three hydroxyls at 5, 12, 18; S,R,R stereochemistry for RvE1 (the natural isomer).

(Evidence level: In Vitro + Animal Model — multiple Serhan-lab and follow-up papers.)

### 3.2 D-series resolvins (DHA-derived)

**Members:** RvD1 (7S,8R,17S-trihydroxy-DHA), RvD2 (7S,16R,17S-trihydroxy-DHA), RvD3 (4S,11R,17S-trihydroxy-DHA), RvD4 (4S,5R,17S-trihydroxy-DHA), RvD5 (7S,17S-dihydroxy-DHA).

**Primary receptors:**
- **RvD1 →** ALX/FPR2 (high affinity) and GPR32 (DRV1)
- **RvD2 →** GPR18 (DRV2) — confirmed with selective GPR18 antagonist reversal ([Lopategi 2018 DOI](https://doi.org/10.1002/JLB.3HI0517-206RR), PMID 29601102)
- **RvD3/D5 →** GPR32 (lower affinity)
- **RvD4 →** receptor less well-characterized; candidate GPR32

**Aspirin-triggered epimers:** 17R-RvD (AT-RvD1, AT-RvD3) with 17R rather than 17S stereochemistry. Generated via aspirin-acetylated COX-2 → 17R-HpDHA → 17R-RvD. Equally potent or moderately more potent at the same receptors, with different PK (somewhat longer plasma half-life because the R-epimer is a poorer substrate for the endogenous inactivating dehydrogenase 15-PGDH).

**Cell types:** Monocytes, macrophages (high expression of ALX/FPR2, GPR32, GPR18), neutrophils (ALX/FPR2), T cells (low), nociceptor sensory neurons (a key finding of [Zaninelli 2022](https://doi.org/10.1111/bph.15897), PMID 35716378).

**Effector profile:**
- RvD1: blocks neutrophil chemotaxis; switches macrophages M1 → M2; reduces IL-1β, TNF, IL-6; in gouty arthritis, reduces CGRP release from nociceptors (Zaninelli 2022)
- RvD2: blocks ASC oligomerization and NLRP3 inflammasome assembly in BMDMs (Lopategi 2018, via GPR18); reduces IL-1β; promotes M2 markers (CD206, arginase-1) in peritoneal macrophages
- RvD3/D5: primarily efferocytosis-promoting and cytokine-dampening

**Half-life:** Short (minutes to low hours), unless R-epimer (marginally longer).

**Structure sketch:** 22-carbon backbone with conjugated triene/tetraene system and two to three hydroxyls; characteristic S,R,S trihydroxy pattern for RvD1.

(Evidence level: In Vitro + Animal Model — Lopategi 2018 is the direct RvD2 → GPR18 → NLRP3 blockade paper.)

### 3.3 Protectins (DHA-derived)

**Members:** PD1/NPD1 (10R,17S-dihydroxy-DHA — "neuroprotectin D1" in neural tissue), PDX (10S,17S-dihydroxy-DHA — stereoisomer, separate biology).

**Primary receptor:** **GPR37** has emerged as a functional PD1/NPD1 receptor on macrophages and neurons ([DOI 10.1016/j.neuron.2017.04.022](https://doi.org/10.1016/j.neuron.2017.04.022) and subsequent work; PMID 40287118 is a recent GPR37 review). The receptor identification is more recent and less fully characterized than for RvD1/RvD2.

**Cell types:** Neurons (high), microglia, macrophages, epithelial cells.

**Effector profile:**
- Blocks neutrophil transmigration
- Strongly neuroprotective — reduces inflammatory pain, protects neurons from excitotoxic and ischemic damage (the NPD1 literature)
- Reduces IL-1β and COX-2 in activated macrophages (Caron 2019 in equine synoviocytes — see §6.4)

**Half-life:** Short; less stable than resolvins.

**Structure:** 22-carbon with conjugated triene and two hydroxyls; the E/Z geometry around the triene distinguishes PD1 from PDX.

(Evidence level: In Vitro — receptor-ligand biology still being refined.)

### 3.4 Maresins (DHA-derived)

**Members:** MaR1 (7R,14S-dihydroxy-DHA), MaR2 (13R,14S-dihydroxy-DHA).

**Primary receptors:** **LGR6** (canonical MaR1 receptor), plus CMKLR1 at low affinity. Recent papers ([DOI 10.1016/j.immuni.2020.04.013](https://doi.org/10.1016/j.immuni.2020.04.013) and follow-up, e.g., PMIDs 40516692, 40139646, 38718314) extend and refine LGR6 + MaR1 biology.

**Cell types:** Macrophages (high LGR6 on resolution-phase macrophages), platelets (12-LOX biosynthetic machinery), osteoblasts, cardiomyocytes (emerging tissue roles).

**Effector profile:**
- Potently promotes macrophage efferocytosis
- Drives M1 → M2 macrophage switch
- Promotes tissue regeneration (the "M" in "maresin" = **M**acrophage-derived mediator of inflammation **res**olution)
- In gout specifically: **upregulates Prdx5 → AMPK/Nrf2 signaling → NLRP3 suppression** ([Jiang 2023 DOI](https://doi.org/10.1186/s10020-023-00756-w), PMID 37996809). This is distinct from the RvD1 → ALX/FPR2 axis — MaR1 works via an intracellular antioxidant / metabolic-homeostasis arm.

**Half-life:** Short.

**Structure:** 22-carbon with conjugated triene and two hydroxyls (7R,14S for MaR1); the R,S stereochemistry and the 7,14 positional arrangement are defining.

(Evidence level: In Vitro + Animal Model — Jiang 2023 is the direct MSU gout validation.)

### 3.5 Lipoxins (AA-derived)

**Members:** LXA4 (5S,6R,15S-trihydroxy-EET), LXB4 (5S,14R,15S-trihydroxy-EET). Aspirin-triggered 15-epi-LXA4 (**AT-LXA4**, 15R-epimer) is the aspirin-specific product of acetylated COX-2 + 5-LOX.

**Primary receptor:** **ALX/FPR2** (a.k.a. lipoxin A4 receptor / formyl peptide receptor 2). LXA4 is the prototypic ALX/FPR2 ligand. LXB4 has a distinct, poorly-characterized receptor profile.

**Cell types:** Broadly expressed — neutrophils (high), monocytes/macrophages, T cells, epithelial cells, vascular smooth muscle.

**Effector profile:**
- Blocks neutrophil chemotaxis and adhesion
- Inhibits pro-inflammatory cytokine production
- Promotes non-phlogistic efferocytosis (macrophages clear dead neutrophils without further inflammation)
- Suppresses ROS generation
- Modulates T cell and NK cell responses

**Half-life:** Very short (LXA4 is a poor substrate for 15-PGDH inactivation compared to some resolvins; AT-15-epi-LXA4 is more stable — another reason aspirin-triggered lipoxin is pharmacologically more useful than native LXA4).

**Structure:** 20-carbon conjugated tetraene with three hydroxyls.

(Evidence level: In Vitro + Animal Model — the earliest-characterized SPM family, Serhan and Samuelsson 1984 onward.)

### 3.6 Comparison table

| Family | Substrate | Key members | Primary receptor(s) | Defining effector |
|---|---|---|---|---|
| E-resolvins | EPA | RvE1, RvE2, RvE3 | CMKLR1/ChemR23 + BLT1 (antagonist) | Neutrophil chemotaxis stop |
| D-resolvins | DHA | RvD1-D5 | ALX/FPR2, GPR32, GPR18 | Macrophage M2 switch; NLRP3 block |
| Protectins | DHA | PD1/NPD1, PDX | GPR37 (emerging) | Neuroprotection; cytokine suppression |
| Maresins | DHA | MaR1, MaR2 | LGR6 | Efferocytosis; tissue regeneration; Prdx5/AMPK |
| Lipoxins | AA | LXA4, LXB4, AT-15-epi-LXA4 | ALX/FPR2 (LXA4) | Non-phlogistic efferocytosis; broad |
| Aspirin-triggered D-resolvins | DHA + aspirin-COX-2 | 17R-RvD series | Same receptors as native RvD | Longer PK (resistant to 15-PGDH) |
| Aspirin-triggered lipoxin | AA + aspirin-COX-2 | 15-epi-LXA4 | ALX/FPR2 | Longer PK; equipotent |
| n-3 DPA series | DPA | RvD_n-3DPA, MaR_n-3DPA | Presumed shared with DHA series | Parallel family; less well-characterized |

---

## 4. Receptor Biology

### 4.1 ALX/FPR2 — the canonical pro-resolving receptor

**Gene:** FPR2 (HGNC:3827, chromosome 19q13.4). **Protein:** 351 aa, 7-TM class A GPCR. **ChEMBL target:** [CHEMBL4550](https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4550) (the canonical FPR2/ALX entry).

**Endogenous ligands — a context-dependent menu:**
- **Pro-resolving lipids:** LXA4, AT-15-epi-LXA4, RvD1
- **Pro-resolving proteins:** Annexin A1 (AnxA1) — another major endogenous ALX/FPR2 agonist
- **Pro-inflammatory peptides:** Serum amyloid A (SAA), urokinase-type plasminogen activator receptor (uPAR) peptide, amyloid-β peptide, mitochondrial-derived formyl peptides
- **Implication:** The same receptor binds pro-resolving and pro-inflammatory ligands. Which signaling branch dominates depends on **biased agonism** and **cellular context** (which G-proteins and β-arrestins are available, which co-receptors are on the surface, cell activation state). This is why saying "ALX/FPR2 is a pro-resolving receptor" is an oversimplification — it is more accurately "a receptor whose pro-resolving vs. pro-inflammatory output is under ligand-selective and context-selective control."

**G-protein coupling:** Primarily Gαi (inhibits cAMP), with varying β-arrestin recruitment depending on ligand. Lipid-mediator agonism (LXA4, RvD1) tends to favor β-arrestin pathways associated with resolution; SAA-type agonism triggers more Gαi-dominated pro-inflammatory calcium flux and chemotaxis.

**Expression:** Neutrophils (high), monocytes/macrophages (high), dendritic cells, eosinophils, Th17 and Treg cells (induced), NK cells, epithelial cells (gut, lung, skin), vascular smooth muscle, platelets (low).

**Downstream of pro-resolving agonism:**
- cAMP inhibition → PKA suppression (competes with pro-inflammatory PKA-dependent signaling)
- β-arrestin-biased PI3K-γ suppression in neutrophils → chemotaxis arrest
- Nrf2 activation in macrophages → antioxidant program
- Efferocytosis receptor upregulation (MerTK, CD36, CD206)
- Suppression of NF-κB nuclear translocation downstream of pro-inflammatory stimuli

(Evidence level: In Vitro — extensively characterized; the context-dependence is a known complication of FPR2 pharmacology that has dogged drug development.)

### 4.2 GPR32 — the DRV1 receptor

**Gene:** GPR32. **Protein:** 365 aa, 7-TM class A GPCR. Human-specific; **no rodent ortholog** — GPR32 is a pseudogene in mouse and rat. This is one of the more significant species-gap issues in SPM pharmacology: murine RvD1 / RvD3 / RvD5 biology cannot act via GPR32 because the receptor does not exist in mouse; whatever function is observed in murine studies must act through ALX/FPR2 or another receptor. When translating rodent studies to human, GPR32 signaling is a gain in humans.

**Ligands:** RvD1, RvD3, RvD5; some evidence for RvD2 cross-binding.

**Signaling:** Gαi-coupled, β-arrestin recruitment. Downstream effects overlap with ALX/FPR2 (suppresses neutrophil chemotaxis, promotes efferocytosis).

**Expression:** Monocytes/macrophages, some T cell subsets, adipose tissue. Not widely characterized beyond leukocytes.

(Evidence level: In Vitro — limited structural biology; known only in human systems because of the rodent ortholog absence.)

### 4.3 GPR18 — the DRV2 (RvD2) receptor

**Gene:** GPR18. **Protein:** 331 aa, 7-TM. Also a known N-arachidonoylglycine receptor in some literature — another example of ligand promiscuity at SPM receptors.

**Ligands:** RvD2 (primary); N-arachidonoyl glycine (NAGly); partial MaR1 agonism reported in some systems.

**Signaling:** Gαi-coupled. In the Lopategi 2018 study ([DOI](https://doi.org/10.1002/JLB.3HI0517-206RR), PMID 29601102), a selective GPR18 antagonist **abrogated** RvD2's anti-NLRP3 effects in BMDMs, establishing GPR18 as the RvD2 receptor for NLRP3 inflammasome suppression.

**Expression:** Macrophages, some lymphocyte subsets, endothelium.

### 4.4 ChemR23 / CMKLR1 — the RvE1 receptor

**Gene:** CMKLR1 (Chemokine-Like Receptor 1). **Protein:** 373 aa, 7-TM. **ChEMBL target:** [CHEMBL5072](https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5072).

**Ligands:** RvE1 (primary), chemerin-derived peptides (competing ligand class — chemerin is pro-inflammatory, adding to the context-dependent dual agonism pattern seen at ALX/FPR2).

**Signaling:** Gαi-coupled. RvE1 activates Gαi while chemerin activation at the same receptor has distinct signaling bias — another biased-agonism system.

**Expression:** Macrophages, dendritic cells, NK cells, some neurons, adipocytes.

### 4.5 LGR6 — the MaR1 receptor

**Gene:** LGR6 (Leucine-rich repeat-containing G-protein coupled receptor 6). **Protein:** 967 aa (long extracellular domain). Originally a Wnt-pathway co-receptor; MaR1 agonism is distinct.

**Ligands:** MaR1 (primary lipid ligand); R-spondins (protein ligands — separate biology, Wnt signaling).

**Signaling:** Gαs/Gαi; cAMP modulation.

**Expression:** Macrophages (resolution-phase), skin stem cells, osteoblasts.

(Evidence level: In Vitro — LGR6 + MaR1 biology is a more recent addition; 2020 onward literature.)

### 4.6 GPR37 — the emerging protectin receptor

**Gene:** GPR37. **Protein:** 613 aa, 7-TM. Endogenous ligands include head activator peptide, prosaptide, **and PD1/NPD1** (emerging as a lipid ligand).

**Signaling:** Gαi-coupled; engages β-arrestin.

**Expression:** Central nervous system neurons (high), macrophages, oligodendrocytes.

(Evidence level: In Vitro — receptor-ligand relationship for protectins established ~2018-2020; several confirmatory papers 2020-2025.)

### 4.7 Comparative receptor table

| Receptor | Gene | Primary SPM ligand(s) | Non-SPM ligands | Cell types | Species caveat |
|---|---|---|---|---|---|
| ALX/FPR2 | FPR2 | LXA4, AT-15-epi-LXA4, RvD1 | AnxA1, SAA, uPAR peptide, Aβ | Broad leukocyte + epithelium | Rodent ortholog exists |
| GPR32 (DRV1) | GPR32 | RvD1, RvD3, RvD5 | — | Leukocytes | **Human-only; pseudogene in rodents** |
| GPR18 (DRV2) | GPR18 | RvD2 | NAGly | Macrophages | Rodent ortholog exists |
| CMKLR1 (ChemR23) | CMKLR1 | RvE1 | Chemerin | Macrophages, DCs | Rodent ortholog exists |
| LGR6 | LGR6 | MaR1 | R-spondins (Wnt) | Macrophages, stem cells | Rodent ortholog exists |
| GPR37 | GPR37 | PD1/NPD1 | Head activator, prosaptide | Neurons, macrophages | Rodent ortholog exists |

---

## 5. Functional Effects of SPMs — What They Actually Do

SPMs operate across the full arc of an inflammatory episode. The canonical "hallmarks of resolution" are:

### 5.1 Stop neutrophil infiltration

SPMs block three of the steps neutrophils need to reach tissue:
- **Rolling/tethering:** Reduce P-selectin/L-selectin avidity on neutrophil and endothelium
- **Adhesion:** Suppress LFA-1 / Mac-1 (CD11b) upregulation
- **Transmigration:** Block PECAM-1-mediated diapedesis and chemokine responsiveness

The CP6a link: RvE1 antagonizes BLT1 so neutrophils cannot respond to LTB4 gradients, effectively neutralizing the dominant neutrophil-amplification chemoattractant. This is a direct pro-resolving ↔ CP6a cross-talk at the receptor level.

### 5.2 Trigger neutrophil apoptosis and efferocytosis

SPMs accelerate neutrophil apoptosis (via Mcl-1 suppression in some assays) and simultaneously upregulate macrophage efferocytosis machinery (MerTK, CD36, GAS6/Protein S). The result: dead neutrophils are cleared by macrophages **without** secondary pro-inflammatory cytokine release ("non-phlogistic efferocytosis"). This is the switch between a productive resolution and a chronic-inflammation-promoting secondary necrosis.

### 5.3 Macrophage M1 → M2 phenotype switch

SPMs (especially RvD2 via GPR18, MaR1 via LGR6, and PD1/NPD1 via GPR37) drive macrophage reprogramming:
- Down: iNOS, TNFα, IL-6, IL-1β, IL-12
- Up: CD206 (mannose receptor), arginase-1, IL-10, TGF-β, MerTK (efferocytosis), Prdx5 (antioxidant)

The M1 → M2 switch is itself self-reinforcing through IL-4/IL-13 → ALOX15 induction → more SPM biosynthesis from the same macrophages. This is the positive feedback loop that locks in resolution once it starts.

### 5.4 Edema resolution and tissue repair

SPMs promote lymphatic drainage (clearing edema), endothelial barrier restoration, angiogenesis in the repair phase, and epithelial/fibroblast regeneration. This is the "rebuild" phase, distinct from the "stand down" phase.

### 5.5 Specific anti-NLRP3 mechanisms

The most important CP5b mechanism for gout:

- **RvD2 → GPR18 → block ASC oligomerization** in bone-marrow-derived macrophages (BMDMs) challenged with LPS + ATP or LPS + palmitate ([Lopategi 2018](https://doi.org/10.1002/JLB.3HI0517-206RR), PMID 29601102). RvD2 reduced pro-IL-1β expression and mature IL-1β secretion, and in thioglycolate-elicited peritoneal macrophages RvD2 reduced ASC oligomerization, inflammasome assembly, and caspase-1 activity. In vivo in self-resolving zymosan A peritonitis, RvD2 reduced IL-1β in exudates, suppressed osteopontin and MCP-1, and induced M2 markers (CD206, arginase-1). **Effects were abrogated by a selective GPR18 antagonist** — establishing GPR18 as the receptor.

- **MaR1 → Prdx5 upregulation → AMPK/Nrf2** → NLRP3 suppression in BMDMs and in vivo MSU peritonitis/arthritis models ([Jiang 2023](https://doi.org/10.1186/s10020-023-00756-w), PMID 37996809). Distinct mechanism from the RvD2 → ASC block.

- **RvD1 → disrupt nociceptor-macrophage communication** → reduce CGRP-dependent macrophage activation and MSU phagocytosis, reduce ASC speck formation and IL-1β ([Zaninelli 2022](https://doi.org/10.1111/bph.15897), PMID 35716378). Adds a **neuroimmune** axis to the CP5b story — SPMs don't just act on immune cells, they dampen the sensory neuron drive that primes the inflammation.

(Evidence level: Animal Model + In Vitro — all three papers are direct, gout-specific validations at CP5b.)

### 5.6 Preserved host defense — a critical distinction

Unlike immunosuppression, SPM signaling does **not** impair anti-microbial defense. In sepsis and bacterial infection models, SPMs accelerate bacterial clearance while resolving inflammation — the opposite of glucocorticoid or canakinumab-style suppression, which can impair host response. This is a defining feature of the pro-resolving class: resolution ≠ immunosuppression.

---

## 6. Gout-Specific Evidence (Direct MSU Models)

This is the most important evidence tier for the exploit map — **direct MSU-triggered gout animal data**, not extrapolation from other inflammatory models.

### 6.1 RvD1 — Zaninelli 2022 (PMID 35716378)

According to PubMed, Zaninelli TH, Fattori V, Saraiva-Santos T, et al. ["RvD1 disrupts nociceptor neuron and macrophage activation and neuroimmune communication, reducing pain and inflammation in gouty arthritis in mice."](https://doi.org/10.1111/bph.15897) *Br J Pharmacol* 2022;179(18):4500-4515. PMID 35716378. (Animal Model.)

**Model:** Male mice, intra-articular MSU (knee) induces gouty arthritis; mechanical hyperalgesia measured by electronic von Frey aesthesiometer. RvD1 administered intrathecally (CNS-targeted, to study sensory-neuron role) or intraperitoneally (systemic).

**Findings — dose- and time-dependent reductions in:**
- **Mechanical hyperalgesia** (primary pain readout)
- **Joint leukocyte recruitment** (knee joint wash counts + immunofluorescence)
- **Joint IL-1β production** (ELISA)
- **NF-κB phosphorylation** (immunofluorescence)
- **ASC oligomerization / speck formation** (immunofluorescence — CP3 in the exploit map)
- **CGRP expression and release** from peptidergic sensory neurons (EIA + immunofluorescence)
- **Macrophage MSU phagocytosis** (confocal microscopy) — mechanistic: CGRP stimulated MSU phagocytosis + IL-1β by macrophages; RvD1 blocked both the CGRP release upstream and the macrophage response downstream

**Key insight — the nociceptor-macrophage-CGRP axis:** Zaninelli 2022 uncovered a previously-uncharacterized neuroimmune loop in gouty arthritis — peptidergic sensory neurons release CGRP, which stimulates macrophages to phagocytose MSU more aggressively and produce more IL-1β. RvD1 disrupts this loop both at the neuron (reducing CGRP release) and at the macrophage (blocking CGRP-dependent IL-1β). This is one of the first examples of an SPM directly targeting the neuron-immune cross-talk in a crystalopathy and suggests that SPM pharmacology in gout is **not just an anti-inflammatory effect but an anti-pain effect** — clinically meaningful given how refractory gout pain is.

### 6.2 MaR1 — Jiang 2023 (PMID 37996809)

According to PubMed, Jiang H, Song D, Zhou X, et al. ["Maresin1 ameliorates MSU crystal-induced inflammation by upregulating Prdx5 expression."](https://doi.org/10.1186/s10020-023-00756-w) *Mol Med* 2023;29(1):158. PMID 37996809. (Animal Model + In Vitro.)

**Models:**
- In vitro: BMDMs pretreated with MaR1, stimulated with palmitic (C16:0) + stearic (C18:0) fatty acids + MSU crystals (FA + MSUc model)
- In vivo: MSUc-induced peritonitis and arthritis in mice; MaR1 treatment or Prdx5 deficiency (genetic) arms

**Mechanism:**
1. FA + MSUc decreased Prdx5 (peroxiredoxin 5) mRNA and protein
2. MaR1 reversed the Prdx5 decrease
3. MaR1 acted via the **Keap1-Nrf2 signaling axis** to upregulate Prdx5 transcription
4. Prdx5 then activated **AMPK** → improved TXNIP/TRX homeostasis → alleviated mitochondrial fragmentation → reduced NLRP3 activation
5. Prdx5 also inhibited CPT1A → reduced fatty acid oxidation (FAO) and urea-cycle dysfunction that drive the sterile inflammatory response

**Key insight:** MaR1 operates **upstream** of NLRP3 via an antioxidant/metabolic pathway (Keap1-Nrf2-Prdx5-AMPK), distinct from RvD1's neuroimmune axis and RvD2's direct ASC-oligomerization block. The three SPMs converge on NLRP3 via three different upstream routes — architecturally redundant, which is favorable for clinical robustness.

### 6.3 Lopategi 2018 — RvD2 and ASC oligomerization (broader mechanism, gout-relevant)

According to PubMed, Lopategi A, Flores-Costa R, Rius B, et al. ["Frontline Science: Specialized proresolving lipid mediators inhibit the priming and activation of the macrophage NLRP3 inflammasome."](https://doi.org/10.1002/JLB.3HI0517-206RR) *J Leukoc Biol* 2018;105(1):25-36. PMID 29601102. (In Vitro + Animal Model.)

**Findings:**
- RvD2 suppressed pro-IL-1β and mature IL-1β in BMDMs with LPS + ATP (classical NLRP3 model) and LPS + palmitate (lipotoxic model)
- In peritoneal macrophages, RvD2 **reduced ASC oligomerization, inflammasome assembly, and caspase-1 activity**
- In vivo zymosan A peritonitis: RvD2 reduced IL-1β in exudates, suppressed osteopontin and MCP-1, induced M2 markers (CD206, arginase-1)
- A **selective GPR18 antagonist abrogated** RvD2 effects — establishing the receptor

**Gout relevance:** Though not an MSU-specific model, this is the mechanistic core of RvD2's NLRP3-blocking activity and establishes the **GPR18 → ASC oligomerization block** pathway that plausibly generalizes to MSU-induced NLRP3 activation. Combined with Jiang 2023 (MSU-specific MaR1 effect) and Zaninelli 2022 (MSU-specific RvD1 effect), this paper anchors the mechanistic branch of CP5b.

### 6.4 Caron 2019 — SPM effects in IL-1β-stimulated equine synoviocytes (PMID 30836143)

According to PubMed, Caron JP, Gandy JC, Brown JL, Sordillo LM. ["Omega-3 fatty acids and docosahexaenoic acid oxymetabolites modulate the inflammatory response of equine recombinant interleukin1β-stimulated equine synoviocytes."](https://doi.org/10.1016/j.prostaglandins.2019.02.007) *Prostaglandins Other Lipid Mediat* 2019;142:1-8. PMID 30836143. (In Vitro.)

**Findings:**
- Equine synoviocytes pretreated with EPA or DHA + reIL-1β showed reduced ADAMTS4, MMP-1, MMP-13, IL-1β, IL-6, COX-2 expression
- **The docosanoids RvD1, RvD2, MaR1, and PDX — alone and in combination — abrogated ADAMTS4, MMP-1, MMP-13, and IL-6 expression** in IL-1β-stimulated synoviocytes
- **RvD1, RvD2, and MaR1 suppressed COX-2 expression**

**Gout relevance:** This is not a crystal-arthritis model but it demonstrates that D-resolvins, maresin, and protectin suppress the exact cytokine and matrix-degrading-enzyme profile (IL-1β, IL-6, COX-2, MMPs) that characterizes the gout synovium. The equine model is physiologically closer to the human joint than murine peritonitis. Combined with the murine MSU data (§6.1, §6.2), the synoviocyte evidence strengthens the mechanistic case that CP5b SPMs would work at the gouty joint.

### 6.5 Zaninelli 2023 Review (PMID 37651647)

According to PubMed, Zaninelli TH, Martelossi-Cebinelli G, Saraiva-Santos T, et al. ["New drug targets for the treatment of gout arthritis: what's new?"](https://doi.org/10.1080/14728222.2023.2247559) *Expert Opin Ther Targets* 2023;27(8):679-703. PMID 37651647. (Review.)

This review from the same group as Zaninelli 2022 **explicitly names ALX/FPR2 agonism as one of four priorities for gout drug development**, alongside (1) repurposing of existing therapies, (2) multitarget natural products, and (3) targeting the neuroinflammatory component of GA. The review notes that only ~4.4% of registered clinical trials for gout target natural products or "current hot targets" — a massive gap between the preclinical literature (which is rich in SPM validation) and clinical development (which is almost nothing).

### 6.6 Flag — no human gout trials with SPMs

As of 2026-04-24, **no clinical trial of any SPM or ALX/FPR2 agonist in gout has been registered or reported**. This is a clean literature gap, not a search artifact. The preclinical evidence is strong (Zaninelli 2022, Jiang 2023, Lopategi 2018, Caron 2019); the clinical evidence is absent. An investigator-initiated Phase 1/2 of oral fish-oil-derived SPMs or aspirin-triggered resolvins in recurrent-flare gout would be the shortest path to human validation.

---

## 7. Complement-Resolution Link — aggNETs as the Physical Substrate of Gout Resolution

### 7.1 Schauer 2014 — the foundational observation

According to PubMed, Schauer C, Janko C, Munoz LE, et al. ["Aggregated neutrophil extracellular traps limit inflammation by degrading cytokines and chemokines."](https://doi.org/10.1038/nm.3547) *Nat Med* 2014;20(5):511-7. PMID 24784231. (In Vitro + Animal Model + Clinical histopathology.)

**Findings:**
- Neutrophils recruited to MSU inflammation undergo oxidative burst and form NETs
- At **high neutrophil density**, NETs **aggregate** (aggNETs) and their associated serine proteases (neutrophil elastase, cathepsin G) **degrade cytokines and chemokines** in the extracellular space
- **Tophi share morphological and biochemical characteristics with aggNETs** — tophi are, on this view, chronic aggregated-NET structures representing a resolution attempt that never completed
- **NETosis-deficient mice** develop exacerbated and chronic neutrophilic inflammation; adoptive transfer of pre-formed aggNETs reduces the disease

### 7.2 Why this matters for CP5b

- aggNET formation depends on adequate local SPM signaling to **switch** neutrophil death from spreading NETs (which drive tissue damage) to aggregating NETs (which absorb and degrade the inflammatory soup)
- SPM deficit → NETs spread rather than aggregate → prolonged flare, chronic tissue damage, possibly failed tophus formation (paradoxically, tophi are the "successful" chronic aggNET resolution endpoint; failed aggregation may produce even worse disease)
- **Tophi are frozen resolution attempts.** In this model, they are the body's chronic attempt to sequester a stimulus it cannot clear (crystals) within an aggNET-like structure
- CP5b (SPM signaling) is therefore mechanistically upstream of both **acute flare resolution** and **chronic tophus formation** — two faces of the same process

### 7.3 The CP0 → CP6a → CP5b loop

Cross-link with [complement-c5a-gout.md](./complement-c5a-gout.md):

1. **CP0:** MSU activates complement → C5a generated → neutrophil recruitment
2. **CP6a:** Neutrophils arrive, amplify via LTB4 / 5-LOX
3. **CP5b:** Adequate SPM signaling → neutrophils aggNET → cytokines/chemokines sequestered → C5a locally degraded (anaphylatoxins are peptides, susceptible to neutrophil serine proteases)
4. **Loop closure:** aggNET-mediated C5a degradation reduces further CP0 priming → self-limiting flare
5. **Failure mode:** Insufficient SPM → NETs spread → no aggregation → C5a persists → flare continues → chronic phase → tophus formation as backup resolution attempt

This is a mechanistically elegant closed loop. It also predicts that **CP0 blockade (avacopan) and CP5b enhancement (SPMs) are complementary, not redundant** — avacopan blocks the incoming signal, SPMs accelerate the outgoing resolution. A combination should be additive.

### 7.4 The SPM / aggNET context switch

One unresolved question: what determines whether NETs spread (tissue damage) vs. aggregate (resolution)? The Schauer 2014 data points to neutrophil density as a major determinant, but SPM signaling is almost certainly another. In vitro, SPMs promote aggregation in cell-density-dependent assays, but the molecular switch is not fully characterized. This is an open mechanistic question (§13 #6).

---

## 8. Kinetics of Resolution

Resolution is not instantaneous. It has its own timescale and measurable kinetic parameters.

### 8.1 Timescales

- **Self-limited acute inflammation:** Resolution begins within hours of the stimulus peak and completes over 24-72 hours (dermal sterile inflammation, self-resolving peritonitis). With adequate SPM signaling, neutrophil counts peak at 4-8 h and decline to baseline by 24-48 h in murine zymosan peritonitis.
- **Gout flare:** Typical human gout flare resolves in 7-14 days untreated, faster with NSAID/colchicine/steroid. This is an order of magnitude slower than dermal sterile inflammation — reflecting both the persistent crystal stimulus and possibly sub-optimal SPM signaling at the joint.
- **Failed resolution — chronic inflammation:** Tophaceous gout, rheumatoid synovitis, atherosclerosis, chronic liver disease. Weeks to years. The inflammatory infiltrate persists because the resolution program fails to switch on at sufficient magnitude.

### 8.2 Resolution-index metrics

A quantitative framework for resolution kinetics (Bannenberg/Serhan et al., multiple methodological papers):

| Metric | Definition | Interpretation |
|---|---|---|
| **Ψmax** (PMN max) | Peak neutrophil count in the exudate | Magnitude of the inflammatory response |
| **Tmax** | Time to peak PMN count | Speed of recruitment |
| **T50** | Time for PMN count to decline to 50% of Ψmax | **Resolution speed — the key SPM-sensitive parameter** |
| **Ri** (resolution interval) | Tmax to T50 — the "resolution window" | Direct measurement of how fast resolution is |
| **LB_max** | Leukocyte burden, integrated over time | Total inflammatory impact |

Shortening T50 (faster decline of the PMN infiltrate) is the classic SPM pharmacodynamic signal in animal models. RvE1, RvD1, RvD2, MaR1, PD1 all shorten T50 in murine peritonitis and dermatitis models at nanomolar-to-low-microgram doses.

### 8.3 Application to gout

Gout flares don't readily permit Ψmax/T50 measurement in humans (invasive joint aspiration at multiple timepoints is not ethically feasible outside a dedicated trial). Surrogate clinical endpoints are:
- **Time to 50% pain reduction** (typically 24-48 h on NSAID; unknown on SPM)
- **Time to normalization of joint swelling**
- **Duration of flare** (patient-reported days of disability)
- **Flare recurrence rate** over 6-12 months

An SPM clinical trial in gout could pre-register "time to 50% pain reduction" as the resolution-proxy endpoint, analogous to Ri in animal models.

(Evidence level: Mechanistic Extrapolation — the Ψ/T50 framework is well-validated in animal models; its human gout translation is untested.)

---

## 9. "Absence of Resolution as Exploit" — Philosophical Framing

Most anti-inflammatory drugs work by **suppression**:
- NSAIDs block COX-1/COX-2 → less PGE2, less pain signaling
- Corticosteroids activate the glucocorticoid receptor → broad transcriptional suppression of inflammatory genes (also of resolution genes — steroids paradoxically can *impair* resolution)
- Canakinumab/anakinra/rilonacept block IL-1β signaling → no downstream inflammatory amplification (CP5a)
- TNF inhibitors block TNFα → reduce cytokine storm

SPMs and SPM-inducers operate through a **different mechanism class**: they *promote* the active resolution program rather than *blocking* the inflammation. Key consequences:

1. **Combination is additive, not redundant.** Allopurinol (crystal elimination upstream) + canakinumab (IL-1β suppression, CP5a) + SPM (resolution at CP5b) operate at three independent layers and should stack cleanly.
2. **Preserved host defense.** SPM-promoted resolution does not impair anti-microbial response (see §5.6). Unlike IL-1β blockade, which carries a real infection risk, SPMs appear neutral or mildly protective in sepsis models.
3. **Tissue repair.** SPMs actively promote tissue regeneration (§5.4). Suppression-only drugs do not — they simply reduce ongoing damage. In chronic tophaceous joints, this distinction could be disease-modifying.
4. **Different side-effect profile.** No evidence SPMs cause immunosuppression, GI ulceration (unlike NSAIDs), osteoporosis (unlike steroids), or weight gain (unlike steroids). The "dirty" side-effect profile of fish oil is GI (fishy reflux, mild diarrhea at high doses) and, at very high doses, minor increases in bleeding time.
5. **Pharmacologic class-distinct from what most of the stack covers.** The Open Enzyme stack is predominantly suppression-class (EGCG, curcumin, quercetin, sulforaphane — all NF-κB / ROS suppressors). Adding SPMs (via omega-3 loading or direct SPM supplements) is the stack's resolution arm.

The framing: **"You can't fight your way out of gout by suppression alone. You have to switch on resolution."**

---

## 10. Dose, Delivery, Supplementation

### 10.1 Omega-3 precursor loading

**Typical dose for anti-inflammatory / pro-resolution effect:** 3-4 g/day combined EPA + DHA. Below ~2 g/day, effects are marginal; above ~4 g/day, diminishing returns and increased GI/bleeding risk.

**Conversion efficiency to SPMs:** Estimated 5-10% of precursor pool is enzymatically converted to SPMs at rest. Higher during active inflammation (when 5-LOX/15-LOX/12-LOX are upregulated). Bioavailability depends on formulation (triglyceride > ethyl ester > phospholipid in some studies; re-esterified triglyceride preferred for absorption).

**DHA-emphasis for gout — the key nuance (per round 2 synthesis commit 1d720b2):**
The direct MSU-gout animal evidence at CP5b is **DHA-derived, not EPA-derived**:
- RvD1 (DHA → ALX/FPR2) — Zaninelli 2022 PMID 35716378
- MaR1 (DHA → LGR6) — Jiang 2023 PMID 37996809
- RvD2 (DHA → GPR18) — Lopategi 2018 PMID 29601102 (not MSU but the mechanistic core)
- PDX / PD1 (DHA → GPR37) — Caron 2019 PMID 30836143 (equine synoviocytes)

Separately, DHA correlates with lower circulating TNFSF14 in a Mendelian-randomization study (see [tnfsf14-gout-target.md](./tnfsf14-gout-target.md), Huang 2024 PMID 38235898), tying DHA to the CP1a (LIGHT amplifier) arm.

EPA is not inactive — EPA → RvE1 operates at CP5b (CMKLR1) and EPA substrate competition reduces LTB4 at CP6a. But for **gout-specific** use, the weight of direct MSU evidence is DHA. **Prefer DHA-emphasis or high-DHA formulations** (algae oil is often 2-3× higher DHA than EPA; most fish oils are EPA-dominant because they target cardiovascular endpoints).

Practical dosing: 2-3 g DHA + 1-2 g EPA/day is a reasonable gout-targeted SPM precursor load. With food to improve absorption and reduce GI side effects.

### 10.2 Aspirin-triggered SPM

**Mechanism:** Low-dose aspirin (81 mg/day) acetylates COX-2 (irreversibly; 10-50% of circulating COX-2 is acetylated at steady state on 81 mg daily), shifting its product profile toward **15-epi-LXA4** (from AA) and **17R-RvD series** (from DHA via CYP450 + aspirin-COX-2 tandem). These R-epimers are equipotent or more potent at ALX/FPR2 / GPR32 / GPR18 and have **longer plasma half-lives** because 15-PGDH (the dehydrogenase that inactivates native S-epimer SPMs) processes R-epimers less efficiently.

**Practical upshot:** Adding low-dose aspirin to a DHA-loaded regimen **qualitatively shifts the SPM output** toward longer-lived R-epimer forms. This repositions "baby aspirin" from an anti-platelet drug into a **pro-resolution synergist**. The gout literature on aspirin is equivocal (some patients report benefit, mainstream guidelines have not endorsed); this provides a mechanistic rationale at CP5b, distinct from the anti-platelet mechanism.

**Caveats:**
- Aspirin and urate handling: aspirin at very low dose (<325 mg/day) paradoxically *increases* serum urate by inhibiting URAT1-mediated renal excretion; at high dose (>3 g/day) it is uricosuric. For gout, the 81 mg dose is in the urate-raising zone, a real if small concern
- Bleeding risk: 81 mg aspirin + fish oil at 3-4 g/day marginally increases bleeding time; not clinically significant for most patients but worth checking if any surgical plan is imminent
- Aspirin sensitivity / NSAID-induced respiratory disease: absolute contraindication

The combined "aspirin + fish oil" stack for SPM production is used in some functional-medicine practices; rigorous clinical evidence for gout specifically is absent.

### 10.3 Direct SPM supplements

**SPM Active (Metagenics)** and similar products (Specialized Pro-Resolving Mediators, SPM Supreme, etc.):
- Standardized to 17-HDHA, 18-HEPE, 14-HDHA — the **stable hydroxy intermediates** upstream of the fully-formed trihydroxy resolvins/maresins/protectins
- Typical dose: 2 softgels/day, providing a few hundred micrograms of mixed SPM precursors
- Cost: $80-120/month — expensive for a supplement, cheap relative to pharma SPM-mimetics
- Bypasses the precursor-conversion bottleneck (if the limiting step is substrate availability)
- Doesn't bypass the tissue-level biosynthetic machinery (still requires 5-LOX/15-LOX/CYP to convert intermediates to active SPMs)
- Clinical evidence is modest — mostly single-arm trials in chronic pain / post-surgical recovery showing reduced CRP and improved pain scores
- **No gout-specific data**

**Research-grade SPMs** (Cayman Chemical and similar vendors for RvD1, MaR1, RvE1) are available for preclinical work only; not clinically deployable (unstable, pg-mg quantities, no pharmacology-quality formulation).

### 10.4 Lactoferrin as an indirect SPM / resolution modulator

Lactoferrin promotes resolution through multiple overlapping mechanisms — iron sequestration, antimicrobial activity, macrophage modulation toward M2, and possible partial FPR2 engagement. See [lactoferrin.md](./lactoferrin.md) for the full dossier (engineering feasibility in *A. oryzae* at >2 g/L submerged culture per Ward 1995 PMID 9634791, recombinant human form data, and fermentation pathway). The overlap with SPM signaling is partial; lactoferrin is not a canonical SPM but it operates in the same functional space.

**Substrate-supply synergy with uricase (2026-05-05 addition; Speculative).** Beyond its resolution-adjacent role, lactoferrin has a mechanistically distinct second axis of synergy with the platform's primary urate-lowering mechanism: lactoferrin suppresses TNFα (Habib 2023 PMID 37926296; Animal Model), and TNFα suppresses intestinal ABCG2 (Ferrer-Picón 2020 PMID 31211831; In Vitro + clinical biopsy). The composed mechanism — Lf → ↓ TNFα → ↑ ABCG2 transport → ↑ luminal urate substrate → ↑ effective uricase activity — positions lactoferrin as a substrate-supply synergist for the gut-lumen-sink platform, not just a parallel NLRP3 modulator. This mechanism is **Speculative** (no published experiment in this combined geometry); the direct test is the lactoferrin rescue arm in [`validation-experiments.md §1.14`](./validation-experiments.md#114-additive-abcg2-suppression-by-androgens--tnfα--butyrate-rescue--lactoferrin-synergy). Full mechanistic write-up in [`lactoferrin.md §4.7`](./lactoferrin.md). (source: lactoferrin.md, koji-endgame-strain.md)

### 10.5 Pharma development — ALX/FPR2 agonism

**BMS-986235 (Bristol-Myers Squibb):** Small-molecule ALX/FPR2 agonist in clinical development for heart failure. Validates ALX/FPR2 as a pharmacologically tractable target but is not being developed for gout. ClinicalTrials.gov records confirm Phase 2 heart failure indication as of late 2024.

**Compound 43 / ACT-389949 (Actelion):** Small-molecule FPR2 agonist, Phase 1 tested in healthy volunteers; demonstrated target engagement (LPS challenge studies) but development status unclear post-Idorsia acquisition.

**No ALX/FPR2 agonist has been tested in gout clinical trials as of 2026-04.** A gout-repurposing trial of BMS-986235 or a similar compound would be the most direct pharma path to CP5b validation.

(Evidence level: Clinical Trial for BMS-986235 in heart failure; Mechanistic Extrapolation for gout.)

---

## 11. Engineered Production — What's Feasible

### 11.1 Direct SPM biosynthesis in yeast/koji

**The hard engineering problem:** SPMs are enzymatic products of long-chain polyunsaturated fatty acids (EPA, DHA, AA, n-3 DPA), which are not native to S. cerevisiae or A. oryzae in significant quantities. A fully-engineered SPM-producing yeast would need:

1. **Substrate engineering** — heterologous ω-3 desaturase pathway (elongase + Δ15 desaturase + Δ17 desaturase or equivalent) to produce EPA/DHA from native fatty acid precursors. Precedent exists: *Yarrowia lipolytica* has been engineered to produce EPA at commercial scale (~15% of dry cell weight as EPA) for aquaculture feed. The engineering is real but complex (6-10 heterologous enzymes, careful flux balancing to avoid lipid accumulation that stalls cell growth).
2. **SPM biosynthetic enzymes** — heterologous mammalian 5-LOX, 12-LOX, 15-LOX, specific CYP450s (CYP1A1, CYP2C/J), and epoxide hydrolase. Mammalian LOX enzymes have been expressed in yeast for biochemistry; SPM-specific tandem pathways less characterized.
3. **Product stability** — SPMs are labile (oxidation-prone, short-half-life lipids). Co-formulation with antioxidants would be required. Extraction yields from yeast biomass are untested.
4. **GRAS compatibility** — A. oryzae and S. cerevisiae are GRAS; Yarrowia is not yet GRAS for food use in the US (it is for some feed applications).

### 11.2 Realistic near-term path: precursor co-formulation

**Short-term (years 1-2):** EPA/DHA omega-3 co-formulation with uricase koji. No engineering required; leverages existing global omega-3 supply chain. This is **CP5b coverage at the substrate-loading level** — not direct SPM production but substrate provision at adequate titer to drive endogenous SPM biosynthesis.

Formulation logic: One daily dose of engineered koji uricase (crystal-eliminator, CP upstream) + one daily dose of DHA-emphasis omega-3 (SPM precursor for CP5b) + optional low-dose aspirin (aspirin-triggered SPM enhancement). Zero engineering burden on the SPM side; all the engineering complexity is on the uricase koji.

### 11.3 Medium-term: lactoferrin co-expression in koji (resolution-adjacent)

Lactoferrin in *A. oryzae* or *A. awamori* is a demonstrated-in-literature target (Ward 1992 PMID 1368268, Ward 1995 PMID 9634791, Sun 1999 PMID 10089347). Co-expressing lactoferrin alongside uricase in a single engineered koji strain would cover both upstream crystal elimination (uricase) and resolution-adjacent macrophage modulation (lactoferrin), without requiring SPM-direct biosynthesis. **See [lactoferrin.md](./lactoferrin.md) for the dedicated feasibility dossier.**

This is a more tractable near-term target than direct SPM biosynthesis in yeast, and it fills a complementary resolution niche (protein-based, macrophage-targeting) that SPMs (lipid-based, multi-receptor) do not fully cover.

### 11.4 Long-term: dedicated SPM-producing strain

A dedicated engineered SPM-producing strain is a **distinct project** from the uricase koji — probably better pursued as a separate chassis (e.g., engineered *Y. lipolytica* with a heterologous 15-LOX / 12-LOX / CYP1A1 pathway producing 17-HDHA / 14-HDHA / 18-HEPE precursors), formulated alongside the uricase koji. This is years 5+ research, not Phase 0.

### 11.5 Assessment — honest accounting

The engineered-koji platform covers CP5b **indirectly** (via lactoferrin if that co-expression clears feasibility, via downstream resolution signaling) but **not directly** (no native or near-native SPM production in GRAS yeast/koji). The practical CP5b stack for the Open Enzyme platform is:

1. **Substrate-loaded omega-3** (DHA-emphasis, 2-3 g DHA + 1-2 g EPA/day) — commercial, unengineered
2. **Engineered koji uricase + lactoferrin** (if co-expression feasibility clears) — platform-native, indirect CP5b via lactoferrin
3. **Aspirin-triggered shift** (low-dose aspirin, optional) — off-the-shelf, repositions SPM output toward longer-lived R-epimers
4. **Direct SPM supplements** (SPM Active or similar) — commercial supplement-grade
5. **Future: engineered SPM-producing yeast** (years 5+) — research-stage

This is an honest assessment. The platform has substrate loading, indirect resolution-modulator (lactoferrin), and commercial access to direct SPMs, but does **not** produce SPMs at enzyme-engineered scale. That's a tractable future project, not a current deliverable.

---

## 12. Clinical Biomarkers and Self-Experiment Relevance

### 12.1 Serum / plasma SPM measurement

**Method:** LC-MS/MS lipidomics. A typical panel quantifies RvD1, RvD2, RvD5, RvE1, MaR1, PD1, LXA4 (and occasionally AT-15-epi-LXA4 and 17R-RvD) at pg/mL levels in 100-500 μL plasma.

**Technical challenges:**
- Pre-analytic: plasma must be collected with antioxidants (e.g., BHT) to prevent ex vivo oxidation; rapid freezing at -80°C; avoidance of freeze-thaw cycles
- Analytic: requires a specialty lipidomics lab (typically academic core facilities or Metabolon/Core Metabolomics-style vendors)
- Cost: ~$300-700 per panel (research pricing; not reimbursable)
- Reference ranges: not well-established for gout; existing data come from healthy volunteers and chronic inflammatory disease cohorts

**Practical utility in gout:** Mostly research-setting. SPM panels during flare vs. inter-flare vs. on fish-oil loading would inform a specific patient's resolution signaling, but there's insufficient comparative data to act on a result clinically yet.

### 12.2 Urinary LTE4 (already in self-experiment §3)

Urinary LTE4 is a CP6a (5-LOX pathway) readout — indicates leukotriene production. **Inverse relationship with SPMs is expected**: high LTE4 + low SPMs indicates a pro-inflammatory 5-LOX/15-LOX ratio shifted toward LTB4/LTE4 (inflammation) vs. RvE1/lipoxin (resolution). Per [self-experiment-protocol.md §"Chokepoint-biomarker map"](./self-experiment-protocol.md#chokepoint-biomarker-map), urinary LTE4 is already in the planned assay panel. Pairing with an SPM plasma panel would let you compute a simple "resolution ratio" (e.g., RvE1/LTE4 or sum-SPM/LTE4) as a CP6a ↔ CP5b axis biomarker.

### 12.3 Surrogate clinical endpoints

For self-experiment or a future trial:
- **Time to 50% pain reduction** from flare onset — resolution speed proxy
- **Duration of flare** (hours/days)
- **Recurrence rate** over 6-12 months
- **Inter-flare pain baseline** (chronic low-grade pain/stiffness indexed)
- **hsCRP decline kinetics** from flare peak to baseline

### 12.4 Omega-3 index

The omega-3 index (% EPA + DHA in erythrocyte membranes) is a more stable measure of dietary/supplement omega-3 intake than plasma fatty acid panels. Target >8% for cardiovascular benefit; for SPM production, rising the index from ~4-5% (typical Western diet) to ~8-10% correlates with detectable increases in plasma SPMs. Commercial tests (OmegaQuant) at ~$50-100. This is a cheap, practical biomarker for "am I loading enough omega-3 substrate" before considering direct SPM panels.

---

## 13. Open Research Questions

1. **Why do gout patients' SPM levels remain low during flare?** Is there a specific SPM-biosynthesis deficit in chronic gout patients (dietary precursor shortage? 15-LOX/12-LOX expression defect? age-related decline in ALOX15?), or is the problem simply that demand outpaces production during acute flares? A lipidomic study of flare-phase vs. inter-flare plasma SPMs in the same patient (N=20-30, paired) would resolve this.
2. **ALX/FPR2 polymorphisms in gout.** Are there genetic variants of FPR2 associated with gout flare severity, tophi formation rates, or SPM response? An association study using existing gout biobank DNA is feasible.
3. **GPR18 variants and gout.** GPR18 is the RvD2 receptor (Lopategi 2018). Variants that alter RvD2 binding or signaling could predict resolution failure. No gout-specific GPR18 association study exists.
4. **SPM ratios in gout — which family dominates resolution?** Are gout-patient flares resolved primarily by D-resolvins, maresins, protectins, or a combination? A ratio-based biomarker could guide targeted supplementation (e.g., DHA-emphasis for D-resolvin-dominant resolvers vs. EPA emphasis for E-resolvin-dominant).
5. **Gout-specific ALX/FPR2 agonist (BMS-986235 or similar) trial.** No trial exists. An investigator-initiated Phase 2 in refractory gout is the shortest path to human validation.
6. **The aggNET-vs-spreading NET molecular switch.** What determines whether NETs aggregate (resolution) vs. spread (damage) beyond neutrophil density? Is SPM signaling the dominant modulator? Mechanistic dissection in human neutrophil cultures ± SPMs.
7. **Low-dose aspirin in gout — trial-worthy?** The aspirin-triggered SPM mechanism provides a specific rationale for low-dose aspirin as a pro-resolution adjunct in recurrent-flare gout, distinct from its anti-platelet role. A cross-over trial (N=30-50, aspirin 81 mg vs. placebo on a fish-oil background) measuring flare frequency would be low-cost.
8. **SPM Active supplement in gout.** No clinical trial has tested any commercial SPM supplement in gout. A single-arm pilot (N=20, SPM Active 2 softgels/day × 90 days, flare frequency + urinary LTE4 + omega-3 index + flare-phase plasma SPMs) would generate the first human gout-SPM data.
9. **DHA-vs-EPA dosing in gout.** The preclinical evidence favors DHA for gout (RvD1, MaR1 both DHA-derived). A head-to-head DHA-dominant vs. EPA-dominant vs. balanced fish-oil trial in recurrent-flare gout would clarify the optimal formulation. Marginal cost; high informational value.
10. **Resolution index (T50) measurement in human gout.** Can the animal-model Ψmax/T50 framework be adapted to clinical gout monitoring? Serial ultrasound joint imaging + synovial fluid sampling across a flare is invasive but feasible in a dedicated research setting. Would provide the first human resolution-kinetic measurement in a crystalopathy.
11. **Lactoferrin + SPM combination.** If engineered koji lactoferrin clears feasibility (see [lactoferrin.md](./lactoferrin.md)), the combination of koji lactoferrin + DHA-emphasis omega-3 would cover CP5b via two independent mechanisms (lactoferrin M2 macrophage polarization + SPM direct receptor agonism). A preclinical MSU-model combination study would test for additivity.
12. **Engineered SPM biosynthesis in yeast — feasibility scoping.** Which yeast chassis (Y. lipolytica for substrate, S. cerevisiae for enzyme library, A. oryzae for GRAS/koji platform) is the best fit for direct SPM production? A design-phase literature review and retrosynthetic analysis would frame the long-term research arm.

---

## 14. Sources (Annotated Bibliography)

### Direct MSU gout SPM evidence (the CP5b canon)

1. Zaninelli TH, Fattori V, Saraiva-Santos T, Badaro-Garcia S, Staurengo-Ferrari L, Andrade KC, Artero NA, Ferraz CR, Bertozzi MM, Rasquel-Oliveira F, Manchope MF, Amaral FA, Teixeira MM, Borghi SM, Rogers MS, Casagrande R, Verri WA Jr. "RvD1 disrupts nociceptor neuron and macrophage activation and neuroimmune communication, reducing pain and inflammation in gouty arthritis in mice." *Br J Pharmacol* 2022;179(18):4500-4515. [DOI: 10.1111/bph.15897](https://doi.org/10.1111/bph.15897). PMID: 35716378. **Direct MSU gout RvD1 effect via ALX/FPR2; neuroimmune nociceptor-macrophage-CGRP axis.**

2. Jiang H, Song D, Zhou X, Chen F, Yu Q, Ren L, Dai Q, Zeng M. "Maresin1 ameliorates MSU crystal-induced inflammation by upregulating Prdx5 expression." *Mol Med* 2023;29(1):158. [DOI: 10.1186/s10020-023-00756-w](https://doi.org/10.1186/s10020-023-00756-w). PMID: 37996809. **Direct MSU gout MaR1 effect via Prdx5 → AMPK/Nrf2 upstream of NLRP3.**

3. Lopategi A, Flores-Costa R, Rius B, López-Vicario C, Alcaraz-Quiles J, Titos E, Clària J. "Frontline Science: Specialized proresolving lipid mediators inhibit the priming and activation of the macrophage NLRP3 inflammasome." *J Leukoc Biol* 2018;105(1):25-36. [DOI: 10.1002/JLB.3HI0517-206RR](https://doi.org/10.1002/JLB.3HI0517-206RR). PMID: 29601102. **RvD2 → GPR18 → ASC oligomerization block in BMDMs; establishes GPR18 as the RvD2 receptor for NLRP3 suppression.**

4. Caron JP, Gandy JC, Brown JL, Sordillo LM. "Omega-3 fatty acids and docosahexaenoic acid oxymetabolites modulate the inflammatory response of equine recombinant interleukin1β-stimulated equine synoviocytes." *Prostaglandins Other Lipid Mediat* 2019;142:1-8. [DOI: 10.1016/j.prostaglandins.2019.02.007](https://doi.org/10.1016/j.prostaglandins.2019.02.007). PMID: 30836143. **RvD1, RvD2, MaR1, PDX suppress IL-1β-induced ADAMTS4, MMPs, IL-6, COX-2 in equine synoviocytes — joint-relevant target validation.**

5. Zaninelli TH, Martelossi-Cebinelli G, Saraiva-Santos T, Borghi SM, Fattori V, Casagrande R, Verri WA Jr. "New drug targets for the treatment of gout arthritis: what's new?" *Expert Opin Ther Targets* 2023;27(8):679-703. [DOI: 10.1080/14728222.2023.2247559](https://doi.org/10.1080/14728222.2023.2247559). PMID: 37651647. **Review explicitly naming ALX/FPR2 agonism as a gout therapeutic priority.**

### Complement-resolution link

6. Schauer C, Janko C, Munoz LE, Zhao Y, Kienhöfer D, Frey B, Lell M, Manger B, Rech J, Naschberger E, Holmdahl R, Krenn V, Harrer T, Jeremic I, Bilyy R, Schett G, Hoffmann M, Herrmann M. "Aggregated neutrophil extracellular traps limit inflammation by degrading cytokines and chemokines." *Nat Med* 2014;20(5):511-7. [DOI: 10.1038/nm.3547](https://doi.org/10.1038/nm.3547). PMID: 24784231. **aggNETs degrade cytokines/chemokines; tophi are chronic aggNET structures; foundational for the resolution-complement loop.**

### Foundational SPM biology

7. Serhan CN. "Pro-resolving lipid mediators are leads for resolution physiology." *Nature* 2014;510(7503):92-101. [DOI: 10.1038/nature13479](https://doi.org/10.1038/nature13479). PMID: 24899309. **Foundational SPM biology review by the field's originator.**

8. Serhan CN, Levy BD. "Resolvins in inflammation: emergence of the pro-resolving superfamily of mediators." *J Clin Invest* 2018;128(7):2657-2669. [DOI: 10.1172/JCI97943](https://doi.org/10.1172/JCI97943). **Modern SPM superfamily overview.**

### Receptor structure / function

9. Krishnamoorthy N, Abdulnour RE, Walker KH, Engstrom BD, Levy BD. "Specialized Proresolving Mediators in Innate and Adaptive Immune Responses in Airway Diseases." *Physiol Rev* 2018;98(3):1335-1370. [DOI: 10.1152/physrev.00026.2017](https://doi.org/10.1152/physrev.00026.2017). **Receptor and cell-type comprehensive review.**

10. Chiang N, Serhan CN. "Structural elucidation and physiologic functions of specialized pro-resolving mediators and their receptors." *Mol Aspects Med* 2017;58:114-129. [DOI: 10.1016/j.mam.2017.03.005](https://doi.org/10.1016/j.mam.2017.03.005). **Receptor identification and signaling biology.**

### Engineering and production

11. Xue Z, Sharpe PL, Hong SP, Yadav NS, Xie D, Short DR, Damude HG, Rupert RA, Seip JE, Wang J, Pollak DW, Bostick MW, Bosak MD, Macool DJ, Hollerbach DH, Zhang H, Arcilla DM, Bledsoe SA, Croker K, McCord EF, Tyreus BD, Jackson EN, Zhu Q. "Production of omega-3 eicosapentaenoic acid by metabolic engineering of Yarrowia lipolytica." *Nat Biotechnol* 2013;31(8):734-40. [DOI: 10.1038/nbt.2622](https://doi.org/10.1038/nbt.2622). **Yarrowia EPA production precedent — the existing industrial chassis for heterologous ω-3 biosynthesis.**

### Gout context

12. Cumpelik A, Ankli B, Zecher D, Schifferli JA. "Neutrophil microvesicles resolve gout by inhibiting C5a-mediated priming of the inflammasome." *Ann Rheum Dis* 2016;75(6):1236-45. [DOI: 10.1136/annrheumdis-2015-207338](https://doi.org/10.1136/annrheumdis-2015-207338). PMID: 26245757. **C5a as dominant priming signal; cross-link to [complement-c5a-gout.md](./complement-c5a-gout.md).**

### Lactoferrin (resolution-adjacent, engineering target)

13. Ward PP, Lo JY, Duke M, May GS, Headon DR, Conneely OM. "Production of biologically active recombinant human lactoferrin in Aspergillus oryzae." *Nat Biotechnol* 1992;10(7):784-789. [DOI: 10.1038/nbt0792-784](https://doi.org/10.1038/nbt0792-784). PMID: 1368268. **First mammalian glycoprotein in Aspergillus; 25 mg/L; α-amylase promoter + A. niger glucoamylase 3' region.**

14. Ward PP, Piddington CS, Cunningham GA, Chang N, Young RT, Conneely OM. "A system for production of commercial quantities of human lactoferrin: a broad spectrum natural antibiotic." *Nat Biotechnol* 1995;13(5):498-503. [DOI: 10.1038/nbt0595-498](https://doi.org/10.1038/nbt0595-498). PMID: 9634791. **>2 g/L in *A. awamori* as glucoamylase fusion + KEX-2 processed; classical strain improvement; retained iron binding, enterocyte-receptor binding, antimicrobial activity.**

15. Sun XL, Baker HM, Shewry SC, Jameson GB, Baker EN. "Structure of recombinant human lactoferrin expressed in Aspergillus awamori." *Acta Crystallogr D Biol Crystallogr* 1999;55(Pt 2):403-407. PMID: 10089347. **Confirmed native fold of Aspergillus-produced hLF.**

### Additional MeSH anchors (for connectivity, not exhaustively annotated)

16. MaR1 / LGR6 biology: additional 2020-2025 papers including PMIDs 40516692, 40139646, 38718314 (LGR6 receptor validation and follow-on).
17. GPR37 / protectin biology: PMID 40287118 and related 2020-2025 GPR37 ligand-identification literature.
18. GPR18 / RvD2 macrophage biology: PMIDs 40759181, 39490925, 39320982, 38608525, 38498346 (ongoing receptor-function studies).
19. Huang et al. 2024 (PMID 38235898) — Mendelian randomization linking DHA to lower circulating TNFSF14; cross-link at [tnfsf14-gout-target.md](./tnfsf14-gout-target.md).
20. Fish oil → plasma SPM dose-response in humans: PMIDs 38778807, 38003333, 37488250 (recent randomized and observational data).

### Regulatory / pharma development

21. BMS-986235 (Bristol-Myers Squibb) — small-molecule ALX/FPR2 agonist; Phase 2 in heart failure; ClinicalTrials.gov records 2022-2024. Validates ALX/FPR2 as a pharmacologically-tractable target.

22. SPM Active (Metagenics) — commercial SPM precursor supplement, standardized to 17-HDHA, 18-HEPE, 14-HDHA. Supplement-grade; no FDA drug approval; modest clinical evidence in chronic pain and post-surgical recovery; no gout-specific data.

---

*This page is part of the Open Enzyme research library. Phase 0 — Research and Design. No claims in this document constitute medical advice. All therapeutic discussion is research-stage. Citation attribution per PubMed terms of use — all DOIs included inline.*
