---
title: "KPV Self-Delivery Through GSDMD Pyroptotic Pores vs. the PepT1 Baseline — Computational Analysis (comp-042)"
date: 2026-07-13
tags:
  - computational
  - comp-042
  - kpv
  - gsdmd
  - pyroptosis
  - drug-delivery
  - pept1
  - slc15a1
  - nlrp3
  - selectivity
  - gout
related:
  - gsdmd-pore-delivery-paradox.md
  - kpv-peptide.md
  - computational-experiments.md
  - validation-experiments.md
  - delivery-route-matrix.md
  - nlrp3-inflammasome.md
sources:
  - "Dalmasso G et al. Gastroenterology 2008;134(1):166-78 (PMID 18061177, DOI 10.1053/j.gastro.2007.10.026) — PepT1-mediated KPV uptake; NF-κB inhibition at nanomolar KPV; Km 160 µM (Caco2) / 700 µM (Jurkat)"
  - "Xia S et al. Nature 2021;593:607-611 (PMID 33883744, DOI 10.1038/s41586-021-03478-3) — GSDMD pore cryo-EM: 33-subunit, ~21.5 nm inner diameter, negatively-charged conduit, cationic-cargo electrostatic filtering"
  - "Sborgi L et al. EMBO J 2016;35(16):1766-78 (PMID 27418190, DOI 10.15252/embj.201694696) — GSDMD pore AFM ring diameter 21.2 ± 5.6 nm"
  - "Viennois E et al. Cell Mol Gastroenterol Hepatol 2016;2(3):340-357 (PMID 27458604, DOI 10.1016/j.jcmgh.2016.01.006) — PepT1-mediated KPV in inflamed-tissue macrophages"
status: complete (v1; peer-reviewed; verdict YELLOW-provisional)
---

# KPV Self-Delivery Through GSDMD Pores vs. the PepT1 Baseline (Computational, comp-042)

> **Frozen analysis lives at [`./etc/experiments/comp-042-kpv-gsdmd-pore-influx/`](./etc/experiments/comp-042-kpv-gsdmd-pore-influx/) — README + analyze.py + inputs/ + outputs/ all committed for reproducibility.**
> Stdlib-only Python 3; deterministic given RNG seed 42; runs in ~1 s.

## The question

The [GSDMD pore self-delivery paradox](./gsdmd-pore-delivery-paradox.md) proposes a "Trojan-horse" delivery mechanism: during a gout flare, pyroptotic macrophages open GSDMD pores (~20 nm inner diameter), and membrane-impermeant anti-inflammatory payloads flood **selectively** into exactly the dying cells driving the flare. [KPV](./kpv-peptide.md) (Lys-Pro-Val; inhibits intracellular NLRP3 assembly + NF-κB priming) is proposed as the ideal payload.

comp-042 stress-tests that thesis **for KPV specifically**. Two assumptions are load-bearing:

- **A1 — flux sufficiency:** over a pore's short open lifetime (1–30 min), does enough KPV diffuse in to clear its intracellular IC50 (~10 nM)?
- **A2 — selectivity over the PepT1 baseline (the quietly weak one):** KPV **already** enters cells — including immune cells — via the **PepT1 transporter (SLC15A1)**, independent of any pore. So the pore only confers *selectivity* if it delivers meaningfully MORE than PepT1 already does, AND healthy (non-pyroptotic) cells don't already admit KPV via PepT1. The crux is **synovial-macrophage PepT1 expression**.

The real decision-question is **not** "can KPV fit through a 15 nm pore" (trivially yes — KPV is ~1 nm). It is: **does the pore route beat the PepT1 route KPV already has, and is there a real pyroptotic-vs-healthy selectivity margin?**

## Verdict

**YELLOW (provisional).** The transport physics of self-delivery is sound; the KPV-specific *selective*-Trojan-horse rationale is not supported. Split three ways:

| Claim | Verdict | Why |
|---|---|---|
| **(a) KPV as a *selective* Trojan-horse payload** | **Effectively falsified** | KPV has a constitutive transporter route (PepT1) in the very cells that matter; the pore adds no demonstrable selectivity, and a PD timing mismatch (below) means pore-delivery arrives after KPV's upstream target has fired. |
| **(b) KPV *reaches therapeutic intracellular levels* via the pore** | **GREEN (intra-articular); marginal (SC); RED (oral)** | A ~20 nm pore equilibrates intracellular [KPV] to extracellular within ~2 s. IA clears the 10 nM IC50 by ~4 orders of magnitude. |
| **(c) The *platform* thesis — pore delivery of a transporter-orphan, membrane-impermeant payload** | **Genuinely open** | The physics that makes (b) work applies to any small membrane-impermeant molecule; the selectivity failure is specific to KPV's transporter, not to the pore. |

Provisional because the favorable read rests on ≥3 compounding named assumptions (pores/cell ≥ ~10; design-space SC/oral synovial PK; the synovial-macrophage PepT1 scenario band).

## Why this matters

The paradox page lists KPV among the payloads that "fall in or near the permissive [pore] size window" and frames KPV as a strong Trojan-horse candidate. comp-042 shows the size-window framing is the wrong lens for KPV: KPV clears the size window by a factor of ~15–40 in radius, so passage is never in doubt — but **selectivity, the actual selling point of the paradox, is undermined by the one property that makes KPV attractive as an oral drug: it already has a transporter.** This is a genuine stress-test result, not a decoration of the thesis.

## Method summary (transport / mass-balance — no MD, no docking)

- **Per-pore diffusive permeability** of a short cylindrical aperture, *including two-sided access (convergence) resistance* (Hall/Hille): `p_pore = H·D·π·r²/(L + π·r/2)`. The access term (`π·r/2` ≈ 15.7 nm at r=10 nm) dominates the channel term (`L` ≈ 7 nm), so this is an **access-resistance-limited** pore and the exact channel length is low-sensitivity. Steric-electrostatic hindrance `H ≈ 1`: KPV's ~0.5 nm radius is 20–40× smaller than the pore radius, and the pore conduit is negatively charged and electrostatically favors KPV's **+1** charge (Xia 2021).
- **Cell equilibration:** the macrophage is treated as a well-mixed compartment; intracellular [KPV] approaches extracellular with time constant `τ_eq = V_cell/(N_pores·p_pore)`, peak `C_in = C_ext·(1 − exp(−τ_life/τ_eq))`.
- **PepT1 baseline** (present in both cells): healthy-cell steady state `C_in,healthy = C_in_max·C_ext/(Km + C_ext)` with `C_in_max = AR_lin·Km`, where `AR_lin` (the linear-regime accumulation ratio) encodes the *unknown* synovial-macrophage PepT1 expression across four scenarios (absent / low / moderate / high-concentrative). In the pyroptotic cell the huge pore conductance short-circuits PepT1 (and the membrane potential), clamping `C_in,pyroptotic = C_ext`.
- **Selectivity** `S = C_in,pyroptotic / C_in,healthy = (Km + C_ext)/C_in_max`.
- **Three routes** — intra-articular (IA), subcutaneous (SC), oral — each with a synovial [KPV] (IA computed from dose/synovial-volume; SC/oral are named PK assumptions).
- **20,000-sample Monte Carlo** over all uncertain parameters for the [KPV]/IC50 distributions and P(clear IC50); deterministic robustness sweep over pore lifetime × pores/cell.

## Key results

### The core physics: the cell equilibrates in seconds

At central parameters (200 pores, 3000 µm³ macrophage, 20 nm pore), the per-pore permeability is **6.9 × 10⁻¹⁸ m³/s** and the equilibration time constant is **τ_eq ≈ 2.2 s** — far shorter than the minutes-scale pore lifetime. So intracellular [KPV] reaches essentially 100% of the extracellular (synovial) value. The naive "moles-in-over-lifetime ÷ cell volume" estimate overshoots C_ext by ~140× (it assumes a fixed gradient that never builds up), which simply confirms the cell **saturates**: peak intracellular [KPV] is **capped at the synovial [KPV]**.

