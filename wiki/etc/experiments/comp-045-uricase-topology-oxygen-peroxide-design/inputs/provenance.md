# Input provenance — comp-045

## Direct human small-bowel-fluid prior

Miyazaki et al. 2025 (PMID 40033341; PMCID PMC11877951) sampled terminal-ileal fluid from 34 patients undergoing balloon-assisted enteroscopy. The reported median urate concentration was 99.5 pg/µL. Using urate molecular weight 168.11 g/mol:

- 99.5 pg/µL = 99.5 µg/L = 0.591874 µmol/L;
- the reported IQR converts to 0.060080–1.154006 µmol/L.

The design rounds the median to 0.59 µM. This is a **direct human terminal-ileum measurement in the sampled clinical cohort**, not a jejunal measurement, healthy-population baseline, or UOX activity result. No cited UOX configuration was tested at 0.59 µM.

## Exact PULSE configuration precedents

Gao et al. 2025 (PMID 41038159; PMCID PMC12629798) constructed three HucR/YgfU-regulated EcN UOX topologies:

- intracellular smUOX;
- LamB-smUOX;
- InaK-N-smUOX.

Each baseline topology was assayed at 250 µM urate. The authors then added one joint `VHb-KatG` vector to each topology and compared each baseline with its joint-module counterpart under the paper's low-oxygen method. The method used filled, sealed tubes but did not report a dissolved-oxygen target. These are direct whole-configuration precedents. They are not KatG-only or VHb-only comparisons.

The source reports LamB-supernatant-associated UOX activity and InaK-N fusion/whole-cell activity. It does not provide a dedicated surface-accessibility assay that independently establishes the claimed InaK-N outer-surface localization.

The paper used different 1:1:1 mixtures in different animal experiments: a non-KV topology mixture in acute mice and the 30-day rat study, and the three `-KV` topologies in a short eight-hour diet-induced rat comparison. It did not establish a three-topology mixture as an in-vitro positive control across 0.59/50/250 µM. COMP-045 therefore treats the KV mixture only as a proposed cross-plate anchor.

## Related intracellular precedents

Zhao et al. 2022 (PMID 35491895; PMCID PMC9067508) compared an intracellular EcN `PucL^M/PucM-vhb-ygfU-katG` configuration with the related construct lacking both VHb and KatG. The complete joint-module construct lowered measured ROS and improved restricted-DO urate degradation in the reported comparison. Zhao did not test KatG-only or VHb-only arms.

Li et al. 2023 (PMCID PMC10242094) supports a related intracellular PucLM+YgfU EcN configuration at 250 µM in defined medium and FaSSIF-V2. It supplies no KatG or VHb evidence.

The C6 periplasmic EcN UOX architecture (PMCID PMC10013758) is a separate localization precedent. It is outside the four-topology design and supports no current row.

## Proposed configurations and evidence vocabulary

No cited primary source establishes secreted active UOX in *A. oryzae*. The two koji rows are proposed configurations. Native intracellular catalase is background context, not a second physical arm and not evidence of peroxide closure at a secreted UOX reaction site.

The evidence model separates:

- `direct_exact_configuration_precedent`;
- `proposed_configuration_from_published_topology`;
- `no_direct_uox_precedent`;
- `proposed_isolation_test_from_joint_module_precedent`;
- `direct_joint_module_effect_component_attribution_unresolved`;
- `proposed_novel_module_configuration`;
- reaction-site peroxide status;
- oxygen status.

“Direct” applies only to the whole published configuration and source scope. Isolated KatG and VHb effects remain unresolved in every topology. PULSE supplies direct joint KatG+VHb construct precedents for all three EcN topologies, but the secreted/displayed configurations do not establish extracellular reaction-site peroxide closure.

The 250 µM arm is the lowest PULSE topology-assay concentration. The 0.59 µM arm is the terminal-ileal human-fluid prior described above. The 50 µM arm is a sensitivity scenario only. No numerical efficacy score or topology ranking is assigned.
