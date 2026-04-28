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
sources:
  - nlrp3-exploit-map.md
---

# Disulfiram (Antabuse): The Repurposed GSDMD Inhibitor

**Disulfiram** (brand name: Antabuse) is an FDA-approved drug prescribed to alcoholics as a deterrent — it causes severe flushing and illness if alcohol is consumed. In 2020, researchers discovered it has an entirely different and remarkable mechanism: **direct gasdermin D inhibition at the final step of the NLRP3 inflammasome pathway.**

This represents one of the most accessible, underrated, and economically efficient gout interventions available today.

**Repurposing surface origin:** Disulfiram is one of three concrete examples surfaced by the Open Enzyme discovery engine's chokepoint-to-FDA-drug mapping methodology — FDA-approved drugs that hit a gout chokepoint but were never clinically tested for gout. The other two are zileuton (CP6a 5-LOX, FDA-approved for asthma) and avacopan (CP0 C5aR1, FDA-approved for ANCA vasculitis). See [open-enzyme-vision.md §2.2](./open-enzyme-vision.md) for the full repurposing surface framing. (source: open-enzyme-vision.md)

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

### Safety Profile: 70+ Years of Data

Disulfiram has been prescribed for alcohol use disorder since the 1950s. Decades of clinical experience demonstrate:

- Excellent safety profile at standard doses (250 mg/day)
- No hepatotoxicity (unlike MCC950, which caused liver failure in Phase 1 RA trials)
- Well-characterized pharmacokinetics
- Extensive understanding of drug interactions

This safety history means disulfiram can move directly to gout trials without extensive new safety work.

**(Source: nlrp3-exploit-map.md)** — "It's FDA-approved. It has 70+ years of safety data. It costs ~$30/month. You can get a prescription by... having a conversation with a doctor about alcohol use disorder, or by finding a physician interested in repurposed drug applications."

## Economic Efficiency

This is the most cost-effective intervention in the entire gout pharmacopeia:

| Drug | Mechanism | Annual Cost |
|------|-----------|-------------|
| **Disulfiram** | GSDMD inhibitor | ~$120–360 (generic) |
| **Colchicine** | Microtubule/inflammasome | ~$120–250 |
| **Allopurinol** | Xanthine oxidase inhibitor | ~$12–50 |
| **Pegloticase (IV)** | Recombinant uricase | ~$100,000+ per course |
| **Dapansutrile** (Phase 3) | NLRP3 inhibitor | Unknown (likely $200–500/month) |
| **Canakinumab** | Anti-IL-1β monoclonal | ~$300,000/year (uninsured) |

Disulfiram is not only effective but **extraordinarily affordable**, placing it in the same price tier as current standard-of-care flare prevention.

## Practical Implementation

### Getting a Prescription

Disulfiram requires a prescription. Access strategies:

1. **Honest disclosure:** Work with a physician on alcohol use — even patients with mild or history of alcohol issues can receive disulfiram for that indication
2. **Repurposed indication:** A rheumatologist or forward-thinking internist willing to prescribe off-label for gout given the GSDMD mechanism
3. **Research enrollment:** Some clinical trials may test disulfiram for gout

**(Source: nlrp3-exploit-map.md)** — "You can get a prescription by... having a conversation with a doctor about alcohol use disorder, or by finding a physician interested in repurposed drug applications. This is the single most accessible pharma-grade NLRP3 pathway exploit in this entire document."

### Dosing

- **Standard (alcohol deterrent):** 250 mg once daily, typically in the morning
- **Gout prophylaxis:** Likely similar to standard dose, though formal trials are needed
- **Acute flare:** Unclear; probably prophylactic use rather than acute dosing

### Safety Considerations

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

**Dose-dependent risk profile:**
- 250 mg/day (standard): well-tolerated in alcohol-abstinent patients. Hepatotoxicity (idiosyncratic) is the main rare serious side effect; baseline + periodic LFTs recommended.
- 500 mg/day (historical dose, less common now): more side effects (drowsiness, peripheral neuropathy, hepatic stress) without proportional efficacy gain.
- Disulfiram-ethanol reaction severity scales with both disulfiram dose and ethanol exposure.

