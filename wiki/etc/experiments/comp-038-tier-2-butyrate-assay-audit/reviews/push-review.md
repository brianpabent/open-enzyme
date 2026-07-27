COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: c2b1ecc27d8820fbb81c1f2f23d0a810746b5ee29e706481dfd504239ecb3b76
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective/bounded COMP-038 assay-method status only
SYNTHESIS_ALLOWED_SCOPE: bounded assay-method synthesis with explicit matrix/provenance limits
FORBIDDEN_INFERENCES: ready-to-adopt Tier 1 or Tier 2 OE butyrate assay; De Baere full-text verification; De Baere underivatized method; butyrate-specific De Baere LOD/LOQ endpoints; exhaustive assay-landscape absence claim; culture-supernatant/stool/serum/breath interchangeability; simplified linear electrochemical transfer from Gu; OE matrix qualification; target-compartment exposure; ABCG2/Q141K rescue; gout efficacy; safety or clinical inference

# Independent comp review — comp-038

## Reviewed snapshot
Independent daemon reviewer; push manifest SHA-256 supplied as `c2b1ecc27d8820fbb81c1f2f23d0a810746b5ee29e706481dfd504239ecb3b76` for source commit `1b57f9c213d67eda156ac41119428b0a09555ea9`. Shard auditors reported complete inspection of the text artifacts in scope; targeted repository reopening confirmed the active interpretive page, computational index excerpt, result JSON, and README content. I could not reopen a committed `push-review.manifest.json` file by path, so manifest binding relies on the daemon-provided hash and shard coverage receipt.

## Bottom-line verdict
Action required, but the bounded scientific result is usable with warnings. COMP-038 correctly supports a YELLOW assay-method conclusion: no ready Tier 1/Tier 2 Open Enzyme butyrate assay; HPLC-UV is a Tier 3 culture-supernatant transfer candidate; Gu electrochemical/ANN is a stool-specific Tier 2 candidate not yet adopted. Required corrections are provenance/link hygiene and reproducibility guardrails, not reversal of the core verdict.

## Implementation and constraint closure
The computation is a literature/method audit, not a biochemical or clinical model. It can answer “what candidate butyrate measurement methods surfaced and what validation is required,” but it cannot establish target exposure, ABCG2 engagement, gout efficacy, safety, or assay adoption.

Implementation traced:
- `analyze.py` generated/inspected the 2026-05-20 abstract-level PubMed packet: 27 queries, 74 title/abstract records, no OpenRouter calls for the frozen run.
- The July 2026 current result is not reproduced by legacy `analyze.py`; it is a targeted two-source primary-source verification artifact.
- `--prepare-codex` can overwrite `pubmed-snapshot.json`, `results.json`, and `summary.md` despite README language saying legacy code must not overwrite corrected current outputs. This is a reproducibility/maintenance defect.
- Dry-run expected outputs omit `outputs/primary-source-verification-2026-07-24.json`, even though that file controls the repaired claims.
- The committed codex packet is abstract-level and does not itself contain the complete original multi-trajectory synthesis/verifier output. It is discovery evidence only.

Constraint closure:
- De Baere: abstract-only verification supports bacterial culture supernatant, UV 210 nm after acidification and ether back-extraction, matrix-matched 0.5–50 mM calibration, and analyte-spanning LOD/LOQ ranges. It does not support full-text implementation, “underivatized,” or butyrate-specific LOD/LOQ endpoints.
- Gu: full-text verification supports a specific VBS-100/G3 gold-electrode/pretreatment/voltammetry-feature/ANN stack for human stool. The n=30 within-study fecal test cohort is not independent external replication. Reported high fit must stay coupled to the statistically nonzero butyrate bias and full-stack transfer requirement.
- Breath H₂/CH₄ and breath/EBC signals are fermentation/exposure proxies at best, not butyrate-specific quantification.
- ELISA/colorimetric conclusions are bounded by noisy query hits and representative protocol mismatch; they are not exhaustive negative evidence across all vendors.
- Matrix, transport, compartment, residence time, coproduct, and safety questions are outside this assay audit and are correctly deferred to validation gates.

## Summary-fidelity audit
README, `outputs/results.json`, `outputs/summary.md`, the interpretive page, `wiki/computational-experiments.md`, and `wiki/validation-experiments.md` are materially aligned on the YELLOW boundary and matrix-specific next gates.

