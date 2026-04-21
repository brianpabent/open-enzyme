---
title: Bio AI Tools
aliases: [AI-tools, AI-bio, GPT-Rosalind, Amazon-Bio-Discovery, Anthropic-Coefficient, computational-biology, protein-language-models, open-source-bio-AI]
related: [engineered-yeast-uricase, engineered-koji-protocol, validation-experiments, uricase, nlrp3-inflammasome]
sources: [ai-bio-tools-playbook.md]
---

# Bio AI Tools

## Overview

Three major commercial AI biology tools launched in April 2026 that can accelerate Open Enzyme: **GPT-Rosalind** (OpenAI), **Amazon Bio Discovery**, and **Anthropic's Coefficient Bio acquisition**. However, Rosalind requires institutional access and Bio Discovery costs $486/month. A robust ecosystem of **open source protein AI tools** — including ESM-2, AlphaFold/ColabFold, Boltz-2, RFdiffusion2, ProteinMPNN, and others — is freely available and covers most of the computational biology workflow. These open source tools are the project's primary computational toolkit. This document covers all three tiers: commercial, open source, and free web tools.

---

## Open Source Protein AI Tools (Available Now)

These tools are freely available and cover the core computational biology workflow for Open Enzyme. Many are the same models that power commercial platforms like Bio Discovery under the hood.

### Structure Prediction

