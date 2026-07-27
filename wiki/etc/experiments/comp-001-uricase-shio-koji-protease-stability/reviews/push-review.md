COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 79de417c28c4d4644b70962752e06c0e302a7d3c2984e60ee813fba4fd991cb9
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective/proxy-only COMP-001 boundary and empirical-gate reminders only
SYNTHESIS_ALLOWED_SCOPE: use only as deterministic fixed-filter inventory for Q00511 plus pLDDT context, with empirical protease risk unresolved
FORBIDDEN_INFERENCES: protease survival; LOW/MODERATE/HIGH risk; solvent accessibility or burial; cleavage probability; retained UOX activity; fermentation performance; production/secretion/dose/shelf-life/gastric-transit/target-compartment exposure; benchmark transfer to other payloads or COMPs; clinical evidence or medical advice

# Independent comp review — comp-001

## Reviewed snapshot
Independent daemon reviewer; push manifest SHA-256 `79de417c28c4d4644b70962752e06c0e302a7d3c2984e60ee813fba4fd991cb9`; source commit `0ef99dcc9102323608fc4e5384e09617e95e17e8`. Shard coverage reports complete inspection of the COMP-001 artifact text, generated outputs, and relevant wiki surfaces. I performed targeted cross-checks of the COMP README, code, inputs/provenance, output summary, interpretive page, registry segments available through tool reads, and validation pages via shard audit. Snapshot is treated as matched; no deterministic binary block was reported.

## Bottom-line verdict
Action required, but the scientific result is usable only in a narrow corrective/proxy scope. The implementation appears to answer the stated narrow question—enumerating Q00511 adjacent-pair matches to three fixed legacy filters and reporting local AlphaFold pLDDT context—but it does not and cannot resolve protease stability, cleavage, accessibility, retained activity, or shio-koji survival. One reader-facing issue remains: the interpretive page’s registry anchor is likely stale/mismatched and should be corrected. Primary sources were not independently re-fetched in this review.

## Implementation and constraint closure
The computation is a deterministic sequence/filter enumeration, not a biological proteolysis model. The code loads a fixed Q00511 FASTA, pLDDT JSON, and legacy filter JSON; validates sequence SHA-256, position–residue–pLDDT mapping SHA-256, finite pLDDT in `[0,100]`, exact 1..302 position coverage, canonical residues, unique rule IDs, and explicit legacy-provenance status. It then enumerates every peptide bond where P1/P1′ satisfy each Boolean filter and reports an inclusive local window of P1/P1′ plus up to three residues on either side, truncated at termini. Self-checks cover first bond, internal bond, and terminal K301/L302 behavior.

No hidden physiological-rate substitution was found because the current artifact explicitly avoids rate, cleavage, exposure, or activity claims. The dominant constraints remain unclosed by design: protease identity/concentration/specificity, solvent exposure/SASA, folding state in the ferment, secretion/localization, finite protease exposure time, salt/pH/matrix effects, residence time, replenishment, product/activity retention, and off-target/safety burdens. Sensitivity is also bounded: no inferential sensitivity analysis is planned because this is an exact enumeration of fixed filters; alternate filter encodings or pLDDT window widths are new designs requiring fresh review.

The load-bearing implementation numbers inspected are internally consistent: sequence length 302; mean pLDDT 97.13612582781457 rounded to 97.14; minimum 80.50; maximum 98.94; 293 residues ≥90 and 9 residues 70–<90; filter match totals ALP 215, NPr 97, acid-protease 44; lowest local mean pLDDT 84.54, 84.54, and 93.52 respectively.

## Summary-fidelity audit
`outputs/summary.md`, the COMP README, and the interpretive page preserve the core boundary: **PROXY ONLY — EMPIRICAL PROTEASE RISK UNRESOLVED**. They correctly state that legacy arrays lack claim-level provenance, pLDDT is model confidence rather than solvent accessibility, and §1.10 retained-activity testing remains the feasibility gate.

The computational registry and validation §1.10, as audited by shards, are materially aligned: COMP-001 is not a validated protease-stability benchmark; it cannot support cross-payload survival comparisons; and it cannot validate pLDDT-to-accessibility mapping for later DAF/CD55 or stalk-truncation claims. The direct UOX dependent thermal-stability page also appears reconciled by distinguishing thermal in-vitro facts from ferment survival predictions and by labeling multi-day attrition as conjecture.

Mismatch/action item: `wiki/uricase-protease-stability-computational.md` links to a registry fragment that appears stale/fragile for the current comp-001 heading. This is reader-facing navigation drift, not a quantitative-result defect.

## Reader-facing ownership audit
The focused interpretive page owns the COMP-001 evidence boundary and does not turn the computation into portfolio priority, chassis winner, treatment instruction, or fermentation recommendation. Cross-track benchmark transfer is appropriately barred in registry and validation surfaces. I found no personalized treatment advice or clinical-evidence upgrade in the inspected COMP-001 surfaces.

The page placement is acceptable: focused COMP page for evidence, registry for index status, validation §1.10 for the empirical gate. The remaining link-anchor drift should be fixed without adding long duplicated exposition.

