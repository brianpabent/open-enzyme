COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 7aacc97a7e879d00cf653980b8e053e57a190c9c443e7da421e82ff89cf17589
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective-only propagation of comp-020 boundaries: unranked assay-specific literature inventory, low-tier RA numeric provenance, bounded search gaps, no dietary/gout efficacy
SYNTHESIS_ALLOWED_SCOPE: none when blocked
FORBIDDEN_INFERENCES: no top-tier or cross-class potency ranking; no operative gout-compartment potency; no dietary efficacy or sourcing decision; no exhaustive empty-class claims; no direct C5-convertase potency ≤100 µM claim for rosmarinic acid; no independent C5aR1 re-scan claim; no comp-018 rank/chassis inheritance

# Independent comp review — comp-020

## Reviewed snapshot
Independent daemon reviewer; bound to push-review manifest SHA-256 `7aacc97a7e879d00cf653980b8e053e57a190c9c443e7da421e82ff89cf17589` at source commit `1b57f9c213d67eda156ac41119428b0a09555ea9`. Shard auditors reported complete text inspection of the manifest files; I performed targeted cross-check reads of the experiment README, per-node findings, search log, interpretive page, and `wiki/computational-experiments.md`. Snapshot match was accepted from the supplied hash-bound daemon coverage; deterministic blocks: none.

## Bottom-line verdict
Action required. The core experiment artifact and interpretive page are appropriately bounded as Phase 1 literature mining, not a quantitative model. However, `wiki/computational-experiments.md` over-synthesizes comp-020 into “top-tier” mechanistic positions, per-node winners, and a “confirmed” convergence candidate, despite the README and interpretive page explicitly disclaiming headline compounds, comparative potency, platform priority, and cross-paper ordering.

## Implementation and constraint closure
No executable model exists; this is a literature-mining artifact with documented Paperclip/WebSearch queries. The implementation contract is therefore source-traceability, not code reproducibility. Load-bearing values traced into `outputs/per-node-findings.md` and `outputs/search-log.md`.

Constraint closure is partial and honestly described in the artifact:
- Assays are heterogeneous: CH50/AP50 hemolysis, ELISA deposition, WieLISA, C3c ELISA, cell-based C3b deposition, and direct convertase assays are not interchangeable.
- Rosmarinic acid’s 34 µM C3b deposition record is mechanistically distinct from its 1500 µM direct C5-convertase inhibition; the artifact cannot support a direct C5-convertase threshold hit.
- Polysaccharides/heparins are material-specific and often mass-concentration records; no valid molar ranking exists without exact material characterization.
- Gout-relevant exposure, residence time, protein binding, metabolism, MSU-associated access, local peaks, safety, and compartment are unresolved.
- Factor H upregulators, membrane-regulator upregulators, fungal/bacterial direct upstream modulators, and Factor B/D natural-product direct inhibitors are bounded search gaps, not universal absence proofs.
- C5aR1 was not independently re-executed in comp-020; it was ruled out by cross-reference to comp-014.

## Summary-fidelity audit
`wiki/upstream-complement-verification-rerun-computational.md` is materially faithful: it preserves in-vitro-only status, non-interchangeable assay values, exact-material requirements, unresolved delivery/exposure, no rank, no dietary efficacy, and the MSU-associated serum follow-up gate.

`wiki/computational-experiments.md` is not fully faithful. The comp-020 entry states “Three classes occupy distinct top-tier mechanistic positions within ~5–20×,” lists “Top per node,” calls luteolin “convergence-multi-mechanism candidate confirmed,” and identifies rosmarinic acid as “highest mechanistic-distinctiveness candidate.” These phrasings exceed the experiment’s own “not a ranking surface” and “no headline compound/tier/comparative potency/platform priority” boundary. ChEMBL coverage statements are directionally supportable but approximate and spot-checked; they should not be treated as precise curation-rate statistics.

The comp-039 interpretive page/source surface also needs provenance reconciliation where it treats Sahu 1999/RA numeric values as more directly verified than comp-020’s provenance permits.

## Reader-facing ownership audit
The focused comp-020 interpretive page mostly owns its evidence and reader contract: it states sourcing, exact-material, delivery, exposure, and falsification gates, and avoids personalized instructions.