Fidelity issues requiring or meriting correction:
- The interpretive page and validation §1.45 label “PMID 42041444” but link to a PMC URL. Since the source line also cites PMCID/DOI, the science is probably intact, but identifier-link mismatch impairs provenance verification and should be corrected.
- `wiki/computational-experiments.md` reports Gu MAE/RMSE/R² but omits the bias caveat present in the detailed page/results. For a short index this is not fatal, but any downstream quantitative summary should include “within-study n=30; small statistically nonzero bias; no independent external transfer.”
- The computational index’s “generic free-fatty-acid colorimetric kits are a false-friend class” should remain tied to the representative-protocol/vendor-dependent boundary and not become a universal exclusion of all future colorimetric chemistry.
- Historical July 14/15 “both full-text verified” claims are retracted in the current outputs; no inspected active page appeared to rely on them.

## Reader-facing ownership audit
The focused COMP-038 interpretive page owns the evidence tier, sources, matrices, delivery/exposure non-claims, and falsification gates. Portfolio-style comparisons are not duplicated there beyond necessary method tiering. Validation §1.31 and §1.45 appropriately own the culture-supernatant and stool follow-up protocols. No personalized treatment instructions were found in the inspected COMP-038 surfaces.

Remaining ownership risks:
- Link/provenance mismatch on the Gu citation should be fixed on the focused page and validation page.
- Legacy experiment maintenance instructions should not imply `analyze.py` can reproduce the current repaired artifact.

## Conjecture preservation audit
Unsupported factual assertions were mostly corrected rather than deleted:
- De Baere as “underivatized” and “full-text verified” is retracted.
- Gu as a promising stool Tier 2 candidate survives, bounded to exact hardware/chemistry/model reproduction plus external transfer.
- HPLC-UV as a culture-supernatant Tier 3 transfer candidate survives, bounded to exact OE matrix spike/recovery and paired GC-MS.
- Butyrate as a biological hypothesis for ABCG2/Q141K or gout is not killed by this COMP; COMP-038 only says the measurement path is not yet qualified.

Adjacent conjectures that survive: matrix-qualified butyrate production QC by HPLC-UV/GC-MS; stool monitoring by reproduced Gu stack; future vendor-kit/colorimetric review if a named primary method-comparison source is found.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/README.md` | artifact text | Yes | Correct current boundary; maintenance text needs guard alignment. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/analyze.py` | code | Yes | Legacy discovery code; can overwrite repaired outputs; dry-run omits verification artifact. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/model-config.json` | input | Yes | Config labels are not execution proof. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/query-strategy.json` | input | Yes | Bounded PubMed strategy; not global/multilingual exhaustive search. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/provenance.md` | input/provenance | Yes | Correctly limits original scan and future search needs; referenced receipt not in inspected set. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/primary-source-verification-plan-2026-07-24.md` | input/plan | Yes | Acceptance criteria mostly reflected in outputs; lifecycle receipt not independently supplied. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/.gitkeep` | generated/scaffold | Yes | Harmless stale scaffold, not evidence. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/codex-synthesis-packet.md` | generated output | Yes | Abstract-level discovery packet only; not adoption-grade evidence. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/pubmed-snapshot.json` | generated output | Yes | 27-query/74-record abstract snapshot; noisy query hits; bounded search. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/primary-source-verification-2026-07-24.json` | generated output | Yes | Controls repaired claims; two-source targeted verification. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/results.json` | generated output | Yes | Faithful YELLOW structured result with limits. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md` | generated output | Yes | Faithful compact summary; blocks clinical/OE inference. |
| `wiki/tier-2-butyrate-assay-audit-computational.md` | proposed/active wiki update | Yes | Scientifically aligned; Gu PMID link target mismatch. |
| `wiki/computational-experiments.md` | proposed/active wiki update | Yes | Aligned concise index; keep Gu bias and non-exhaustive limits in downstream uses. |
| `wiki/validation-experiments.md` | proposed/active wiki update | Yes | §1.31/§1.45 aligned; Gu identifier/link mismatch also present. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 27 queries / 74 PubMed records | `pubmed-snapshot.json`, `results.json`, computational index | Discovery-scan scope | Direct committed snapshot; abstract metadata only | Verified as bounded discovery, not exhaustive search |
| No ready Tier 1/Tier 2 OE assay | `results.json`, `summary.md`, wiki pages | Core verdict | Derived from bounded scan plus two-source repair | Supported with limitations |
| De Baere HPLC-UV culture-supernatant candidate | Verification JSON, results, interpretive page | Tier 3 transfer candidate | Primary abstract only | Supported only at abstract-level |
| De Baere 0.5–50 mM calibration | Same | Dynamic range/method description | Abstract-supported | Supported for source method, not OE matrix |
| De Baere LOD/LOQ 0.13–0.33/0.5–1.0 mM | Same | Sensitivity context | Analyte-spanning abstract range | Do not assign endpoints to butyrate |
| De Baere “underivatized” | Retracted in results/summary | None valid | Not supported by accessible text | Forbidden inference |
| Gu electrochemical/ANN stool stack | Verification JSON, results, validation §1.45 | Tier 2 candidate gate | Full-text verified per artifact | Supported only for exact stack/source study |
| Gu n=30 fecal MAE/RMSE/R² 0.029/0.034/0.998 | Results/wiki | Performance summary | Full-text-derived; not public dataset | Supported with bias and transfer caveat |
| Gu bias −0.015 mM; LoA −0.065 to 0.035 mM | Results/interpretive page | Method-comparison limitation | Full-text-derived | Must accompany quantitative accuracy claims |
| ELISA RED-provisional | Results/interpretive page | Deprioritization | Bounded noisy search, no qualifying comparison found | Supported only as non-exhaustive provisional status |
| Breath H₂/CH₄ not butyrate-specific | Snapshot/results/wiki | Method exclusion | Abstract-level proxy literature | Supported for butyrate-specific quantification boundary |
| OE/gout/clinical efficacy false | Results/summary/wiki | Safety and inference boundary | Assay-method evidence only | Correctly blocked |