**Stack-level safety note — fermented foods:**
- **Kombucha and koji-fermented foods** may contain residual ethanol that could trigger reaction in disulfiram-sensitive patients. Practical limit: dietary intake of well-fermented foods at typical portion sizes is generally below the threshold but is patient-specific. Disulfiram users should avoid kombucha entirely and treat any koji-derived fermented foods as a per-batch ethanol-content question.
- **Home-fermented amazake / shio-koji:** wild-yeast contamination of a "failed" batch can push residual ethanol to 1–3% v/v. Disulfiram users running the [koji home-fermentation protocol](./koji-home-fermentation.md) should pre-screen every finished batch with consumer ethanol test strips (~$15, ±0.1% v/v) before consumption and discard any batch reading >0.1%. Do not rely on cook-off / volatilization — see the "Drug-interaction warning" subsection in [koji-home-fermentation.md](./koji-home-fermentation.md) for the routine precaution. (source: koji-home-fermentation.md)
- **Hepatotoxicity stacking concern with EGCG, high-dose curcumin, acetaminophen:** all four contribute to hepatic stress; layering is a relative contraindication.

(source: supplements-stack.md)

## Comparison: Disulfiram vs. Other Inflammasome Inhibitors

| Drug | Chokepoint | Class | Status | Cost | Safety Data |
|------|-----------|-------|--------|------|-------------|
| **Disulfiram** | 6b (GSDMD pore) | Approved (Rx) | Widely available | ~$30/month | 70+ years |
| **Zileuton** | 6a (5-LOX/LTB4) | Approved (Rx, asthma) | Available; off-label in gout | ~$50/month generic | 30+ years (asthma) |
| **DMF** | 6b (GSDMD) | Approved (MS) | Requires MS diagnosis | High | 15+ years (MS) |
| **Dapansutrile** | 2 (NLRP3) | Phase 3 clinical | Investigational | Unknown | <5 years |
| **Oridonin** | 1, 2 | Natural/research | Preclinical | ~$30/month | Unknown human data |
| **Colchicine** | 3 (ASC/microtubule) | Approved (Rx) | Standard of care | ~$20/month | 50+ years |

**Key insight:** Disulfiram is the only GSDMD inhibitor with both FDA approval and extensive clinical safety history. It's a uniquely accessible entry point to inflammasome modulation.

## The Black Hat Insight

**(Source: nlrp3-exploit-map.md)** — "This is the black hat's dream exploit. Disulfiram — Antabuse — the drug prescribed to alcoholics since the 1950s — was discovered in 2020 (Nature Immunology) to specifically block gasdermin D pore formation at nanomolar concentrations... It's FDA-approved. It has 70+ years of safety data. It costs ~$30/month."

Disulfiram represents a market inefficiency in medical knowledge: rheumatologists and immunologists know about NLRP3 inhibitors and GSDMD as a target, but gout specialists have not widely integrated this discovery into clinical practice. This is an underutilized tool that could be deployed immediately.

## Integration with Multi-Attack Strategy

In the context of comprehensive gout management:

- **Remove the cause:** [[engineered-koji|Engineered koji]] or [[engineered-yeast|yeast expressing uricase]] address the underlying uric acid burden
- **Defuse the bomb (upstream):** [[bhb-ketones|BHB]], [[kpv-peptide|KPV]], [[oridonin|oridonin]] suppress NLRP3 priming and assembly
- **Defuse the bomb (downstream):** **Disulfiram** blocks the final IL-1β release step
- **Heal the damage:** [[peptide-therapy|BPC-157, TB-500]] for tissue repair

Disulfiram provides a simple, affordable, well-tolerated entry point to the NLRP3 pharmacological toolkit.

## Related Concepts

- [[nlrp3-inflammasome|NLRP3 Inflammasome]] — The general pathway
- [[gasdermin-d|Gasdermin D]] — The specific target
- [[gout|Gout Flare Cascade]] — The disease mechanism
- [[dapansutrile|Dapansutrile (OLT1177)]] — The Phase 3 NLRP3 inhibitor

## Key Insight

**Disulfiram is the most economically efficient, safest, and most accessible gout pharmacotherapy targeting the NLRP3 inflammasome.** It blocks IL-1β release at the final step, preventing the inflammatory amplification that causes pain. It costs ~$30/month, has 70 years of safety data, and is available immediately with a prescription. The limitation is awareness — this repurposed drug has not yet entered rheumatology practice for gout, despite strong mechanistic rationale and exceptional economic and safety characteristics.

---

*Last updated: April 2026*
*Wiki synthesized from primary research documents*
