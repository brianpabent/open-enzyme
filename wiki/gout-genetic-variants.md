---
title: "Gout Genetic Variants — Unified Index Across the Cascade"
date: 2026-05-16
tags:
  - genetics
  - variants
  - gwas
  - polymorphism
  - stratification
  - gout
  - hyperuricemia
  - abcg2
  - urat1
  - glut9
  - nlrp3
  - il1b
  - hla-b5801
  - pharmacogenetics
  - hprt1
  - prps1
  - uox
related:
  - gout-pathophysiology.md
  - abcg2-modulators.md
  - androgen-urate-axis.md
  - uricase.md
  - crispr-uricase.md
  - nlrp3-inflammasome.md
  - uricase-abcg2-genotype-stratification-computational.md
  - intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md
  - chassis-pending-interventions.md
  - fructose-connection.md
sources:
  - "Tin et al. 2019 — Nature Genetics meta-analysis (~1M participants, 351 loci, PMID 31578528)"
  - "Major et al. 2018 — Nat Rev Rheumatol genetics-of-gout review (PMID 30262909)"
  - "Köttgen et al. 2013 — Nat Genet GUGC GWAS meta-analysis (PMID 23263486)"
  - "Matsuo et al. 2009 — Sci Transl Med, common dysfunctional ABCG2 variants (PMID 19952304)"
  - "Saranko et al. 2013 — BBRC, Q141K folding defect (PMID 23800412)"
  - "Enomoto et al. 2002 — Nature, URAT1 cloning + RHUC1 (PMID 12024214)"
  - "Ichida et al. 2004 — Kidney Int, URAT1 W258X in Japanese RHUC1 (PMID 14747400)"
  - "Vitart et al. 2008 — Nat Genet, SLC2A9 GLUT9 + serum urate (PMID 18327257)"
  - "Hollis-Moffatt et al. 2009 — Arthritis Rheum, SLC2A9 polymorphisms (PMID 19644967)"
  - "Hung et al. 2005 — PNAS, HLA-B*5801 + allopurinol SCAR (PMID 15743917)"
  - "Oda et al. 2002 — Mol Biol Evol, primate UOX pseudogenization (PMID 11919282)"
  - "Wu et al. 1989 — PNAS / J Mol Evol, UOX nonsense mutations (PMID 2780565)"
  - "Hoffmann et al. 1967, Lesch & Nyhan 1964 — HPRT1 deficiency; OMIM #300322"
  - "OMIM #311850 — PRPS1 superactivity"
  - "Aksentijevich et al. 2002, 2007 — NLRP3 CAPS variants; OMIM #606416"
  - "ACR 2020 gout management guideline (Clinical Trial — guideline)"
  - "dbSNP (NCBI), ClinVar, UniProt, PharmGKB, GWAS Catalog (database verification per CLAUDE.md Rule 4)"
status: published
---

# Gout Genetic Variants — Unified Index Across the Cascade

## What this page is