## Conjecture preservation audit
Unsupported factual assertions about protease survival, LOW-risk classification, accessibility, retained UOX activity, and ferment performance have been corrected or bounded. The useful idea survives as a compact Phase 0 conjecture: secreted UOX may fail if the actual shio-koji process destroys abundance or activity, and the discriminating observation is a direct retained-activity time-course in the exact matrix. Negative/limited COMP-001 results kill only pLDDT/filter-derived stability claims, not the broader uricase intervention, other routes, or exact-material empirical testing.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/README.md` | COMP artifact text | Yes | Correct proxy-only boundary; reproduce command/deps stated; follow-up corpus-search requirement noted. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/analyze.py` | COMP code | Yes | Deterministic enumeration with input/hash/schema validation; no biological-risk derivation. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/Q00511.fasta` | COMP input | Yes | Fixed 302-aa Q00511 sequence; hash checked by code. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/alphafold_Q00511_plddt.json` | COMP input | Yes | Complete pLDDT vector; code validates exact aligned mapping. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/legacy_preference_filters.json` | COMP input | Yes | Legacy Boolean filters only; claim-level provenance absent. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/provenance.md` | COMP provenance | Yes | Names UniProt/AlphaFold sources and transformation; primary-source re-fetch not performed in this review. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/cleavage_sites.json` | generated output | Yes | Quantitative inventory consistent with code and summary. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/summary.md` | generated output | Yes | Summary faithfully bounded; rounded values match JSON. |
| `wiki/computational-experiments.md` | proposed/affected wiki update | Yes, via shard coverage and targeted reads | Registry boundaries align; COMP-001 not a benchmark. |
| `wiki/uricase-protease-stability-computational.md` | proposed/affected wiki update | Yes | Scientifically aligned; registry anchor likely stale. |
| `wiki/uricase-shio-koji-thermal-stability-computational.md` | affected wiki page | Yes | Direct UOX dependent appears reconciled and separately bounded. |
| `wiki/validation-experiments.md` | affected wiki page | Yes, full shard coverage | §1.10 correctly makes retained-activity assay decisive and bars model-score-only pass. |
| `wiki/etc/experiments/comp-032-abcg2-q141k-chaperone-screen/inputs/provenance.md` | unrelated manifest text | Yes | No COMP-001 propagation issue; separate comp-032 provenance limitations noted by shard. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Q00511 sequence length 302 | FASTA; code; JSON output | Enumerated peptide bonds and pLDDT coverage | UniProt Q00511 release named; not re-fetched here | Usable as committed input; primary-source verification unresolved. |
| Sequence SHA-256 `cb5d...f877` | `analyze.py`, provenance | Hard validation before output | Artifact-internal hash | Implementation closed. |
| pLDDT mapping SHA-256 `90ab...2f80` | `analyze.py`, provenance | Hard validation of aligned position/residue/pLDDT vector | AlphaFold DB model named; extraction described; not re-fetched here | Implementation closed; primary-source verification unresolved. |
| AlphaFold pLDDT meaning | provenance, summary, interpretive page | Descriptive confidence bins only | AlphaFold DB FAQ named | Correctly not used as accessibility/risk. |
| Legacy ALP/NPr/acid-protease arrays | `legacy_preference_filters.json` | Boolean inclusion filters | Legacy encoding; claim-level provenance absent | Usable only as fixed code filters, not specificity rules. |
| Window definition P1/P1′ ±3 residues | README, code, output | Computes local mean pLDDT | Prespecified design | Closed; alternate windows require new design. |
| Match totals 215/97/44 | `cleavage_sites.json`, summary | Reported result | Derived from committed sequence/filter enumeration | Internally consistent. |
| Lowest local means 84.54/84.54/93.52 | JSON, summary | Reported descriptive context | Derived from committed pLDDT vector | Internally consistent. |
| “Empirical protease risk unresolved” | README, outputs, wiki | Verdict boundary | Follows from model limitations | Supported. |
| §1.10 retained-activity gate | README, interpretive page, validation | Required empirical discriminator | Protocol is proposed/design-stage | Correct gate; its thresholds remain provisional unless separately frozen. |

## Affected wiki pages
- `wiki/uricase-protease-stability-computational.md` — change required — scientific boundary is consistent, but registry anchor link should be corrected to the actual `wiki/computational-experiments.md` heading/slug.
- `wiki/computational-experiments.md` — already consistent — COMP-001 is proxy-only and not a protease-stability benchmark; related comp-006/012 warnings block benchmark transfer.
- `wiki/validation-experiments.md` — already consistent — §1.10 requires direct UOX abundance/activity in actual ferment and rejects model-score-only passage.
- `wiki/uricase-shio-koji-thermal-stability-computational.md` — already consistent — separates thermal proxy/conjecture from direct ferment retention evidence.
- `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/summary.md` — already consistent — generated summary matches JSON and code boundaries.
- `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/README.md` — already consistent — command/dependencies and decision boundary are stated.

## New connections or implications
Research Conjecture boundary: COMP-001 and the invalidated/limited pLDDT-proxy history across COMP-005/012 jointly support a corpus-wide rule that pLDDT-confidence windows may be retained as descriptive structural-confidence context but must not be promoted to protease-accessibility, cleavage, or survival evidence for any payload. The discriminating observation remains exact expressed-product retention/function testing in the real process matrix.

## Required actions
1. Fix the registry link in `wiki/uricase-protease-stability-computational.md` so it resolves to the actual COMP-001 heading in `wiki/computational-experiments.md`; verify by checking the rendered anchor or using a stable file/folder link if heading slugs remain fragile.
2. Preserve propagation limits in any downstream synthesis: COMP-001 may be cited only for deterministic fixed-filter match counts and pLDDT context, never as protease stability, ferment survival, or benchmark evidence.
3. If COMP-001 source provenance becomes load-bearing beyond committed-input reproducibility, independently re-fetch/verify UniProt Q00511 and AlphaFold `AF-Q00511-F1-model_v6` rather than relying on citation strings.

## Review limits
I did not execute `python3 analyze.py`; daemon mode relies on inspection and shard audits. I did not independently re-fetch UniProt, AlphaFold DB, MEROPS, or cited protease-specificity sources. Repository grep was unavailable in this environment, so corpus search relied on shard-bound full/targeted inspections and targeted file reads rather than live full-text search. No binary artifacts were reported in the deterministic-block list.
