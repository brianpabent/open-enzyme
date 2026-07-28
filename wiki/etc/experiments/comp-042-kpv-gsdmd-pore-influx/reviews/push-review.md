COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: 4a593d03c6c859cbcd860f8c8e5af6265c8a55f59206933c003e2ec5a6283e7d
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: no
PROPAGATION_ALLOWED_SCOPE: passive GSDMD-pore influx within the declared model; exposure-proxy A1 engineering states; A2 unresolved; matched uptake-test routing
SYNTHESIS_ALLOWED_SCOPE: bounded physical-delivery and validation-design synthesis using A1 as an exposure proxy and A2 as an unresolved heuristic; no route qualification
FORBIDDEN_INFERENCES: KPV efficacy; intracellular target engagement; observed synovial KPV exposure; route qualification; physiological or total-cell selectivity; safety; therapeutic-timing sufficiency; GSDMD pore-delivery platform validation or refutation; design-space fractions as probabilities; universal equilibration; chassis choice; clinical advice

# Independent comp review — comp-042

## Reviewed snapshot

Fresh context-isolated Codex reviewer (GPT-5 family), bound to canonical `push-review.manifest.json` SHA-256 `4a593d03c6c859cbcd860f8c8e5af6265c8a55f59206933c003e2ec5a6283e7d` at source commit `8c434f9d44d27a9d20915697f78bce0e90337930`. The fresh manifest binds all 15 non-review COMP files and the five current referencing surfaces, including the uncommitted `open-questions.md` and `validation-experiments.md` states. All manifest entries were inspected completely; targeted mechanism/payload searches also covered the KPV page, GSDMD hypothesis page, dashboard entry, and other KPV/GSDMD/PepT1 references. No unsupported binary entry exists. The modern pre-run/post-run authoring lifecycle validates.

The documented command was executed twice under CPython 3.14.5, as explicitly authorized. Every output was byte-identical before the first run, between runs, and after the second run; the six final SHA-256 values match the manifest, and `git diff --exit-code` reports no output change.

## Bottom-line verdict

Clean with limitations. COMP-042 is reproducible and internally coherent for its narrow purpose: a passive pore-influx calculation compared with an extracellular cell-assay exposure proxy, plus an explicitly unvalidated A2 equation-response map. Its `YELLOW-A2-unresolved` verdict is supported. The limitations are the scientific boundaries already carried in the artifact—not required corrections—so both lanes are eligible only within the allowed scopes above and no queue action remains.

## Implementation and constraint closure

The implementation loads the fixed JSON inputs, computes single-pore diffusive permeability with cylindrical-channel and two-sided access resistance, scales by pore count, and solves a well-mixed intracellular approach to the extracellular boundary. The concentration is capped at `C_ext`; no sign, unit, time-base, denominator, or serialization mismatch was found. A1 divides only the modeled passive pore contribution by the 10 nM extracellular cell-assay proxy. A2 divides that pore-only contribution by the declared healthy-cell PepT1 heuristic; it does not add concurrent PepT1 influx to the pore-forming cell. Zero healthy baseline is encoded in strict JSON as `null` plus an explicit positive-infinity state, not silently treated as missing data.

The stored macrophage surface area and KPV charge are contextual rather than numerical drivers; both are identified as such. Molecular weight supports the separately declared intra-articular arithmetic but is not silently used to infer the route boundary. No suspicious load-bearing input is stored without an auditable role, and no hidden default changes the decision rules.

No biochemical reaction, cosubstrate, cofactor, enzymatic stoichiometry, or coproduct is modeled. The relevant constraints are solute size/diffusion, pore radius and length, access resistance, pore count and lifetime, cell volume, extracellular concentration, and the PepT1 comparator. The model does not resolve finite-bath depletion, efflux, intracellular degradation, membrane repair/lysis, changing pore abundance, target pharmacology, cytokine timing, or local safety. Those omissions block physiological and therapeutic inference but do not invalidate the declared passive-transport prior.

The exact-runtime contract is explicit and reproducible on the available environment: CPython 3.14.5 is checked in code and named in the README. The contract promises same-platform byte identity, not portability across Python versions. The two independent reruns satisfy that contract.

## Summary-fidelity audit

