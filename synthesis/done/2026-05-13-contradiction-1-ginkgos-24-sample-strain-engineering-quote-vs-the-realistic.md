---
type: contradiction
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 1
global_index: 5
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# Ginkgo’s $24/sample strain-engineering quote vs. the realistic cost of fungal fermentation.

1. **Ginkgo’s $24/sample strain-engineering quote vs. the realistic cost of fungal fermentation.** `wiki/ginkgo-cloud-lab-evaluation.md` reports a sales bot’s quote of ≈$2,340 for 96 *S. cerevisiae* constructs (≈$24.38/sample). The page itself flags this as “almost certainly a lead-magnet teaser” and notes that historic Ginkgo campaigns at this scope have priced mid-five to six figures. Meanwhile, `wiki/ward-1995-lab-access.md` and `wiki/team.md` frame the community-college / academic-collaborator path as the realistic route for fungal strain engineering, with costs in the $3,000–5,000 range for a single dual-cassette experiment. The tension: **the cloud-lab marketing suggests strain engineering is productized and cheap; the platform’s actual experience and the Ginkgo page’s own analysis suggest it is not.** This is not a contradiction between wiki pages — it’s a contradiction between a vendor’s lead-generation pricing and the project’s grounded cost model. The wiki correctly flags the discrepancy, but the existence of the $24/sample number in the corpus could mislead a future reader who skims the evaluation without reading the deep-dive analysis. *Locations:* `wiki/ginkgo-cloud-lab-evaluation.md` §“Pricing analysis” vs. `wiki/ward-1995-lab-access.md` and `wiki/validation-experiments.md` §1.9 cost estimates. *Analysis:* The risk is low because the Ginkgo page explicitly debunks its own quote, but the number is memorable. Consider adding a one-line cost-reality anchor in the evaluation’s TL;DR: “Do not budget against the $24/sample number; real strain-engineering campaigns at this scope cost $3,000–$50,000+.”

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` The cost-tension claim is already well grounded in `ginkgo-cloud-lab-evaluation.md`: its TL;DR reports the ≈$2,340 / ≈$24.38-per-sample quote, calls it "almost certainly a lead-magnet teaser," and says not to budget against it until a formal quote lands. The realistic-cost anchor is also supported by `validation-experiments.md` §1.9's $3,000–5,000 Ward 1995 gate and the lab-access page's academic-collaboration cost framing; the only addition would be a sharper TL;DR sentence, not a new contradiction.

---

## ✓ Actioned 2026-05-15

Bigger scope than the original Pass 2 / Pass 3 proposal. The walkthrough surfaced that the page's $39 cell-free *recommendation* (TL;DR + Suggested first run + Recommended next move) was outdated — a prior conversation (2026-05-13, transcript `80545de4...` line 11:29:29Z) had reached the decision to skip the $39 path for now, but that decision had never landed in the canonical wiki page. The wiki was still recommending an action that had already been deferred.

**Files shipped:**

- **`wiki/ginkgo-cloud-lab-evaluation.md` TL;DR** — replaced "the $39 cell-free offer is real and worth using as a sequence-validation pre-gate" with an explicit "Decision (2026-05-13): skip the $39 cell-free for now" bullet. Rationale: the cell-free test was scoped as a pre-gate for fungal wet-lab work, that work isn't currently load-bearing, and the existing computational corpus (comp-019 / comp-022 / comp-023 / ViennaRNA + ESM2 proxies) already answers the questions the test would surface to high confidence.
- **TL;DR $24/sample anchor** — sharpened the existing "don't budget against the $24/sample number" framing with explicit $3,000–$50,000+ band cross-linked to `ward-1995-lab-access.md` and `validation-experiments.md` §1.9. Addresses the original Pass 2 / Pass 3 ask.
- **"Suggested first run" section** — converted from active recommendation ("run one $39 cell-free on the lead uricase variant") to deferred-future-option ("held as a future option, not a current action").
- **"Recommended next move" section** — rewritten to lead with "No action" + the priority-stack rationale. Preserved the original rationale for reference, framed as "the rationale stands; the *timing* is what changed."
- **Construct-fit analysis preserved.** The per-construct technical analysis (uricase fits E. coli-lysate well, DAF doesn't, digestive enzymes mixed) is unchanged — the skip-for-now decision is about timing and incremental value, not technical fit.

The wiki is now the canonical record of the skip-for-now decision. If/when wet-lab work becomes load-bearing, the page's existing per-construct analysis is ready to anchor the revisit.
