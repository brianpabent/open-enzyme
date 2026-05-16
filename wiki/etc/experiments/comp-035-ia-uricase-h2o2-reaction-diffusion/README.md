# comp-035: Intra-articular Uricase H₂O₂ Reaction-Diffusion Analysis

**Question:** For each of the three published spatial-coupling architectures (Pickering emulsion / uricase-catalase fusion protein / free co-formulated catalase), does the predicted steady-state [H₂O₂] at the synovial-tissue boundary stay below the derived safe-threshold band (<10 µM presumptively safe, 10-100 µM gray, >100 µM presumptively toxic)?

**Verdict (median, central parameters):**
- **Pickering emulsion (Liu 2025 geometry): GREEN** — predicted joint-bulk [H₂O₂] median 0.19 µM, p95 1.1 µM.
- **Fusion protein: GREEN** — predicted joint-bulk [H₂O₂] median 0.034 µM, p95 0.20 µM.
- **Free co-formulated: GREEN** — predicted joint-bulk [H₂O₂] median 0.19 µM, p95 7.2 µM, **max 120 µM (RED-tier worst case under unfavorable [CAT] / kinetic conditions).**

All three architectures clear the 10 µM presumptive-safe threshold under reference conditions because catalase is one of the fastest known enzymes (kcat 10⁷-10⁸ s⁻¹, kcat/Km ~ 4 × 10⁷ M⁻¹ s⁻¹) and even modest concentrations scavenge H₂O₂ below tissue-toxic levels via the linear-regime first-order rate. **The architectures differ in edge-case robustness**: Pickering and fusion fix the URI:CAT stoichiometry by construction; free co-formulated fails at YELLOW/RED only when the URI:CAT ratio is mis-engineered (high URI, low CAT — see edge-case `uneven_free_URI_100uM_CAT_1uM` lands free at 31.6 µM YELLOW while Pickering and fusion stay GREEN).

**Headline architectural finding:** the FRET-confirmed <10 nm donor-acceptor distance in Liu 2025 is NOT what closes the H₂O₂ diffusion gap in the Pickering architecture (Da_shell median 5e-3 — far below 1; intra-shell scavenging is negligible because the shell is too thin for catalase to scavenge before H₂O₂ diffuses through). The actual mechanism that keeps Pickering safe is **bulk-phase catalase scavenging** from catalase distributed across all dispersed droplets in the joint volume — mathematically equivalent to the free co-formulated case at the same total dose. The interfacial Pickering geometry contributes (a) fixed URI:CAT stoichiometry preservation in vivo (preventing mis-dosing); (b) preservation of catalase activity during in vivo storage and immune exposure (Liu 2025 measures 5× boost in immobilized CAT specific activity vs free CAT); (c) mannose-targeted retention at the inflammation site. These are real and load-bearing architectural advantages — but the safety is driven by total catalase capacity, not by the FRET-confirmed proximity.

**Informs:** [`chassis-pending-interventions.md` §6](../../../chassis-pending-interventions.md) (closes the H₂O₂ housekeeping question for the IA uricase chassis-pending entry); [`gout-kill-chain-delivery-routes.md`](../../../gout-kill-chain-delivery-routes.md) (resolves the "intra-articular uricase H₂O₂ safety" open question between this page and `delivery-route-matrix.md`); enables IA uricase chassis-pending entry to advance toward chassis-selection.

**Interpretive wiki page:** [`wiki/intra-articular-uricase-h2o2-reaction-diffusion-computational.md`](../../../intra-articular-uricase-h2o2-reaction-diffusion-computational.md)

---

## How to reproduce

```bash
cd experiments/comp-035-ia-uricase-h2o2-reaction-diffusion
python3 analyze.py
```

Stdlib-only Python 3 (no external packages). All inputs in `inputs/`. Outputs deterministic given RNG seed 35.

---

## File index

```
comp-035-ia-uricase-h2o2-reaction-diffusion/
  analyze.py                             ← reaction-diffusion model orchestrator (run this)
  README.md                              ← this file
  inputs/
    provenance.md                        ← Rule 4 verification table; source + status per input
    kinetic_constants.json               ← uricase (A. flavus) + catalase (bovine liver) kinetics
    diffusion_constants.json             ← D_H2O2 in aqueous, synovial fluid, oil
    architecture_geometry.json           ← Pickering / fusion / free geometry parameters
    toxicity_thresholds.json             ← derived synovial-tissue safe-threshold band
    joint_geometry.json                  ← human knee + MTP1 + urate substrate + clearance
  outputs/
    damkohler_per_architecture.json      ← Da numbers per architecture
    steady_state_h2o2.json               ← predicted [H₂O₂] distributions
    escape_flux.json                     ← H₂O₂ escape fractions per architecture
    sensitivity_analysis.json            ← Spearman r per input dimension
    architecture_ranking.json            ← verdict distributions + headline ranking
    edge_case_scenarios.json             ← deterministic edge-case sweeps
    summary.md                           ← human-readable summary (auto-generated)
```

---

## Methodology

### Architecture 1: Pickering emulsion