- **ColabFold (AlphaFold 2)** — Gold standard for protein structure prediction. Free on Google Colab. Use for generating uricase variant structures. ([GitHub](https://github.com/sokrypton/ColabFold))
- **ESMFold** — ~60× faster than AlphaFold, trades small accuracy loss for speed. Use for rapid screening of dozens of variants. ([Hugging Face](https://huggingface.co/facebook/esmfold_v1))
- **Boltz-2** — First open source model approaching AlphaFold 3 for complexes (protein-ligand, protein-protein). MIT license. Predicts binding affinities 1000× faster than physics-based FEP. Use for uricase-uric acid binding, tetramer assembly, NLRP3 inhibitor docking. ([GitHub](https://github.com/jwohlwend/boltz))
- **Protenix-v1** — Open source structure predictor that outperforms AlphaFold 3. Alternative to Boltz-2. ([GitHub](https://github.com/bytedance/protenix))

### Protein Language Models & Variant Scoring

- **ESM-2 (Meta)** — Workhorse protein language model (650M params). Score every possible mutation by evolutionary plausibility. Zero-shot fitness prediction. Foundation for downstream tools. ([GitHub](https://github.com/facebookresearch/esm))
- **ESM-C** — Drop-in ESM-2 replacement, better performance at lower compute. Free academic API tier. ([EvolutionaryScale](https://www.evolutionaryscale.ai/))
- **ESM-3-open** — Next-gen multimodal model (sequence + structure + function). Generated a novel GFP with 58% identity to known — equivalent to ~500M years of evolution. Non-commercial license. ([GitHub](https://github.com/evolutionaryscale/esm))

### Protein Design & Engineering

- **RFdiffusion2 (Baker Lab)** — De novo enzyme design from active site geometry alone. Designed enzymes with catalytic efficiency up to 53,000 M⁻¹s⁻¹. BSD license. Phase 2 tool for designing acid-stable uricase scaffolds. ([GitHub](https://github.com/RosettaCommons/RFdiffusion2))
- **ProteinMPNN (Baker Lab)** — Designs amino acid sequences that fold into target structures. MIT license. Essential companion to RFdiffusion2. ([GitHub](https://github.com/dauparas/ProteinMPNN))

### Stability & Variant Effect Prediction

- **SPURS** — State-of-the-art ΔΔG prediction for mutations. Directly answers "will this mutation make the enzyme more or less stable?" ([GitHub](https://github.com/mj-hwang/SPURS))
- **RaSP** — Rapid saturation mutagenesis stability scans (<1 second per residue). Map the complete stability landscape of uricase. ([GitHub](https://github.com/KULL-Centre/papers))
- **DDGemb** — Predicts combined effect of multiple simultaneous mutations (epistasis). Critical for evaluating combinatorial variants. ([GitHub](https://github.com/PeppeL-G/DDGemb))
- **FoldX** — Physics-based stability calculations including pH dependence. Free for academics. Industry standard for 15+ years. ([foldxsuite.crg.eu](https://foldxsuite.crg.eu/))

### Molecular Docking

- **DiffDock** — AI-powered docking using diffusion models. 38% success rate vs. 23% for traditional tools. MIT license. Use for uric acid binding validation and NLRP3 inhibitor screening. ([GitHub](https://github.com/gcorso/DiffDock))

### Codon Optimization

- **CodonTransformer** — Deep learning codon optimizer trained on 1M+ DNA-protein pairs from 164 organisms, including S. cerevisiae and A. oryzae. ([GitHub](https://github.com/Adibvafa/CodonTransformer))
- **GenSmart, IDT, VectorBuilder** — Free web-based codon optimization tools. Cross-validate against CodonTransformer.

### Practical Setup

**Free tier (Google Colab):** ColabFold + ESM-2 + CodonTransformer + SPURS/RaSP = covers variant selection, codon optimization, and stability screening at zero cost.

**Colab Pro ($10/month):** Adds Boltz-2, RFdiffusion2, DiffDock for complex prediction, de novo design, and docking.

See [ai-bio-tools-playbook.md](../docs/ai-bio-tools-playbook.md) §Part 01b for full details, hardware requirements, and mapping to project prompts.

---

## GPT-Rosalind (OpenAI)

### What It Is

**Named after Rosalind Franklin**, GPT-Rosalind is OpenAI's first domain-specific reasoning model—trained directly on biological data including proteins, genes, chemical reactions, molecular pathways, and disease biology. It doesn't just answer biology questions better than GPT-5.4; it reasons differently because its training incorporated the structure of biological knowledge at a fundamental level.

Think of it: regular GPT-5.4 has read every biology paper. Rosalind was trained to **think in biological primitives** — amino acid sequences, gene regulatory networks, metabolic pathways, protein-protein interactions — the way you think in code architecture.

(Source: ai-bio-tools-playbook.md, §1)

### Capabilities

- **Protein structure prediction** (complementary to AlphaFold, reasoning about structure-function)
- **Codon optimization** (custom to specific organisms)
- **Gene expression analysis** (analyzing promoter strength, RBS, terminator compatibility)
- **Molecular interaction prediction** (protein-protein, RNA-protein, ligand-protein)
- **Drug candidate generation** (structure-based compound design)
- **Sequence-to-function interpretation** (what does this mutation do?)
- **Experimental planning** (design optimal assay workflows)
- **Multi-step literature review** with database cross-referencing (pulls from PDB, UniProt, NCBI, KEGG, ChEMBL)

(Source: ai-bio-tools-playbook.md, §1)

### Training Data

- 50 of the most common biological workflows
- Native access to: PDB, UniProt, NCBI, KEGG, ChEMBL, and other major public databases
- Protein folding trajectories
- Gene regulatory networks
- Metabolic pathway maps
- Disease biology literature

### Access Model

**Trusted Access Program** — limited to qualified US enterprise customers. Requires:
- Legitimate research with clear public benefit
- Governance and misuse-prevention controls
- Approved users in secure environments
- Currently a research preview (pricing TBD)

**Free alternative:** OpenAI shipped a **free Codex plugin** the same day connecting to 50+ biology databases. Works with GPT-5.4 (which most people already have access to). Codex adds database connectivity; Rosalind adds deeper biological reasoning. (Source: ai-bio-tools-playbook.md, §1)

### Specific Prompts for Open Enzyme

#### Prompt 1: Codon Optimization for Target Organism

```
You are a synthetic biology expert. I need to optimize the A. flavus uricase gene 
(GenBank X61766.1, 906 bp coding sequence) for expression in Saccharomyces cerevisiae.

Task:
1. Analyze the native A. flavus codon usage against S. cerevisiae codon preferences
2. Identify rare codons and potential issues (cryptic polyA sites, splice sites, secondary structures that interfere with expression)
3. Generate a codon-optimized version minimizing changes while maximizing expression efficiency
4. Maintain the protein sequence exactly (no amino acid changes)
5. Provide before/after codon usage comparison

Output format:
- Native sequence (1st 50 bp shown, then "...")
- Optimized sequence (1st 50 bp shown)
- Codon usage table comparison (native vs. S. cerevisiae optimal)
- Identified problem regions and fixes
```

**Expected output:** Detailed codon optimization with rationale. Can then submit to gene synthesis service (Twist, IDT, GenScript) with minor tweaks.

---

#### Prompt 2: Promoter and Regulatory Element Design

```
Design an expression cassette for A. flavus uricase in S. cerevisiae.

Requirements:
- Constitutive expression (always on, no glucose repression)
- Strong but not maximum (avoid metabolic stress; target ~5-10% of total protein)
- Suitable for food fermentation (no inducible systems that require chemicals)
- Include secretion signal for extracellular expression (optional second variant)

Cassette components needed:
1. Promoter recommendation (strength ranking vs. alternatives)
2. 5' UTR / RBS equivalent for yeast
3. Signal peptide options if secretion desired
4. Terminator selection
5. Selectable marker (mention both lab and food-production versions)

Output:
- Two cassette diagrams (intracellular vs. secreted)
- Justification for each component choice
- Expected expression levels based on known benchmarks
- Known failure modes (what could go wrong?)
```

**Expected output:** Practical design immediately usable for cloning; literature-backed recommendations.

---

#### Prompt 3: Literature Mining for Enzyme Variants

```
I need alternative uricase genes that could express well in Saccharomyces cerevisiae.

Known options:
- A. flavus uricase (rasburicase source; >20 years clinical use)
- C. utilis uricase (higher specific activity; less characterized in yeast)
- V. vulnificus uricase (published 2025 in S. boulardii; may work in S. cerevisiae)

Task:
1. Search literature (last 5 years) for uricase expression in heterologous systems
2. Identify any other organisms producing uricase that might express well in yeast
3. Compare specific activities (μmol/h/mg protein or equivalent)
4. Rank by likelihood of success in S. cerevisiae based on:
   - Protein size and quaternary structure
   - Cofactor requirements (if any)
   - Expression levels achieved in similar hosts
5. Highlight advantages/disadvantages of each

Output table:
- Gene source | Specific activity | Expression track record | Advantages | Disadvantages | Confidence rank
```

**Expected output:** Comparative analysis with citations. Informs gene selection for Phase 1 validation.

---

#### Prompt 4: Transformation Strategy Optimization

```
I'm transforming S. cerevisiae with a new uricase expression construct.

Goal: High transformation efficiency (>100 transformants per μg DNA) with stable integrants.

Current plan: Use chromosomal integration at a neutral locus, not episomal plasmid.

Questions:
1. Which loci in S. cerevisiae genome are "neutral" for high transgene expression?
   (Literature shows some loci give 100x higher expression than others)
2. What transformation method is best for chromosomal integration?
   - Lithium acetate (simple, ~90% efficiency with competent cells)
   - Electroporation (faster, more DNA control)
   - Agrobacterium tumefaciens (for A. oryzae, also works for some yeasts)
3. Selectable markers: recommend lab (G418, hygromycin) vs. food-safe (auxotrophic complementation, prototrophic)?
4. How many integrants should I screen, and what's the expected range of expression?
5. Any known problems with multi-copy integration at my target locus?

Output:
- Locus recommendation with expression expectations
- Transformation method + protocol summary
- Marker recommendation + rationale
- Quality control checkpoints (how to verify integration, verify expression)
```

**Expected output:** Strategic guidance that saves weeks of trial-and-error.

---

#### Prompt 5: Enzyme Activity Prediction and Assay Design

```
I've successfully expressed A. flavus uricase in S. cerevisiae. Now I need to assay activity.

Enzyme: Urate oxidase (uricase)
- Native MW: ~135 kDa (homotetrameric)
- pH optimum: 8.5-9.5
- Cofactors: None (unusual for oxidase; no metal or heme)
- Substrate: Uric acid
- Product: Allantoin (also produces CO2 and H2O2)

Questions:
1. What's the best assay method for high-throughput screening?
   - Spectrophotometric (measure uric acid decrease at 293 nm)
   - HPLC (separate uric acid, allantoin, intermediates)
   - Other?
2. Expected specific activity in our construct? (Benchmark from literature)
3. Assay protocol:
   - Buffer pH (8.5-9.5 optimal; physiological pH 7.4 for comparison)
   - Temperature (37°C for relevant, but stability at different temps?)
   - Time course (how long until plateau?)
   - Controls (positive: purified uricase; negative: non-transformed yeast)
4. Calculation: specific activity formula (μmol substrate consumed / min / mg protein)
5. What's the minimum activity level needed for therapeutic relevance?

Output:
- Recommended assay protocol (step-by-step)
- Expected values vs. benchmarks
- Troubleshooting guide (low activity? high variability?)
```

**Expected output:** Ready-to-execute assay protocol with success metrics.

---

#### Prompt 6: Fermentation Optimization

```
I have engineered S. cerevisiae expressing uricase. Now I need to ferment it for product.

Application: Daily oral supplement (lyophilized yeast powder)

Fermentation parameters to optimize:
1. Temperature: Standard S. cerevisiae fermentation is 25-30°C. Does uricase stability change this?
2. Aeration: Aerobic (faster growth, higher biomass) vs. anaerobic (traditional brewing)?
3. Media: YPD (yeast peptone dextrose standard) vs. minimal media?
4. Duration: Typical is 24-48h. Enzyme production profile?
5. Cell density at harvest: How high can we grow without stress?
6. Post-fermentation: Do we need special handling (pH adjustment, clarification)?
7. Drying method for shelf stability:
   - Heat drying (risk: denatures uricase)
   - Lyophilization (better; enzyme stability testing needed)
   - Spray drying (industrial scale)
8. Shelf life: What's expected stability at room temperature vs. refrigerated?

Output:
- Optimized fermentation protocol
- Enzyme stability profile over growth curve
- Recommended harvest point (maximum enzyme + viable biomass)
- Drying method recommendation with stability data
- Cost estimates (media, equipment, labor for scale-up)
```

**Expected output:** Fermentation SOP ready for manufacturing.

---

### Output Example: Rosalind Analyzing Uricase Expression

When given the above prompts, Rosalind might produce something like:

> **Codon Optimization Analysis:**
>
> Your A. flavus uaZ sequence uses 23 codons rare in S. cerevisiae (>1% frequency). Key problems:
> - Position 145-150 (rare CGA, CGA, CGA for Arg): introduces secondary structure blocking ribosome
> - Position 280 (CTT for Leu): rare even though Leu codons are usually okay
> - Positions 450-460: contains "AATAAA" (cryptic polyA signal that S. cerevisiae RNA polymerase recognizes)
> 
> Optimized version (sample):
> - Replace CGA (3% in S. cerevisiae) → CGC (50% frequency): increases expression ~2-fold at this motif
> - Replace CTT (8%) → CTC (40%): small gain (~1.1x)
> - Remove AATAAA context via silent codon change: prevents premature termination
> 
> **Predicted improvement:** 1.5-2.5× higher expression in S. cerevisiae with optimized codon usage alone.
> 
> **Recommended promoter:** pTEF1 (constitutive, ranked #1 for S. cerevisiae among 40+ options)
> - Strength: ~2500 FPKM in RNAseq studies (nearly maximal)
> - RBS context: AGGA (Kozak-like) upstream of start codon recommended
> - Integration site: HO locus (neutral, stably expressed, ~1-3 copy integration natural)

---

## Amazon Bio Discovery

### What It Is

Amazon's platform for high-throughput biological model screening and molecular design. ~40 pre-trained models covering:
- Protein function prediction
- Gene expression forecasting
- Metabolic pathway modeling
- Drug-enzyme interaction
- Strain fitness prediction

### Capabilities

- **Strain optimization:** Predict effects of genetic modifications before building them
- **Pathway engineering:** Model multi-step enzymatic cascades
- **Fitness prediction:** Will my engineered strain survive in fermentation?
- **Substrate specificity:** Will enzyme recognize the substrate I want?
- **Expression level forecasting:** What promoter+RBS combination gives highest yield?

### Access Model

Web-based platform; AWS account required. Free tier available for academic users.

### Specific Use for Open Enzyme

#### Use Case 1: Predict S. cerevisiae Growth with Integrated Uricase

**Input:**
- S. cerevisiae reference genome
- Proposed uricase gene insertion at HO locus
- pTEF1 promoter driving expression

**Model:** Strain fitness prediction

**Output:** 
- Predicted growth rate under fermentation conditions
- Metabolic burden estimate (% of total protein expression)
- Risk of metabolic stress (if too high)

This tells you: Will my engineered strain still grow robustly, or did I overexpress and slow growth?

---

#### Use Case 2: Pathway Engineering for Dual Koji

**Input:**
- A. oryzae native genome with lipase, protease, amylase genes
- Added A. flavus uricase gene
- Multi-gene expression modeling

**Model:** Metabolic pathway + expression competition

**Output:**
- Resource allocation: how much ATP/ribosomes go to each enzyme?
- Risk of imbalanced expression (uricase high, lipase crashes)
- Optimal RBS + promoter combinations for balanced expression
- Predicted total enzyme levels (per g rice)

This is crucial for [[engineered-koji-protocol]] design—too much uricase suppresses native enzymes.

---

#### Use Case 3: Probiotic Persistence Modeling

**Input:**
- S. boulardii fitness in mixed microbiota (simulated competition with other gut bacteria)
- Metabolic preferences (S. boulardii uses glucose; compete with E. coli for this resource)
- Fermentation conditions (pH, nutrient availability)

**Model:** Multi-organism ecosystem dynamics

**Output:**
- Predicted S. boulardii survival curves with/without engineered uricase
- Competitive advantage/disadvantage vs. wild-type
- Conditions that favor persistence (lower pH? higher lactate?)

---

### Example Amazon Query

```
Model Name: StrainFitness

Input:
- Organism: S. cerevisiae
- Integration: uricase (A. flavus uaZ) at HO locus
- Promoter: pTEF1 (constitutive, strong)
- Expression level target: 10% total protein

Question: Will my engineered strain grow acceptably in fermentation?

Output (expected):
- Growth rate: 0.42 h⁻¹ (wild-type ~0.45 h⁻¹; 7% reduction = tolerable)
- Doubling time: 98 min (vs. 92 min wild-type)
- Metabolic burden: 10% protein production is sustainable
- Recommendation: pTEF1 is appropriate; don't go to higher-expressing promoters
- Risk flags: None; proceed to build construct
```

---

## Coefficient Bio (Anthropic Acquisition)

### What It Is

Anthropic acquired Coefficient Bio in 2024 ($400M investment) to integrate biological reasoning into its AI models. The goal: Anthropic's models can now reason about protein sequences, molecular dynamics, and biological systems end-to-end.

### Capabilities

- **Protein engineering:** Claude can reason about amino acid changes and predict consequences
- **Literature synthesis:** Pull biology papers, cross-reference databases, generate hypotheses
- **Experimental design:** Plan complex multi-step molecular biology experiments
- **Safety assessment:** Evaluate engineered organisms for off-target effects
- **Technical writing:** Generate SOPs, experimental protocols, safety documents

### Access Model

Integrated into Claude API (available now for enterprise customers; roadmap for general access Q3 2026)

### Specific Use for Open Enzyme

#### Use Case 1: Literature Synthesis on NLRP3 Inhibitors

**Prompt to Claude:**

```
Synthesize a comprehensive map of every natural compound and approved drug that 
inhibits the NLRP3 inflammasome. For each, provide:
1. Mechanism (which chokepoint in the NLRP3 pathway?)
2. Dose range for humans
3. Published efficacy data (if available)
4. Safety profile
5. Accessibility (OTC vs. prescription vs. research chemical)

Focus on compounds relevant to gout. Cross-reference:
- PubMed (NLRP3 + compound name)
- ChEMBL (molecular structure, activity data)
- Clinical trial registries (Firsekibart, Dapansutrile, others)

Output: Structured table with ranking by evidence strength
```

**Expected output:** The [[nlrp3-inflammasome]] wiki page content—comprehensive, literature-backed, practically organized.

---

#### Use Case 2: Protocol Generation for Koji Engineering

**Prompt to Claude:**

```
Generate a complete, step-by-step protocol for:
1. Cloning the A. flavus uaZ uricase gene into an A. oryzae expression vector
2. Transformation of A. oryzae protoplasts
3. Screening and selection of high-expressing transformants
4. Fermentation on rice substrate
5. Dosing optimization for therapeutic use

Requirements:
- Suitable for a community biolab (not requiring BSL-2 containment)
- All reagents and equipment available from standard suppliers
- Costed out (total materials, labor, timeline)
- Safety checkpoints at each stage
- Troubleshooting guide for common failures

Output: Publication-quality protocol document (SOP format)
```

**Expected output:** [[engineered-koji-protocol]]-level detail, immediately executable.

---

#### Use Case 3: Strain Safety Assessment

**Prompt to Claude:**

```
I'm proposing to engineer S. cerevisiae with:
- A. flavus uricase gene (same as in rasburicase drug)
- Chromosomal integration (one copy)
- No antibiotic resistance markers (urea auxotrophy for selection)

Task: Comprehensively assess safety for human consumption as fermented food product.

Evaluate:
1. Protein (uricase) safety: FDA approval history, off-target activity, toxicity
2. Host organism (S. cerevisiae) safety: GRAS status, no pathogenic potential
3. Genetic construct safety: No oncogenic sequences, no hidden regulatory elements
4. Manufacturing safety: Fermentation contamination risks, shelf stability
5. Consumer use safety: Oral delivery, gut microbiota interactions, allergenic potential
6. Regulatory pathway: What would FDA require for "food product" vs. "drug"?

Output: Safety assessment document (white paper format) with:
- Risk summary
- Mitigation strategies
- Regulatory recommendations
- Unknowns (what still needs research?)
```

**Expected output:** Rigorous risk analysis that directly informs Phase 3 study design and potential regulatory strategy.

---

#### Use Case 4: Personalized Supplementation Stack Design

**Prompt to Claude:**

```
Generate a personalized anti-gout supplement stack for a 55-year-old male with:
- Serum uric acid: 8.2 mg/dL
- Recent gout flare (ankle, resolved but recurrent)
- No significant comorbidities (kidney function normal)
- Cannot tolerate allopurinol (rash)
- Interested in NLRP3 inflammasome targeting (not just uric acid lowering)

Task:
1. Design a multi-compound stack targeting multiple NLRP3 chokepoints
2. Each compound should have published human or animal evidence
3. Address drug-supplement interactions
4. Provide dosing, timing, sourcing
5. Cost breakdown
6. Monitoring biomarkers (to assess efficacy)
7. Timeline (when to escalate if not working)

Output: Personalized protocol document (similar to [[supplements-stack]] but individualized)
```

**Expected output:** [[supplements-stack]]-level detail but customized to one person's needs.

---

## Integration: Using All Three Tools Together

### Workflow Example: Design Engineered Koji from Scratch

**Step 1: Literature Mining (Claude/Coefficient)**
- Comprehensive search on A. oryzae genetic engineering capabilities
- Find all published cases of multi-gene expression in koji
- Identify best transformation methods and expression systems

**Step 2: Gene Selection (GPT-Rosalind)**
- Compare uricase genes: A. flavus vs. others
- Codon optimize for A. oryzae
- Design optimal expression cassette (promoter, RBS, terminator)

**Step 3: Fitness Prediction (Amazon Bio Discovery)**
- Model what happens when we add uricase to koji's native enzyme portfolio
- Predict growth rates, enzyme yields, metabolic balance
- Identify potential bottlenecks

**Step 4: Protocol Generation (Claude/Coefficient)**
- Write complete transformation and fermentation protocol
- Generate SOPs, safety assessments, troubleshooting guides
- Design validation experiments

**Step 5: Safety & Regulatory (Claude/Coefficient)**
- Comprehensive safety assessment
- Identify regulatory pathway (food vs. drug)
- Draft pre-clinical study plan

**Total timeline:** 2–4 weeks of design work (instead of months)

---

## Cautions & Limitations

### GPT-Rosalind

- **Training cutoff:** April 2026; newer papers not yet included
- **Overfitting risk:** Trained on common workflows; unusual cases may not be handled well
- **Verification required:** Always check Rosalind's literature citations; hallucinations possible
- **Limited access:** Only US enterprise customers (as of April 2026)

### Amazon Bio Discovery

- **Model quality varies:** Some models are validated, others are beta
- **Garbage in, garbage out:** Predictions depend on accurate input (genome sequences, parameters)
- **No real-time biology:** Models trained on static data; can't predict emergent properties

### Claude/Coefficient Bio

- **New capability:** As of April 2026, still in limited release
- **Domain-specific reasoning:** Excellent for design and synthesis; less good for predicting unexpected biological outcomes
- **Not a substitute for wet lab:** All recommendations must be validated experimentally

---

## Practical Recommendation

**For Open Enzyme project, in priority order:**

1. **Open source tools first** — ColabFold, ESM-2, SPURS/RaSP, CodonTransformer, DiffDock. Free, available now, quantitative outputs. These cover structure prediction, variant scoring, stability prediction, codon optimization, and docking — the core computational workflow.

2. **Use Claude for reasoning and synthesis** — literature mining, protocol generation, experimental design, safety assessment, cross-domain reasoning. Claude is the connective tissue that interprets open source tool outputs and makes design decisions.

3. **Try GPT-Rosalind if you get access** — deeper biological reasoning for complex design questions. Apply via the Trusted Access Program; the open source + therapeutic enzyme + citizen science angle is a strong public-benefit argument.

4. **Use Amazon Bio Discovery strategically** — the free trial (5 experiments) is worth using for lab-in-the-loop integration (routing to Twist/Ginkgo). The $486/month ongoing cost is harder to justify when open source covers most model capabilities.

**Monthly cost estimate:**
- Open source tools (Google Colab free tier): $0
- Google Colab Pro (if needed for GPU): $10/month
- Claude: $20 (subscription)
- GPT-Rosalind (if access granted): $0 (research preview)
- Amazon Bio Discovery: $0 (free trial) or $486/month (probably not needed)

**Total:** $20-30/month covers the full computational stack.

---

*These tools accelerate the design phase dramatically. But they do not replace experimental validation. Every prediction must be tested. [[validation-experiments]] remains the truth source.*

(Source: ai-bio-tools-playbook.md)