## Affected wiki pages
- `wiki/tier-2-butyrate-assay-audit-computational.md` — change required — correct/verify PMID 42041444 link target; retain matrix-specific and bias limits.
- `wiki/computational-experiments.md` — already mostly consistent / minor caution — concise COMP-038 summary is aligned, but downstream quantitative reuse should preserve Gu bias and non-external-replication caveat.
- `wiki/validation-experiments.md` — change required — §1.45 repeats the Gu PMID-to-PMC link mismatch; otherwise §1.31/§1.45 are consistent.
- `wiki/quantification-ladder.md` — already consistent by reference only; no inspected conflict.
- `wiki/open-questions.md` — not directly inspected in this review; interpretive page links a matrix-specific assay gap, so verify on next touched update that it does not imply a ready stool/culture transfer.

## New connections or implications
The result sharpens a cross-track rule: butyrate biology hypotheses must not advance on production claims unless the exact matrix measurement is qualified. Culture-supernatant production QC, stool monitoring, and cellular/intestinal exposure are separate observability problems.

Research Conjecture boundary: Gu-style electrochemical/ANN could become a lower-burden stool monitoring tool for future exposure studies if the exact hardware–chemistry–model stack reproduces and externally transfers. The unsupported leap is that source-study stool performance will generalize to OE operators, cohorts, or intervention conditions.

## Required actions
1. Correct the Gu citation link target on `wiki/tier-2-butyrate-assay-audit-computational.md` and `wiki/validation-experiments.md`; verification criterion: PMID link resolves to PubMed for PMID 42041444 or the label explicitly says PMCID/PMC when linking to PMC.
2. Add a maintenance guard or documented workflow separation for legacy `analyze.py`; verification criterion: running discovery/packet preparation cannot silently overwrite `results.json`, `summary.md`, or the 2026-07-24 verification-controlled state without an explicit current-output regeneration mode.
3. Update the dry-run/lifecycle expected-output check to include `outputs/primary-source-verification-2026-07-24.json`; verification criterion: artifact integrity fails if the controlling verification JSON is absent.
4. In any future propagation of Gu performance numbers, include “within-study n=30, exact stack, statistically nonzero bias, no independent external transfer”; verification criterion: no index/priority table uses R² alone as adoption evidence.

## Review limits
I did not execute experiment code. Primary papers were not independently retrieved; source verification is assessed from the committed verification artifact and shard audit. Repository fixed-string search tooling failed because the backend `rg` executable was unavailable, so affected-surface discovery relied on shard coverage plus targeted `read_file` reopening. The daemon-supplied manifest hash was used because `push-review.manifest.json` was not readable by path in this environment.