**This quantitatively answers [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md) Open Question #4** ("Pore lifetime… minutes to tens of minutes — the timeline matters for whether a drug can accumulate intracellularly before the cell lyses"): for a small solute like KPV, even the *short* end of the lifetime range is orders of magnitude longer than needed. Lifetime is not the binding constraint. (Mechanistic Extrapolation, in silico.)

### Metric 1 — peak intracellular [KPV] ÷ IC50 (flux sufficiency, A1)

| Route | synovial [KPV] | intracellular [KPV] | ÷ IC50 (10 nM) | P(clear IC50) | A1 |
|---|---|---|---|---|---|
| Intra-articular | ~292 µM | ~292 µM | **~29,000×** | 1.00 | **GREEN** |
| Subcutaneous | ~30 nM | ~30 nM | **~3×** | 0.68 | YELLOW (assumption-limited) |
| Oral | ~1 nM | ~1 nM | **~0.1×** | 0.04 | **RED** |

Because the IC50 is nanomolar, the flux bar is trivially cleared by any route that reaches even nanomolar synovial [KPV] — which is exactly why **selectivity, not flux, is the real decision variable.** SC's ~3× margin sits inside the IC50-proxy's own uncertainty (see Limitations), so SC is better described as *assumption-limited* than confidently therapeutic.

### Metric 2 — selectivity ratio over the PepT1 baseline (A2)

`S` = intracellular[pyroptotic] ÷ intracellular[healthy], across the four synovial-macrophage PepT1 scenarios:

| Route | PepT1 absent | low (AR 0.3) | moderate (AR 1) | high (AR 3) |
|---|---|---|---|---|
| Intra-articular | ∞ | 4.7× | 1.4× | 0.47× |
| Subcutaneous | ∞ | 3.3× | 1.0× | 0.33× |
| Oral | ∞ | 3.3× | 1.0× | 0.33× |

Meaningful selectivity (≥3×) survives **only** in the "PepT1 absent/low" scenarios. If synovial macrophages express functional PepT1 at moderate/high levels, selectivity collapses to ~1 or **below 1 (anti-selective — healthy cells accumulate KPV *more* than pyroptotic cells)**, because a concentrative electrogenic symporter plus an intact membrane potential concentrates a +1 cation in the healthy cell, while the pyroptotic cell (Vm collapsed) only reaches C_ext. **Which scenario is real is unknown** — and functional PepT1 in immune cells is *demonstrated* (Dalmasso 2008, Jurkat), making "absent" the least likely. The table is, if anything, **optimistic** (see Limitations: the healthy-cell curve is a heuristic ceiling, so true S ≤ tabulated).

### Metric 3 — robustness (pore lifetime × pores/cell)

The A1 (flux) verdict is robust: for **pores/cell ≥ ~10**, the cell equilibrates within any lifetime in range (τ_eq ≤ ~40 s), IA clears IC50 by ~4 orders of magnitude, and SC clears it ~3×. Only the physically implausible single-pore case is flux-limited at short lifetimes. The A2 (selectivity) verdict is robustly *unquantifiable* regardless of pore parameters — it is set by PepT1 expression, not by pore biophysics.

### Decision filter

