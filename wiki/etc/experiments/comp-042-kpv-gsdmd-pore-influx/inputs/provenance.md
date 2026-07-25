# comp-042 — Input Provenance

Per CLAUDE.md Rule 4 (pre-commit grep-verify gate). Every load-bearing input is traced to a primary/authoritative source, or explicitly flagged as a NAMED ASSUMPTION with its basis. Scope is biophysics/pharmacology — natural-product / TCM query matrix does not apply (`inputs/query-strategy.json`, `natural_product_scope: false`).

According to PubMed, the primary sources below carry the load-bearing values.

---

## KPV physical properties

| Quantity | Value | Source | Status |
|---|---|---|---|
| Molecular weight | 342.43 Da (C16H30N4O4) | Computed from Lys(146.19)+Pro(115.13)+Val(117.15) − 2×H2O(36.03). Consistent with PubChem KPV entry. | **VERIFIED** (arithmetic; task brief states ~342 Da). |
| Net charge at pH 7.4 | +1 (monovalent cation) | N-terminal α-amine (+1) + Lys ε-amine (+1) + C-terminal carboxylate (−1). | **VERIFIED** (standard pKa). Xia 2021 supports favorable conduit electrostatics for cationic cargo in the studied system, but this does not quantify a KPV-specific effective hindrance or partition factor. |
| Hydrodynamic radius | 0.45–0.60 nm, central 0.50 | Stokes-Einstein back-calc + empirical small-peptide radii. | **[ESTIMATED]**. Crossed with the 5.0–10.75 nm pore-radius band, λ = r_solute/r_pore is approximately 0.04–0.12 and `(1−λ)²` approximately 0.77–0.92; this motivates the declared hindrance sensitivity rather than a no-hindrance claim. |
| Aqueous diffusion coefficient | 4–6 × 10⁻¹⁰ m²/s (5×10⁻⁶ cm²/s central) | Stokes-Einstein: D = kT/(6πη r_h); at 37 °C, η=0.69 mPa·s, r_h=0.5 nm → 6.6×10⁻¹⁰; at 25 °C → 4.5×10⁻¹⁰. Standard order for ~340 Da solute. | **[ESTIMATED — STOKES-EINSTEIN]**. Low sensitivity: p_pore and access resistance both scale with D, so τ_eq scales uniformly as 1/D. |
| Pore hindrance factor, H | 0.5–1.0 (central 1.0) | Conservative engineering band applied to neutral diffusive permeability. It does not credit possible favorable electrostatic partition. | **[NAMED ENGINEERING SENSITIVITY]**. No direct KPV-through-GSDMD permeability measurement exists. |
| Intracellular degradation | Uncharacterized | The corpus contains an extracellular/serum-stability statement, but no source here establishes intracellular KPV retention or degradation in the relevant cells. | **NAMED GAP; not modeled.** No extracellular-to-intracellular stability transfer is claimed. |

## GSDMD pore geometry

| Quantity | Value | Source | Status |
|---|---|---|---|
| Inner diameter | 10–21.5 nm (central 20) | Sborgi et al. *EMBO J* 2016 (PMID 27418190, DOI 10.15252/embj.201694696) — AFM ring diameters **21.2 ± 5.6 nm (n=164)**; Xia et al. *Nature* 2021 (PMID 33883744, DOI 10.1038/s41586-021-03478-3) — cryo-EM **33-subunit** pore, inner diameter **~215 Å = 21.5 nm**. Our corpus `gsdmd-pore-delivery-paradox.md` line 40 states 10–20 nm. | **VERIFIED** (two independent structural methods + corpus). |
| Conduit electrostatics | Negatively charged; favors cationic/neutral cargo | Xia 2021 (PMID 33883744) — pore conduit "predominantly negatively charged"; liposomes release positively-charged/neutral cargo faster than negative; passes mature IL-1β over acidic pro-IL-1β (electrostatic filtering). | **VERIFIED** for the studied cargo comparisons. It does not provide a KPV-specific permeability multiplier; the model therefore tests H=0.5–1.0 and does not credit enhancement above 1. |
| Channel length | 4–10 nm (central 7) | Bilayer ~4–5 nm + β-barrel protrusion. | **[ESTIMATED]** — low sensitivity (access resistance dominates). |
| Pores per pyroptotic cell | 10–10⁴ (central 200) | **NAMED ASSUMPTION.** Full-text check of Sborgi 2016 (PMC5010048) and Xia 2021 confirms NEITHER reports a per-cell pore count — they characterize pore structure, not cellular abundance. | **[NAMED ASSUMPTION — DESIGN SPACE]**. The deterministic robustness grid reports exposure-proxy outcomes without assigning plausibility to a pore-count value. |
| Open lifetime | 60–1800 s (1–30 min) | Our corpus `gsdmd-pore-delivery-paradox.md` Open Question #4: "minutes to tens of minutes" before ESCRT repair or lysis. | **[CORPUS OPEN QUESTION]**. Tested jointly with pore count; the run reports equilibration fraction and exposure-proxy state for every declared grid cell. |

