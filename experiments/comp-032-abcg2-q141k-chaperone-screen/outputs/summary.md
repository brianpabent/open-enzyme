# comp-032 — ABCG2 Q141K Pharmacological-Chaperone Virtual Screen

**Target:** Human ABCG2 (UniProt Q9UNQ0), Q141K variant (rs2231142, p.Gln141Lys)

**AlphaFold model:** AF-Q9UNQ0-F1-model_v6 (monomer, 655 aa)

**Q141 confidence (AlphaFold pLDDT):** 97.06 / 100

---

## Verdict

**GREEN — Shortlist of 10 candidates** passes the four-gate filter + drug-class diversity filter (max 2 per class). Recommend per-hit cell-based Q141K trafficking-rescue assay (HEK293-ABCG2-Q141K transfectant + apical-membrane localization readout, e.g., flow cytometry against extracellular 5D3 epitope). Triage further by real-docking re-screen (AutoDock Vina) before wet-lab commit.

---

## Positive-control validation

CFTR-corrector class is the load-bearing positive control. If these don't score above the decoy mean, the heuristic is uninformative.

| Control | Composite | Rank | Top-percentile |
|---|---|---|---|
| ivacaftor | 0.861 | 9 / 134 | top 6.7% |
| tezacaftor | 0.902 | 7 / 134 | top 5.2% |
| elexacaftor | 0.829 | 14 / 134 | top 10.4% |
| lumacaftor | 1.000 | 1 / 134 | top 0.7% |

| Comparison | Value |
|---|---|
| Decoy mean composite | 0.581 |
| Decoy max composite | 0.684 |
| All controls above decoy mean? | **YES** |
| All controls above decoy max? | **YES** |

> **Positive-control pass.** All CFTR correctors score above the highest-scoring decoy — heuristic separates the chaperone-class signal from the decoy noise.

---

## Pocket descriptor (Q141 NBD)

| Metric | Value |
|---|---|
| Anchor residue | GLN 141 (pLDDT 97.1) |
| Pocket radius (Q141 CA centered) | 10.0 A |
| Residues in pocket | 21 |
| Mean pLDDT across pocket | 95.6 / 100 |
| Pocket charged residues (positive) | 4 |
| Pocket charged residues (negative) | 1 |
| WT pocket net charge | 3 |
| Q141K pocket net charge | 4 (delta +1 from Q -> K) |
| Aromatic residues in pocket | 2 |
| Hydrophobic residues in pocket | 10 |
| Distance Q141 to Walker A (80-87) | 28.23 A |
| Distance Q141 to ATP loop 2 (184-190) | 16.51 A |
| Overlaps ATP pocket? | NO (chaperone site distinct from ATP pocket) |

---

## Top-20 ranked candidates (raw, pre-gate)

| Rank | Name | Class | Composite | Tier | PK |
|---|---|---|---|---|---|
| 1 | lumacaftor | CFTR corrector | 1.000 | tier2_component_of_approved | oral_bioavailable |
| 2 | tafamidis | Transthyretin tetramer stabilizer | 0.956 | tier2_component_of_approved | oral_bioavailable |
| 3 | ursodiol | Bile acid chaperone (UDCA) | 0.956 | tier1_usp_nf | oral_bioavailable |
| 4 | diflunisal | NSAID + TTR stabilizer (off-label) | 0.950 | tier1_usp_nf | oral_bioavailable |
| 5 | tauroursodeoxycholic_acid | Bile acid chaperone (TUDCA) | 0.934 | tier2_component_of_approved | oral_bioavailable |
| 6 | deflazacort | Corticosteroid (Duchenne stabilizer effect) | 0.919 | tier2_component_of_approved | oral_bioavailable |
| 7 | tezacaftor | CFTR corrector | 0.902 | tier2_component_of_approved | oral_bioavailable |
| 8 | romidepsin | HDAC inhibitor | 0.884 | tier2_component_of_approved | iv_only |
| 9 | ivacaftor | CFTR potentiator | 0.861 | tier2_component_of_approved | oral_bioavailable |
| 10 | minocycline | Tetracycline | 0.854 | tier1_usp_nf | oral_bioavailable |
| 11 | ambroxol | Pharmacological chaperone (GCase, off-label) | 0.849 | tier1_usp_nf | oral_bioavailable |
| 12 | ganetespib | Hsp90 inhibitor (research) | 0.844 | not_503a | iv_only |
| 13 | vorinostat | HDAC inhibitor | 0.836 | tier2_component_of_approved | oral_bioavailable |
| 14 | elexacaftor | CFTR corrector | 0.829 | tier2_component_of_approved | oral_bioavailable |
| 15 | ko143 | ABCG2 inhibitor (research) | 0.824 | not_503a | oral_bioavailable |
| 16 | curcumin | Polyphenol / ABCG2 inhibitor | 0.824 | tier1_usp_nf | oral_bioavailable |
| 17 | glycerol_phenylbutyrate | Ammonia scavenger / chaperone | 0.821 | tier2_component_of_approved | oral_bioavailable |
| 18 | fumitremorgin_c | ABCG2 inhibitor (research) | 0.818 | not_503a | oral_bioavailable |
| 19 | naringenin | Flavonoid | 0.812 | tier1_usp_nf | oral_bioavailable |
| 20 | ver155008 | Hsp70 inhibitor (research) | 0.806 | not_503a | iv_only |

