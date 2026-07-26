# comp-047 — Control and exclusion read-out

Frozen docking run date: 2026-07-14. N=134 molecules with valid docking.

Affinities are Vina scores in kcal/mol (more negative = stronger). Margin = transport − fold@Q141K (>0 favors the modeled fold-site box). These are method diagnostics, not binding or rescue measurements.

## Cross-protein chaperone mechanism comparators

CFTR correctors are not validated ABCG2 fold-site binders. Their failure to earn rank shows that this setup did not recover these cross-protein chaperone comparators; it is not proof that ABCG2 lacks a rescuable site.

| molecule | fold@Q141K | fold@WT | Walker A | margin | base-run fold rank | docking tier | executable row |
|---|---|---|---|---|---|---|---|
| lumacaftor | -7.35 | -7.03 | -8.77 | -1.42 | 2/134 | no | no |
| tezacaftor | -5.91 | -5.61 | -7.35 | -1.44 | 16/134 | no | no |
| elexacaftor | -5.80 | -6.21 | -7.75 | -1.95 | 18/134 | no | no |
| ivacaftor | -4.54 | -5.01 | -6.80 | -2.26 | 91/134 | no | no |

## Curated ABCG2 negative controls

| molecule | fold@Q141K | Walker A | margin | base-run fold rank | ChEMBL activity | DrugBank relationship | executable row |
|---|---|---|---|---|---|---|---|
| novobiocin | -6.36 | -6.61 | -0.25 | 7/134 | yes | yes | no |
| elacridar | -6.30 | -8.23 | -1.94 | 8/134 | yes | yes | no |
| tariquidar | -6.16 | -7.75 | -1.59 | 11/134 | unqueried | no | no |
| itraconazole | -5.89 | -7.61 | -1.71 | 17/134 | unqueried | yes | no |
| sulfasalazine | -5.78 | -7.34 | -1.56 | 19/134 | unqueried | yes | no |
| ketoconazole | -5.56 | -7.15 | -1.58 | 23/134 | unqueried | no | no |
| methotrexate | -5.54 | -7.35 | -1.81 | 24/134 | unqueried | yes | no |
| fumitremorgin_c | -5.06 | -6.74 | -1.68 | 56/134 | unqueried | no | no |
| ko143 | -4.75 | -6.26 | -1.52 | 75/134 | unqueried | no | no |
| topotecan | -4.74 | -6.90 | -2.16 | 76/134 | unqueried | yes | no |
| etoposide | -4.55 | -6.64 | -2.09 | 90/134 | unqueried | yes | no |
| mitoxantrone | -4.29 | -6.20 | -1.91 | 99/134 | unqueried | yes | no |
| cyclosporine_a | n/a | n/a | n/a | ?/134 | unqueried | no | no |

## Axis-2 impact on docking-tier survivors

| molecule | docking tier | ChEMBL activity | substrate exclusion | DrugBank relationship | final executable row |
|---|---|---|---|---|---|
| rosuvastatin | uncertain | no | yes | yes | no |
| vorinostat | uncertain | no | no | no | uncertain |

## Diagnostic interpretation

- Cross-protein chaperone comparators reaching an executable tier: **0** (none).
- Curated ABCG2 negative controls left as executable rows after Axis 2: **0** (none).
- The first result does not validate sensitivity, because the comparator molecules are established for CFTR rather than ABCG2. The second shows that the exclusion layer works for the declared controls; it does not validate the fold-site ranking.