The portfolio index currently imports comparison/ranking language into a tracking surface without preserving enough of the evidence boundary. It should summarize comp-020 as an unranked assay-specific inventory and route readers to the interpretive page for constraints. Cross-track rankings or “top” claims should be removed or confined to a separate portfolio comparison surface with explicit non-ranking caveats.

No narrative foil or medical advice was found in the inspected comp-020 interpretive page. Some cross-page duplication is acceptable as compact boundary text, but repeated “top-tier” wording should not propagate.

## Conjecture preservation audit
Unsupported factual claims should be corrected, not all ideas deleted. Surviving grounded conjectures:
- Rosmarinic acid remains a mechanistically distinctive upstream-complement lead because the cited record describes covalent interaction with activated C3b, but its gout-operating concentration and direct C5-convertase potency are unestablished.
- *Helicteres* lignans remain an exact-material replication conjecture, bounded by a single in-vitro paper.
- Luteolin/flavonoids and exact polysaccharide materials remain unranked assay leads, not dietary or class-wide recommendations.
- The matched assay-format mapping idea survives as a Research Conjecture: cross-paper value spreads may reflect assay step, pathway, serum dilution, material, or lab context; only matched-material, matched-condition panels can discriminate.
- Negative bounded searches do not kill future undiscovered natural-product inhibitors outside the scanned corpus.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/README.md` | experiment text | yes | Correctly disclaims headline compound, tier, comparative potency, and platform priority. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/provenance.md` | experiment input/provenance | yes via shard | RA numeric potency not primary full-text verified; multilingual work deferred. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/query-strategy.md` | experiment input | yes via shard | Strategy required multi-vendor/non-English checks; completion deferred. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/target-nodes.json` | experiment input | yes via shard | Scope pre-rules some nodes by prior corpus; not new evidence. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md` | generated output | yes | Useful unranked inventory; includes heterogeneous assay formats, comparators, inverse hits, and bounded gaps. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/outputs/search-log.md` | generated output | yes | Supports targeted Phase 1 scan, not exhaustive literature census. |
| `wiki/upstream-complement-verification-rerun-computational.md` | proposed/interpretive update | yes | Faithful and appropriately bounded. |
| `wiki/computational-experiments.md` | proposed/index update | yes | Change required: overstates ranking/top-tier/convergence claims. |
| `wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md` | affected wiki page | yes via shard | Change required for RA provenance-tier reconciliation and comp-020 scope boundaries. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/reviews/push-review.md` | affected review surface | yes via shard | No comp-020 reuse conflict found. |
| `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md` | affected tombstone | yes via shard | No active invalid comp-007 dependency found for comp-020. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| RA C3b deposition IC50 34 µM | `per-node-findings.md`, `search-log.md` | Literature record supporting mechanistic distinctiveness | PMID/search-snippet anchored; primary full text not verified in artifact | Usable only as lower-tier descriptive record. |
| RA CP/AP hemolysis 180/160 µM and direct C5 convertase 1500 µM | same | Assay heterogeneity and non-threshold direct C5-convertase boundary | Same unresolved primary verification tier | Supports heterogeneity; forbids direct C5-convertase ≤100 µM inference. |
| *Helicteres* compounds CH50/AP50 0.009/0.021 mM and 0.040/0.105 mM | `per-node-findings.md` | Single-paper lead record | Paperclip/PMC line-grep verified per log | In-vitro single-paper anchor; replication required. |
| Luteolin CH50/AP50 0.19/0.17 mM | `per-node-findings.md` | Flavonoid assay record | Paperclip/PMC line-grep verified | Descriptive in-vitro record; not target-mapped or gout-operational. |
| Heparin LP/CP/AP 2/39/76 µg/mL; C4 cleavage 102 µg/mL | `per-node-findings.md` | Assay/pathway spread | Paperclip/PMC line-grep verified | Material-specific mass units; no molar rank. |
| Marine polysaccharides ~0.98–24.65 µg/mL CP | `per-node-findings.md` | Marine class descriptive records | Paperclip/PMC line-grep verified | Exact-material in-vitro records only. |
| Bupleurum polysaccharide LP/CH50/AP50 values | `per-node-findings.md` | Polysaccharide lead records | Paperclip/PMC line-grep verified | Exact extract/material only; no class-wide conclusion. |
| ChEMBL anti-complement coverage ~20% | `per-node-findings.md` | Coverage-gap argument | Approximate spot-check, not scripted census | Directionally usable; not precise quantitative verdict. |
| Empty Factor H/CD55/CD59/CR1/fungal/bacterial classes | `per-node-findings.md`, `search-log.md` | Coverage-gap conclusion | Bounded 28 Paperclip + 2 WebSearch query trail | Bounded absence only; not universal proof. |
| C5aR1 absence | `target-nodes.json`, `per-node-findings.md` | Residual node disposition | Cross-reference to comp-014, not re-executed | Must be excluded from independent comp-020 scan claims. |

## Affected wiki pages
- `wiki/upstream-complement-verification-rerun-computational.md` — already consistent — preserves no-rank/no-gout-efficacy/no-delivery boundary.
- `wiki/computational-experiments.md` — change required — comp-020 entry overstates top-tier/per-node winner/comparative potency/convergence claims.
- `wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md` — change required — reconcile RA numeric provenance with comp-020’s snippet/abstract-tier status and avoid implying comp-020 surfaced all comp-039 candidates.
- `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/reviews/push-review.md` — already consistent — no active comp-020 conflict.
- `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md` — already consistent — comp-020 references are historical/descriptive only.
- Other linked surfaces (`complement-c5a-gout.md`, `validation-experiments.md`, `H05`, TCM/mushroom pages) were not reopened in this daemon pass; if they carry “top-tier,” “highest,” dietary, or exhaustive-empty wording, they require the same corrective boundary.

## New connections or implications
Research Conjecture: comp-020 strengthens a corpus-level warning that ChEMBL-centered triage under-detects natural-product and polysaccharide complement modulators. Premises: comp-020 spot-checks show natural-product/polysaccharide complement records missing from ChEMBL; comp-013/014 reported related database-coverage gaps. Unsupported leap: the exact missingness rate and all affected chemical spaces are not measured by a reproducible census. Discriminating observation: scripted, source-pinned ChEMBL/PubMed/PMC reconciliation for named complement assay endpoints.

Research Conjecture: matched MSU-associated complement assays should be prioritized over more literature ranking. Premises: comp-020 shows assay spreads up to 44× for RA and 50× for heparin, with unresolved compartment exposure. Unsupported leap: the spread is caused by assay format rather than material/lab/serum conditions. Discriminating observation: one exact material tested across harmonized formats plus MSU-associated C5a/C5b-9 endpoint and recovery.

## Required actions
1. Update `wiki/computational-experiments.md` comp-020 entry to remove “top-tier,” “Top per node,” “within ~5–20×,” “confirmed” convergence, and “highest” language. Verification: entry states unranked assay-specific Phase 1 inventory with no comparative potency/platform priority.
2. Add/adjust RA provenance language wherever comp-020 or comp-039 uses Sahu/Englberger/Peake numeric values. Verification: full-text-unverified or primary-verification status is explicit; numeric values are not presented as high-confidence primary-verified anchors unless verification is actually added.
3. Ensure all downstream pages using comp-020 preserve bounded search-gap language for Factor H, membrane regulators, fungal/bacterial classes, and C5aR1. Verification: no universal “empty class” or independent C5aR1 rerun claim remains.
4. Preserve material-specific wording for heparin, polysaccharides, *Helicteres*, RA, and luteolin. Verification: no dietary efficacy, botanical-name-only sourcing, molar cross-rank, gout compartment potency, or wet-lab priority is inferred from comp-020 alone.

## Review limits
I did not execute code; none exists for this literature-mining comp. Primary papers were not independently fetched beyond the committed text/provenance and shard-reported inspection; RA primary full-text verification remains unresolved. Repository search tool failed because `rg` was unavailable, so affected-surface discovery relied on shard coverage plus targeted file reads rather than complete fresh grep. Other linked wiki pages not in the daemon manifest were not fully reopened in this pass.
