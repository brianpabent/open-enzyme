---
title: "Gut-Lumen UOX Sink"
aliases: [gut lumen, intestinal urate sink, ABCG2 secretion]
related: [uricase.md, blood-barrier-exploits.md, abcg2-modulators.md, validation-experiments.md, luminal-uox-break-even-identifiability-computational.md]
sources: [gout-clinical-pipeline.md, gut-lumen-uricase-physiologic-regime-computational.md, luminal-uox-break-even-identifiability-computational.md]
---

# Gut-Lumen UOX Sink

The hypothesis places active UOX in the intestinal lumen, where it can degrade urate delivered through intestinal transport without requiring the enzyme itself to enter blood. Orally administered ALLN-346 reduced plasma urate in urate-oxidase-deficient mice under the reported study conditions ([Pierzynowska et al. 2020](https://doi.org/10.3389/fmed.2020.569215)). Human evidence is limited to short Phase 1 exposure in healthy volunteers and a Phase 2a conference abstract reporting the first 11 participants in Study 201; Study 202 was terminated for company financing and has no posted results. No validated calculation currently supplies a human dose, serum-urate effect, genotype ordering, topology winner, or production-sufficiency claim. **Animal Model + limited Clinical Trial evidence.**

[COMP-044](./gut-lumen-uricase-physiologic-regime-computational.md) shows that the earlier flat-dose calculation was not robust after adding substrate occupancy and a finite active window. It is an internal-consistency audit, not a replacement efficacy model. [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md) and [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) own the current falsification path.

[COMP-050](./luminal-uox-break-even-identifiability-computational.md) shows why urate concentration alone cannot identify UOX removal. It conditionally maps qualified product fate to local removal and separates calibrated reaction-site capacity from the source and boundary-fate observations needed to reconstruct the declared ledger; practical closure also requires the algebraic residual to pass a prespecified tolerance. Its biological regime is not evaluated.

## Transport and sink hypothesis

ABCG2 is expressed on the apical intestinal epithelium and contributes materially to extra-renal urate handling. Loss-of-function ABCG2 variants increase hyperuricemia and gout risk, supporting the importance of intestinal transport. That biology establishes substrate delivery to the lumen; it does not establish how much additional systemic flux a luminal enzyme can induce.

The proposed sequence is:

1. Transporters deliver some urate to an intestinal compartment.
2. Active luminal UOX consumes locally accessible urate.
3. Local urate concentration and reabsorption may change.
4. Transport, replenishment, reabsorption, renal compensation, and other urate-disposal pathways determine whether the perturbation changes serum urate.

Steps 3–4 are **Mechanistic Extrapolation**. Allantoin disposition, transporter coupling, and “gradient pulling” must be measured; the page does not assume that secreted urate is normally reabsorbed in a fixed fraction, that allantoin cannot be reabsorbed, or that UOX automatically recruits additional ABCG2 flux.

## Substrate-supply and genotype boundary

UOX cannot degrade urate that does not reach its reaction site. Q141K and other ABCG2 variation may therefore matter, but no valid model currently predicts the direction or magnitude of genotype-specific UOX response.

Use genotype as a prospective stratification variable only after a UOX topology clears physiological substrate, oxygen, peroxide, access, survival, and transit gates. [Validation §1.14](./validation-experiments.md#114-abcg2-response-to-dht-and-tnf-with-butyrate-and-lactoferrin-rescue) separately tests transporter induction or rescue hypotheses. Butyrate induction of wild-type ABCG2 does not establish direct Q141K trafficking rescue.

## Evidence

### ALLN-346

ALLN-346 was an engineered *Candida utilis* UOX intended to act in the gut lumen. Study 201 ([NCT04987242](https://clinicaltrials.gov/study/NCT04987242)) completed with an actual registry enrollment of 16; the Phase 2a conference abstract reports only the first 11 adults with hyperuricemia and normal renal function through stage 2 CKD, not receiving concurrent urate-lowering therapy. In those 11, the abstract reports a statistically significant mean serum-urate reduction versus placebo, no serious adverse events or significant safety signals, and no detectable systemic absorption by ELISA ([Terkeltaub et al. 2022](https://doi.org/10.1136/annrheumdis-2022-eular.1662)). Study 202 ([NCT04987294](https://clinicaltrials.gov/study/NCT04987294)) enrolled 19 adults with hyperuricemia, gout, and stage 2 or 3 CKD, then terminated for company financing; its registry has no posted results. These records establish short-exposure human testing and a small reported signal, not another construct's dose, serum effect, safety, formulation, or chassis. **Clinical Trial; conference-abstract and registry evidence.** See [gout clinical pipeline](./gout-clinical-pipeline.md).

### PULSE

PULSE used engineered *E. coli* Nissle with a local urate-responsive controller, multiple UOX topologies, and oxygen/peroxide-management components. Oral administration altered urate phenotypes in hyperuricemic rodents. It does not establish which component, topology, or local activity is sufficient under human intestinal conditions. **In Vitro + Animal Model** (Gao et al. 2025, PMID 41038159).

### Engineered *S. boulardii*

An engineered probiotic-yeast system demonstrated UOX expression and urate-degradation activity under its reported assay conditions. That supports construct feasibility, not human reaction-site activity, dose, or serum effect. **In Vitro.** See [engineered yeast UOX proposal](./engineered-yeast-uricase-proposal.md).

## Physiological gates

The decision variable is active UOX at the reaction site over time, not protein mass, CFU, promoter strength, or a favorable purified-enzyme assay.

Measure together:

- initial and terminal urate amount with measured volume and sampling correction;
- systemic and other urate influx, reabsorption, and outflow;
- algebraic reconstruction of unattributed residual loss against a prespecified acceptance tolerance;
- qualified total and source-resolved UOX product fate;
- UOX topology, calibrated reaction-site active capacity, access, release, and persistence;
- oxygen availability and coupling;
- H₂O₂ generation and reaction-site scavenger capacity;
- organism or formulation survival through production, storage, and transit;
- urate and allantoin movement, including reabsorption;
- epithelial injury and microbiome effects;
- renal and other compensatory urate handling in later translation.

[Validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) owns the matched reaction-site experiment. [§1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) determines whether the evidence supports animal escalation.

## Implementation candidates

Yeast, koji, bacterial, purified-enzyme, and other formulations are unranked implementation candidates. Each must report the same reaction-site activity and safety variables. A food-use history, secretion precedent, expression yield, or residence-time hypothesis does not make a chassis the project or establish a product format.

Track-specific work lives in:

- [Engineered yeast UOX proposal](./engineered-yeast-uricase-proposal.md)
- [Engineered koji protocol](./engineered-koji-protocol.md)
- [Engineered LBP chassis](./engineered-lbp-chassis.md)
- [Delivery route matrix](./delivery-route-matrix.md)

## What the route avoids—and inherits

The route avoids the need to transport a large active enzyme across epithelium. It inherits uncertain substrate supply, topology, oxygen, peroxide, access, survival, transit, reabsorption, local safety, and systemic compensation. Systemic UOX delivery remains a separate exploit with different gates; see [systemic UOX delivery attack surface](./blood-barrier-exploits.md).

## Falsification

Kill or redirect the tested configuration if no topology produces reproducible urate consumption at relevant substrate and oxygen conditions without unacceptable peroxide, epithelial injury, viability loss, or other safety failure. Even a bench pass does not establish clinical effect: translation must still show a sustained systemic consequence under controlled conditions.

Failure of the gut-lumen UOX track does not hold up Open Enzyme. It documents why this exploit fails and redirects work to another urate-disposal mechanism, delivery route, inflammatory chokepoint, or local intervention.
