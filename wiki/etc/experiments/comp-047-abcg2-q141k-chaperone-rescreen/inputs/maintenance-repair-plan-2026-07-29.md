# COMP-047 bounded maintenance repair plan

## Question

Can the current frozen COMP-047 artifact be made exactly reviewable while
correcting count, sensitivity-scope, and Axis-2 semantics without rerunning
docking or changing its candidate tiers?

## Authorized execution

After Gate 1, run only:

```bash
python3 build_results.py
```

Run it twice and require identical hashes for:

- `outputs/results.json`
- `outputs/controls.md`
- `outputs/summary.md`
- `outputs/receptor_verification.json`

Do not run `analyze.py`, `sensitivity.py`, `repair.py`, `prep_receptor.py`, or
`resolve_smiles.py`. Do not access PubChem, ChEMBL, DrugBank, UniProt, Vina, or
Open Babel.

## Fixed evidence

- `outputs/results.json` contains 135 result rows. Exactly 134 have complete
  fold-Q141K, fold-WT, and Walker-A scores; `cyclosporine_a` is incomplete.
- `logs/run.log` is a UTF-8 text artifact and records the incomplete
  `cyclosporine_a` row.
- `outputs/sensitivity.json` records only the Q141K fold-site panel named in
  `sensitivity.py`: base, x +2 Å, x -2 Å, y +2 Å, +3 Å xyz diagonal, size 18 Å,
  size 26 Å, two alternate seeds, and neutral ligand preparation.
- `outputs/chembl_axis2.json` and
  `outputs/drugbank_substrate_axis.json` remain separate evidence axes.
  `has_activity=false` means no activity record in the bounded ChEMBL check; it
  does not establish absence of an ABCG2 substrate, inhibitor, or other
  relationship. DrugBank flags establish a relationship only, not a subtype.

## Planned changes

1. Treat `.log` files as inspectable text in push-review sharding and cover the
   behavior with a regression test.
2. Render `135 attempted / 134 complete / cyclosporine_a incomplete`
   consistently.
3. Describe the exact limited sensitivity panel and restrict its implication
   to Q141K fold-site score/rank stability.
4. Replace broad ChEMBL-absence wording with bounded-record language.
5. Record the immutable-output, ligand-hash, process-log, and live-query
   snapshot contract required for any future re-dock.

## Scientific and invalidation boundary

The current disposition remains **INCONCLUSIVE — no defensible docking-backed
candidate ranking**. The repair cannot promote or demote any molecule, infer
binding or chaperone activity, invalidate Q141K rescue, or establish absence of
an ABCG2 relationship. Vorinostat remains a marginal non-priority docking-tier
row; its independent phenotypic precedent is not docking validation.

## Failure criteria

Stop without closing the queue item if:

- the pre-run manifest or receipt does not validate exactly;
- either deterministic build changes a docking score, candidate tier, Axis-2
  flag, or result-row identity;
- the two output hash sets differ;
- the run requires a docking or live-query tool;
- the run log remains classified as binary; or
- Gate 2 identifies any unresolved scientific, implementation, provenance, or
  interpretation defect.

## Proposed external surface

- `wiki/abcg2-q141k-chaperone-rescreen-computational.md`

No other reader-facing page is expected to change unless the correction-cascade
grep finds an active stale count, sensitivity, or Axis-2 statement.
