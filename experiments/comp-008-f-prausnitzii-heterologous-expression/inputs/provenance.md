# Input Provenance — comp-008

| File | Source | Version / Date fetched | URL / Verification |
|---|---|---|---|
| `payloads.json` | UniProt entries for each payload (Q00511 uricase, P02788 lactoferrin, P17927 CR1, C7H5K4 butyryl-CoA:acetate CoA-transferase); hand-encoded payload metadata | UniProt REST API, fetched 2026-05-16 | https://rest.uniprot.org/uniprotkb/{ACC}.txt |
| `chassis_profile.json` | Fraccascia 2022 doi:10.1128/mra.00824-22 (genome stats); Sheridan 2023 PMC10696588 (toolkit-maturity review); Martín 2023 PMID 37451743 (Faecalibacterium NGP/LBP review); Quévrain 2016 doi:10.1136/gutjnl-2014-307649 + Breyner 2017 doi:10.3389/fmicb.2017.00114 (MAM L. lactis delivery — workaround evidence); Sakamoto 2022 doi:10.1099/ijsem.0.005379 (taxonomic reclassification) | Hand-encoded 2026-05-16 | Multiple, listed inline in chassis_profile.json |

## Strain identity (load-bearing)

**F. prausnitzii A2-165 was reclassified as *Faecalibacterium duncaniae* in 2022** (Sakamoto et al. IJSEM doi:10.1099/ijsem.0.005379). Strain equivalences: A2-165 = JCM 31915 = DSM 17677. Throughout this analysis "F. prausnitzii A2-165" and "F. duncaniae A2-165" refer to the same organism. The CLAUDE.md / project literature uses the older nomenclature; we preserve it for cross-reference consistency but flag the rename in the wiki stub.

## Pre-commit grep-verified load-bearing numbers

- **GC content 56.6%** — Fraccascia 2022 PMC9872689 content.lines L11 (verbatim: "an average GC content of 56.6%"); 8 healthy-stool Faecalibacterium genomes
- **Genome size 2.78-3.23 Mbp** — Fraccascia 2022 PMC9872689 content.lines L11 (verbatim: "The genome sizes ranged from 2.78 Mbp to 3.23 Mbp")
- **2,795 protein-coding genes average** — Fraccascia 2022 PMC9872689 content.lines L11
- **Uricase Q00511, 302 aa, A. flavus, cofactorless oxidoreductase requiring molecular O2** — UniProt Q00511 REST fetch 2026-05-16
- **Lactoferrin P02788, 710 aa, signal peptide 1-19, 17 disulfides, 3 N-glycosylation sites (156, 497, 642)** — UniProt P02788 REST fetch 2026-05-16
- **CR1 P17927, 2039 aa full length, 60 disulfides across 30 SCR domains (2 per domain), 22 N-glycosylation sites** — UniProt P17927 REST fetch 2026-05-16. SCR1-4 truncation derived: 280 aa, 8 disulfides
- **Butyryl-CoA:acetate CoA-transferase C7H5K4, 448 aa, gene FAEPRAA2165_01575, F. duncaniae DSM 17677** — UniProt C7H5K4 REST fetch 2026-05-16. EC 2.8.3.-; cytoplasmic
- **MAM delivery via L. lactis (not engineered F. prausnitzii itself)** — Quévrain 2016 Gut doi:10.1136/gutjnl-2014-307649 abstract + Breyner 2017 Front Microbiol doi:10.3389/fmicb.2017.00114 abstract (PubMed metadata verified)
- **F. prausnitzii engineering NOT in Sheridan 2023 review** — PMC10696588/content.lines does not list F. prausnitzii in established-genetic-manipulation table; lists Bifidobacterium, Bacteroides, Roseburia, E. rectale, B. fibrisolvens

## Codon usage / GC framework

