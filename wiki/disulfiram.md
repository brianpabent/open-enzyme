---
title: Disulfiram (Antabuse)
aliases:
  - Antabuse
  - Gasdermin D Inhibitor
  - GSDMD Blocker
related:
  - nlrp3-inflammasome
  - gout
  - approved-drugs
  - gasdermin-d
  - chokepoint-6b
  - zileuton
  - gsdmd-pore-delivery-paradox
sources:
  - nlrp3-exploit-map.md
---

# Disulfiram (Antabuse): The Repurposed GSDMD Inhibitor

**Disulfiram** (Antabuse) is an FDA-approved alcohol-deterrent drug that also blocks gasdermin D pore formation, the pyroptotic exit step of the NLRP3 pathway. Its gout-relevant hypothesis is downstream containment of IL-1β release after inflammasome activation. That mechanism is preclinical; disulfiram has not established efficacy or a safe dose window in gout.

**Compounding route:** Bulk API availability makes a lower-dose extended-release formulation technically testable, but useful release kinetics, GSDMD target engagement, alcohol-response separation, and safety have not been established. (source: compounding-pharmacy-track.md)

**Off-target flag:** ChEMBL v37 reports **LOXL4 IC50 = 59 nM** (pChEMBL 7.23, *Bioorg Med Chem Lett* 2018). Relevance to gout or GSDMD biology is unclear and requires primary-source verification. See [chembl-cross-check.md](./etc/chembl-cross-check.md). (In Vitro)

> **Complementary pharma at CP6**: zileuton (5-LOX inhibitor, CP6a) and disulfiram (GSDMD inhibitor, CP6b) hit different branches of the same chokepoint. See [wiki/zileuton.md](./zileuton.md) for the CP6a pharma-grade option.

## The GSDMD Target: Chokepoint 6b (Pyroptotic Exit)

In the NLRP3 inflammasome cascade, gasdermin D (GSDMD) is the "exit route" — the final executor that forms membrane pores and releases IL-1β into the extracellular space. Once IL-1β is outside the cell, it triggers the full inflammatory storm: neutrophil recruitment, pain, swelling, and the full gout flare symptomatology.

By blocking gasdermin D pore formation, disulfiram prevents IL-1β release without stopping the upstream inflammasome assembly.

**(Source: nlrp3-exploit-map.md)** — "Disulfiram — Antabuse — the drug prescribed to alcoholics since the 1950s — was discovered in 2020 (Nature Immunology) to specifically block gasdermin D pore formation at nanomolar concentrations. It covalently modifies Cys191 on GSDMD, preventing the N-terminal fragment from oligomerizing into membrane pores."

## Mechanism: Covalent GSDMD Modification

### The Chemistry

Disulfiram covalently modifies **Cys191** (in humans; Cys192 in mice) on the gasdermin D protein. This modification prevents the processed N-terminal fragment of GSDMD from oligomerizing into the membrane-spanning pore structure required for IL-1β release.

Critically, disulfiram allows GSDMD cleavage by caspase-1 to proceed normally — it doesn't block the upstream inflammasome cascade. Instead, it blocks only the final pore-formation step.

**(Source: nlrp3-exploit-map.md)** — "The elegance: disulfiram still allows IL-1β and GSDMD processing (caspase-1 can still cleave them) but abrogates pore formation. No pores = IL-1β stays trapped inside the cell. No pores = no pyroptosis = no inflammatory amplification from cell death."

### Alternative Modifications

Other compounds target the same Cys191 vulnerability:

- **DMF (Dimethyl Fumarate / Tecfidera):** Succin ylates Cys191, forming S-(2-succinyl)-cysteine. FDA-approved for multiple sclerosis; discovered to block GSDMD as a mechanism
- **NSA:** Research compound that modifies Cys191 via a different chemistry

The fact that multiple independent compounds converge on this single cysteine residue confirms it is a universal vulnerability.

## Clinical Validation

### The 2020 Discovery

Published in Nature Immunology (2020): researchers screened a library of FDA-approved drugs for NLRP3 pathway inhibition and found disulfiram's GSDMD-blocking activity. This wasn't a drug designed for this purpose — it was an accidental discovery during pharmacological screening.

