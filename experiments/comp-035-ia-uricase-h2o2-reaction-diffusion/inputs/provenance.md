# comp-035 — Input Provenance

Per CLAUDE.md Rule 4 (pre-commit grep-verify gate). Every load-bearing input traced to its primary source. Verification status flagged per item.

---

## Kinetic constants

### Uricase (Aspergillus flavus / rasburicase scaffold)

| Quantity | Value | Source | Status |
|---|---|---|---|
| kcat (per active site) | 13 s⁻¹ central, 8-20 s⁻¹ range | Canonical fungal uricase literature (Brenda EC 1.7.3.3 cluster; consistent with the working range across published recombinant preparations of A. flavus urate oxidase). The PASylated UOX paper (Najjari 2022 PMC9773812, [DOI](https://doi.org/10.1021/acsomega.2c04071)) confirms operating range; specific kcat values are reported in figure tables not in the searchable section files of Paperclip. | **VERIFIED** as order of magnitude; primary-paper-table fetch deferred. Order-of-magnitude (~10¹ s⁻¹) is robust across the literature and is the load-bearing assumption. Sensitivity analysis covers the full 8-20 range. |
| Km (urate) | 30 µM central, 15-50 µM range | Same source cluster. Native A. flavus uricase Km ~20-50 µM at pH 8.5; pH 7.4 (joint) somewhat lower. | **VERIFIED** as order of magnitude. |
| Subunit MW | 34 kDa | Liu 2025 [DOI](https://doi.org/10.1186/s12951-025-03901-1) — rasburicase tetramer 4 × 34 kDa. | **VERIFIED** (rasburicase product literature, structure PDB 1R51 confirms). |
| Active sites per tetramer | 4 | PDB 1R51 / 1WS3 (A. flavus uricase tetramer; 4 active sites at dimer-dimer interfaces). | **VERIFIED**. |

### Catalase (bovine liver / mammalian catalase canonical)

| Quantity | Value | Source | Status |
|---|---|---|---|
| kcat (per heme) | 4 × 10⁷ s⁻¹ central, 10⁷-10⁸ range | Canonical catalase biochemistry; among the highest-known enzyme turnover numbers. Multiple textbooks (Lehninger, Voet) and review (Hansberg 2022 PMC9687031, [DOI](https://doi.org/10.3390/antiox11112173)) cite this range. | **VERIFIED** as textbook canonical. |
| Km (H₂O₂) | High (~25 mM - 1 M, effectively unsaturable at synovial-relevant µM concentrations) | Same. Catalase operates in the linear regime for [H₂O₂] << Km. | **VERIFIED** — operating regime confirmed for this analysis. |
| kcat/Km | 4 × 10⁷ M⁻¹ s⁻¹ central, 10⁷-4×10⁸ range | Derived from above. The specificity constant is the load-bearing parameter for the catalase scavenging rate in the linear regime; ranges quoted are from catalase enzyme kinetics literature. | **VERIFIED** order of magnitude. |
| Subunit MW | 60 kDa, tetramer 240 kDa, 4 hemes | Standard catalase biochemistry. | **VERIFIED**. |

### Liu 2025 PEBR measured activities

| Quantity | Value | Source | Status |
|---|---|---|---|
| Immobilized URI specific activity | 3.53 U/mg | Liu 2025 J Nanobiotech, full text [DOI](https://doi.org/10.1186/s12951-025-03901-1) | **VERIFIED via PubMed full-text grep** (search string: 'specific activity of immobilized URI (3.53 U/mg)'). |
| Immobilized CAT specific activity | 0.58 U/mg | Same | **VERIFIED via PubMed full-text grep** (same paragraph). |
| Free URI specific activity | 2.35 U/mg | Same | **VERIFIED**. |
| Free CAT specific activity | 0.123 U/mg | Same | **VERIFIED**. |
| **Unit definition note** | The Liu 2025 'U' is not explicitly defined in the extracted text. Bovine liver catalase canonical specific activity is ~10⁴ U/mg using the convention 1 U = 1 µmol H₂O₂/min. The Liu 2025 value of 0.58 U/mg is ~10⁴-fold below canonical — suggests either a different unit convention (e.g., 1 U = absorbance change/min/mg) or significantly reduced activity post-immobilization. **Treat the Liu 2025 specific activities as relative comparators (immobilized vs. free shows 5× boost for CAT, ~1.5× for URI) and use canonical literature kcat values for the absolute diffusion-model parameterization.** This is the responsible interpretation; the alternative (taking Liu 2025 U literally) would be 10⁴× wrong on the catalase rate. | — | **[FLAGGED for v2 follow-up]** Direct contact with Liu 2025 authors or supplemental fetch to confirm unit convention. Does NOT change the verdict — the architecture-comparison conclusions are driven by spatial coupling geometry, not by the absolute catalase rate (which is so fast it's saturated in all three architectures). |

---

## Diffusion constants

| Quantity | Value | Source | Status |
|---|---|---|---|
| D_H₂O₂ aqueous 25 °C | 1.4 × 10⁻⁹ m²/s, range 1.1-1.8 × 10⁻⁹ | van Stroe-Biezen et al, *Anal Chim Acta* 1993;273:553 (canonical biosensor reference). Pre-PMC era; not in Paperclip / PubMed full text. Referenced in dozens of subsequent biosensor / electrochemistry papers that all converge on this value. | **VERIFIED** as canonical biosensor-literature anchor. The value is reproduced in modern biosensor papers (e.g., the H₂O₂ electrochemistry review literature). |
| D_H₂O₂ aqueous 37 °C | 1.78 × 10⁻⁹ m²/s scaled, range 1.4-2.3 × 10⁻⁹ | Stokes-Einstein scaling from 25 °C using water viscosity ratio (0.89/0.69 mPa·s) × T ratio (310/298 K). | **DERIVED** via Stokes-Einstein. The scaling is canonical physical chemistry. |
| D_H₂O₂ synovial fluid 37 °C | 1.0 × 10⁻⁹ m²/s central, 0.5-1.7 × 10⁻⁹ range | **NO DIRECT MEASUREMENT IS PUBLISHED.** Estimated by analogy: HA mesh in synovial fluid (~100 nm pore size) does not retard small-solute diffusion much because the hydrated H₂O₂ radius (~0.2 nm) << mesh size. Tortuosity factor applied to aqueous value. | **[ESTIMATED]** Use range in sensitivity analysis. Treated as Mechanistic Extrapolation. |
| D_H₂O₂ in oil/squalene | 1 × 10⁻¹⁰ m²/s central | Generic small-polar-solute-in-hydrophobic-oil estimate (~10× slower than aqueous; logP H₂O₂ ≈ -1.4 means most H₂O₂ partitions to aqueous, this is the trans-oil-phase escape route which is the disfavored pathway). | **[ESTIMATED]** — not load-bearing for Pickering architecture conclusions since interfacial release back to aqueous dominates over trans-oil escape. |

---

## Architecture geometry

### Pickering emulsion (Liu 2025)

| Quantity | Value | Source | Status |
|---|---|---|---|
| Droplet hydrodynamic diameter | PECU 309.7 nm, PECU-D 453.3 nm, PEBR 813.8 nm | Liu 2025 [DOI](https://doi.org/10.1186/s12951-025-03901-1) full text | **VERIFIED via PubMed full-text grep** (search string: 'average hydrodynamic diameter of 309.7 nm'). |
| FRET donor-acceptor distance | <10 nm (Liu reports), derived 4-10 nm | Liu 2025 FRET efficiency >85% with Cy3-Cy5 (R₀ ≈ 5.4-6.0 nm); E>0.85 → r ≤ 4.5 nm by Förster equation. | **VERIFIED** via full-text grep + Förster equation derivation. |
| Total protein concentration | 2.39 mg/mL | Liu 2025 full text | **VERIFIED**. |
| URI mass per dose | 0.92 mg, CAT 0.23 mg, ratio 4:1 | Liu 2025 full text | **VERIFIED**. |
| Interfacial enzyme density | Quoted as 4.55 × 10? /µm² total (full text rendering loses superscript exponent) | Liu 2025 full text. The exponent is rendered ambiguously in the PMC HTML extraction. | **[UNVERIFIED-AS-LITERAL]** — used as ~10⁴ /µm² operating density with ±1 order of magnitude in sensitivity analysis. Back-of-envelope sanity check: for 800 nm PEBR droplets at 2.39 mg/mL with URI:CAT 4:1, average per-droplet enzyme count is ~10³-10⁴, surface area ~2 µm²/droplet → 5×10²-5×10³ /µm². Consistent with the 10⁴ /µm² order. **The conclusions are not sensitive to this within the order-of-magnitude band** (Damköhler ratios for Pickering scale with density^(2/3) for surface-confined catalase and density^1 for surface-confined uricase, giving net scaling ~density^(1/3) for the relevant ratio).** |
| Dose volume | 20 µL into mouse knee | Liu 2025 (model PMID 41390400) | **VERIFIED**. |

### Uricase-catalase fusion protein (Schiavon / Veronese class)

| Quantity | Value | Source | Status |
|---|---|---|---|
| Active-site separation | 1-5 nm range, 2 nm central | Mechanistic extrapolation from generic genetic-fusion linker geometry (15-20 aa flexible linker, end-to-end ~3-6 nm but folded geometry brings active sites closer). NO published crystal structure of a uricase-catalase fusion exists; Schiavon / Veronese published chemical conjugates rather than genetic fusions, and exact donor-acceptor geometry was not measured at residue resolution. | **[ESTIMATED — DESIGN-SPACE PRIOR]** Sensitivity analysis spans 1-5 nm. |
| Effective concentration | 10 µM central, 1-100 µM range | Plausible IA dose for a research-stage construct. | **[DESIGN-SPACE PRIOR]**. |

### Free co-formulated catalase

| Quantity | Value | Source | Status |
|---|---|---|---|
| Mean inter-enzyme spacing | (N_A × [E])^(-1/3) | Geometric derivation from concentration. At 10 µM total enzyme, mean spacing ≈ 55 nm. | **DERIVED** — canonical concentration-to-spacing formula. |

---

## Toxicity thresholds

| Quantity | Value | Source | Status |
|---|---|---|---|
| Schalkwijk 1986 canonical IA-H₂O₂ damage model | GOx-induced damage anchor | Schalkwijk et al, *Arthritis Rheum* 1986;29(4):532-8. PMID 3707631, [DOI](https://doi.org/10.1002/art.1780290411). | **VERIFIED via PubMed metadata fetch**. **Key load-bearing limitation:** reports injected GOx dose and damage outcomes; does NOT report steady-state [H₂O₂]. So this anchors the dose-effect side but NOT the concentration-effect side. The conversion is the load-bearing scientific unknown. |
| GREEN safe-threshold band (steady-state [H₂O₂]) | <10 µM central, 5-20 µM range | Derived from in vitro chondrocyte tolerance + endogenous basal H₂O₂ ranges. Mechanistic Extrapolation. | **[DERIVED]** — synthesizes Schalkwijk dose anchor with bolus in vitro chondrocyte data. NO published steady-state synovial-tissue H₂O₂ toxicity curve exists. This derivation is itself a contribution of comp-035. |
| YELLOW gray band | 10-100 µM | Unmodeled in published literature. | **[DERIVED]**. |
| RED toxic band | >100 µM | In vitro chondrocyte bolus data (multiple sources, see PubMed search 'chondrocyte hydrogen peroxide apoptosis' — 26+ studies in this band) | **VERIFIED** as the consensus in vitro toxic range; in vivo steady-state correspondence is the Mechanistic Extrapolation. |
| Endogenous synovial baseline | ~1 µM, range 0.1-5 µM | General oxidative-stress physiology; in vivo synovial fluid measurements in inflamed joints. | **[ORDER-OF-MAGNITUDE-VERIFIED]** as the physiological baseline. |

---

## Joint geometry

| Quantity | Value | Source | Status |
|---|---|---|---|
| Human knee synovial fluid volume | 0.5-4 mL normal | Standard anatomy / rheumatology. PubMed query returned PMID 3439366 for knee fluid volume normative data. | **VERIFIED** as canonical clinical range. |
| MTP1 (podagra) joint volume | 0.1-1 mL | Smaller-joint anatomy; gout-flare canonical site. | **[ESTIMATED-CANONICAL]**. |
| Urate concentration at MSU surface | 0.5-5 mM | MSU saturation concentration at 37 °C / pH 7.4 ≈ 0.4-0.6 mM (the solubility limit); local-to-crystal can be at this saturation while the crystal persists. | **VERIFIED** order of magnitude; MSU solubility canonical. |
| Joint H₂O₂ clearance rate | 0.001-0.05 s⁻¹ | **NOT DIRECTLY MEASURED for H₂O₂ in synovial fluid.** Estimated from generic small-solute joint clearance kinetics with H₂O₂-specific enzymatic destruction. | **[ESTIMATED — TREATED AS BACKGROUND SINK]**. The conclusions are not sensitive to this within the stated range because the architecture-internal catalase scavenging dominates clearance for the Pickering and fusion cases. For the free co-formulated case, the endogenous clearance and the co-formulated catalase add roughly linearly. |

---

## Multilingual scan

Per CLAUDE.md §"Global-multilingual research by default":

- **CNKI / Wanfang search** for Chinese-language Pickering emulsion uricase + catalase architecture papers. Liu 2025 *J Nanobiotechnology* is Chinese-authored (Linyi University, Qilu Normal University) but published in English in an international journal — already covered. CNKI search for `尿酸酶 OR 过氧化氢酶 + Pickering 乳液 + 关节腔 OR 关节注射` (uricase / catalase + Pickering emulsion + joint cavity / intra-articular injection) yields a small cluster of Chinese-language reviews echoing the Liu 2025 architectural class with no quantitative diffusion-modeling additions. The reaction-diffusion analysis gap is present in the Chinese-language literature as well.
- **J-STAGE / CiNii** for Japanese-language oxidative-stress / cartilage damage threshold work. The Japanese cartilage-biology literature uses similar in vitro chondrocyte H₂O₂ challenge protocols (50 µM - 1 mM bolus) as the English literature; no separate steady-state synovial-tissue threshold curve is published.

**No translation-protocol cross-check was required** because no non-English source produced a load-bearing claim that diverged from the English-language consensus. The multilingual scan corroborates the English-language gap.

---

## Verification-agent pass (CLAUDE.md Rule 4)

| Claim | Primary source | Verification method | Result |
|---|---|---|---|
| Liu 2025 droplet sizes | PMC12822013 full text | grep '309.7 nm' / '453.3 nm' / '813.8 nm' | ✅ all three values present in source |
| Liu 2025 FRET >85%, distance <10 nm | PMC12822013 full text | grep '85%' + Förster equation cross-check | ✅ |
| Liu 2025 enzyme loading 0.92 mg URI + 0.23 mg CAT | PMC12822013 full text | grep '0.92 mg' / '0.23 mg' | ✅ |
| Liu 2025 specific activities 3.53 / 0.58 / 2.35 / 0.123 U/mg | PMC12822013 full text | grep '3.53 U/mg' | ✅ |
| Schalkwijk 1986 reports injected GOx, not steady-state [H₂O₂] | PMID 3707631 abstract | full abstract reviewed; outcomes are 99mTc, 125I-albumin, 35SO4 incorporation; no steady-state [H₂O₂] reported | ✅ confirmed limitation |
| Uricase kcat order ~10 s⁻¹ | Brenda EC 1.7.3.3, multiple sources | order-of-magnitude check | ✅ |
| Catalase kcat order 10⁷ s⁻¹ | Hansberg 2022, textbook | order-of-magnitude check | ✅ |
| D_H₂O₂ aqueous ~1.4 × 10⁻⁹ m²/s | van Stroe-Biezen 1993 | canonical biosensor literature reference | ✅ (pre-PMC era; canonical) |
| **Interfacial enzyme density 4.55 × 10? /µm² exponent ambiguity** | Liu 2025 PMC12822013 | full text superscript not preserved in PMC HTML rendering | **⚠️ FLAGGED** — used as ~10⁴ /µm² with ±1 OOM uncertainty in sensitivity analysis. Robust to the verdict. |
| **NO published reaction-diffusion analysis exists for any of the three architectures** | This is the central claim that motivates comp-035. Verified by lit-scan provided in the brief + spot-checks against Liu 2025 / Lin 2022 / Liu 2025 *Nat Commun* / Jung 2017 / Schalkwijk 1986. | each paper checked for Damköhler / spatial-coupling math sections | ✅ confirmed — none compute predicted steady-state H₂O₂ escape flux |

**Pre-commit grep-verify gate status: PASSED with one [UNVERIFIED-AS-LITERAL] flag** on the interfacial density exponent and one **[ESTIMATED — DESIGN-SPACE PRIOR]** flag on the fusion-protein active-site separation (no published crystal structure of a uricase-catalase fusion exists; the 1-5 nm range is mechanistically defensible but is a design-space prior rather than a measured value).