A unified, cascade-stratified reference catalogue of the genetic variants that drive — or modulate — gout and hyperuricemia. The wiki already does substantial genotype-stratified intervention modeling in [`uricase-abcg2-genotype-stratification-computational.md`](./uricase-abcg2-genotype-stratification-computational.md), [`intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md), [`abcg2-modulators.md` §6](./abcg2-modulators.md), [`androgen-urate-axis.md`](./androgen-urate-axis.md), and [`gout-pathophysiology.md` §"Genomics and GWAS"](./gout-pathophysiology.md), but none of those pages link back to a single index of *all* relevant variants. This page is that index. Downstream stratification analyses should cross-reference this catalogue rather than re-list variants each time.

**Audience.** PhD-level scientists, clinical translation collaborators, and downstream subagents performing stratified literature scans or computational modeling.

**Privacy gradient.** This is a public-research reference. No personal genotypes. No clinical data tied to individuals. Anyone reading this page is welcome to do so; nothing here would be inappropriate for an external collaborator.

**How to use it.** Each variant entry carries an explicit evidence tier per [`CLAUDE.md` §"Evidence Levels"](../CLAUDE.md). When the source literature disagrees on effect direction, allele frequency, or evidence strength, the disagreement is surfaced in the entry rather than silently resolved — per the multi-source reconciliation discipline encoded in CLAUDE.md §"Pre-commit grep-verify gate." If you are running a stratified subagent task, link to specific table rows by anchor or quote the row inline; do not paraphrase across rows (paraphrasing loses the evidence-tier and cross-source-disagreement information).

**Scope discipline.** This is a *reference index*, not a deep-dive page. The mechanism and intervention discussion for each variant lives on the canonical wiki page named in the rightmost column. Long mechanism narrative does not belong here.

---

## Unified summary table — top variants by load-bearing impact

The 12 variants below are the ones a downstream stratification subagent or computational-experiment author would touch first. Order is approximate — by depth of evidence × OE-platform relevance — not by raw effect size alone.

| # | Variant | Gene | Cascade step | Effect | Why it matters for OE |
|---|---|---|---|---|---|
| 1 | **UOX pseudogenization** (codons 33, 187 + splice site) | UOX | Urate degradation (absent in humans) | Universal human loss-of-function → no urate → allantoin clearance | The chokepoint that every OE uricase track (engineered koji, CRISPR uricase, pegloticase analogs) is designed to restore |
| 2 | **rs2231142 (p.Gln141Lys, Q141K)** | ABCG2 | Renal + intestinal urate secretion | ~50% reduction in transport activity per allele | #1 common genetic risk for gout; rescue lever (HDI, butyrate, fiber, chaperones); large ancestry-frequency gradient |
| 3 | **rs2199936** | ABCG2 | Renal + intestinal urate secretion | Intronic; tag SNP for ABCG2 haplotype | Most significant ABCG2 association in 2025 UK Biobank gout GWAS (p = 1.75 × 10⁻⁹⁷; per [`gout-pathophysiology.md` §"Genomics and GWAS"](./gout-pathophysiology.md)) |
| 4 | **rs734553 / rs58656183** | SLC2A9 (GLUT9) | Basolateral renal urate exit | Largest per-allele effect on serum urate of any known locus | The other dominant urate transporter; less druggable than URAT1/ABCG2 currently |
| 5 | **SLC22A12 W258X (rs121907892)** | SLC22A12 (URAT1) | Renal urate reabsorption | LOSS-of-function → urate doesn't get reabsorbed → **protective** (causes RHUC1) | Validates the URAT1-inhibitor pharmacology class (lesinurad, dotinurad, pozdeutinurad); also the [siRNA against URAT1 modality](./sirna-urat1-modality.md) endpoint |
| 6 | **HPRT1 LoF** (multiple alleles) | HPRT1 (Xq26) | Purine salvage → de novo synthesis dysregulation | LOSS-of-function → Lesch-Nyhan; partial → Kelley-Seegmiller (early-onset gout) | The rare-but-illustrative case of urate **overproduction** from a genetic source; X-linked |
| 7 | **PRPS1 superactivity** (multiple alleles, e.g., D52H, A87T, L129I) | PRPS1 (Xq22.3) | De novo purine biosynthesis | GAIN-of-function → ↑ PRPP → ↑ purine flux → early-onset gout | Direct human-genetic anchor for the [PRPS chokepoint](./prps-purine-biosynthesis-chokepoint.md) thesis |
| 8 | **NLRP3 CAPS variants** (R260W, D303N, T348M, others) | NLRP3 | Inflammasome assembly | GAIN-of-function → constitutive IL-1β release (FCAS / MWS / CINCA-NOMID) | Validates the anti-IL-1β class (canakinumab, anakinra, rilonacept) and the NLRP3-inhibitor class (dapansutrile, oridonin); informs the [NLRP3 exploit map](./nlrp3-exploit-map.md) |
| 9 | **rs10754558 (NLRP3 3′-UTR)** | NLRP3 | Inflammasome assembly | Common polymorphism associated with NLRP3 mRNA stability; modest gout-flare-severity signal | Common-variant counterpart to CAPS; informs flare-stratification subagent design |
| 10 | **rs16944 (IL1B −511 C/T)** | IL1B | Inflammasome output (IL-1β production) | Common promoter variant; T allele associated with ↑ IL-1β production in some studies | Modulates flare amplitude; relevant to anti-IL-1β responder stratification |
| 11 | **HLA-B\*58:01** | HLA-B (MHC class I) | Pharmacogenetics — allopurinol immunogenicity | Carrier → very high allopurinol SCAR / SJS / TEN risk; OR > 500 in Han Chinese (Hung 2005, PMID 15743917) | ACR 2020 strong recommendation: test before allopurinol in East Asian / Han Chinese / Korean / Thai ancestry |
| 12 | **rs780094 (GCKR)** | GCKR | Comorbidity — fructose / metabolic-syndrome × urate | Common variant linking glucokinase regulation to serum urate via fructose handling | Mechanistic bridge between [`fructose-connection.md`](./fructose-connection.md) and the urate axis |

Per-category tables and per-variant notes for the load-bearing entries follow below.

---

## Category 1 — Urate transporters

Renal and intestinal urate handling collectively determine ~95% of inter-individual variance in serum urate at the polygenic level (Tin 2019, Köttgen 2013). The three dominant loci are **ABCG2**, **SLC2A9 (GLUT9)**, and **SLC22A12 (URAT1)**. Several minor transporters round out the renal handling apparatus.

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **rs2231142 (p.Gln141Lys, Q141K)** | ABCG2 (chr4q22) | Renal tubular + intestinal urate secretion | Reduces ABCG2 transport activity by ~50% per allele (mild folding/processing defect → reduced plasma-membrane delivery; Saranko 2013, PMID 23800412) → ↑ serum urate | T allele ~10–15% in European-ancestry cohorts; ~30% in East Asian (Han Chinese, Japanese, Korean); ~3–5% African-ancestry. Substantial ancestry stratification — see [`abcg2-modulators.md` §6](./abcg2-modulators.md) for trial-design implications. | **Clinical Trial** (GWAS replication across multiple ancestries; Wallace 2018 meta-analysis OR ≈ 2.43 in homozygotes) | Rescue lever stack: HDI-mediated trafficking rescue (butyrate, vorinostat — In Vitro); PPARγ-mediated WT-allele induction (butyrate, fermentable fiber — Animal Model + Clinical Trial); pharmacological chaperone class ([chassis-pending §7](./chassis-pending-interventions.md), [comp-032](./computational-experiments.md)). Q141K-stratified butyrate RCT is the canonical computational-experiment design. | [abcg2-modulators.md](./abcg2-modulators.md), [uricase-abcg2-genotype-stratification-computational.md](./uricase-abcg2-genotype-stratification-computational.md) |
| **rs2199936** | ABCG2 (chr4q22) | Renal tubular + intestinal urate secretion | Intronic; tag SNP for the ABCG2 risk haplotype | Common; LD pattern varies by ancestry | **Clinical Trial** (GWAS — 2025 UK Biobank gout study, p = 1.75 × 10⁻⁹⁷ per [`gout-pathophysiology.md`](./gout-pathophysiology.md)) | Index SNP for genotyping panels that don't include rs2231142 directly; both should be on any gout-relevant array | [gout-pathophysiology.md](./gout-pathophysiology.md) §"Genomics and GWAS" |
| **rs2231137 (p.Val12Met, V12M)** | ABCG2 (chr4q22) | Renal tubular + intestinal urate secretion; also **Jr(a−) blood group phenotype** (per UniProt Q9UNQ0) | Modest effect on transport activity; partially LD with Q141K in some populations | T allele ~30–40% in East Asian; lower in European/African | **In Vitro + Clinical Trial** (GWAS-associated; mechanism less characterized than Q141K) | Secondary ABCG2 marker; complicates pure-Q141K stratification because of LD | [abcg2-modulators.md](./abcg2-modulators.md) |
| **rs734553** | SLC2A9 (chr4p16, GLUT9) | Basolateral renal urate exit | Intronic; one of the most strongly urate-associated common SNPs anywhere in the genome (Vitart 2008, PMID 18327257; Köttgen 2013, PMID 23263486) | Common; major allele frequency varies by ancestry | **Clinical Trial** (GWAS — replicated across multiple cohorts >100k each) | GLUT9 is the second-strongest GWAS locus but currently the least druggable major urate transporter; relevant to subagent-driven natural-product target screens (GLPP per [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md)) | [gout-pathophysiology.md](./gout-pathophysiology.md), [fructose-connection.md](./fructose-connection.md) |
| **rs58656183** | SLC2A9 (chr4p16, GLUT9) | Basolateral renal urate exit | Intronic; reported as the most significant SLC2A9 hit in the 2025 UK Biobank gout GWAS (p = 5.52 × 10⁻⁹⁰; per [`gout-pathophysiology.md`](./gout-pathophysiology.md)) | Common | **Clinical Trial** (GWAS) | Same as rs734553 — GLUT9 effect tagging | [gout-pathophysiology.md](./gout-pathophysiology.md) |
| **SLC22A12 W258X (rs121907892, p.Trp258Ter)** | SLC22A12 (chr11q13, URAT1) | Renal urate reabsorption | LOSS-of-function (stop-gained at residue 258 per dbSNP, UniProt Q96S37) → URAT1 cannot reabsorb urate → **renal hypouricemia type 1 (RHUC1)** → PROTECTIVE against gout but at risk for exercise-induced AKI and urolithiasis (Ichida 2004, PMID 14747400) | Pathogenic-rare globally; substantially enriched in East Asian: TOMMO (Japanese) MAF ≈ 2.2%, Korean MAF ≈ 1.3% (dbSNP rs121907892) — accounts for ~50%+ of Japanese RHUC1 cases | **Clinical Trial** (clinical phenotype; OMIM #220150) | Human proof-of-concept for the URAT1-inhibitor pharmacology class (lesinurad, dotinurad, pozdeutinurad) and the [siRNA against URAT1 modality](./sirna-urat1-modality.md); the *opposite* direction — restoring reabsorption — has no clinical use case | [sirna-urat1-modality.md](./sirna-urat1-modality.md), [gout-pathophysiology.md](./gout-pathophysiology.md) |
| **SLC22A12 R90H, R434H, V138M, T217M, E298D** | SLC22A12 (chr11q13, URAT1) | Renal urate reabsorption | LOSS-of-function missense variants causing RHUC1; reduced or strongly reduced urate transport per UniProt Q96S37 (in vitro transport assays) | Rare; some enriched in specific ancestries (e.g., R90H rs121907896 reported in non-East-Asian RHUC1) | **In Vitro + Clinical Trial** (functional + clinical RHUC1 phenotype) | Allelic series demonstrating URAT1 is dosage-sensitive and druggable across the whole transport mechanism, not just one binding pocket | [sirna-urat1-modality.md](./sirna-urat1-modality.md) |
| **GLUT9 missense variants** (e.g., p.Arg380Trp, p.Pro412Arg) | SLC2A9 (chr4p16) | Basolateral renal urate exit | LOSS-of-function → **renal hypouricemia type 2 (RHUC2)**; PROTECTIVE against hyperuricemia (Matsuo 2008, OMIM #612076) | Rare | **In Vitro + Clinical Trial** | Same direction as URAT1 RHUC1 — GLUT9 LoF protects; the analogous URAT1-inhibitor-style approach to GLUT9 has no major program but the human-genetic safety case is established | [gout-pathophysiology.md](./gout-pathophysiology.md) |
| **SLC17A1 / SLC17A3** (NPT1 / NPT4) variants | SLC17A1/A3 (chr6p22) | Apical renal urate secretion | Common variants associated with serum urate at modest effect size; some uricosuric-drug interaction | Common | **Clinical Trial** (GWAS) | Secondary renal-handling layer; less directly druggable in current pipeline | [gout-pathophysiology.md](./gout-pathophysiology.md) |
| **PDZK1 variants** | PDZK1 (chr1q21) | Transporter scaffolding (URAT1, NPT1, OAT4 anchor) | Common variants modulating renal transporter complex assembly; modest serum urate signal | Common | **Clinical Trial** (GWAS; mechanism In Vitro) | Scaffold target — pharmacological tractability poor; included for mechanistic completeness | [gout-pathophysiology.md](./gout-pathophysiology.md) |
| **LRP2 (megalin) variants** | LRP2 (chr2q31) | Receptor-mediated reuptake; broad renal solute handling | Modest serum urate association in some GWAS; mechanism mixed | Common | **Mechanistic Extrapolation** (GWAS associations; direct urate-specific mechanism less well established than transporter genes above) | Background renal context; not a current OE intervention target | — |

**Multi-source disagreement to flag.** The Q141K homozygote odds ratio for gout in published meta-analyses ranges from ~2.0 (some European-ancestry cohorts) to ~3.5 (East Asian cohorts), reflecting both real ancestry-related allele-frequency differences and study-design heterogeneity (case definition, ULT-status filtering). Wallace 2018 meta-analysis cites OR ≈ 2.43 ([`uricase-abcg2-genotype-stratification-computational.md`](./uricase-abcg2-genotype-stratification-computational.md)). The "~50% reduction in transport activity" framing is from in-vitro studies (Saranko 2013); the *in-vivo* serum-urate effect per allele is smaller (~0.2–0.5 mg/dL) because of compensatory renal flux. Both numbers are accurate at their own evidence tier; downstream stratification should specify which one is being invoked.

**Per-variant note — Q141K is the load-bearing one.** The Q141K rescue thesis is one of the most-developed scope areas in the wiki. The [`abcg2-modulators.md` §6](./abcg2-modulators.md) page documents (a) PPARγ-induction of wild-type ABCG2 by butyrate, (b) HDAC-inhibitor trafficking rescue of the Q141K variant specifically (Basseville 2012, PMID 22472121, In Vitro), and (c) the pharmacological-chaperone class as a chassis-pending intervention. The genotype-stratified butyrate trial design at [`abcg2-modulators.md` §6 "Q141K × fiber differential response"](./abcg2-modulators.md) is the canonical pharmacogenomic-RCT scope for the platform.

---

## Category 2 — Urate-production enzymes

The "over-producer" half of gout. Common gout (~90% of patients) is under-excretion; the genetic-overproduction phenotypes are rare but mechanistically illustrative.

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **HPRT1 LoF** (multiple alleles) | HPRT1 (Xq26.2-q26.3) | Purine salvage; LoF re-routes hypoxanthine/guanine into degradation → urate | LOSS-of-function → **Lesch-Nyhan syndrome** (severe, OMIM #300322) or partial-function **Kelley-Seegmiller syndrome** (early-onset gout, hyperuricemia without neurological features) | Rare; X-linked recessive | **Clinical Trial** (clinical phenotype) | Validates that **purine salvage failure → urate flux** is a quantitatively meaningful axis; relevant to allopurinol/febuxostat use in over-producer phenotypes | [gout-pathophysiology.md](./gout-pathophysiology.md) §"Step 1" |
| **PRPS1 superactivity** (e.g., p.Asp52His, p.Ala87Thr, p.Leu129Ile) | PRPS1 (Xq22.3) | De novo purine biosynthesis (rate-limiting) | GAIN-of-function → ↑ PRPP → ↑ purine flux → early-onset gout + sensorineural deafness in some pedigrees (OMIM #311850) | Rare; X-linked | **Clinical Trial** (clinical phenotype; In Vitro mechanism) | Direct human-genetic anchor for the [PRPS chokepoint](./prps-purine-biosynthesis-chokepoint.md) thesis — proves PRPP elevation alone drives clinical hyperuricemia | [prps-purine-biosynthesis-chokepoint.md](./prps-purine-biosynthesis-chokepoint.md) |
| **XDH** (xanthine dehydrogenase / oxidase) variants | XDH (chr2p23) | Hypoxanthine → xanthine → urate (rate-limiting degradation) | LOSS-of-function → xanthinuria (PROTECTIVE against gout but causes xanthine stones, OMIM #278300); common variants modulate XO activity with modest serum urate signal | Common variants ubiquitous; LoF rare | **Clinical Trial** (xanthinuria — clinical); **GWAS — Clinical Trial** for common variants | Human proof-of-concept for the XO-inhibitor class (allopurinol, febuxostat); also informs the natural-product XO-inhibition screens ([`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md), astilbin) | [gout-pathophysiology.md](./gout-pathophysiology.md) |
| **ADA** (adenosine deaminase) variants | ADA (chr20q13) | Adenosine → inosine (purine catabolism upstream of XO) | LoF → severe immunodeficiency (ADA-SCID); modulating ADA changes flux entering the XO → urate pipeline (Mechanistic Extrapolation for gout) | LoF very rare; common variants present | **Clinical Trial** for SCID phenotype; **Mechanistic Extrapolation** for ADA × gout | Surfaced as a chokepoint candidate by comp-014 (Cordycepin / *Cordyceps militaris* / pentostatin biology); see [`gout-pathophysiology.md` §"ADA"](./gout-pathophysiology.md) and [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) | [medicinal-mushroom-compound-mapping-computational.md](./medicinal-mushroom-compound-mapping-computational.md) |
| **G6PC LoF** (glucose-6-phosphatase) | G6PC1 (chr17q21) | Glycogen metabolism; LoF → von Gierke (GSD type Ia, OMIM #232200) → fructose-1,6-bisphosphate accumulation → ↑ AMP deaminase flux → ↑ urate | LOSS-of-function → secondary hyperuricemia + gout in GSD-I patients | Rare | **Clinical Trial** (clinical phenotype) | Mechanistic anchor for the **fructose → ATP depletion → AMP → urate** pathway documented in [`fructose-connection.md`](./fructose-connection.md); validates that fructose-driven urate production is real at clinical magnitude | [fructose-connection.md](./fructose-connection.md) |

---

## Category 3 — UOX (uricase pseudogene) — the universal human variant

This is the special case. The human *UOX* locus is **a pseudogene in every human** — not a polymorphism but a fixed loss-of-function state shared across the species. Functional uricase persists in most mammals (rats, mice, pigs, cows; reconstructed via CRISPR knock-in) but was inactivated independently in great apes and lesser apes ~15–20 million years ago.

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **UOX pseudogenization** — nonsense mutations at codons 33 and 187 + aberrant splice site (Wu 1989, PMID 2780565; Oda 2002, PMID 11919282) | UOX (chr1p22.3 in humans) | Urate → allantoin degradation (would be the terminal step in mammals with functional uricase) | LOSS-of-function — fixed in human population | **Allele frequency = 1.0** (every human is homozygous pseudogene-carrier) | **Clinical Trial** (universal human phenotype: serum urate ~4–7 mg/dL vs ~1 mg/dL in uricase-positive mammals) | The **root chokepoint** every OE uricase track addresses: engineered koji (gut-lumen sink), [CRISPR uricase](./crispr-uricase.md) (germline / somatic restoration via ancestral-sequence reconstruction per Gaucher lab 2025), pegloticase / SEL-212 / PRX-115 (pegylated recombinant uricase as systemic enzyme replacement), rasburicase (acute tumor-lysis use of A. flavus uricase in S. cerevisiae background). Cross-references [`uricase.md`](./uricase.md) and [`crispr-uricase.md`](./crispr-uricase.md). | [uricase.md](./uricase.md), [crispr-uricase.md](./crispr-uricase.md) |

**Important framing.** The "variant" here is not heterogeneous — there is no human population with a functional uricase locus to compare against. The therapeutic target is therefore not stratification but **species-level restoration**. This makes uricase replacement architecturally different from every other entry on this page: every other variant defines a sub-population for stratified treatment; UOX defines the universal human background that the entire OE platform is engineered against. (See [`uricase.md` §"Evolutionary Loss"](./uricase.md) and the Johnson fructose-fat-storage hypothesis for the proposed selective pressure that led to the loss.)

---

## Category 4 — Inflammasome assembly / NLRP3

The inflammasome arm gates how much IL-1β a person produces in response to a given MSU crystal load. NLRP3 itself harbors both the rare CAPS gain-of-function variants (clinically severe autoinflammatory disease) and several common polymorphisms with modest gout-related signals.

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **NLRP3 CAPS variants** — p.Arg260Trp, p.Asp303Asn, p.Thr348Met, p.Ala441Pro, p.Tyr570Cys, others | NLRP3 (chr1q44) | Inflammasome assembly | GAIN-of-function → constitutive ASC speck formation → constitutive IL-1β release → **cryopyrin-associated periodic syndromes** (FCAS, MWS, CINCA/NOMID spectrum, OMIM #606416, autosomal dominant) | Rare; pedigree-specific | **Clinical Trial** (clinical phenotype; In Vitro mechanism) | Human proof-of-concept that **NLRP3 alone is sufficient to drive IL-1β–mediated disease** — validates the entire IL-1 inhibitor class (anakinra, canakinumab, rilonacept) and informs the NLRP3-inhibitor class ([dapansutrile](./gout-clinical-pipeline.md), oridonin per [`nlrp3-inhibitor-screen.md`](./nlrp3-inhibitor-screen.md)) | [nlrp3-inflammasome.md](./nlrp3-inflammasome.md), [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) |
| **rs10754558 (NLRP3 3′-UTR)** | NLRP3 (chr1q44) | Inflammasome assembly | C/G common variant in 3′-UTR; G allele associated with altered NLRP3 mRNA stability in some reports; modest effect-size signal for gout-flare severity in mixed-ancestry cohorts (dbSNP "benign" significance flag) | Common; both alleles substantial-frequency in all major ancestries | **In Vitro + GWAS — Clinical Trial** (modest effect, replication mixed) | Common-variant counterpart to CAPS; relevant for flare-stratification subagent design but **not a clinical-grade pharmacogenetic marker on its own** | [nlrp3-inflammasome.md](./nlrp3-inflammasome.md) |
| **rs35829419 (NLRP3 p.Gln705Lys, Q705K)** | NLRP3 (chr1q44) | Inflammasome assembly | Missense at residue 705 (NP_004886.3:p.Gln705Lys per dbSNP); rare in most populations; reported as a low-penetrance susceptibility allele for several inflammatory conditions; relevance to gout-flare severity uncertain | Rare in most ancestries (T allele MAF <2% in most cohorts) | **In Vitro + GWAS — Clinical Trial** (mixed; dbSNP "benign, conflicting-interpretations-of-pathogenicity") | Lower-priority than rs10754558 for stratified analysis; included for catalogue completeness | [nlrp3-inflammasome.md](./nlrp3-inflammasome.md) |
| **NLRP1 / AIM2 variants** | NLRP1 (chr17p13), AIM2 (chr1q23) | Alternative inflammasome platforms (DNA-sensing AIM2, NLRP1 in epithelial / dendritic cells) | Various; NLRP1 implicated in vitiligo / autoimmune inflammatory diseases; AIM2 implicated in cytosolic dsDNA sensing — relevance to MSU-driven gout is mostly Mechanistic Extrapolation | Common variants present | **Mechanistic Extrapolation** for direct gout role | Included for catalogue completeness; gout-specific role is upstream-of-evidence | [nlrp3-inflammasome.md](./nlrp3-inflammasome.md) |

---

## Category 5 — Inflammasome priming + IL-1β output

Variants here modulate how much pro-IL-1β is available for the inflammasome to cleave (priming arm) and how strongly downstream TLR4 / MyD88 signaling amplifies the response.

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **rs16944 (IL1B −511 C/T)** | IL1B (chr2q14) | IL-1β priming (transcriptional) | Common promoter variant; T allele associated with ↑ IL-1β production in some LPS-stimulation assays (mixed across studies) | Common; both alleles substantial-frequency in all major ancestries | **In Vitro + GWAS — Clinical Trial** (mixed replication) | Modulates flare amplitude; relevant to anti-IL-1β responder-stratification logic | [nlrp3-inflammasome.md](./nlrp3-inflammasome.md) |
| **rs1143634 (IL1B +3954 C/T, p.Phe105Phe synonymous)** | IL1B (chr2q14) | IL-1β output | Synonymous variant in exon 5; T allele reported in some studies as associated with ↑ IL-1β secretion (mechanism uncertain — likely LD with regulatory variant); inconsistent replication | Common | **In Vitro + GWAS — Clinical Trial** (inconsistent; dbSNP "association, benign") | Same role as rs16944; the two SNPs together form the historical "IL1B haplotype" used in pre-GWAS-era inflammation studies | [nlrp3-inflammasome.md](./nlrp3-inflammasome.md) |
| **rs4986790 (TLR4 p.Asp299Gly, D299G)** | TLR4 (chr9q33) | Inflammasome priming (TLR4 → NF-κB) | Missense; G allele reduces LPS-responsive TLR4 signaling in some in-vitro assays — could in principle dampen NF-κB priming of pro-IL-1β. Direction in gout context is **mechanistically ambiguous** (less priming might reduce flares, but TLR4 also has roles in clearance) | T allele MAF ~5–10% in European-ancestry; lower in East Asian; ~10% in some African-ancestry cohorts | **In Vitro + GWAS — Clinical Trial** (mixed for gout specifically) | Inflammasome-priming-axis stratifier; relevant to the [complement-c5a-gout track](./complement-c5a-gout.md) and the [TNFSF14 priming amplifier](./tnfsf14-gout-target.md) | [complement-c5a-gout.md](./complement-c5a-gout.md), [tnfsf14-gout-target.md](./tnfsf14-gout-target.md) |
| **rs4986791 (TLR4 p.Thr399Ile, T399I)** | TLR4 (chr9q33) | Inflammasome priming | Missense often co-inherited with D299G in European-ancestry populations | Common haplotype with D299G | **In Vitro + GWAS — Clinical Trial** | Same priming-axis role | [complement-c5a-gout.md](./complement-c5a-gout.md) |
| **MyD88 variants** | MYD88 (chr3p22) | Inflammasome priming (TLR-axis adapter) | Common variants modest; rare gain-of-function variants (e.g., p.Leu265Pro) drive activated B-cell lymphoma — not gout-relevant | Common common variants; rare oncogenic GoF | **Mechanistic Extrapolation** for direct gout role | Included for catalogue completeness; not a near-term OE intervention target | — |

---

## Category 6 — Pharmacogenetics relevant to gout treatment

The HLA-B*58:01 risk allele for allopurinol SCAR is the single most clinically-actionable pharmacogenetic finding in gout management. ACR 2020 guidelines strongly recommend pre-testing in patients of East Asian ancestry. Several additional variants modulate response to less-frequently-used drugs.

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **HLA-B\*58:01** | HLA-B (chr6p21, MHC class I) | Pharmacogenetics — allopurinol immunogenicity | Carrier → very high allopurinol-induced SCAR (SJS / TEN / DRESS) risk via oxypurinol-restricted T-cell activation; OR > 500 in Han Chinese (Hung 2005, PMID 15743917) | ~6–8% in Han Chinese, ~10–12% in Korean, ~6–8% in Thai; ~1–2% in European-ancestry; ~3–4% in African-ancestry | **Clinical Trial** (PharmGKB Level 1A; ACR 2020 strong recommendation; FDA label warning) | Mandatory pre-test in East Asian / Han Chinese / Korean / Thai ancestry before allopurinol initiation per ACR 2020; alternative ULT (febuxostat, pozdeutinurad, dotinurad) for carriers. The OE engineered-koji / CRISPR uricase tracks **sidestep this pharmacogenetic constraint entirely** because neither requires XO inhibition. | [gout-pathophysiology.md](./gout-pathophysiology.md), [gout-clinical-pipeline.md](./gout-clinical-pipeline.md) |
| **TPMT variants** (e.g., \*2, \*3A, \*3B, \*3C) | TPMT (chr6p22) | Pharmacogenetics — azathioprine metabolism | LoF variants → reduced thiopurine S-methyltransferase activity → ↑ azathioprine toxicity (myelosuppression) | TPMT\*3A ~5% in European-ancestry; \*3C more common in Asian / African | **Clinical Trial** (PharmGKB Level 1A) | Relevant only to mixed-comorbidity patients on azathioprine (e.g., gout + IBD); not a frontline gout pharmacogenetic | — |
| **CYP2C9 variants** (\*2, \*3) | CYP2C9 (chr10q24) | Pharmacogenetics — sulfinpyrazone, some uricosurics, warfarin co-medication | Reduced metabolism of substrate drugs | Common | **Clinical Trial** (PharmGKB) | Modulates dose-response for older uricosurics; less relevant to current pipeline (pozdeutinurad / dotinurad have different metabolism) | — |
| **G6PD deficiency** (multiple alleles) | G6PD (Xq28) | Pharmacogenetics — pegloticase, rasburicase | LOSS-of-function → severe hemolysis on uricase-class drugs (rasburicase contraindicated; pegloticase relative contraindication) | Variable; ~10% in some Mediterranean / African-ancestry populations | **Clinical Trial** (FDA boxed warning on rasburicase) | Hard contraindication for **systemic** recombinant uricase (rasburicase, pegloticase, SEL-212, PRX-115). **The engineered-koji gut-lumen approach is plausibly safer for G6PD-deficient patients because the uricase acts in the intestinal lumen rather than the bloodstream — but this is an explicit open question that has not been empirically tested.** Cross-reference [`crispr-uricase.md`](./crispr-uricase.md) for the systemic-uricase G6PD framing and [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) for the gut-lumen track. | [crispr-uricase.md](./crispr-uricase.md) |

**Multi-source disagreement to flag.** The HLA-B\*58:01 prevalence in East Asian populations is reported in the 6–20% range across published sources, depending on the specific sub-population (Han Chinese ~6–8%, Korean ~10–12%, Thai ~6–8%, with some Taiwanese cohorts reported as high as ~15%). The ACR 2020 guideline lumps these as "East Asian, Han Chinese, Korean, Thai" without finer stratification. Downstream pharmacogenetic-screening protocols should use the specific sub-population frequency where known.

---

## Category 7 — Comorbidity-coupled loci

Variants here are not direct urate-cascade actors but modulate metabolic, lipid, or fructose-handling pathways with downstream urate consequences. These are the loci that link gout to metabolic syndrome.

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **rs780094 (GCKR intron)** | GCKR (chr2p23) | Metabolic-syndrome × fructose × urate | Common variant in glucokinase regulatory protein; T allele associated with ↑ serum urate, ↑ triglycerides, ↓ fasting glucose (mixed lipid / glucose / urate pattern). Mechanism likely via altered hepatic fructose handling → AMP → urate flux | Common; both alleles substantial-frequency in all major ancestries | **Clinical Trial** (GWAS — Tin 2019, Köttgen 2013; multi-trait pleiotropy) | Mechanistic bridge between [`fructose-connection.md`](./fructose-connection.md) and the urate axis; relevant to dietary-fructose-stratification subagent design | [fructose-connection.md](./fructose-connection.md) |
| **APOA1/C3/A4/A5 cluster variants** | APOA1-A5 (chr11q23) | Metabolic syndrome × triglycerides | Modest serum urate signal at GWAS scale; shared genetic architecture with hypertriglyceridemia | Common | **Clinical Trial** (GWAS) | Background-comorbidity loci; not a near-term OE intervention target | — |
| **PNPLA3 p.Ile148Met (rs738409)** | PNPLA3 (chr22q13) | NAFLD risk / lipid droplet biology | G allele strongly associated with NAFLD; modest serum urate signal in some GWAS | G allele ~20–25% in European-ancestry; ~50% in Hispanic-ancestry; ~10% in African-ancestry | **Clinical Trial** (GWAS for NAFLD; modest for urate) | Comorbidity stratifier; relevant when gout intersects with NAFLD treatment | — |
| **MLXIPL (ChREBP) variants** | MLXIPL (chr7q11) | Carbohydrate-responsive transcription | Common variants associated with serum urate at GWAS scale; mechanism via carbohydrate-responsive lipogenic flux | Common | **Clinical Trial** (GWAS) | Background fructose-metabolism context | [fructose-connection.md](./fructose-connection.md) |
| **HNF1A / HNF4A variants** | HNF1A (chr12q24), HNF4A (chr20q13) | Hepatic transcription / MODY | Common variants associated with serum urate at modest effect size; rare LoF cause MODY (maturity-onset diabetes of the young) | Common common variants; rare MODY-causing | **Clinical Trial** (GWAS + MODY phenotype) | Background; relevant to mixed gout + early-diabetes phenotypes | — |

The Tin et al. 2019 *Nature Genetics* meta-analysis (PMID 31578528, ~1M participants, **351 loci**) and the 2025 UK Biobank gout GWAS (N=150,542, 13 gout-diagnosis loci with marked sex-specific architecture per [`gout-pathophysiology.md`](./gout-pathophysiology.md)) are the canonical meta-analytic anchors for the comorbidity-coupled tail. Most of the 351 loci are individually small-effect and not catalogued individually here — they are best treated as a polygenic-risk-score input rather than a per-variant intervention target.

---

## How to test — testing tiers at a glance

| Tier | What it covers | Approximate cost (USD, 2026 pricing) | When useful |
|---|---|---|---|
| **Single-SNP clinical PCR** (Quest, LabCorp, equivalent) | One named SNP (e.g., rs2231142 for Q141K, HLA-B\*58:01 typing) | ~$40–150 per SNP / typing | Pre-allopurinol HLA-B\*58:01 screen (ACR 2020 recommendation); Q141K stratification at clinical-trial enrollment per [`abcg2-modulators.md` §6](./abcg2-modulators.md) |
| **Consumer SNP array** (23andMe, AncestryDNA) | ~600k–1M tagged common SNPs across the genome | ~$100–200 one-time | Personal exploration only; **NOT clinical-grade** — known accuracy issues at lower-frequency variants and rare alleles. The CLIA-certified clinical PCR is the right tool for any trial-grade or clinical-decision context. |
| **Whole exome sequencing (WES)** | Coding sequence across ~20,000 genes | ~$300–1,000 clinical / ~$500 research | Rare-variant catalog (Lesch-Nyhan, PRPS1 superactivity, RHUC1, NLRP3 CAPS); useful when family history suggests Mendelian etiology |
| **Whole genome sequencing (WGS)** | Coding + regulatory + intronic + structural | ~$500–2,000 clinical / ~$200–600 research | Most complete; useful for research panels and rare-disease workups; overkill for routine gout stratification |
| **Targeted gout panel** (where offered) | Curated ABCG2 + SLC2A9 + SLC22A12 + NLRP3 + HLA-B + GCKR | Variable; not yet standard of care | Useful when commercially available; depends on local lab offerings |

**Key practical note.** For most gout-relevant downstream work, the highest-value single test is the **HLA-B\*58:01 pre-allopurinol screen in East Asian / Han Chinese / Korean / Thai ancestry patients** — ACR 2020 strong recommendation, single-test cost, prevents life-threatening SCAR. The Q141K (rs2231142) clinical PCR is the next-highest-value if pharmacogenomic stratification of butyrate / fiber / HDI interventions is being considered (per [`abcg2-modulators.md` §6](./abcg2-modulators.md) RCT design).

---

## Open questions / coverage gaps

These are the gaps the OE corpus has noted but does not yet have evidence depth for. Each is a candidate for a future literature-scan subagent pass or computational-experiment design.

1. **Comprehensive SLC22A12 (URAT1) allelic series across non-East-Asian RHUC1 cases.** Most published URAT1 LoF variants are characterized in Japanese cohorts (Ichida 2004, Enomoto 2002). The full allelic series in European, South Asian, and African-ancestry RHUC1 patients is less well documented; gnomAD provides exome-frequency data that could anchor a more complete catalogue.
2. **Common-variant NLRP3 polymorphisms and gout-flare severity.** rs10754558 and rs35829419 (Q705K) have mixed replication for gout-flare-severity stratification. A dedicated meta-analysis across published gout-flare cohorts would help establish whether these variants justify being a NLRP3-inhibitor responder-stratification marker (relevant to dapansutrile, oridonin development per [`nlrp3-inhibitor-screen.md`](./nlrp3-inhibitor-screen.md)).
3. **Polygenic risk score (PRS) calibration for gout across ancestries.** The 351 loci of Tin 2019 are predominantly European-ancestry-derived. Cross-ancestry PRS portability for serum urate is documented as moderate at best; the East Asian Biobank GWAS (Boocock 2020 and successors) would be the natural anchor for an East-Asian-calibrated PRS. The platform's stratification-mining computational experiments would benefit from PRS rather than single-variant indexing for some questions.
4. **Q141K homozygote PK / PD response to systemic vs gut-lumen uricase.** [comp-019](./uricase-abcg2-genotype-stratification-computational.md) modeled this at the flux level (Q141K homozygotes show the smallest gut-lumen-sink response among typical genotypes but get a synergy bonus from rescue interventions). The empirical question — does this carry to the clinic? — is open and waits on actual genotype-stratified uricase trial data (currently absent from the literature).
5. **GLUT9 druggability.** SLC2A9 has the largest per-allele effect on serum urate of any locus, yet no clinical-grade GLUT9-targeted drug exists. Whether this is a tractability problem (structural / selectivity) or a clinical-priority problem (URAT1 was a richer initial substrate) deserves a dedicated chassis-pending entry.
6. **G6PD deficiency × gut-lumen uricase safety.** Stated open question above in Category 6: whether the engineered-koji gut-lumen approach is safer for G6PD-deficient patients than systemic recombinant uricase is **mechanistically plausible but empirically untested**. Worth queuing as a peer-track open question.
7. **East-Asian-literature deep dive on TCM-era gout cohorts.** Per [`CLAUDE.md` §"Global-multilingual research by default"](../CLAUDE.md), there is likely substantial Chinese-language (CNKI, WanFang) and Japanese-language (J-STAGE, CiNii) gout-cohort data — particularly for Q141K, HLA-B\*58:01, and URAT1 W258X — that has not been ingested into this index. A dedicated multilingual-source subagent pass would close this gap.

---

## Cross-references

- [gout-pathophysiology.md](./gout-pathophysiology.md) — the full cascade in which these variants act (§"Genomics and GWAS" is the partner section)
- [abcg2-modulators.md](./abcg2-modulators.md) — Q141K rescue lever stack; §6 is the canonical Q141K dossier
- [uricase-abcg2-genotype-stratification-computational.md](./uricase-abcg2-genotype-stratification-computational.md) — comp-019 flux modeling, Q141K-stratified gut-lumen uricase predictions
- [intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) — comp-017 intestinal-ABCG2 sex-dimorphism scan
- [androgen-urate-axis.md](./androgen-urate-axis.md) — sex-hormone × ABCG2 axis (interacts with Q141K stratification)
- [uricase.md](./uricase.md) — UOX pseudogene background; ancestral-sequence reconstruction context
- [crispr-uricase.md](./crispr-uricase.md) — UOX restoration via CRISPR; ancestral sequence reconstruction (Georgia State / Gaucher lab 2025)
- [nlrp3-inflammasome.md](./nlrp3-inflammasome.md) — NLRP3 biology
- [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) — NLRP3 chokepoint map
- [prps-purine-biosynthesis-chokepoint.md](./prps-purine-biosynthesis-chokepoint.md) — PRPS1 superactivity as the human-genetic anchor for the PRPS chokepoint
- [fructose-connection.md](./fructose-connection.md) — fructose → AMP → urate pathway (G6PC, GCKR, MLXIPL relevance)
- [sirna-urat1-modality.md](./sirna-urat1-modality.md) — URAT1 LoF (RHUC1) as the human-genetic anchor for URAT1-targeted siRNA
- [chassis-pending-interventions.md](./chassis-pending-interventions.md) — pharmacological-chaperone class for Q141K (§7)
- [gout-clinical-pipeline.md](./gout-clinical-pipeline.md) — current drug pipeline; informs which variants are clinically actionable now

---

*Index page; no inline mechanism deep-dives. Variant-specific mechanisms, rescue strategies, and intervention design belong on the canonical wiki pages linked in the "Canonical wiki page" column of each table.*
