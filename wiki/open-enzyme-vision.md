---
title: Open Enzyme — Founding Vision
date: April 2026
tags: [enzyme deficits, therapeutic enzymes, GRAS organisms, uricase, digestive enzymes, koji, yeast engineering, open source biotechnology]
status: published
---

# Open Enzyme: Founding Vision

An open source library of food-grade, engineered microbial strains — each producing a therapeutic enzyme, each growable at home, each freely available to anyone.

**By:** Brian Abent  
**Date:** April 2026  
**Document Type:** North Star Document

---

## 1. The Problem

Hundreds of millions of people worldwide suffer from enzyme deficits. Not rare genetic anomalies — common, often debilitating conditions where the body either lost the ability to produce an enzyme (like uricase, silenced in all humans ~15 million years ago) or can't produce enough of one (like the lipases, proteases, and amylases needed to digest food).

| Statistic | Value |
|-----------|-------|
| Americans with gout (uricase deficit) | 9.2M |
| Global population with lactose malabsorption | ~65% |
| Americans with exocrine pancreatic insufficiency | ~90K |
| Annual cost of IV enzyme replacement therapies | $50K+ |

The list goes on: phenylketonuria (PKU), oxalate kidney stones, histamine intolerance, sucrase-isomaltase deficiency. Each is an enzyme deficit. Each leaves patients caught between pharmaceutical interventions that are staggeringly expensive ($50,000+ per year for IV enzyme replacement, $30–100/month for daily supplements forever) or simply suffering.

These aren't problems of understanding. The enzymes are well-characterized. The genes are sequenced. The biology is solved. What's missing is **accessibility** — a way to bridge the gap between what science knows how to make and what patients can actually get.

---

## 2. The Insight

