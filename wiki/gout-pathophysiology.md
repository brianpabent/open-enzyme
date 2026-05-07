---
title: Gout Pathophysiology
aliases: [gout-cascade, purine-metabolism, uric-acid-handling, inflammasome, urate-transporters, clinical-treatments]
related: [nlrp3-inflammasome, fructose-connection, validation-experiments, supplements-stack, complement-c5a-gout, spm-resolution-pathway, tnfsf14-gout-target, androgen-urate-axis, abcg2-modulators, theaflavins, zileuton]
sources: [gout-deep-dive.md, nlrp3-exploit-map.md, complement-c5a-gout.md, tnfsf14-gout-target.md, spm-resolution-pathway.md, androgen-urate-axis.md, abcg2-modulators.md, theaflavins.md, zileuton.md]
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

### The De Novo Purine Biosynthesis Arm — PRPS as a Distinct Chokepoint

**Phosphoribosyl pyrophosphate synthetase (PRPS)** catalyzes the rate-limiting first committed step of de novo purine biosynthesis: ribose-5-phosphate + ATP → PRPP + AMP. PRPP is the central substrate for purine (and pyrimidine) biosynthesis. PRPS sits **one biosynthetic step upstream** of the degradation pathway above — inhibiting PRPS reduces total purine flux at the source, which is mechanistically orthogonal to XO inhibition (which acts after purines are built and being broken down). (Mechanistic Extrapolation; source: prps-purine-biosynthesis-chokepoint.md)

PRPS is regulated by allosteric feedback from IMP and ADP/GDP. Conditions that deplete these (e.g., fructose-driven ATP depletion → AMP rise → IMP via AMP deaminase) **disinhibit PRPS** → PRPP rises → de novo purine biosynthesis accelerates → urate production rises. This is the canonical pathological PRPP-elevation pathway linking fructose to gout (see [fructose-connection.md](./fructose-connection.md)). PRPS1 gain-of-function mutations cause early-onset gout — direct human-genetic evidence that PRPS dysregulation drives clinical hyperuricemia. (In Vitro + Clinical Genetics; source: prps-purine-biosynthesis-chokepoint.md)

The first natural-product PRPS modulator documented in the OE corpus is **eurycomanol** from *Eurycoma longifolia* (tongkat ali), which suppresses PRPS-driven purine biosynthesis in vitro (PMID 34785103). Tongkat ali Physta also shows SUA ↓7–11% in a 2021 placebo-controlled human RCT (n=105). See [prps-purine-biosynthesis-chokepoint.md](./prps-purine-biosynthesis-chokepoint.md) for the full chokepoint scope page and [androgen-natural-modulation.md](./androgen-natural-modulation.md) §1 for the tongkat ali entry. (In Vitro + Clinical Trial; source: prps-purine-biosynthesis-chokepoint.md, androgen-natural-modulation.md)

(Source: gout-deep-dive.md, §1; prps-purine-biosynthesis-chokepoint.md)

### The Evolutionary Loss

In most mammals, uric acid isn't the end of the line. An enzyme called **uricase** (urate oxidase) converts uric acid into allantoin, which is far more soluble and easily excreted by the kidneys.

**Humans, great apes, and some other primates lost the functional uricase gene roughly 15–20 million years ago.** The gene that once encoded it — *UOX* — is now a pseudogene, inactivated by two nonsense mutations at codons 33 and 187 and an aberrant splice site.

We are stuck at the uric acid step. **This is the root cause of gout.**

(Source: gout-deep-dive.md, §1)

---

## Step 2: Renal Handling — The Excretion Bottleneck

### Normal Uric Acid Handling

Approximately **70% of daily uric acid elimination happens through the kidneys**. The proximal tubule engages in a complex dance of filtration, reabsorption, and secretion involving multiple transporter proteins.

### The Key Transporters

