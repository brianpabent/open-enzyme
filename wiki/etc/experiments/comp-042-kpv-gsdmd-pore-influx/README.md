# comp-042: KPV self-delivery through GSDMD pyroptotic pores vs. the PepT1 baseline

**Question:** Does the physics support KPV (Lys-Pro-Val) flooding into pyroptotic macrophages through GSDMD pores fast enough to clear its intracellular IC50 (A1), and — the quietly weak assumption — does the pore confer real *selectivity* over the PepT1 route KPV already has (A2)?

**Verdict:** **YELLOW (provisional).**
- **A1 (flux sufficiency): GREEN.** A ~20 nm pore equilibrates intracellular [KPV] to the extracellular synovial concentration within **~2 seconds** (τ_eq ≪ the minutes-scale pore lifetime). Intra-articular dosing clears the 10 nM IC50 by ~4 orders of magnitude; subcutaneous marginally (~3×); oral fails on absolute synovial concentration.
- **A2 (selectivity over PepT1): unquantifiable.** Because KPV already enters cells (including immune cells — Jurkat, Dalmasso 2008) via PepT1, the pore's selectivity is gated entirely by **synovial-macrophage PepT1 expression, which is uncharacterized.** No route clears both a therapeutic AND a meaningful-selectivity threshold.

**Headline:** The transport physics of KPV self-delivery is sound, but KPV is arguably the *wrong payload to demonstrate pore-selectivity* — precisely because it has an independent constitutive import route. The Trojan-horse selectivity thesis needs a transporter-orphan, truly membrane-impermeant payload to be proven.

**Informs:** [`gsdmd-pore-delivery-paradox.md`](../../../gsdmd-pore-delivery-paradox.md) (quantitatively answers Open Question #4 on pore lifetime; stress-tests the KPV-as-ideal-payload claim); [`kpv-peptide.md`](../../../kpv-peptide.md); [`validation-experiments.md`](../../../validation-experiments.md) §1.32 (the proposed fluorescent-KPV-uptake wet-lab).

**Interpretive wiki page:** [`wiki/kpv-gsdmd-pore-influx-computational.md`](../../../kpv-gsdmd-pore-influx-computational.md)

---

## How to reproduce

```bash
cd wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx
python3 analyze.py
```

Stdlib-only Python 3 (no external packages). All inputs in `inputs/`. Outputs deterministic given RNG seed 42. ~1 s wall-clock.

---

## File index

```
comp-042-kpv-gsdmd-pore-influx/
  analyze.py                     ← diffusive-flux / mass-balance model (run this)
  README.md                      ← this file
  inputs/
    query-strategy.json          ← scope declaration (natural_product_scope: false)
    provenance.md                ← Rule-4 verification table; source + status per input
    kpv_properties.json          ← MW, charge, radius, D_aq, enzymatic-resistance note
    pore_geometry.json           ← GSDMD inner diameter, length, count, lifetime
    macrophage_geometry.json     ← cell volume, surface area
    pept1_and_ic50.json          ← PepT1 Km, expression scenarios, KPV NF-κB IC50
    route_concentrations.json    ← IA / SC / oral synovial [KPV]
  outputs/
    central_results.json         ← deterministic central pass (permeability, τ_eq, per-route)
    monte_carlo.json             ← 20k-sample distributions of [KPV]/IC50 + P(clear)
    selectivity_grid.json        ← route × PepT1-scenario selectivity table (A2)
    robustness_sweep.json        ← lifetime × pores/cell grid (M3)
    verdicts.json                ← per-route A1/A2/combined + overall
    summary.md                   ← human-readable summary (auto-generated)
```

---

## Model (transport / mass-balance only — no MD, no docking)

Per-pore permeability of a short wide aperture **including access (convergence) resistance**:

```
p_pore = H · D · π · r_p² / (L_pore + π·r_p/2)          [m³/s]
```

- `H ≈ 1`: KPV radius (~0.5 nm) is 20–40× smaller than the pore radius; the negatively-charged conduit favors KPV's +1 charge (Xia 2021). Steric hindrance ≈ 1.
- The access term `π·r_p/2` (~15.7 nm at r_p=10 nm) dominates the channel term `L_pore` (~7 nm) → access-resistance-limited pore.

Cell equilibration (well-mixed compartment):

```
τ_eq   = V_cell / (N_pores · p_pore)
C_in(t) = C_ext · (1 − exp(−t/τ_eq))          → peak capped at C_ext
```

PepT1 baseline (both cells; healthy-cell saturating uptake):

```
C_in,healthy = C_in_max_healthy · C_ext/(Km + C_ext),   C_in_max_healthy = AR_lin · Km
S            = C_in,pyroptotic / C_in,healthy = (Km + C_ext) / C_in_max_healthy
```

`AR_lin` (linear-regime accumulation ratio) encodes the **unknown** synovial-macrophage PepT1 expression (scenarios: absent / low / moderate / high-concentrative). In the pyroptotic cell the pore short-circuits PepT1 → `C_in,pyroptotic = C_ext`.

### Three orthogonal metrics per route (IA / SC / oral)
1. **peak intracellular [KPV] / IC50** — flux/therapeutic sufficiency (A1)
2. **selectivity ratio S vs healthy cell** — pore benefit over the PepT1 baseline (A2)
3. **robustness** — sweep pore lifetime (1–30 min) × pores/cell (10–10⁴)

### Decision filter
A route PASSES only if it clears BOTH ≥1× IC50 AND ≥3× selectivity with the named assumptions holding. **No route passes.**

---

## Explicitly NOT done (mud-sculpture traps avoided)
- **No molecular-dynamics** of KPV threading the pore — the pore is 15–40× wider than KPV; there is no meaningful threading physics.
- **No docking** of KPV to NLRP3/NF-κB — that is a separate pharmacology question, out of scope. The IC50 is taken from the cell-assay literature.

Model kept to transport/mass-balance. Stdlib-only. Deterministic.

---

## Status
Complete (v1, 2026-07-13). Pre-commit grep-verify gate passed; three named compounding assumptions → verdict **provisional**. Subagent peer review incorporated (see interpretive page Limitations).
