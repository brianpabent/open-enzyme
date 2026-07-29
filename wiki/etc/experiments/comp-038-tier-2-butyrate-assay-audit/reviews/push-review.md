COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: e3455db27a3cd381eb6dd7bc6d6ed15be77b30fa958780981994160822c6f753
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: bounded YELLOW assay-method correction only: no ready OE Tier 1/2 butyrate assay; HPLC-UV culture and electrochemical/ANN stool candidates require matrix-specific validation
SYNTHESIS_ALLOWED_SCOPE: use as assay-availability and validation-gate evidence with explicit source-scope, matrix, and transfer limits
FORBIDDEN_INFERENCES: clinical or gout efficacy; target-compartment exposure; ABCG2 engagement or Q141K rescue; safety; serum/breath butyrate quantification readiness; culture/stool method interchangeability; De Baere full-text verification; exhaustive absence of all Tier 2 methods; adoption of Gu stack without complete-stack reproduction and independent transfer

# Independent comp review — comp-038

## Reviewed snapshot
Independent daemon reviewer; bound to push-review manifest SHA-256 `e3455db27a3cd381eb6dd7bc6d6ed15be77b30fa958780981994160822c6f753` at source commit `14833b44e90fe92f7aa6738a3f85edde188dabe9`. Authoring gates are reported modern and valid. Shard audits covered the COMP artifact outputs, code, inputs, maintenance tests, interpretive page, computational index, and validation-experiment surfaces; targeted repository reads of `results.json`, `summary.md`, README, interpretive page, computational index, and validation sections matched the reported boundaries. No binary deterministic blocks were reported.

## Bottom-line verdict
Clean with limitations; action required for documentation polish, not for invalidating the bounded scientific result. The artifact supports a YELLOW result: no ready-to-adopt OE Tier 1/2 butyrate assay; De Baere HPLC-UV is a Tier 3 culture-supernatant transfer candidate; Gu electrochemical/ANN is a stool-specific Tier 2 candidate requiring complete-stack reproduction and external transfer. The result cannot support method adoption, clinical/gout claims, or exhaustive assay-landscape absence.

## Implementation and constraint closure
The implemented object is a literature/verification audit, not a biochemical model. Default `analyze.py` now functions primarily as a required-file check; shard findings show it checks file existence/regular-file status, not output hashes or semantic integrity. That is acceptable only because README delegates integrity to the manifest/lifecycle check. Regeneration modes are risky: `--prepare-codex` and OpenRouter paths can rewrite discovery outputs but do not recreate the controlling `primary-source-verification-2026-07-24.json`; legacy `write_summary()` can generate a discovery-style summary without current retraction boundaries. README and repair plan partly close this by requiring reviewed lifecycle snapshots and discarding mixed output sets, but regeneration is not itself a deterministic reproduction of the current interpretation.

Constraint closure is good for an assay audit. The artifact distinguishes matrix, operating range, and method class: De Baere’s 0.5–50 mM calibration and analyte-spanning LOQ 0.5–1.0 mM are culture-supernatant-scale and unsuitable for serum-level µM butyrate without another validated method. De Baere requires diethyl-ether back extraction, pH<2 acidification, 210 nm nonselective UV detection, chromatographic separation, and matrix-matched calibration; it is not a simple low-prep/colorimetric/home assay. Gu requires the exact VBS-100/G3 electrode, pretreatment, first-scan/triplicate, feature extraction, and ANN stack; the butyrate pretreatment time and nonpublic data/code/weights materially limit transfer. Breath H₂/CH₄ remains a fermentation/transit proxy, not butyrate-specific quantification. ELISA/colorimetric conclusions are bounded non-identifications from the May search, not universal absence claims.

## Summary-fidelity audit
README, `outputs/results.json`, `outputs/summary.md`, `wiki/tier-2-butyrate-assay-audit-computational.md`, and `wiki/computational-experiments.md` materially agree on the YELLOW verdict, source-scope correction, matrix separation, and no-adoption boundary. The interpretive page and computational index correctly include the Gu bias and De Baere abstract-only caveats. `outputs/summary.md` is mostly faithful but omits the statistically nonzero Gu butyrate bias that `results.json` and the wiki pages include; because bias is a decision-relevant transfer limitation, the compact output summary should add it.

`wiki/validation-experiments.md` §1.31 and §1.45 are largely consistent with COMP-038: culture-supernatant HPLC-UV transfer and stool electrochemical/ANN reproduction are separated, with GC-MS comparison and external transfer requirements. One planning inconsistency remains outside the core COMP result: §1.14 dashboard says 4–6 weeks while the detailed section says timeline is TBD after pilot; reconcile before scheduling or rollups.

## Reader-facing ownership audit
The focused interpretive page owns its evidence, sourcing, matrix limitations, and falsification gates without portfolio-ranking overreach. The computational index gives a concise portfolio-facing summary and links out appropriately. Validation pages own experimental next gates rather than duplicating the full literature narrative. I found no personalized treatment instruction, clinical upgrade, narrative foil, or duplicated long exposition that changes the reader contract.

