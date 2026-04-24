---
title: "Self-Experiment Protocol — Brian's Personal Monitoring Plan"
date: 2026-04-24
tags: ["self-experiment", "n-of-1", "safety", "monitoring", "microbiota", "gout", "open-enzyme"]
related:
  - open-enzyme-vision.md
  - supplements-stack.md
  - engineered-koji-protocol.md
  - gout-deep-dive.md
  - cross-validation.md
  - validation-experiments.md
sources:
  - "n-of-1 trial methodology (see e.g. Kravitz & Duan, Ann Intern Med 2014)"
  - "Open Enzyme synthesis 2026-04-23 (microbiota safety discussion)"
  - "ALLN-346 Phase 2a safety profile (frame-of-reference)"
---

# Self-Experiment Protocol

**Purpose.** Open Enzyme is not pursuing regulatory approval. The purpose of this document is to lay out a minimum-viable monitoring plan for Brian's self-experimentation with engineered koji and the supplement stack — so that (a) the risks are known in advance, (b) the data is collected prospectively rather than reconstructed after the fact, (c) there are explicit halt criteria, and (d) the n-of-1 data is structured well enough to inform future collaborators (Rheinallt, Lauren, Valerie) if they decide to run anything more rigorous.

**Evidence level for this page.** The monitoring plan itself is Mechanistic Extrapolation — it assumes standard clinical safety monitoring principles applied to a novel intervention. The red-flag criteria are derived from known failure modes of related compounds (EGCG hepatotoxicity; immunomodulators → infection risk; chronic yeast dosing → dysbiosis), not from direct Open Enzyme data (which does not yet exist).

---

## 1. Scope

This protocol covers **oral self-administration** of:

- Engineered koji (when available) — uricase ± NLRP3 modulators
- Supplement stack components (currently: quercetin, ursolic acid, carnosine, BHB, KPV, EGCG, sulforaphane, curcumin, oridonin, β-caryophyllene, others per `wiki/supplements-stack.md`)
- Any new compound added during the self-experiment window

It does **not** cover:

- Injectable or IV products (not in scope for Open Enzyme)
- Off-label prescription drug modifications (separate conversation with Brian's physician)
- Diet/lifestyle changes unless they are part of a specific protocol arm

---

## 2. Timepoints

| Timepoint | Draw | Self-report | Notes |
|---|---|---|---|
| T0 (baseline) | Blood panel + stool 16S | Symptom diary start | Before first dose; establishes personal baseline |
| T1 (week 4) | Blood panel | Diary (daily) | Early signal window for hepatotox / CRP shift |
| T2 (week 8) | Blood panel | Diary (daily) | Mid-window; likely inflection for efficacy signals |
| T3 (week 12) | Blood panel + stool 16S | Diary (daily) | Primary endpoint window; microbiota re-sample |
| Ad hoc | Any time | Any time | If red-flag criterion triggers, halt and re-evaluate |

**Why this cadence.** 12 weeks is the minimum window for (a) microbiota community-level shifts to become detectable (~6-8 weeks for stable shifts), (b) chronic-dosing hepatotoxicity from EGCG/curcumin to manifest if it is going to, (c) meaningful changes in serum urate and flare frequency to aggregate. Monthly blood draws are cheap (~$80/panel at Quest) and catch acute problems before 12 weeks.

---

## 3. Blood panel (every 4 weeks)

Standard add-on to an annual physical; can be ordered through Quest / Labcorp or via direct-to-consumer services. Approximate total cost: **~$80-120 per draw**.

| Test | Why |
|---|---|
| **CBC with differential** | Catches infection, anemia, WBC shifts (monitor for immunosuppression from NLRP3 blockade — canakinumab's known side effect class) |
| **CMP (comprehensive metabolic panel)** | Liver enzymes (ALT, AST, ALP, bilirubin), kidney function (creatinine, BUN, eGFR), electrolytes. EGCG can cause hepatotoxicity at high dose; curcumin at very high dose; any koji contaminant (aflatoxin) would hit liver first. |
| **Uric acid** | Primary efficacy endpoint. Target: <6 mg/dL (or personal symptom-threshold if different). |
| **hs-CRP** | Systemic inflammation. Expected to drop if the NLRP3 pathway modulators are working. Doubling from baseline is a red flag. |
| **LDH** (optional, first + last draw) | Cell turnover; flag if anything is lysing |
| **HbA1c** (baseline + T3 only) | Some stack compounds (berberine, EGCG) affect glucose metabolism; useful baseline context |

---

## 4. Stool 16S (baseline + week 12 only)

A single paired baseline/endpoint microbiota sequencing is sufficient to detect whether chronic koji dosing has caused a dysbiotic shift. Quarterly re-sampling is overkill for personal use; the signal takes weeks to stabilize.

- **Service**: Direct-to-consumer options like BiomeSight, Tiny Health, Flore, or uBiome-successors; approximate cost ~$100-200 per sample.
- **Primary metrics**: alpha diversity (Shannon, Simpson) — flag >20% drop from baseline; beta diversity (UniFrac) — note magnitude of community shift; taxa abundance at phylum level — flag dramatic Firmicutes/Bacteroidetes ratio inversion, or loss of Faecalibacterium prausnitzii / Akkermansia muciniphila (both gout-protective commensals).
- **Secondary metrics** (if service provides): SCFA-producer abundance, LPS-producer abundance, uricase-gene carriage if detectable.
- **Caveat**: 16S resolution bottoms out at genus level for most taxa; it will not detect strain-level engineered-koji persistence. If strain persistence is a specific question, consider qPCR for the engineered cassette's selection marker on spiked stool.

---

## 5. Symptom diary (daily, 5 fields)

Goal: capture the signals that show up between blood draws, in a format that is quick to enter (<60 seconds/day) and easy to aggregate.

| Field | Scale | Notes |
|---|---|---|
| **Stool form** | Bristol 1-7 | Watch for sustained 6-7 (diarrhea) or 1-2 (constipation) |
| **Bloating / GI discomfort** | 0-3 (none / mild / moderate / severe) | |
| **Flare intensity** | 0-10 (0 = no joint pain, 10 = unable to walk) | Include affected joint and whether a new location |
| **Energy / fatigue** | 0-10 (0 = severe fatigue, 10 = unusually energetic) | Gut inflammation and systemic inflammation both manifest as fatigue |
| **Novel signal** | Free text (blank if nothing) | Rash, fever, headache, sleep, mood — anything not covered above |

Storage: simple spreadsheet, text file, or journaling app. Timestamped entries, one row per day. Export to CSV at endpoint for analysis.

---

## 6. Red-flag halt criteria

If **any** of the following occur, halt the intervention immediately, document the trigger, and re-evaluate before resuming:

1. **New GI bleeding** (blood in stool, melena, hematemesis) — halt + seek care same-day
2. **Persistent diarrhea >72 hours** — halt + evaluate for *C. difficile* / dysbiosis
3. **hs-CRP doubles from baseline** on a scheduled draw — halt + re-draw at 1 week to confirm
4. **Liver enzymes (ALT or AST) >2× upper limit of normal** — halt + re-draw at 2 weeks; evaluate which compound is most likely culprit (EGCG > curcumin > others)
5. **Unexplained weight loss >5 lb over 4 weeks** — halt + evaluate
6. **New fever without identified infection** — halt + seek care
7. **New joint involvement that does not resolve with standard gout management within 7 days** — halt + re-evaluate whether intervention is working *or* whether it's unmasking a new pattern
8. **Eosinophilia or new hypersensitivity signal** (rash, urticaria, angioedema) — halt immediately; consider allergic response to koji or a stack component
9. **Kidney function decline** (eGFR drop >15% from baseline or creatinine rise) — halt + evaluate (uricase + high-dose NLRP3 blockers both plausibly stress kidneys)

"Halt" means: stop all investigational Open Enzyme compounds (koji, any added supplement not previously in long-term use). It does **not** mean stop medically-prescribed therapy (allopurinol, colchicine) unless the trigger specifically implicates those.

---

## 7. Logging and version control

- **Raw data**: kept in a private, dated directory outside this public repo. Don't commit blood-panel PDFs or stool-report JSON into the wiki.
- **Summary log**: a stripped, de-identified summary can be added to `logs/self-experiment-log.md` (append-only). Fields: date, intervention (what's being taken), observation, any protocol deviation. This log is for Brian's own pattern-recognition, not for external eyes.
- **When a stack compound is added or removed**: note it in the log with a 1-line rationale. This is the counterpart to commit messages for the body.

---

## 8. What this protocol does NOT do

- **Establish efficacy against a control.** This is n-of-1, uncontrolled, unblinded. Any efficacy signal is suggestive at best. It is good enough to motivate a future controlled trial by a collaborator; it is not good enough to generalize.
- **Replace medical supervision.** Brian's primary care + rheumatologist should know what he's doing. The blood panels should land in their system, not just his. Red-flag criteria are escalation-to-care triggers, not self-directed.
- **Cover regulatory territory.** Open Enzyme is a research project; this is personal self-experimentation. Do not distribute engineered strains to others under this protocol — that requires a different framework (see `wiki/open-source-platform.md` on strain-sharing).

---

## 9. Review and update

Review this document: (a) before starting a new intervention arm, (b) after any red-flag halt, (c) at least annually, (d) whenever new stack compounds or engineered strains are added to the self-experiment. Changes tracked in git, not inline.
