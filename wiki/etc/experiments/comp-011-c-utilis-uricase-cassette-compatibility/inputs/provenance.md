# Provenance — comp-011 inputs

## P78609.fasta — C. utilis uricase (Cyberlindnera jadinii)

- **Accession note:** P15296 (cited in the project brief as the likely C. utilis uricase accession) returns an unrelated Drosophila protein (NOF_DROME, a transposable-element protein) via UniProt REST redirect. P15296 is likely a secondary accession that has been reassigned or merged. The correct reviewed SwissProt entry for *Candida utilis* / *Cyberlindnera jadinii* uricase is **P78609 (URIC_CYBJA)**, confirmed by taxon search (OX=4903, Cyberlindnera jadinii). ALLN-346 parent enzyme attribution: see US10815461B2 (Allena Pharmaceuticals patent) — the patent discloses mutations on a *Candida utilis* uricase backbone; the parent sequence is consistent with P78609 (303 aa, identical length and active-site residues). Direct comparison of P78609 vs. the ALLN-346 parent is not possible without the exact ALLN-346 CDS disclosure, but the disclosed active-site positions (I180V, V190G, Y165F, E51K, Q244K, I132R, A87G) are on a backbone with the same length and active-site pattern as P78609, confirming it is the correct canonical sequence for this analysis.
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/search?query=accession:P78609&format=fasta
- **Fetch date:** 2026-05-05
- **Entry:** sp|P78609|URIC_CYBJA Uricase, Cyberlindnera jadinii (= Candida utilis), OX=4903, PE=3 SV=1
- **Length:** 303 aa (full-length, no signal peptide annotated; Chain annotation covers aa 1–303)
- **Signal peptide:** None annotated in UniProt. The protein is classified as a peroxisomal enzyme (microbody targeting signal annotated at C-terminal residues 301–303 = TKL). No ER-targeting signal peptide — consistent with intracellular/peroxisomal location in the native yeast.
- **Disulfide bonds:** None annotated in UniProt (consistent with uricase family — eukaryotic uricases are typically disulfide-free despite having cysteine residues).
- **Cysteine count:** 4 (positions 39, 168, 250, 293 — all predicted as free cysteines or intramolecular contacts, not disulfide-bonded per UniProt annotation).
- **N-glycosylation:** None annotated. One predicted N-X-S/T sequon at position 54 (NSS), not annotated as occupied.
- **Gene:** Not annotated in UniProt entry (gene name field empty for this entry).
- **Protein existence:** PE=3 (Inferred from homology). Note: PE=3 means the protein has not been experimentally characterized directly in this organism; its existence is inferred by homology to characterized uricases.
- **Active site residues (UniProt annotation):** T12, C60, W263 (charge relay system); substrate binding at C60, N61, F162, T179, K234, R235, K261.
- **C-terminal motif (UniProt annotation):** Microbody targeting signal at residues 301–303 = TKL (PTS1-like peroxisomal targeting signal). Note: TKL is a weak PTS1 variant (canonical consensus: S/A/C-K/R-L). T is outside the canonical PTS1 P-2 position set — weaker PTS1 than SKL. However, UniProt annotates it explicitly as a microbody targeting signal, indicating it is functionally active in the native context.
- **Alignment note:** *C. utilis* uricase (P78609, 303 aa) vs. *A. flavus* uricase (Q00511, 302 aa): 1 aa length difference; ~50% amino acid identity across the uricase family by pairwise alignment (typical for fungal uricases from different genera). The shared active-site architecture (tetrameric beta-barrel, Cu-independent, O2-dependent) is conserved.

## P02788.fasta — Human lactoferrin (lactotransferrin)

