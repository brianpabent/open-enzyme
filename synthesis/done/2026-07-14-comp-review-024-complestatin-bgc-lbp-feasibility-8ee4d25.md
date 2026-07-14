---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-024
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-024

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-024-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-024-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-024

## Bottom-line verdict

**Action required.** The qualitative recommendation — do not prioritize an in-situ colonic LBP complestatin BGC program, and route attention toward C1-INH instead — is plausible and broadly consistent with the corpus. However, the **quantitative feasibility scores are expert-prior bookkeeping, not a closed computational model**, and several artifact/summary contracts overstate implementation closure, primary-source verification, sensitivity robustness, and C1-INH comparator validity.

The most important implementation finding is that `analyze.py` **loads** `inputs/bgc_architecture.json` and `inputs/chassis_profiles.json`, but the load-bearing feasibility scores are **hardcoded constants** in `SCORES` and `C1_INH_SCORES`. The input JSON mostly feeds output summaries, not scoring derivation. That is acceptable only if the result is explicitly framed as an expert-scored prioritization prior; it should not be presented as a data-derived feasibility computation.

## Implementation and constraint closure

What I traced:

- `analyze.py` deterministically computes:
  - EcN complestatin geometric mean: **0.544**, verdict **YELLOW**.
  - *B. thetaiotaomicron* geometric mean: **0.225**, verdict **RED**.
  - C1-INH EcN comparator geometric mean: **0.774**, verdict **GREEN**.
- The geometric mean calculation is straightforward and deterministic, with factor values clamped only below `0.01` for log safety.
- The committed `outputs/results.json` and `outputs/summary.md` appear structurally consistent with the hardcoded scoring logic shown in `analyze.py`.
- `chassis = json.loads(...)` is loaded but not used in any factor scoring.
- Most `bgc_architecture.json` values are used only in the output `bgc_summary`, not in the actual scoring factors.
- `CHANNEL_WEIGHTS` is defined but empty and unused.

Stored-but-unused / weakly used findings:

- Many inputs flagged by the heuristic are indeed **stored documentation inputs rather than executable inputs**. Examples: native aromatic amino-acid supply, CAI estimates, GC content, P450 redox partner compatibility, clinical precedents, comparator C1-INH recombinant details.
- This is not a bug if the method is manual expert scoring, but it is a summary-fidelity problem where the artifact implies the JSON inputs are quantitatively driving the model.
- `outputs/results.json` says “Nine feasibility factors per host,” but C1-INH uses **11 factors**. The summary caveats this apples-to-oranges comparison, but the machine-readable `scoring_method` field remains inaccurate for the comparator.
- The README says factor scores are justified in `outputs/summary.md`; the committed summary mostly lists scores in tables. The substantive per-factor justifications live primarily in `analyze.py` comments, not in the output summary.

Constraint closure:

- Reaction substrates and cofactors are only partially closed:
  - NRPS substrate set is represented: Hpg / Cl₂-Hpg, Tyr, Trp, β-OHTyr.
  - Tailoring dependencies are represented qualitatively: ComI/ComJ P450s, ComH nonheme halogenase, Hmo FMN oxidase.
  - ComH cofactors are named in JSON: α-ketoglutarate, Fe(II), Cl⁻, O₂.
  - P450 electron-transfer requirements are named qualitatively, but no NADPH, ferredoxin/reductase stoichiometry, intracellular redox capacity, or redox-partner kinetic compatibility is modeled.
  - PPTase requirement is represented qualitatively, but CoA / phosphopantetheinylation efficiency is not modeled.
- Physiological operating regime is not quantitatively closed:
  - No colonic O₂ concentration, mucus-vs-lumen microoxic gradient, EcN residence niche, or intracellular O₂ availability is modeled.
  - “O₂-dependent tailoring vs anaerobic-resident lifestyle” is represented by a hardcoded score, not by exposure-time or rate modeling.
  - This is especially important for EcN: the conclusion that EcN is a poor in-situ colonic host is plausible, but “fundamentally incompatible” is stronger than the implemented evidence because EcN is facultative and can tolerate microaerobic exposure. For *Bacteroides*, the strict-anaerobe incompatibility is much stronger.
- Mass balance is not closed:
  - No finite precursor flux for tyrosine, tryptophan, α-KG, chloride, iron, NADPH, or Hpg/β-OHTyr pathway intermediates.
  - No product titer requirement is estimated for CP0-relevant complement inhibition.
  - No residence time, exposure window, secretion/export rate, or luminal dilution is modeled.
