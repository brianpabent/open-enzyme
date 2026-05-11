---
title: Bridge recombinase + AlphaGenome — platform-capability dossier
date: 2026-05-10
status: working-note
tags: [genome-editing, bridge-recombinase, alphagenome, microbiome, hgt, regulatory-genomics, platform]
---

# Bridge recombinase + AlphaGenome

Working notes, not a post. Two platform-level capability shifts that landed this spring and that should change how Open Enzyme thinks about pathway portability and variant-effect prediction. Source for the prompt: a tweet from `@Doudna_lab` (verified) on 2026-05-10 announcing bridge-recombinase work, and the AlphaGenome page at deepmind.google/science.

The two are unrelated mechanistically (one rewrites DNA, one predicts what DNA does), but they show up together because they're both *2025-2026 step-changes* that arrived without much fanfare relative to the impact. The dossier covers each individually, then where they connect for OE.

---

## Part 1 — Bridge recombinases

### The tweet, briefly

`@Doudna_lab` is the verified handle of the Doudna lab at IGI / UC Berkeley. The tweet announces bridge-recombinase work for "genome-scale editing across diverse bacterial systems, microbiome editing, and programmable horizontal gene transfer." All three phrases map to a single April 2026 bioRxiv preprint from IGI-affiliated authors (Patel, Swartz et al.). The Doudna lab is amplifying it pre-peer-review; she is at minimum institutionally vouching. Senior-authorship status not fully confirmed from public summaries.

### The 2024 → 2026 arc

Three connected milestones, not one:

| When | What | Lab |
|---|---|---|
| **June 2024 (Nature 630:984)** | Bridge RNAs discovered. The IS110 family of bacterial mobile elements produces a bispecific guide RNA: one loop binds the mobile element, the other binds target DNA, each independently programmable. Demonstrated in *E. coli*: 60%+ insertion, 94%+ specificity. | Durrant, Perry, Hsu (Arc Institute / Berkeley) |
| **2026 Science (back-to-back, `adz0276` + `adz1884`)** | Bridge recombinases ported to **human cells**. ISCro4 ortholog identified by screening dozens of variants. Deep mutational scanning + RNA engineering → 20% insertion, 82% specificity, **megabase-scale** rearrangement (up to 0.93 Mb), Friedreich's GAA-repeat excision (>80% elimination), BCL11A enhancer removal (the FDA-approved sickle-cell target replicated). | Hsu / Konermann / Perry (Arc Institute) |
| **April 29, 2026 (bioRxiv 10.64898/2026.04.29.721476)** | Bridge recombinases work **across the bacterial tree of life** (5 phyla). 142 kb insertions at >90% efficiency, 2.3 Mb inversions, 50 kb excisions, **metagenomic editing in human gut microbiomes**, **programmable interphylum HGT** of intact pathway clusters. | Patel, Swartz et al. (IGI / Berkeley) — this is the tweet |

### Why this is regime-change vs CRISPR-Cas9

CRISPR-Cas9 cuts → double-strand break → cell's repair machinery does NHEJ (error-prone) or HDR (template-dependent, inefficient). Properties that follow:

- Scarring, off-targets, indel byproducts
- ~kilobase ceiling for clean, programmable insertion
- Megabase-scale rearrangement is essentially out of reach
- Repeat-rich and heterochromatic regions break Cas9

Prime editing and base editing solve precision at the single-nucleotide / short-insert end. Nothing in the CRISPR toolkit does multi-megabase rearrangement cleanly.

Bridge recombinases use a **DSB-free** recombination mechanism (closer to serine integrases mechanistically, but with RNA-guided retargeting). Three properties that compound:

1. **Multi-kb to megabase substrates.** 142 kb insert at >90% in bacteria. 2.3 Mb inversion. That's pathway-scale and chromosome-arm-scale, not gene-scale.
2. **No double-strand break.** Scarless joining. No NHEJ artifacts. Much friendlier for repeat-rich and heterochromatic regions where Cas9 self-destructs.
3. **Both ends programmable.** One bridge RNA loop addresses target, the other addresses donor — mix and match. That's what lets one toolkit do *insertion, inversion, and excision*, and what lets the bacterial paper move whole **pathways** between phyla.

Friedreich's ataxia is the canonical "CRISPR can't do this" demo: trinucleotide-repeat expansions are exactly where Cas9 stumbles, and bridge recombinases knocked >80% of them out cleanly.