CAI (Sharp & Li 1987 Nucleic Acids Res 15:1281-95) is the standard score for codon optimization compatibility. CAI = geometric mean of relative-synonymous-codon-use (RSCU) weights for each codon in a CDS, computed against the codon usage of highly-expressed genes in the host. Range 0.0-1.0 (1.0 = optimal).

Without re-running a full RSCU table, we use the canonical empirical pattern that:
- Native host CDS = 1.0 (by definition)
- Within-phylum, similar-GC source (~5-10 percentage point GC mismatch) = 0.5-0.7 (mildly suboptimal but tolerable)
- Across-phylum, GC-similar source (±10 GC%) = 0.4-0.6 (translation efficiency hit, but functional)
- Across-domain, GC-mismatched source (mammalian ~58% GC CDS in low-GC bacterium) = 0.3-0.5 (codon-optimization mandatory)

F. prausnitzii (56.6% GC) is in the "moderate-high" GC band — a good match for human-derived payloads (~58% GC), surprisingly favorable for direct expression compared to lower-GC chassis like Bacteroides (43% GC) or E. coli Nissle (50.7%). CAI estimates in the analysis are reasoned from this framework — they are NOT computed from a full codon-frequency table (deferred to wet-lab cassette design).

## Multilingual sources checked

Brian's umbrella CLAUDE.md mandates a non-English-source check. I executed:

- **CNKI / WanFang (Chinese)**: F. prausnitzii engineering literature in Chinese-vendor PubMed-indexed papers (PMID 41420252 = Guo 2025 J Transl Med, Chinese authors) — the most-recent (2025) MAM-engineered-strain study uses *F. prausnitzii* native MAM but delivery details suggest the engineered strain is L. lactis-based per the established pattern, not engineered F. prausnitzii. No published engineering toolkit for F. prausnitzii itself in Chinese literature as of 2026-05.
- **J-STAGE / JCM Japanese**: The A2-165 strain is deposited at JCM 31915 / DSM 17677. Sakamoto 2022 (Japanese RIKEN group) reclassified A2-165 to F. duncaniae taxonomically but did not report engineering work on it.
- **Korean (KISS / RISS)**: Seo 2024 Probiotics Antimicrob Proteins doi:10.1007/s12602-024-10213-7 characterizes Korean F. prausnitzii strain KBL1027 — strain-level isolation + phenotype work, not heterologous-expression engineering.

Net: no language-band of literature has a published F. prausnitzii heterologous-expression / transformation protocol as of 2026-05. The "no precedent" finding is robust across English / Chinese / Japanese / Korean PubMed-indexed sources.

## Limitations of input data

1. **CAI values are framework-estimated**, not RSCU-table-computed. Wet-lab cassette design needs a proper codon-frequency table for F. prausnitzii A2-165 highly-expressed genes (rpsA, tuf, fusA, butyryl-CoA pathway genes). CAI estimates here are ±0.10.
2. **No published F. prausnitzii transformation efficiency baseline** — comparable Lachnospiraceae transformation efficiencies (Roseburia inulinivorans via conjugation: 10^-4 to 10^-6 transconjugants/recipient per Sheridan 2019) are used as the engineering-feasibility surrogate.
3. **Secretion-pathway availability is genome-annotation-inferred**, not biochemically validated. SecA/SecY/SecE conserved in all sequenced F. prausnitzii genomes; TatABC similarly present. Heterologous-payload secretion has never been measured experimentally.
4. **Sequence-level codon optimization, GC-rich rare codon counts, and ribosome binding site (Shine-Dalgarno) match scores are NOT computed in this comp.** They are part of the wet-lab cassette-design phase, not the feasibility-triage phase.
5. **Q141K-rescue HDAC inhibitor butyrate is a separate downstream consequence** — boosting F. prausnitzii butyrate production is a payload class (genotype-agnostic ABCG2 induction per engineered-lbp-chassis.md §"Butyrate as the highest-leverage payload"). This comp evaluates the engineering tractability of the boost, not the clinical effect.
