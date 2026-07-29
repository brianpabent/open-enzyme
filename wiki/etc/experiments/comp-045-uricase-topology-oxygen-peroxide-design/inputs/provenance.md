# Input provenance — comp-045

## Primary-source verification map

The source locations below bind each load-bearing input to an inspectable
primary record. Section and figure locators refer to the public full text.

| Source | Bibliographic identity and record | Source locator | Bound input and limit |
|---|---|---|---|
| Gao et al. 2025 | *Cell Reports Medicine* 6:102379. DOI [10.1016/j.xcrm.2025.102379](https://doi.org/10.1016/j.xcrm.2025.102379); PMID 41038159; PMCID [PMC12629798](https://pmc.ncbi.nlm.nih.gov/articles/PMC12629798/). Version-of-record full text retrieved through Europe PMC on 2026-07-29. | Results, “Construction of engineered bacteria for UA degradation,” Figure 3B–I; Results, “PULSE-mediated control of UA homeostasis in hyperuricemic rats,” Figure 5C and paragraph beginning “To alleviate hypoxic conditions”; Figure S10 | Three HucR/YgfU-regulated EcN smUOX topologies were assayed at 250 µM. The low-oxygen comparison added KatG and VHb jointly and used filled, sealed tubes; it does not isolate either module or specify a dissolved-oxygen target. |
| Zhao et al. 2022 | *Gut Microbes* 14:2070391. DOI [10.1080/19490976.2022.2070391](https://doi.org/10.1080/19490976.2022.2070391); PMID 35491895; PMCID [PMC9067508](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067508/). Version-of-record full text retrieved through Europe PMC on 2026-07-29. | Results, “Engineering strain for UA degradation in either hypoxia conditions or anoxia conditions with reduced oxidative stress,” Figure 3a–d | The related intracellular PucL-mutant/PucM+YgfU configuration was compared with the joint KatG+VHb configuration. Figure 3d defines restricted dissolved oxygen as 15% of the normal-medium condition; no isolated KatG-only or VHb-only arm was reported. |
| Gencer et al. 2023 | *Frontiers in Bioengineering and Biotechnology* 11:1191162. DOI [10.3389/fbioe.2023.1191162](https://doi.org/10.3389/fbioe.2023.1191162); PMID 37288353; PMCID [PMC10242094](https://pmc.ncbi.nlm.nih.gov/articles/PMC10242094/). Version-of-record full text retrieved through Europe PMC on 2026-07-29. | Results, “Engineering *E. coli* to lower serum uric acid levels,” Figures 4–6; Methods, “Colorimetric uric acid assay” | PucLM and YgfU were combined in intracellular engineered *E. coli*, including EcN, and tested at 250 µM in M9 minimal medium and FaSSIF-V2. This is related precedent, not an exact PULSE construct, and supplies no KatG or VHb evidence. |
| Miyazaki et al. 2025 | *Journal of Translational Medicine* 23:257. DOI [10.1186/s12967-025-06145-7](https://doi.org/10.1186/s12967-025-06145-7); PMID 40033341; PMCID [PMC11877951](https://pmc.ncbi.nlm.nih.gov/articles/PMC11877951/). Version of record dated 2025-03-03; main text and [Supplementary Material 2](https://media.springernature.com/original/springer-static/esm/art%3A10.1186%2Fs12967-025-06145-7/MediaObjects/12967_2025_6145_MOESM2_ESM.docx) retrieved 2026-07-29. | Main text, paragraphs 2 and limitations; Supplementary Material 2, “Additional Methods,” “Collection of small intestinal fluid and uric acid measurement” | Baseline small-intestinal-fluid urate was 99.5 pg/µL (IQR 10.1–194.0) in 34 clinically indicated balloon-enteroscopy patients. The supplementary method states that every procedure occurred in the terminal ileum of the pelvis. This is a direct human observational compartment measurement, not a Clinical Trial or healthy-population baseline. |
| PubChem CID 1175 | Uric acid, formula C5H4N4O3, molecular weight 168.11 g/mol. [PUG REST property response](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/1175/property/MolecularFormula,MolecularWeight/JSON), retrieved 2026-07-29; CID is the record accession. | `PropertyTable.Properties[0].MolecularWeight` | Conversion denominator only. |

## Direct human small-bowel-fluid prior

Miyazaki et al. 2025 (PMID 40033341; PMCID PMC11877951) sampled terminal-ileal fluid from 34 patients undergoing balloon-assisted enteroscopy. The reported median urate concentration was 99.5 pg/µL. Using urate molecular weight 168.11 g/mol:

- 99.5 pg/µL = 99.5 µg/L = 0.591874 µmol/L;
- the reported IQR converts to 0.060080–1.154006 µmol/L.

The design rounds the median to 0.59 µM. This is a **direct human observational terminal-ileum measurement in the sampled clinical cohort**, not a Clinical Trial, jejunal measurement, healthy-population baseline, or UOX activity result. No cited UOX configuration was tested at 0.59 µM.

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

Gencer et al. 2023 (PMID 37288353; PMCID PMC10242094) supports a related intracellular PucLM+YgfU EcN configuration at 250 µM in defined medium and FaSSIF-V2. It supplies no KatG or VHb evidence.

The C6 periplasmic EcN UOX architecture (PMCID PMC10013758) is a separate localization precedent. It is outside the four-topology design and supports no current row.

## Proposed configurations and evidence vocabulary

No primary source in the bounded 2026-07-29 search described in `query-strategy.json` established secreted active UOX in *A. oryzae*. The two koji rows are candidate configuration classes. Host catalase localization and activity are unresolved for the eventual strain and culture condition and provide no evidence of peroxide closure at a secreted UOX reaction site.

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