## Conjecture preservation audit
Unsupported prior claims were corrected rather than over-deleted: “both full-text verified,” “July 14 full-text pass,” and De Baere “underivatized” shorthand are retracted. The useful adjacent conjectures survive with gates: culture-supernatant production QC can be qualified by matrix-matched HPLC-UV/GC-MS transfer; fecal monitoring may become a Tier 2 research method only if the Gu stack reproduces and transfers. Negative findings kill only the reviewed adoption claims for current OE use, breath as butyrate-specific quantification, and generic kit/colorimetry assumptions in the bounded search—not all future low-cost butyrate chemistry.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/pubmed-snapshot.json` | generated_output | Yes | Abstract/metadata snapshot; supports bounded discovery only, not GREEN readiness or exhaustive absence. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/codex-synthesis-packet.md` | generated_output | Yes | Correctly states full-text/protocol/vendor comparison needed; contains false-positive query hits requiring article-level filtering. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/primary-source-verification-2026-07-24.json` | generated_output | Yes | Load-bearing correction; De Baere abstract-only, Gu full-text; no ready OE assay. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/results.json` | generated_output | Yes | Structured YELLOW verdict is faithful and bounded. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md` | generated_output | Yes | Mostly faithful; should add Gu statistically nonzero bias. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/README.md` | proposed_update | Yes | Current boundary and lifecycle cautions are accurate; regeneration caveat is important. |
| `wiki/tier-2-butyrate-assay-audit-computational.md` | proposed_update | Yes | Faithful reader-facing interpretation with source/matrix boundaries. |
| `wiki/computational-experiments.md` | proposed_update | Yes | Comp-038 index entry is consistent and appropriately concise. |
| `wiki/validation-experiments.md` | proposed_update | Yes | §1.31/§1.45 consistent; §1.14 timeline/dashboard inconsistency needs correction. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 27 queries / 74 PubMed records | `results.json`, `pubmed-snapshot.json`, computational index | Describes May discovery scan | Committed snapshot, abstract-level only | Supported as run metadata; not exhaustive search proof. |
| No ready OE Tier 1/2 butyrate assay | `results.json`, README, interpretive page | Overall verdict | Derived from bounded scan plus two-source repair | Supported as bounded YELLOW, not universal absence. |
| De Baere HPLC-UV matrix and range | `primary-source-verification`, `pubmed-snapshot`, interpretive page | Culture transfer candidate | Primary abstract only; full text not verified | Supported only at abstract scope. |
| De Baere LOD/LOQ 0.13–0.33 / 0.5–1.0 mM | Same | Sensitivity boundary | Analyte-spanning in accessible text | Do not assign as butyrate-specific. |
| De Baere “underivatized” retraction | `results.json`, verification JSON | Prevents shorthand overclaim | Accessible source lacks explicit support | Correctly retracted. |
| Gu exact electrochemical/ANN stack | verification JSON, interpretive page, validation §1.45 | Stool Tier 2 candidate gate | Full text via PMC, but no public code/data/weights | Supported; transfer unresolved. |
| Gu fecal test cohort n=30, MAE/RMSE/R² 0.029/0.034/0.998 mM | `results.json`, interpretive page, validation §1.45 | Quantitative candidate support | Source-study full-text extraction | Supported as within-study validation only. |
| Gu bias −0.015 mM, LOA −0.065 to 0.035 mM, statistically nonzero | `results.json`, interpretive page, validation §1.45 | Transfer/adoption limitation | Source-study full-text extraction | Supported; add to output summary. |
| Breath H₂/CH₄ not butyrate-specific | snapshot/packet, results | RED for quantification | Abstract-level proxy/confounding literature | Supported. |
| ELISA/colorimetric RED-provisional | results, summary | Prevents kit adoption | Bounded May search with false positives | Supported only as non-qualifying surfaced records. |

## Affected wiki pages
- `wiki/tier-2-butyrate-assay-audit-computational.md` — already consistent — owns the YELLOW result, matrices, source scope, and gates.
- `wiki/computational-experiments.md` — already consistent — comp-038 entry preserves caveats and avoids efficacy/adoption claims.
- `wiki/validation-experiments.md` — change required — §1.31/§1.45 are consistent, but §1.14 dashboard timeline conflicts with detailed TBD timeline.
- `wiki/quantification-ladder.md` — already consistent by reported cross-reference — HPLC-UV/GC-MS tier boundary is used correctly; no direct contradiction surfaced.
- `wiki/open-questions.md` — not directly reopened in this review; referenced matrix-specific assay gap should remain bounded to method qualification, not efficacy.
- `wiki/genotype-informed-supplement-workflow.md` — affected by assay availability only; no claim inspected here should treat stool butyrate measurement as exposure, ABCG2, or Q141K proof.

## New connections or implications
COMP-038’s most useful cross-corpus implication is assay-routing, not biology: future butyrate/ABCG2 or microbiome-product hypotheses need separate production, stool/exposure, target-compartment, and mechanism assays. A culture-supernatant production pass cannot stand in for intestinal-wall exposure, and a fecal electrochemical/ANN pass cannot qualify culture production QC. Research Conjecture boundary: a validated fecal Tier 2 butyrate workflow could reduce monitoring burden for stool-specific research, but only after complete-stack transfer and only as an exposure-matrix measure, not as a gout mechanism or clinical endpoint.

## Required actions
1. Update `outputs/summary.md` to include the Gu butyrate statistically nonzero negative bias, matching `results.json` and the interpretive page.
2. Reconcile `wiki/validation-experiments.md` §1.14 dashboard “4–6 weeks” with the detailed TBD-after-pilot timeline before using it in scheduling/cost rollups.
3. Preserve the regeneration warning in README/maintenance docs: any future regenerated outputs must include a newly reviewed `primary-source-verification-2026-07-24.json` equivalent and must not interpret mixed discovery/current output sets.

## Review limits
I did not execute code or independently reproduce PubMed/API retrievals. Primary-source verification is assessed from committed extraction artifacts and shard audits; I did not re-read paywalled De Baere full text. Repository fixed-string search tool failed because `rg` was unavailable, so affected-surface discovery relied on shard coverage plus targeted file reads rather than a fresh full-corpus grep. No clinical evidence or medical advice is inferred.
