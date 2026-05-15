---
title: Bio AI Tools
aliases: [AI-tools, AI-bio, GPT-Rosalind, Amazon-Bio-Discovery, Anthropic-Coefficient, computational-biology, protein-language-models, open-source-bio-AI]
related: [engineered-yeast-uricase, engineered-koji-protocol, validation-experiments, uricase, nlrp3-inflammasome, paperclip-deep-dive]
sources: [ai-bio-tools-playbook.md, paperclip-deep-dive.md]
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

```text
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

```text
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

```text
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

```text
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

```text
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

```text
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

```text
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

```text
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

```text
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

```text
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

```text
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

## Anthropic Life Sciences Marketplace (à la carte MCP servers + skills)

### What It Is

Anthropic's ["Bio Research" experience on claude.ai](https://claude.com/plugins/bio-research) is presented as a single plugin, but in Claude Code it ships as an **à la carte marketplace of 17 individual plugins** hosted at [github.com/anthropics/life-sciences](https://github.com/anthropics/life-sciences). Each plugin is either an MCP server (database access) or a skill (domain-specific workflow). You install only what you need — which for Open Enzyme is **better** than the bundled claude.ai experience, because Phase 0 doesn't need the wet-lab skills, and the oncology-leaning ones (Owkin, Medidata) aren't relevant at all.

**Critical for this project:** these plugins install in Claude Code, so the Open Enzyme workflow stays in the terminal where the wiki and sweep daemon live. No bouncing to claude.ai.

(Source: verified against [anthropics/life-sciences/.claude-plugin/marketplace.json](https://github.com/anthropics/life-sciences/blob/main/.claude-plugin/marketplace.json) — 17 plugins listed as of April 2026.)

### Installation in Claude Code

**Step 1 — register the marketplace (one-time):**

```text
/plugin marketplace add anthropics/life-sciences
```

**Step 2 — install the Phase 0 core (5 MCP servers):**

```text
/plugin install pubmed@life-sciences
/plugin install biorxiv@life-sciences
/plugin install clinical-trials@life-sciences
/plugin install chembl@life-sciences
/plugin install open-targets@life-sciences
```

> **Note on skills:** The claude.ai bundle exposes `/scientific-problem-selection` and other skills (`/start`, etc.), but these are **not exposed as installable plugins** in the Claude Code marketplace — the repo has directories for them, but `marketplace.json` only lists the MCP servers and a subset of skills. If you need problem-scoping help, ask Claude directly against `wiki/synthesis.md` — no skill required.

**Step 3 — reload and verify:**

```text
/reload-plugins
```

After reload, the MCP servers auto-attach as callable tools in every session in this repo, and the `/scientific-problem-selection` skill becomes available as a slash command. Most of the literature servers (PubMed, bioRxiv, ClinicalTrials.gov) work out of the box; Wiley and 10x Genomics Cloud request auth on first use.

### The Full Marketplace (17 plugins)

| Plugin | Type | Open Enzyme relevance |
|---|---|---|
| **pubmed** | MCP | **Install now.** Biomedical literature search. Biggest single win — replaces WebFetch for the sweep daemon and every new wiki page. |
| **biorxiv** | MCP | **Install now.** Preprint search. Newer uricase / koji / NLRP3 engineering work often lands here before peer review. |
| **clinical-trials** | MCP | **Install now.** ClinicalTrials.gov access. Track ALLN-346, Dapansutrile (OLT1177), Firsekibart, PULSE probiotic, Rilonacept. |
| **chembl** | MCP | **Install now.** Compound bioactivity database (IC50/Ki/Kd). Look up NLRP3 inhibitors, xanthine oxidase inhibitors, CB2 agonists in one query instead of parsing papers. |
| **open-targets** | MCP | **Install now.** Target–disease evidence platform. Validates target rationale for gout / EPI / SIBO. |
| **biorender** | MCP | Optional. Scientific illustration generation. Useful when publishing figures; not Phase 0 critical. |
| **synapse** | MCP | Optional. Sage Bionetworks collaborative data management. Install if/when collaborators join and we need a shared data platform. |
| **wiley-scholar-gateway** | MCP | Optional. Wiley journal access. Useful when a cited paper is paywalled. |
| **nextflow-development** | Skill | Defer. Runs nf-core pipelines (RNA-seq, variant calling, ATAC-seq) on local or public GEO/SRA data. Load-bearing when wet-lab sequencing data arrives. |
| **scvi-tools** | Skill | Defer. Deep-learning single-cell omics. Relevant for macrophage NLRP3 response phenotyping or gut immune cell atlases — future. |
| **single-cell-rna-qc** | Skill | Defer. Automated scRNA-seq QC following scverse best practices. Same future phase as scvi-tools. |
| **instrument-data-to-allotrope** | Skill | Defer. Converts raw plate-reader / HPLC / flow-cytometer output to Allotrope Simple Model format. Install when wet-lab data starts flowing. |
| **10x-genomics** | MCP | Defer. 10x Genomics Cloud access. Requires 10x API token; install only if single-cell / spatial experiments start. |
| **clinical-trial-protocol** | Skill | Defer. Generates FDA/NIH-compliant trial protocols. Relevant far downstream if/when Open Enzyme enters clinical evaluation. |
| **tooluniverse** | Skill | Optional. General-purpose scientific AI agents. Evaluate after the core MCP set is in place. |
| **owkin** | MCP | Skip. Oncology-focused collaborative biology agents. Not relevant to gout / EPI. |
| **medidata** | MCP | Skip. Clinical trial site ranking and platform help. Not relevant at Phase 0. |

### Workflow Mapping: Where the Plugin Fits in the Current Process

**1. Doc Sweep Daemon** (`scripts/wiki-watch.sh` → `scripts/sweep-prompt.md`)

Pass 1 of the sweep (propagate findings across wiki pages) currently uses Claude's general literature awareness. With the plugin installed, the sweep prompt can explicitly call PubMed + bioRxiv + ClinicalTrials.gov MCP servers to ground claims in current primary literature — raising the evidence floor without changing the file-watching infrastructure.

*Action:* Once the plugin is installed, update `scripts/sweep-prompt.md` to instruct the daemon to prefer PubMed/bioRxiv MCP over WebFetch for biomedical claims.

**2. Action Queue Pruning** (`wiki/synthesis.md`)

The synthesis queue is prose + bullets. `/scientific-problem-selection` is purpose-built to convert an unranked list of candidate investigations into a scored, scoped ranking. Run it against the current synthesis queue to produce a ranked action list without ad-hoc prioritization.

**3. Compound / Target Research** (cannabinoids-terpenes.md, nlrp3-inhibitor-screen.md, etc.)

Future compound deep dives can query ChEMBL for canonical bioactivity data (IC50, Ki, Kd) and Open Targets for target–disease evidence before touching web searches. This reduces citation-hunting for the "benchmark compounds" sections we keep building out.

**4. Clinical Pipeline Tracking** (uricase, NLRP3 drugs)

`index.md`'s `Clinical Precedent` references (ALLN-346, Rasburicase, PULSE, Dapansutrile) are currently checked manually. A quarterly ClinicalTrials.gov MCP pull keeps these rows current.

**5. Literature Front-Door for New Pages**

New wiki pages (like the cannabinoids page we just graduated) start with a literature scan. With the plugin, that scan is PubMed MCP + bioRxiv MCP in one structured call rather than a WebSearch chain.

### What This Replaces vs. What Stays

| Task | Before plugin | After plugin |
|---|---|---|
| Biomedical literature search | WebSearch + WebFetch (fragile, scraping) | PubMed / bioRxiv MCP (structured) |
| Compound bioactivity lookup | Read individual papers | ChEMBL MCP |
| Target–disease evidence | Wiki page synthesis | Open Targets MCP |
| Clinical trial status | Manual ClinicalTrials.gov browsing | ClinicalTrials.gov MCP |
| Problem ranking / experiment prioritization | Ad-hoc in `synthesis.md` | `/scientific-problem-selection` |
| Protein structure / docking / design | ColabFold, Boltz-2, RFdiffusion2, DiffDock | **Unchanged** — the plugin is research/literature-oriented; core computational biology stays with the open-source stack |
| Codon optimization | CodonTransformer | **Unchanged** |
| Stability prediction | SPURS, RaSP, DDGemb, FoldX | **Unchanged** |

The plugin augments the **research and reasoning** layer. The computational biology layer (structure, design, stability, docking) stays open-source; the plugin doesn't replace it.

### Limitations

- **MCP servers are Anthropic-hosted and opaque** — you can't swap in a different PubMed backend or override auth. For 99% of use cases this doesn't matter, but it means the sweep daemon's literature sourcing is only as current as Anthropic keeps the servers.
- **Skills are bundled, not hand-editable** — unlike a `.claude/skills/` directory, these live inside the plugin package. Customization means forking the plugin or adding complementary skills alongside.
- **No offline mode** — remote HTTP MCP servers require network. The sweep daemon still runs locally, but skill calls that hit the plugin need connectivity.

### How It Differs from OpenAI's Codex Life Sciences Plugin

Covered in [ai-bio-tools-playbook.md](./ai-bio-tools-playbook.md) §Codex. Both connect Claude / GPT to life-science databases. The Bio Research plugin is tighter (10 curated servers + 6 vetted skills) where Codex is broader (50+ databases, looser scaffolding). For Open Enzyme, which runs inside Claude Code, the Bio Research plugin wins on environment fit — it stays in the terminal with the wiki.

---

## Paperclip (GXL) — Agent-Native Scientific Literature MCP

[Paperclip](https://paperclip.gxl.ai/) is an MCP server built by GXL (Generative Expert Labs), a Stanford-adjacent group connected to James Zou's lab. It exposes scientific literature to an LLM as a structured filesystem — search, grep, cat, map, and SQL operations chain through a stateful `results_id`, so an agent can narrow a corpus iteratively without re-searching. See [paperclip-deep-dive.md](./paperclip-deep-dive.md) for full documentation.

(source: paperclip-deep-dive.md)

### Corpus

| Source | Coverage | Type |
|---|---|---|
| PubMed Central | ~5M+ | Full text, biomedical, open access |
| arXiv | ~3M | Full text, ML / math / quant-bio / physics / CS |
| bioRxiv + medRxiv | ~3M+ | Full text, preprints |
| OpenAlex | ~150M+ | Abstracts + structured metadata only |

Total: ~11M full-text papers + ~150M abstracts. Coverage caveats: PMC has embargo periods for some journals; only open-access full text is indexed. (source: paperclip-deep-dive.md)

### Key Commands

| Command | Function |
|---|---|
| `search` | Hybrid (BM25 + vector embedding) search; returns 1–2 sentence TL;DRs |
| `grep` | Regex / keyword search within full text |
| `cat` | Reads structured paper text (sections, tables, figures) |
| `map` | Applies a prompt across a result set — the synthesis primitive |
| `ask-image` | Multimodal query against figures and images |
| `--from <results_id>` | Chains operations against a previous result set |

The `--from` chaining is the load-bearing feature: every search produces a cloud-stored `results_id`, and subsequent grep / map / cat operations can target it without re-searching. (source: paperclip-deep-dive.md)

### Setup

```
claude mcp add --transport http paperclip https://paperclip.gxl.ai/mcp
```

Currently free; no API key required. Pricing tiers not yet announced. (source: paperclip-deep-dive.md)

### Relationship to the Anthropic Life Sciences Marketplace

Paperclip is **complementary, not a replacement** for the Anthropic marketplace plugins:

- **Marketplace wins on per-source depth:** PubMed's MeSH vocabulary index, ChEMBL's bioactivity tables, Open Targets' target–disease evidence — these are best-in-class for their specific sources.
- **Paperclip wins on full-text search and cross-source synthesis:** searching *within* papers, cross-domain queries spanning biomedical + ML, multi-paper synthesis via `map`, and agent-driven workflows that need stateful corpus narrowing.

**When to use Paperclip for Open Enzyme:**
- Uricase mutation landscape — search + grep + map across PMC and arXiv to catalog published variants, hosts, catalytic parameters, immunogenicity (complements `uricase.md`, `crispr-uricase.md`, `engineered-koji-protocol.md`)
- NLRP3 inhibition mechanisms — map across the NLRP3 corpus for dosing and efficacy data (complements `nlrp3-exploit-map.md`, `nlrp3-inhibitor-screen.md`)
- Koji / *A. oryzae* expression systems — cross-reference food-science and synthetic-biology literature for promoter / cassette / yield data (expands `aspergillus-oryzae.md`, `koji-endgame-strain.md`)
- Cross-domain queries — e.g., grep for "uricase" + "food-grade" or "ABCG2" + "probiotic" across the full corpus to surface intersections that PubMed and Scholar fragment
- arXiv coverage for protein language models, directed-evolution algorithms, and novel delivery vectors (keeps `bio-ai-tools.md` current without bouncing between PubMed and arXiv)

(source: paperclip-deep-dive.md)

### Reliability — Trust Ranking by Tool (2026-05-05 verification)

A first end-to-end test (uricase variant landscape + *A. oryzae* expression evidence) surfaced a systematic hallucination pattern in the `map` operator. (source: paperclip-deep-dive.md)

| Tool | Reliability | Notes |
|---|---|---|
| `search` | **High** | Returns real PMC / bioRxiv / arXiv records with accurate IDs and titles |
| `cat /papers/<id>/meta.json` | **High** | Authoritative paper metadata — use as ground truth for abstract-level claims |
| `grep PATTERN /papers/<id>/...` | **High** | Returns real text from indexed paper bodies |
| `cat /papers/<id>/content.lines` | **High** | Real full-text |
| `map --from <id> "extract X"` | **LOW — hallucinates quantitative data and misattributes organisms** | Lighter reader model substitutes plausible-looking domain values when full text doesn't support the requested field |
| `reduce --from <map-id> ...` | **Compounding risk** | If underlying `map` is wrong, `reduce` consolidates wrong claims into a confident-looking summary |

**Verification discipline for any Paperclip session:** (1) Use `search` and `grep` as primary evidence; treat `map` as hypothesis-generation only. (2) Grep-verify every load-bearing number against the paper body. (3) Anchor identity claims (organism, gene, host) to `meta.json`. (4) Never propagate `reduce` summaries directly. (5) Check computational vs. wet-lab status from the abstract or methods section. (source: paperclip-deep-dive.md)

### Sweep-Daemon Integration — DECIDED 2026-05-05: Do Not Integrate

**Decision: do not wire Paperclip into the three-pass sweep daemon.** A verification test (uricase variant landscape, ~12 papers with known-correct ground truths) revealed a systematic hallucination pattern in the `map` operator that is disqualifying for any automated pipeline. (source: paperclip-deep-dive.md)

**Concrete hallucination examples from the 2026-05-05 test** (In Vitro / verification):

| Paper | Abstract / body says | `map` returned |
|---|---|---|
| PMC9773812 (Najjari 2022, PASylated UOX) | *A. flavus* UOX, K<sub>m</sub> 52.61 µM | *A. globiformis* uricase variant, K<sub>m</sub> 0.007 mM (~7,500× off) |
| PMC4881585 (Xie 2016, chimeric uricase) | Porcine-human exon-replacement chimera | *P. chrysogenum*-human exon chimera (different organism) |
| PMC10561068 (Yan 2023, *Arthrobacter* CSAJ-16) | Optimal T 20°C, K<sub>m</sub> 0.048 mM | Optimal T 40°C, K<sub>m</sub> 0.015 mM |
| PMC12106716 (Rahbar 2025, A. flavus disulfide design) | Pure computational paper — no wet-lab | Invented Tm, K<sub>m</sub>/k<sub>cat</sub> measurements; named non-existent mutation pair |

These are confabulations — plausible-looking values that would pass casual review but are not in the underlying full text. Wiring this into the sweep would inject a structured external hallucination source into a corpus designed for PhD-grade rigor.

**Reopen condition:** if GXL ships a verified upgrade of the `map` reader model and the uricase variant probe (~12 papers, multiple known-correct ground truths via abstract + grep) passes cleanly, revisit. Until then Paperclip remains a manual-research-only tool. (source: paperclip-deep-dive.md; Mechanistic Extrapolation)

### Limitations

- PMC embargo lag: recent high-impact papers in non-OA journals will be abstract-only
- Rate limits: untested for sustained automated query volume
- Pricing: currently free; plan for the possibility of usage limits
- MeSH vocabulary searches not supported (use PubMed MCP for those)

(source: paperclip-deep-dive.md)

---

## BioDesignBench — LLM Agent Evaluation for Protein Design

**Status: VERIFIED 2026-05-15** — full PDF read via `pdftotext` after Brian provided local copy (bioRxiv web layer + Cloudflare blocked headless WebFetch; bioRxiv API surfaced only abstract + metadata; the bioRxiv MCP server in OE's stack was failing to connect at the time of verification).

Kim & Romero (Duke University), bioRxiv [10.64898/2026.05.06.723381](https://www.biorxiv.org/content/10.64898/2026.05.06.723381v1) — "Benchmarking and behavioral characterization of LLM agents for protein design." Posted 2026-05-08. NIH R01GM150929. **Note: DOI prefix is `10.64898/`, not `10.1101/` — bioRxiv migrated DOI registrars; references using the old prefix are wrong.**

### What the paper actually finds

The headline finding is **behavioral, not capability-limited.** Top LLM agents (DeepSeek V3, GPT-5) can match or exceed a deterministic hardcoded pipeline at protein design but consistently underperform expert practice — and the gap is **not** that they pick the wrong tools. The gap is that they **evaluate candidate designs too shallowly, never compare alternatives, and never discard candidates**:

- Scoring/evaluation tools invoked at only **~14% of expert intensity** (Fig. 3c)
- **No LLM condition ever discarded a generated candidate across all 836 task–condition observations** (Section 2.4) — agents treat stochastic samples as deterministic answers
- Evaluation-variety vs. score: Spearman ρ = 0.68 (p < 10⁻¹¹⁵; n = 836)
- Forced-depth intervention (≥3 evaluation-metric categories per candidate, compute-matched against shallow control): DeepSeek V3 +9.3 points (p = 0.002), GPT-5 +15.9 points (p < 0.001) — gains concentrated in Approach + Orchestration, not structural Quality
- The hardcoded pipeline (which already has multi-metric evaluation built into its fixed workflow) gains nothing from the forced-depth intervention (∆ = 1.6, n.s.) — confirming the deficit is **specifically behavioral**, not generic compute

### Leaderboard (full benchmark; mean total score out of 100)

| Condition | Score |
|---|---|
| Human oracle (expert-curated optimal tool sequence per task — benchmark ceiling) | 75.2 |
| Human expert (single practitioner, same 17 MCP tools as agents) | 61.7 |
| **DeepSeek V3 unguided** | **60.6** |
| DeepSeek V3 guided | 58.6 |
| GPT-5 unguided | 55.8 |
| GPT-5 guided | 55.4 |
| Hardcoded pipeline (deterministic 4-stage; non-LLM reference) | 54.5 |
| Claude Sonnet 4.5 guided | 50.5 |
| Claude Sonnet 4.5 unguided | 41.2 |
| Gemini 2.5 Pro guided | 8.8 |
| Gemini 2.5 Pro unguided | 8.1 |

DeepSeek V3 significantly outperformed all other LLM conditions (Wilcoxon signed-rank with Bonferroni correction; p < 0.05). Gemini 2.5 Pro's near-zero score is attributed by the paper to "a systematic tool-calling failure rather than poor scientific reasoning."

### Tool-gap vs. science-gap (the GAP tag pilot's empirical anchor)

The paper's Section 2.3 + Supplementary G formally decompose agent failures into:
- **Tool gap** — correct plan, failed execution (knew what to do, fumbled the toolchain)
- **Science gap** — wrong plan altogether (didn't understand the biology)

Per-model dominance (guided mode, all 76 tasks): **DeepSeek V3 and GPT-5 dominated by tool gap; Gemini 2.5 Pro dominated by science gap** across all molecular subjects.

This empirically grounds the GAP tag pilot wired into OE's Pass 3 prompts on 2026-05-15. Operational definitions, pilot scope, promote/abandon gates: [`scripts/SWEEP-ARCHITECTURE.md` §"Pilot — Tool-Gap vs. Science-Gap Disagreement Attribution"](../scripts/SWEEP-ARCHITECTURE.md).

### Task taxonomy (76 tasks, 5×2 matrix)

| | De novo (n=47) | Redesign (n=29) | Total |
|---|---|---|---|
| Antibody | — | — | 9 |
| **Enzyme** | — | — | **12** |
| Mini-protein binder | (all) | empty | 19 |
| Scaffold | — | — | 25 |
| Fluorescent protein | — | — | 11 |

Binder × redesign is biologically empty. **Per-task specifications are deliberately not publicly released** to prevent data contamination of future LLM training — only condition-level aggregates are available via the leaderboard. Per-task data requires a data use agreement with the authors. All tasks drawn from 2024–2026 publications, post-cutoff for evaluated models.

### Tool integrations — the 17-tool MCP package

The paper exposes all 17 protein-design tools through a **single MCP interface** (`github.com/jasonkim8652/protein-design-mcp`, MIT licence, Docker images for reproducible deployment). Four functional categories:

| Category | Tools | OE-pipeline status |
|---|---|---|
| Generative | RFdiffusion, ProteinMPNN, ESM-IF | RFdiffusion + ProteinMPNN **NOT currently in OE stack — gap to investigate for DAF SCR1-4 + lactoferrin redesign work** |
| Predictive (structure) | AlphaFold2, AlphaFold3, Boltz-2, ESMFold | AlphaFold2 in OE stack via ColabFold; AlphaFold3 / Boltz-2 / ESMFold not yet integrated |
| Physics-based | Rosetta / PyRosetta, DSSP | **Not currently in OE stack** |
| Analysis | Interface metrics, TM-align, sequence identity | TM-align / sequence identity available; interface-metrics not yet integrated |

The protein-design-mcp package is **directly deployable** — OE could mount it as a sibling MCP server to abent-somm, papercip, pubmed, etc.

### What this means for OE

1. **OE's existing N-of-M concordance methodology (comp-022 with N-of-5 ≥ 4 across CAI / ViennaRNA / chaperone-load / promoter-SP / ESM2) IS the BioDesignBench-recommended cure** for the shallow-evaluation failure mode. The paper validates the methodology empirically.
2. **Audit OE's other comp-NNNs for shallow-eval risk.** comp-019 (5-metric flux Monte Carlo) and comp-022 are clearly multi-metric; comp-023, comp-024, comp-025, comp-026, comp-027 should be audited against three axes — (a) multiple candidates generated? (b) multi-metric evaluation? (c) head-to-head comparison + filtering? Audit table at [`autonomous-screening-methodology.md` §"BioDesignBench evaluation-depth audit"](./autonomous-screening-methodology.md).
3. **Tool-stack gap is concrete and addressable.** For OE's DAF SCR1-4 + lactoferrin redesign work, RFdiffusion + ProteinMPNN are the canonical de-novo / sequence-design tools that the protein-design-mcp package would unlock at near-zero integration cost.
4. **Citation hook.** Direct reference for both [`autonomous-screening-methodology.md`](./autonomous-screening-methodology.md) §"Computational-to-wet-lab handoff: N-of-M concordance" and the cross-vendor heterogeneity-guard paper draft.

### Code + leaderboard (public)

- **Framework**: [github.com/RomeroLab/BioDesignBench](https://github.com/RomeroLab/BioDesignBench) (MIT)
- **17-tool MCP**: [github.com/jasonkim8652/protein-design-mcp](https://github.com/jasonkim8652/protein-design-mcp) (MIT; Docker images + pip package)
- **Leaderboard**: [huggingface.co/spaces/RomeroLab-Duke/BioDesignBench-Leaderboard](https://huggingface.co/spaces/RomeroLab-Duke/BioDesignBench-Leaderboard) — accepts new agent submissions; returns scores from deterministic evaluation pipeline

### Deployment status — OE locally deployed 2026-05-15 (CPU mode, partial)

`pip install protein-design-mcp` (v1.0.0) + `protein-design-mcp-setup --local --client claude-code -y`. Local Python config written to `~/.claude/mcp.json` invoking `python3 -m protein_design_mcp.server`. Loads on next Claude Code session start (not current session).

**9 of 19 tools active in CPU mode:**

| Status | Tools | Why disabled |
|---|---|---|
| **Active (CPU)** | `predict_structure`, `predict_complex`, `score_stability`, `energy_minimize`, `analyze_interface`, `validate_design`, `suggest_hotspots`, `get_design_status`, `design_sequence` / `optimize_sequence` (CPU-slow but functional via ProteinMPNN) | — |
| **GPU-required** | `design_binder`, `design_fold`, `generate_backbone` (RFdiffusion-backed) | No NVIDIA GPU on Mac. Apple Silicon MPS port spec'd in `abent-family-health/brian/open-enzyme-backlog.md` (A4 task) |
| **PyRosetta-required** | `rosetta_score`, `rosetta_relax`, `rosetta_interface_score`, `rosetta_design` | UW export-control review of academic PyRosetta license, in effect since 2026-04-01. Email license@uw.edu queued 2026-05-15. When unblocked: `pip install "protein-design-mcp[rosetta]"` |
| **Boltz-2-required** | `predict_structure_boltz`, `predict_affinity_boltz` | Boltz-2 requires isolated torch venv (conflicts with RFdiffusion torch==2.0.1); not installed. Defer until either RFdiffusion port lands or separate venv setup |

**Deployment decisions captured:**
- **A1 (CPU-mode local install)** — done 2026-05-15. Covers DAF SCR1-4 + lactoferrin redesign without RFdiffusion. ProteinMPNN slow on CPU but functional.
- **A2 (Modal cloud GPU)** — not pursued. Fallback option if RFdiffusion becomes load-bearing before A4 lands.
- **A4 (Apple Silicon MPS port)** — backlogged at [`abent-family-health/brian/open-enzyme-backlog.md`](../../abent-family-health/brian/open-enzyme-backlog.md) §"Next up → In-silico." YaoYinYing's fork has a working MPS branch (~13 min/design vs. ~30–60s on NVIDIA); SE3-Transformer NVTX/DGL surgery + Mac-native build. Spec session planned for tonight or tomorrow.

**Ghcr.io Docker image pull failed during setup** with `unauthorized` error (the public image at `ghcr.io/jasonkim8652/protein-design-mcp:latest` is apparently access-gated). Local Python path used instead. If Modal cloud deployment becomes the right move (A2), the Modal proxy entry point is `protein-design-mcp-modal`.

(Source: Kim & Romero 2026, bioRxiv 10.64898/2026.05.06.723381; verified against full PDF at `/private/tmp/claude-501/biodesignbench.txt`, 2026-05-15. Original "Cloudflare blocked direct fetch 2026-05-12" PRIMARY-SOURCE-PENDING flag was lifted via Brian-provided local PDF copy + pdftotext extraction; the structural failure mode was treating a single failed fetch attempt as a durable gate without trying alternative tools — see [`memory/feedback_dont_treat_single_failed_fetch_as_durable_gate.md`](../../../.claude/projects/-Users-brianabent-Documents-Claude-Projects-abent/memory/feedback_dont_treat_single_failed_fetch_as_durable_gate.md).)

---

## Integration: Using All Three Tools Together

### Workflow Example: Design Engineered Koji from Scratch

**Step 1: Literature Mining (Bio Research plugin → PubMed + bioRxiv MCP)**
- Comprehensive search on A. oryzae genetic engineering capabilities
- Find all published cases of multi-gene expression in koji
- Identify best transformation methods and expression systems
- Cross-reference with ClinicalTrials.gov for any enzyme-replacement gout trials

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

1. **Install the Phase 0 core from Anthropic's life-sciences marketplace in Claude Code** — `/plugin marketplace add anthropics/life-sciences`, then install `pubmed`, `biorxiv`, `clinical-trials`, `chembl`, and `open-targets` (each as `/plugin install <name>@life-sciences`), then `/reload-plugins`. This is the single highest-leverage change: literature, trials, and compound databases move from web-scraping to structured MCP calls without leaving the terminal. Immediate wins on sweep daemon quality and new-page literature scans. Defer the wet-lab skills (`nextflow-development`, `scvi-tools`, `single-cell-rna-qc`, `instrument-data-to-allotrope`) until wet-lab data arrives.

2. **Open source tools for computational biology** — ColabFold, ESM-2, SPURS/RaSP, CodonTransformer, DiffDock. Free, available now, quantitative outputs. These cover structure prediction, variant scoring, stability prediction, codon optimization, and docking. The plugin doesn't replace them; it complements them.

3. **Use Claude (with the plugin) for reasoning and synthesis** — literature mining (now via PubMed/bioRxiv MCP), protocol generation, experimental design, safety assessment. Claude is the connective tissue that interprets open source tool outputs and makes design decisions.

4. **Try GPT-Rosalind if you get access** — deeper biological reasoning for complex design questions. Apply via the Trusted Access Program; the open source + therapeutic enzyme + citizen science angle is a strong public-benefit argument.

5. **Use Amazon Bio Discovery strategically** — the free trial (5 experiments) is worth using for lab-in-the-loop integration (routing to Twist/Ginkgo). The $486/month ongoing cost is harder to justify when open source covers most model capabilities.

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