---

## Final shortlist (post-gate)

| Rank | Name | Drug class | Composite | 503A tier | CNS pen | Q141K rescue rationale |
|---|---|---|---|---|---|---|
| 1 | lumacaftor | CFTR corrector | 1.000 | tier2_component_of_approved | no | Same ABC superfamily as CFTR; clinically validated F508del-CFTR corrector at the NBD/TMD interface — strongest mechanistic prior in the shortlist. |
| 2 | tafamidis | Transthyretin tetramer stabilizer | 0.956 | tier2_component_of_approved | yes | Transthyretin tetramer stabilizer; binds at a hydrophobic-aromatic interface, structurally analogous to the pocket type Q141K presents. Highly selective for misfolded state. |
| 3 | ursodiol | Bile acid chaperone (UDCA) | 0.956 | tier1_usp_nf | no | Bile acid (UDCA); broad ER-stress chemical chaperone via ATF6/Hsp70 axis; reduces aggresome retention in F508del-CFTR and TTR amyloid models. |
| 4 | diflunisal | NSAID + TTR stabilizer (off-label) | 0.950 | tier1_usp_nf | yes | TTR stabilizer + NSAID; off-label use for hereditary ATTR amyloidosis (pre-tafamidis). Anionic at pH 7.4 — strong electrostatic match for Q141K +1 pocket. |
| 5 | tauroursodeoxycholic_acid | Bile acid chaperone (TUDCA) | 0.934 | tier2_component_of_approved | yes | TUDCA; bile-acid chemical chaperone; specifically used in F508del-CFTR rescue programs and ALS clinical trials. CNS-penetrant. |
| 6 | deflazacort | Corticosteroid (Duchenne stabilizer effect) | 0.919 | tier2_component_of_approved | yes | Corticosteroid; secondary chaperone-activity literature in Duchenne (dystrophin trafficking). FDA-approved for DMD. |
| 7 | ivacaftor | CFTR potentiator | 0.861 | tier2_component_of_approved | no | CFTR potentiator; binds at TMD-NBD gating interface. Gating mechanism not folding rescue, but ABC-superfamily binding validates the pocket-fit profile. |
| 8 | minocycline | Tetracycline | 0.854 | tier1_usp_nf | yes | Tetracycline antibiotic with documented neuroprotective chaperone-like activity (huntingtin, alpha-synuclein); CNS-penetrant. |
| 9 | ambroxol | Pharmacological chaperone (GCase, off-label) | 0.849 | tier1_usp_nf | yes | GCase pharmacological chaperone (off-label Gaucher / GBA-Parkinson trials); mucolytic indication. Direct precedent for an FDA-approved drug being repurposed as a pharmacological chaperone. |
| 10 | vorinostat | HDAC inhibitor | 0.836 | tier2_component_of_approved | yes | HDAC inhibitor; the Basseville 2012 rescue precedent for Q141K-ABCG2 specifically (rescues trafficking from aggresome). Mechanism is HDAC-mediated, not direct binding — but the heuristic correctly elevates it. |

