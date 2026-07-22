---
title: Thymulin
aliases:
  - FTS
  - facteur thymique sérique
  - serum thymic factor
  - thymulin acetate
  - metFTS
related:
  - nlrp3-inflammasome
  - nlrp3-exploit-map
  - peptide-gout-addendum
  - kpv-peptide
  - gout
sources:
  - peptide-gout-addendum.md
  - nlrp3-exploit-map.md
  - validation-experiments.md
tags:
  - thymulin
  - peptides
  - NF-κB
  - CP1a
  - NLRP3
  - inflammaging
  - myeloid
status: published
---

# Thymulin

Thymulin is a zinc-dependent thymic nonapeptide whose **gout-relevant weakness it might exploit is NF-κB priming (Chokepoint 1a)** — the transcriptional arm that produces pro-IL-1β and NLRP3 itself. A 2026 *Nature Communications* study is the first to show, in macrophages and with human cells, that thymulin inhibits canonical NF-κB signalling and suppresses the exact cytokine set (IL-1α, IL-1β, IL-6, TNF-α) that drives the gout flare. The result was obtained in an aging/cancer-immunology context, not a gout model, so the gout application is mechanistic extrapolation at the priming node — but it is now anchored by direct macrophage and human-cell evidence rather than inference from adjacent inflammation models.

