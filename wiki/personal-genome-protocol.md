---
title: Personal Genome Protocol — Kitchen-Table Sequencing + Gout Pharmacogenomics
date: 2026-05-07
tags: [self-experiments, sequencing, pharmacogenomics, ABCG2, HLA-B5801, infrastructure, nanopore]
related:
  - self-experiment-protocol.md
  - abcg2-modulators.md
  - gout-pathophysiology.md
  - ai-bio-tools-playbook.md
sources:
  - Hung S-I et al. 2005 (HLA-B*5801 and allopurinol SCAR; PNAS)
  - Matsuo H et al. 2009 (ABCG2 Q141K and gout; Sci Transl Med)
  - Cleophas MCP et al. 2017 (ABCG2 Q141K and allopurinol response)
  - GINA (US, 2008) — health insurance + employment only
  - Oxford Nanopore Technologies product specs (R10.4.1, Dorado)
---

# Personal Genome Protocol

Dual-purpose page: **(1)** Brian's personal genome sequencing as a self-experiment, and **(2)** the same hardware/wetware capability becomes Open Enzyme strain-QC infrastructure (CRISPR integration verification, off-target indel checks, plasmid validation). One investment, two outputs. The capability build is load-bearing for the platform either way; the personal genome is the ride-along.

## Why this isn't 23andMe

The privacy threat model is **active**, not paranoid:

- 23andMe's 2023 credential-stuffing breach (~7M users) plus their 2024-25 financial wobble means "who buys the database in a sale?" is an open question. Pure data-governance risk, no scientific defense.
- 23andMe's GSK pharma partnership monetizes user data into ML drug-discovery pipelines without per-user compensation — the "you are the product" critique made literal.
- **GINA gap (US):** the 2008 Genetic Information Nondiscrimination Act protects against genetic discrimination in **health insurance and employment only**. **Life insurance, disability insurance, and long-term-care insurance have NO statutory protection.** Real underwriting risk if your genome ends up in a queryable database.
- A SNP chip (23andMe-class) is enough to genetically fingerprint you and your relatives in any future database. WGS contains everything but isn't more identifying than a chip — both are unique.

## Privacy gradient (worst → best)

