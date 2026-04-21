# reference/ — Canonical read-only material

This directory holds canonical source material that the sweep daemon **reads but never modifies**.

## What goes here

- **Published papers** — PDFs, markdown transcripts, or extracted text of peer-reviewed research.
- **External reports** — FDA filings, trial registries, third-party market data.
- **Vendor data** — manufacturer specifications, strain catalogs, regulatory documents.
- Anything authored outside this project that should be cited as-is.

## reference/generated/

Output from scripts and analysis programs goes here. These are machine-produced artifacts (sequence alignments, protein structures, docking scores, BLAST hits, etc.) that should be treated as reference material — consumed by the docs, not rewritten by them.

If a program's output needs to be updated, re-run the program. Do not edit the output in place.

## Rules (enforced by `scripts/sweep-prompt.md`)

- The daemon never writes to any file under `reference/`.
- If the sweep is triggered by a file under `reference/` (which shouldn't happen — `wiki-watch.sh` doesn't watch this directory), the daemon aborts with a logged note.
- Docs in `docs/` may cite files here with standard provenance: `(source: reference/<path>)`.

## reference/papers/

Structured reference files (one `.md` per paper) for primary research cited across the wiki. Each file includes full bibliographic metadata, the verbatim abstract, DOI/PMID/PMC links, and a brief "Relevance to Open Enzyme" note. These files are read-only — the daemon does not modify them.

### Uricase / Gut-Lumen Enzymatic Therapy

| File | Citation | What it establishes |
|------|----------|---------------------|
| [alln-346-uricase-2020.md](papers/alln-346-uricase-2020.md) | Pierzynowska et al., Front. Med. 2020 (PMID 33330529) | ALLN-346 oral uricase reduces hyperuricemia 44% in URKO mice; gut-lumen delivery proof-of-concept |
| [pulse-probiotic-2025.md](papers/pulse-probiotic-2025.md) | Gao et al., Cell Rep Med 2025 (PMID 41038159) | PULSE engineered E. coli Nissle with HucR urate biosensor driving urate oxidase; efficacy in acute and chronic rodent models |
| [sboulardii-uric-acid-2025.md](papers/sboulardii-uric-acid-2025.md) | Wang et al., ACS Synth Biol 2025 (PMID 40340401) | Engineered S. boulardii; 365.32 μmol/h/OD uric acid-degrading activity; Vibrio vulnificus uricase + chimeric UapA transporter |
| [gaucher-crispr-uricase-2025.md](papers/gaucher-crispr-uricase-2025.md) | Balico & Gaucher, Sci Rep 2025 (PMID 40681749) | CRISPR insertion of ancestral uricase in human hepatocytes; confirms intracellular urate reduction and triglyceride blunting |

### Uricase Evolutionary Biology

| File | Citation | What it establishes |
|------|----------|---------------------|
| [oda-uricase-evolution-2002.md](papers/oda-uricase-evolution-2002.md) | Oda et al., Mol Biol Evol 2002 (PMID 11961098) | CGA→TGA nonsense mutation in exon 2 inactivated uricase in hominoids; two-step deterioration model |
| [kratzer-ancient-uricases-2014.md](papers/kratzer-ancient-uricases-2014.md) | Kratzer et al., PNAS 2014 (PMID 24550457) | Ancestral uricase resurrection; activity declined along primate lineage; 3D structure; pharmacokinetics in rodents |

### NLRP3 Inflammasome Inhibitors

| File | Citation | What it establishes |
|------|----------|---------------------|
| [oridonin-nlrp3-2018.md](papers/oridonin-nlrp3-2018.md) | He et al., Nat Commun 2018 (PMID 29959312) | Oridonin covalently modifies NLRP3 Cys279 in NACHT domain; blocks NEK7 interaction; efficacy in gouty arthritis model |
| [disulfiram-gsdmd-2020.md](papers/disulfiram-gsdmd-2020.md) | Hu et al., Nat Immunol 2020 (PMID 32367036) | Disulfiram (FDA-approved) blocks GSDMD pore formation at Cys191/Cys192 at nanomolar concentrations |
| [bhb-nlrp3-youm-2015.md](papers/bhb-nlrp3-youm-2015.md) | Youm et al., Nat Med 2015 (PMID 25686106) | BHB blocks NLRP3 by preventing K+ efflux and ASC oligomerization; ketogenic diet reduces urate crystal-induced peritonitis in vivo |
| [tranilast-nlrp3-embo-2018.md](papers/tranilast-nlrp3-embo-2018.md) | Huang et al., EMBO Mol Med 2018 (PMID 29531021) | Tranilast (approved anti-allergic drug) directly binds NLRP3 NACHT domain; blocks oligomerization; efficacy in gout, CAPS, T2D models |

### Enzyme Engineering / Expression Systems

| File | Citation | What it establishes |
|------|----------|---------------------|
| [disulfide-aflavus-uricase-2025.md](papers/disulfide-aflavus-uricase-2025.md) | Rahbar et al., Sci Rep 2025 (PMID 40419569) | Computational disulfide bond engineering in A. flavus uricase; Ala6-Cys290 and Ser119-Cys220 variants increase stability without occluding substrate tunnel |
| [pmc12010093-codon-optimization-2025.md](papers/pmc12010093-codon-optimization-2025.md) | Demissie et al., J Microbiol Biotechnol 2025 (PMC12010093) | Benchmarks codon optimization tools (JCat, OPTIMIZER, GeneOptimizer) in S. cerevisiae; advocates multi-criteria CAI + GC + ΔG + CPB framework |
| [pmc4480987-yeast-promoters-2015.md](papers/pmc4480987-yeast-promoters-2015.md) | Peng et al., Microb Cell Fact 2015 (PMC4480987) | Constitutive glycolytic promoters drop during diauxic shift; HXT7/SSA1/ADH2 increase post-diauxically; promoter selection guide for yeast fermentation |
| [pmc3628533-alpha-mating-secretion-2013.md](papers/pmc3628533-alpha-mating-secretion-2013.md) | Lin-Cereghino et al., Gene 2013 (PMC3628533) | Deletion of α-MF prepro aa 57–70 (helix 3) increases secretion ≥50% in P. pastoris; optimized secretion signal for heterologous enzyme secretion in yeast |

---

## What does NOT go here

- Living research notes → `wiki/`
- Daemon synthesis output → `ai-analysis/`

If you're not sure whether something is "canonical" or "living," the test is: *can I imagine the daemon rewriting this next week when new findings land?* If yes → `wiki/`. If no → `reference/`.