**Sequence:** H-Pyr-Ala-Lys-Ser-Gln-Gly-Gly-Ser-Asn-OH (pyroglutamyl nonapeptide). Biological activity requires bound zinc; the zinc-free (apo) peptide is inactive, and circulating thymulin activity declines with age. (In Vitro; Kanemaru et al. 2026, *Nat Commun* 17:6534, [DOI 10.1038/s41467-026-75383-0](https://doi.org/10.1038/s41467-026-75383-0))

## Mechanism of Action — Gout-Axis Summary

### NF-κB priming inhibition (Signal 1 / Chokepoint 1a)

In aged bone-marrow-derived macrophages (BMDMs), thymulin treatment **inhibited NF-κB p65 DNA-binding activity in nuclear extracts** and **decreased LPS-induced phosphorylation of IκBα** — i.e. it holds NF-κB inactive in the cytoplasm rather than acting downstream. A gain/loss-of-function luciferase reporter closed the loop: thymulin suppressed LPS-induced NF-κB-dependent reporter activity, and **mutation of the NF-κB binding site abolished the effect**, establishing that the cytokine suppression runs specifically through NF-κB. (In Vitro; Kanemaru et al. 2026, Fig. 6i–k)

This places thymulin at **CP1a** alongside [KPV](./kpv-peptide.md) and TB-500 in the [NLRP3 Exploit Map](./nlrp3-exploit-map.md). What distinguishes the thymulin evidence from most CP1a entries is that the NF-κB block is demonstrated directly in the gout effector cell (the macrophage), with a binding-site-mutation control, rather than inferred from a functional cytokine readout alone.

### Pro-inflammatory cytokine suppression (output node)

Thymulin lowered IL-1α, IL-1β, IL-6, and TNF-α across three systems: aged BMDMs (In Vitro, ELISA), aged mouse circulating myeloid cells (Animal Model), and — the point that raises this above the older rodent-only thymulin literature — **human peripheral blood mononuclear cells** (In Vitro, ex vivo). These are the same cytokines targeted by IL-1-axis biologics used in refractory gout, so the output node is mechanistically aligned; the trigger in every experiment was LPS or the aging state, never MSU crystals. (In Vitro + Animal Model; Kanemaru et al. 2026)

### Age-dependence

The anti-inflammatory effect was present in aged animals and essentially absent in young ones, tracking the age-related decline in endogenous thymulin. Aged myeloid cells in both mice and humans upregulate inflammasome components (NLRP3, PYCARD/ASC) as part of their pro-inflammatory signature (single-cell, Fig. 2g). Because gout incidence rises steeply with age, an intervention whose activity is restricted to aged myeloid cells is demographically aligned with the target population rather than a liability. (Animal Model + human single-cell; Kanemaru et al. 2026)

## What the 2026 paper does *not* establish for gout

1. **No MSU-crystal trigger.** Every anti-inflammatory readout used LPS or the aging state. Whether thymulin blunts urate-crystal-initiated priming (the CP0 C5a/ROS route and the CP1a transcriptional route in a gout context) is untested.
2. **Priming only — not assembly or caspase-1.** The paper demonstrates Signal-1 (NF-κB) inhibition. It does not show thymulin blocks NLRP3 oligomerization (CP2), ASC speck assembly (CP3), or caspase-1 (CP4), and did not measure mature secreted IL-1β from a crystal stimulus. Reduced priming lowers pro-IL-1β and NLRP3 substrate, which is a plausible route to a smaller flare, but that is a hypothesis, not a measured gout outcome.
3. **Immunomodulatory context.** The paper's therapeutic thrust is enhancing antitumor T-cell immunity and sensitizing tumors to anti-PD-L1 therapy in aged hosts. A peptide that tunes systemic myeloid and T-cell immunity carries different safety considerations from a locally-acting inflammasome or IL-1 intervention; those considerations are unexamined for a gout indication.

## Sourcing & Delivery

Thymulin is a nine-residue peptide requiring stoichiometric zinc for activity; native circulating half-life is short. In the 2026 study, active dosing was **thymulin acetate 1.5 mg/kg co-administered with an equimolar concentration of ZnCl₂, intraperitoneally, daily, continued for 4 weeks and tolerated** (control animals received ZnCl₂ alone). (Animal Model; Kanemaru et al. 2026, Methods) The zinc-loading requirement is thus a solved formulation detail in the preclinical setting rather than an open problem. A metabolically stabilized synthetic analog (metFTS) has been described in the earlier thymulin literature and is the more plausible starting point than the native peptide for any translational route; oral and gut-luminal delivery of a zinc-dependent nonapeptide has not been demonstrated and would be the delivery gate for any Open Enzyme fermentation or barrier-restricted framing.

## Evidence Level

| Claim | Tier | Source |
|---|---|---|
| Thymulin inhibits NF-κB p65 DNA-binding + IκBα phosphorylation in aged macrophages; effect is NF-κB-binding-site-dependent (reporter) | In Vitro | Kanemaru 2026 Fig. 6i–k |
| Suppresses IL-1α/IL-1β/IL-6/TNF-α in human PBMCs (ex vivo) | In Vitro | Kanemaru 2026 |
| Suppresses pro-inflammatory cytokines in aged mouse myeloid cells in vivo; effect age-dependent | Animal Model | Kanemaru 2026 |
| Enhances antitumor T-cell immunity; sensitizes tumors to anti-PD-L1 (age-dependent) | Animal Model | Kanemaru 2026 |
| Any effect on MSU-crystal-driven priming, inflammasome assembly, caspase-1, or a gout flare | Mechanistic Extrapolation | no direct evidence |

## Falsification Gate

The single experiment that would advance or kill the gout hypothesis: **aged human (or mouse) macrophages primed with MSU crystals ± thymulin (+ Zn²⁺), reading out mature secreted IL-1β and cleaved caspase-1**, with an LPS+MSU positive control and a young-donor arm to test the age-dependence. The full tiered protocol is registered as [§1.44 (THY-1)](./validation-experiments.md#144-thymulin--msu--nlrp3-in-aged-macrophages-thy-1--age-stratified-priming-to-flare-test); it is age-stratified because thymulin's effect is age-dependent, and it fits the existing MSU-stimulated-macrophage assay family already used in the corpus (§1.17; androgen×MSU×NLRP3 screen §1.23). If thymulin's NF-κB priming block translates to reduced crystal-driven IL-1β in aged macrophages, thymulin graduates from a CP1a mechanistic-extrapolation entry to a gout-validated priming inhibitor. If mature IL-1β is unchanged despite priming suppression, the priming-only limitation is confirmed and thymulin stays a systemic-immunomodulation hypothesis, not a flare intervention.

## Related Concepts

- [NLRP3 Inflammasome](./nlrp3-inflammasome.md) — the cascade and chokepoint vocabulary
- [NLRP3 Exploit Map](./nlrp3-exploit-map.md) — CP1a NF-κB priming node and full compound catalog
- [Peptides & Gout Addendum](./peptide-gout-addendum.md) — comparator peptides (KPV, TB-500, BPC-157)
- [KPV Tripeptide](./kpv-peptide.md) — the closest CP1a peptide analog

---

*Research-stage analysis. Phase 0 — Research & Design. Not medical advice.*