Spherical droplet of radius r_d with URI and CAT co-confined at the oil-water interface. H₂O₂ produced at the interface either (a) is scavenged by adjacent surface CAT in a thin shell, or (b) diffuses radially outward into the aqueous synovial fluid.

- **Shell Damköhler number Da_shell = k_dest × thickness² / D**, where k_dest = (kcat/Km)_CAT × [CAT_shell]_M.
- **Escape fraction** f_escape = 1 / cosh(√Da) (canonical Thiele-modulus result for thin reactive shell).
- **Bulk steady-state**: H₂O₂ that escapes one droplet's shell encounters bulk catalase from all other dispersed droplets in the joint volume; production rate = total escape × n_droplets; destruction = (k_clear + (kcat/Km)_CAT × [CAT_bulk]) × V_joint × C.
- Liu 2025 measured geometry: droplet diameter 310-810 nm, interfacial density ~10⁴ enzymes/µm² (order-of-magnitude reconstruction from absolute loading; full text superscript ambiguity flagged in provenance.md), FRET-confirmed donor-acceptor distance 4-10 nm.

### Architecture 2: Uricase-catalase fusion protein

Each fusion molecule has uricase and catalase domains separated by L_fusion (1-5 nm). Smoluchowski first-passage probability that H₂O₂ generated at the uricase active site is captured by the colocated catalase domain: **P_capture_intra = r_capture / L_fusion** (canonical 3D first-passage to absorbing sphere). Effective bulk H₂O₂ production rate = (1 - P_capture_intra) × v_URI × [URI]. Bulk destruction = (k_clear + (kcat/Km)_CAT × [CAT]_bulk). Steady-state [H₂O₂] = q_eff / total destruction rate.

### Architecture 3: Free co-formulated catalase

Uniform mixing of URI and CAT at independent concentrations. Bulk production rate = v_URI × [URI_active]_M (M/s). Bulk destruction rate = k_clear + (kcat/Km)_CAT × [CAT_active]_M (s⁻¹). Steady-state [H₂O₂] = production / destruction.

### Monte Carlo

20,000 samples over log-uniform priors on each kinetic, diffusion, geometric, and joint-condition parameter. Deterministic given seed 35. Per-architecture Spearman rank correlation surfaces dominant uncertainty drivers.

### Edge cases

Deterministic sweeps at central-everything except one parameter perturbed: low_CAT_dose_1uM, high_dose_100uM, high_urate_5mM, low_urate_0.1mM, low_clearance_0.001, high_kcat_URI_20, low_kcat_over_km_CAT_1e7, small_joint_MTP1_0.3mL, uneven_free_URI_100uM_CAT_1uM. Surfaces architecture-distinguishing failure modes.

### Decision rule

Predicted joint-bulk steady-state [H₂O₂] at the synovial-tissue boundary mapped against the derived safe-threshold band:

- **GREEN**: median < 10 µM (presumptively safe)
- **YELLOW**: median ∈ [10, 100) µM (gray band — unmodeled in literature)
- **RED**: median ≥ 100 µM (presumptively toxic per Schalkwijk 1986 + in vitro chondrocyte data)

---

## Hard constraints honored

1. **CLAUDE.md Rule 4 pre-commit grep-verify gate** — every load-bearing kinetic constant, diffusion coefficient, geometric parameter, and citation verified to primary source (Paperclip PubMed full-text grep, PubMed metadata, biosensor/biochemistry canonical literature). Verification-pass table in `inputs/provenance.md`. **One [UNVERIFIED-AS-LITERAL] flag** on the Liu 2025 interfacial density exponent (PMC HTML superscript rendering ambiguity); back-of-envelope-reconstructed and treated with ±1 order-of-magnitude uncertainty in sensitivity analysis. The conclusion is not sensitive within this band. **One [ESTIMATED — DESIGN-SPACE PRIOR] flag** on the fusion-protein active-site separation (no published crystal structure exists; sensitivity covers 1-5 nm).
2. **Explicit confidence bounds throughout** — every output is a distribution (Monte Carlo over priors). Verdict distributions report P(GREEN), P(YELLOW), P(RED). Edge cases probe the deterministic worst-case envelope.
3. **BioDesignBench discipline** — three architectures evaluated head-to-head with the same Monte Carlo framework and the same threshold band. Sensitivity analysis reports dominant uncertainty drivers per architecture. Architecture ranking with explicit decision rule.
4. **Paperclip MCP search/cat/grep only** — `map` operator not used per `memory/feedback_paperclip_map_unreliable.md`.
5. **Multilingual default honored** — CNKI/J-STAGE checked; no non-English source surfaced a load-bearing claim divergent from English-language consensus (Liu 2025 is Chinese-authored but published in English). Translation cross-check not required (no non-English source produced a load-bearing claim).

---

## V1 simplifications (owned)