| Tier | Option | Privacy posture | Cost | Data | Tradeoff |
|------|--------|-----------------|------|------|----------|
| 1 | 23andMe / Ancestry / MyHeritage | Worst — monetized; breach + sale risk | $99–199 | SNP chip | You are the product |
| 2 | Sequencing.com / Dante / generic WGS services | Better but third-party-held; read TOS not marketing | $400–600 | WGS | "We don't sell your data" usually means "yet" |
| 3 | Nebula Genomics | Privacy-architected (blockchain-gated access; you can host your own decrypted data) | $300–600 | WGS | Still a third party physically holds the sample |
| 4 | **Clinical routing — physician-ordered CLIA WGS** | Best send-out option (HIPAA chain of custody; lab destroys sample) | $1,000–3,000 | WGS | Needs willing physician |
| 5 | **MinION at home, basecall locally** | Self-sovereign — data never leaves your laptop | **~$3,000+ setup** [VERIFIED 2026-05-07 — Nanopore Store entry-tier MinION bundles start over $3K; the historical "$1K MinION" marketing era is over. Per-bundle exact cost should be verified against [https://store.nanoporetech.com/minion.html](https://store.nanoporetech.com/minion.html) before purchase] + ~$200–300/run reagents | Long-read WGS | Higher per-base raw error; you do all the wet work |

**Recommendation for the privacy-prioritizing self-experimenter: Tier 5** — but note that current Nanopore Store pricing has narrowed the cost gap with Tier 4 (physician-routed CLIA WGS $1,000–3,000) considerably. The Tier 5 case is now anchored less on "cheapest" and more on "self-sovereign data + dual-purpose hardware (Project Crossover below) + amortized cost across many runs." If short-read accuracy is later needed for a clinical-grade SNP confirmation (e.g., HLA-B*58:01 typing), do it Tier 4 (physician-routed) — never touch Tier 1.

## Kitchen-table setup

### Hardware (one-time, ~$3,000+ for MinION starter; laptop + microcentrifuge separate)
- **Oxford Nanopore MinION Mk1B starter pack (~$3,000+)** — [VERIFIED 2026-05-07 against [Nanopore Store](https://store.nanoporetech.com/minion.html); historical ~$1,000 starter pricing era is over. The corpus inherited the "$1K MinION" claim from earlier marketing material; current store-listed entry tier is meaningfully higher. Verify current bundle structure (device + flow cells + sequencing kits + accessories) before purchase. The Mk1C variant with embedded compute runs higher still; Mk1B requires GPU laptop.]
- Laptop with NVIDIA GPU (8GB+ VRAM) for Dorado basecaller — local, no cloud round-trip. ~$1,500–3,000 if purchasing new; many CTO-tier self-experimenters already own one.
- Microcentrifuge (used eBay, $100–200) — needed for library prep

### Per-run consumables (~$200–300/genome)
- Rapid sequencing kit (SQK-RAD114) or ligation kit (SQK-LSK114) for ~30× WGS depth
- DNA extraction kit (saliva collection + magnetic-bead extraction; ~$30/sample)
- Flow cell (R10.4.1, ~$500–900; reusable for ~24h runtime if washed between samples per ONT protocol)

### Software stack (open source, all local)
- **Dorado** (Oxford Nanopore, GPU-accelerated basecaller)
- **Flye** or **Shasta** (long-read genome assembly)
- **Clair3** or **PEPPER-Margin-DeepVariant** (variant calling from long reads)
- **bcftools** / **vcftools** (variant filtering)
- **IGV** (visualization)

### Total time
~2 days end-to-end: 1 day wet lab + library prep, 1 day sequencing + basecall + assembly + variant calling. Iteration loop is fast enough for routine strain QC once the workflow is dialed in.

## Gout-specific pharmacogenomic query list

Once you have your VCF, the highest-signal queries given Open Enzyme's gout focus:

### Tier 1 — Critical drug-safety variants

- **HLA-B*58:01** — Allopurinol-induced Stevens-Johnson syndrome / TEN risk. (Clinical Trial; Hung et al. 2005 PNAS; ACR guidelines recommend pre-prescribing screening in Asian-ancestry populations.) **Carrier status changes prescribing.** If positive: never take allopurinol; febuxostat is the alternative. Confirm with CLIA-grade short-read assay before clinical action — long-read HLA typing is improving (R10.4.1 chemistry) but historically short-read territory due to repeat density.

### Tier 2 — Gout risk + drug response variants

- **ABCG2 Q141K (rs2231142)** — Major gout risk allele; reduced renal/gut urate secretion. (Clinical Trial; Matsuo et al. 2009; Cleophas et al. 2017.) Heterozygotes ~1.5–2× gout risk; homozygotes ~3×. Predicts **reduced allopurinol response**. See [`abcg2-modulators.md`](./abcg2-modulators.md) for the full mechanism + butyrate/HDAC-inhibitor rescue strategy — Q141K homozygotes are exactly the population the Open Enzyme butyrate-coexpression thesis is designed for.
- **SLC2A9 (GLUT9) variants** — Renal urate reabsorption; multiple GWAS hits. Smaller per-variant effect, cumulative across the locus.
- **SLC22A12 (URAT1) variants** — Both loss-of-function (protective; common in some Asian populations) and gain-of-function (gout risk).
- **PDZK1 variants** — Scaffolding for renal urate transporters; modulates URAT1 / GLUT9 surface expression.

### Tier 3 — Inflammasome-related variants (NLRP3 chokepoint relevance)

- **MEFV variants** — Familial Mediterranean Fever spectrum; pyrin-driven IL-1β. (Mechanistic Extrapolation from FMF biology to gout cross-reactivity.) Worth checking if there's a history of unexplained inflammatory episodes.
- **NLRP3 gain-of-function variants** — Cryopyrin-associated periodic syndromes (CAPS); rare but high-effect.

### Tier 4 — Conditionally relevant (EPI co-target only)

- **CFTR, PRSS1, SPINK1** — only if EPI is in personal/family history. Otherwise skip.
- **HNF1A, HNF1B** — pancreatic function modifiers; relevant only if EPI co-target applies.

## Interpretation discipline

- **Evidence-level tagging.** Every finding gets the standard wiki tagging (Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation). A pharmacogenomic finding from a single GWAS in one population is not the same as an FDA-actionable variant.
- **Confounders matter.** ABCG2 Q141K interacts with diet, BMI, alcohol, NSAIDs. A "high-risk" variant in someone with an elite-athlete phenotype is not the same as in someone with metabolic syndrome.
- **Don't act on findings without confirmation.** Long-read consensus accuracy at 30× is ~99%, but for a critical variant (e.g., HLA-B*58:01 typing for an allopurinol decision), confirm with a CLIA-grade short-read assay before changing prescribing.
- **GINA gap reminder.** Life / disability / LTC underwriting can use genetic data. Once findings are shared (with doctors, into EHRs), the disclosure is hard to retract.

## Project crossover — strain QC infrastructure

Same MinION + library prep + variant-calling pipeline that sequences Brian's genome does:

- **CRISPR integration verification** — confirm the engineered cassette is at the intended locus + orientation in *A. oryzae* / *S. cerevisiae* / *F. prausnitzii*.
- **Off-target indel screening** — check for unintended Cas9 cuts elsewhere in the strain genome.
- **Plasmid validation** — verify the construct sequence matches the design before transformation. Catches synthesis errors before wet-lab spend.
- **Released-strain genome QC** — every released engineered strain in the Open Enzyme library ships with its own assembled genome as proof-of-construct. Open-source strain library + open-source genome data is the OE thesis literalized: forkable strains include their full reference genome.

This is not optional for Phase 1+ wet work. The hardware investment is both personal genomics AND platform infrastructure — same dollar, two outputs.

## Open questions / follow-ups

- **Can MinION-only confirm HLA-B*58:01?** HLA typing is historically short-read territory due to repeat density. Long-read methods are improving (PacBio HiFi works well; nanopore R10.4.1 chemistry is closing the gap). Worth verifying current SOTA before relying on nanopore alone for a prescribing-relevant call.
- **Strain-genome publication policy.** Should every released OE strain have its assembled genome published as part of the strain release? Cost ~$300/genome at nanopore tier. Aligns with the open-source-strain-library thesis. Decision pending.
- **Self-experiment integration.** Pharmacogenomic findings should feed [`self-experiment-protocol.md`](./self-experiment-protocol.md) as priors — e.g., "if ABCG2 Q141K homozygote, allopurinol response will be blunted, plan biomarker monitoring accordingly." Likely yes; integration not yet drafted.

## See also

- [`self-experiment-protocol.md`](./self-experiment-protocol.md) — biomarker monitoring framework
- [`abcg2-modulators.md`](./abcg2-modulators.md) — pharmacological levers on ABCG2; PPARγ induction via butyrate; HDAC-inhibitor rescue of Q141K
- [`gout-pathophysiology.md`](./gout-pathophysiology.md) — full gout cascade including 351 GWAS loci
- [`ai-bio-tools-playbook.md`](./ai-bio-tools-playbook.md) — computational stack including variant interpretation
- [`practitioner-toolkit.md`](./practitioner-toolkit.md) — section umbrella (self-experiments + DIY-bio + rigor disciplines)
