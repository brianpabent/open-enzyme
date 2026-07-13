# comp-042 — Input Provenance

Per CLAUDE.md Rule 4 (pre-commit grep-verify gate). Every load-bearing input is traced to a primary/authoritative source, or explicitly flagged as a NAMED ASSUMPTION with its basis. Scope is biophysics/pharmacology — natural-product / TCM query matrix does not apply (`inputs/query-strategy.json`, `natural_product_scope: false`).

According to PubMed, the primary sources below carry the load-bearing values.

---

## KPV physical properties

| Quantity | Value | Source | Status |
|---|---|---|---|
| Molecular weight | 342.43 Da (C16H30N4O4) | Computed from Lys(146.19)+Pro(115.13)+Val(117.15) − 2×H2O(36.03). Consistent with PubChem KPV entry. | **VERIFIED** (arithmetic; task brief states ~342 Da). |
| Net charge at pH 7.4 | +1 (monovalent cation) | N-terminal α-amine (+1) + Lys ε-amine (+1) + C-terminal carboxylate (−1). | **VERIFIED** (standard pKa). Load-bearing: the GSDMD conduit favors cationic cargo (Xia 2021), so KPV's +1 makes hindrance ≥ 1. |
| Hydrodynamic radius | 0.45–0.60 nm, central 0.50 | Stokes-Einstein back-calc + empirical small-peptide radii. | **[ESTIMATED]**. λ = r_solute/r_pore ≈ 0.05 → steric hindrance ≈ 1 (solute 20–40× smaller than pore radius). |
| Aqueous diffusion coefficient | 4–6 × 10⁻¹⁰ m²/s (5×10⁻⁶ cm²/s central) | Stokes-Einstein: D = kT/(6πη r_h); at 37 °C, η=0.69 mPa·s, r_h=0.5 nm → 6.6×10⁻¹⁰; at 25 °C → 4.5×10⁻¹⁰. Standard order for ~340 Da solute. | **[ESTIMATED — STOKES-EINSTEIN]**. Low sensitivity: p_pore and access resistance both scale with D, so τ_eq scales uniformly as 1/D. |
| Enzymatic resistance | Qualitative | Our corpus `kpv-peptide.md` line 98: KPV "resistant to significant enzymatic degradation." | **LOAD-BEARING, DIRECTION-FLIPPED**: this is an extracellular/serum-stability claim. If it also holds intracellularly, a PepT1+ healthy cell *retains* KPV → higher healthy baseline → *less* pore selectivity. Intracellular peptidase susceptibility not separately characterized. |

## GSDMD pore geometry

| Quantity | Value | Source | Status |
|---|---|---|---|
| Inner diameter | 10–21.5 nm (central 20) | Sborgi et al. *EMBO J* 2016 (PMID 27418190, DOI 10.15252/embj.201694696) — AFM ring diameters **21.2 ± 5.6 nm (n=164)**; Xia et al. *Nature* 2021 (PMID 33883744, DOI 10.1038/s41586-021-03478-3) — cryo-EM **33-subunit** pore, inner diameter **~215 Å = 21.5 nm**. Our corpus `gsdmd-pore-delivery-paradox.md` line 40 states 10–20 nm. | **VERIFIED** (two independent structural methods + corpus). |
| Conduit electrostatics | Negatively charged; favors cationic/neutral cargo | Xia 2021 (PMID 33883744) — pore conduit "predominantly negatively charged"; liposomes release positively-charged/neutral cargo faster than negative; passes mature IL-1β over acidic pro-IL-1β (electrostatic filtering). | **VERIFIED**. Supports hindrance ≥ 1 for KPV (+1). |
| Channel length | 4–10 nm (central 7) | Bilayer ~4–5 nm + β-barrel protrusion. | **[ESTIMATED]** — low sensitivity (access resistance dominates). |
| Pores per pyroptotic cell | 10–10⁴ (central 200) | **NAMED ASSUMPTION.** Full-text check of Sborgi 2016 (PMC5010048) and Xia 2021 confirms NEITHER reports a per-cell pore count — they characterize pore structure, not cellular abundance. | **[NAMED ASSUMPTION — DESIGN SPACE]**. Robustness sweep shows the A1 verdict is stable for ≥ ~10 pores/cell, so this poorly-constrained value does not drive the flux verdict. |
| Open lifetime | 60–1800 s (1–30 min) | Our corpus `gsdmd-pore-delivery-paradox.md` Open Question #4: "minutes to tens of minutes" before ESCRT repair or lysis. | **[CORPUS OPEN QUESTION]**. comp-042 quantitatively answers it: equilibration is complete within seconds, so even the short-lifetime end suffices. |

## PepT1 (SLC15A1) kinetics + expression

According to PubMed:

