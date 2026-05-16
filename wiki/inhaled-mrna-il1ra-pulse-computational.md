---
title: "Inhaled mRNA-IL-1Ra pulse therapy — dose-AUC modeling + partner-ID (comp-033)"
date: 2026-05-16
tags:
  - chassis-pending
  - mrna-lnp
  - acute-flare-abort
  - il1ra
  - anakinra-equivalent
  - dose-modeling
  - discovery-engine-output
  - computational
related:
  - chassis-pending-interventions.md
  - etc/open-enzyme-vision.md
  - modality-chokepoint-matrix.md
  - delivery-route-matrix.md
  - gout-clinical-pipeline.md
  - nlrp3-inflammasome.md
sources:
  - "experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy/ — Monte Carlo dose-AUC model, n=20,000, seed 33"
  - "UniProt P18510 (verified 2026-05-16 via rest.uniprot.org)"
  - "Kineret USPI; Yang 2003 anakinra PK; Granowitz 1992"
  - "Rowe et al. 2023 J Cyst Fibros (Translate Bio MRT5005 CF)"
  - "Pardi 2018 Nat Rev Drug Discov; Ogata 2022 CID (BNT162b2 plasma protein); Patton & Byron 2007"
status: published
---

# Inhaled mRNA-IL-1Ra pulse therapy — computational analysis (comp-033)

**Verdict: RED** on the systemic-anakinra-equivalent gate at currently-feasible inhaled mRNA doses (4–24 mg per administration). **The verdict does not close the modality** — three honest paths forward keep the chassis-pending entry [`chassis-pending-interventions.md` §4](./chassis-pending-interventions.md) active.

## Dose-AUC headline

Monte Carlo n=20,000 over priors anchored on Translate Bio MRT5005 + Arcturus ARCT-032 disclosed clinical doses, BNT162b2 plasma-protein detection, Patton & Byron alveolar→systemic transit, and Kineret PK. Median predicted plasma Cmax **0.025 µg/mL** [5th–95th pct 0.002–0.28] vs anakinra benchmark **1.5 µg/mL** — median ratio **2% of anakinra**. Reverse-dose calculation: ~195 mg mRNA needed for median 0.5 µg/mL Cmax (1/3 anakinra); ~585 mg for full anakinra-equivalent. Both 8–25× above the highest currently-disclosed inhaled-mRNA clinical dose (24 mg). Top sensitivity driver: translation efficiency mass ratio (ρ = +0.78).

## Three paths forward (the chassis-pending entry stays open)

1. **Repeat dosing within a single flare** — 2–4 nebulizer administrations per 24h plausibly accumulate to therapeutic AUC without requiring single-dose breakthroughs. Not modeled quantitatively here; warrants a follow-up comp-NNN AUC-accumulation analysis.
2. **Intra-articular mRNA-IL-1Ra** as a different chassis for the same target. Local concentration at the affected joint bypasses systemic dilution that dominates the inhaled math; sister architecture to the comp-035 intra-articular uricase + catalase work. Already flagged as 🟡 cell in [`delivery-route-matrix.md`](./delivery-route-matrix.md) (RNA platforms × intra-articular).
3. **Sub-anakinra exposure may still be therapeutically meaningful.** Anakinra's trough (Cmin) is 0.05 µg/mL and the drug retains efficacy at that exposure; the upper-decile prior in this model (Cmax 0.28 µg/mL sustained over 48h) reaches comparable AUC to anakinra trough-band exposure. The RED verdict is specifically against full anakinra Cmax matching, not against any therapeutic effect.

## Construct-design priors

m1Psi (Karikó–Weissman) chemistry; human alpha-globin 5'UTR + truncated alpha-globin / mtRNR1 3'UTR for transient expression matching the 24–48h flare window; 80–120 nt polyA; native IL-1Ra signal peptide (alveolar type II pneumocytes are highly secretory). LNP class ALC-0315 / SM-102 / Acuitas LP-01 with nebulization-stability screen. Vibrating-mesh nebulizer for POC; DPI for commercial product.

## Economic comparison (holds independently of dose-feasibility)

Cost-per-flare at scale: $2 (low) / $18 (central) / $120 (high). Annual cost at 5–10 flares/yr: $10–1,200. Canakinumab benchmark: $105K–300K/yr. **Cost ratio 50–3,000× in favor of inhaled mRNA-IL-1Ra approach** — dominated by mRNA-LNP scale economics, robust across all dose-feasibility scenarios.

## Partner landscape — 15 candidates, 4 Tier A

**Tier A (active inhaled-mRNA clinical/preclinical programs, 4):** Arcturus Therapeutics (LUNAR-CF / ARCT-032, Phase 2); ReCode Therapeutics (RCT2100 + SORT-LNP, Phase 1); Ethris (SNIM-RNA / AstraZeneca, preclinical); Sanofi (legacy Translate Bio MRT5005 platform). **Tier B (7 CDMOs):** CordenPharma, Aldevron/Danaher, Lonza, Recipharm (inhalation devices), Acuitas (LNP IP), Precision NanoSystems, TriLink/Maravai. **Tier C (4 academic labs):** Mitchell (UPenn), Sahay (OSU), Anderson (MIT), Siegwart (UTSW — SORT-LNP origin).

**Recommended first contacts:** Arcturus, ReCode, Siegwart Lab UTSW, Mitchell Lab UPenn.

## Implication for the platform

Chassis-pending entry stays open. Discovery-engine handoff package (target validation + construct-design priors + dose math + economic argument + partner shortlist) is shippable now — RED on systemic-equivalent reframes the partner conversation as "this chassis needs a repeat-dose protocol or route pivot, here's the math," not "this won't work." The 50–3,000× cost edge vs canakinumab is what makes the partner conversation worth having.

## Cross-references

[comp-033 reproducible analysis](../experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy/) | [`chassis-pending-interventions.md` §4](./chassis-pending-interventions.md) | [`etc/open-enzyme-vision.md` §10 "temporal stack"](./etc/open-enzyme-vision.md) | [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) | [`delivery-route-matrix.md`](./delivery-route-matrix.md)
