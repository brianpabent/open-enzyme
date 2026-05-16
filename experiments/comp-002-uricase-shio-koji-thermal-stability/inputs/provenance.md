# Input Provenance — comp-002

| File | Source | Version / Date fetched | URL / Citation |
|---|---|---|---|
| `Q00511.fasta` | UniProt REST API | UniProt release 2025_03; copied from comp-001/inputs on 2026-05-16 | https://rest.uniprot.org/uniprotkb/Q00511.fasta |
| `alphafold_Q00511_plddt.json` | AlphaFold Protein Structure Database (EMBL-EBI); B-factor column of PDB = per-residue pLDDT | AlphaFold v6 model; copied from comp-001/inputs on 2026-05-16 | https://alphafold.ebi.ac.uk/files/AF-Q00511-F1-model_v6.pdb |
| `tetramer_interface_residues.json` | Hand-encoded interface residue footprint from published *A. flavus* uricase crystal structure analyses (PDB 1R56 + Colloc'h et al. 1997) | 2026-05-16 | Retailleau et al. 2004, Acta Cryst D60:453-462; Colloc'h et al. 1997, Nat Struct Biol 4:947-952 |
| `biophysical_priors.json` | Primary literature biophysical parameters (Tm, half-life, pH-activity curve, salt-stability factors) for WT *A. flavus* uricase | 2026-05-16 | Imani & Shahmohamadnejad 2017 (PMID:28667645, DOI:10.1007/s13205-017-0841-3); Rezaeian Marjani et al. 2020 (PMID:33850949, DOI:10.30498/IJB.2020.2662); Timasheff 2002 (Biochemistry 41:13473); Daniel & Danson 2010 (Trends Biochem Sci 35:584) |

## Protein identity

- **UniProt accession:** Q00511
- **Protein name:** Uricase (urate oxidase), *Aspergillus flavus*
- **Gene:** uaZ
- **Length:** 302 amino acids in the AlphaFold model and the source FASTA (full precursor including iMet). UniProt mature CHAIN is 2..302 = 301 aa after iMet removal (INIT_MET FT entry: "Removed"). For this analysis, the AlphaFold pLDDT array is 1-indexed across all 302 model residues, and the FASTA sequence is the 302-residue precursor — internally consistent. The 1-aa precursor-vs-mature discrepancy does not affect this analysis (no residue-position-specific load-bearing claim depends on the 301/302 distinction).
- **Quaternary structure:** D2-symmetric homotetramer (confirmed by UniProt CC SUBUNIT line, ECO:0000269|PubMed:16478683)
- **Native disulfides:** ZERO — UniProt Q00511 feature table contains no DISULFID entries. WT tetramer integrity is purely non-covalent (hydrophobic packing + interfacial ion pairs + hydrogen bonds). This is load-bearing for the comp-002 analysis: there are no covalent constraints holding the tetramer together against thermal/pH perturbation. Engineered disulfide variants (Ala6Cys, Ser282Cys — Rezaeian Marjani 2020) exist but are out of scope here.
- **Active sites:** residues 11, 58, 257 (charge relay system; UniProt FT ACT_SITE annotations, PDB 4N3M/4N9M/4N9S/4N9V evidence)

## Key biophysical priors — primary-source verification

### Tm (melting temperature)

- **Value used: 27°C** for WT *A. flavus* uricase in standard buffer
- **Primary source:** Imani & Shahmohamadnejad 2017, *3 Biotech* 7:201, DOI:10.1007/s13205-017-0841-3 (PMID:28667645)
- **Abstract quote (grep-verified):** "The presence of raffinose increased UOX T[m] to a lesser extent, whereas lactose notably enhanced the T[m] from 27 to 37°C." → WT Tm = 27°C; lactose-supplemented Tm = 37°C
- **Implication for comp-002:** Shio-koji fermentation at 22°C sits 5°C below WT Tm. This is a tighter thermal margin than is typically assumed for industrial enzymes. The Tm = 27°C result is per-monomer thermal denaturation as detected by activity loss; tetramer-disassembly threshold may differ.

### Thermal half-life at 40°C

- **Value used: 38 min** for WT enzyme
- **Primary source:** Imani & Shahmohamadnejad 2017 (PMID:28667645)
- **Abstract quote (grep-verified):** "Half-life and T[m] analysis showed that UOX half-life is almost 38 min" — context is thermal inactivation studies at 40°C ("Thermal inactivation studies at 40°C showed that nearly 15% of UOX activity was preserved")
- **Independent cross-check:** Rezaeian Marjani et al. 2020 (PMID:33850949): "Estimation of half life for wild-type enzyme demonstrated 38.5 min" — independent group, similar order of magnitude.
- **Implication for comp-002:** Two independent papers converge on ~38 min half-life at the 40°C thermal-inactivation reference. This is the empirical anchor for Arrhenius extrapolation to shio-koji 22°C.

### pH-activity profile

- **Values used (fraction of pH-optimum activity, see `biophysical_priors.json`):** pH 4.5 → 0.12; pH 5.0 → 0.25; pH 5.5 → 0.45; pH 6.0 → 0.65; pH 7.0 → 0.90
- **Sources:** Rezaeian Marjani et al. 2020 (PMID:33850949) places WT pH optimum at 7; broader literature (rasburicase product information, Sanofi-Aventis Elitek package insert) places enzymatic activity range at pH 7.5-9.0 with sharp dropoff below pH 6. The pH 4.5 / 5.0 / 5.5 / 6.0 values are interpolated/estimated from these references — they are NOT direct per-pH measurements at every point. Uncertainty: ±0.10 fraction at each value below pH 7.0.
- **Caveat:** pH 4.5-6.0 readings are below the active-stable range of native uricase. Activity readouts at these pH values may reflect partial denaturation + reduced catalytic turnover combined.

### Salt-stability factor (preferential hydration)

- **Value used: +5.8% net stabilization at 17.5% NaCl**
- **Source:** Timasheff 2002, *Biochemistry* 41:13473 — kosmotrope-mediated stabilization theory; 5-20% ΔΔG_unfolding gain at ~3 M NaCl is typical for globular proteins.
- **Counterbalancing factor:** Ion-pair screening at very high [NaCl] reduces interfacial salt-bridge stabilization energy by ~5-15%. Combined: 1.15 (hydration gain) × 0.92 (ion-pair loss) = 1.058 net.
- **Caveat:** This is a generic globular-protein prior, not measured for Q00511 specifically. The true Q00511 behavior may deviate; AUC or DSF in 15-20% NaCl on purified uricase would tighten this materially.

## Interface residue footprint

- Source: PDB 1R56 (Retailleau et al. 2004, Acta Cryst D60:453-462) and Colloc'h et al. 1997, Nat Struct Biol 4:947-952
- The interface residue ranges in `tetramer_interface_residues.json` are **approximate footprints derived from published structural analyses** — not coordinates extracted in this analysis run (which uses stdlib only, no PDB parser). A future comp-NNN using a proper PDB parser (e.g., Biopython on a real workstation) would tighten the interface footprint by 1-3 residues per range.
- The 3 named interface salt-bridge pairs in the JSON file are inferred from the sequence + published interface footprint, not directly coordinated-extracted. Treat as a model-with-stated-assumptions, not as ground truth.

## Multilingual literature check (2026-05-16)

Per CLAUDE.md "Global-multilingual research by default" rule. Sources checked for non-English literature on koji + protein thermal/pH stability:

- **J-STAGE / J-GLOBAL (Japanese):** Searched for shio-koji protein stability; the canonical Japanese-origin literature on koji protease salt-tolerance (Tominaga & Tsujisaka, Ikeda et al.) is cited in comp-001's protease analysis and is the primary Japanese contribution to this question domain. No additional Japanese-language papers specifically on heterologous protein thermal stability *in shio-koji* were identified. Soy-sauce fermentation literature (Ito & Matsuyama 2021, *J Fungi*, PMC8399179 — koji-author paper published in English) covers koji enzymology in the same biophysical regime.
- **CNKI / WanFang (Chinese):** Searched for Chinese-language uricase stability / sodium chloride papers. The accessible literature on Q00511 thermal stability is dominated by Iranian (Imani, Rezaeian Marjani) and Indian (engineered-yeast precedents) groups publishing in English. No additional Chinese-language primary thermal-stability data on *A. flavus* uricase identified.
- **Conclusion:** For this specific question (thermal/pH/salt stability of *A. flavus* Q00511), the primary literature is predominantly English-language. Multilingual search did not surface additional load-bearing primary data. This finding does not weaken the multilingual default — the search was performed, the result is empirical, not a "language barrier" excuse.

## Method note — stdlib-only constraint

Per CLAUDE.md and the comp-001 design pattern, `analyze.py` uses Python stdlib only (no GROMACS, OpenMM, Rosetta, MDAnalysis, or Biopython). The analysis is therefore:

- **NOT** a molecular dynamics simulation (no 50-100 ns trajectory of the tetramer in explicit solvent)
- **NOT** a Rosetta ΔΔG calculation (no force-field-based interface energetics)
- **IS** a composite biophysical scoring framework combining: (i) AlphaFold pLDDT-derived interface integrity, (ii) Arrhenius extrapolation of measured 40°C half-life to ferment conditions, (iii) Henderson-Hasselbalch-derived pH-dependent ion-pair stability at known interface, (iv) Hofmeister/preferential-hydration model for salt effects, (v) per-condition retention-fraction prediction over the 7-14 day ferment window with explicit uncertainty bounds

The brief acknowledges the MD/Rosetta path as the rigorous next step; that path is named in `wiki-archive.md` Limitations as the load-bearing follow-up if §1.10 wet-lab data deviates from this analysis's predictions.
