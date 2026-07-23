ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: e94a028963cd9fce98fbe066e6cae26bad7501530ecc9582d34de89f86b11fdc

# Independent comp review — comp-019

## Reviewed snapshot

Reviewer `/root/comp019_post_review_final`; authoring-time Gate 2 manifest canonical SHA-256 `e94a028963cd9fce98fbe066e6cae26bad7501530ecc9582d34de89f86b11fdc`. The manifest file’s byte-level SHA-256 is `22b19e901b0410781b4851a2f8e9ac446e701c7f5093d58307bb086dd56a1497`. All seven manifest entries matched their recorded byte counts and SHA-256 hashes and were inspected completely.

The two queue deletions were inspected separately because they are intentionally outside the manifest. Both files are absent from the working tree, and their prior required actions were compared directly with the current bound surfaces.

## Bottom-line verdict

Clean. This exact metadata-only tombstone and downstream-consistency batch accurately routes the current UOX evidence owners, separates COMP-044’s deterministic audit result from the mechanistic inference that routes unresolved constraints to validation §1.33, directly source-justifies `yanthine`, and preserves the complete prohibition on COMP-019 quantitative or decision reuse.

The current actions in both `synthesis/queue/comp-review-019.md` and `synthesis/queue/comp-review-044.md` are closed. Both queue files are genuinely deletable in this batch.

## Implementation and constraint closure

The live non-review COMP-019 directory contains only `README.md` and `invalidation.json`. It contains no code, inputs, outputs, executable, symlink, bytecode, reproduction command, or result-bearing artifact. The README’s `git show` example retrieves historical source for audit; it does not execute or restore the retired model.

The retirement ledger was independently checked against commit `dc7f4d2047dfb3bd378ee7a73618a11b67217257`. All nine retired blobs matched their recorded byte counts and hashes, and the canonical retired-file-set digest recomputed to `ce744f989acb744a78f365e3a61f0154dc300545b7b4843ae05851bb5722529e`.

Static inspection of the retired model confirmed the invalidation basis: the capacity calculation used nominal specific activity for 1,440 minutes per day and compared that saturated capacity with genotype-scaled daily intestinal flux. The stored physiological luminal-urate concentration and UOX Km did not enter `evaluate_scenario`, and no finite physiological exposure window constrained the result. The live tombstone therefore correctly invalidates every Phase B ΔSUA, capacity, genotype-order, dose, yield, trial, efficacy, safety, and topology/chassis conclusion.

Current evidence ownership is coherent:

- the COMP-019 interpretation owns the invalidation boundary and bounded dated search observation;
- COMP-044 owns the deterministic physiological-regime consistency audit;
- COMP-045 owns the topology × oxygen × peroxide experimental design without selecting a topology;
- validation §1.33 owns configuration-level physiological comparison;
- validation §1.36 owns the subsequent antioxidant-loss and peroxide safety gate.

## Summary-fidelity audit

The only surviving COMP-019 observation remains bounded to the sources searched as of 2026-05-08: no Q141K-stratified uricase clinical outcome was identified in that searched corpus. Every inspected surface explicitly rejects treating this as universal absence.

The README, invalidation record, computational index, current COMP-019 interpretation, COMP-044 interpretation, H08, graph, open-questions page, and validation plan consistently reject any replacement ΔSUA, dose, genotype ordering, physiological regime, efficacy model, topology/chassis selection, production target, or safety conclusion.

The graph now makes the required provenance distinction:

- “legacy flat-dose classification not robust under the tested diagnostics” is labeled a **Deterministic Computational Audit**;
- routing unresolved substrate, oxygen, localization, and peroxide constraints to §1.33 is labeled **Mechanistic Extrapolation**;
- the edge itself says the audit “motivates empirical closure,” rather than implying that COMP-044 supplied biological validation.

The validation dashboard and protocol are consistent. The deterministic checker passed; 52 dashboard IDs match 52 numbered protocol sections. The previously relevant planning discrepancies are closed:

- §1.10 agrees on `$2,460–4,460`, `3–4` weeks, a four-lane core, and an optional separately costed fifth lane;
- §1.20 agrees on a 3×3 factorial plus a separately declared midpoint when needed;
- §1.22 agrees on `$5,000–8,000` and `8–10` weeks;
- §1.25 agrees on `$4,445–6,745 (two-arm)`, `6–8` weeks, and mandatory RIB40 plus NSlD-ΔP10 arms;
- all numbered sections, including §§1.26–1.32, are represented in the dashboard;
- §§1.33 and 1.34 agree with their dashboard `TBD` cost and duration metadata.

## Reader-facing ownership audit

The tombstone is concise and archival rather than explanatory duplication of the retired model. It directs readers to current evidence owners without ranking sequences, hosts, topologies, or product formats.

The graph remains a routing surface rather than an evidence home. COMP-045 keeps topology conclusions configuration-specific and leaves all tested topologies open. Validation §1.33 owns the empirical decision rule and explicitly prohibits serum-urate, dose, production, or cross-host winner claims.

No proposed change introduces personalized treatment instructions, a cross-track narrative foil, or duplicated scientific exposition.

## Conjecture preservation audit

The batch kills only COMP-019’s invalid Phase B numerical and decision scope. It does not kill the gut-lumen UOX hypothesis, ABCG2/Q141K as a prospective stratification variable, or the possibility that a specific configuration may pass physiological substrate, oxygen, localization, persistence, peroxide, and safety gates.

