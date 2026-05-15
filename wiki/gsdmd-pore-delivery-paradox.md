---
title: GSDMD Pore Self-Delivery Paradox
date: May 2026
tags:
  - gsdmd
  - gasdermin
  - pyroptosis
  - drug-delivery
  - nlrp3
  - cp6b
  - caspase-1
  - cp4
  - novel-mechanism
related:
  - nlrp3-exploit-map.md
  - gout-kill-chain-delivery-routes.md
  - nlrp3-inflammasome.md
sources:
  - "bioRxiv Feb 2025 — caspase inhibitor delivery through GSDMD pores (https://www.biorxiv.org/content/10.1101/2025.02.11.637513v1.full)"
  - "PNAS 2018 — Ac-FLTD-CMK GSDMD-derived blocking peptide"
  - "Nature Immunology 2020 — disulfiram modifies GSDMD Cys191"
status: published
---

# GSDMD Pore Self-Delivery Paradox

A February 2025 bioRxiv preprint describes a delivery mechanism that has not been incorporated into any gout pharmacology or drug delivery program: once gasdermin D pores form in the plasma membrane of a pyroptotic cell, those pores become passive delivery conduits for membrane-impermeant compounds that would otherwise be unable to enter the cell.

The inflammatory cell's own exit pore is the drug delivery portal.

---

## The mechanism

Gasdermin D (GSDMD) is cleaved by activated caspase-1 (or caspase-4/5/11). The cleaved N-terminal fragment oligomerizes into pores in the plasma membrane. These pores have an **inner diameter of 10–20 nm** — wide enough for:

- Small molecules (< 1 kDa): easy passage
- Peptides (1–5 kDa): passage demonstrated
- Nanobodies (~12–15 kDa): at the upper limit; passage likely for flexible structures
- Full-size antibodies (~150 kDa): too large

Under normal conditions, the plasma membrane is a selective barrier. Many pharmacologically active compounds — charged peptides, certain caspase inhibitors, hydrophilic small molecules — are membrane-impermeant: they can be present in the extracellular fluid at therapeutic concentrations but cannot cross an intact plasma membrane to reach their intracellular target.

Once GSDMD pores form, that barrier is breached locally. Membrane-impermeant compounds in the surrounding extracellular fluid passively diffuse through the pores into the cell.

The 2025 preprint demonstrates this specifically for caspase inhibitors: membrane-impermeant caspase inhibitors enter GSDMD-pore-expressing cells at higher rates than cells with intact membranes. The pore-expressing cells become selectively more permeable to these compounds. (In Vitro — preprint, not yet peer-reviewed)

---

## Why this matters for gout

The gout flare involves a cascade where caspase-1 and GSDMD are co-activated in the same cell at the same time:

```
CP4: Caspase-1 activated → cleaves pro-IL-1β, pro-IL-18, and GSDMD simultaneously
CP6b: GSDMD N-terminal fragment → plasma membrane pore formation
```

These are not sequential — they happen in the same cell within the same brief window. Caspase-1 cleaves GSDMD; GSDMD pores then form. The pores appear during the same time window that caspase-1 is still active.

**The delivery implication:**

A membrane-impermeant caspase-1 inhibitor present in the synovial fluid at the moment GSDMD pores form can now enter the macrophage through those pores and inhibit caspase-1 before it cleaves all its substrate.

Specifically relevant compounds:
- **Ac-FLTD-CMK** — a GSDMD-derived octapeptide inhibitor (PNAS 2018, Rathkey et al.) that selectively blocks GSDMD cleavage sites and caspase-1 activity. This compound is membrane-impermeant under normal conditions — it cannot cross an intact plasma membrane to reach intracellular caspase-1. Through GSDMD pores, it can. This converts Ac-FLTD-CMK from a research tool with no cell-permeability into a potential self-targeted therapeutic at the exact moment it's needed.
- **Z-YVAD-FMK** class caspase-1 inhibitors — peptidic, poorly cell-permeable, currently used as research tools rather than drugs for this reason. GSDMD pores could change the delivery calculus for this entire compound class.
- **VX-765 (belnacasan)** — oral prodrug, converts to VRT-043198 (caspase-1 inhibitor). VRT-043198 is designed for cell permeability, so the pore-delivery effect is less critical here. But the pore phenomenon would still enhance intracellular concentration of the active metabolite in pyroptotic cells specifically.

---

## The paradox, precisely stated

The paradox has two faces:

**Face 1 — Therapeutic window:** The compounds that most need intracellular delivery (membrane-impermeant caspase/GSDMD inhibitors) gain access precisely at the moment their target is most active. The activation of the target creates its own delivery mechanism.

**Face 2 — Race condition:** IL-1β exits through the same pores that drugs enter. Once pores form, there is a race: membrane-impermeant circuit-breakers diffuse in; IL-1β, IL-18, and other cytosolic contents leak out. The earlier the drug reaches the extracellular space around pore-forming cells (i.e., the more drug is already present in the synovial fluid), the faster the race is won.

