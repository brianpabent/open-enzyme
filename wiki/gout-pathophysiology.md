---
title: Gout Pathophysiology
aliases: [gout-cascade, purine-metabolism, uric-acid-handling, inflammasome, urate-transporters, clinical-treatments]
related: [nlrp3-inflammasome, fructose-connection, validation-experiments, supplements-stack, complement-c5a-gout, spm-resolution-pathway, tnfsf14-gout-target, androgen-urate-axis, abcg2-modulators, theaflavins, zileuton, medicinal-mushroom-compound-mapping-computational]
sources: [gout-deep-dive.md, nlrp3-exploit-map.md, complement-c5a-gout.md, tnfsf14-gout-target.md, spm-resolution-pathway.md, androgen-urate-axis.md, abcg2-modulators.md, theaflavins.md, zileuton.md, medicinal-mushroom-compound-mapping-computational.md]
---

# Gout Pathophysiology

## The Complete Cascade

Gout is the clinical endpoint of a multi-step biochemical cascade. Understanding each step matters because each step is a potential therapeutic target.

---

## Step 1: Purine Metabolism → Uric Acid Production

### The Degradation Pathway

```text
Purines (from DNA/RNA turnover or dietary intake)
    ↓ (adenosine deaminase, nucleotidases)
Hypoxanthine
    ↓ Xanthine Oxidase (XO)
Xanthine
    ↓ Xanthine Oxidase (XO)
URIC ACID (end product in humans — we lack uricase)
```

Every cell in your body contains DNA and RNA built from purine bases (adenine and guanine). When cells turn over, or when you eat purine-rich foods (organ meats, shellfish, beer), those purines are metabolized. The final step is catalyzed by **xanthine oxidase (XO)**, which converts hypoxanthine → xanthine → uric acid.

This is where drugs like **allopurinol** and **febuxostat** intervene — they inhibit XO to reduce uric acid production at the source.

> **Reactome graph anchor (2026-06-01):** Human purine catabolism is represented by `R-HSA-74259`. The xanthine oxidoreductase branch includes hypoxanthine-to-xanthine reactions (`R-HSA-74247`, `R-HSA-9727347`) and xanthine-to-urate reactions (`R-HSA-74258`, `R-HSA-9727349`). Reactome correctly terminates the human pathway at urate; engineered microbial uricase is an Open Enzyme design layer rather than a missing human Reactome step. (Pathway anchor; source: `reference/generated/reactome/2026-06-01-open-enzyme-audit/`)

### The De Novo Purine Biosynthesis Arm — PRPS as a Distinct Chokepoint

**Phosphoribosyl pyrophosphate synthetase (PRPS)** catalyzes the rate-limiting first committed step of de novo purine biosynthesis: ribose-5-phosphate + ATP → PRPP + AMP. PRPP is the central substrate for purine (and pyrimidine) biosynthesis. PRPS sits **one biosynthetic step upstream** of the degradation pathway above — inhibiting PRPS reduces total purine flux at the source, which is mechanistically orthogonal to XO inhibition (which acts after purines are built and being broken down). (Mechanistic Extrapolation; source: prps-purine-biosynthesis-chokepoint.md)

PRPS is regulated by allosteric feedback from IMP and ADP/GDP. Conditions that deplete these (e.g., fructose-driven ATP depletion → AMP rise → IMP via AMP deaminase) **disinhibit PRPS** → PRPP rises → de novo purine biosynthesis accelerates → urate production rises. This is the canonical pathological PRPP-elevation pathway linking fructose to gout (see [fructose-connection.md](./fructose-connection.md)). PRPS1 gain-of-function mutations cause early-onset gout — direct human-genetic evidence that PRPS dysregulation drives clinical hyperuricemia. (In Vitro + Clinical Genetics; source: prps-purine-biosynthesis-chokepoint.md)

The first natural-product PRPS modulator documented in the OE corpus is **eurycomanol** from *Eurycoma longifolia* (tongkat ali), which suppresses PRPS-driven purine biosynthesis in vitro (PMID 34785103). Tongkat ali Physta also shows SUA ↓7–11% in a 2021 placebo-controlled human RCT (n=105). See [prps-purine-biosynthesis-chokepoint.md](./prps-purine-biosynthesis-chokepoint.md) for the full chokepoint scope page and [androgen-natural-modulation.md](./androgen-natural-modulation.md) §1 for the tongkat ali entry. (In Vitro + Clinical Trial; source: prps-purine-biosynthesis-chokepoint.md, androgen-natural-modulation.md)

(Source: prps-purine-biosynthesis-chokepoint.md)

### ADA (Adenosine Deaminase) — Purine Catabolism Chokepoint Candidate