| Quantity | Value | Source | Status |
|---|---|---|---|
| Km, KPV via hPepT1 (epithelial) | ~160 µM | Dalmasso et al. *Gastroenterology* 2008 (PMID 18061177, DOI 10.1053/j.gastro.2007.10.026), Fig 4C, Caco2-BBE, [³H]KPV kinetics. | **VERIFIED via PMC full-text fetch** (PMC2431115). |
| Km, KPV via hPepT1 (immune) | ~700 µM | Same, Fig 5F, Jurkat T cells. Model uses immune Km (700 µM) as central; sensitivity 160–1000. | **VERIFIED via PMC full-text fetch**. |
| PepT1 in immune cells | Functionally present | Dalmasso 2008: "KPV acts via hPepT1 expressed in immune and intestinal epithelial cells"; Viennois 2016 (PMID 27458604, DOI 10.1016/j.jcmgh.2016.01.006); KPV-nanoparticle colitis work targets inflamed-tissue macrophages via PepT1 (PMID 39211778 DOI 10.3389/fphar.2024.1442876; PMID 31408067 DOI 10.1039/c9bm00925f). | **VERIFIED qualitatively**. |
| **PepT1 in SYNOVIAL macrophages** | **UNCHARACTERIZED** | No study quantifies SLC15A1 expression/function in resting or MSU-activated synovial-joint macrophages. | **[NAMED GAP — HEADLINE LIMITATION]**. Sole determinant of A2 selectivity. Modeled via 4 AR_lin scenarios (0 / 0.3 / 1 / 3). |
| KPV NF-κB effective concentration (IC50 proxy) | 1–100 nM, central 10 | Dalmasso 2008: "Nanomolar concentrations of KPV inhibit the activation of NF-κB"; lowest effective = **10 nM** (Caco2-BBE NF-κB luciferase + IL-1β). | **VERIFIED via PMC full-text fetch**. Conservative proxy (extracellular effective conc in a PepT1+ cell already convolves transport + potency). |

## Macrophage geometry

| Quantity | Value | Source | Status |
|---|---|---|---|
| Cell volume | 1000–5000 µm³ (central 3000) | Sphere of 15–21 µm diameter (activated macrophage). 18 µm → 3050 µm³. | **[STANDARD CELL BIOLOGY]**. Sets intracellular-concentration denominator and τ_eq numerator. |
| Surface area | 700–4000 µm² | Geometric SA (18 µm sphere ≈ 1018 µm²) with ruffling ×2–4. | **[STANDARD]** — not directly load-bearing (model uses explicit pore count, not density×area). |

## Route concentrations

| Route | Synovial [KPV] | Source | Status |
|---|---|---|---|
| Intra-articular | 15–1460 µM (central 292) | Computed: dose (0.1–1 mg) / synovial volume (2–20 mL). 0.2 mg/2 mL = 292 µM. | **COMPUTED** from dose + anatomy. >> IC50 and near/above PepT1 Km → PepT1 saturates in healthy cells too. |
| Subcutaneous | 3–200 nM (central 30) | **NAMED PK ASSUMPTION**: 0.5 mg SC, BA>80% (`kpv-peptide.md`), Vd~15 L → ~0.1 µM plasma; synovial:plasma partition 0.3–0.5; short t½. | **[DESIGN-SPACE PK]**. Only ~3× IC50 — thin margin. |
| Oral | 0.1–3 nM (central 1) | **NAMED PK ASSUMPTION**: oral BA optimized for local gut PepT1; systemic 10–100× below SC. | **[DESIGN-SPACE PK]**. Below IC50 for joint delivery. |

---

## Compounding-optimistic-assumption check (Rule 4 "provisional" trigger)

The favorable read ("KPV self-delivers and is selective") rests on ≥ 3 compounding optimistic assumptions:
1. **Pores/cell ≥ ~10** so the cell equilibrates within the lifetime (NAMED ASSUMPTION; not measured per-cell).
2. **SC/oral synovial PK** reaches ≥ IC50 (DESIGN-SPACE assumption; KPV systemic PK poorly characterized).
3. **PepT1 absent/low in synovial macrophages** so the pore confers selectivity (NAMED GAP; functional immune-cell PepT1 is actually *demonstrated*, making this the least likely scenario).

Because ≥ 3 optimistic assumptions compound toward "it works and it's selective," the verdict is labeled **YELLOW (provisional)** and the three assumptions are named. Removing "provisional" requires: a per-cell pore count, a KPV synovial-PK measurement, and — decisively — a synovial-macrophage PepT1 expression measurement.

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

**Pre-commit grep-verify gate status: PASSED.** Structural, kinetic, and potency anchors verified to primary sources. Named assumptions (pores/cell, SC/oral synovial PK, synovial-macrophage PepT1) explicitly flagged; ≥3 compound optimistically → verdict labeled **provisional**.
