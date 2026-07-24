---
title: "Androgen–urate intervention leads"
date: 2026-05-07
tags:
  - testosterone
  - androgens
  - clomiphene
  - enclomiphene
  - eurycoma-longifolia
  - eurycomanol
  - cordycepin
  - urate
  - urat1
  - prps
related:
  - androgen-urate-axis.md
  - prps-purine-biosynthesis-chokepoint.md
  - validation-experiments.md
  - medicinal-mushroom-complement-track.md
  - t-axis-adjuvant-urate-mapping-computational.md
sources:
  - PMID 29422889
  - PMID 31920654
  - PMID 34785103
  - PMC8254464
status: draft
---

# Androgen–urate intervention leads

## Gout weakness and evidence boundary

Androgen manipulation and urate handling intersect, but hormone direction
alone does not predict serum urate. The usable weakness is narrower: a defined
intervention might change an androgen endpoint and an urate-production or
urate-transport endpoint at the same exposure. Each axis must be measured
independently. The mechanistic background belongs in the
[androgen–urate axis](./androgen-urate-axis.md).

No evidence assembled here establishes a natural substitute for clomiphene,
a gout treatment, or a candidate ranking. The retired
[COMP-015](./t-axis-adjuvant-urate-mapping-computational.md) failed because it
treated botanical extracts, purified compounds, related quassinoids, animal
results, and in-vitro assays as interchangeable evidence objects.

## Source-specific evidence

| Evidence object | What was tested | What survives |
|---|---|---|
| Physta *Eurycoma longifolia* extract | A characterized oral extract was studied for 12 weeks in 105 men. Serum urate appeared in the safety table; week-12 comparisons with placebo were null (`p=0.88` at 100 mg/day and `p=0.52` at 200 mg/day), and placebo also declined. **Clinical Trial — null urate outcome**; PMC8254464. | Human androgen evidence for this exact extract may motivate a dual-axis study. The trial does not show urate lowering and does not transfer to purified eurycomanone or eurycomanol. |
| 70% ethanol *E. longifolia* stem extract | The extract was tested at 100, 200, and 400 mg/kg in hyperuricemic animals. In the same report, quassinoids 4–7 inhibited hURAT1 at 50 µM; eurycomanone was compound 3 and showed comparatively low activity. **Animal Model + In Vitro**; PMID 31920654. | The extract and compounds 4–7 are separate urate leads. Neither supplies a Physta result or a purified-eurycomanone efficacy claim. |
| Purified eurycomanol | Oral eurycomanol at 5–20 mg/kg lowered serum urate, increased 24-hour urate clearance, decreased hepatic PRPS expression, and changed renal and intestinal transporter measurements in hyperuricemic mice. **Animal Model**; PMID 34785103. | A purified-compound urate lead survives. Concurrent expression, clearance, and transporter changes do not establish direct PRPS binding, causal PRPS-flux control, or human efficacy. |
| Purified cordycepin | Oral cordycepin at 15, 30, and 60 mg/kg lowered serum urate and changed renal URAT1 expression in hyperuricemic mice. **Animal Model**; PMID 29422889. | Cordycepin remains an exact-material urate lead. Whole *Cordyceps*, cordycepin, and cordycepin-plus-pentostatin preparations are not evidence-equivalent. |
| Enclomiphene and racemic clomiphene | Clinical studies measured endocrine and reproductive outcomes. The cited studies did not establish a matched-exposure urate comparison. **Clinical Trial for endocrine outcomes; Mechanistic Extrapolation for urate**. | Their different hormone profiles make a controlled urate comparison testable; they do not establish a urate direction or a preferred intervention. |

### Evidence objects that do not yet bridge both axes

Boron, magnesium, zinc, DIM/I3C, *Fadogia agrestis*, cistanche, epimedium,
Kampo formulas, and other androgen-associated materials have heterogeneous
evidence and safety profiles. An androgen signal, deficiency-correction
effect, traditional use, or animal endocrine result is not an urate result.
They enter this program only after exact identity, exposure, an androgen
endpoint, and an independently supported urate mechanism can be specified.

