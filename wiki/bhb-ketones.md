---
title: Beta-Hydroxybutyrate (BHB)
aliases:
  - Ketone Body
  - BHB
  - β-Hydroxybutyrate
  - Endogenous Ketone
related:
  - nlrp3-inflammasome
  - kpv-peptide
  - gout
  - fasting-ketogenic
  - inflammasome-chokepoints
sources:
  - nlrp3-exploit-map.md
  - gout-deep-dive.md
  - peptide-gout-addendum.md
---

# Beta-Hydroxybutyrate (BHB): The Endogenous NLRP3 Inhibitor

**BHB** is a ketone body produced by the liver during fasting or nutritional ketosis. Its gout-relevant hypothesis is a tension between two effects: direct suppression of NLRP3 signaling and a transient rise in serum urate from competition for renal handling. Whether the inflammatory effect outweighs the urate effect at achievable exposure is unresolved.

> **Species-gap caveat:** Rodent NLRP3 potency does not establish human-cell potency; apply the cross-species standard in [`chembl-cross-check.md`](./etc/chembl-cross-check.md) before making dose claims.

## Mechanism: Multi-Chokepoint Direct NLRP3 Inhibition

BHB is a *specific* NLRP3 inflammasome inhibitor (not a general anti-inflammatory) that acts directly as a signaling molecule on inflammasome assembly — **independent of** AMPK, autophagy, ROS reduction, or any fasting/metabolic pathway. It hits three chokepoints from one metabolite: CP1 (NF-κB priming block), CP2 (potassium-efflux block + ASC-speck reduction), and CP4 (caspase-1 suppression). In rats on a ketogenic diet, gout flares were significantly reduced. The full mechanism, the Nature Medicine primary source, and the chokepoint map are owned by [nlrp3-exploit-map.md](./nlrp3-exploit-map.md). (Source: nlrp3-exploit-map.md)

**Overlap note (CP2 layering):** CBD, CBC, and THCV also suppress K⁺ efflux via P2X7 receptor block (CBD reduces nigericin-induced K⁺ efflux ~13% at 10 μM in THP-1 monocytes; In Vitro, Liu et al., *J Nat Prod* 2020). P2X7 sits upstream of K⁺ efflux. Stacking a P2X7-blocking cannabinoid on top of BHB hits the same chokepoint from a slightly different angle — likely diminishing returns rather than additive. For additive CP2 coverage, a mechanistically distinct inhibitor (oridonin at Cys279, beta-caryophyllene via CB2/NLRP3 direct docking) is a better layering choice than another K⁺-efflux blocker. See [Cannabinoids & Terpenes](./cannabinoids-terpenes.md). (source: cannabinoids-terpenes.md)

## The urate–inflammation tradeoff

There is an old clinical concern that ketosis **raises serum uric acid** in the short term. This is true: ketone bodies compete with uric acid for renal excretion (the URAT1 transporter handles both). In gout patients without other interventions, ketosis can trigger flares.

BHB simultaneously suppresses the inflammatory response to crystals in preclinical systems. That creates a testable tradeoff, not a resolved prophylactic conclusion. The direction may differ between an intercritical state and an active flare because the urate substrate is already high during the latter. Uric acid-lowering therapy could separate the two effects, but the combination has not established that NLRP3 suppression dominates in humans. (Mechanistic Extrapolation; source: [nlrp3-exploit-map.md](./nlrp3-exploit-map.md))

## Endogenous vs. Exogenous

### Endogenous Production (Fasting/Ketosis)

The body naturally produces BHB when carbohydrate availability is low:

- **Intermittent fasting (16:8):** Modest BHB elevation, typically 0.5–1.5 mM
- **Extended fasting (24h):** Higher BHB, 2–4 mM
- **Ketogenic diet (strict):** 1–3+ mM sustained
- **Cyclical ketosis:** Alternating keto/normal eating periods

Serum BHB levels peak 12–18 hours into a fast or after several days on a ketogenic diet.

### Exogenous Supplementation

- **BHB salts:** Calcium or sodium β-hydroxybutyrate, 5–15g/day, rapidly elevates serum BHB to 1–2 mM
- **MCT oil:** Medium-chain triglycerides metabolized rapidly to ketones, 1–2 tbsp elevates BHB moderately
- **Ketone esters:** More potent than salts, ~8–10g provides rapid BHB spike to 1+ mM