- Localization / access is not closed:
  - The code assesses BGC expression tractability but does not model whether complestatin produced by EcN or *Bacteroides* would be exported, remain stable, reach C1q/C4b-relevant sites, or avoid binding nonspecific luminal proteins/cell-wall targets.
  - ComL is treated as a self-resistance/export mitigation, but no host-specific transporter compatibility is modeled.
- Safety/off-target closure is qualitative only:
  - Vancomycin-family D-Ala-D-Ala binding and host toxicity are acknowledged.
  - No local peak concentration, microbiome off-target killing, resistance, containment, or LBP safety handling is quantified.
- Sensitivity closure is missing:
  - README says scores are robust to ±0.1 variation, but no sensitivity sweep is implemented or committed.
  - Dominant uncertainties are not systematically varied: colonic O₂ availability, P450 redox productivity, product titer needed for complement inhibition, expression burden, export, toxicity, and C1-INH glycosylation/protease behavior.

## Summary-fidelity audit

Clean / consistent points:

- README, `outputs/summary.md`, the interpretive page, and `wiki/computational-experiments.md` agree on the key numbers:
  - EcN complestatin **0.544 YELLOW**.
  - *Bacteroides* **0.225 RED**.
  - LBP-track framing **RED**.
  - C1-INH comparator **0.774 GREEN-provisional**.
- The interpretive page correctly notes the apples-to-oranges caveat for C1-INH’s 11-factor comparator.
- `wiki/computational-experiments.md` has already propagated the main comp-024 conclusion and notes that comp-037 later substantiated the C1-INH follow-up.

Mismatches / overstatements requiring action:

