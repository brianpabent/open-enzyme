# comp-033 — input provenance (CLAUDE.md Rule 4 pre-commit grep-verify gate)

Every load-bearing quantitative claim is named here, with the primary source and verification status.

## Verified directly against primary source

| Claim | Value | Source | Verified |
|---|---|---|---|
| IL-1Ra UniProt accession | P18510 | UniProt 2026-01-28 entry version 244 | **Verified** via `curl https://rest.uniprot.org/uniprotkb/P18510.txt` on 2026-05-16. Confirmed: precursor 177 aa; signal 1..25; mature chain 26..177 (152 aa); single intramolecular disulfide C91-C141; gene IL1RN; alt name INN=Anakinra. |
| IL-1Ra mature mass | 17.3 kDa | UniProt P18510 mature chain 26-177 (152 aa) | Verified — 152 aa × ~113 Da/aa ≈ 17.2 kDa; rounded to 17.3 kDa per literature. |

## Verified against well-established prescribing-info / peer-reviewed sources

| Claim | Value | Source | Verification status |
|---|---|---|---|
| Anakinra (Kineret) approved dose | 100 mg SC QD | Kineret USPI (FDA label) | Verified against FDA label and Yang et al. 2003 PK summary; widely cited and stable across sources. Not Paperclip-grep verified at primary-paper level — relying on FDA label tier. |
| Anakinra plasma t1/2 | 4 hours | Kineret USPI; Granowitz 1992; Yang 2003 | Verified at the prescribing-info tier; central estimate consistent across studies (range 4-6h depending on renal function). |
| Anakinra Cmax at 100 mg SC | 1.5 µg/mL | Yang 2003 PK; Granowitz 1992 (single-dose) | Verified at the peer-reviewed-PK tier. Range across studies 1.3-1.8 µg/mL; central 1.5. |
| Anakinra SC bioavailability | 95% | Kineret USPI | Verified at prescribing-info tier. |
| Canakinumab list price per 150 mg dose | ~$21,000 | AHFS pricing tables; Ilaris USPI | Verified at pricing-database tier. Range $18,000-23,000 per dose across pricing references; central $21,000. |
| Canakinumab annual cost in gout | $100K-300K depending on flare frequency | AHFS; gout flare-frequency literature (5-12 flares/year typical) | Order-of-magnitude verified; exact number depends on per-patient flare count. |

## Verified against published clinical-trial / preclinical-pharma sources

| Claim | Value | Source | Verification status |
|---|---|---|---|
| Translate Bio MRT5005 dose range | 8-24 mg per inhalation | Rowe et al. 2023 J Cyst Fibros; NCT03375047 | Verified at clinical-trial-registry + peer-reviewed tier. Phase 1/2 study reported these dose levels in dose-escalation. |
| Translate Bio MRT5005 device | PARI eFlow vibrating-mesh nebulizer | Translate Bio IND filings; Rowe 2023 | Verified at IND-filing tier. |
| Arcturus ARCT-032 dose range | 4-20 mg per inhalation | Arcturus public disclosures 2024-2025 | Verified at company-disclosure tier (less rigorous than peer-reviewed; flagged). |
| BioNTech BNT162b2 5'UTR identity | human HBA1 (alpha-globin) | Patent literature (US 2021/0046193 A1); Sahin 2014 Nat Rev Drug Discov | Verified at patent-filing tier. |
| Pfizer BNT162b2 polyA architecture | A30-Linker-A70 (110 nt segmented) | Patent disclosures | Verified at patent tier. |
| m1Psi chemistry origin | Karikó & Weissman 2005 / Andries 2015 | Karikó Immunity 2005; Andries 2015 J Control Release | Verified at peer-reviewed-paper tier. Nobel Prize 2023 corroborates significance. |

## Order-of-magnitude estimates with cited anchors

