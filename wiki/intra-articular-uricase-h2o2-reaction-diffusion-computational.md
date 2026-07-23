---
title: "Intra-articular Uricase H₂O₂ Reaction-Diffusion Analysis Across Three Spatial-Coupling Architectures (Computational, comp-035)"
date: 2026-05-16
tags:
  - computational
  - comp-035
  - intra-articular
  - uricase
  - catalase
  - hydrogen-peroxide
  - reaction-diffusion
  - damkohler
  - pickering-emulsion
  - fusion-protein
  - chassis-pending
  - gout
related:
  - chassis-pending-interventions.md
  - gout-kill-chain-delivery-routes.md
  - delivery-route-matrix.md
  - engineered-koji-protocol.md
  - uricase.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "Liu Y et al. J Nanobiotechnology 2025;24(1):51 (PMID 41390400, DOI 10.1186/s12951-025-03901-1) — Pickering emulsion URI+CAT IA cascade; FRET <10 nm; PEBR 810 nm droplets; URI 0.92 mg + CAT 0.23 mg per dose; interfacial enzyme density"
  - "Lin A et al. Nano Lett 2022;22(1):508-516 (PMID 34968071, DOI 10.1021/acs.nanolett.1c04454) — Pt/CeO₂ nanozyme uricase/catalase self-cascade for acute gout"
  - "Liu L et al. Nat Commun 2025;16(1):2339 (PMID 40057522, DOI 10.1038/s41467-025-56100-9) — UOx + sodium citrate hollow mesoporous silica nanomotor"
  - "Jung S, Kwon I. Sci Rep 2017;7:44330 (PMID 28287162, DOI 10.1038/srep44330) — UOX + AuNP catalase-mimic cascade"
  - "Schalkwijk J et al. Arthritis Rheum 1986;29(4):532-8 (PMID 3707631, DOI 10.1002/art.1780290411) — canonical IA H₂O₂ damage model via cationized GOx"
  - "van Stroe-Biezen et al. Anal Chim Acta 1993;273:553 — D_H₂O₂ aqueous ~1.4 × 10⁻⁹ m²/s biosensor canonical reference"
  - "Hansberg W. Antioxidants (Basel) 2022;11(11):2173 (PMC9687031, DOI 10.3390/antiox11112173) — monofunctional heme-catalase mechanism review with kcat ~10⁷-10⁸ s⁻¹"
  - "Najjari A et al. ACS Omega 2022;7(50):46251-46262 (PMC9773812, DOI 10.1021/acsomega.2c04071) — PASylated A. flavus urate oxidase kinetic characterization"
status: complete (frozen v1; non-decision-grade Phase-0 prior; empirical peroxide and tissue-safety gates open)
---

# Intra-articular Uricase H₂O₂ Reaction-Diffusion Analysis (Computational, comp-035)

> **Current interpretation:** comp-035 is a non-decision-grade Phase-0 prior. It does not establish a safe H₂O₂ threshold, clear any architecture, select a chassis, or authorize economics-driven selection. Its frozen v1 values describe one simplified implementation and remain historical model outputs only. (Mechanistic Extrapolation)

> The frozen artifact is preserved at [`./etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion/`](./etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion/) for provenance. Its artifact-era GREEN/YELLOW/RED labels are not active decision labels.

## The question

Can Pickering emulsion, uricase-catalase fusion, or free co-formulation control H₂O₂ at the reaction site without unsafe local tissue exposure?

comp-035 evaluated a narrower question: steady-state bulk H₂O₂ under assumed uricase production and catalase scavenging in three idealized architectures. It did not resolve a spatial synovial-tissue boundary, reaction-site time course, local peaks, enzyme retention or inactivation, or tissue response. The computation therefore cannot answer the safety question by itself.

## Historical v1 outputs — non-authorizing

The frozen v1 artifact reported the following modeled distributions:

| Architecture | Historical modeled bulk H₂O₂, median | Historical modeled bulk H₂O₂, p95 |
|---|---:|---:|
| Pickering emulsion | 0.19 µM | 1.1 µM |
| Uricase-catalase fusion | 0.034 µM | 0.20 µM |
| Free co-formulation | 0.19 µM | 7.2 µM |

These are not measured concentrations, validated tissue-boundary predictions, or safety margins. The artifact compared them with a derived 10 µM steady-state threshold that was not verified for sustained local synovial-tissue exposure. That threshold and the resulting GREEN/YELLOW/RED classifications are retired from active decision use.

## What the model still contributes

Within its own assumptions, comp-035 suggested a testable distinction between nanometer-scale capture and bulk catalase scavenging: the Pickering shell calculation did not retain most modeled H₂O₂ locally, while the assumed bulk catalase sink carried the predicted steady-state result. This does not establish the operative in vivo safety mechanism. The conclusion depends on unresolved loading, active-site, activity, retention, and transport assumptions.

The 2026-07-14 review identified four interpretation-limiting implementation problems:

- the calculation is a well-mixed steady-state bulk surrogate, not a spatial tissue-boundary or exposure-time model;
- Pickering loading and active-site accounting were hardcoded or internally unresolved;
- named edge cases did not perturb all architectures consistently; and
- sensitivity summaries included variables unused by the architecture being summarized.

Accordingly, comp-035 neither rules an architecture in nor rules one out. It provides no architecture or chassis winner and no basis for moving selection to production economics, regulatory pathway, or manufacturing complexity.

## Remaining gates

Architecture comparison remains blocked on all four of the following:

1. **Matched reaction-site H₂O₂ time course:** measure each architecture under matched substrate conditions and explicitly matched uricase and catalase activities, spanning the intended operating window rather than relying on a single steady-state estimate.
2. **Catalase activity, stoichiometry, retention, and diffusion:** quantify the delivered active URI:CAT ratio, catalase activity over the exposure period, retention or loss from the reaction site, and transport through the formulation and surrounding medium.
3. **Local exposure:** resolve bulk concentration and local magnitude-duration profiles at crystals, injection or formulation depots, and the tissue-facing boundary.
4. **Tissue safety:** test the measured local exposure profiles against relevant synovial and cartilage endpoints; do not substitute the retired 10 µM model threshold for this gate.

Only after these gates are met can non-peroxide criteria be used in an architecture comparison. comp-035 supplies no ordering among Pickering, fusion, and free co-formulation.

## Evidence status

- **Mechanistic Extrapolation:** every comp-035 concentration, capture, sensitivity, and architecture comparison is an in silico output conditional on the frozen assumptions.
- **Animal Model / In Vitro:** the cited studies provide formulation-specific precedent and input anchors; they do not validate comp-035's generic threshold or cross-architecture safety ranking.
- **Clinical Trial:** no clinical IA uricase evidence is represented here.

## Reproduction

From the repository root, the frozen v1 model can be rerun with:

```bash
cd wiki/etc/experiments/comp-035-ia-uricase-h2o2-reaction-diffusion
python3 analyze.py
```

Reproduction regenerates the historical model outputs; it does not validate the safety interpretation.