**Adenosine deaminase (ADA)** catalyzes the irreversible deamination of adenosine → inosine and 2'-deoxyadenosine → 2'-deoxyinosine, a key step in purine catabolism upstream of xanthine oxidase. ADA sits in the purine degradation pathway between adenosine and inosine — modulating ADA activity changes the flux of purine nucleosides entering the XO → urate pipeline. (Mechanistic Extrapolation; source: medicinal-mushroom-compound-mapping-computational.md)

comp-014 identified ADA as a chokepoint candidate (medicinal mushroom compound × chokepoint mapping, Phase 2, 2026-05-06): the breadth aggregation of 6,798 fungal compounds across ChEMBL + LOTUS + PubMed identified ADA as a target with fungal-compound coverage, notably via **GLPP polysaccharide-peptide** from *Ganoderma lucidum* (lingzhi/reishi) and **cordycepin** (3'-deoxyadenosine) from *Cordyceps militaris*, which is itself an adenosine analog and ADA substrate. The native co-production of **pentostatin** (a clinical-grade ADA inhibitor) alongside cordycepin in *C. militaris* (Xia 2017, PMID 29056419) makes whole-fermentate Cordyceps a natural ADA-modulating preparation. (Mechanistic Extrapolation; source: medicinal-mushroom-compound-mapping-computational.md, medicinal-mushroom-complement-track.md)

**Status:** Chokepoint candidate — not yet formalized as a named chokepoint in the modality-chokepoint-matrix or NLRP3 exploit map. Pending Phase 3-6 comp-014 follow-ups for formal admit/reject decision. (source: medicinal-mushroom-compound-mapping-computational.md)

### Purinergic resolution: ADA has a second, time-dependent role

Extracellular ATP is both a danger signal and the substrate for CD39/CD73-mediated production
of adenosine. Adenosine can promote inflammatory resolution, while ADA removes it into the
inosine→hypoxanthine→urate pathway. ADA inhibition can therefore reduce precursor flow to
urate **and** prolong an anti-inflammatory signal, but the beneficial window may depend on
when it is applied relative to MSU activation. (Mechanistic Extrapolation from acute-gout
purinergic evidence.) [Validation experiment 1.40](./validation-experiments.md#140-cd39cd73adenosine-gout-resolution-time-course)
measures both axes through time.

### Succinate bifurcation: production and inflammation share a metabolite

Human gout metabolomics identifies succinate-associated signatures. Separate mechanistic
work links hepatic succinate to AMPD2-dependent purine degradation/urate production and
immune succinate to SUCNR1/HIF-1α inflammatory signaling. The same circulating metabolite
may therefore increase urate production in one tissue and NLRP3/IL-1β tone in another.
(Human Observational + Animal Model/In Vitro; composed mechanism untested.) See [validation
experiment 1.42](./validation-experiments.md#142-succinate-compartment-dissociation-hepatic-ampd2-vs-immune-sucnr1).

### Microbial bile acids bridge disposal and inflammation

FXR can regulate intestinal ABCG2, while TGR5 signaling can restrain NLRP3 activation. Gut
microbial bile-acid transformations may therefore alter urate disposal and flare biology at
once. The joint direction is not inferable from a generic “more secondary bile acids” score;
species, receptor bias, and tissue exposure matter. (Mechanistic Extrapolation.) See
[validation experiment 1.41](./validation-experiments.md#141-parallel-fxrabcg2-and-tgr5nlrp3-bile-acid-screen)
and the [multihop program](./gout-multihop-research-program.md).

### PINK1/Mitophagy — NLRP3-Priming-Adjacent Chokepoint Candidate

**PINK1 (PTEN-induced kinase 1)** is a mitochondrial serine/threonine kinase that serves as the master sensor of mitochondrial damage, recruiting Parkin (PRKN) to depolarized mitochondria to initiate mitophagy — the selective autophagic clearance of damaged mitochondria. Damaged mitochondria are a primary source of the mtROS that drives NLRP3 inflammasome activation (CP2). Enhancing PINK1/Parkin-mediated mitophagy clears damaged mitochondria before they can trigger NLRP3 assembly. (Mechanistic Extrapolation; source: medicinal-mushroom-compound-mapping-computational.md)

comp-014 identified PINK1/mitophagy as a chokepoint candidate (Phase 2, 2026-05-06): the breadth aggregation identified fungal compounds with PINK1-modulating activity. This mechanism is **NLRP3-priming-adjacent** — it operates upstream of CP2 (K⁺ efflux / mtROS) by removing the mitochondrial source of the activation signal, rather than blocking NLRP3 assembly directly. It is mechanistically distinct from both direct NLRP3 inhibitors (oridonin, dapansutrile) and pathway modulators (BHB, quercetin). (Mechanistic Extrapolation; source: medicinal-mushroom-compound-mapping-computational.md)

**Status:** Chokepoint candidate — not yet formalized. Pending Phase 3-6 comp-014 follow-ups for formal admit/reject decision. (source: medicinal-mushroom-compound-mapping-computational.md)

### The Evolutionary Loss

In most mammals, uric acid isn't the end of the line. An enzyme called **uricase** (urate oxidase) converts uric acid into allantoin, which is far more soluble and easily excreted by the kidneys.

**Humans, great apes, and some other primates lost the functional uricase gene roughly 15–20 million years ago.** The gene that once encoded it — *UOX* — is now a pseudogene, inactivated by two nonsense mutations at codons 33 and 187 and an aberrant splice site.

Loss of functional human UOX raises the background urate burden, but gout is not a single-cause UOX deficiency. Purine production, renal and intestinal transport, crystal formation, innate inflammation, and resolution all influence whether hyperuricemia becomes clinical gout.

---

## Step 2: Renal Handling — The Excretion Bottleneck

### Normal Uric Acid Handling

Approximately **70% of daily uric acid elimination happens through the kidneys**. The proximal tubule engages in a complex dance of filtration, reabsorption, and secretion involving multiple transporter proteins.

### The Key Transporters

| Transporter | Gene | Role | Status |
|---|---|---|---|
| **URAT1** | SLC22A12 | Reabsorbs uric acid from tubular lumen back into blood. The primary villain — reabsorbs ~90% of filtered urate. | Major drug target (probenecid, lesinurad, pozdeutinurad, dotinurad). **Long-horizon discovery-engine output:** kidney-tropic siRNA against URAT1 mRNA is a sequence-specific knockdown approach that avoids small-molecule reactive-metabolite mechanisms; gated on kidney-tropic conjugate delivery. See [sirna-urat1-modality.md](./sirna-urat1-modality.md). (**Mechanistic Extrapolation**.) |
| **GLUT9** | SLC2A9 | Basolateral exit transporter; moves uric acid from tubular cells into blood. Also handles fructose (the fructose-gout link). | Strongest GWAS hit for gout; under-explored as drug target |
| **ABCG2** | ABCG2 | Secretes uric acid into both gut lumen AND renal tubule. Loss-of-function variants are #1 genetic risk for gout. | Enhancing ABCG2 activity is unexplored (most drugs inhibit, not enhance). Candidate levers include butyrate-associated PPARγ signaling, sulforaphane-associated Nrf2 signaling, TNFα-suppression contexts, and direct Q141K trafficking rescue; each requires functional urate-flux validation. Direct androgen suppression of intestinal ABCG2 is unsupported—see [androgen-urate-axis.md](./androgen-urate-axis.md). |
| **OAT1/OAT3** | SLC22A6/8 | Basolateral uptake of urate from blood into tubular cells for secretion. | Modulated by some existing uricosurics |
| **NPT1/NPT4** | SLC17A1/3 | Apical secretion of urate into tubular lumen. | Emerging targets |

> **Reactome transporter anchor (2026-06-01):** Reactome models URAT1/SLC22A12 urate-lactate exchange as `R-HSA-561253` under `R-HSA-561048` Organic anion transport by SLC22 transporters. SLC2A9 and ABCG2 are present as Reactome entities, but the audit did not find a clean ABCG2-intestinal urate-efflux reaction. Downstream ABCG2 gut-sink claims on this page should therefore stay anchored to primary physiology and genetics rather than Reactome. (Pathway anchor/gap note; source: `reference/generated/reactome/2026-06-01-open-enzyme-audit/`)

### The Gut Excretion Pathway

**Approximately one-third of daily uric acid elimination occurs through the gut**, not the kidneys. This happens via the **ABCG2 transporter** on intestinal epithelial cells, which actively secretes uric acid into the intestinal lumen.

This gut-lumen pathway creates a testable opening for luminal uricase: active enzyme can degrade urate that reaches the lumen, but the resulting effect on net intestinal urate disposal and serum urate cannot be inferred from enzyme activity alone. The Open Enzyme yeast and koji implementations remain conditional research tracks. Built and characterized configurations enter the physiological reaction-site screen in [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial); an exact survivor must then clear the antioxidant-loss/peroxide safety assay in [§1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay). Functional in-vivo disposal and any serum effect remain later questions under [§§2.1–2.2](./validation-experiments.md#21-selected-uox-configuration-in-vivo-persistence-and-localization). (**Mechanistic Extrapolation**; sources: [gut-lumen sink](./gut-lumen-sink.md), [COMP-044](./gut-lumen-uricase-physiologic-regime-computational.md))

### The Under-Excretor Problem

Renal under-excretion is common in gout, but the relative contributions of production, renal transport, intestinal export, and mixed phenotypes vary. Mechanism studies should measure the relevant fluxes rather than infer an intervention from a single label. Gut-lumen degradation remains a research hypothesis for increasing net disposal.

### Urate-handling weaknesses and candidate mechanisms

The map below records which current candidate classes touch renal transport, intestinal export, purine production, or inflammatory priming. It is an evidence map, not a recommendation to combine tracks. Empty cells are biological or sourcing gaps; filled cells still require exposure, tissue-selectivity, safety, and functional urate-flux validation.

**Mechanism-first view** (transporter rows × track columns; modality-first view in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) is the complementary surface):

| Renal node / Enzyme | Mechanism | Engineered-organism UOX hypothesis | Medicinal mushroom track | TCM × rigor track |
|---|---|---|---|---|
| **URAT1** (SLC22A12) | Reabsorbs urate from tubular lumen back into blood; major drug target | — | **Cordycepin** (animal-model URAT1 mRNA reduction; PMID 29422889) | **Astilbin** from *Smilax glabra* (animal-model + classical TCM use) |
| **GLUT9** (SLC2A9) | Basolateral exit transporter; strongest GWAS hit | — | **GLPP** (animal-model GLUT9 modulation per comp-014 outputs) | — |
| **ABCG2 — direct modulation** | Secretes urate into gut lumen + renal tubule; #1 genetic risk locus | — *(no current OE platform coverage at the direct-modulation tier — gap)* | — | — |
| **ABCG2 — indirect derepression** *(Mechanistic Extrapolation, two-step composed)* | Indirect — via TNFα suppression → reduced transcriptional repression of ABCG2; weaker evidence tier than direct transporter effects | **Lactoferrin → TNFα suppression → ABCG2 derepression** (lactoferrin → TNFα suppression is Animal Model + In Vitro per [`lactoferrin.md`](./lactoferrin.md) §4.7; TNFα suppression → ABCG2 derepression is the Mechanistic Extrapolation step composed onto it; see also [`koji-endgame-strain.md`](./koji-endgame-strain.md) §2.2) | — | — |
| **OAT1 / OAT3** (SLC22A6/8) | Basolateral uptake of urate from blood into tubular cells for secretion | — | **GLPP** (animal-model OAT1 modulation per comp-014 outputs) | — |
| **Xanthine oxidase** (upstream) | Catalyzes hypoxanthine → xanthine → urate; #1 pharmacological target (allopurinol, febuxostat) | — | — | **Astilbin** (Animal Model XO inhibition + classical TCM use); **Acacetin** from *Agastache rugosa* / Huo Xiang (In Vitro IC50 = 0.58 μM, Yuk 2023 PMC9914411 — most potent flavonoid in panel, beats luteolin); **Kaempferol** from *Chrysanthemum morifolium* / Ju Hua (In Vitro IC50 = 2.18 μM, Wee 2023 PMC9864848; DKB114 formula 38.3% UA ↓ at 200 mg/kg, Lee 2018 PMC6213378); **Rhein** from *Rheum palmatum* / Da Huang (Animal Model direct XO inhibition, Meng 2015 — separable from emodin which acts via transporter excretion not XO). All four are flavonoid- or anthraquinone-class XO chokepoint hits supported by the classical-formula search. |
| **PRPS** (upstream) | Rate-limiting enzyme of de novo purine biosynthesis; PRPP synthesis; distinct chokepoint class from XO | — | — | **Eurycomanol** from *Eurycoma longifolia* / tongkat ali (In Vitro PRPS suppression, PMID 34785103; 2021 RCT SUA ↓7–11%, n=105) — see [prps-purine-biosynthesis-chokepoint.md](./prps-purine-biosynthesis-chokepoint.md) |
| **Gut-lumen urate sink** (post-renal) | Candidate degradation of luminal urate; the effect on net intestinal flux and serum urate remains unmeasured | Conditional yeast or koji expression of active uricase; no chassis is selected, and neither implementation has passed §1.33 or §1.36 (**Mechanistic Extrapolation**) | — | — |
| **ROS / CP1b priming** *(speculative)* | NLRP3 priming via reactive oxygen species — Fenton chemistry (iron-catalyzed hydroxyl-radical generation) and direct hydroxyl-radical / peroxynitrite scavenging are mechanistically orthogonal | **Lactoferrin** — iron sequestration → reduced Fenton-available iron → reduced ROS-driven NLRP3 priming (Animal Model + In Vitro per [`lactoferrin.md`](./lactoferrin.md) §4.1; Habib 2023 PMID 37926296; Shan 2026 PMID 41524100) | **Ergothioneine** from *P. citrinopileatus* (7.0 mg/g DW per Phase 7-1c correction in [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md)); direct thiol scavenging of hydroxyl radicals + peroxynitrite, Nrf2 induction. **Caveat:** mechanism is correct in principle but **not yet demonstrated in gout-relevant cell models** — support is gated on the proposed ergothioneine + lactoferrin combination ROS assay in MSU-stimulated THP-1 macrophages. Koji natively produces some EGT; cross-track distinction is *quantitative* (P. citrinopileatus ~5–10× more dietary EGT than koji-native) not *mechanistically-unique*. | — |

**Evidence-tier discipline.** The cited cordycepin, GLPP, and astilbin transporter or enzyme effects have animal-model support. The proposed yeast- or koji-delivered luminal UOX implementation does **not**: its current status is **Mechanistic Extrapolation** until the construct, exposure, physiological flux, and safety gates are measured. The **lactoferrin → ABCG2** link is also **Mechanistic Extrapolation** (lactoferrin → TNFα suppression is documented in vitro / clinical biopsy per [`lactoferrin.md`](./lactoferrin.md) §4.7; TNFα suppression → ABCG2 transcriptional derepression is the extrapolated step).

**Compartment discipline.** The mechanisms are multi-compartment: cordycepin and astilbin have systemic bioavailability sufficient to act at renal URAT1 (per animal-model evidence cited in [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) and the medicinal mushroom track scope page); GLPP acts primarily in the gut; a successful luminal-UOX construct would also act there; and lactoferrin's TNFα-suppression effect is systemic. Read the map as a mechanism-plus-compartment composite.

**Experimental implication.** Stratify studies by production versus under-excretion phenotype, then test one target mechanism at a time. Apparent multi-node coverage does not establish additivity, adequate exposure, or a clinically meaningful effect. Combination testing belongs after the individual arms pass their biological and safety gates.

(Sources: [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md), [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md), [`lactoferrin.md`](./lactoferrin.md), and [`androgen-urate-axis.md`](./androgen-urate-axis.md).)

#### Houttuynia × PDB combination hypothesis

A proposed fourth architecture pairs dietary *Houttuynia cordata* polysaccharide with an engineered PDB live biotherapeutic. The earlier version specified “PDB-derived butyrate on EcN” as though CBT2.0's product were known. It is not: engineered EcN carbon fate must first pass [validation experiment 1.37](./validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test).

| Chokepoint coverage | Houttuynia cordata polysaccharide (dietary) | Engineered PDB arm | Composition logic |
|---|---|---|---|
| **CP0 — complement priming** (MSU → C1/CRP → C3/C5 convertase → C5a) | Multi-target at C2 + C4 + C5 (Chen Daofeng / Fudan group; Lu 2018 PMC5925397 CH50 79–318 µg/mL) | — | Houttuynia covers CP0 entry-blockade from the gut-luminal side |
| **CP1 — TLR4 / NF-κB priming** | TLR4-MD2 partial agonism / hormetic antagonism → NF-κB → NLRP3 suppression (Yu 2026 PMC12937656; tight-junction restoration + intestinal NLRP3/caspase-1/IL-1β/IL-18 suppression per Li 2025 PMC12254813). **First dual-CP0+CP1 dietary candidate in the corpus.** | — | Houttuynia uniquely doubles as a CP1 candidate |
| **ABCG2 substrate supply** | — | Conditional: only if the selected strain produces sufficient butyrate and epithelial flux confirms an effect | Product and exposure gates are open |
| **NLRP3 dampening** (CP2 / CP4 downstream) | NLRP3/caspase-1/IL-1β suppression in vivo via TLR4 priming dampening (Li 2025) | HDAC inhibition independently dampens NLRP3 (per [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md)) | Two independent mechanisms converging on the same downstream node |

**Current interpretation:** the production stacks are distinct, but biological additivity is not “by construction.” Houttuynia activity, PDB carbon fate, epithelial exposure, and functional urate flux must each pass before combination testing.

**Combination gate.** Do not test the combination until both arms clear their individual validation gates: the Houttuynia §1.30 prioritization screen and PDB carbon-fate, stability, exposure, and urate-flux validation. The route used to produce either arm does not establish additivity.

**Cross-references:** [`complement-c5a-gout.md` §9.7](./complement-c5a-gout.md) (Houttuynia as Tier 1d dietary CP0+CP1 candidate), [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md) (PDB chassis + conditional SCFA biology), [`abcg2-modulators.md` §6](./abcg2-modulators.md) (supported WT induction; direct butyrate Q141K rescue unvalidated), [`validation-experiments.md` §1.30](./validation-experiments.md), [`chassis-pending-interventions.md`](./chassis-pending-interventions.md).

---

## Step 3: Crystallization — When Chemistry Becomes Pathology

When serum urate exceeds ~**6.8 mg/dL** (its saturation point at physiological pH and temperature), monosodium urate (MSU) crystals can form and deposit in joints, tendons, and surrounding tissues.

But here's the thing: **crystallization isn't immediate or inevitable.** Many people have hyperuricemia for years—even decades—without a single gout attack. Local factors influence when and where crystals form:

- **Temperature:** Cooler joints like the big toe crystallize first (why gout often starts in the foot)
- **pH:** Lower pH favors crystallization
- **Mechanical stress:** Trauma or movement increases risk. See [`mechanical-flare-triggers.md`](./mechanical-flare-triggers.md) for the five-mechanism research-gap page and the Li XD 2012 n=1,713 Qingdao cohort data on exertion/fatigue as trigger axis. (source: mechanical-flare-triggers.md)
- **Nucleation sites:** Existing crystals seed new crystal growth

**Open question — what triggers deposited crystal beds to flare?** The five-mechanism research-gap page at [`mechanical-flare-triggers.md`](./mechanical-flare-triggers.md) maps what's known and unknown about the mechanical-use / exertion / fatigue axis as a flare trigger. Empirically, 劳累 (fatigue/overwork) at 19.3% in the Li XD 2012 Qingdao n=1,713 cohort far exceeds 外伤 (trauma) at 0.35% — suggesting metabolic-overload over mechanical-shedding. The gap in trigger-attribution methodology and four testable experimental designs are documented there. (source: mechanical-flare-triggers.md)

---

## Step 4: The Inflammatory Cascade — NLRP3 and the Flare

### MSU Crystals as Danger Signal

MSU crystals are the match. The **NLRP3 inflammasome** is the gasoline. When tissue-resident macrophages encounter MSU crystals, the crystals are phagocytosed (engulfed). Inside the cell, crystals damage the lysosomal membrane, causing:

1. **Potassium efflux** (K⁺ leaks out of lysosomes)
2. **Reactive oxygen species (ROS) generation** (oxidative stress)

These are "danger signals" recognized by the immune system.

**Complement priming (CP0 — upstream of NF-κB):** MSU crystals also directly activate the complement system via classical and alternative pathways before intracellular signaling. Complement activation cleaves C5 → **C5a**, which binds C5aR1 on macrophages and generates ROS — the dominant priming signal for NLRP3 in gout (Cumpelik et al. 2016; Khameneh et al. 2017). This complement axis operates in parallel to TLR4/NF-κB priming and is not addressed by most NF-κB inhibitors. (Animal Model; source: complement-c5a-gout.md)

**TNFSF14/LIGHT (CP1a — priming amplifier):** TNFSF14 (LIGHT) is produced at the inflamed joint and is the second-highest fold-change gout-flare biomarker after IL-6 (Ea et al. 2024, *Ann Rheum Dis*). LIGHT signals via HVEM/LTβR → NF-κB, amplifying priming in parallel to LPS/TLR4. (Clinical Trial + In Vitro; source: tnfsf14-gout-target.md)

### The NLRP3 Inflammasome Assembly

```text
MSU Crystal Phagocytosis
    ↓
Lysosomal damage → K⁺ efflux + ROS generation
    ↓
NLRP3 Sensor Protein activation
    ↓
Assembly of complex: NLRP3 + ASC (adaptor) + pro-Caspase-1
    ↓
Caspase-1 activation (proteolytic cleavage)
    ↓
Cleavage of pro-IL-1β → active IL-1β (the master cytokine of gout)
    ↓
MASSIVE INFLAMMATORY STORM:
  - Neutrophil recruitment
  - Vasodilation
  - Pain signaling
  - NF-κB positive feedback loop
```

(Source: nlrp3-exploit-map.md, §1)

### Why Gout Flares Are So Explosively Painful

The NLRP3 inflammasome is one of the most potent inflammatory amplifiers in the innate immune system. It evolved to respond to danger signals from pathogens. MSU crystals hijack that system.

IL-1β is a master cytokine—one molecule has cascading effects across the entire immune system. A single flare can recruit thousands of neutrophils and trigger systemic inflammatory mediators.

---

## Acute flare vs. chronic tophus — two different problems

Open Enzyme's chokepoint kill chain (CP0–CP6) is built around the **acute flare**: MSU crystal → NLRP3 → IL-1β → neutrophils (innate, fast, self-limiting). The **tophus** is a distinct, *chronic* problem — an organized granuloma (crystal core + macrophages + multinucleated giant cells + fibrous capsule + an adaptive-immune corona). Dissolving a tophus is two separate problems: (1) **dissolve the crystals** through sustained urate control; the [gut-lumen uricase sink](./gut-lumen-sink.md) is only a candidate contributor if it passes §1.33 and §1.36 and produces a sufficient systemic effect; and (2) **resolve the organized inflammation + eroded bone** — driven by an innate-stromal **SPP1/MMP9 macrophage** subset + RANKL/osteoclast activity (*not* the Th17 axis, which single-cell tophus data show is a bystander), which the platform does **not** currently address. See [`open-questions.md` §"Chronic tophaceous gout — the adaptive-immune axis"](./open-questions.md) for the scoped no-go, the dissolution kinetics, and the intervention-node map.

## Current Treatment Landscape

The treatment landscape and clinical guidance live in [gout-deep-dive.md](./gout-deep-dive.md#current-treatment-landscape) and the compound dossiers. Mechanistically, colchicine disrupts microtubule-dependent ASC transport, P2X7-associated activation, neutrophil migration, and crystal phagocytosis. This pathway map does not provide a regimen or individualized treatment instruction.

### Why durable control requires sustained mechanism coverage

Durable urate control can act through sustained reduction of production, increased renal or intestinal disposal, systemic enzyme replacement, restoration of UOX activity, or a validated gut-lumen sink that changes net urate flux. These routes have different exposure, safety, and durability constraints. None is assumed necessary or sufficient, and inflammatory control remains a separate outcome from crystal-burden reduction.

---

## The Clinical Pipeline (2026)

The full drug-by-drug pipeline table and Open Enzyme positioning live at [gout-deep-dive.md §The Clinical Pipeline](./gout-deep-dive.md#the-clinical-pipeline--whats-coming) and the dedicated [gout-clinical-pipeline.md](./gout-clinical-pipeline.md). Gut-lumen UOX is one conditional Open Enzyme track within that broader attack surface, not an established mechanism or the project itself.

---

## Genomics and GWAS: Who Gets Gout and Why?

> **Unified variant index.** This section is the summary view. The full cascade-stratified catalogue — all gout-relevant variants across urate transporters, production enzymes, the UOX pseudogene, NLRP3 / inflammasome, IL-1β priming, pharmacogenetics, and comorbidity loci — lives at [`gout-genetic-variants.md`](./gout-genetic-variants.md). Use that page for stratification subagents and for variant-by-variant evidence-tier lookups.

### The Big Numbers

A meta-analysis of over **one million participants** identified **351 loci** associated with serum urate levels, with 17 previously unreported. A 2025 UK Biobank study (N=150,542) identified 13 loci associated with gout diagnosis, with notable sex-specific differences (16 loci in males, only 2 in females). The sex-specific GWAS signal is consistent with the **androgen-urate axis** (see [androgen-urate-axis.md](./androgen-urate-axis.md)) — sex hormones modulate URAT1/ABCG2 expression, gating which transporter polymorphisms actually manifest as hyperuricemia.

### The Three Transporter Genes

The same three transporter genes that dominate the genetic architecture of gout — **ABCG2** (strongest association; Q141K rs2231142, ~50% function loss), **GLUT9/SLC2A9** (second-strongest; largest per-allele urate effect; also transports fructose), and **URAT1/SLC22A12** (the reabsorption villain) — are detailed with their roles and drug-target status in the [Step 2 transporter table](#step-2-renal-handling--the-excretion-bottleneck) above. The variant-by-variant catalogue (alleles, effect sizes, evidence tiers) lives at [`gout-genetic-variants.md`](./gout-genetic-variants.md).

### Beyond Transporters

Several GWAS loci point to biology beyond kidney transport:
- Glycolysis and insulin signaling genes
- Lipid metabolism genes
- Inflammatory and immune-regulatory genes

This reinforces: gout susceptibility isn't just about urate levels—it's about how your immune system responds to crystals, your metabolic syndrome risk, and your inflammatory baseline.

(Source: gout-deep-dive.md, §4)

---

## Two separable biological problems

> Gout research must separate two outcomes:
> 
> **(1) Keep urate below crystallization conditions** — through production, excretion, or degradation mechanisms
> 
> **(2) Interrupt the inflammatory response to existing MSU crystals** — through NLRP3, IL-1, neutrophil, or resolution mechanisms
>
> Success on the inflammatory axis does not establish urate control, and success on the urate axis does not establish acute-flare control.

(Source: gout-deep-dive.md, §1)

### Research implication: test both outcomes independently

- Urate-control experiments must measure production, renal and intestinal disposal, luminal flux, and crystal burden as appropriate.
- Inflammation experiments must measure priming, inflammasome activation, IL-1 output, neutrophil amplification, and resolution as appropriate.
- Combination studies require each arm to pass independently and must test nonredundancy rather than assume that multiple mechanisms add.

---

## Linked Conditions

Gout is not isolated; it's embedded in broader metabolic dysfunction:

- **Metabolic syndrome:** Obesity, insulin resistance, dyslipidemia often co-occur
- **Chronic kidney disease:** Reduced GFR worsens uric acid excretion
- **Cardiovascular disease:** Gout patients have higher CV risk (from inflammation + shared metabolic pathways)
- **Hypertension:** Uric acid may drive blood pressure via renin-angiotensin system
- **Type 2 diabetes:** Shared metabolic roots, NLRP3 inflammasome implicated in both

(Source: gout-deep-dive.md, §1)

---

## Summary Diagram

```text
PURINE INTAKE → Purine Metabolism (XO) → URIC ACID
                                            ↓
                                    SERUM URIC ACID
                                    (Renal reabsorption,
                                     Intestinal secretion)
                                            ↓
                        CRYSTALLIZATION (MSU crystals in joint)
                                            ↓
                        Macrophage Phagocytosis + Inflammation
                                            ↓
                        NLRP3 Inflammasome Assembly
                                            ↓
                        Caspase-1 Activation
                                            ↓
                        IL-1β Release
                                            ↓
                        GOUT FLARE
                    (Pain, swelling, erythema)

INTERVENTION POINTS:
- PRPS inhibition: Reduce de novo purine biosynthesis at the source (eurycomanol from tongkat ali, In Vitro; distinct from XO inhibition downstream) — see [prps-purine-biosynthesis-chokepoint.md](./prps-purine-biosynthesis-chokepoint.md)
- ADA modulation: Alter purine catabolism flux upstream of XO (GLPP from *G. lucidum*, cordycepin + native pentostatin from *C. militaris* — chokepoint candidate identified by comp-014 Phase 2, 2026-05-06) — see [medicinal-mushroom-compound-mapping-computational.md](./medicinal-mushroom-compound-mapping-computational.md)
- PINK1/mitophagy enhancement: Clear damaged mitochondria before they trigger NLRP3 (fungal compounds with PINK1-modulating activity — chokepoint candidate identified by comp-014 Phase 2, 2026-05-06) — see [medicinal-mushroom-compound-mapping-computational.md](./medicinal-mushroom-compound-mapping-computational.md)
- XO inhibitors: Block uric acid production (Allopurinol, Febuxostat)
- URAT1 inhibitors: Reduce renal reabsorption (Pozdeutinurad, Lesinurad)
- ABCG2 enhancement: Boost gut secretion via butyrate/PPARγ (fermentable fiber, DASH RCT 0.25–0.73 mg/dL UA reduction, Clinical Trial), sulforaphane/Nrf2, Q141K rescue via HDAC inhibitors (In Vitro) — see [abcg2-modulators.md](./abcg2-modulators.md)
- Uricase: Degrade uric acid (systemic products have clinical evidence; engineered gut organisms remain conditional on §1.33 and §1.36)
- C5a/C5aR1 blockade: Block complement priming (Avacopan — repurposing candidate; CP0)
- TNFSF14/LIGHT blockade: Suppress priming amplifier (CERC-002, EGCG; CP1a)
- NLRP3 inhibitors: Block inflammasome (Dapansutrile, Oridonin, BHB; CP2–CP4)
- 5-LOX/LTB4 inhibitors: Block neutrophil amplification (Quercetin 300 nM, AKBA, Zileuton FDA-approved 5-LOX inhibitor; CP6a) — see [zileuton.md](./zileuton.md) for the full repurposing dossier
- IL-1 blockers: Block cytokine (Firsekibart, Anakinra, Canakinumab; CP5a)
- SPMs/ALX/FPR2 agonists: Active resolution (Omega-3-derived RvD1/MaR1; CP5b)
- Colchicine: Block neutrophil migration, inflammasome assembly
- Theaflavins (black-tea polyphenols): NLRP3-NEK7 disruption (CP2/CP3 assembly block) + ↓URAT1/↓GLUT9 renal urate reabsorption + secondary TNFSF14/HVEM modulation (CP1a); direct MSU peritonitis Animal Model (Chen 2023 PMID 37221235); Tier 2 supplement candidate — see [theaflavins.md](./theaflavins.md) (source: theaflavins.md)
```

---

Each step is an exploitable weakness, not a promise that acting at any one point is sufficient. Multiple mechanisms can be tested together only after the individual arms pass and a prespecified interaction experiment distinguishes useful increment, redundancy, antagonism, and new safety liabilities.

(Source: gout-deep-dive.md, nlrp3-exploit-map.md)
