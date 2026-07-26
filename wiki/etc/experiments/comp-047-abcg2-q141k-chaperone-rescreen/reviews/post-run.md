ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 653f8371398e01f8c5db1813984f1a161a2163d5cbf6eb5e94e4d6fc8b47b3ea

# Adversarial post-run review — comp-047

## Verdict

**PASS.** The corrected artifact supports the narrow conclusion that this
static docking configuration produces no defensible Q141K-chaperone ranking. It
does not reject the broader Q141K rescue hypothesis.

No required action remains. The six-action COMP-047 synthesis queue is fully
resolved and should be deleted in the completion commit.

## Exact snapshot and lifecycle

- Post-manifest verification passed at the digest above.
- The pre-run receipt passed at
  `0d309f67efc46529fc8d2a61fe31dbf60c28461aeca4d2c318685b3f7aa93b49`.
- All 22 pre/post design entries are identical by path, bytes, and SHA-256.
- All seven frozen pre-run output baselines equal the post-run outputs.
- The post manifest covers all nine authorized updates.

## Executable result

Independent traversal and recomputation of all 135 result rows found no merge,
tier, margin, selectivity, exclusion, or final-candidate discrepancy.

- Attempted molecules: **135**
- Complete docking-score rows: **134**
- Original docking tiers: **132 `no`, 2 `uncertain`, 1 `error`**
- Final executable result: **134 `no`, 1 `uncertain`, 0 `yes`**
- Sole executable row: **vorinostat, `uncertain`**
- Rosuvastatin: `substrate_disqualified: true`,
  `drugbank_abcg2_interacting: true`, `final_known_abcg2: true`,
  `wetlab_candidate: "no"`
- Vorinostat: no frozen ChEMBL-activity or DrugBank-relationship flag,
  `final_known_abcg2: false`, `wetlab_candidate: "uncertain"`

The FDA CRESTOR label independently supports rosuvastatin's BCRP-substrate
classification. Basseville et al. (PMID 22472121) supports the separate
**In Vitro** vorinostat/romidepsin/panobinostat trafficking and
drug-substrate-efflux rescue precedent. The corpus keeps that phenotype
independent of the docking row.

## Generated outputs

| Output | SHA-256 |
|---|---|
| `chembl_axis2.json` | `034706fc6f1cb9e8739f4755d7e1c32282d0f381997513268f149bb9acbd352c` |
| `controls.md` | `f07b893f26bf23fa776eb8cf2c96c4d8845e6c77ae2ae9d129c50518099bc9ba` |
| `drugbank_substrate_axis.json` | `2345c9a721784683a03c10dfc9da17bd9eceb19c1ab15c7cf909a6434ade74e9` |
| `receptor_verification.json` | `83bddfeef563b4c20b2ebe51edfcdfbe0f8e46694c3c1cc7d943e59059b4f17e` |
| `results.json` | `91b96283ccda185107b32c31e2dfad4c7b045135435304240f812235203ee9a0` |
| `sensitivity.json` | `95b7ea59e49a0399e4161debbb8c24f345297ceb003c8fb6be98e5e9214a41ba` |
| `summary.md` | `92768759e1acb0d79e545d4f74e12f19b778e2931f695905474a1e62eb470caa` |

The deterministic standard-library merger and receptor verifier contain no
generated timestamps. Exact equality between pre-run baselines and post-run
outputs supplies lifecycle-level repeat evidence.

## Receptor integrity

Independent parsing confirms:

- clean WT/Q141K PDBs: 5,087 atoms and 655 residues each;
- WT/Q141K PDBQTs: 6,190 atoms and 655 residues each;
- expected GLN141 and LYS141 atom sets;
- byte-identical clean-structure ATOM records outside residue 141;
- the same single nonstandard PDBQT residue, `A:655:UNK`, in both files;
- expected 22 Å boxes and independently recomputed 32.61 Å separation;
- every receptor and box hash in `receptor_expected.json`.

The symmetric `SER655`→`UNK` warning and missing historical
score-to-receptor provenance are disclosed.

## Controls and sensitivity

The four CFTR correctors are cross-protein chaperone-mechanism comparators, not
validated ABCG2 positives. None reaches an executable tier. That is a setup
diagnostic, not an ABCG2-chaperone sensitivity estimate or evidence against a
rescuable site.

All curated ABCG2 negative controls remain non-executable. This tests the
exclusion layer, not the fold-site ranking.

The sensitivity artifact tracks 16 molecules across 10 fold-site@Q141K
conditions. Across the nine non-base conditions, 2–7 of eight candidate
positions changed. Reader-facing text uses this only to reject robustness of
the base ordering; it does not claim pocket absence or a globally robust null.

## Evidence-axis and process semantics

- Axis 2a is bounded ChEMBL **activity** evidence.
- Axis 2b is a UniProt-exposed DrugBank **relationship** flag.
- A generic relationship flag can conservatively exclude a row but cannot
  assign substrate or inhibitor subtype.
- Rosuvastatin's subtype comes from the FDA label.
- Axis 2 can exclude but cannot promote or establish rescue.

The reusable ChEMBL guidance now states that source hierarchy. The shared helper
is internally consistent:

- API: `chembl_activity()` and `build_conservative_exclusions()`
- fields: `chembl_activity`, `drugbank_relationship`,
  `conservative_exclusion`
- top-level collection: `conservative_exclusions`
- CLI, metadata, documentation, and smoke behavior use the same semantics
- no repository caller depends on the removed schema

## Affected surfaces

| Surface | Review conclusion |
|---|---|
| `index.md` | Correct compact verdict and survivor/exclusion boundary. |
| canonical COMP-047 page | Owns result, limits, receptor verification, surviving hypothesis, and §1.22 handoff. |
| `computational-experiments.md` | Registry and tracking row match the executable artifact. |
| superseded COMP-032 page | Ranking is retired; compounds remain unranked hypotheses. |
| `chassis-pending-interventions.md` | Route remains unvalidated; no compounding decision. |
| `abcg2-modulators.md` | Phenotypic rescue stays separate from direct-binding claims. |
| validation §1.22 | Owns trafficking, urate-flux, inhibition, exposure, viability, and barrier gates. |
| ChEMBL guidance | Relationship-versus-subtype rule prevents recurrence. |
| shared helper | API/schema implements activity/relationship exclusion semantics. |

No unauthorized hypothesis card, intervention page, portfolio reranking, or
unrelated Q141K/butyrate propagation is present.

## Hypothesis and invalidation scope

The correction kills only the decision-usable ranking produced by this static
configuration. It preserves the Q141K rescue route, independent **In Vitro**
HDAC-directed rescue evidence, the COMP-032 compounds as an unranked hypothesis
inventory, future folding-ensemble/ΔΔG work as a new experiment, and the
possibility of a direct chaperone outside the tested setup.

## Queue closure

All six `synthesis/queue/comp-review-047.md` actions are closed:

1. Axis 2b and independent substrate exclusion are executable.
2. Result and reports agree on rosuvastatin exclusion and marginal vorinostat.
3. The registry reflects sensitivity, both Axis-2 checks, and the verdict.
4. Reproduction is portable and fail-closed; private paths are removed.
5. Validation follow-up is specifically registered in §1.22.
6. Receptor intermediates are hash-, count-, mutation-, warning-, and
   geometry-verified.

**Queue-deletion verdict: delete the queue item in this completion commit.**

## Review limits

- The reviewer did not run result-bearing COMP scripts.
- The historical docking environment lacks a complete exact lock.
- The frozen external evidence sets were audited for semantics and fidelity,
  not refreshed.
- Push review remains a separate gate.

## Required actions

None.
