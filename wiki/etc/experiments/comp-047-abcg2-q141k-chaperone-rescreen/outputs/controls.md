# comp-047 — Control performance (validity check)

Generated 2026-07-15. N=134 molecules with valid docking.

Columns: fold@Q141K / fold@WT / transport (Walker A) affinities (kcal/mol, more negative = stronger); margin = transport − fold@Q141K (>0 = fold-selective); fold-rank = rank of fold@Q141K among all molecules (1 = strongest fold binder).

## POSITIVE controls — CFTR correctors (must EARN rank, no prior)

| molecule | fold@Q141K | fold@WT | transport | margin | fold-rank | chaperone tier | wetlab candidate |
|---|---|---|---|---|---|---|---|
| lumacaftor | -7.35 | -7.03 | -8.77 | -1.42 | 2/134 | no | no |
| tezacaftor | -5.91 | -5.61 | -7.35 | -1.44 | 16/134 | no | no |
| elexacaftor | -5.80 | -6.21 | -7.75 | -1.95 | 18/134 | no | no |
| ivacaftor | -4.54 | -5.01 | -6.80 | -2.26 | 91/134 | no | no |

## NEGATIVE controls — known/empirical ABCG2 inhibitors & substrates (must NOT rank as chaperone)

| molecule | fold@Q141K | transport | margin | fold-rank | chaperone tier | ChEMBL ABCG2 | wetlab candidate |
|---|---|---|---|---|---|---|---|
| novobiocin | -6.36 | -6.61 | -0.25 | 7/134 | no | yes | no |
| elacridar | -6.30 | -8.23 | -1.94 | 8/134 | no | yes | no |
| tariquidar | -6.16 | -7.75 | -1.59 | 11/134 | no | curated | no |
| itraconazole | -5.89 | -7.61 | -1.71 | 17/134 | no | curated | no |
| sulfasalazine | -5.78 | -7.34 | -1.56 | 19/134 | no | curated | no |
| ketoconazole | -5.56 | -7.15 | -1.58 | 23/134 | no | curated | no |
| methotrexate | -5.54 | -7.35 | -1.81 | 24/134 | no | curated | no |
| fumitremorgin_c | -5.06 | -6.74 | -1.68 | 56/134 | no | curated | no |
| ko143 | -4.75 | -6.26 | -1.52 | 75/134 | no | curated | no |
| topotecan | -4.74 | -6.90 | -2.16 | 76/134 | no | curated | no |
| etoposide | -4.55 | -6.64 | -2.09 | 90/134 | no | curated | no |
| mitoxantrone | -4.29 | -6.20 | -1.91 | 99/134 | no | curated | no |
| cyclosporine_a | n/a | n/a | n/a | ?/134 | error | curated | no |

## Validity read-out

- Known ABCG2 inhibitors/substrates ranked as chaperone candidates: **0** (none). PASS — screen correctly rejects inhibitors.
- CFTR correctors that EARNED a candidate tier from docking: **0** (none).
