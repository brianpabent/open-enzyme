# COMP-038 maintenance repair plan

**Mode:** Non-result-bearing reproducibility repair  
**Scientific decision:** Unchanged  
**Canonical evidence home:** `wiki/tier-2-butyrate-assay-audit-computational.md`

## Defect being repaired

The current scientific result is controlled by
`outputs/primary-source-verification-2026-07-24.json`, but the legacy
discovery runner has two explicit modes that can replace
`pubmed-snapshot.json`, `results.json`, and `summary.md` without acknowledging
that controlling artifact. Its default integrity check also omits the
verification JSON.

## Planned implementation

1. Keep the default command read-only.
2. Require `--regenerate-current-outputs` together with either
   `--prepare-codex` or `--run-openrouter` before any network access or output
   replacement.
3. Make the two mutation modes mutually exclusive.
4. Reject `--regenerate-current-outputs` when no mutation mode is selected.
5. Include `outputs/primary-source-verification-2026-07-24.json` in the
   default required-file check and require every expected path to be a regular
   file.
6. Keep every default failure path read-only, including when `outputs/` is
   absent.
7. Bind a COMP-local behavioral regression suite to the exact manifest.

The repair will not execute either mutation mode and will not alter a
scientific output. The explicit authorization flag prevents accidental
replacement; it does not authorize use of regenerated results without a new
reviewed lifecycle.

## Planned verification

After Gate 1 passes, run from
`wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/` with CPython
3.14.5:

```bash
python3 -m unittest -v test_maintenance.py
python3 analyze.py
python3 analyze.py
python3 analyze.py --prepare-codex
python3 analyze.py --run-openrouter
python3 analyze.py --regenerate-current-outputs
python3 analyze.py --prepare-codex --run-openrouter
```

The test suite and the two default commands must exit 0. Each of the final
four commands must exit 2 before environment loading, network access, output
directory creation, or output mutation and must name the missing,
incompatible, or mutually exclusive authorization state.

Before and after the commands, run this from the repository root:

```bash
git diff --exit-code -- wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs
```

Both comparisons must exit 0. The COMP-local tests create isolated temporary
trees to prove that a missing verification JSON fails with exit 1, an absent
output directory is not created, directory-shaped output paths are rejected,
and current-file hashes remain unchanged.

Finally, `python3 -m unittest discover -s tests` from the repository root must
exit 0. These maintenance checks use only the Python standard library plus the
manifest-bound repository helper. No random seed, environment secret, network
service, or external-model version applies because all reviewed paths must
stop before those facilities are invoked.

Authorized regeneration is outside this maintenance execution and remains
non-atomic. Before any future authorized run, the outputs directory must match
a committed reviewed snapshot. If regeneration fails after a partial write,
discard the entire outputs-directory working-tree delta and restore the
committed snapshot before retrying; do not retain or interpret a mixed set.

## Interpretation update

`wiki/computational-experiments.md` may retain the source-study Gu performance
numbers only when it also states that they came from the exact published
hardware–chemistry–model stack, that butyrate had a small statistically
nonzero negative bias, and that independent external transfer remains open.
No treatment, exposure, ABCG2, Q141K, gout-efficacy, safety, or cross-matrix
claim is authorized.

## Failure criteria

The repair fails if:

- a historical mutation mode reaches network or write logic without the
  explicit authorization flag;
- the default check passes when the controlling verification JSON is absent;
- a default failure creates the absent output directory or accepts an expected
  output path that is not a regular file;
- any current generated output changes during the bounded verification run;
- the scientific YELLOW verdict or its matrix boundaries change; or
- the exact post-run review requires further action.