Exogenous BHB does not provide the full metabolic benefits of fasting (autophagy, etc.) but does deliver the direct NLRP3 inhibitory effect.

## Delivery routes and exposure

| Approach | BHB Level | Timeline | Side Effects | Adherence |
|----------|-----------|----------|-------------|-----------|
| **Intermittent fasting** | 0.5–1.5 mM | 12–18h per session | Hunger, hypoglycemia risk | Challenging for many |
| **Ketogenic diet** | 1–3+ mM sustained | Days to weeks | Keto flu, electrolyte issues | Requires dietary commitment |
| **BHB salt supplement** | 1–2 mM | <30 min to peak | GI upset, salty taste | Simple dosing, expensive |
| **MCT oil** | 0.5–1 mM | 1–2 hours | GI upset, loose stools | Better tolerated than salts |

## Contraindications, Drug Interactions, and Dose-Dependent Risk

**Contraindications:**
- **Active gout flare:** Ketone bodies and urate compete for renal handling; the documented transient ketotic urate rise may add inflammatory substrate during a flare. BHB has not been validated as an acute-flare intervention. (source: [gout-action-guide.md](./gout-action-guide.md))
- **Three-axis interaction during prolonged fasting (BHB × urate × cortisol):** A 24h+ fast simultaneously elevates BHB, transiently elevates urate, and engages a biphasic cortisol response. Direct human-gout evidence connecting all three arms is absent. (Mechanistic Extrapolation; source: [cortisol-fasting-glucocorticoid-inflammasome-lit-scan-2026-05-19](../logs/cortisol-fasting-glucocorticoid-inflammasome-lit-scan-2026-05-19.md))
- T1DM without close glucose monitoring (ketoacidosis risk distinct from physiological ketosis)
- Pregnancy (insufficient data on exogenous ketone safety)
- Severe hepatic disease (impaired ketone metabolism)
- Carnitine-deficiency syndromes if using MCT-based induction

**Drug interactions:**
- **SGLT2 inhibitors (canagliflozin, empagliflozin, dapagliflozin):** additive ketosis; euglycemic diabetic ketoacidosis risk in T2DM patients on these drugs.
- **Insulin / insulin secretagogues:** dietary ketosis lowers glucose requirements; dose adjustment needed to avoid hypoglycemia.
- **Acetazolamide / topiramate / zonisamide:** carbonic anhydrase inhibitors compound metabolic acidosis risk on ketogenic regimens.

**Dose-dependent risk profile:**
- 5–20g/day exogenous BHB: well-tolerated; GI upset is the main side effect (most common with ketone salts; mineral load matters).
- >30g/day or aggressive nutritional ketosis: transient serum UA rise of 5–10% (ketone bodies and urate compete for renal MCT/URAT1 reabsorption). This is the gout-relevant dose ceiling. Sustained nutritional ketosis can also produce mild hyperuricemia for the same reason.
- MCT >2 tbsp at one sitting: GI distress is the practical limiter.

**Stack interactions:**
- **Antagonism with intermittent fasting during active flares:** both ketogenic states transiently raise serum UA via competition for renal urate excretion; layering fasting on top of exogenous ketones during a flare amplifies the spike.
- **Synergy with NAC, omega-3:** BHB-driven NLRP3 inhibition (CP1–CP3) is mechanistically additive with NAC's glutathione/ROS axis (CP2) and omega-3 SPM-driven resolution (CP5).
- **No ABCG2 interaction documented.** Neutral on the gut-lumen-sink axis.

(source: supplements-stack.md)

---

## Falsification tests

1. Measure BHB, serum urate, ASC specks, caspase-1, and IL-1β across matched endogenous and exogenous exposure. The hypothesis weakens if NLRP3 target engagement appears only at exposures that materially worsen urate.
2. Test BHB with and without established urate lowering in an MSU model. This separates direct inflammatory target engagement from changes in the urate substrate.
3. Compare intercritical and active-flare conditions rather than assuming one net direction across both states.

## Related Concepts

- [[nlrp3-inflammasome|NLRP3 Inflammasome]] — The target pathway
- [[kpv-peptide|KPV Peptide]] — Another NLRP3 inhibitor (hits fewer chokepoints)
- [[oridonin|Oridonin]] — Natural NLRP3 inhibitor
- [[gout|Gout and the NLRP3 Cascade]] — The disease mechanism