Code, all generated outputs, README, interpretive page, experiment index, chassis page, current open-question pointer, validation §1.32, KPV page, GSDMD hypothesis page, and dashboard agree:

- Overall verdict: `YELLOW-A2-unresolved`.
- Central A1 ratios versus the 10 nM proxy: intra-articular 29,200 (GREEN), subcutaneous 3 (YELLOW), and oral 0.1 (RED).
- Unweighted design-space fractions clearing the proxy: 1.0, 0.679, and 0.03635; none is presented as a probability.
- A2 retains favorable heuristic corners but remains unresolved because the healthy-cell equation, PepT1 scenarios, and synovial-macrophage baseline are unvalidated; total-cell selectivity is not calculated.
- Route colors remain attached to design-space/not-observed-PK language on the pages that enumerate them. No page qualifies intra-articular, subcutaneous, or oral delivery.

The current `open-questions.md` entry is a concise pointer to the physical-delivery hypothesis and §1.32, not a duplicated results narrative. Targeted grep confirms no dangling `See.` remains on the inspected COMP-042 surfaces. Validation §1.32 now carries `TBD` cost and time rather than unsupported dollar/week estimates. The dependency diagram no longer asserts a false §2.3→§3.3 edge; it states the EPI configuration test and the independent wild-type fungal-enzyme timing branch separately.

## Reader-facing ownership audit

The focused KPV page owns exact-material requirements, evidence, delivery/exposure gaps, and falsification. The GSDMD page owns the transporter-orphan pore-delivery conjecture. Validation §1.32 owns the matched tracer and KPV-comparator gate. The computational page owns model results and boundaries; portfolio/index surfaces remain short summaries. No COMP-042 surface adds personalized dosing, clinical guidance, editorial history, page-placement narration, a chassis decision, or an inappropriate cross-track narrative foil.

## Conjecture preservation audit

No unsupported factual upgrade was found. COMP-042 neither proves nor falsifies KPV efficacy, KPV physiological selectivity, or the wider GSDMD pore-delivery platform. The corpus preserves two distinct bounded ideas: KPV as a PepT1-confounded uptake comparator and separate pre-pore priming conjecture, and a transporter-orphan membrane-impermeant payload as the cleaner physical-delivery probe. §1.32 discriminates the latter with matched pore-on/off cells and confines any result to the exact tracer, exposure, cell model, pore state, and time window.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/README.md` | design | yes | Question, execution contract, decision rules, and exclusions are explicit. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/analyze.py` | design | yes | Units, formulas, rules, strict serialization, and runtime guard close. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/kpv_properties.json` | design | yes | Estimate/sensitivity status is preserved; no KPV-specific permeability claim. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/macrophage_geometry.json` | design | yes | Cell volume is used; surface area is explicitly contextual. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/pept1_and_effective_concentration.json` | design | yes | Km/proxy sources and unmeasured synovial baseline are explicit. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/pore_geometry.json` | design | yes | Structural anchors and named pore-count/lifetime assumptions are separated. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/provenance.md` | design | yes | Primary anchors, calculations, assumptions, and gaps are distinguished. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/query-strategy.json` | design | yes | Search scope and non-retrieval limits are documented. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/route_concentrations.json` | design | yes | IA arithmetic and SC/oral design-space PK assumptions are not observed PK. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/central_results.json` | generated_output | yes | Central transport and A1/A2 values match code and summaries. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/monte_carlo.json` | generated_output | yes | Deterministic unweighted design-space diagnostics; not probabilities. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/robustness_sweep.json` | generated_output | yes | Twenty declared stress rows preserve nonequilibrium cases. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/selectivity_grid.json` | generated_output | yes | All 108 heuristic cases and zero-baseline states are explicit. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/summary.md` | generated_output | yes | Faithful to passive-contribution, proxy, timing, and A2 boundaries. |
| `wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/verdicts.json` | generated_output | yes | Route states and overall cap follow the preregistered rules. |
| `wiki/chassis-pending-interventions.md` | proposed_update | yes | No route or chassis qualification; §1.32 is the empirical gate. |
| `wiki/computational-experiments.md` | proposed_update | yes | Compact numeric summary and next gate match outputs. |
| `wiki/kpv-gsdmd-pore-influx-computational.md` | proposed_update | yes | Canonical interpretation preserves all material exclusions. |
| `wiki/open-questions.md` | proposed_update | yes | Concise unresolved-hypothesis pointer; no dangling `See.`. |
| `wiki/validation-experiments.md` | proposed_update | yes | §1.32 is bounded, cost/time are TBD, and dependency residue is absent. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| KPV radius 0.45–0.60 nm; diffusion 4–6×10⁻¹⁰ m²/s | `kpv_properties.json`, `provenance.md` | Permeability sensitivity | Stokes–Einstein engineering estimate, not direct KPV/GSDMD measurement | Properly bounded. |
| GSDMD inner diameter 10–21.5 nm; effective length 4–10 nm | `pore_geometry.json`, `provenance.md` | Radius/length sensitivity | Structural papers named; length partly engineering estimate | Properly bounded. |
| Hindrance 0.5–1.0 | `kpv_properties.json` | Multiplicative permeability sensitivity | Named engineering sensitivity; no enhancement credited | Properly bounded. |
| Cell volume 1,000–5,000 µm³; pore count 10–10,000; lifetime 60–1,800 s | geometry inputs | Equilibration and finite-time fraction | Volume is a cell-biology estimate; count/lifetime are named design assumptions | No physiological-frequency inference allowed. |
| IA 15–1,460 µM; SC 0.003–0.2 µM; oral 0.0001–0.003 µM | `route_concentrations.json` | External boundaries and A1 | IA arithmetic from named dose/volume assumptions; SC/oral named PK spaces | Route colors are design states only. |
| 10 nM extracellular KPV proxy | PepT1 input, provenance | A1 denominator | Artifact records Dalmasso primary full-text verification; not independently refetched in this push review | Exposure proxy only. |
| PepT1 Km 160/700/1,000 µM | PepT1 input, provenance | A2 sensitivity | Artifact records Dalmasso figure-level verification; no synovial-macrophage operating constant | Heuristic sensitivity only. |
| PepT1 scenarios AR_lin 0/0.3/1/3 | PepT1 input | A2 denominator | Unweighted named scenarios, not measured expression or probabilities | Keeps A2 unresolved. |
| A1 route states and `YELLOW-A2-unresolved` | all six outputs | Decision output | Recomputed twice from bound inputs/code under CPython 3.14.5 | Byte-identical and rule-consistent. |