| Transporter | Gene | Role | Status |
|---|---|---|---|
| **URAT1** | SLC22A12 | Reabsorbs uric acid from tubular lumen back into blood. The primary villain — reabsorbs ~90% of filtered urate. | Major drug target (allopurinol, lesinurad, pozdeutinurad, dotinurad). **Long-horizon discovery-engine output:** kidney-tropic siRNA against URAT1 mRNA is a sequence-specific knockdown approach that eliminates the benzbromarone-class off-target metabolite risk; gated on kidney-tropic conjugate delivery chemistry maturation (3–5 yr horizon). See [sirna-urat1-modality.md](./sirna-urat1-modality.md). (Mechanistic Extrapolation; source: sirna-urat1-modality.md) |
| **GLUT9** | SLC2A9 | Basolateral exit transporter; moves uric acid from tubular cells into blood. Also handles fructose (the fructose-gout link). | Strongest GWAS hit for gout; under-explored as drug target |
| **ABCG2** | ABCG2 | Secretes uric acid into both gut lumen AND renal tubule. Loss-of-function variants are #1 genetic risk for gout. | Enhancing ABCG2 activity is unexplored (most drugs inhibit, not enhance). Pharmacological levers now mapped — see [abcg2-modulators.md](./abcg2-modulators.md): butyrate (PPARγ induction, Animal Model + Clinical Trial), sulforaphane (Nrf2 induction), TNFα suppression (functional ABCG2 restoration in IBD organoids, In Vitro + clinical biopsy), Q141K trafficking rescue via HDAC inhibitors (In Vitro). Androgens (T, DHT) suppress ABCG2 transcriptionally — see [androgen-urate-axis.md](./androgen-urate-axis.md). |
| **OAT1/OAT3** | SLC22A6/8 | Basolateral uptake of urate from blood into tubular cells for secretion. | Modulated by some existing uricosurics |
| **NPT1/NPT4** | SLC17A1/3 | Apical secretion of urate into tubular lumen. | Emerging targets |

### The Gut Excretion Pathway

**Approximately one-third of daily uric acid elimination occurs through the gut**, not the kidneys. This happens via the **ABCG2 transporter** on intestinal epithelial cells, which actively secretes uric acid into the intestinal lumen.

This gut-lumen pathway is the mechanistic foundation for [[engineered-yeast-uricase]] and [[engineered-koji-protocol]] — if you place active uricase in the gut, it degrades uric acid present there, creating a "sink" that pulls additional uric acid from the serum.

(Source: gout-deep-dive.md, §1; engineered-yeast-uricase-proposal.md, §1)

### The Under-Excretor Problem

**Gout is, at its core, a kidney transporter problem.** Most gout patients (~90%) are "under-excretors" — their kidneys reabsorb too much uric acid. Only ~10% are true "over-producers."

This distinction matters enormously for treatment strategy:
- Under-excretors: benefit from URAT1 inhibitors, uricosurics, enhanced ABCG2, or gut-lumen degradation
- Over-producers: benefit from XO inhibitors (allopurinol, febuxostat)

(Source: gout-deep-dive.md, §2)

### Multi-track urate transporter coverage (added 2026-05-06)

The Open Enzyme platform's three concurrently-developing tracks — **engineered koji**, **medicinal mushroom complement**, and **TCM × modern rigor** — each address a different therapeutic mechanism. When mapped onto the renal urate handling nodes plus xanthine oxidase upstream, they collectively cover all four major transporter targets + the production enzyme. This coverage is **emergent, not designed** — each track was chosen for an independent therapeutic mechanism, and the multi-node coverage fell out as a happy accident. The map is operationally useful: it shows which combinations of tracks are mechanism-additive (covering different nodes) vs. which would be redundant (covering the same node) for any given patient phenotype.

**Mechanism-first view** (transporter rows × track columns; modality-first view in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) is the complementary surface):

