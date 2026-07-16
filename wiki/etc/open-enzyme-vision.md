---
title: Open Enzyme — Mission and Operating Principles
date: 2026-07-16
tags: [gout, red teaming, exploit mapping, engineering, research strategy]
status: current
---

# Open Enzyme: Mission and Operating Principles

## Mission

**Use red-teaming techniques to identify exploitable weaknesses in gout, and use creative engineering to exploit them.**

The target is gout as a system: urate production and transport, crystal formation, immune priming and activation, inflammatory amplification, resolution, delivery, adherence, and translation. The intervention is not predetermined. It may be an enzyme, organism, molecule, formulation, device, delivery route, repurposed drug, or combination.

Open Enzyme is Phase 0 research and design. It does not provide medical advice or treat a mechanistic hypothesis as clinical evidence.

## Operating model

1. **Map the system.** Describe the causal chain, compartments, chokepoints, feedback loops, and boundary conditions.
2. **Attack the map.** Look for bottlenecks, mismatched assumptions, unprotected interfaces, neglected populations, and ways one subsystem can be used against another.
3. **Create falsifiable tracks.** Turn a plausible exploit into a specific intervention hypothesis with explicit assumptions and safety constraints.
4. **Run the cheapest discriminating test.** Prefer a result that kills, redirects, or strengthens a track over work that merely adds detail.
5. **Update the portfolio.** Promote, revise, pause, or kill the track. Preserve the evidence that changes the current conclusion; use Git for superseded prose and process history.

The [NLRP3 exploit map](../nlrp3-exploit-map.md), [gout kill-chain and delivery routes](../gout-kill-chain-delivery-routes.md), and [validation experiments](../validation-experiments.md) are current implementations of this method.

## Tracks, not a product chain

Open Enzyme is a portfolio of attacks on gout. Current tracks include:

- gut-lumen urate degradation and other urate sinks;
- engineered koji and yeast enzyme production;
- engineered live biotherapeutics and purine-degrading bacteria;
- renal transporter modulation, including URAT1 and ABCG2;
- complement, NLRP3, gasdermin-D, and inflammatory-resolution interventions;
- repurposed or reformulated compounds;
- medicinal-mushroom and traditional-medicine leads evaluated with modern evidence standards;
- local, systemic, and compartment-specific delivery strategies.

The [track template](./track-template.md) defines the common contract. The [koji track](../koji-track.md) is the first reference implementation.

No chassis is the mission. No requirement says one strain must carry every useful payload. Accessibility, food-grade production, and open-source reproducibility are valuable engineering objectives when a track can support them; they are not evidence that the biology works and they are not constraints on unrelated tracks.

## What failure means

A failed experiment updates the smallest claim justified by the evidence.

- Failure to express a payload in *A. oryzae* weakens that payload–chassis pairing.
- Failure of community fermentation weakens that production model.
- Failure of luminal uricase at physiological conditions weakens that topology or the broader gut-sink track, depending on the experiment.
- None of those results, alone, falsifies the red-team mission.

A track is killed when its stated kill criteria fire. The next move is to preserve what the result teaches about the gout system and redirect effort to a better exploit.

## Evidence and authorship discipline

- Distinguish clinical, animal, in-vitro, computational, and mechanistic evidence.
- Source the project claim before challenging it. Do not invent a stronger claim to make a critique easier.
- Keep detailed evidence in one canonical home; other pages link and state only the local implication.
- Verify load-bearing numbers against primary sources before they enter the corpus.
- Computational evidence requires current hash-bound pre-run, post-run, and push-review receipts where the modern COMP lifecycle applies.
- Keep current scientific state in the live tree. Git is the revision history.

## Knowledge-system cadence

Every push publishes the current site. Relevant pushes receive bounded propagation, and changed COMPs receive independent exact-artifact review before COMP-derived claims can propagate. Full-corpus synthesis is an explicit batch operation: it reads the current corpus in full, searches for cross-domain connections, reopens the raw sources behind candidates, and advances its own coverage cursor only after independent review.

This split preserves grounded creativity without paying for a full sweep on every push.
