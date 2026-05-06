# operations/

**Operational / transactional content for the Open Enzyme project.** Public by default — same posture as the rest of this repo. Open Enzyme is open-source / radical-transparency by design (`wiki/open-source-platform.md`); the operational layer is no exception. Everything here is visible on GitHub for the same reason the wiki and experiments are: the project's value compounds when its working state is fully inspectable. Outreach context, project todos, lab partnership scoping, decision logs — all of it is fine to be public and arguably better that way (collaborators and future contributors get the full operating picture, not just the polished research surface).

## How this differs from `wiki/` and `experiments/`

The boundary is **epistemic, not visibility.** All three folders are public.

- **`wiki/`** — research library. PhD-audience. Mechanism + evidence + chokepoint-mapped + evidence-tier-tagged. The substrate the sweep daemon operates on; the substrate external collaborators evaluate. Rigorous.
- **`experiments/`** — reproducible comp-NNN computational artifacts. Peer-reviewable, scripts + inputs + outputs committed. The substrate any collaborator can clone and re-run.
- **`operations/`** — transactional working state. Outreach context, todos, action items, decision logs. Public, but not held to the same evidence-tier-rigor bar as `wiki/` because it's not research content — it's the operating layer that surrounds the research.

## What lives here

- **Outreach context pages** — substantive context (not literal email drafts) for reaching out to specific labs, CROs, collaborators, partners (e.g., `ward-1995-lab-access.md`)
- **Active-todo lists** — scattered action items that don't fit the `wiki/synthesis.md` Strategic Reflections Queue (which is for content-triggered research-strategy reflections, not transactional todos)
- **Project-state checkpoints** — periodic snapshots of where things stand, useful for orientation but not research material
- **Procedural notes** — how-to-execute-X content that's specific to the project's operational flow rather than generalizable methodology
- **Decision logs** — when something operational was decided, why, who decided. Public audit trail of how the project actually runs.

## What does NOT live here (and what does NOT live anywhere in this repo)

The PII / hygiene filters that apply to the rest of the repo apply here too. Operational ≠ private; operational ≠ exempt-from-content-rules.

- **Mechanism, evidence, or hypothesis content** → `wiki/`
- **Reproducible computational analyses** → `experiments/comp-NNN-*/`
- **Falsification cards** → `wiki/hypotheses/`
- **Pre-registration / claim-tracking** → `wiki/hypotheses/` (with frozen-on-commit discipline)
- **Personal medical content (specific lab values, clinical-decision data, PHI)** → private sibling repos per the umbrella `~/Documents/Claude/Projects/abent/CLAUDE.md` privacy boundary; never in this repo. Operational notes about *cadence* or *framework* are fine in the public wiki / operations; specific values are not.
- **Personal financial content** → never in this repo (umbrella privacy boundary)
- **Family-private content** → never in this repo
- **Sensitive credentials, API keys, secrets** → never anywhere in version control
- **Specific people's private contact info** they haven't published — verifiable corresponding-author emails on published papers are fine; phone numbers, personal cell, internal-only emails are not

## Why this folder exists

Drawn 2026-05-05 in response to a specific structural mistake: an operational outreach page (literal email draft + fee structures + "email Maruyama tomorrow morning" calendar plan) was initially placed in `wiki/`, blurring the line between research library and transactional working state. Brian's correction surfaced the actual reframe: the boundary is epistemic (research vs. operational), not visibility (public vs. private). Both layers stay public; both stay subject to PII / credential hygiene; but they answer different questions and serve different readers. Splitting the layers preserves the wiki's PhD-audience integrity while giving the operational working state a clean home.

Same structural pattern as `experiments/` (created earlier when computational analyses needed peer-reviewable artifact homes distinct from the wiki narrative).

## How to add content here

1. Decide it doesn't belong in `wiki/` (research) or `experiments/` (computational artifact). If unsure, default to `wiki/` and only move here if the content turns out to be transactional / outreach / todo-style.
2. Create the file with a clear, dated, scoped name (e.g., `ward-1995-lab-access.md`, `2026-05-05-self-experiment-supply-list.md`).
3. Frontmatter is optional but recommended for operational pages — at minimum `title`, `date`, `status` (active / archived / done).
4. Cross-link to relevant `wiki/` pages where the underlying research lives. Don't duplicate research content here.