| Renal node / Enzyme | Mechanism | Engineered koji track | Medicinal mushroom track | TCM × rigor track |
|---|---|---|---|---|
| **URAT1** (SLC22A12) | Reabsorbs urate from tubular lumen back into blood; major drug target | — | **Cordycepin** (animal-model URAT1 mRNA reduction; PMID 29422889) | **Astilbin** from *Smilax glabra* (animal-model + classical TCM use) |
| **GLUT9** (SLC2A9) | Basolateral exit transporter; strongest GWAS hit | — | **GLPP** (animal-model GLUT9 modulation per comp-014 outputs) | — |
| **ABCG2** | Secretes urate into gut lumen + renal tubule; #1 genetic risk locus | **Lactoferrin → TNFα suppression → ABCG2 derepression** (Mechanistic Extrapolation — indirect, not direct transporter modulation; see [`lactoferrin.md`](./lactoferrin.md) §4.7 + [`koji-endgame-strain.md`](./koji-endgame-strain.md) §2.2) | — | — |
| **OAT1 / OAT3** (SLC22A6/8) | Basolateral uptake of urate from blood into tubular cells for secretion | — | **GLPP** (animal-model OAT1 modulation per comp-014 outputs) | — |
| **Xanthine oxidase** (upstream) | Catalyzes hypoxanthine → xanthine → urate; #1 pharmacological target (allopurinol, febuxostat) | — | — | **Astilbin** (animal-model XO inhibition + classical TCM use) |
| **PRPS** (upstream) | Rate-limiting enzyme of de novo purine biosynthesis; PRPP synthesis; distinct chokepoint class from XO | — | — | **Eurycomanol** from *Eurycoma longifolia* / tongkat ali (In Vitro PRPS suppression, PMID 34785103; 2021 RCT SUA ↓7–11%, n=105) — see [prps-purine-biosynthesis-chokepoint.md](./prps-purine-biosynthesis-chokepoint.md) |
| **Gut-lumen urate sink** (post-renal) | Direct degradation of urate in gut lumen, creating concentration gradient that pulls serum urate into gut for ABCG2-mediated secretion | **Uricase** (engineered koji secretes active uricase into gut lumen — degrades luminal urate, *direct mechanism*) | — | — |

**Evidence-tier discipline.** Direct transporter / enzyme effects (URAT1 by cordycepin, GLUT9/OAT1 by GLPP, XO by astilbin, gut-lumen urate degradation by koji uricase) sit at **Animal Model** evidence tier from primary literature. The **lactoferrin → ABCG2** link is **Mechanistic Extrapolation** (lactoferrin → TNFα suppression is documented in vitro / clinical biopsy per [`lactoferrin.md`](./lactoferrin.md) §4.7; TNFα suppression → ABCG2 transcriptional derepression is the Mechanistic Extrapolation step composed onto it). This is a substantively weaker claim than the direct-modulation claims and should be flagged as such whenever the multi-track coverage map is invoked downstream.

**Compartment discipline.** Pass 2's framing called this an "all gut-luminal" coverage map. **That's wrong.** The mechanisms are multi-compartment: cordycepin and astilbin both have systemic bioavailability sufficient to act at renal URAT1 (per animal-model evidence cited in [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) and the medicinal mushroom track scope page); GLPP and the koji uricase work primarily in the gut-luminal compartment; lactoferrin's TNFα-suppression effect is systemic. The coverage map is best read as **mechanism + compartment composite** rather than collapsed to either dimension alone.

**Operational implication.** For a hyperuricemic patient phenotype where the dominant defect is **under-excretion** (~90% of gout patients per the Under-Excretor Problem section above), the mechanism-additive combination is **engineered koji (gut-lumen + ABCG2-derepression)** + **medicinal mushroom (URAT1 / GLUT9 / OAT1 direct)** + optionally **TCM-derived astilbin (URAT1 / XO)**. This is not a treatment recommendation — it's a mechanism-coverage map that informs clinical-design conversations once the platform reaches the relevant translation phase. For an **over-producer** phenotype (~10%), XO inhibition (astilbin or pharmacological allopurinol/febuxostat) is the priority, with under-excretor mechanisms as add-ons.

(Source: synthesized 2026-05-06 from individual mechanism documentation across [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md), [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md), [`lactoferrin.md`](./lactoferrin.md), and [`androgen-urate-axis.md`](./androgen-urate-axis.md). Cross-reference: modality-first view in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md).)

---

## Step 3: Crystallization — When Chemistry Becomes Pathology

When serum urate exceeds ~**6.8 mg/dL** (its saturation point at physiological pH and temperature), monosodium urate (MSU) crystals can form and deposit in joints, tendons, and surrounding tissues.

But here's the thing: **crystallization isn't immediate or inevitable.** Many people have hyperuricemia for years—even decades—without a single gout attack. Local factors influence when and where crystals form:

- **Temperature:** Cooler joints like the big toe crystallize first (why gout often starts in the foot)
- **pH:** Lower pH favors crystallization
- **Mechanical stress:** Trauma or movement increases risk
- **Nucleation sites:** Existing crystals seed new crystal growth

(Source: gout-deep-dive.md, §1)

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

(Source: gout-deep-dive.md, §1; nlrp3-exploit-map.md, §1)

### Why Gout Flares Are So Explosively Painful

The NLRP3 inflammasome is one of the most potent inflammatory amplifiers in the innate immune system. It evolved to respond to danger signals from pathogens. MSU crystals hijack that system.

IL-1β is a master cytokine—one molecule has cascading effects across the entire immune system. A single flare can recruit thousands of neutrophils and trigger systemic inflammatory mediators.

(Source: gout-deep-dive.md, §1)

---

## Current Treatment Landscape

### Acute Flare Management

**Colchicine** (first-line) — see [colchicine.md](./colchicine.md) for the full dossier
- Inhibits microtubule polymerization → prevents microtubule-mediated ASC transport to NLRP3 (CP3 block)
- Also directly inhibits P2X7 pore → blocks K⁺ efflux upstream of NLRP3 activation (CP2 block) (Leung et al. 2015 PMID 26228647)
- Reduces neutrophil chemotaxis and phagocytosis of MSU crystals
- Low-dose regimen (1.2 mg + 0.6 mg at 1 h) validated by AGREE trial (Terkeltaub 2010 PMID 20131255); replaced older "dose-to-GI-failure" approach (Clinical Trial)
- Cardiovascular repositioning: COLCOT (23% CV event reduction) and LoDoCo2 (31% reduction) led to FDA approval of Lodoco 0.5 mg for atherosclerotic CVD, June 2023 (Clinical Trial)
- **ULT-initiation prophylaxis:** ACR 2020 guideline recommends concurrent colchicine 0.5–0.6 mg once or twice daily for 3–6 months when starting allopurinol/febuxostat, to prevent mobilization flares as tophaceous urate dissolves. Duration keyed to stable serum UA <6.0 mg/dL with no flares for ≥3 months. Same dissolution-flare bridge applies to CRISPR-uricase gene therapy — see [crispr-uricase.md](./crispr-uricase.md) for the post-therapy prophylaxis protocol. (Clinical Trial — guideline; source: colchicine.md)
- Problem: Narrow therapeutic index (~3–5×); CYP3A4/P-gp interaction surface (macrolides, azoles, calcineurin inhibitors); renal/hepatic dose adjustment required

**NSAIDs** (indomethacin, naproxen)
- Reduce inflammation and pain
- Problem: GI bleeding risk, cardiovascular risk, renal toxicity

**Corticosteroids** (prednisone)
- Typically 30–40 mg tapering over 7–10 days
- Fast-acting and effective
- Problem: Cumulative side effects (bone loss, metabolic disruption, rebound flare on discontinuation)

**IL-1 Inhibitors** (anakinra, canakinumab)
- Off-label for refractory acute gout
- Directly block IL-1β signaling
- Problem: Expensive, immunosuppressive

(Source: gout-deep-dive.md, §2)

### Urate-Lowering Therapy (ULT)

**Allopurinol** (XO inhibitor, approved 1966)
- Cheap, effective for many
- Requires dose titration
- Problem: Rare but potentially fatal hypersensitivity reaction (HLA-B*5801 associated)
- Many patients don't reach target urate levels

**Febuxostat** (XO inhibitor, approved 2009)
- More potent than allopurinol, no renal dose adjustment needed
- Problem: CARES trial raised cardiovascular mortality concerns (somewhat controversial)

**Probenecid** (uricosuric, URAT1 inhibitor)
- Increases renal uric acid excretion
- Problem: Requires adequate kidney function, increases kidney stone risk, fallen out of favor

**Pegloticase** (pegylated recombinant uricase, IV)
- Nuclear option for severe, refractory, tophaceous gout
- Enzymatically converts uric acid to allantoin
- Dramatically effective: tophi dissolve, urate levels plummet
- Problem: ~40–50% develop anti-drug antibodies; treatment failure from immunogenicity

(Source: gout-deep-dive.md, §2)

### Why There's No Cure