### The bacterial / microbiome paper specifically

Three load-bearing claims from the Patel et al. preprint:

1. **Bacterial tree of life coverage.** Isolates across 5 phyla edited. The recombinase isn't host-restricted by an obscure cofactor; it works wherever cargo can be delivered. This is the chassis-agnostic property.

2. **Metagenomic editing in human gut microbiomes.** The headline. What "metagenomic editing" actually means here matters a lot — possibilities range from (a) edits on ex vivo stool extracts under selection, (b) edits in defined synthetic communities, (c) edits in gnotobiotic mice, (d) edits in live human gut samples. The preprint's public summary is ambiguous; the methods section is decisive. Even (a)-(b) would be notable; (c)-(d) would be transformative. **Open question for follow-up.**

3. **Programmable interphylum HGT of pathway clusters.** Captured chromosomal pathways and transferred them between phyla. This is where "horizontal gene transfer" stops being a metaphor and becomes a programmable operation: tell the system "pick up this 50-142 kb pathway from organism A, install it at locus X in organism B," and it does it without cloning into a vector first.

Author affiliations include Spencer Diamond (metagenomics) and Suzanne Devkota (gut microbiome / IBD), which suggests the microbiome work is real microbiome biology, not just *in vitro* on a single isolate.

### Skepticism

- **Preprint, not peer-reviewed.** April 29, 2026. The Doudna lab account amplifying it pre-review is itself a signal worth tracking. Numbers may move.
- **"Metagenomic editing in human gut microbiomes" needs the methods read.** As above.
- **Delivery in situ is unsolved at scale.** Editing a strain in a Petri dish is one thing; getting the bridge-recombinase machinery into the right strain in a living gut is the field's hard problem. Phage delivery, conjugation, or nanoparticle approaches all have their own failure modes. This paper probably doesn't solve it.
- **Off-target landscape in complex genomes.** 82% specificity in human cells is great for a first-gen tool and unacceptable for a clinic. Bacterial off-targets at the 50-142 kb cargo scale could break essential operons if mis-targeted. Need to see the specificity profiling.
- **"Programmable HGT" framing is marketing-flavored.** The mechanism is closer to programmable transposition than to true conjugation/transformation. Fine, but worth keeping straight.

### Implications for OE

- **The koji chassis is one expression of pathway portability, not the only one.** If bridge recombinases can lift a 50-142 kb biosynthetic cluster from a soil actinomycete and install it intact in a tractable GRAS host — koji, *Bacillus subtilis*, *S. cerevisiae*, *L. lactis* — the design space gets a lot wider. The chassis-selection page in the wiki probably needs an update naming this as an emerging route. Not a commitment to it. Just naming it.
- **Microbiome therapeutics — direct path.** OE's uricase + gut-degrader thesis currently leans on strain replacement (engineered *S. boulardii*, *L. lactis*, etc. with uricase) which has to colonize and persist against the resident community. Bridge-recombinase metagenomic editing flips the problem: edit a resident strain that's already won. "Install a urate-degrading pathway into a stable resident *Bacteroides*" becomes a tractable question rather than a fantasy. Same logic for any gut-derived intervention.
- **Programmable HGT as a platform primitive.** For OE's "open biology platform" framing, interphylum pathway transfer is worth naming as a capability primitive, even before it's ready for prime time. The community-assembly story — building polyfunctional consortia by editing in place rather than designing from scratch — is the part of this that's genuinely new.

### What to read next

1. Patel et al. bioRxiv methods + figures, specifically the gut microbiome demo. Pin down what "metagenomic editing" means.
2. Whether Doudna is senior or one-of-many — affects how strongly to read the tweet as official endorsement vs. amplification.
3. Serine integrase background literature (the closest mechanistic analogue) for context on long-term integration stability and rearrangement landscape.

### Source list (Bridge)

- `https://www.biorxiv.org/content/10.64898/2026.04.29.721476v1` — Patel, Swartz et al. 2026 bacterial preprint
- `https://www.science.org/doi/10.1126/science.adz0276` — Megabase-scale human genome rearrangement (Science 2026)
- `https://www.science.org/doi/10.1126/science.adz1884` — Programmable genome editing in human cells (Science 2026)
- `https://www.nature.com/articles/s41586-024-07552-4` — Durrant et al. original bridge RNA paper (Nature 2024)
- `https://www.nature.com/articles/s41587-026-03071-x` — Nat Biotech research highlight (2026)
- `https://arcinstitute.org/news/bridge-recombinases-human-cells` — Arc Institute summary