---

## Limitations

1. **Heuristic is NOT real docking.** No 3D pose, no conformer sampling, no scoring function trained on co-crystal data. Real binding affinity could re-order the ranking. The shortlist is a triage layer, NOT a final hit list — every shortlisted molecule needs an AutoDock Vina or DiffDock re-screen before any wet-lab assay is funded.
2. **Library size 134 << full DrugBank (~3,800 approved entries).** Coverage is enriched for chaperone/CFTR/ABC classes (the brief categories) plus decoy classes for control. The screen does NOT exhaustively cover the FDA-approved surface — molecules outside the curated classes could be missed. Mitigation: the chaperone-class prior is the strongest signal; molecules outside known chaperone classes carry a low prior in this framework anyway.
3. **Q141K mutant structure is INFERRED from WT AlphaFold + sidechain reasoning, NOT independently predicted.** A true Q141K AlphaFold model (via ColabFold mutation) would refine the pocket descriptor. The +1 charge perturbation we apply is qualitatively correct (Q -> K adds a positive charge) but does not capture mut-induced conformational reorganization. Most importantly: Q141K's mild folding defect may NOT be due to a localized pocket change — it may be due to destabilization of the Q141 backbone hydrogen-bonding pattern with the ATP-binding loop, which a side-chain-replacement model cannot capture.
4. **No solvent / membrane context.** ABCG2 is a membrane protein; the NBD is cytoplasmic but the full transporter assembles as a homodimer with TMDs in the lipid bilayer. The AlphaFold monomer is not the biological assembly. Real chaperone binding must accommodate the dimer interface and TMD context.
5. **CFTR-corrector mechanism is debated.** Ivacaftor binds to CFTR directly; tezacaftor/elexacaftor act on the TMD-NBD interface. The Q141K rescue mechanism, if it exists, may be at a TMD-NBD interface site that this NBD-centric pocket does not cover. The brief asked for an NBD virtual screen because Q141K is in the NBD; this is the correct first cut but does not exhaust the corrector binding-site possibilities.
6. **The 503A bulk-API availability flag is preliminary.** Final 503A eligibility requires per-compound USP/NF monograph check (Tier 1) or current FDA-approved drug product status (Tier 2). The library uses class-level approximations; per-hit verification is required before any compounding-pharmacy partner conversation.
7. **No Q141K vs WT selectivity test.** A real chaperone needs to bind preferentially to the misfolded variant — binding equally to WT and Q141K only adds inhibition (bad). This screen ranks by Q141K-pocket fit, NOT by selectivity. Selectivity must be assessed wet-lab.
8. **Verdict provisional regardless of shortlist size.** A GREEN verdict here means "worth a real-docking re-screen"; it does NOT mean "clinical candidate ready." A RED verdict means "FDA-approved surface is poorly populated for this target at heuristic resolution"; it does NOT mean "chaperone rescue is impossible" — novel-binder design via RFdiffusion remains a coherent next step.

---

## Impact on experimental priorities

This comp-032 result feeds the next-step decision tree for the pharmacological-chaperone track ([`chassis-pending-interventions.md` §7](../wiki/chassis-pending-interventions.md)).

- **GREEN shortlist (>= 4 candidates):** open compounding-pharmacy partner conversation in parallel with a real-docking re-screen. Top 3 candidates queued for HEK293-Q141K trafficking-rescue assay (~$8-15K wet-lab cost).
- **YELLOW shortlist (1-3 candidates):** real-docking re-screen first; wet-lab only if real docking confirms. Compounding-pharmacy conversation deferred until wet-lab confirmation.
- **RED shortlist (zero candidates):** drop the repurposing-surface thesis for this target. Pivot the Q141K chaperone track to AI-aided novel binder design (RFdiffusion + ProteinMPNN + AlphaFold confidence-filter pipeline). The novel-binder path is significantly more expensive ($50-150K compute + IP path) but is the only remaining option for this chokepoint.

---

*Generated by `analyze.py` on the inputs documented in `inputs/provenance.md`. Heuristic scoring; no external dependencies. Re-run with `python3 analyze.py` after any library or pocket-radius update.*