## Affected wiki pages

- `wiki/kpv-gsdmd-pore-influx-computational.md` — already consistent — owns the bounded model interpretation.
- `wiki/computational-experiments.md` — already consistent — route states remain engineering/proxy results.
- `wiki/validation-experiments.md` — already consistent — §1.32 separates the tracer test from KPV/PepT1 uptake and carries no unsupported cost/timeline or false dependency.
- `wiki/chassis-pending-interventions.md` — already consistent — no route, platform, or chassis qualification.
- `wiki/open-questions.md` — already consistent — concise pointer; no dangling-reference residue.
- `wiki/kpv-peptide.md` — already consistent — owns KPV evidence, sourcing, delivery gaps, and the distinct priming conjecture.
- `wiki/gsdmd-pore-delivery-paradox.md` — already consistent — owns the wider transporter-orphan physical-delivery conjecture.
- `index.md` — already consistent — one-line verdict preserves the A1/A2 boundary.
- Other targeted KPV/GSDMD/PepT1 surfaces — already consistent — no COMP-042-derived efficacy, route, safety, or selectivity upgrade found.

## New connections or implications

No unpropagated implication found. The useful connection is already routed: favorable passive-pore calculations justify a transporter-orphan matched-uptake test, while KPV remains a deliberately confounded comparator whose separate pre-pore biology requires its own PepT1/timing experiment. This is a validation-design implication, not evidence of therapeutic delivery.

## Required actions

None.

## Review limits

Every manifest file and generated output was inspected, and the documented code was executed twice under the exact declared runtime. Primary papers were not independently refetched during this push review; figure-level verification statements were assessed from the bound provenance and the valid historical authoring gates. The receipt therefore does not upgrade those sources beyond their named structural, in-vitro, estimate, assumption, or gap status. The model remains a simplified passive-transport prior and cannot answer pharmacokinetics, total-cell accumulation, target engagement, efficacy, timing sufficiency, or safety.
