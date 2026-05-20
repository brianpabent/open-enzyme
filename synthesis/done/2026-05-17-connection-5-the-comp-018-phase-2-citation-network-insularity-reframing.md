---
type: connection
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 5
global_index: 5
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The comp-018 Phase 2 "citation-network insularity" reframing — where "language barrier" was rediagnosed as traditional-name vs. mechanism-name query framing — generalizes into a discovery methodology applicable to every non-Western-medicine compound class in the OE corpus.

5. **The comp-018 Phase 2 "citation-network insularity" reframing — where "language barrier" was rediagnosed as traditional-name vs. mechanism-name query framing — generalizes into a discovery methodology applicable to every non-Western-medicine compound class in the OE corpus.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `upstream-complement-modulator-sweep-computational.md` (Phase 2), `tcm-modern-rigor-intersection.md`, `medicinal-mushroom-compound-mapping-computational.md`, `CLAUDE.md`
   - *Page-pair linkage:* The comp-018 Phase 2 reframing is documented in upstream-complement-modulator-sweep-computational.md but hasn't been propagated as a general methodology principle to tcm-modern-rigor-intersection.md or the CLAUDE.md global-multilingual rule. The operational insight — "query by traditional-formula-name + species-name + traditional-pathology-framing IN ADDITION TO mechanism-name" — is currently scoped to the upstream-complement subfield but generalizes.
   - *Why It Matters:* comp-018 Phase 2 explicitly reframed the "language barrier" diagnosis: Chen Daofeng / Yamada-Kiyohara groups publish 80–95% in English-language journals; the actual barriers are citation-network insularity, traditional-formula-name vs. Western-mechanism-name query framing, and source-journal impact-factor underweighting. The operational discipline that surfaced Houttuynia — "a 'C3 convertase inhibitor' query misses Houttuynia; a 'Houttuynia cordata anti-complementary' query catches it" — is a general discovery principle. Applied to TCM gout compounds: "xanthine oxidase inhibitor" misses Smilax glabra formulations; "Tu Fu Ling 土茯苓 hyperuricemia" catches them. Applied to medicinal mushrooms: "NLRP3 inhibitor" misses *G. lucidum* spore powder; "lingzhi 灵芝 anti-inflammatory mechanism" catches it. The CLAUDE.md global-multilingual rule (§"Global-multilingual research by default") should encode this as an explicit operational sub-discipline rather than leaving it buried in a specific comp-NNN Phase 2 finding.
   - *Suggested Action:* Add a short "Query-framing discipline" subsection to CLAUDE.md under the global-multilingual rule: "For non-Western-medicine compound discovery, query by traditional-formula-name + species-name + traditional-pathology-framing IN ADDITION TO mechanism-name. Mechanism-name is the wrong starting point for non-Western literature. Example: 'C3 convertase inhibitor' misses Houttuynia; 'Houttuynia cordata anti-complementary' catches it." Cross-reference the comp-018 Phase 2 finding as the canonical worked example. Propagate to tcm-modern-rigor-intersection.md as an explicit sub-rule.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` comp-018 Phase 2 states the methodological lesson verbatim: the “language barrier” diagnosis was wrong; the real barriers were citation-network insularity and traditional-name / species-name / pathology-framing query mismatch, and “C3 convertase inhibitor” misses Houttuynia while “Houttuynia cordata anti-complementary” catches it. The TCM methodology page already has global-multilingual rigor, but this specific query-framing discipline is not present as a first-class rule there or in the grep-checked `CLAUDE.md`. Propagating it is an actionable process improvement, not just a content addition.

---

**WALKED 2026-05-19 — Closed (query-framing discipline promoted to project-wide rule in CLAUDE.md + tcm-modern-rigor-intersection.md with cross-mechanism illustrative cases).**

Actioned:
- ✓ Added "Query-framing discipline" bullet to `CLAUDE.md` §"Global-multilingual research by default" Operational rules. Documents the rule (traditional-formula-name + species-name + traditional-pathology-framing IN ADDITION TO mechanism-name), the canonical Houttuynia worked example, and the three-failure-mode rediagnosis (citation-network insularity + traditional-name-vs-mechanism-name query mismatch + source-journal impact-factor underweighting, NOT "language barrier"). Plus illustrative cases per Brian's call (Cluster M walkthrough):
  - URAT1: "Si Miao San 四妙散 hyperuricemia" catches Smilax glabra formulations that "URAT1 inhibitor natural product" misses
  - XO: "Jiang Huang 姜黄 xanthine oxidase" catches turmeric curcuminoids
  - NLRP3: "Lingzhi 灵芝 anti-inflammatory mechanism" catches *G. lucidum* spore-powder evidence
  - Complement modulators: the canonical Houttuynia case
- ✓ Added §7 "Query-framing discipline — traditional-name FIRST, mechanism-name SECOND" to `wiki/tcm-modern-rigor-intersection.md` after §6 (Falsification card per major claim). Explains why this is its own discipline rather than a sub-point of §2 (ChEMBL cross-check): ChEMBL undercoverage reflects what's been curated; traditional-name-anchored papers that never made it into ChEMBL are invisible to mechanism-name search regardless of language. Same cross-mechanism examples + cross-reference to CLAUDE.md rule.

**Brian's flagged follow-up:** "I have a question about previous lit scans and what we may have missed!" — this is a sharp retrospective question worth engaging at end-of-walk. Most of this session's lit scans (A2 multilingual gout cohort, J2 food-grade Penicillium, J3.2 substrate engineering, H2 cortisol-glucocorticoid, Houttuynia CP1) were already framed with species-name + multilingual scope per the existing global-multilingual rule, so this session's findings are likely OK. But pre-2026-05-19 lit scans + earlier sweep cycles may have used mechanism-name-only framing and systematically under-found traditional-name-anchored evidence. Queueing a retrospective audit as end-of-walk follow-up.

Also closes:
- 2026-05-17 open-question-2 (does this apply beyond CP0? — Pass 3 confirmed yes; the illustrative cases in the propagated rule make this explicit)
- 2026-05-17 priority-action-2 (propagate to CLAUDE.md — Pass 3 confirmed; done as part of canonical closure)
