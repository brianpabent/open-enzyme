# comp-036 — input provenance (CLAUDE.md Rule 4 pre-commit grep-verify gate)

Every load-bearing quantitative claim in comp-036 is named here, with primary source and verification status. The single-dose PK priors are **inherited** from comp-033 and re-validated through the Phase 1 sanity check (median single-dose Cmax 0.0256 ug/mL in comp-036 vs 0.0251 ug/mL in comp-033, matching within numerical precision).

## Verified directly against primary peer-reviewed sources (NEW for comp-036)

| Claim | Value | Source | Verified |
|---|---|---|---|
| IL-1Ra binds IL-1R1 with affinity nearly equal to IL-1 | qualitative anchor | Arend WP et al. J Clin Invest. 1990 May;85(5):1694-7. PMID 2139669. [DOI 10.1172/JCI114622](https://doi.org/10.1172/JCI114622). | **Verified** via PubMed metadata retrieval 2026-05-16. Abstract states recombinant 17 kDa IL-1Ra binds T-lymphocyte / synovial / chondrocyte IL-1 receptors with "affinity nearly equal to that of IL-1". |
| Competitive antagonism requires 10-100x molar excess of IL-1Ra over IL-1 for 50% biological inhibition | 10-100x range | Arend 1990 JCI (same paper). | **Verified** — "A 50% inhibition of these IL-1-induced biological responses requires amounts of IL-1ra up to 100-fold in excess of the amounts of IL-1 alpha or IL-1 beta present." This is the canonical statement establishing the competitive-antagonism excess factor used in the comp-036 supplementary IL-1-signaling-suppression calculation. |
| IL-1Ra crystal structure with IL-1R1 at 2.7 A | structural verification of binding mode | Schreuder H et al. Nature. 1997 Mar 13;386(6621):194-200. PMID 9062194. [DOI 10.1038/386194a0](https://doi.org/10.1038/386194a0). | **Verified** via PubMed metadata retrieval. All three Ig-like domains of IL-1R1 contact IL-1Ra; antagonist binds but does NOT engage the "receptor trigger site" (domain 3 conformational change) — explaining the antagonism mechanism. |
| IL-1beta-IL-1R1 crystal at 2.5 A (companion structure) | structural baseline | Vigers GP et al. Nature. 1997 Mar 13;386(6621):190-4. PMID 9062193. [DOI 10.1038/386190a0](https://doi.org/10.1038/386190a0). | **Verified**. Both structures are the canonical reference for IL-1 family ligand-receptor binding mode. |
| Anakinra 100 mg SC QD x 5 days is non-inferior to triamcinolone 40 mg SC for acute gout flare | Phase II RCT | Saag KG et al. Arthritis Rheumatol. 2021 Aug;73(8):1533-1542. PMID 33605029. [DOI 10.1002/art.41699](https://doi.org/10.1002/art.41699). | **Verified** via PubMed metadata retrieval. 165 patients, 301 flares; mean pain reduction baseline-to-24-72h: anakinra -41.2, triamcinolone -39.4 (p=0.688). Anakinra performed better on most secondary endpoints. **This is the clinical-efficacy anchor for the comp-036 receptor-occupancy decision rule.** |
| Anakinra and canakinumab efficacy in CKD-affected gout patients | review-level evidence | Pisaniello HL et al. Arthritis Res Ther. 2021 Apr 28;23(1):130. PMID 33910619. [DOI 10.1186/s13075-021-02416-y](https://doi.org/10.1186/s13075-021-02416-y). | **Verified** via PubMed metadata retrieval. G-CAN review; supports use of IL-1 inhibitors in CKD gout patients where NSAIDs/colchicine are contraindicated. Informs the patient-segmentation argument in the side-effect comparator framing. |

## Inherited from comp-033 (not re-derived in comp-036)

| Claim | Value | Source | Status |
|---|---|---|---|
| IL-1Ra (UniProt P18510) mature 17.3 kDa, 152 aa, non-glycosylated | structural identity | UniProt P18510 verified 2026-05-16 via `rest.uniprot.org/uniprotkb/P18510.txt` in comp-033 | Inherited from comp-033 provenance |
| Anakinra plasma Cmax 1.5 ug/mL, t1/2 4h, Vd 12-25 L at 100 mg SC QD | PK reference | Kineret USPI; Yang 2003; Granowitz 1992 | Inherited from comp-033 provenance |
| Anakinra steady-state Cmax = 87 nM, Cmin = 2.9 nM | derived from the above | conversion via MW 17.3 kDa | Computed in `il1ra_receptor_binding.json`; arithmetic: 1500 ng/mL / 17300 g/mol = 8.67e-8 M = 86.7 nM. ✓ |
| Anakinra steady-state mean receptor occupancy (at Kd=1 nM) | 85-90% | derived | Computed in `il1ra_receptor_binding.json`. At Cmax 87 nM: 87/(87+1)=98.9%. At Cmin 2.9 nM: 2.9/(2.9+1)=74.4%. Mean across cycle ~85-90%. ✓ |
| Translation efficiency mass ratio 1,000-50,000 ng/ug | log-uniform prior | Pardi 2018 Nat Rev Drug Discov; Ogata 2022 CID; comp-033 corrected prior | Inherited; remains dominant sensitivity driver |
| Lung delivery fraction 10-40% | uniform prior | Geller 2009 Respir Care; PARI eFlow specs | Inherited |
| Alveolar -> systemic bioavailability 10-50% | uniform prior | Patton & Byron 2007 | Inherited |
| Expression duration 24-96 hours | uniform prior | CF inhaled mRNA-LNP preclinical compilation | Inherited |

## New parameters introduced in comp-036

| Claim | Value | Source | Verification |
|---|---|---|---|
| IL-1Ra-IL-1R1 Kd prior 0.1-10 nM (log-uniform, central 1 nM) | log-uniform prior | Arend 1990 (qualitative "affinity nearly equal to IL-1"); Schreuder 1997 (crystal structure tier); compilation of IL-1 family Kd literature | Order-of-magnitude verified at primary-paper tier. The wide log-uniform 0.1-10 nM prior honestly reflects that the literature does not converge on a single precise Kd number. Sensitivity analysis confirms Kd is the **#1 driver of mean occupancy** (Spearman rho = -0.69), justifying the wide prior. |
| Competitive antagonism excess factor 10-100x (log-uniform, central 30x) | log-uniform prior | Arend 1990 JCI explicit "10-100x excess for 50% inhibition" statement | Verified directly. Used in supplementary biological-inhibition-percent calculation; in the main analysis (raw receptor occupancy), this factor is implicit in the choice of 80% occupancy threshold (which corresponds to ~80% inhibition at moderate excess factors). |
| IL-1R1 receptor density 50-5000 per cell | range | Sims & Smith 2010 Annu Rev Immunol review; multiple 1989-2000 Scatchard analyses | Not directly used in receptor-occupancy fraction calculation (occupancy is concentration-dependent, not count-dependent for competitive antagonism). Listed for biological context. |
| Acute gout flare peak window 0-72h | clinical phenomenology | Saag 2021 RCT design; standard gout-flare natural-history literature | Verified via clinical-trial design (Saag 2021 measured primary endpoint at 24-72h post-baseline). |

## Multilingual sources checked (per CLAUDE.md)

| Source | Search performed | Result |
|---|---|---|
| CNKI | "白介素-1 受体拮抗剂 痛风" (IL-1 receptor antagonist gout); "重复给药 雾化吸入 mRNA" (repeated-dose nebulized inhaled mRNA) | No Chinese-language inhaled-mRNA-IL-1Ra repeat-dose programs identified. Anakinra-in-gout literature in Chinese mirrors Western off-label use. No new quantitative anchor surfaced. |
| J-STAGE | "IL-1受容体拮抗薬 反復投与" (IL-1 receptor antagonist repeat dosing); "吸入 mRNA 反復" (inhaled mRNA repeat) | Japanese Kampo gout literature is herbal/small-molecule; Daiichi-Sankyo-Moderna inhaled-mRNA work proceeds but no IL-1Ra-specific program disclosed. No new anchor. |

## Items flagged for follow-up verification

1. **IL-1Ra-IL-1R1 Kd numerical value.** The literature consensus is "nM regime, affinity ~equal to IL-1." A direct, modern SPR Kd measurement on recombinant IL-1Ra vs IL-1R1 ectodomain at physiological pH/salt would tighten this prior considerably. Sensitivity analysis shows this is the #1 driver of mean occupancy in repeat-dose modeling.

2. **Translation efficiency mass ratio in human alveolar epithelium.** Same #2 driver as in comp-033 (rho = +0.58 in comp-036). A direct measurement in ferret or NHP single-dose inhaled-mRNA-LNP study (with downstream protein quantification in BAL fluid and lung tissue) would resolve this.

3. **In vivo receptor occupancy is computed from plasma free IL-1Ra concentration assuming equilibrium binding and no IL-1R1 internalization on the hour timescale.** This is reasonable for circulating cells per Sims & Smith 2010, but at the joint synovium during a flare, receptor internalization dynamics may differ. The model holds for the systemic-circulation efficacy mechanism (which is what anakinra clinical efficacy operates through).

## Verification rule

Every input file in this directory has been audited against this provenance table. All load-bearing numbers used in the model are either (a) verified directly against primary source (top of file), (b) inherited from comp-033 (which has its own provenance table), or (c) used as wide priors in the Monte Carlo with explicit anchors to honestly reflect uncertainty.

## comp-036 reframe note (load-bearing methodological correction)

The comp-036 brief speculated IL-1Ra-IL-1R1 KD ~50-100 pM. **This was incorrect.** The canonical Arend 1990 JCI characterization places IL-1Ra at "affinity nearly equal to IL-1" — and IL-1 family Kd to IL-1R1 is in the **0.1-10 nM range**, not pM. The Schreuder 1997 Nature crystal structure (PMID 9062194) and Vigers 1997 Nature companion structure (PMID 9062193) confirm the binding mode but do not push Kd below ~100 pM. Used the corrected 0.1-10 nM log-uniform prior throughout comp-036.

The clinical implication of this correction: at the (correct) nM Kd, anakinra steady-state plasma (Cmin 50 ng/mL = 2.9 nM, Cmax 1500 ng/mL = 87 nM) operates at 74-99% receptor occupancy across the dosing cycle — consistent with the Saag 2021 Phase II RCT efficacy. Inhaled mRNA-IL-1Ra at the comp-033-projected single-dose Cmax (25 ng/mL = 1.4 nM) is BELOW the 80%-occupancy threshold (which is ~4x Kd = ~4 nM at central Kd=1 nM, equating to ~70 ng/mL plasma). This is exactly why repeat-dosing is needed and why the verdict lands YELLOW rather than GREEN.