## PepT1 (SLC15A1) kinetics + expression

According to PubMed:

| Quantity | Value | Source | Status |
|---|---|---|---|
| Km, KPV via hPepT1 (epithelial) | ~160 µM | Dalmasso et al. *Gastroenterology* 2008 (PMID 18061177, DOI 10.1053/j.gastro.2007.10.026), Fig 4C, Caco2-BBE, [³H]KPV kinetics. | **VERIFIED via PMC full-text fetch** (PMC2431115). |
| Km, KPV via hPepT1 (immune) | ~700 µM | Same, Fig 5F, Jurkat T cells. Model uses immune Km (700 µM) as central; sensitivity 160–1000. | **VERIFIED via PMC full-text fetch**. |
| PepT1 in immune cells | Functionally present | Dalmasso 2008: "KPV acts via hPepT1 expressed in immune and intestinal epithelial cells"; Viennois 2016 (PMID 27458604, DOI 10.1016/j.jcmgh.2016.01.006); KPV-nanoparticle colitis work targets inflamed-tissue macrophages via PepT1 (PMID 39211778 DOI 10.3389/fphar.2024.1442876; PMID 31408067 DOI 10.1039/c9bm00925f). | **VERIFIED qualitatively**. |
| **PepT1 in SYNOVIAL macrophages** | **UNCHARACTERIZED** | No study quantifies SLC15A1 expression/function in resting or MSU-activated synovial-joint macrophages. | **[NAMED GAP — HEADLINE LIMITATION]**. Dominant empirical gap in A2. Modeled via 4 unweighted AR_lin scenarios (0 / 0.3 / 1 / 3); the heuristic ratio also varies with C_ext/Km. |
| KPV NF-κB extracellular effective-concentration proxy | 1–100 nM design-space band, central 10 | Dalmasso 2008: "Nanomolar concentrations of KPV inhibit the activation of NF-κB"; lowest tested effective concentration = **10 nM** (Caco2-BBE NF-κB luciferase + IL-1β). | **VERIFIED via PMC full-text fetch**. This is not an intracellular concentration or fitted IC50. It is a cross-compartment engineering proxy and cannot establish target engagement, timing, or efficacy. |

## Macrophage geometry

| Quantity | Value | Source | Status |
|---|---|---|---|
| Cell volume | 1000–5000 µm³ (central 3000) | Sphere of 15–21 µm diameter (activated macrophage). 18 µm → 3050 µm³. | **[STANDARD CELL BIOLOGY]**. Sets intracellular-concentration denominator and τ_eq numerator. |
| Surface area | 700–4000 µm² | Geometric SA (18 µm sphere ≈ 1018 µm²) with ruffling ×2–4. | **[STANDARD]** — not directly load-bearing (model uses explicit pore count, not density×area). |

## Route concentrations

