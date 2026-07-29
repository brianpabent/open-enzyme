COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 685e18c26647c493b86be90f1b7da96860fc74935e8e26eb78d8dfff240a6689
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: bounded COMP-017 correction/status propagation and ownership cleanup only; no derived intervention claims
SYNTHESIS_ALLOWED_SCOPE: unresolved healthy-human intestinal ABCG2 baseline plus source-specific evidence-tier corrections only
FORBIDDEN_INFERENCES: quantified healthy-human intestinal ABCG2 sex-null; physiological hormone-regulation magnitude from nominal Caco-2 exposure; direct androgen-receptor exclusion; clomiphene mechanism or guidance; pan-male responder rule; Q141K-conditioned luminal-uricase response ordering; clinical or intervention advice

# Independent comp review — comp-017

## Reviewed snapshot
Independent daemon consolidated review for `SOURCE_COMMIT` 14833b44e90fe92f7aa6738a3f85edde188dabe9, bound to `push-review.manifest.json` SHA-256 `685e18c26647c493b86be90f1b7da96860fc74935e8e26eb78d8dfff240a6689`. The supplied authoring gates are modern/valid, no deterministic binary blocks were reported, and targeted readbacks matched the shard-inspected text surfaces.

## Bottom-line verdict
Action required. The core scientific result is bounded and usable: COMP-017 did **not** extract direct sex-stratified healthy-human intestinal GTEx/HPA values and therefore did **not** test the prespecified 1.5× baseline threshold. The correction of Hoque/Liu/Slepnev/MacLean evidence contexts is mostly faithful. Required actions are documentation/contract issues: dependent-page ownership drift, inconsistent provenance-tier reporting, missing machine-output propagation of a forbidden inference, and non-executable provenance/gate dependencies.

## Implementation and constraint closure
`analyze.py` is a deterministic renderer/validator of committed JSON inputs. It validates GTEx/HPA “NOT EXTRACTED” status, paper IDs, evidence-level enums, required findings, and boundary schema, then writes `results.json` and `summary.md`. It does not retrieve literature, compute expression distributions, or test the 1.5× threshold. The 1.5× value is therefore a declared untested decision rule, not an evaluated statistic.

Implementation gaps:
- `inputs/provenance.md` is load-bearing for verification scope but is not read or validated by `analyze.py`.
- `cross_paper_synthesis.forbidden_inferences` includes “pan-male responder rule,” but `results.json`/`summary.md` do not carry that list as a machine-readable/human-visible output field.
- The README reproduction contract requires a passing current Gate 1 receipt, but the executable does not reference or validate that receipt.

Constraint closure is appropriate for an evidence audit, not a biochemical model. No reaction stoichiometry is modeled. The artifact correctly separates RNA, total protein, apical localization, and functional urate flux; it does not convert transcript or Caco-2 protein changes into urate transport. Nominal 1–100 µM sex-hormone Caco-2 exposures and 100 µM estradiol-benzoate conditions are treated as in-vitro/pharmacological, not physiological intestinal exposure. Q140K mouse disease-state flux and Western-blot measurements are not substituted for healthy-human baseline. No intervention, clomiphene guidance, uricase response, or safety conclusion is supported.

## Summary-fidelity audit
The experiment README, `outputs/results.json`, `outputs/summary.md`, `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`, `wiki/computational-experiments.md`, and `wiki/t-abcg2-suppression-evidence-mining-computational.md` are materially aligned on the main verdict: healthy-human intestinal ABCG2 sex stratification remains unresolved; the 1.5× threshold was not tested.

Fidelity issues:
- Hoque provenance is stronger/different in `inputs/provenance.md` than in rendered outputs. Provenance says Nature HTML/XML/PDF/supplement/source workbook were checked; outputs state Europe PMC XML tier. This is conservative but inconsistent for the 53%/88% exclusion claim.
- `full_text_extract.json` contains explicit forbidden inferences not fully emitted by outputs, especially “pan-male responder rule.”
- `wiki/abcg2-modulators.md` and `wiki/androgen-urate-axis.md` contain extended COMP-017-derived narrative despite the README’s dependent-update boundary saying dependents should receive only correction/status plus link.
- `mkdocs.yml` was inspected; no decision-relevant nav mismatch was reported.
- Related COMP-015/016/019/044 and Q141K pages are broadly consistent in not reusing retired genotype-response or 53%/88% claims.