## Sourcing, delivery, and exposure

The scientific unit is the tested material, not the species name or product
category.

- **Characterize identity.** A named extract requires a composition
  fingerprint and lot record. A purified compound requires orthogonal identity
  and purity checks. Extract ratios and botanical names do not establish
  equivalent quassinoid or cordycepin exposure.
- **Preserve preparation boundaries.** Physta, a 70% ethanol stem extract,
  purified eurycomanone, and purified eurycomanol are four different evidence
  objects. Whole *Cordyceps* can change cordycepin stability through associated
  metabolites, but that does not make whole material equivalent to purified
  cordycepin.
- **Measure delivered exposure.** Oral animal administration establishes a
  route used in those models, not human target-compartment exposure. Free
  concentration, metabolism, and time above the assay-relevant range must be
  measured for the exact preparation.
- **Separate compartments and mechanisms.** Serum urate, urinary clearance,
  transporter expression, transporter flux, PRPS expression, and
  isotope-resolved purine flux are different readouts. Movement in one does
  not prove the others.
- **Carry safety with the material.** Botanical source, extraction process,
  impurities, endocrine activity, and off-target effects must be assessed for
  the same lot used in the efficacy assay.

## Research conjecture

> **Research conjecture — an exact material can separate androgen benefit from urate liability**{ .research-conjecture-label }
>
> **Grounded premises:** Characterized *E. longifolia* preparations have human
> androgen evidence (**Clinical Trial**). Purified cordycepin, a source-specific
> *E. longifolia* extract, selected quassinoids, and purified eurycomanol supply
> separate urate leads (**Animal Model** and **In Vitro**; PMID 29422889, PMID
> 31920654, and PMID 34785103). Physta's human urate comparison was null
> (**Clinical Trial — null urate outcome**; PMC8254464).
>
> **Novel leap:** One compositionally verified material might improve an androgen endpoint without worsening urate, or might improve both, at the same measured exposure. No direct evidence tests this dual-axis connection.
>
> **Why it matters:** A positive result would expose an androgen–urate control
> point without assuming that all androgen manipulation carries the same urate
> effect.
>
> **Discriminating observation:** Run the matched design in
> [validation §2.8](./validation-experiments.md#28-exact-material-androgen--urate-dual-axis-validation).
> Require identity, exposure, androgen endpoints, urate mass balance, direct
> transporter or PRPP-flux readouts, and safety for each material. A null
> rejects only the tested material–exposure configuration.

## Experimental program

1. **Qualify one evidence object.** Fix the material, lot, identity method,
   purity or composition fingerprint, vehicle, and exposure measurement.
2. **Test the axes separately.** Measure androgen outcomes and urate mass
   balance without using either as a proxy for the other.
3. **Localize the urate effect.** If urate changes, distinguish production
   from excretion with direct flux and transporter-function measurements.
   PRPS expression alone is insufficient.
4. **Test causality.** Use matched positive and negative controls,
   perturbation/rescue where feasible, and predeclared decision rules.
5. **Advance only the exact configuration.** A positive result does not
   transfer to a related compound, extract, formulation, or species.

The clomiphene-specific exposure question remains in
[H10](./hypotheses/H10-clomiphene-dose-urate-coupling.md). The earlier
intestinal estrogen-receptor mechanism in
[H07](./hypotheses/H07-clomid-intestinal-er-antagonism.md) is retracted.

## Related evidence

- [PRPS / PRPP supply](./prps-purine-biosynthesis-chokepoint.md)
- [Medicinal-mushroom complement track](./medicinal-mushroom-complement-track.md)
- [ABCG2 modulators](./abcg2-modulators.md)
- [Exact-material validation §2.8](./validation-experiments.md#28-exact-material-androgen--urate-dual-axis-validation)