- The artifact presents a “computational feasibility” result, but implementation is **manual expert scoring with hardcoded factors**. This needs explicit labeling wherever scores are cited.
- “Pre-commit grep-verified” / “grep-verified” claims are not independently verifiable from the artifact because primary source text is not committed. The provenance file reports author verification via WebFetch/WebSearch, but the review cannot confirm it by inspection.
- The README command is path-ambiguous/wrong from repo root: it says `cd experiments/comp-024-...`, while the tracked path is `wiki/etc/experiments/comp-024-...`.
- `outputs/results.json` states “Nine feasibility factors per host” even though the C1-INH comparator has 11 factors.
- The C1-INH comparator’s GREEN score is partly inflated by assigning non-applicable NRPS/BGC factors to `1.0`. The summary acknowledges this, but the machine-readable result still reports it as a GREEN comparator without embedding the caveat.
- The “C1-INH informative-factor mean ~0.70” statement is not implemented in code and should either be computed explicitly or softened.
- The README / provenance robustness claim “geometric mean is robust to ±0.1 variation” is not backed by a committed sensitivity analysis.
- `wiki/chassis-pending-interventions.md` still has a “Pending entries” item saying the next move is a C1-INH comp-NNN; this is stale because comp-037 now exists.
- H05 still frames C1-INH as a sister card if a future comp-NNN passes; comp-037 has landed MODERATE, so the hypothesis-card surface should be updated or a parallel C1-INH hypothesis card should be created.
- `validation-experiments.md` / comp-037 surfaces indicate a C1-INH wet-lab kinetic-competition gate should be specified, but that is not yet clearly propagated as a validation entry.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| EcN complestatin score = 0.544 YELLOW | `analyze.py` `SCORES`; `outputs/results.json` | Direct geometric mean over hardcoded factors | Internal arithmetic inspectable; factor origins expert-estimate | Reproducible as code output, but not data-derived |
| *B. thetaiotaomicron* score = 0.225 RED | `analyze.py` `SCORES`; `outputs/results.json` | Direct geometric mean over hardcoded factors | Internal arithmetic inspectable; factor origins expert-estimate | Reproducible as code output, but not data-derived |
| C1-INH comparator = 0.774 GREEN | `analyze.py` `C1_INH_SCORES`; `outputs/results.json` | Direct geometric mean over 11 hardcoded factors | Internal arithmetic inspectable; comparator model not equivalent to BGC model | Needs caveated machine-readable framing |
| 48.7 kb original cluster | `inputs/bgc_architecture.json`; provenance.md | Output summary only; not used in score except via hardcoded score rationale | Citation given to Chiu 2001; source text not committed | Unresolved primary verification in this review |
| 54.5 kb reconstituted cluster | `inputs/bgc_architecture.json`; provenance.md | Output summary only; hardcoded cluster-size score rationale | Citation given to Park 2016; source text not committed | Unresolved primary verification |
| 16 ORFs | `inputs/bgc_architecture.json`; provenance.md | Output summary only | Citation given; no primary text committed | Unresolved primary verification |
| 7 NRPS modules | `inputs/bgc_architecture.json`; provenance.md | Output summary only | Citation given; no primary text committed | Unresolved primary verification |
| ComI/ComJ P450 phenolic coupling required for active architecture | JSON, README, summary, interpretive page | Qualitative basis for hardcoded P450/O₂ scores | Citation to Park 2016; source not committed | Plausible but primary verification unresolved |
| Park 2016 M55/S56 deletion derivatives inactive | README, summary, JSON oxygen-dependence | Load-bearing support for “tailoring is essential” | Citation string only in artifact | Must be primary-verified before strong wording |
| ComH requires α-KG + Fe(II) + Cl⁻ + O₂ | `bgc_architecture.json` | Qualitative support for O₂-dependence score | Canonical biochemical claim; no direct source attached | Mechanistically plausible; source incomplete |
| Hmo is O₂-dependent FMN oxidase | JSON, README, summary | Qualitative support for O₂-dependence score | No direct source beyond BGC provenance | Needs source tie if load-bearing |
| EcN facultative anaerobe / colon lumen essentially anoxic | `chassis_profiles.json`; code comments | Basis for O₂ factor 0.30 | Chassis profile cites “canonical references,” not specific sources | Plausible but under-sourced |
| *Bacteroides* strict anaerobe, cannot grow with O₂ | `chassis_profiles.json`; code comments | Basis for O₂/P450 factors 0.05 | General microbiology; no specific source attached | Plausible; source tie incomplete |
| GC Streptomyces ~72%, EcN 50.7%, *B. theta* 42.8% | JSON + provenance | Only indirectly via hardcoded GC scores | Some named sources; Streptomyces genus-typical; no direct verification | Under-verified, but not dominant |
| CAI unoptimized/optimized estimates | `chassis_profiles.json` | Not used in code; only comments/rationale | Explicitly rough estimates ±0.1 | Documentation-only; should not be over-weighted |
| No full complestatin BGC precedent in EcN/Bacteroides | provenance.md; code comments | Hardcoded precedent scores 0.35 / 0.10 | Negative literature-search claim; no reproducible search snapshot | Unresolved; absence-of-evidence caveat needed |
| *S. lividans* TK24 expression precedent | provenance.md, summary | Output summary; rationale for “aerobic fermentation candidate” | Citation to Park 2016; no primary text committed | Unresolved primary verification |
| Thresholds GREEN ≥0.60, YELLOW 0.30–0.59, RED <0.30 | `analyze.py` constants | Direct verdict mapping | No empirical calibration | Arbitrary expert rubric; must be labeled |
| Robustness to ±0.1 factor variation | README limitations | Not implemented | No committed sensitivity output | Unsupported; action required |
| C1-INH Pichia titers 0.5–2 g/L | `chassis_profiles.json`; provenance.md | Documentation for comparator, not code-derived | Provenance admits secondary-source summaries | Not primary-verified; do not use as verified load-bearing value |
| Reproduction command | README | User-facing reproducibility | Path mismatch from repo root | Needs correction |

## Affected wiki pages

- `wiki/complestatin-bgc-lbp-feasibility-computational.md` — **change required** — qualitatively consistent, but should explicitly label scores as hardcoded expert priors, not data-derived computation; “grep-verified” should be framed as author-reported unless primary source excerpts are committed.
- `wiki/computational-experiments.md` — **already mostly consistent** — comp-024 row correctly reflects the main verdict and comp-037 follow-up. Optional improvement: note that comp-024’s numerical scores are expert-scored priors.
- `wiki/chassis-pending-interventions.md` — **change required** — “Pending entries” still says C1-INH’s next move is a comp-NNN; comp-037 is now complete. Move/update the item to point to comp-037 and the wet-lab kinetic-competition gate.
- `wiki/engineered-lbp-chassis.md` — **already mostly consistent** — incorporates comp-037 and comp-043. Optional improvement: do not let comp-024’s C1-INH 0.774 stand alone without the later comp-037 MODERATE caveat.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — **change required** — still says C1-INH becomes a sister hypothesis if a future comp-NNN passes. Comp-037 has landed; create/update a parallel C1-INH hypothesis card or update H05 cross-reference.
- `wiki/validation-experiments.md` — **change required** — comp-037 identifies a C1-INH RCL kinetic-competition wet-lab gate, but a clear validation entry is not yet propagated.
- `wiki/complement-c5a-gout.md` — **already broadly consistent from inspected sections** — the two-chassis CP0 architecture is compatible with comp-024/037. Optional improvement: wherever comp-024 is cited, distinguish C1-INH comparator prior from comp-037’s higher-resolution MODERATE verdict.
- `wiki/modality-chokepoint-matrix.md` — **already consistent** — includes two-chassis CP0 architecture and comp-037 caveat. Optional improvement: avoid implying comp-024 alone substantiates C1-INH beyond provisional ranking.
- `wiki/upstream-complement-modulator-sweep-computational.md` — **already consistent** — comp-018 Phase 2 appropriately grounds C1-INH as an engineering thread.