## Reader-facing ownership audit
The focused COMP-017 evidence page properly owns the detailed source correction, boundaries, next discriminating work, and conjecture. Dependent pages should not duplicate the audit narrative or use COMP-017 as a foil for broader portfolio/intervention argument. `abcg2-modulators.md` and `androgen-urate-axis.md` currently over-own COMP-017 detail relative to the stated contract; they should be compact status/correction/link surfaces. No personalized treatment instruction was identified in the inspected COMP-017 propagation, but clomiphene/intervention implications must remain explicitly out of scope.

## Conjecture preservation audit
Unsupported factual assertions were mostly corrected rather than deleted. The negative COMP-017 result kills only the claim that this run established a healthy-human intestinal sex difference/null or tested the 1.5× threshold. It also blocks direct AR-repression, physiological hormone-magnitude, clomiphene, pan-male, and Q141K-luminal-uricase responder inferences from these sources.

The adjacent conjecture that intestinal ABCG2 response may be genotype × hormone state × inflammatory-context dependent survives as a clearly labeled Research Conjecture with animal/in-vitro premises and a discriminating donor-derived intestinal-model observation. This preservation is appropriate.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/README.md` | experiment artifact | yes | Correct bounded design; dependent-update and Gate 1 reproduction contracts need closure. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/analyze.py` | code | yes | Deterministic renderer; does not validate provenance.md or forbidden-inference propagation. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/full_text_extract.json` | input | yes | Contains source records and forbidden inferences; pan-male boundary not fully emitted. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/gtex_data.json` | input | yes | Correctly records no direct sex-stratified GTEx extraction. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/hpa_data.json` | input | yes | Correctly records no direct sex-stratified HPA protein extraction. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/provenance.md` | input/provenance | yes | More expansive Hoque verification than outputs report; not executable-validated. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/outputs/results.json` | generated_output | yes | Core verdict supported; missing explicit forbidden-inference field/list. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/outputs/summary.md` | generated_output | yes | Human-readable result faithful; same forbidden-inference/provenance limitations. |
| `mkdocs.yml` | proposed_update/navigation | yes | No material issue reported. |
| `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` | proposed_update/evidence home | yes | Strongly consistent; owns detailed evidence and conjecture appropriately. |
| `wiki/computational-experiments.md` | proposed_update/index | yes | COMP-017 registry entry faithful and bounded. |
| `wiki/t-abcg2-suppression-evidence-mining-computational.md` | proposed_update/historical evidence page | yes | Correctly demotes COMP-016 to bounded historical scan. |
| `wiki/abcg2-modulators.md` | proposed_update/dependent page | yes | Scientifically bounded, but too much duplicated COMP-017 exposition for dependent surface. |
| `wiki/androgen-urate-axis.md` | proposed_update/dependent page | yes | Scientifically bounded, but too much duplicated COMP-017 exposition for dependent surface. |
| `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md` | affected artifact | yes | Consistent with COMP-017 correction cascade; no reuse of COMP-015 invalid verdicts found here. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/README.md` | affected artifact | yes | Correctly delegates current ABCG2 corrections to COMP-017. |
| `wiki/etc/manual-literature-mining.md` | affected methods page | yes | Supports need for line/provenance anchoring; no direct conflict. |
| `wiki/gout-genetic-variants.md` | affected mechanism page | yes | Maintains Q141K as prospective stratification only; no COMP-017 overreach reported. |
| `wiki/open-questions.md` | affected portfolio page | yes | Consistent with unresolved Q141K/UOX and ABCG2 responder boundaries. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| No direct healthy-human GTEx intestinal sex-stratified values extracted | `gtex_data.json`, outputs | Validated as `NOT EXTRACTED`; emitted | Committed operational record only; no portal reproduction | Supports unresolved verdict. |
| No direct HPA intestinal sex-stratified protein values extracted | `hpa_data.json`, outputs | Validated as `NOT EXTRACTED`; emitted | Committed record only | Supports unresolved verdict. |
| 1.5× population threshold | README, `analyze.py`, outputs | Rendered, not tested | Prespecified in artifact; no data evaluation | Must be described as untested. |
| Hoque 78% jejunal vs 44% renal Western-blot reduction | `full_text_extract.json`, outputs, wiki pages | Rendered from input | Citation plus artifact provenance; primary not independently reverified in this review | Usable as artifact-verified correction, with provenance-tier clarification needed. |
| Historical 53%/88% Hoque intestinal sentence unsupported | provenance/input/output/wiki | Rendered from input | Provenance says multiple primary/publisher materials checked; output tier inconsistent | Correction usable; reconcile verification wording. |
| Liu 100 µM estradiol benzoate at 48h, no dose-dependent response | input/output/wiki | Rendered from input | Europe PMC XML tier stated; primary not reverified here | Usable only as in-vitro pharmacological context. |
| Slepnev 1/10/100 µM hormone Caco-2 increase; PXR/FXR conditions | input/output/wiki | Rendered from input | Official English abstract tier; no full numerical extraction | Usable only as abstract-tier in-vitro boundary. |
| MacLean healthy-rat no sex-specific difference | input/output/wiki | Rendered from input | PubMed abstract tier; no effect size | Animal qualitative null only, not human null. |
| “Pan-male responder rule” forbidden inference | `full_text_extract.json` | Stored but not emitted as output list | Input-owned | Needs output propagation. |
| Gate 1 receipt prerequisite | README | Not used by executable | External authoring-gate supplied in daemon brief | Link or document reproducibility dependency. |

## Affected wiki pages
- `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` — already consistent — correct evidence home and bounded conjecture.
- `wiki/computational-experiments.md` — already consistent — registry states direct-human baseline unresolved and separates evidence contexts.
- `wiki/t-abcg2-suppression-evidence-mining-computational.md` — already consistent — COMP-016 remains historical bounded scan.
- `wiki/abcg2-modulators.md` — change required — reduce duplicated COMP-017 narrative to correction/status plus link.
- `wiki/androgen-urate-axis.md` — change required — reduce duplicated COMP-017 narrative to local boundary plus link.
- `wiki/gout-genetic-variants.md` — already consistent — does not convert Q141K into UOX response or serum-urate ordering.
- `wiki/open-questions.md` — already consistent — maintains unresolved UOX/genotype and safety gates.
- `wiki/etc/manual-literature-mining.md` — already consistent — reinforces provenance/anchoring requirements.
- `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/README.md` — already consistent — delegates corrected attribution/magnitude to COMP-017.
- `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md` — already consistent — flags correction cascade and invalidates old T-axis adjudications.

## New connections or implications
COMP-017 strengthens a cross-corpus separation: ABCG2 supply-side hypotheses must distinguish baseline healthy-human expression, disease/genotype-state transporter abundance, apical localization, and functional urate flux. This supports keeping butyrate/PPARγ/Q141K rescue, gut-lumen UOX responder stratification, and hormone-axis pages in conjecture or validation-gate status until matched functional urate-flux evidence exists.

Research Conjecture boundary: genotype × hormone state × inflammatory context may matter more than binary sex for intestinal ABCG2 capacity, but COMP-017 supplies only mixed animal/in-vitro premises and no direct human effect estimate.

## Required actions
1. In `wiki/abcg2-modulators.md` and `wiki/androgen-urate-axis.md`, replace extended COMP-017-derived exposition with compact local correction/status plus link to the COMP-017 evidence home. Verification: dependent pages no longer duplicate source-by-source audit narrative or portfolio implications.
2. Reconcile Hoque provenance wording across `inputs/provenance.md`, `inputs/full_text_extract.json`, `outputs/results.json`, and `outputs/summary.md`. Verification: outputs either report the full checked-source set or explicitly say why a lower/conservative verification tier is emitted.
3. Add a machine-readable and human-visible forbidden-inferences section to generated outputs, including “pan-male responder rule.” Verification: rerendered `results.json`/`summary.md` carry the full input forbidden-inference list or an explicitly validated subset.
4. Close the provenance-validation gap: either make `analyze.py` validate required provenance/forbidden-inference fields or document that provenance is manually reviewed and outside deterministic reproduction. Verification: code or README states the contract unambiguously.
5. Clarify the Gate 1 reproduction dependency by linking or naming the hash-bound Gate 1 receipt, or remove it from the executable reproduction contract. Verification: a reader can tell what must exist before rerunning.

## Review limits
Arbitrary experiment code was not executed in daemon mode. Primary sources were not independently re-opened beyond committed text/provenance; source verification is assessed as artifact-provenance status, not reviewer-confirmed primary-source truth. Repository-wide grep was unavailable in the tool environment, so affected-surface assessment relied on the supplied hash-bound shard coverage plus targeted readbacks of decision-relevant files. No medical or clinical inference is made.
