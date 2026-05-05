# Provenance — comp-010 inputs

## Q00511.fasta — A. flavus uricase sequence
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/Q00511.fasta
- **Fetch date:** 2026-05-05 (originally fetched for comp-001)
- **Entry:** sp|Q00511|URIC_ASPFL Uricase, Aspergillus flavus, PE=1 SV=3
- **Length:** 301 aa (mature protein; no signal peptide; homotetramer in native context)
- **Gene:** uaZ — primary candidate per uricase-variant-selection.md; parent of rasburicase (FDA 2001)
- **Copy provenance:** Copied from experiments/comp-001-uricase-shio-koji-protease-stability/inputs/Q00511.fasta

## P02788.fasta — Human lactoferrin (lactotransferrin) sequence
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P02788.fasta
- **Fetch date:** 2026-05-05 (originally fetched for comp-005)
- **Entry:** sp|P02788|TRFL_HUMAN Lactotransferrin, Homo sapiens, PE=1 SV=6
- **Length:** 710 aa (canonical isoform, including signal peptide aa 1–19)
- **Signal peptide:** residues 1–19 (MKLVFLVLLFLGALGLCLA)
- **Mature protein:** residues 20–710 (691 aa)
- **N-glycosylation sites (UniProt annotation):** N137 (N-X-S: NIS), N478 (N-X-S: NVS), N623 (N-X-S: NKS)
- **Disulfide bonds (UniProt annotation):** 17 disulfide bonds (34 cysteine residues, fully paired)
- **Copy provenance:** Copied from experiments/comp-005-lactoferrin-shio-koji-protease-stability/inputs/P02788.fasta

## glucoamylase_carrier.fasta — A. awamori glucoamylase (Ward 1995 carrier protein)
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P69327.fasta
- **Fetch date:** 2026-05-05
- **Entry:** sp|P69327|AMYG_ASPAW Glucoamylase, Aspergillus awamori, PE=1 SV=1
- **Length:** 640 aa (includes signal peptide + propeptide + catalytic domain + Ser/Thr-rich linker stalk)
- **Role in Ward 1995 architecture:** N-terminal fusion carrier. The Ward 1995 design fuses the glucoamylase coding sequence (or its C-terminal catalytic domain) to the payload via a K-R KEX2 site. The host's endogenous Kex2p cleaves the KR dipeptide in the late secretory pathway, releasing mature payload. In the Huynh 2020 validation (PMC7257131), the specific design is P_amyB :: amyB signal peptide :: glucoamylase :: KRGGG :: payload :: T_amyB.
- **Citation:** Ward PP, Piddington CS, Cunningham GA, Zhou X, Wyatt RD, Conneely OM. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791); Huynh HH et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131)

## a_oryzae_codon_usage.json — A. oryzae RIB40 codon usage table
- **Source:** Codon Usage Database (Kazusa) — Aspergillus oryzae entry; cross-validated against:
  - Nakao M et al. Nucleic Acids Res 1992;20(21):5739-48 (PMID 1482437) — A. oryzae codon bias analysis
  - Machida M et al. Nature 2005;438:1157-61 (PMID 16372010) — A. oryzae RIB40 genome annotation
  - GC content of coding regions ~54% (consistent with Kazusa entry for A. oryzae)
- **Fetch date:** 2026-05-05 (manually transcribed from Kazusa database; values represent RSCU and freq/1000 for highly-expressed genes)
- **Units:** RSCU (Relative Synonymous Codon Usage) and freq_per1000 (frequency per 1000 codons)
- **Rare-codon threshold applied:** RSCU < 0.4 (i.e., codon used at < 40% of the neutral expected rate for that amino acid)
- **Limitation:** Codon usage tables vary by expression context (constitutive vs. inducible genes); the Kazusa table represents a genome-wide average. Highly-expressed secreted proteins (glucoamylase, amylase) may have slightly different preferences. Values should be treated as approximate (±15% error on RSCU estimates is typical for genome-wide tables).

## kex2_site_specs.json — KEX2 cleavage rules
- **Sources:**
  - Bathurst IC et al. Science 1987;235:348-50 — KEX2 recognition site KR|X (PMID 3099383)
  - Rockwell NC, Krysan DJ, Komiyama T, Fuller RS. Chem Rev 2002;102(12):4525-48 — comprehensive P1' preferences review (PMID 12475198)
  - Brenner C, Fuller RS. Proc Natl Acad Sci 1992;89:922-6 — P1' acidic residues abolish cleavage (PMID 1371243)
  - Huynh HH et al. Fungal Biol Biotechnol 2020;7:7 — KRGGG linker validated in A. oryzae (PMC7257131)
  - Ward PP et al. Biotechnology (N Y) 1995;13:498-503 — original glucoamylase-KR-hLf design (PMID 9634791)
- **Limitation:** KEX2 P1' rules are characterized mainly in S. cerevisiae Kex2p and mammalian furin. A. oryzae kexB enzyme specificity has not been independently published with a full P1' preference matrix. The rules here are the canonical Kex2p family rules, assumed to apply to A. oryzae kexB by homology (supported by Huynh 2020 validation of KRGGG cleavage in A. oryzae).