This race condition means that prophylactic or early-flare dosing matters more than acute intervention at peak flare. If the drug is already present in the joint fluid when the first macrophages begin pyroptosis, the self-delivery mechanism captures the earliest pore-forming cells — before IL-1β amplification has cascaded.

---

## Implications for OE platform

The OE stack currently addresses CP6b via:
- Disulfiram / DMF (oral, Cys191 covalent modification — prevents GSDMD oligomerization)
- Lactoferrin (oral kojied, mitophagy-mediated upstream prevention — PINK1/Parkin pathway)

These are prevention-oriented: they work by stopping GSDMD from forming pores in the first place. The pore self-delivery mechanism is a *response*-oriented complement: useful once pores are already forming, as a circuit-breaker.

For the OE platform specifically, there is a potential engineered application: if koji-derived compounds or peptides can be formulated to reach the synovial fluid and are membrane-impermeant under baseline conditions, the pore self-delivery mechanism selectively concentrates them in the most active pyroptotic cells. A compound that is otherwise too hydrophilic or charged to enter cells passively becomes self-targeted during the flare. This is speculative but mechanistically grounded. (Mechanistic Extrapolation)

---

## What this page does NOT claim

1. This is based on a **preprint** (bioRxiv February 2025). It has not been peer-reviewed as of May 2026. The mechanism is plausible and the in vitro data is described — but load-bearing numbers (exact pore sizes, exact passage rates for specific compounds) should be verified against the primary preprint before any downstream reasoning depends on them.

2. The therapeutic window implication — that membrane-impermeant inhibitors can be self-delivered through GSDMD pores in vivo, in a live joint, during an acute gout flare — is **Mechanistic Extrapolation**. The preprint demonstrates the phenomenon in cell culture. Translation to in vivo joint pharmacokinetics involves additional variables (drug stability in synovial fluid, joint fluid turnover rate, competition with IL-1β efflux, pore kinetics in primary vs. cell-line macrophages).

3. **No drug development program in any disease** has been designed around this delivery mechanism as of May 2026. This is genuinely novel territory — a research opportunity, not an established approach.

---

## Where this fits in the kill chain

```
CP4 (Caspase-1) ←── GSDMD pores allow membrane-impermeant
         ↓              caspase inhibitors to enter during
CP6b (GSDMD)  ──→    the same activation window
```

The pore self-delivery mechanism creates a pharmacological shortcut between CP6b (the point at which delivery is enabled) and CP4 (the target that becomes newly accessible). In the kill chain framing: hitting CP6b pharmacologically (preventing GSDMD pore formation) and exploiting CP6b mechanistically (using pore formation as a delivery route) are two distinct strategies. The OE stack currently only considers the former.

---

## Broader relevance beyond gout

GSDMD-mediated pyroptosis drives pathology in:
- Sepsis (macrophage pyroptosis → cytokine storm)
- ARDS / COVID-19 (alveolar macrophage pyroptosis)
- Atherosclerosis (macrophage foam cell pyroptosis in plaques)
- NASH / liver disease (hepatocyte pyroptosis)
- Cryopyrin-associated periodic syndromes (CAPS)

The pore self-delivery paradox is disease-agnostic — it applies wherever GSDMD is the terminal effector of inflammasome activation. Any membrane-impermeant compound targeting a molecule co-active with GSDMD (caspase-1, caspase-4/5, gasdermin family members) becomes more deliverable in any of these contexts through the same mechanism.

This makes the delivery paradox a platform insight, not a gout-specific one. Gout is the immediate OE application but the intellectual territory is wider.

---

## Open questions

1. **Pore kinetics vs. IL-1β efflux kinetics:** Which is faster — drug influx through GSDMD pores or IL-1β efflux? This determines how much of the therapeutic race can actually be won. Not characterized in the preprint.

2. **Primary macrophage vs. cell line:** The preprint uses cell line data. Do primary human synovial macrophages show the same pore self-delivery effect? Unknown.

3. **Compound size limit in practice:** The 10–20 nm pore inner diameter is the structural upper bound. What is the practical permeability limit for globular peptides vs. linear peptides vs. small molecules through the pore under physiological conditions? Not characterized.

4. **Pore lifetime:** GSDMD pores can be repaired by membrane shedding (ESCRT machinery) or persist until cell lysis. How long does the delivery window last? Minutes to tens of minutes — the timeline matters for whether a drug circulating in synovial fluid can accumulate intracellularly before the cell lyses.

5. **First gout-relevant compound to test through pores:** Ac-FLTD-CMK is the most structurally interesting candidate (GSDMD-derived, selectively targets the same protein that created the pore). A cell culture experiment in LPS+MSU-stimulated primary human macrophages comparing Ac-FLTD-CMK efficacy before and after GSDMD pore formation would directly test the paradox in the gout context. This is a $2,000–5,000 experiment if a wet-lab partner has the MSU stimulation setup.