The honest answer: **gout is a chronic metabolic deficiency.** Humans lack a gene. You can manage the downstream consequences — reduce production (XO inhibitors), increase excretion (uricosurics), treat inflammation (colchicine/NSAIDs/IL-1 blockers), or temporarily replace the missing enzyme (pegloticase) — but none address the root genetic deficit.

Stop treatment, and uric acid climbs right back up.

**A true cure would require:**
1. Restoring uricase expression in human cells (gene therapy) — [[crispr-uricase]]
2. Permanently altering kidney transporter function to excrete more urate
3. Making the immune system permanently tolerant of MSU crystals

(Source: gout-deep-dive.md, §2)

---

## The Clinical Pipeline (2026)

The gout pipeline is more active now than it's been in decades:

| Drug | Mechanism | Phase | Status |
|---|---|---|---|
| **Pozdeutinurad (AR882)** | Next-gen selective URAT1 inhibitor | Phase 3 | REDUCE 1 & 2 pivotal trials fully enrolled. NDA planned 2026. |
| **SEL-212** | Pegylated ***C. utilis* uricase** (pegadricase) + rapamycin nanoparticles (prevents immunogenicity) — Sands 2022 *Nat Commun* PMID 35022448 | Phase 3 | DISSOLVE I & II completed. 46–56% response rates. Superior to pegloticase. |
| **Firsekibart (Genakumab)** | Anti-IL-1β monoclonal antibody | Phase 3 | Reduced new flare risk by 90% at 12 weeks, 87% at 24 weeks. |
| **Dapansutrile (OLT1177)** | Oral selective NLRP3 inflammasome inhibitor | Phase 2a only | 2020 Phase 2a (N=34): 52–68% pain reduction. **No Phase 2b/3 in gout registered as of April 2026 — gout development appears stalled.** (source: gout-clinical-pipeline.md) |
| **Dotinurad (URECE)** | Selective URAT1 inhibitor | Approved (Asia) | Approved in Japan, China, Thailand, Philippines. |
| **HNW005** | Dual NLRP3 + URAT1 inhibitor | Preclinical | Single molecule hitting both inflammation and uric acid. IL-1β IC50 = 1.7 μM. |
| **Canakinumab (Ilaris)** | Anti-IL-1β monoclonal antibody | **FDA approved Aug 2023 for gout** | First biologic formally indicated for gout in the US. (source: gout-clinical-pipeline.md) |
| **PRX-115 (RELEASE)** | Pegylated recombinant uricase ± methotrexate, IV | Phase 2 (recruiting) | Protalix; NCT07280156 started Dec 2025, N=150. **The new systemic-uricase competitor.** (source: gout-clinical-pipeline.md) |
| **SSS11** | Pegylated *Candida utilis* uricase, IV | Phase 1 | Shenyang Sunshine; NCT06629376. First clinical *C. utilis* uricase. (source: gout-clinical-pipeline.md) |
| **ALLN-346** | Engineered oral *C. utilis* uricase (gut-lumen) | **Discontinued** | Phase 2a CKD trial NCT04987294 terminated September 2022 (19/200 enrolled). (source: gout-clinical-pipeline.md) |

**Key insight:** The paradigm shift is toward **dual-mechanism approaches**—targeting both uric acid levels AND inflammation simultaneously. (Source: gout-deep-dive.md, §3)

**Pipeline reality check (2026-04-23):** The most consequential 2022–2025 changes for Open Enzyme's positioning: (1) ALLN-346 (gut-lumen uricase) was terminated September 2022 — the gut-lumen-uricase clinical precedent has gone dormant; (2) dapansutrile gout development has not progressed past Phase 2a despite the 2020 signal; (3) canakinumab finally got FDA approval for gout (August 2023); (4) PRX-115 (Protalix Phase 2 RELEASE, started Dec 2025) is the new systemic-uricase contender. **No active program in any phase targets the gut-lumen-uricase angle Open Enzyme pursues.** See [gout-clinical-pipeline.md](gout-clinical-pipeline.md) for the full snapshot. (source: gout-clinical-pipeline.md)

---

## Genomics and GWAS: Who Gets Gout and Why?

### The Big Numbers

