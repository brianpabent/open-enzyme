---
type: connection
sweep_date: 2026-05-15
sweep_sha: ebbce26
section_index: 3
global_index: 3
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The inhaled mRNA-IL-1RA pulse bridges the chronic oral platform with acute flare termination, closing the speed-of-onset gap.

3. **The inhaled mRNA-IL-1RA pulse bridges the chronic oral platform with acute flare termination, closing the speed-of-onset gap.** *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `delivery-route-matrix.md`, `chassis-pending-interventions.md`, `modality-chokepoint-matrix.md`, `open-enzyme-vision.md`
   - *Page-pair linkage:* The new delivery-route-matrix and chassis-pending inventory both flag inhaled mRNA-IL-1RA as a future acute-flare intervention, but they frame it as a standalone concept. The broader platform currently has no fast-acting tool — the koji uricase and NLRP3 supplement stacks are chronic-prevention modalities. The addition of a transiently-expressed IL-1 receptor antagonist delivered by pulmonary inhaler provides a **temporal complement**: chronic koji for baseline urate disposal and inflammasome dampening; inhaled mRNA pulse for aborting flares at onset.
   - *Why It Matters:* This trims the most significant functional blind spot: the inability to act quickly when a flare starts. The combination is mechanistically clean — short-lived lung expression of IL-1RA does not interfere with gut-lumen sink or chronic NLRP3 modulation. It also leverages mRNA-LNP manufacturing economics against the $300K/yr canakinumab benchmark. The temporal separation (chronic vs. pulsatile) means minimal drug-drug interaction risk.
   - *Suggested Action:* Scope a comp-NNN to estimate mRNA-IL-1RA dose requirements and LNP pulmonary delivery feasibility using published inhaled mRNA programs (CF, RSV) as prior art. Include a PK/PD model comparing inhaled mRNA area-under-curve to subcutaneous anakinra, with cost-per-flare comparison.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The temporal-complement framing is correct: `chassis-pending-interventions.md` §4 names inhaled mRNA-IL-1RA as a CP5a acute-flare intervention with synthetic mRNA + LNP + inhaler as the candidate chassis, while `delivery-route-matrix.md` and `gout-kill-chain-delivery-routes.md` surface pulmonary / mRNA IL-1RA pulse concepts as open delivery cells. Pass 2 adds the useful platform-level composition: chronic oral/koji prevention leaves a speed-of-onset gap, and a short-lived IL-1RA expression pulse is a mechanistically clean acute-flare complement rather than a competing chassis. Route to chassis-pending / mRNA-LNP feasibility, not away from the platform.

---

## ✓ Actioned 2026-05-16

Named the temporal-complement framing as a platform-positioning statement across three canonical surfaces. The intervention itself (chassis-pending §4) was already documented; what was new and worth naming was the **chronic-prevention + pulsatile-flare-abort = temporal stack** insight and the **OE-as-discovery-engine-output vs pharma-as-manufacturer** role boundary.

- [`wiki/open-enzyme-vision.md`](../../wiki/open-enzyme-vision.md) — added "### Chronic prevention + pulsatile flare-abort — the temporal stack" subsection inside §10 "Multi-Attack Strategy." Names the gap (chronic stack doesn't act in the flare-window timescale), the candidate solution (inhaled mRNA-IL-1RA pulse with vibrating-mesh nebulizer POC and DPI eventual product), and — explicitly — OE's bounded role (target validation + construct-design priors + economic argument + partner identification, NOT manufacturing). Tiered cost split documented: $0–50 OE subagent analysis → $50K–200K animal POC (partner) → $100M+ clinical (pharma partner) → ~$25–200/yr/patient COGS at scale vs canakinumab benchmark $300K/yr. Generalizes the temporal-stack framing beyond mRNA-IL-1RA to any 12–72h-expression-window acute-flare-abort candidate.
- [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) — added comp-033 to Planned Analyses table promoting the chassis-pending §4 placeholder to a concrete brief: target validation + dose modeling against anakinra AUC anchor + construct-design priors (Karikó/Weissman pseudouridine chemistry, UTR choice for transient expression) + economic comparison + partner-identification scan across CF / RSV inhaled-mRNA programs and CDMOs. Multilingual default applied (J-STAGE / CNKI for Japanese / Chinese inhaled-biologics literature).
- [`wiki/nlrp3-inflammasome.md`](../../wiki/nlrp3-inflammasome.md) — added "Inhaled mRNA-IL-1RA pulse (chassis-pending, pulmonary delivery)" bullet under §"Chokepoint 5" (CP5a) Exploits, alongside the existing anakinra entry. Frames as complementary to chronic urate-lowering rather than competitive; cross-links chassis-pending §4 + comp-033 + open-enzyme-vision §10 temporal-stack section.

No new wiki page. No additional Phase 2 follow-ups beyond comp-033. The framing generalization (temporal stack applies to any 12–72h-window candidate, not just inhaled mRNA-IL-1RA) is now publicly stated in the platform vision page, so future intra-articular uricase / hepatic-mRNA / etc. acute-flare candidates inherit the framing automatically.

**Walkthrough side-note:** Brian asked good cost / device / supply-chain feasibility questions before approving; answers were summarized in conversation and the headline tiered-cost split + OE-role-boundary made it into the wiki page directly so future readers see the same framing without needing the live Q&A.