| Route | Synovial [KPV] | Source | Status |
|---|---|---|---|
| Intra-articular | 15–1460 µM (central 292) | Arithmetic from assumed 0.1–1 mg doses and assumed 2–20 mL synovial compartments; central 0.2 mg/2 mL. | **[NAMED DESIGN ASSUMPTIONS]**. The arithmetic is checked, but the dose and volume anchors are not source-qualified here and are not clinical-exposure claims. |
| Subcutaneous | 3–200 nM (central 30) | **NAMED PK ASSUMPTION**: 0.5 mg SC, BA>80% (`kpv-peptide.md`), Vd~15 L → ~0.1 µM plasma; synovial:plasma partition 0.3–0.5; short t½. | **[DESIGN-SPACE PK]**. Central value is ~3× the exposure proxy; this is an engineering margin, not an efficacy prediction. |
| Oral | 0.1–3 nM (central 1) | **NAMED PK ASSUMPTION**: oral BA optimized for local gut PepT1; systemic 10–100× below SC. | **[DESIGN-SPACE PK]**. Central value is below the exposure proxy. |

---

## Compounding-optimistic-assumption check (Rule 4 "provisional" trigger)

The favorable read ("KPV self-delivers and is selective") rests on ≥ 3 compounding optimistic assumptions:
1. **Pores/cell and pore lifetime** jointly determine the modeled passive pore contribution (NAMED ASSUMPTION; not measured per-cell).
2. **SC/oral synovial PK** reaches the extracellular cell-assay exposure proxy (DESIGN-SPACE assumption; KPV systemic PK poorly characterized).
3. **PepT1 absent/low in synovial macrophages** so the heuristic ratio favors the pore (NAMED GAP; PepT1-mediated uptake in Jurkat cells does not determine the synovial-macrophage scenario).

Because these assumptions compound toward a favorable transport/selectivity interpretation, the overall machine verdict is capped below GREEN while A2 is unresolved. Per-cell pore counts and KPV synovial PK would narrow A1; a matched synovial-macrophage PepT1/healthy-cell accumulation measurement is required to resolve A2.

## Multilingual scan

Per CLAUDE.md §"Global-multilingual research by default": the GSDMD-pore and KPV/PepT1 primary literature is English-language international-journal work. Several contributing groups are China-based (e.g., Shi/Shao NIBS Beijing for gasdermin biology; the KPV-nanoparticle colitis groups at Georgia State / Southwest Medical University / Huazhong) but publish in English; no non-English source was found to carry a divergent load-bearing value. No translation cross-check required (no non-English source produced a load-bearing claim). This is a structural-biology/pharmacology scope, not a traditional-medicine scope.

## Verification-agent pass

| Claim | Source | Method | Result |
|---|---|---|---|
| GSDMD pore inner diameter ~20–21.5 nm | Sborgi 2016 / Xia 2021 | PMC full-text + metadata | ✅ 21.2±5.6 nm AFM; 21.5 nm cryo-EM |
| Pore conduit negatively charged, favors cations | Xia 2021 | abstract + PMC | ✅ |
| No per-cell pore count published | Sborgi 2016, Xia 2021 | PMC full-text check | ✅ confirmed absent → NAMED ASSUMPTION |
| KPV NF-κB effective at 10 nM | Dalmasso 2008 | PMC2431115 full-text | ✅ |
| PepT1 Km(KPV) 160 µM epithelial / 700 µM immune | Dalmasso 2008 | PMC2431115 full-text (Fig 4C/5F) | ✅ |
| PepT1 functional in immune cells | Dalmasso 2008 | abstract + full-text | ✅ (Jurkat) |
| Synovial-macrophage PepT1 uncharacterized | literature | PubMed searches returned no synovial-macrophage SLC15A1 quantification | ✅ confirmed gap |
| KPV MW 342.43, net +1 | sequence | arithmetic | ✅ |

**Pre-commit grep-verify gate status: PASSED.** Structural, kinetic, and cell-assay anchors were verified to the named primary sources. Pores/cell, the hindrance band, SC/oral synovial PK, and synovial-macrophage PepT1 remain explicit assumptions or gaps.