## Index

- [`ward-1995-lab-access.md`](./ward-1995-lab-access.md) — global lab-access landscape for §1.9 Ward 1995 dual-cassette feasibility test (active outreach in flight)
- [`todos.md`](./todos.md) — active operational todos across the project
- [`notable-moments.md`](./notable-moments.md) — append-only log of project moments worth external communication (blog posts, LinkedIn posts, talks). Translated for non-scientific human readers.

## Standing rule — log noteworthy moments as they happen

Whenever something genuinely remarkable, noteworthy, or surprising happens in the project — a long-held assumption breaks, a methodology produces a non-trivial result, AI-assisted research velocity does something a human-only workflow couldn't, an external collaborator engages meaningfully, a wet-lab result lands — **add an entry to [`notable-moments.md`](./notable-moments.md) immediately**, while the context is fresh. Don't batch noteworthy-moment-logging; the freshness is part of the value.

The log is for **non-scientific human readers** — write it accessibly, not in evidence-tier-tagged PhD-audience prose. Translate the science into plain language. The notable-moments log is the substrate for actual external communication; the wiki is the substrate for evaluating the project rigorously. Different jobs.

### Every entry must include the honest caveats — those ARE the recruiting angle

**Don't make these entries marketing fluff.** Every notable-moment entry must include a "what's still open / what could kill this / what we don't yet know" section, framed honestly. The substance of the caveats — the unresolved questions, the wet-lab unknowns, the mechanism gaps — is **itself the angle that makes the project engaging to external readers.** A post that says "we figured out CP0!" is a marketing claim that smart readers will discount. A post that says "we found a path that closes 80% of the CP0 problem in silico, here are the three specific things wet-lab still has to confirm, and here's what helping with question #2 would look like" is a substantive invitation that smart readers can act on.

The recruiting / engagement model the project actually wants:
- **Substance attracts substance.** Researchers working on related questions read honest "here's what's open" framing and recognize it as an invitation to collaborate.
- **Honest caveats build trust.** Readers who see the project naming its own unknowns trust the things it claims as solved.
- **Open questions are concrete asks.** "Does the SCR1-4 truncated DAF retain CCP-regulatory activity?" is a question a complement biologist can immediately know whether they can help answer, vs. a vague "we're working on complement regulation in gout."

This is the same epistemic discipline as the wiki's evidence-tier rule (Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation). The notable-moments log applies the discipline at the external-communication layer.

### When the moment becomes external

When a notable-moment entry actually gets used externally (LinkedIn post lands, talk gets given, podcast soundbite happens, blog post published), append a "Used in:" line at the bottom of the entry with the URL/venue + date. Keep the entry — the log is also a record of what's been said publicly about the project.

### Mutual-audit invitation — standing posture

Whenever a notable-moment entry surfaces a finding about another project, tool, paper, or claim, the entry MUST close with the **explicit reciprocal invitation:** Open Enzyme is published in public for exactly the same reason — so that other people can find OUR mistakes and make us better. The verification disciplines we apply to other people's tools (grep every number, anchor identity to canonical metadata, cross-check every claim, line-anchored citation) apply equally to anyone auditing this corpus. We hope readers push back on our evidence-tier tags, find the edges in our chokepoint claims, surface the mechanisms we haven't documented honestly enough.

**This isn't a softener after a critical finding.** It's the structural premise of the whole project. Open infrastructure compounds when downstream users audit upstream tools AND upstream tools audit downstream uses. We're trying to be a participant in that feedback loop, not just a beneficiary of it. If you find a mistake in this corpus — a wrong PMID, a fabricated number, an evidence-tier inflation, a missing limitation, a wrong-direction mechanistic claim — please tell us. **That's the deal we're trying to participate in.**

Triggered by Brian 2026-05-05: "and we hope people find our mistakes and make us better too" — said in response to the Paperclip notable-moment entry. The reciprocal-invitation language is the closing posture of every relevant entry from now on; not optional.

This standing rule was added 2026-05-05 in the same conversation that created the file, after observing that ~6 hours of working session moved CP0 from "platform gap" to "active engineering candidate" — the kind of arc that's invisible in commits but exactly what an external reader would find compelling. If we don't log these moments as they happen, they evaporate into git history that nobody reads.