---

## Part 2 — AlphaGenome

### The TL;DR

DeepMind's regulatory-genomics foundation model. Takes a 1 Mb DNA sequence in, predicts 11 different regulatory readouts across 5,000+ human tracks and 1,000+ mouse tracks. Beats prior SOTA (Enformer, Borzoi) on 25 of 26 variant-effect-prediction benchmarks. Preprint + blog June 2025, *Nature* publication January 2026, **source code open-sourced January 2026**.

### What it actually predicts

11 output modalities from a single forward pass:

- Gene expression (RNA-seq tracks)
- Transcription initiation (CAGE-seq)
- Chromatin accessibility (ATAC-seq, DNase-seq)
- Histone modifications (ChIP-seq for H3K27ac, H3K4me3, etc.)
- Transcription factor binding (ChIP-seq across hundreds of TFs)
- Chromatin contact maps (Hi-C / Micro-C-like, 3D structure)
- Splice site usage
- Splice junction coordinates
- Splice junction strength
- (and others — total 11 across the 5,000+ tracks)

The headline use case is **variant effect prediction**: given a single SNV or short indel anywhere in the 1 Mb window, predict the change in all 11 modalities relative to the reference. That's what makes it useful for GWAS, non-coding variant interpretation, fine-mapping, and regulatory genetics generally.

### Architecture

U-Net-style: convolutional encoder downsamples the 1 Mb sequence to identify short patterns, transformer blocks in the middle communicate information across all positions (with inter-device communication for the long context), convolutional decoder upsamples back to base-pair resolution for the per-track predictions.

Trained on human + mouse genomes against GTEx, ENCODE, FANTOM, and similar bulk-tissue functional genomics datasets.

### Performance vs prior SOTA

- **Beats Enformer + Borzoi on 25/26 variant-effect benchmarks.**
- eQTL prediction (fine-mapped GTEx as ground truth): tissue-weighted mean Spearman ρ improved 0.39 → 0.49. Sign auROC improved 0.75 → 0.80.
- Personal genome prediction (direction of expression effect): odds ratio improved 3.0× over Enformer; in some cases reverses previously-negative correlations to positive.

The 1 Mb context window is the architectural jump that matters most. Enformer was 196 kb. Bridging the gap between "gene neighborhood" (Enformer) and "TAD-scale regulatory landscape" (AlphaGenome) is what enables the eQTL gains, because most regulatory variants in GWAS hits act at >200 kb distances.

### What it can't do (acknowledged + critiqued)

- **Ultra-distal regulation beyond 1 Mb stays out of reach.** Some enhancer-promoter contacts span multiple megabases; AlphaGenome will miss those.
- **Bulk-tissue training bias.** GTEx / ENCODE / FANTOM are bulk-tissue. Rare cell types, immune subsets, gut subsets, neural subtypes — all underrepresented. Predictions for those tissues are worse and require retraining or fine-tuning on better single-cell data when it becomes available.
- **Personal-genome prediction improved but still limited.** The August 2025 independent evaluation ("AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations") showed AlphaGenome beats Enformer on direction-of-effect, but combinatorial effects (the realistic case where a personal genome has thousands of variants interacting) remain hard.
- **Trained on reference + variants, not on synthetic / engineered sequences.** Its prior is human / mouse natural variation. Predicting the effect of inserting a designed cassette is out of distribution.

### Availability

- **Source code open-sourced January 28, 2026** (StatNews / SiliconANGLE coverage).
- Free API for researchers (DeepMind hosts).
- Weights available (per the open-source announcement) — meaning you can fine-tune.

### Why this is platform-relevant for OE

Three angles:

1. **Variant prioritization for the platform thesis.** Open Enzyme's uricase / urate / NLRP3 work threads through human regulatory variation: ABCG2 polymorphisms, SLC2A9 variants, NLRP3 promoter variation, IL-1β regulatory variation. AlphaGenome gives a way to systematically score what *non-coding* variants in these loci actually do — which is most of GWAS but historically the part nobody could predict mechanistically.