H08 remains open. COMP-045 eliminates no topology. Q141K remains a prospective variable with unresolved direction and magnitude. These surviving ideas are correctly routed to empirical discrimination rather than presented as COMP-019 results.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` | design | Yes | Clean non-runnable tombstone; COMP-045 now included among current evidence owners. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/invalidation.json` | design | Yes | Hash-bound retirement record; COMP-045 included symmetrically in `superseded_by`; invalidated and surviving scopes unchanged. |
| `wiki/computational-experiments.md` | proposed update | Yes | COMP-019 remains non-decision-usable; COMP-044 numbers appear only as a bounded internal-consistency counterexample. |
| `wiki/etc/GRAPH.md` | proposed update | Yes | Correctly separates deterministic audit provenance from mechanistic routing to §1.33. |
| `wiki/open-questions.md` | proposed update | Yes | `yanthine` terminology and evidence tier are now source-justified and appropriately caveated. |
| `wiki/uricase-topology-oxygen-peroxide-design-computational.md` | proposed update | Yes | COMP-045 owns experimental design; no topology, efficacy, dose, or safety winner asserted. |
| `wiki/validation-experiments.md` | proposed update | Yes | Dashboard/protocol metadata consistent; §§1.33, 1.34, and 1.36 preserve the required UOX boundaries. |
| `synthesis/queue/comp-review-019.md` | out-of-manifest queue deletion | Yes | Every listed action is closed; deletion verified in the working tree. |
| `synthesis/queue/comp-review-044.md` | out-of-manifest queue deletion | Yes | Every listed action is closed; deletion verified in the working tree. |

There are no generated outputs in this metadata-only post-run manifest.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Gate 2 snapshot | `post-run.manifest.json` | Exact review binding | Canonical digest recomputed; seven entries hash-matched | Pass |
| Retired nine-file ledger | `invalidation.json`; retired Git commit | Historical auditability only | Every blob byte count/hash matched | Pass |
| Retired-file-set digest | `invalidation.json` | Detect ledger alteration | Independently recomputed exactly | Pass |
| COMP-019 failure boundary | Retired `flux_model.py`; live tombstone | Prohibit Phase B reuse | Static code inspection confirmed no physiological substrate occupancy or finite active window in the decision calculation | Pass |
| COMP-045 ownership | README, invalidation record, computational index, COMP-045 page | Route topology/oxygen/peroxide design | Present on all relevant current surfaces; no topology selected | Pass |
| COMP-044 provenance split | `wiki/etc/GRAPH.md` | Distinguish audit result from experimental-routing inference | Explicit deterministic-audit and Mechanistic-Extrapolation labels | Pass |
| Validation dashboard coverage | `wiki/validation-experiments.md` | Planning consistency | 52 dashboard rows equal 52 numbered sections; checker passed | Pass |
| §1.33 decision boundary | Validation §1.33 | Empirical configuration gate | Requires product at human-baseline prior with matched peroxide/viability controls; forbids dose, serum, production, and cross-host conclusions | Pass |
| `yanthine` identity | Open questions; validation §1.34 | PDB intermediate nomenclature | [Li et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507026/) identifies UA reduction to 2,8-dioxopurine (`yanthine`), confirms the product by LC-MS and co-elution with a commercial standard, and treats xanthine as a distinct route | Pass |
| `yanthine` biomarker scope | Open questions | Candidate analytical readout | Primary study reports a small serum case-control result; current text calls it a Human Observational biomarker candidate, not validated individual function | Pass |
| No COMP-019 quantitative restoration | Current corpus search and all bound pages | Prevent stale decision reuse | Quantitative values occur only as explicitly bounded COMP-044 audit comparisons or retired-history warnings | Pass |
| Queue closure | Both deleted queue files versus current surfaces | Remove resolved actions | COMP-045 routing, graph provenance, validation consistency, nomenclature, invalidation policy, and forbidden-inference boundaries all closed | Pass |

## Affected wiki pages

- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` — already consistent — complete current-owner routing and non-runnable boundary.
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/invalidation.json` — already consistent — machine-readable owner and invalidation scopes agree with README.
- `wiki/computational-experiments.md` — already consistent — tombstone, bounded survivor, and replacement gates are accurate.
- `wiki/etc/GRAPH.md` — already consistent — deterministic audit and mechanistic routing are separated.
- `wiki/open-questions.md` — already consistent — `yanthine` is directly justified and appropriately bounded.
- `wiki/uricase-topology-oxygen-peroxide-design-computational.md` — already consistent — no topology elimination or transferable winner.
- `wiki/validation-experiments.md` — already consistent — dashboard and protocols agree; §§1.33, 1.34, and 1.36 own the correct empirical gates.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — no Phase B result survives.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — COMP-044 remains a bounded audit, not a replacement model.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — hypothesis remains open and non-numeric.
- `index.md` — already consistent — COMP-044 is summarized with all forbidden inferences explicit.
- `synthesis/queue/comp-review-019.md` — actions closed; delete.
- `synthesis/queue/comp-review-044.md` — actions closed; delete.

## New connections or implications

None found. This batch closes archival and routing consistency only; it introduces no new scientific result or mechanistic claim.

## Required actions

None.

## Review limits

No COMP-019 or COMP-044 experiment/result-bearing logic was executed. The retired COMP-019 implementation was inspected statically, and its Git blobs and ledger were hash-verified. The dated 2026-05-08 Phase A literature search was not rerun, so its survivor remains valid only as the explicitly bounded searched-corpus observation. The Li et al. primary article was inspected directly for `yanthine`; other COMP-045 primary claims were not independently re-reviewed because this batch changes ownership metadata rather than COMP-045’s scientific result.