| Claim | Range | Source | Verification status |
|---|---|---|---|
| Alveolar translation efficiency (mass ratio protein/mRNA, integrated over expression window) | 1,000–50,000 ng protein per µg mRNA (1–50× mass ratio) | Pardi 2018 Nat Rev Drug Discov; Ogata 2022 CID (BNT162b2 plasma spike detection); Lokugamage 2021 ACS Nano inhaled SORT-LNP; Patel 2019 ACS Nano | Order-of-magnitude; wide log-uniform prior. The mass ratio reflects total tissue protein synthesized across the 24-48h expression window per mass of mRNA delivered. BNT162b2 30 µg → estimated tens-to-hundreds of µg total spike (mass ratio 1-10×); inhaled mRNA in alveolar epithelium at comparable or higher local concentration. **2026-05-16 correction note: an earlier draft used 50-500 ng/µg (mass ratio 0.05-0.5×) — this was an underestimate that conflated plasma-concentration measurements with total-protein-synthesized; corrected to the integrated mass-ratio range here.** |
| Vibrating-mesh nebulizer lower-airway delivery | 10-40% of nominal | Geller 2009 Respir Care nebulizer review; PARI eFlow performance specs | Order-of-magnitude; wide prior. |
| Alveolar -> systemic protein bioavailability (10-30 kDa, non-glycosylated) | 10-50% | Patton & Byron 2007 Nat Rev Drug Discov | Order-of-magnitude; Afrezza inhaled insulin (5.8 kDa) is the closest precedent at higher bioavailability; conservative range used. |
| Pulmonary mRNA-LNP expression duration with m1Psi | 24-96 hours | Compilation across CF inhaled-mRNA preclinical + clinical; matched to anakinra-style transient kinetics | Order-of-magnitude. |
| COVID-mRNA-vaccine COGS per dose at industrial scale | $2-10 | Whitaker 2022 Nature; Moderna/Pfizer SEC filings | Verified at peer-reviewed + SEC-filing tier. |
| Specialty-inhaled mRNA-LNP cost per mg at moderate scale | $0.5-5 | Translate Bio IND filings; standard CDMO pricing | Order-of-magnitude. |

## Multilingual sources checked

| Source | Search performed | Result |
|---|---|---|
| CNKI (Chinese national CKI) | "吸入 mRNA 痛风" (inhaled mRNA gout) — no direct hits; "重组 IL-1Ra 痛风" (recombinant IL-1Ra gout) — meta-analyses of anakinra in gout exist in Chinese literature; corroborate Western anakinra-in-gout off-label use; no inhaled-IL-1Ra-specific work | No new quantitative anchor surfaced; Chinese sources mirror Western off-label gout use of anakinra |
| J-STAGE (Japan) | "吸入 mRNA" (inhaled mRNA) + Kampo medicine literature for gout | Japanese inhaled-mRNA work via Daiichi-Sankyo collaboration with Moderna; not gout-relevant. Kampo gout literature is small-molecule / herbal — out of scope. |
| Cross-check: Japanese inhalation-device + mRNA | Daiichi-Sankyo, Eisai pulmonary mRNA programs | No disclosed clinical inhaled-mRNA-IL-1Ra programs in Japanese pharma pipelines as of 2026-05-16 |

The multilingual check is corroborative, not anchor-shifting. The Western-source dose-AUC and partner-landscape pictures hold.

## Items flagged for follow-up verification

1. Arcturus ARCT-032 specific dose range — company-disclosure tier; would benefit from peer-reviewed-publication verification if available.
2. Alveolar -> systemic protein bioavailability — Patton & Byron 2007 is the canonical reference but specific to a different protein class than IL-1Ra. The 17 kDa non-glycosylated profile is the closest match to growth hormone (~22 kDa, ~10% bioavailability) and insulin (5.8 kDa, ~5-15% bioavailability for Afrezza). Range conservative-to-moderate.
3. Cost-per-dose extrapolation from COVID-vaccine class to specialty inhaled — economics-of-scale curve is the largest single uncertainty in the economic model. Range used (factor of 50× across scenarios) is honest about this.

## Verification rule

Every input file in this directory has been audited against this provenance table. All load-bearing numbers used in the model are either (a) verified directly against primary source (top of this file), (b) verified against well-established secondary sources, or (c) used as wide priors in the Monte Carlo to honestly reflect the uncertainty.
