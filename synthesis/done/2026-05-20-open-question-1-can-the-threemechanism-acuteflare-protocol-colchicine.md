---
type: open-question
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 1
global_index: 10
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Can the three‑mechanism acute‑flare protocol (colchicine + topical CBD:THC + DHA‑emphasis omega‑3) be tested as a named n = 1 protocol under the existing self‑experiment framework?

1. **Can the three‑mechanism acute‑flare protocol (colchicine + topical CBD:THC + DHA‑emphasis omega‑3) be tested as a named n = 1 protocol under the existing self‑experiment framework?** The colchicine arm is Clinical Trial‑grade; the CBD:THC arm is In Vitro/Animal Model with an n = 1 anchor; the DHA/SPM arm is Animal Model with a falsifiable C5a‑decline prediction. The combination is Speculative but compositionally coherent.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` Testing the colchicine + topical CBD:THC + DHA-resolution composition under the existing self-experiment framework is appropriate, provided the protocol stays prospective and tags the combination as Speculative. `self-experiment-protocol.md` already supports flare biomarker tracking, `gout-action-guide.md` contains the acute-route protocols, and `spm-resolution-pathway.md` supplies the CP5b resolution readout logic. The experiment should separate timing and endpoints by mechanism rather than treating “flare better” as one undifferentiated outcome.

---

## ✓ Actioned 2026-05-21

[`self-experiment-protocol.md` §13](../../wiki/self-experiment-protocol.md) added: **"Acute-flare stack sub-experiment — Protocol C, prospective n=1."** Pass 3's mechanism-separation discipline is the central design: per-arm endpoints with different time windows so the three arms can be evaluated independently rather than collapsed into one "flare better" composite.

Mechanism-separated endpoints landed:
- Colchicine arm (suppression, systemic): joint pain VAS, joint circumference, global flare severity at 6h / 24h / 48h / 72h
- Topical CBD:THC arm (suppression, local): local pain VAS at 30min / 1h / 2h / 4h — separate rapid-onset window before systemic colchicine kinetics would predict
- DHA SPM arm (resolution-class, systemic): serum C5a decline slope days 3-7 (resolution-phase per [`spm-resolution-pathway.md` §7.3](../../wiki/spm-resolution-pathway.md)) + onset C5a anchor; serum 17-HDHA / 14-HDHA if LC-MS/MS lipidomic panel accessible
- Composite resolution: flare duration to < 2/10 pain (days)

Within-subject control framework: requires several flares to compare across omega-3-index states (≥ 8% vs. < 4%) at flare onset; logging discipline (§5 symptom diary) is the load-bearing variable. n=1 caveats explicit (suggestive only, cannot generalize, cannot substitute for a formal RCT).

Cross-references: [`gout-action-guide.md` §"Combined-route flare protocols" Protocol C](../../wiki/gout-action-guide.md), [`spm-resolution-pathway.md` §7.3](../../wiki/spm-resolution-pathway.md), [`colchicine.md` §3.3.1](../../wiki/colchicine.md), [`cannabinoids-terpenes.md` §4a](../../wiki/cannabinoids-terpenes.md), [`complement-c5a-gout.md` §3.1](../../wiki/complement-c5a-gout.md).

Pairs with [the Item 3 closure](./2026-05-20-connection-3-the-multimodal-acuteflare-protocol-combining-colchicine-cp3.md) — protocol composition canonical surface at `gout-action-guide.md`.