A meta-analysis of over **one million participants** identified **351 loci** associated with serum urate levels, with 17 previously unreported. A 2025 UK Biobank study (N=150,542) identified 13 loci associated with gout diagnosis, with notable sex-specific differences (16 loci in males, only 2 in females). The sex-specific GWAS signal is consistent with the **androgen-urate axis** (see [androgen-urate-axis.md](./androgen-urate-axis.md)) — sex hormones modulate URAT1/ABCG2 expression, gating which transporter polymorphisms actually manifest as hyperuricemia.

### The Three Transporter Genes

Three genes dominate the genetic architecture of hyperuricemia and gout:

**ABCG2** (chromosome 4) — THE STRONGEST ASSOCIATION
- The common Q141K variant (rs2231142, ~10% European, ~30% East Asian)
- Reduces ABCG2 transport function by ~50%
- Means less uric acid secretion into gut and kidney
- 2025 UK Biobank GWAS: most significant association at rs2199936 in ABCG2 (p = 1.75 × 10⁻⁹⁷)

**GLUT9** (SLC2A9, chromosome 4) — SECOND STRONGEST
- rs58656183 (p = 5.52 × 10⁻⁹⁰)
- Largest per-allele effect on serum urate of ANY known locus
- Transports BOTH urate and fructose (the link between [[fructose-connection]] and gout)

**URAT1** (SLC22A12, chromosome 11) — THE REABSORPTION VILLAIN
- Loss-of-function variants PROTECT against gout (and cause renal hypouricemia)
- Gain-of-function or regulatory variants increase gout risk

(Source: gout-deep-dive.md, §4)

### Beyond Transporters

Several GWAS loci point to biology beyond kidney transport:
- Glycolysis and insulin signaling genes
- Lipid metabolism genes
- Inflammatory and immune-regulatory genes

This reinforces: gout susceptibility isn't just about urate levels—it's about how your immune system responds to crystals, your metabolic syndrome risk, and your inflammatory baseline.

(Source: gout-deep-dive.md, §4)

---

## The Two-Solution Framework

> **Key Insight:** There are fundamentally two ways to "solve" gout:
> 
> **(1) Prevent uric acid from ever reaching crystallization levels** — traditional medicine approach (allopurinol, febuxostat, uricosurics, uricase)
> 
> **(2) Prevent the immune system from recognizing MSU crystals as a threat** — inflammatory suppression approach (NLRP3 inhibitors, IL-1β blockers)
>
> Current medicine focuses almost entirely on #1. Approach #2—inflammasome modulation—is just now entering clinical trials and could be transformative for patients who can't tolerate or don't respond to urate-lowering therapy.

(Source: gout-deep-dive.md, §1)

### Open Enzyme Approach: Combine Both

- **Solution #1:** [[engineered-yeast-uricase]] and [[engineered-koji-protocol]] address the root genetic deficit by providing active uricase
- **Solution #2:** [[nlrp3-inflammasome]] suppression stack and [[supplements-stack]] target the inflammatory cascade to prevent flares while uricase is being optimized

The multi-attack strategy (Source: open-enzyme-vision.md, §9):
1. **Remove the cause:** Engineered yeast degrading uric acid
2. **Defuse the bomb:** NLRP3 inflammasome suppression stack
3. **Heal the damage:** Peptides for tissue repair (BPC-157, TB-500)
4. **Optimize the terrain:** Gut health, SIBO treatment, barrier support

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
- XO inhibitors: Block uric acid production (Allopurinol, Febuxostat)
- URAT1 inhibitors: Reduce renal reabsorption (Pozdeutinurad, Lesinurad)
- ABCG2 enhancement: Boost gut secretion via butyrate/PPARγ (fermentable fiber, DASH RCT 0.25–0.73 mg/dL UA reduction, Clinical Trial), sulforaphane/Nrf2, Q141K rescue via HDAC inhibitors (In Vitro) — see [abcg2-modulators.md](./abcg2-modulators.md)
- Uricase: Degrade uric acid (Pegloticase, SEL-212, Engineered organisms)
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

*Gout is solved at any point in this cascade. Multiple interventions hitting different points simultaneously (the Open Enzyme multi-attack strategy) have redundancy and resilience.*

(Source: gout-deep-dive.md, nlrp3-exploit-map.md)
