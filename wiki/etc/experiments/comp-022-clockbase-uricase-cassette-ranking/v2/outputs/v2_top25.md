# comp-022 v2 Top-25 cassettes (N-of-5 >= 4 concordance)

v2 run date: 2026-05-14

v2 shortlist size: **71** unique cassettes (vs v1 N-of-4 >= 3 = 501; v1 N-of-4 = 4 strict = 45).

v1-top-cluster (PamyB + amyB-SP + 5p_softened + direct + PTS1-blk + N191Q) survival in v2: **4 / 4** (100%).

ViennaRNA MFE vs v1 GC-clamp proxy: Spearman rho = **0.241** (n=52 pairs).

Five models: CAI (higher better), ViennaRNA 5'-MFE (higher = less structure = better), chaperone load (lower better), promoter x SP prior (higher better), ESM2 pseudo-pLDDT (higher better, ESMFold fallback per provenance.md).

| Rank | Promoter | SP | Codon | Scaffold | Prop | N-glyc | CAI | MFE | ChapLoad | Prior | ESM-pLDDT | N-of-5 | Composite |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PamyB | SPamyB_pro | 5p_softened | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 0.915 | -13.70 | 0.00 | 1.020 | 87.9 | 5 | 0.919 |
| 2 | PamyB | SPamyB_pro | 5p_softened | direct_natag_pts1ok | prop_native | nglyc_ablated | 0.915 | -13.70 | 0.25 | 1.020 | 89.3 | 5 | 0.916 |
| 3 | PglaA | SPamyB_pro | 5p_softened | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 0.915 | -13.70 | 0.00 | 0.867 | 87.9 | 5 | 0.873 |
| 4 | PglaA | SPamyB_pro | 5p_softened | direct_natag_pts1ok | prop_native | nglyc_ablated | 0.915 | -13.70 | 0.25 | 0.867 | 89.3 | 5 | 0.870 |
| 5 | PamyB | SPamyB_pro | cai_max | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -16.70 | 0.00 | 1.020 | 87.9 | 4 | 0.934 |
| 6 | PamyB | SPamyB_pro | high_gc | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -16.70 | 0.00 | 1.020 | 87.9 | 4 | 0.934 |
| 7 | PamyB | SPamyB_pro | cai_max | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -16.70 | 0.25 | 1.020 | 89.3 | 4 | 0.932 |
| 8 | PamyB | SPamyB_pro | high_gc | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -16.70 | 0.25 | 1.020 | 89.3 | 4 | 0.932 |
| 9 | PamyB | SPamyB | cai_max | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -17.10 | 0.00 | 1.000 | 88.7 | 4 | 0.927 |
| 10 | PamyB | SPamyB | high_gc | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -17.10 | 0.00 | 1.000 | 88.7 | 4 | 0.927 |
| 11 | PamyB | SPamyB | cai_max | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -17.10 | 0.25 | 1.000 | 90.0 | 4 | 0.924 |
| 12 | PamyB | SPamyB | high_gc | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -17.10 | 0.25 | 1.000 | 90.0 | 4 | 0.924 |
| 13 | PamyB | SPamyB | cai_max | direct_his6_pts1ok | prop_none | nglyc_ablated | 1.000 | -17.10 | 0.00 | 1.000 | 87.5 | 4 | 0.922 |
| 14 | PamyB | SPamyB | high_gc | direct_his6_pts1ok | prop_none | nglyc_ablated | 1.000 | -17.10 | 0.00 | 1.000 | 87.5 | 4 | 0.922 |
| 15 | PamyB | SPamyB_pro | 5p_softened | direct_his6_pts1ok | prop_none | nglyc_ablated | 0.915 | -13.70 | 0.00 | 1.020 | 86.4 | 4 | 0.912 |
| 16 | PamyB | SPalpA_pro | 5p_softened | direct_his6_pts1ok | prop_none | nglyc_ablated | 0.915 | -12.30 | 0.00 | 0.920 | 85.4 | 4 | 0.894 |
| 17 | PamyB | SPalpA_pro | 5p_softened | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 0.915 | -12.30 | 0.00 | 0.920 | 84.7 | 4 | 0.890 |
| 18 | PglaA | SPamyB_pro | cai_max | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -16.70 | 0.00 | 0.867 | 87.9 | 4 | 0.888 |
| 19 | PglaA | SPamyB_pro | high_gc | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -16.70 | 0.00 | 0.867 | 87.9 | 4 | 0.888 |
| 20 | PglaA | SPamyB_pro | cai_max | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -16.70 | 0.25 | 0.867 | 89.3 | 4 | 0.886 |
| 21 | PglaA | SPamyB_pro | high_gc | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -16.70 | 0.25 | 0.867 | 89.3 | 4 | 0.886 |
| 22 | PglaA | SPamyB | cai_max | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -17.10 | 0.00 | 0.850 | 88.7 | 4 | 0.882 |
| 23 | PglaA | SPamyB | high_gc | direct_3xAla_pts1blk | prop_none | nglyc_ablated | 1.000 | -17.10 | 0.00 | 0.850 | 88.7 | 4 | 0.882 |
| 24 | PamyB | SPalpA | cai_max | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -16.10 | 0.25 | 0.880 | 86.2 | 4 | 0.881 |
| 25 | PamyB | SPalpA | high_gc | direct_natag_pts1ok | prop_native | nglyc_ablated | 1.000 | -16.10 | 0.25 | 0.880 | 86.2 | 4 | 0.881 |