A route passes only if it clears **both** ≥1× IC50 **and** ≥3× selectivity with the named assumptions holding. **No route passes.** IA delivers KPV superbly but at doses that flood *all* synovial cells and saturate PepT1 in healthy cells too (no pore-specific selectivity, and cellular uptake is ~10⁻⁹ of the IA dose, so extracellular KPV isn't even depleted). SC is marginal on flux and unquantifiable on selectivity. Oral fails on absolute synovial concentration.

## The two assumptions, resolved

**A1 (flux sufficiency): confirmed — trivially.** The pore is so wide relative to KPV, and equilibration so fast, that intracellular [KPV] tracks synovial [KPV] within seconds. Self-delivery to therapeutic intracellular levels works for IA (hugely) and marginally for SC.

**A2 (selectivity over PepT1): does the pore beat PepT1, and what's the evidence state?** The pore does **not** demonstrably beat the PepT1 baseline for KPV. In the linear regime (SC/oral), `S ≈ 1/AR_lin` — entirely determined by synovial-macrophage PepT1 expression. In the saturating regime (IA), the extracellular concentration is so high that healthy cells are flooded via PepT1 anyway. **The state of synovial-macrophage PepT1 evidence:** functional PepT1-mediated KPV uptake is *demonstrated in immune cells generally* (Jurkat T cells; Dalmasso 2008) and KPV-nanoparticle programs explicitly target inflamed-tissue macrophages via PepT1 (Viennois 2016; recent colitis-nanoparticle work) — but **no study quantifies PepT1 (SLC15A1) expression or function in synovial-joint macrophages, resting or MSU-activated.** That single missing datum gates the entire selectivity question.

## Limitations (peer-review-incorporated)

The following were surfaced by an independent adversarial peer review of the analysis and are load-bearing for how far the verdict travels:

1. **PD timing mismatch (the deepest conceptual gap).** This is a *transport* model. KPV is an **upstream** inhibitor — it blocks NLRP3 inflammasome *assembly* and NF-κB *priming*. GSDMD pores open **downstream** of inflammasome firing (caspase-1 has already cleaved GSDMD and pro-IL-1β). So even perfectly selective pore-delivery imports KPV into a cell where its target has *already acted* and IL-1β has *already been released*. The pore selects for cells where an upstream inhibitor is too late. The paradox page's own "Face 2 — race condition / prophylactic dosing matters more than acute" logic applies and is not captured by the transport math. This is the mechanistic reason the KPV-selective-Trojan-horse claim is *falsified*, not merely *unquantified*.
2. **The healthy-cell selectivity curve is optimistic.** `C_in,healthy = C_in_max·C_ext/(Km+C_ext)` is a heuristic saturating *ceiling*, describing rate saturation, not the equilibrium intracellular concentration. A genuinely equilibrating transporter gives `C_in,healthy → C_ext` (S → 1); an electrogenic H⁺-coupled/concentrative PepT1 plus the intact-cell membrane potential (Vm −50 to −70 mV; Nernst factor ~7–14× for a +1 cation) gives `C_in,healthy > C_ext` (S < 1). **True selectivity is ≤ the tabulated values, especially at IA.** (Conversely, Vm collapse in the pyroptotic cell is exactly why `C_in,pyroptotic` is correctly capped at C_ext with no Nernst boost.)
3. **No membrane-potential / Donnan term** is modeled explicitly for the healthy cell; the "high" PepT1 scenario (AR 3) likely *understates* the anti-selective tail for an electrogenic symporter.
4. **No mass-balance sink.** A single pyroptotic cell absorbs ~C_ext·V ≈ 9 × 10⁻¹⁶ mol vs a ~5.8 × 10⁻⁷ mol IA dose (~10⁻⁹); even 10⁶ cells capture ~0.1%. Cellular uptake does not deplete extracellular KPV, so the pore creates **no tissue-level selectivity/sparing** at IA doses.
5. **The IC50 is an extracellular reporter value** (10 nM, in a PepT1⁺ Caco2 line) that already convolves transport + intracellular potency. Comparing it to an intracellular concentration in a Vm-collapsed pyroptotic cell may understate the true intracellular target-engagement threshold by several-fold — which is why SC's 3× margin is best read as assumption-limited.
6. **Intracellular KPV degradation is unmodeled (a selectivity lever, not just a caveat).** A payload that is rapidly degraded intracellularly needs *sustained high flux* to maintain effect — which only the open pore can supply — making such a payload *more* pore-selective. KPV's "resistance to significant enzymatic degradation" ([`kpv-peptide.md`](./kpv-peptide.md)) is therefore **anti-selective**: a PepT1⁺ healthy cell that takes up KPV also *retains* it. The ideal Trojan-horse payload is transporter-orphan **and** intracellularly labile — KPV is neither.
7. **Design-space PK.** SC and oral synovial [KPV] are named assumptions (KPV systemic PK is poorly characterized); the pores/cell count is a named assumption (no published per-cell count); well-mixed is marginal (diffusive mixing τ ~0.4 s vs τ_eq ~2 s — conservative). None of these change the qualitative conclusions.

**Single biggest limitation.** Empirically: **synovial-macrophage PepT1 (SLC15A1) expression is uncharacterized** — it is the sole determinant of whether the pore beats KPV's constitutive import route. Conceptually: the **PD timing mismatch** (upstream inhibitor delivered downstream of firing) undercuts the therapeutic logic even if selectivity existed.

## Impact on experimental priorities

**This reframes the proposed [`validation-experiments.md`](./validation-experiments.md) §1.32 KPV wet-lab (fluorescent-KPV uptake → IL-1β efficacy) rather than simply green-lighting or killing it:**

- **It KILLS the "KPV as the ideal *selective* Trojan-horse payload" framing.** The experiment as originally framed — fluorescent-KPV uptake in pore-forming vs. intact macrophages — is **confounded by PepT1**: a positive uptake signal cannot distinguish pore-delivery from constitutive PepT1 uptake, and even a clean selective-uptake result doesn't rescue the therapeutic logic given the timing mismatch.
- **It GREEN-LIGHTS a *redesigned* delivery test** that isolates the pore contribution: run fluorescent-KPV uptake **± a PepT1 inhibitor / in PepT1-knockdown cells**, and — decisively — pair it with a **transporter-orphan membrane-impermeant fluorophore** (e.g., a charged dextran/tracer with no peptide transporter) as the true pore-selectivity probe. That probe is the clean test of the *platform* thesis (verdict (c)), which comp-042 leaves genuinely open.
- **Sequencing:** the platform-thesis delivery test (transporter-orphan tracer, ± pore induction via low-dose nigericin) is the cheaper, more informative first experiment — matching the Tier-1 delivery-readout precursor already noted on the [paradox page](./gsdmd-pore-delivery-paradox.md#open-questions). Gate any KPV-specific efficacy work behind it, but recognize KPV is the wrong molecule to *prove the concept* with.

In short: comp-042 shifts §1.32 from "test whether KPV self-delivers selectively" (mis-specified) to "test whether a transporter-orphan impermeant payload self-delivers selectively, and use KPV only as an anti-inflammatory that happens to also enter pyroptotic cells."

## Cross-references

- [GSDMD pore self-delivery paradox](./gsdmd-pore-delivery-paradox.md) — the thesis under test; Open Question #4 (pore lifetime) is answered here.
- [KPV tripeptide](./kpv-peptide.md) — payload properties; PepT1 uptake; enzymatic-resistance claim (which cuts anti-selective here).
- [Computational experiments index](./computational-experiments.md) — comp-042 registry entry.
- [Validation experiments](./validation-experiments.md) — §1.32 wet-lab, reframed by this analysis.
- [Delivery route matrix](./delivery-route-matrix.md) — where pore-delivery sits among compound-class × route options.

## Evidence summary

- **Mechanistic Extrapolation (in silico)** — all comp-042 outputs (permeability, τ_eq, [KPV]/IC50, selectivity ratios, verdicts) are transport-model predictions over published anchor values.
- **In Vitro** — KPV NF-κB IC50 (~10 nM) and PepT1 Km (160/700 µM) (Dalmasso 2008); GSDMD pore geometry (Sborgi 2016 AFM; Xia 2021 cryo-EM).
- **Named gap** — synovial-macrophage PepT1 expression (no evidence tier; uncharacterized).
- **Clinical Trial** — none. No pore-delivery program exists in any disease.

## Reproduction

```bash
cd etc/experiments/comp-042-kpv-gsdmd-pore-influx
python3 analyze.py
```

Stdlib-only Python 3. Deterministic given RNG seed 42. ~1 s wall-clock.