2. **Tissue-specific regulatory design.** When OE eventually thinks about inducible or tissue-targeted expression cassettes (e.g., gut-lumen-specific uricase induction, kidney-specific ABCG2 modulators), AlphaGenome can score candidate promoter / enhancer designs against predicted tissue specificity. This is exactly the kind of in-silico filter that should run before any in-vitro design commitment.

3. **A foundation model for the regulatory layer that bridge recombinases will rewrite.** Bridge recombinases give you the *write* primitive at megabase scale. AlphaGenome gives you the *predict-what-it-will-do* primitive at megabase scale. The two are natural complements: design large-scale rearrangements with AlphaGenome scoring, execute with bridge recombinases, measure, retrain. The same loop the rest of the field is starting to build out around CRISPR + variant-effect models, but at a scale CRISPR can't touch.

### Skepticism

- **"Beats SOTA on 25/26 benchmarks" is a model-paper claim.** External evaluation has already started flagging that personal-genome combinatorial prediction is still weak. Don't take the headline number as gospel for the use cases that actually matter to OE.
- **GTEx is normal tissue.** OE's disease biology (gout, EPI, inflammation) often involves states that are tissue-state-shifted (inflamed, fibrotic, dysbiotic). AlphaGenome's predictions in those states are worse than in healthy reference tissue, by construction.
- **1 Mb is a hard ceiling.** Some of the most interesting regulatory architecture spans much longer ranges (e.g., some HOX cluster regulatory elements). For OE-relevant loci (urate handling, immune regulation), 1 Mb is probably enough most of the time. Worth checking per-locus.

### Source list (AlphaGenome)

- `https://www.nature.com/articles/s41586-025-10014-0` — *Nature* paper (2026)
- `https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/` — DeepMind blog
- `https://storage.googleapis.com/deepmind-media/papers/alphagenome.pdf` — preprint PDF
- `https://www.statnews.com/2026/01/28/deepmind-opens-alphagenome-source-code/` — open-source release
- `https://www.biorxiv.org/content/10.1101/2025.08.05.668750v2.full` — independent personal-genome critique (Aug 2025)
- `https://www.sciencedirect.com/science/article/pii/S0168952525002896` — "Swiss-army knife" review (Trends in Genetics)
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC12750497/` — PMC mirror of the review
- `https://www.science.org/content/article/deepmind-s-latest-ai-tool-makes-sense-changes-human-genome` — *Science* news coverage

---

## Where the two connect

The cleanest framing: **AlphaGenome is the predict-what-it-does layer; bridge recombinases are the write-it-at-scale layer.** Neither has a clean predecessor at this scale.

- **Pre-2024 stack:** CRISPR-Cas9 for writing (kilobase scale, with DSB scars), Enformer for predicting (196 kb context, gene-neighborhood scale). Mismatched in scale.
- **2026 stack:** bridge recombinases for writing (megabase scale, scarless), AlphaGenome for predicting (1 Mb context, TAD-scale regulatory landscape). Matched in scale.

This is a quietly significant shift. For the first time, you can plausibly design a megabase-scale rearrangement, predict its regulatory consequences across thousands of tracks before building it, and then build it. That closes the design loop at a scale that wasn't a closed loop a year ago.

For Open Enzyme specifically, the most interesting medium-term play is **microbiome-resident pathway engineering**: predict (with non-human extensions of AlphaGenome-style models, or with bacterial-specific equivalents like the GenSLM / Evo lineage) what a given metabolic pathway insertion will do to a resident gut strain's expression landscape, then install it with bridge recombinases. This is years from being a deployable therapeutic, but the building blocks now exist in a way they didn't.

### Open questions for the wiki sweep / synthesis queue

1. Where does the metagenomic editing demo in the Patel preprint actually sit on the ex-vivo / in-vitro / gnotobiotic / in-vivo spectrum? Pin this down before we update any chassis-selection commitments.
2. Is there an Evo / GenSLM / bacterial-specific equivalent of AlphaGenome that handles prokaryotic regulatory architecture (which is genome-organized very differently from eukaryotic — operons, polycistronic mRNAs, sigma factor switching)? Worth a parallel scan.
3. Does the bridge recombinase IP landscape have a clear open-research path, or is the Arc Institute / IGI patent posture closing off academic-use freedom?
4. AlphaGenome on OE-relevant loci specifically: ABCG2 variants, SLC2A9, NLRP3 promoter, IL-1β regulatory region. Has anyone published a benchmark on these yet? If not, this is a cheap evaluation we could run ourselves with the open weights.
