---
prompt_id: 03-nlrp3-mechanism-inference
task_type: mechanism-inference
provenance: synthetic-but-realistic (mirrors Pass 2 mechanism-inference)
target_output_tokens: 800
notes: |
  Mechanism-inference task. Tests whether vendors propose the same upstream
  mechanism for an observation. Expected: meaningful disagreement on
  WHICH mechanism is dominant when multiple are plausible.
---

# Prompt

You are reasoning through a mechanism-inference question for a working scientific wiki on gout and NLRP3-driven inflammation. Audience: PhD-level scientists. State evidence levels and where alternative mechanisms exist, name them explicitly rather than collapsing to the most-cited one.

Observation: Monosodium urate (MSU) crystals in joint tissue activate the NLRP3 inflammasome in resident macrophages, leading to caspase-1 cleavage and IL-1β release. The classical model (signal-1 + signal-2) requires both a priming step (TLR-mediated NF-κB transcription of pro-IL-1β and NLRP3 itself) AND an activating step (the MSU crystal).

Question: In a gout patient with chronic hyperuricemia but NO active flare, joint-resident macrophages are NOT in an inflammasome-activated state despite continuous MSU crystal deposition in tophi. When a flare is triggered (e.g., by an alcohol-binge or a high-purine meal), the macrophages activate within hours.

Propose the three most plausible mechanisms by which the *priming signal* (signal-1) becomes available during a flare trigger but not during chronic-stable tophi presence. For each:

1. Name the mechanism precisely (molecular species, receptor, source tissue)
2. State its evidence level (in vitro / animal / human / mechanistic extrapolation) and cite at least one primary source if you have one
3. Note which mechanism you would prioritize for an in-vivo test, and why
4. Flag any mechanism that is plausible but where the experimental evidence is thin or contested

Then identify ONE alternative non-priming explanation (e.g., something other than signal-1 availability) that would also explain the trigger-driven onset, and say why you find it less likely.