The organisms we need are already in our kitchens. *Aspergillus oryzae* (koji mold) has been used in East Asian food production for over a thousand years. *Saccharomyces cerevisiae* (brewer's yeast) has been baking bread and fermenting beer for millennia. Both hold GRAS (Generally Recognized As Safe) status from the FDA. Both are among the most genetically tractable organisms on Earth, with decades of established transformation protocols and industrial-scale use.

> **The critical realization:** These organisms already produce therapeutic enzymes naturally. Koji produces lipase, protease, and amylase — the same enzymes that patients with exocrine pancreatic insufficiency pay $30–100/month to take as supplements. And for the enzymes they don't produce natively, we have mature, routine genetic engineering techniques to add them.

Genetic engineering of *S. cerevisiae* is undergraduate coursework. Transformation of *A. oryzae* is decades-old industrial practice. Expression of heterologous enzymes in these hosts is published, reproduced, and well-understood. The missing piece was never the biology. It was the packaging — nobody has assembled this knowledge into a platform that a motivated non-scientist can use.

---

## 3. The Platform Vision

Open Enzyme is an open source library of engineered microbial strains. Each strain addresses a specific enzyme deficit. Each is built in a food-safe (GRAS) host organism. Each comes with everything needed to reproduce it: the gene construct, transformation protocol, fermentation instructions, dosing math, and safety data.

Every strain can be grown at home with simple equipment — rice, a basic incubator, a fermentation vessel. No clean room. No bioreactor. No prescription.

### The GitHub Analogy

If you think about this as software, the architecture snaps into focus:

| Software World | Open Enzyme |
|---|---|
| Repository | → Strain definition (enzyme + host + construct) |
| Source code | → Gene construct (promoter + gene + terminator) |
| Runtime / VM | → Host organism (S. cerevisiae, A. oryzae, etc.) |
| Deployment | → Fermentation protocol (grow on rice, dry, capsule) |
| Dependencies | → Selection markers, auxotrophies, media recipes |
| CI / Testing | → In vitro activity assays, biomarker tracking |
| Fork & PR | → Modify a strain, contribute improvements back |

No patents. No prescriptions. No gatekeeping. Fork it, modify it, contribute back. This is **enzyme production as open source infrastructure.**

### Platform Choice — Koji-First, Yeast Retained for Specific Modules

Open Enzyme supports two GRAS hosts, but the platform is now **koji-first** for the therapeutic stack, with *S. cerevisiae* retained for specific modules where yeast expression is better characterized or more likely to succeed.

**Why koji-first (A. oryzae as primary host):**

- **Secretion capacity.** Native koji secretes 25–30 g/L into growth media (industrial fermentation); *S. cerevisiae* typically reaches 0.5–2 g/L for heterologous secreted proteins. An order-of-magnitude advantage for any secreted enzyme.
- **Multi-enzyme baseline.** Wild-type koji already produces lipase, protease, and amylase at therapeutically relevant levels, plus natural kojic acid, ergothioneine, and ferulic acid — pathway-modulator-adjacent compounds on day zero, before any engineering.
- **Home-fermentation feasibility.** Koji grows on steamed rice at 30 °C in 36–48 hours. Equipment: rice cooker, incubator, cheesecloth. No bioreactor required.
- **Food precedent.** 1,000+ years of human consumption in East Asian cuisine. FDA GRAS status. Safety case is trivial compared to any novel organism.
- **Dose scalability.** ~10–15 g of engineered koji is in the therapeutic ballpark for Creon-equivalent digestive enzyme dosing — a lower mass burden than gram-scale yeast consumption for comparable activity.

**Why yeast is retained (S. cerevisiae for specific modules with open expression questions):**

Some heterologous compounds may express better in *S. cerevisiae* than *A. oryzae* — particularly tetrameric proteins (the rasburicase precedent: *A. flavus* uricase expressed in *S. cerevisiae* reportedly reaches 13% of total cellular protein). The yeast track preserves flexibility for compounds where koji expression fails or yields are inadequate. Specific decision points we have not yet resolved:

- **Ursolic acid** — 8.59 g/L record in engineered *S. cerevisiae*; untested in koji.
- **Carnosine** — biosynthesis requires heterologous carnosine synthase; host choice open.
- **Lactoferrin** — 3.5 g/L record in *P. pastoris*; koji expression untested.
- **Uricase itself** — rasburicase proves the *S. cerevisiae* path works; the koji path needs to be developed.

These are empirical questions, not ideological ones. We build in koji first and fall back to yeast when the data says to.

---

## 4. First Targets

### Uricase — Gout (Active Development)

*S. cerevisiae* or *S. boulardii* expressing the *Aspergillus flavus* uricase gene (*uaZ*). The enzyme degrades uric acid in the gut lumen, exploiting the ABCG2 secretion pathway through which approximately one-third of the body's uric acid is excreted into the intestine. By placing the enzyme where the substrate already concentrates, we avoid the need for systemic delivery entirely.

**Validated by:** Rasburicase (FDA-approved since 2001, same A. flavus uricase gene expressed in S. cerevisiae) • ALLN-346 oral uricase (Phase 2a: statistically significant reduction in serum uric acid via gut-lumen degradation) • PULSE probiotic (Cell Reports Medicine, Oct 2025: engineered E. coli Nissle expressing uricase, validated in rodent models) • Engineered S. boulardii for UA degradation (ACS Synthetic Biology, 2025: 365 μmol/h/OD enzymatic activity)

### Digestive Enzymes — EPI / SIBO (Ready Now)

Wild-type *Aspergillus oryzae* (koji). No genetic engineering needed. Traditional koji grown on steamed rice already produces lipase, protease, and amylase at therapeutically relevant levels. This is the simplest possible entry point — a food that has been consumed for over a millennium, produced with equipment available in any kitchen, providing the same enzymes that patients with exocrine pancreatic insufficiency currently buy as pharmaceutical supplements.

**Evidence:** Koji enzyme profiles are extensively characterized in food science literature • Commercial enzyme supplements (Creon, Zenpep) use fungal-derived enzymes from the same family • A. oryzae holds FDA GRAS status with decades of safety data

### Expanding the Library (Future Targets)

Each represents a well-characterized enzyme deficit with a known gene and a feasible GRAS-host expression strategy:

- **Lactase** (lactose intolerance, ~4.7B people globally)
- **Oxalate decarboxylase** (oxalate kidney stones, ~10% lifetime prevalence)
- **Phenylalanine hydroxylase** (PKU, ~1:10,000 births)
- **Diamine oxidase** (histamine intolerance, estimated 1–3% of population)

---

## 5. The Science That Makes This Real

Every claim in this document traces to established, published science. This isn't speculative biology — it's an integration play, assembling known, validated components into a new configuration. Here is the evidence base:

### 1. ALLN-346 Phase 2a Clinical Trial

Oral uricase enzyme (non-living, acid-stable formulation) demonstrated statistically significant reduction in serum uric acid levels via gut-lumen degradation. Proof that an enzyme active in the intestine can lower systemic uric acid without entering the bloodstream.

### 2. PULSE Probiotic (Cell Reports Medicine, Oct 2025)

Engineered *E. coli* Nissle 1917 expressing uricase, validated in rodent models. Demonstrates that a living, orally-delivered microbe can express enough active uricase in the gut to meaningfully reduce uric acid levels.

### 3. Engineered S. boulardii (ACS Synthetic Biology, 2025)

*S. boulardii* engineered for uric acid degradation achieved 365 μmol/h/OD enzymatic activity. Demonstrates that a GRAS yeast can be engineered to express functional uricase at therapeutically relevant activity levels.

### 4. Rasburicase (FDA-Approved Since 2001)

*Aspergillus flavus* uricase gene expressed in *S. cerevisiae*. The exact gene-host combination this project proposes has been FDA-approved for over two decades as an IV drug (Elitek/Fasturtec). We are not inventing a new enzyme or a new expression system — we are changing the delivery route from IV to oral/food.

### 5. ABCG2 Gut Uric Acid Secretion Pathway

Approximately one-third of total uric acid excretion occurs via active secretion into the intestinal lumen through the ABCG2 transporter. This creates a natural substrate pool in the gut that a gut-resident or gut-delivered enzyme can access, making systemic absorption of the enzyme unnecessary.

### 6. A. oryzae & S. cerevisiae Genetic Engineering

Both organisms have decades of established transformation protocols. *S. cerevisiae* is the most genetically tractable organism on Earth, with a mature toolkit of promoters, terminators, selection markers, and expression vectors. *A. oryzae* transformation is routine in industrial biotechnology, with established protoplast and Agrobacterium-mediated methods. Both hold FDA GRAS status.

---

## 6. The Team

### Brian Abent — Platform / Engineering (Founder)

CTO who built Ceros from zero to $50M ARR. No science degree — thinks like an engineer. Currently building Alma.casa (AI real estate) and raising a seed round. Started Open Enzyme because he has gout and got tired of waiting for the system to solve it.

**Answers:** How do we make this reproducible, documentable, and accessible to non-scientists? How do we build this as a platform, not a one-off experiment?

Currently the sole team member. The project is actively recruiting collaborators with deep expertise in gut biology, immune safety, and translational science — each mapping to a critical question the project needs answered.

### Gut Microbiome / In Vivo Validation *(seeking collaborator)*

Expertise needed: gut microbiome dynamics, gnotobiotic (germ-free) animal models, in vivo validation of engineered microbes.

**Would answer:** Will an engineered strain survive and function in the gut? How does it interact with existing microbiota? What do the gnotobiotic validation experiments look like?

### Pharma Translation / Regulatory *(seeking collaborator)*

Expertise needed: inflammatory signaling (NF-κB, intestinal epithelial biology), pharmaceutical development, regulatory pathways for live biotherapeutic products.

**Would answer:** What are the inflammatory signaling implications? How does this map to pharma-grade safety and efficacy standards? Where does citizen science end and clinical development begin?

### Innate Immune Safety *(seeking collaborator)*

Expertise needed: innate immune responses in gut epithelium, TLR signaling, pathogen-associated molecular pattern (PAMP) analysis, epitope risk assessment.

**Would answer:** Will engineered strains trigger adverse immune responses? How do we ensure the host organism's modifications don't create unexpected immunogenic epitopes or aberrant PAMP signaling?

---

## 7. How It Works

The end-to-end flow from identifying a deficit to producing a functional, food-grade therapeutic enzyme:

```mermaid
graph TD
    A["Identify enzyme deficit"] --> B["Source the gene"]
    B --> C["Build expression cassette"]
    C --> D["Transform into food-safe host"]
    D --> E["Screen for activity"]
    E --> F["Optimize fermentation"]
    F --> G["Determine therapeutic format"]
    G --> H["Validate dosing"]
    H --> I["Document and publish open source"]
```

| Step | Action | Details |
|------|--------|---------|
| 1 | **Identify enzyme deficit** | Define target, substrate, location, outcome |
| 2 | **Source the gene** | NCBI/UniProt sequence, codon-optimized DNA (~$80–200) |
| 3 | **Build expression cassette** | Promoter + gene + terminator + marker (Gibson, Golden Gate, or HR) |
| 4 | **Transform into food-safe host** | Lithium acetate/PEG for yeast; protoplast-PEG or Agrobacterium for koji |
| 5 | **Screen for activity** | Plate transformants, assay, select highest-expressing clones |
| 6 | **Optimize fermentation** | Temperature, media, time, aeration; koji on rice 36–48 h at 30 °C |
| 7 | **Determine therapeutic format** | Koji on rice, dried powder, fermented beverage, or encapsulated |
| 8 | **Validate dosing** | In vitro assays, benchmark, self-experimentation with biomarker tracking |
| 9 | **Document and publish** | GitHub-ready: construct map, SOP, activity data, dosing, safety notes |

---

## 8. Cost Reality

A single IV dose of rasburicase costs approximately $5,000–8,000 at US hospital pricing. The total project cost to engineer a new strain from scratch:

| Component | Description | Cost |
|-----------|-------------|------|
| Gene synthesis | Codon-optimized synthetic DNA (IDT, Twist) | ~$80 |
| Cloning & transformation | Vectors, enzymes, competent cells, plates, media | $200–500 |
| Screening & validation | Activity assays, colony screening, confirmation | $500–1,000 |
| Equipment access | Community biolab membership / shared equipment | $0–500 |
| Fermentation supplies | Rice, media, incubation, drying/processing | $50–100 |
| **Total per new strain** | | **$1,200–$2,500** |

> **For perspective:** The total cost to develop one new Open Enzyme strain is less than a single IV dose of rasburicase. Ongoing production cost for home-grown koji or yeast is effectively the price of rice and basic nutrients — under $5/month.

---

## 9. The Multi-Attack Strategy

For the founding use case (Brian's gout), the project isn't just "make uricase." Gout is a cascade: uric acid accumulates, crystallizes in joints, triggers the NLRP3 inflammasome, which drives the acute inflammatory attack. A comprehensive strategy addresses multiple points in the cascade simultaneously:

### Remove the Cause

Engineered yeast or koji producing uricase. Degrades uric acid in the gut lumen before it can accumulate systemically. The primary engineering target of this project.

### Defuse the Bomb

NLRP3 inflammasome suppression stack: beta-hydroxybutyrate (BHB), oridonin, sulforaphane, KPV peptide, quercetin, ursolic acid, β-caryophyllene, carnosine, taurine, lactoferrin, SPMs. Each compound targets a different step in the NLRP3 activation pathway — priming, K⁺ efflux, assembly, IL-1β release, resolution, or neutrophil amplification.

**Platform positioning — pathway modulator, not direct-inhibitor knockoff.** Open Enzyme is a **food-derived, multi-target NLRP3 pathway modulator** platform — not an attempt to produce a food-grade analog of the direct NLRP3 inhibitor class (MCC950, dapansutrile, oridonin). The distinction matters: pharma has tested direct inhibitors in gout and the class has largely stalled (MCC950 hepatotoxicity halt, dapansutrile no Phase 2b/3 post-2a). The only curated direct-human-NLRP3 IC50 values in ChEMBL are dapansutrile (1 μM), oridonin (5.18 μM), and curcumin (24.2 μM). Pharma's only post-2010 gout win at the inflammasome cascade is canakinumab at CP5a (IL-1β receptor blockade, FDA-approved Aug 2023). The Open Enzyme stack is overwhelmingly pathway modulators — hitting upstream priming (CP1a/CP1b), K⁺ efflux (CP2), active resolution (CP5b), and neutrophil amplification (CP6a) — chokepoints that pharma has not rigorously tested in gout. Multi-target pathway modulators hitting redundant nodes can plausibly produce meaningful IL-1β suppression through cumulative effect, even if no single compound matches pharma-grade potency at a single target. This is a more honest and more defensible positioning than "supplement-grade version of MCC950." (source: [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md), [nlrp3-exploit-map.md](./nlrp3-exploit-map.md), [gout-clinical-pipeline.md](./gout-clinical-pipeline.md))

### Heal the Damage

Peptides for tissue repair: BPC-157 (angiogenesis, tendon/joint repair), TB-500/Thymosin β4 (anti-inflammatory, tissue remodeling). Addresses existing damage from prior flares.

### Optimize the Terrain

Gut health optimization: targeted probiotics, SIBO treatment (addressing co-occurring digestive enzyme insufficiency in a close family member, which motivates the EPI track), gut barrier support. A healthy gut is the deployment environment for everything above.

This multi-vector approach reflects an engineering mindset: don't bet on a single point of intervention. Build redundancy into the system. If the uricase strain takes months to optimize, the NLRP3 stack provides relief now. If inflammasome suppression is partial, tissue repair peptides address what gets through.

---

## 10. Principles

- **Open source everything.** No patents on strains, constructs, or protocols. The point is accessibility. If this works, it should be available to every gout patient, every person with EPI, every family managing PKU — not locked behind intellectual property walls.

- **Safety first — GRAS organisms only.** Every strain is built in a host organism that has FDA GRAS status and centuries of safe human consumption. We use established transformation methods with known safety profiles. No novel organisms. No uncharacterized pathways.

- **Rigorous but accessible.** Every protocol should be followable by a motivated non-scientist with basic lab access (community biolab level). But "accessible" never means "sloppy." Documentation is detailed, methods are validated, results are quantified.

- **Community-validated.** Replication is not optional — it's the core quality mechanism. Encourage independent reproduction, share all results (including failures), build a community of practice around each strain.

- **Not medical advice.** This is citizen science, self-experimentation, and open knowledge sharing. We document what we build, what we observe, and what the published literature supports. We do not prescribe, diagnose, or claim to cure.

---

## 11. What This Is Not

- **Not a company** (at least not yet). This is a passion project born from personal necessity, built in the open. If it grows into something larger, it will be because the science worked and the community demanded it — not because of a business plan.

- **Not medical advice or a replacement for professional care.** Anyone using these protocols should be working with their physician, tracking their biomarkers, and making informed decisions about their own health.

- **Not claiming to cure anything.** This is a research and self-experimentation platform. We produce enzymes. We measure their activity. We track biomarkers. We share data. The biology is well-established; the integration into a home-producible format is what's novel.

- **Not reckless.** Every strain uses GRAS organisms. Every method is drawn from published, peer-reviewed protocols. Recruiting PhD-level collaborators in gut biology, immune safety, and translational science is an active priority. We are careful precisely because we are serious.

---

## 12. Related Work & Complementary Projects

Open Enzyme operates in an active research neighborhood. The following are programs and tools that complement or parallel this work — **not competitors**. Open Enzyme is open source; we benefit from every validated data point these groups publish. Where there is overlap (e.g., *C. utilis* uricase work), we learn from their engineering. Where there is divergence (e.g., systemic IV vs. gut-lumen enzymatic), we cover chokepoints they don't reach, and vice versa.

- **ALLN-346 (Allena, terminated 2022)** — engineered *C. utilis* uricase for oral gut-lumen delivery. Validated the mechanism in mice and signaled efficacy in CKD patients (Phase 2a Study 201). Engineering data publicly disclosed in US10815461B2. Allena's bankruptcy left the program orphaned; Open Enzyme can learn from both their success and their economic failure. See [engineered-yeast-uricase-proposal.md](./engineered-yeast-uricase-proposal.md) for the mutation set and how it informs our construct design.

- **SSS11 (Shanghai, Phase 1 recruiting — NCT06629376)** — pegylated *C. utilis* uricase, systemic IV route. Parallel track, not competitive: Open Enzyme targets gut-lumen enzymatic degradation; SSS11 targets systemic urate clearance.

- **PRX-115 (Shanghai Pharma, Phase 1)** — PEG-uricase, systemic IV. Similar non-overlap with gut-lumen strategy.

- **Krystexxa + methotrexate (FDA-approved)** — pegloticase + immunosuppression to reduce anti-drug-antibody response. Systemic, refractory-gout indication. Standard of care for a small patient subset; not a platform comparison.

- **Engineered S. boulardii (ACS Synthetic Biology, 2025)** — probiotic expression of *V. vulnificus* uricase reaching 365 μmol/h/OD. Academic group, non-commercial. Methodologically closest to Open Enzyme; worth following and engaging.

- **Canakinumab (Ilaris, FDA-approved for gout Aug 2023)** — anti-IL-1β mAb, CP5a. ~$300K/year. Complementary, not competitive — Open Enzyme targets upstream chokepoints (CP0–CP2, CP5b, CP6a); canakinumab is the reference for CP5a coverage. Any food-grade approach is automatically cost-differentiated.

- **Avacopan (Tavneos, FDA-approved 2021 for ANCA vasculitis)** — oral C5aR1 antagonist. Mechanism-aligned with Open Enzyme's CP0 gap (see [complement-c5a-gout.md](./complement-c5a-gout.md)). Untested in gout but plausibly repurposable.

- **CERC-002 (Avalo Therapeutics)** — anti-LIGHT mAb, Phase 2 positive in COVID-19 ARDS. Mechanism-aligned with CP1a (TNFSF14). Not in gout development. See [tnfsf14-gout-target.md](./tnfsf14-gout-target.md).

---

## 13. Existing Research Library

The following research documents form the evidence base and technical foundation for the Open Enzyme project. Each was produced as a deep-dive into a specific aspect of the problem:

1. **[Gout: A Deep Dive — State of the Art, Frontier Research, and Unconventional Angles](gout-deep-dive.md)**  
   Comprehensive survey of gout pathophysiology, current treatments, and emerging therapeutic approaches including uricase gene therapy and gut-based strategies.

2. **[The Enzyme Deficit Connection — Gout, Digestion & the Koji Frontier](enzyme-deficit-deep-dive.md)**  
   Mapped the link between Brian's uricase deficit and a co-occurring digestive enzyme insufficiency in a family member. Identified koji as a dual-purpose therapeutic platform and crystallized the Open Enzyme concept.

3. **[Engineering S. cerevisiae for Oral Uricase Delivery — A Research Proposal](engineered-yeast-uricase-proposal.md)**  
   Detailed technical proposal for the uricase yeast strain: gene construct design, expression strategy, transformation protocol, and in vitro/in vivo validation plan.

4. **[Project Koji — Engineering A. oryzae for Dual Enzyme Therapy](engineered-koji-protocol.md)**  
   Full protocol for engineering koji to produce both digestive enzymes (native) and uricase (heterologous). Covers transformation, fermentation, and dosing for a rice-based therapeutic food.

5. **[NLRP3 Exploit Map — Pen-Testing the Inflammatory Cascade](nlrp3-exploit-map.md)**  
   Systematic analysis of every intervention point in the NLRP3 inflammasome pathway. Identified a multi-compound suppression stack (BHB, oridonin, sulforaphane, KPV) targeting priming, assembly, and effector stages.

6. **[Pen-Testing the Gut-Blood Barrier — Every Route to Systemic Uricase](blood-barrier-exploits.md)**  
   Evaluated every possible route for getting uricase from gut to bloodstream. Concluded that gut-lumen degradation (not systemic absorption) is the most viable and safest strategy.

7. **[Peptides & Gout: A Research Addendum](peptide-gout-addendum.md)**  
   Deep dive into BPC-157, TB-500, and KPV for gout-related tissue repair and inflammation control. Established the "heal the damage" arm of the multi-attack strategy.

8. **[AI & Bio Tools Playbook](ai-bio-tools-playbook.md)**  
   Practical guide to using AI for sequence analysis, literature mining, and design of synthetic constructs.

---

> This project exists because the biology is solved and the access is broken. We're not waiting for permission to fix that.

**Open Enzyme Project — April 2026**