## New connections or implications

- The artifact supports a broader design rule already echoed elsewhere: **O₂-dependent biosynthetic payloads are poor fits for obligate-anaerobe resident LBPs unless the active product is made ex situ or the chemistry can run before colonization.** This is analogous to later LBP/uricase findings where enzyme chemistry, not only expression, can mismatch anaerobic physiology.
- Complestatin remains more logically positioned as an **aerobic production/manufacturing candidate** than as an in-situ LBP payload. That is distinct from whether the molecule is mechanistically interesting at CP0.
- The C1-INH comparison is useful as a **triage pointer**, but comp-037 supersedes comp-024 for the real C1-INH evidence tier. Corpus pages should cite comp-037 for C1-INH feasibility and comp-024 mainly for the “complestatin BGC not LBP-first” decision.
- The experiment highlights an important corpus-maintenance pattern: comparator scores embedded inside a different comp can quickly become stale after a dedicated comp lands. Comparator outputs should be marked “superseded by comp-037” where appropriate.

## Required actions

1. **Reframe comp-024 numerical scores as expert-prior rubric scores.** Owner surface: `README.md`, `outputs/summary.md`, `wiki/complestatin-bgc-lbp-feasibility-computational.md`, and `wiki/computational-experiments.md`. Verification criterion: readers can see that JSON inputs are not algorithmically transformed into scores; hardcoded factor scores are manual estimates.
2. **Correct reproducibility path.** Owner surface: comp-024 `README.md`. Verification criterion: command from repo root uses `cd wiki/etc/experiments/comp-024-complestatin-bgc-lbp-feasibility && python3 analyze.py`, or an equivalent unambiguous path.
3. **Either implement or remove the ±0.1 robustness claim.** Owner surface: comp-024 `analyze.py`, README, and output summary. Verification criterion: committed sensitivity output exists, or robustness wording is softened to “not tested.”
4. **Fix machine-readable comparator wording.** Owner surface: `outputs/results.json` generation in `analyze.py`. Verification criterion: `scoring_method` no longer says all analyses use nine factors when C1-INH uses 11; comparator caveat is machine-readable.
5. **Move substantive factor justifications into `outputs/summary.md` or stop claiming they are there.** Owner surface: `analyze.py` summary generation and README. Verification criterion: each factor score has a visible justification in the committed human-readable output, or README points to code comments as the source.
6. **Primary-source verification packet or wording downgrade.** Owner surface: `inputs/provenance.md` and interpretive page. Verification criterion: either source excerpts/search snapshots are committed for Chiu 2001, Park 2016, and key C1-INH comparator anchors, or wording changes from “verified” to “author-reported verification; reviewer has not independently verified primary text.”
7. **Update stale C1-INH propagation.** Owner surfaces: `wiki/chassis-pending-interventions.md`, H05 or a new C1-INH hypothesis card, and `validation-experiments.md`. Verification criterion: comp-037 is cited as completed, and the next gate is the C1-INH RCL kinetic-competition wet-lab assay rather than a future generic comp-NNN.
8. **If the RED-for-LBP decision is retained, separate qualitative conclusion from quantitative precision.** Owner surface: interpretive page and computational index. Verification criterion: conclusion reads as “qualitative design-prior RED for in-situ LBP framing” rather than implying calibrated probability or empirically validated feasibility.

## Review limits

- I did not execute `python3 analyze.py`; reproducibility was assessed by code inspection and committed outputs.
- Repository fixed-string search tool failed because `rg` was unavailable, so affected-surface discovery relied on directory listing and direct reads of likely pages from the bundle and repo.
- Primary literature was not directly available in the artifact. I did not independently verify Chiu 2001, Park 2016, Trauger/Walsh 2000, C1-INH Pichia titer claims, or M55/S56 inactivity against primary full text.
- The validation-experiments page in the bundle was truncated; conclusions about C1-INH validation propagation are based on inspected sections plus comp-037’s own stated handoff.
- I did not inspect every top-level wiki page manually; affected pages are those found from the bundle plus directly inspected likely surfaces.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