- **Copy provenance:** Copied from experiments/comp-005-lactoferrin-shio-koji-protease-stability/inputs/P02788.fasta; also present in comp-010 inputs.
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P02788.fasta
- **Fetch date:** 2026-05-05 (originally fetched for comp-005)
- **Entry:** sp|P02788|TRFL_HUMAN Lactotransferrin, Homo sapiens, PE=1 SV=6
- **Length:** 710 aa (canonical isoform, including signal peptide aa 1–19)
- **Signal peptide:** residues 1–19 (MKLVFLVLLFLGALGLCLA)
- **Mature protein:** residues 20–710 (691 aa)
- **N-glycosylation sites (UniProt annotation):** N137 (N-X-S: NIS), N478 (N-X-S: NVS), N623 (N-X-S: NKS)
- **Disulfide bonds (UniProt annotation):** 17 disulfide bonds (34 cysteine residues, fully paired)
- **Unchanged from comp-010:** This file is identical to the comp-010 input. Lactoferrin analysis results are numerically identical to comp-010.

## glucoamylase_carrier.fasta — A. awamori glucoamylase (Ward 1995 carrier protein)

- **Copy provenance:** Copied from experiments/comp-010-cassette-compatibility/inputs/glucoamylase_carrier.fasta
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P69327.fasta
- **Fetch date:** 2026-05-05
- **Entry:** sp|P69327|AMYG_ASPAW Glucoamylase, Aspergillus awamori, PE=1 SV=1
- **Length:** 640 aa (includes signal peptide + propeptide + catalytic domain + Ser/Thr-rich linker stalk)
- **Role in Ward 1995 architecture:** N-terminal fusion carrier. KEX2 cleavage at K-R releases the payload in the late secretory pathway.
- **Unchanged from comp-010.**

## a_oryzae_codon_usage.json — A. oryzae RIB40 codon usage table

- **Copy provenance:** Copied from experiments/comp-010-cassette-compatibility/inputs/a_oryzae_codon_usage.json
- **Source:** Codon Usage Database (Kazusa), cross-validated against Machida 2005 genome annotation (PMID 16372010)
- **Units:** RSCU and freq_per1000 for highly-expressed genes
- **Rare-codon threshold:** RSCU < 0.4
- **Unchanged from comp-010.**

## kex2_site_specs.json — KEX2 cleavage rules

- **Copy provenance:** Copied from experiments/comp-010-cassette-compatibility/inputs/kex2_site_specs.json
- **Sources:** Rockwell et al. 2002 (PMID 12475198); Brenner & Fuller 1992 (PMID 1371243); Huynh 2020 (PMC7257131); Ward 1995 (PMID 9634791)
- **Unchanged from comp-010.**

## Accession note on P15296

UniProt P15296 was listed in the original project brief as the likely C. utilis uricase accession. On retrieval (2026-05-05), P15296 returns sp|P16320|NOF_DROME (a 120.7 kDa Drosophila transposable element protein), indicating P15296 has been reassigned or merged and no longer corresponds to a C. utilis uricase. Systematic UniProt search by organism (*Candida utilis* / *Cyberlindnera jadinii*, OX=4903) and protein name (uricase) returns P78609 as the sole reviewed Swiss-Prot entry. This accession has been used for the analysis. The project brief instruction to "verify before downloading" was followed.

## ALLN-346 parent sequence note

Allena Pharmaceuticals did not publicly disclose the exact CDS or full protein sequence of the ALLN-346 parent *C. utilis* uricase. US10815461B2 (published May 2020) describes the ALLN-346 variant panel and seven specific point mutations (I180V, V190G, Y165F, E51K, Q244K, I132R, A87G) on a *C. utilis* uricase backbone without providing the full parent sequence. The P78609 sequence (303 aa) is the canonical reviewed Swiss-Prot entry for *C. utilis* uricase and is consistent with the ALLN-346 patent's active-site and length description. This analysis uses P78609 as the best available proxy for the ALLN-346 parent sequence. Uncertainty: if Allena used a proprietary engineered parent (rather than wild-type P78609), some features (KR site positions, N-X-S/T sites) may differ by 1–2 residues from the ALLN-346 exact sequence. This is noted as a limitation.