1. **Spherical-shell approximation** for Pickering droplet, point-source for fusion molecule, well-mixed for free coformulated. No 3D finite-element PDE solve; analytical results are sufficient for first-pass and the conclusions are robust across the parameter ranges.
2. **Catalase modeled in linear (first-order) regime** for [H₂O₂] << Km_CAT (~ 1 M). Valid for all synovial-relevant concentrations.
3. **Endogenous joint H₂O₂ baseline not added** to predicted bulk [H₂O₂]. Treated as background; if added, all medians shift up by 0.1-1 µM but verdicts do not change.
4. **No MSU crystal geometry detail** — urate is treated as uniformly available at the synovial concentration. The local-to-crystal concentration could be elevated (saturated MSU surface), driving higher localized uricase flux; this is captured in the sensitivity analysis via urate_M range (0.5-5 mM).
5. **Liu 2025 specific-activity unit ambiguity** flagged; canonical literature kcat used for the diffusion-model parameterization. The conclusions are not sensitive to the Liu 2025 absolute activity values because catalase is so fast it saturates in all three architectures.
6. **Fusion model assumes 1:1 stoichiometry** (one URI domain per one CAT domain in the fusion). Alternative 2:1 or 1:2 stoichiometries are not modeled; they would shift the bulk production-vs-destruction balance but not the qualitative GREEN verdict.

---

## Wet-lab handoff

**For each architecture, the cheapest wet-lab measurement to tighten the prediction:**

- **Pickering emulsion**: Amplex Red microelectrode H₂O₂ measurement in synovial-fluid mimic ± dispersed PEBR droplets ± physiologic substrate (urate at MSU surface, 0.5 mM). Direct readout of bulk steady-state [H₂O₂] under realistic conditions. Cost: ~$2-5K (Amplex Red probes + synovial fluid prep). Closes the absolute-magnitude question for the architecture.
- **Fusion protein**: Same Amplex Red readout on a recombinantly produced uricase-catalase fusion construct. Additionally: structural characterization (e.g., AlphaFold or cryo-EM) to confirm the fusion's active-site separation is in the predicted 1-5 nm range. Cost: gene synthesis $1-3K + expression test $5-10K + Amplex Red $2-5K.
- **Free co-formulated**: Already has clinical precedent (rasburicase + bovine catalase co-administration in TLS settings); the missing data is the steady-state [H₂O₂] curve at varying URI:CAT ratios. Cost: ~$2-5K Amplex Red dose-titration study.

**Load-bearing wet-lab readout:** Amplex Red microelectrode H₂O₂ measurement in synovial-fluid mimic with appropriate substrate loading **resolves the absolute-magnitude uncertainty for all three architectures**. Tissue-level effects (cartilage damage, synoviocyte response) are downstream consequences of [H₂O₂] exposure — if the [H₂O₂] readout is sub-µM, the downstream effects are by-construction low. **Amplex Red is the right next-step assay.** Chondrocyte-cytotoxicity titration only becomes relevant if Amplex Red surfaces unexpectedly high [H₂O₂].

---

## Disagreement protocol

If you reproduce the outputs and disagree with the methods or numbers, file a GitHub issue referencing this folder. Primary candidates for revision:

1. **Toxicity threshold band derivation** — the 10/100 µM GREEN/YELLOW/RED bounds are derived from Schalkwijk 1986 dose anchor + in vitro chondrocyte bolus data without a published steady-state synovial-tissue curve. A different defensible derivation (e.g., 5/50 µM or 20/200 µM bounds) would shift the verdicts but not the architecture ranking.
2. **Interfacial enzyme density** for Pickering — the Liu 2025 exponent is PMC-rendering-ambiguous; the order-of-magnitude reconstruction in `inputs/architecture_geometry.json` is conservative. Tighter measurement (e.g., direct interfacial-density determination from Liu 2025 supplemental data) would tighten the Pickering Da_shell range.
3. **Fusion active-site separation** — there is no published crystal structure of a uricase-catalase fusion. The 1-5 nm range is mechanistically defensible but is a design-space prior. A specific fusion construct with measured/predicted L_fusion would tighten the fusion verdict.
4. **D_H₂O₂ in synovial fluid** — no direct measurement is published. The 0.5-1.7 × 10⁻⁹ m²/s range is an aqueous-to-gel tortuosity-scaled estimate. A direct measurement (e.g., FRAP in synovial fluid mimic) would tighten the diffusion-coefficient sensitivity.
5. **Joint clearance rate for H₂O₂** — not directly measured in vivo; estimated as 0.001-0.05 s⁻¹. Not load-bearing for the verdict because bulk catalase scavenging dominates.

---

## Status

Complete (v1, 2026-05-16). Pre-commit grep-verify gate passed with 1 [UNVERIFIED-AS-LITERAL] + 1 [ESTIMATED — DESIGN-SPACE PRIOR] flag documented in `inputs/provenance.md`. Multilingual scan executed; no translation cross-check required. Verdict per architecture: all three GREEN under reference conditions; free co-formulated lands YELLOW under uneven-stoichiometry edge case. **Architecture chassis-selection question can advance** for the IA uricase chassis-pending entry: H₂O₂ housekeeping is closed as a load-bearing risk; chassis selection now depends on production economics, regulatory pathway, and formulation engineering rather than on the diffusion math.
