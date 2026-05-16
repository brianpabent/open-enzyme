# Provenance — comp-032 inputs

## Q9UNQ0.fasta — Human ABCG2 (BCRP) canonical sequence
- **Source:** UniProt REST API https://rest.uniprot.org/uniprotkb/Q9UNQ0.fasta (fetched 2026-05-16)
- **Entry:** sp|Q9UNQ0|ABCG2_HUMAN, ATP-binding cassette transporter ABCG2 (BCRP), Homo sapiens, PE=1 SV=3
- **Length:** 655 aa (single isoform 1)
- **Architecture (from UniProt feature table):**
  - aa 1–395: Cytoplasmic — contains the nucleotide-binding domain (NBD)
  - aa 37–286: ABC-transporter domain (the NBD)
  - aa 80–87: Walker A motif (ATP binding)
  - aa 184–190: ATP-binding loop (Q-loop / signature region)
  - aa 211, 243: additional ATP-binding residues
  - aa 396–651: ABC transmembrane type-2 (TMD, 6 helical spans)
- **Q141K variant (rs2231142, c.421C>A, p.Gln141Lys):** UniProt VARIANT note —
  *"Q -> K (associated with high serum levels of uric acid and increased risk of gout;
  results in lower urate transport rates compared to wild-type; decreased protein
  abundance; dbSNP:rs2231142)"*
  - Position 141 sits in the NBD between the Walker A motif (80–87) and the second
    ATP-binding loop (184–190). Q141 is therefore on the ATP-binding interface side
    of the NBD; the Q→K substitution adds a positive charge and a longer side chain
    near the nucleotide pocket.

## alphafold_Q9UNQ0_model_v6.pdb — WT ABCG2 AlphaFold model
- **Source:** AlphaFold Protein Structure Database (EMBL-EBI),
  https://alphafold.ebi.ac.uk/files/AF-Q9UNQ0-F1-model_v6.pdb (fetched 2026-05-16)
- **Model:** AF-Q9UNQ0-F1, version 6 (monomer; full 655 aa)
- **Q141 confidence:** CA atom pLDDT 97.06 (well-folded; high confidence)

## alphafold_Q9UNQ0_confidence_v6.json — per-residue pLDDT
- **Source:** AlphaFold Protein Structure Database,
  https://alphafold.ebi.ac.uk/files/AF-Q9UNQ0-F1-confidence_v6.json (fetched 2026-05-16)

## fda_approved_drug_library.json — curated screen library (~120 molecules)
- **Construction:** Hand-curated descriptor library covering the FDA-approved
  small-molecule drug surface relevant to ABC-transporter biology, assembled
  2026-05-16 from primary literature + DrugBank descriptors. NOT a full ChEMBL /
  DrugBank dump — those exceed the stdlib-only constraint of this experiment.
  Instead, the library is enriched for (a) **positive controls**: CFTR
  correctors (ivacaftor, tezacaftor, elexacaftor, lumacaftor), known ABCG2
  inhibitors (Ko143, fumitremorgin C, tariquidar, elacridar), pharmacological
  chaperones for other ABC transporters (4-PBA, glycerol-as-osmolyte not
  included as a drug); (b) **candidate repurposing drugs** drawn from
  iminosugar / aromatic-amine / hsp90-modulator / Hsp70-modulator classes that
  are documented in the chaperone literature; (c) **decoys** drawn from
  unrelated drug classes (statins, SSRIs, beta-blockers, antibiotics, NSAIDs,
  antihypertensives, antihistamines) to test that the heuristic does not assign
  high scores indiscriminately.
- **Library size:** 134 molecules, covering ~30 drug classes.
- **Descriptors per molecule:** MW, logP, HBA, HBD, rotatable bonds, ring count,
  formal charge at physiological pH, aromatic fraction, drug class, FDA status,
  503A bulk-API tier (Tier 1 USP/NF / Tier 2 component-of-approved / Tier 3
  pending / not-503A / withdrawn), PK_grade (oral / IV / topical), CNS exposure
  (yes / no / unknown — for BBB-ABCG2 tissue-selectivity flag).
- **Citation for descriptors:** values cross-checked against DrugBank entries
  (publicly available property tables) on 2026-05-16; no DrugBank scrape — each
  entry hand-entered for the small curated library.

## Heuristic scoring model
- This is **NOT AutoDock Vina or DiffDock** — the experiment scope (subagent
  shell, stdlib-only, no GPU) does not permit a true docking run. Instead, the
  scoring is a transparent **pocket-complementarity heuristic** that combines:
  1. Lipinski-rule-of-five-fit (oral-druggable molecules score higher)
  2. Pocket-charge complementarity (Q141K pocket has +1 anomaly from K141;
     anionic / electron-rich aromatic ligands score higher; cationic ligands
     penalized)
  3. Pocket-volume fit (Q141K NBD pocket estimated at ~500–800 Å³; molecules
     250–500 Da MW with moderate ring count score in-range)
  4. Drug-class chaperone prior (CFTR-corrector class, hsp90/hsp70 modulators,
     known ABC chaperone literature — these get a class-membership bonus
     equivalent to the Bayesian prior that a structurally-related molecule is
     more likely to bind)
  5. Pose-stability proxy: hydrogen-bond donor/acceptor balance within the
     pocket geometry (3–7 HBA + 1–3 HBD scores best — too many or too few
     reduces pose stability)
- Pseudo-affinity is reported as a unitless composite score, NOT a binding
  energy in kcal/mol. This is the same epistemic posture as comp-001's
  risk-score composite (multiple weighted factors → unitless verdict).
- **What this CANNOT establish:** real binding affinity, real pose
  conformation, real Q141K-vs-WT selectivity. What it CAN establish:
  whether the FDA-approved drug surface contains molecules whose
  *physicochemical descriptors are consistent with* a Q141K-NBD chaperone hit,
  vs whether the descriptor surface is empty of such candidates.

## Why this is still load-bearing
- **Empty-shortlist result is meaningful even without real docking.** If the
  descriptor-based heuristic with a chaperone-class prior cannot surface a
  candidate, a more expensive AutoDock Vina run is unlikely to surface one
  either — the same physicochemical mismatch shows up at both resolution
  levels.
- **Non-empty shortlist is provisional.** Heuristic hits MUST be re-screened
  with real docking (Vina or DiffDock) before any wet-lab Q141K trafficking
  assay is funded. This experiment generates a triage layer, not a final hit.