### Human-use boundary

Disulfiram has decades of human use for alcohol use disorder, so its pharmacology and interactions are better characterized than those of a new chemical entity. That history does not validate gout use. The alcohol reaction, idiosyncratic hepatotoxicity, neuropathy, and drug interactions constrain any dose-finding study.

## Source, formulation, and safety constraints

- **Source:** Generic prescription tablets and bulk API exist; gout remains an off-label research indication.
- **Delivery question:** A lower-dose extended-release formulation could test whether sustained GSDMD engagement can be separated from the aldehyde-dehydrogenase effect, but the modeled window is not a dosing recommendation.
- **Target-engagement requirement:** Parent disulfiram, metabolites, GSDMD pore formation, and aldehyde-dehydrogenase activity need to be measured together.

- **Alcohol interaction:** Disulfiram blocks aldehyde dehydrogenase, causing severe flushing, nausea, and cardiovascular stress if alcohol is consumed. This is intentional for alcohol-use deterrence but requires absolute abstinence
- **Copper chelation:** Disulfiram binds copper; patients on copper-dependent enzyme therapies (e.g., [[gotu-kola|GHK-Cu peptide]]) may experience reduced efficacy
- **Drug interactions:** Check for interactions with anticoagulants and other medications

### Expanded Contraindications and Drug Interactions (source: supplements-stack.md, 2026-04-26)

**Contraindications:**
- **Any alcohol use** (acute disulfiram-ethanol reaction: flushing, tachycardia, hypotension, severe nausea — can be fatal at high alcohol doses). This includes some mouthwashes, OTC cold preparations, kombucha, and fermented foods with residual ethanol.
- Active hepatic disease (LFTs >3× upper limit of normal)
- Severe coronary artery disease (cardiovascular collapse risk on ethanol exposure)
- Severe psychosis (case reports of psychotic exacerbation)
- Pregnancy
- Concurrent metronidazole or other disulfiram-like agents

**Drug interactions:**
- **Metronidazole, tinidazole, cefoperazone, griseofulvin, certain MAOIs, isoniazid:** disulfiram-like reactions amplified.
- **Warfarin:** disulfiram inhibits warfarin metabolism → increased anticoagulation; INR monitoring required.
- **Phenytoin:** disulfiram inhibits phenytoin metabolism → toxicity risk.
- **Theophylline, caffeine (high-dose):** disulfiram inhibits clearance; toxicity risk.
- **Benzodiazepines metabolized by CYP3A4 (alprazolam, midazolam):** disulfiram inhibits clearance; sedation risk.
- **Acetaminophen at high doses:** competing hepatic stress (additive hepatotoxicity).
- **Many ethanol-containing medications (some elixirs, sublingual sprays, IV preparations):** trigger reaction.

- Disulfiram–ethanol reaction severity scales with both exposure levels; ethanol-containing foods and medicines are therefore a study-exclusion and safety-control problem.
- Hepatic stress from other agents is a combination constraint.

(source: supplements-stack.md)

## Falsification tests

1. Demonstrate GSDMD Cys191 engagement and pore blockade in MSU-stimulated human macrophages at exposure below the aldehyde-dehydrogenase effect.
2. In an MSU model, measure intracellular versus extracellular IL-1β, pyroptosis, neutrophil recruitment, and flare readouts while holding urate constant.
3. Compare immediate-release and extended-release exposure with matched parent/metabolite pharmacokinetics. If GSDMD engagement cannot be separated from unacceptable alcohol-response or hepatic risk, the lower-dose formulation hypothesis fails.
4. Test CP6a plus CP6b blockade directly before making an additive claim about zileuton and disulfiram.

## Related Concepts

- [[nlrp3-inflammasome|NLRP3 Inflammasome]] — The general pathway
- [[gasdermin-d|Gasdermin D]] — The specific target
- [[gout|Gout Flare Cascade]] — The disease mechanism
- [[dapansutrile|Dapansutrile (OLT1177)]] — NLRP3 inhibitor; Phase 2a completed in gout (PMID 33005902)
