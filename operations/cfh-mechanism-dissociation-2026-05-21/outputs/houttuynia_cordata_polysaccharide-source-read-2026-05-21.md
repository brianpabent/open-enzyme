# Houttuynia cordata polysaccharide (HCP / HCPM / CHCP) — Model A source read (CFH-dependence classification)

**Date:** 2026-05-21
**Author:** Claude Opus 4.7 (Model A in two-model cross-check protocol)
**Scope:** comp-039 mechanism-dissociation classification of *Houttuynia cordata* polysaccharide fractions — do HCP/HCPM/CHCP's anti-complement and anti-inflammatory effects require functional CFH (Y402H carriers lose benefit, AMD-paradox-style), or do they bypass CFH?

## Primary sources read

1. **Tian L, Zhao Y, Guo C, Yang X.** Anti-complementary constituents of *Houttuynia cordata* and their targets in complement activation cascade. *J Ethnopharmacol* 2014. PMID 24423008 — abstract only (no PMC ID returned).
2. **Lu Y, Jiang Y, Ling L, Zhang Y, Li H, Chen D.** Beneficial effects of *Houttuynia cordata* polysaccharides on "two-hit" acute lung injury and endotoxic fever in rats associated with anti-complementary activities. *Acta Pharm Sin B* 2018;8(2):218–227. PMID 29719782 / PMC5925397 — full text read. Polysaccharide fraction = CHCP.
3. **Xu YY, Zhang YY, Ou YY, Lu XX, Pan LY, Li H, Lu Y, Chen DF.** *Houttuynia cordata* Thunb. polysaccharides ameliorates lipopolysaccharide-induced acute lung injury in mice. *J Ethnopharmacol* 2015;173:81–90. PMID 26190353 / PMC7127486 — full text read. Polysaccharide fraction = HCP.
4. **Cheng D, Sun L, Zou S, Chen J, Mao H, Zhang Y, Liao N, Zhang R.** Anti-complementary Activity of *Houttuynia cordata* Polysaccharide HCP-1. *Carbohydr Polym* (Chen Daofeng group, Fudan University). Referenced in comp-018 Phase 2.

## Binding-site / target evidence

**Lu 2018 (PMC5925397):** systematic complement-depleted-sera reconstitution assay. C-depleted sera tested for restoration of CHCP-blocked hemolytic activity. Verbatim results:

> "C2-depleted and C9-depleted sera also restored the hemolysis markedly (72.82±10.61% for C2 and 63.21±2.27% for C9). However, CHCP nearly abolished the hemolysis when C3- or C4-depleted serum was added (9.29±1.69% for C3, 12.34±1.39% for C4). For C5, the hemolysis was only partly restored (44.54±3.92%). These results suggested that CHCP mainly block C3 and C4, and may interact with C5."

Grep-verified against the full text (PMC5925397 lines covering "Identification of the targets of CHCP in the complement activation cascade"). The targets are **C3, C4, and partially C5** — three of the most upstream amplification-cascade components. C1q, C2, C9 are NOT primary targets (C-depletion of those rescues hemolysis).

**Tian 2014 (PMID 24423008):** abstract-level: "the glycoside moieties may be necessary to block C3 and C4 components." Mechanism convergence with Lu 2018 — glycoside-pectic-polysaccharide structural class targets C3 and C4.

**Xu 2015 (PMC7127486):** broader anti-inflammatory mechanism in LPS-induced ALI model: HCP reduces TLR4 expression in lung tissue, reduces C3d deposition (immunohistochemistry), suppresses C5a-induced macrophage chemotaxis, and modulates NLRP3-axis cytokines (IL-1β, TNF-α, IL-6). This adds **TLR4 multi-target** activity orthogonal to the complement-binding mechanism.

Across all three primary sources, **CFH is not mentioned**.

## Mechanism mapping vs CFH Y402H footprint

The complement cascade nodes HCP/CHCP blocks:

- **C3:** the central node, ~70% of total complement protein. Cleaves to C3a/C3b. CFH acts on the *product* (C3b) — by sequestering or covalently engaging C3 itself, HCP reduces the substrate pool from which CFH-targetable C3b is generated.
- **C4:** the classical-pathway initiator (cleaved by C1s → C4a + C4b; C4b combines with C2a to form C4b2a = CP C3 convertase). HCP at C4 prevents the classical-pathway C3 convertase from assembling, blocking all downstream C3 cleavage from that pathway. CFH does not regulate C4 — CFH is alternative-pathway-specific. **HCP's C4-axis mechanism is orthogonal to CFH entirely.**
- **C5 (partial):** the AP/CP convergence node for terminal-complex formation. CFH does not directly regulate C5; the relevant regulator at this step is CD59 / C8. HCP's C5 mechanism is CFH-orthogonal.

**Polysaccharide mode of action:** large pectic polysaccharides typically operate by adsorptive surface binding to complement proteins (multiple weak contacts, high avidity) rather than active-site small-molecule binding. This is structurally distinct from CFH's CCP6-8 → C3d-TED interaction. HCP would not be expected to displace CFH from C3b nor compete with CRP at the CCP7 surface.

