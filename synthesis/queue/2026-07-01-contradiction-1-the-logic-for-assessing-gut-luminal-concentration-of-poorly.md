---
type: contradiction
sweep_date: 2026-07-01
sweep_sha: 18d3696
section_index: 1
global_index: 4
pass3_verdict: Confirmed
overlap_tag: NOVEL
---

# The logic for assessing gut-luminal concentration of poorly-absorbed supplements is inconsistent across the wiki.

1. **The logic for assessing gut-luminal concentration of poorly-absorbed supplements is inconsistent across the wiki.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `cannabinoids-terpenes.md`, `abcg2-modulators.md`, `supplements-stack.md`
   - *Locations & Analysis:* `cannabinoids-terpenes.md` §"CBD ... GI pharmacokinetics" states: "The low systemic bioavailability does NOT automatically mean high luminal concentration. The majority of unabsorbed CBD is likely degraded in the colon... The 'poor bioavailability = gut-lumen concentration' hypothesis is not supported". In contrast, `abcg2-modulators.md` §"The supplements-stack contradiction" and `supplements-stack.md` build their entire warning about Quercetin, Curcumin, and EGCG inhibiting ABCG2 on the premise that low oral bioavailability *does* lead to high, functionally relevant gut-lumen concentrations.
   - *Resolution:* The two positions are not mutually exclusive but reflect an unstated variable: gut-luminal metabolic stability. A compound can have low absorption but also be rapidly degraded by gut microbiota, leading to low luminal concentration (the CBD case). Another can have low absorption but be relatively stable, leading to high luminal concentration (the quercetin/curcumin case). The wiki applies one logic to cannabinoids and the opposite to flavonoids without explicitly stating that metabolic stability is the discriminating factor.
   - *Suggested Action:* Update both `cannabinoids-terpenes.md` and `abcg2-modulators.md` to include a paragraph on gut-luminal metabolic stability as the key variable that determines whether low bioavailability translates to high luminal concentration. Propose a literature scan on the comparative gut microbial degradation kinetics of CBD vs. quercetin to provide evidence for the differing assumptions.

> **Pass 3 review — Confirmed.** `[OVERLAP: NOVEL]` The contradiction is real and the diagnosis is precise. `cannabinoids-terpenes.md` §"CBD … GI pharmacokinetics" explicitly states: "The low systemic bioavailability does NOT automatically mean high luminal concentration… The 'poor bioavailability = gut-lumen concentration' hypothesis is not supported." Meanwhile `abcg2-modulators.md` §"The supplements-stack contradiction" builds its entire warning about Quercetin, Curcumin, and EGCG inhibiting ABCG2 on the premise that low oral bioavailability *does* produce high, functionally relevant gut-lumen concentrations. Both positions are textually verifiable in the inlined evidence. The synthesizer's resolution — gut-luminal metabolic stability is the unstated discriminating variable — is chemically sound (CBD is microbially degraded; quercetin/curcumin glycosides are relatively stable and reach the colon intact). The action to update both pages with an explicit metabolic-stability paragraph is warranted. One additional location to flag: `supplements-stack.md` also inherits the flavonoid gut-lumen-concentration assumption and should be included in the reconciliation.
