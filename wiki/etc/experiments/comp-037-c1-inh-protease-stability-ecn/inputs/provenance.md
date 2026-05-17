# Provenance — comp-037 inputs

## P05155.fasta — Human C1-INH / SERPING1 sequence

- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P05155.fasta
- **Fetch date:** 2026-05-17
- **Entry:** sp|P05155|IC1_HUMAN Plasma protease C1 inhibitor, Homo sapiens, PE=1 SV=2
- **Length:** 500 aa (canonical isoform, including signal peptide aa 1–22)
- **Annotation boundaries (UniProt P05155 SV=2, grep-verified against the text-format flatfile):**
  - Signal peptide: aa 1–22 (cleaved during ER-targeted secretion in native context; replaced by EcN-native secretion signal in the engineered LBP construct)
  - Mature chain: aa 23–500 ("Plasma protease C1 inhibitor")
  - Mature length: 478 aa
  - Reactive-bond / scissile loop (RCL): R466-T467 (P1-P1' for C1S substrate-mimicry — UniProt SITE 465..466 "Reactive bond for chymotrypsin"; SITE 466..467 "Cleavage; by C1S" + "Reactive bond"). C1-INH inhibits C1r/C1s and MASP-2 by presenting this RCL as a pseudo-substrate, then forming a covalent acyl-enzyme intermediate (serpin suicide mechanism).
- **Glycosylation sites (UniProt CARBOHYD features, all grep-verified):**
  - **N-linked (6 sites in canonical isoform + 1 variant-TA site):** N25, N69, N81, N238, N253, N272 (variant TA), N352. Sequon N-X-(S/T) confirmed for all 7 by direct sequence inspection (N25-A-T, N69-L-T, N81-A-T, N238-L-S, N253-N-S, N272-K-I — note N272 violates the canonical S/T rule at +2 and is annotated as a variant-only site, included here for completeness; N352-A-S).
  - **O-linked (8 sites, all in the mucin-like tandem-repeat region aa 47-96):** T47, T48, S64, T71, T83, T88, T92, T96.
  - **Total glycosylation load:** ~26 kDa of glycan on the ~52 kDa polypeptide (Bos 1998; Stavenhagen 2018 mass-spec characterization, PMID 29381136). The mucin-like O-glycan domain (aa 47-96) carries the bulk of the mass and is essential for plasma half-life in the native circulating context.
- **Disulfide bonds (UniProt DISULFID features, grep-verified, evidence: Bos 1998 PMID 9799502 + crystal structure 17488724):**
  - C123 ↔ C428 (1 bond)
  - C130 ↔ C205 (1 bond)
  - **Total disulfides: 2** (canonical for a serpin; verified by direct grep against the UniProt flatfile). C1-INH does not have the dense disulfide architecture of CD55 (8 per SCR1-4) or DAF.
- **Structural / functional regions:**
  - Mucin-like N-terminal extension (heavily O-glycosylated, disordered): aa 23-119 (mature aa 1-97); 7 × 4-aa tandem repeats of [QE]-P-T-[TQ] at aa 85-119 per UniProt REGION annotation. UniProt annotates aa 20-43 and aa 65-118 as Disordered (MobiDB-lite), with aa 67-118 as Low Complexity. **This region is the dominant disordered liability in a non-glycosylated bacterial expression context.**
  - Serpin core (canonical serpin fold, ~120-450 mature): well-folded β-sheet + α-helix architecture. AlphaFold pLDDT 80+ across most of this region.
  - Reactive-center loop (RCL): aa ~452-467, exposed and flexible — load-bearing for inhibitor mechanism but inherently protease-accessible by design.

- **Engineering note:** For EcN LBP expression of a secreted luminal C1-INH, the human signal peptide (aa 1-22) would be replaced with an EcN-native secretion signal (e.g., OmpA, PelB, or YebF for extracellular release). The mucin-like O-glycan domain (aa 23-119) is a candidate for truncation — see comp-006 → comp-012 precedent where a Ser/Thr stalk was removed to rescue verdict. C1-INH N-glycans (essential for native plasma half-life) are NOT producible in EcN — bacterial N-glycosylation systems (e.g., the *C. jejuni* pgl pathway) exist but are not implemented in EcN by default and produce different glycan structures.

## alphafold_P05155_plddt.json — Per-residue pLDDT confidence scores

- **Source:** AlphaFold Protein Structure Database (EMBL-EBI)
  - Confidence scores: https://alphafold.ebi.ac.uk/files/AF-P05155-F1-confidence_v6.json
- **Model:** AF-P05155-F1, version 6 (canonical isoform, 500 residues)
- **Fetch date:** 2026-05-17
- **Field used:** `confidenceScore` array, re-indexed to 1-indexed string keys to match `experiments/lib/protease_stability.py::load_plddt()` format.
- **Mean pLDDT:** 79.6 / 100 (computed in analyze.py output)
- **Notable disordered region:** N-terminal mucin-like domain (aa 1-119, signal peptide + O-glycan tandem-repeat region) is consistently pLDDT < 60 in the AlphaFold model, reflecting the inherent disorder of this region (confirmed independent of bacterial-expression context).

## protease_specificities.json — EcN-luminal protease panel + colonic-lumen conditions

**Protease-panel sources:**

- **Trypsin (S01.151):** MEROPS database release 12.4; specificity from Schechter & Berger 1967 (P1=K/R); pH curve from Northrop 1932 + Polgar 2005 review. Residual colonic activity well-documented (Carroll 2013 PMID 23859510, fecal-protease characterization).
- **Chymotrypsin (S01.001):** MEROPS; specificity from Schechter & Berger 1967 + Hedstrom 2002 (chemRev PMID 12475195 review); P1 = F/W/Y/L/M.
- **Pancreatic elastase (S01.153):** MEROPS; specificity from Largman 1976 (PMID 988044 review) and Bode 1989 crystal-structure analysis; P1 = small aliphatic (A/V/G/S/L/I/T).
- **OmpT (A26.001):** Dekker 2001 *J Biol Chem* 276:8408 PMID 11226160 (di-basic P1-P1' specificity, K/R-X-X-K/R); Hwang 2007 *Biochem Biophys Res Commun* 360:21 PMID 17263510 (extended specificity refinement). Vandeputte-Rutten 2001 crystal structure (PMID 11566123).
- **DegP / HtrA (S01.273):** Krojer 2008 *Nature* 453:885 PMID 18261546 (substrate engagement); Clausen 2002 review (PMID 12235144); broad hydrophobic P1 preference (V/I/L/F/Y/A).

**Conditions modeled:**

- **pH 6-7:** Colonic-lumen pH range (Fallingborg 1999 PMID 10204470).
- **37°C:** Body temperature.
- **NaCl ~0.9% (~0.15 M):** Physiological extracellular. Held outside the lib's 10-20% salt-inhibition interpolation window — therefore no salt inhibition applied (correct for this environment; the shio-koji-derived lib field name 'NaCl_pct' is retained for API compatibility but the value is set to colonic-physiological).
- **Residence time 1-7 days:** Bracketed by colonic mass-transit (~24-48 h) and longer niche-resident persistence of EcN (up to ~weeks under colonization conditions, Sonnenburg-lab and Synlogic clinical data).
- **Bile-acid exposure:** Present in vivo but not modeled here as a protease-activity modifier. Bile acids can denature proteins and potentially enhance protease access to unfolded regions; treated here as out-of-model.

**Why this panel and not the full colonic-microbiome protease landscape:**

The colonic lumen contains contributions from dozens of bacterial proteases (commensal Bacteroides, Clostridia, etc.) in addition to the host-derived pancreatic enzymes. The five proteases modeled here are the dominant identifiable risks for a heterologous secreted serpin in an EcN LBP context: (1) pancreatic enzymes that reach the colon at residual activity, (2) EcN's own outer-membrane and periplasmic quality-control proteases that act on the heterologous protein during export. Commensal-bacterial proteases are a meaningful additional risk axis but are not well-characterized at the per-enzyme specificity level for this purpose — they would add diffuse risk but are unlikely to redirect the verdict qualitatively. This is the same scope-of-modeling choice the comp-006/comp-012 koji pipeline made (three A. oryzae proteases as the dominant identifiable risks, not the full koji proteome).

**The lib's `shio_koji_conditions` JSON key is retained from the shared library for backward compatibility.** The semantics here are colonic-lumen, not shio-koji.