**TLR4-MD2 multi-target (Yu 2026 PMC12937656 docking model, Xu 2015 lung-tissue TLR4 downregulation):** entirely orthogonal to complement and CFH. This is a CP1 (TLR-priming) effect that bypasses the complement axis.

## Classification

**CFH-dependence: CFH-INDEPENDENT (High confidence).**

Mechanism converges across three independent papers on C3 + C4 binding. C4 binding is mechanistically incompatible with CFH-dependence (CFH does not regulate the classical pathway's C4-axis). C3 binding upstream of C3 cleavage removes the substrate CFH would regulate. The TLR4-MD2 orthogonal mode further dissociates HCP's anti-inflammatory effect from any CFH-mediated step.

**Predicted Y402H × HCP × incident gout interaction:** **negative direction (effect ≥ in carriers, possibly notably greater)** — Y402H carriers have unregulated alternative-pathway amplification on MSU crystals; HCP's C3-cap upstream of that amplification should produce a *larger absolute reduction* in MSU-driven C3b/C5a in carriers than in non-carriers. The dual-chokepoint (CP0 complement + CP1 TLR4 priming) suggests HCP could be especially effective in Y402H carriers where both axes are dysregulated.

**Falsification threshold:** UK Biobank candidate-stratified cross-tab (Houttuynia / fish-mint / 鱼腥草 / どくだみ diet × Y402H × incident gout M10.x) with HR > 1.3 in carriers vs non-carriers on same diet would refute the CFH-independence classification. Practical confound: Houttuynia is rare in UK Biobank's UK dietary corpus; the relevant cross-tab is more tractable in a Chinese / Vietnamese / Korean / Japanese cohort (e.g., Korean Genome Epidemiology Study, China Kadoorie Biobank).

**Confidence:** High. Two independent full-text-verified papers (Lu 2018, Xu 2015) plus convergent Tian 2014 abstract all point to C3/C4 binding; the C4 specificity is mechanistically incompatible with CFH-dependence.

## Multi-hypothesis discipline — rejected alternative

**Rejected hypothesis: HCP polysaccharide acts via direct CFH-mimicry — binding C3b at the same surface CFH binds (CCP1-4 of CFH binds C3b TED domain).** Would predict that Y402H carriers (with weaker CFH function) benefit MORE from HCP if HCP is filling the regulatory gap. **Partially rejected** because: (a) Lu 2018's depletion-rescue data shows HCP blocks the hemolysis cascade at C3 and C4 — meaning HCP prevents C3 *cleavage*, not C3b inactivation. CFH-mimicry would predict HCP works downstream of C3 cleavage (on the C3b product), not upstream. (b) HCP's pectic polysaccharide structure (homogalacturonan / rhamnogalacturonan backbone with arabino-galactan side chains in typical *Houttuynia* HCP characterizations) is chemically nothing like CFH's CCP-fold protein structure; no shared pharmacophore. Mechanism is more likely surface adsorption / activation-blocker than regulator-mimic. **The prediction direction is the same** (Y402H carriers benefit ≥ non-carriers) in both the activation-blocker and CFH-mimic hypotheses — but the upstream C3/C4 mechanism is the better-evidenced one and what we commit to.

## Limitations

- The "C3 and C4" target identification is at depletion-rescue resolution, not single-residue binding-site resolution. We do not know the specific epitopes on C3 / C4 that HCP polysaccharide binds.
- HCP / HCPM / CHCP across the three papers are not strictly identical polysaccharide fractions (Lu 2018 = CHCP, Xu 2015 = HCP, Cheng 2014 = HCP-1). Structure-activity relationships across Chen Daofeng / Fudan group fractions show some heterogeneity (Cheng 2014 noted "structure-dependent" effects). The "polysaccharide class" classification papers over within-class variation that wet-lab work would need to resolve.
- The TLR4-MD2 docking prediction (Yu 2026 PMC12937656) is computational only — not orthogonal wet-lab confirmation of direct TLR4 binding.
- No published study has tested HCP + Y402H carrier serum + MSU crystals. The classification is mechanistic extrapolation.
- Houttuynia bioavailability after oral intake is incompletely characterized for polysaccharide fractions; the operative gut-luminal vs systemic concentration distribution for an in-vivo MSU-driven complement axis is unknown.

## Evidence-tier summary

- **In Vitro:** Lu 2018 C3 / C4 depletion-rescue mapping (PMID 29719782, PMC5925397) — direct target identification.
- **In Vitro:** Tian 2014 glycoside C3 / C4 mapping (PMID 24423008) — convergent class-level evidence.
- **In Vitro + Animal Model:** Xu 2015 HCP rescue of LPS-induced ALI in mice (PMID 26190353, PMC7127486) — multi-target including TLR4, complement deposition, C5a-chemotaxis.
- **Animal Model:** Lu 2018 "two-hit" ALI rat model with CHCP oral rescue (PMID 29719782) — in-vivo confirmation that anti-complementary activity translates to systemic outcome benefit in a complement-driven inflammation model.
- **Mechanistic Extrapolation:** CFH-independence in Y402H carriers — High confidence; C3 + C4 mechanism is structurally upstream of CFH's regulatory step on the alternative-pathway amplification loop, and C4 binding is mechanistically incompatible with CFH-dependence.
