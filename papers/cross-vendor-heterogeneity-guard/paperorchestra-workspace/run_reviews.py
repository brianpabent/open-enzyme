#!/usr/bin/env python3
"""
Cross-vendor review orchestrator.

Fires the three review prompts from review-prompts.md against actual
vendor models via OpenRouter:

  Prompt 1 → deepseek/deepseek-v4-pro on §4 + §5
  Prompt 2 → google/gemini-2.5-pro    on §3 + §6 + §7
  Prompt 3 → anthropic/claude-opus-4-7 AND deepseek/deepseek-v4-pro on §2 (parallel)

Reads OPENROUTER_API_KEY from Open Enzyme's .env (one level above this
workspace). Writes each review's verbatim output to reviews/<filename>.md
and emits a session-summary to stdout for paste into revisions.md.

Run: python3 run_reviews.py
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.request
import urllib.error
import certifi
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# macOS Python 3.13 ships without a system cert bundle; wire certifi in.
SSL_CTX = ssl.create_default_context(cafile=certifi.where())

WS = Path(__file__).parent
PAPER_DIR = WS.parent
OE_ROOT = PAPER_DIR.parent.parent  # Open Enzyme/
REVIEWS_DIR = WS / "reviews"
REVIEWS_DIR.mkdir(exist_ok=True)

# Load OpenRouter key from OE .env
env_path = OE_ROOT / ".env"
api_key = None
for line in env_path.read_text().splitlines():
    if line.startswith("OPENROUTER_API_KEY="):
        api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break
if not api_key:
    sys.exit("ERROR: OPENROUTER_API_KEY not found in Open Enzyme/.env")
print(f"Loaded OpenRouter key (prefix {api_key[:8]}..., {len(api_key)} chars)")


def extract_sections(md_path: Path, section_titles: list[str]) -> str:
    """Extract one or more `## §N ...` sections verbatim and concatenate."""
    md = md_path.read_text()
    parts = re.split(r"\n(?=## )", md)
    wanted = []
    for p in parts:
        first = p.split("\n", 1)[0].strip()
        for t in section_titles:
            if first.startswith(t):
                wanted.append(p)
                break
    if not wanted:
        sys.exit(f"ERROR: none of {section_titles} found in {md_path}")
    return "\n\n".join(wanted)


def call_openrouter(model: str, prompt: str, timeout: int = 300) -> dict:
    """Single chat-completion request to OpenRouter."""
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/brianpabent/open-enzyme",
            "X-Title": "Open Enzyme cross-vendor heterogeneity-guard paper review",
        },
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"error": f"HTTP {e.code}: {body[:500]}", "latency_s": time.time() - t0}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}", "latency_s": time.time() - t0}
    return {
        "content": data["choices"][0]["message"]["content"],
        "usage": data.get("usage", {}),
        "model_returned": data.get("model"),
        "latency_s": time.time() - t0,
    }


PROMPT_1 = """You are running an independent cross-vendor review of a draft scientific paper titled \
"Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted \
scientific literature synthesis." You are DeepSeek V4-Pro. The primary drafter was \
Anthropic Claude Opus 4.7. The paper's central methodology — which this review is part \
of — is that any draft authored by one vendor's model must be independently reviewed \
by a different vendor's model so that vendor-specific blind spots are surfaced.

Your role: review §4 (the heterogeneity-guard rationale) and §5 (four case-study \
vignettes), and emit catches in the format below.

What to check:

1. PRIOR-DISTRIBUTION CLAIMS. §4 asserts that cross-vendor heterogeneity provides \
prior-distribution diversity that within-vendor heterogeneity does not. Stress-test \
this claim. Where is the argument weakest? Where would a skeptical ML reviewer push back?

2. ANTHROPIC-FAVORABLE FRAMING. The primary drafter is an Anthropic model. Watch for \
over-claiming Anthropic's role, under-citing competing vendors, or framing that subtly \
elevates Claude's contribution at the expense of DeepSeek's contribution.

3. FACTUAL CLAIMS IN §5. Each case study makes specific factual claims about an \
operational incident — dates, model versions, numerical magnitudes. Flag any claim \
that strikes you as unsupported by the in-text evidence.

4. THE HOMOGENIZATION DEFINITION. §4 defines epistemic homogenization as distinct from \
per-output hallucination. Is the definition tight? Counterexamples that would weaken it?

5. THE SELF-DEMONSTRATING MOMENT (§4 closing paragraph, §5.4). Is it presented as \
strongly as the evidence supports? Is it over-claimed?

6. ANY CLAIM THAT FEELS TOO CONFIDENT. The paper is a methodology argument with N=1 \
operational deployment. Flag any sentence that overstates what the operational record \
demonstrates.

Output format — one numbered entry per catch:

### Catch N — [section §X.Y]

**Claim under review:** [paste the specific sentence or passage]

**Verdict:** [Confirmed / Partial / Push-back / Rejected]

**Reasoning:** [1-3 sentences explaining the catch]

**Suggested correction:** [proposed rewrite, or "drop the claim," or "needs additional evidence: <what>"]

If a section is clean and you have no catches, say so explicitly — "No catches on §X.Y" — \
rather than producing low-confidence findings to fill the format.

---

{SECTIONS}
"""

PROMPT_2 = """You are running an independent cross-vendor review of a draft scientific paper titled \
"Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted \
scientific literature synthesis." You are Google Gemini 2.5 Pro. The primary drafter was \
Anthropic Claude Opus 4.7.

Your role: review §3 (architecture), §6 (operational data), and §7 (limitations and \
failure modes), and emit catches in the format below.

What to check:

1. ARCHITECTURAL ACCURACY. §3 describes the daemon as three operational passes plus an \
episodic peer-review pattern. Flag any architectural claim that seems internally \
inconsistent or that strains plausibility.

2. MODEL ASSIGNMENT CLAIMS. §3 names specific models for each pass. The Table 1 in §6 \
restates these. Check for internal consistency.

3. OPERATIONAL DATA. §6 cites specific cost and latency numbers. Are the numbers \
internally consistent? Do the per-pass costs roughly sum to the claimed three-pass total?

4. GOOGLE-FAVORABLE FRAMING. You are a Google model. Watch for any framing that subtly \
under-credits Google's role, or any framing that over-claims it. The review pass is for \
reciprocal asymmetry-detection.

5. LIMITATIONS COMPLETENESS. §7 enumerates failure classes the architecture does NOT \
protect against. What's missing? Is there a failure class that should be enumerated \
but isn't?

6. WHEN-THIS-MATTERS / WHEN-IT-DOESN'T (§7 final subsection). Stress-test the line. Are \
there cases on either side that the framing gets wrong?

Output format — one numbered entry per catch:

### Catch N — [section §X.Y]

**Claim under review:** [paste the specific sentence or passage]

**Verdict:** [Confirmed / Partial / Push-back / Rejected]

**Reasoning:** [1-3 sentences explaining the catch]

**Suggested correction:** [proposed rewrite, or "drop the claim," or "needs additional evidence: <what>"]

If a section is clean and you have no catches, say so explicitly.

---

{SECTIONS}
"""

PROMPT_3 = """You are running an independent cross-vendor review of §2 (Related Work) of a draft \
scientific paper titled "Cross-vendor heterogeneity as a guard against epistemic \
homogenization in AI-assisted scientific literature synthesis." §2 was drafted via the \
Ar9av/PaperOrchestra community implementation, driven by an Anthropic Claude session \
(Path B install). All 11 cited papers have been verified against Semantic Scholar.

Your role: review §2 for citation accuracy, framing of prior work, and any drift toward \
Anthropic-favorable or PaperOrchestra-favorable framing.

What to check:

1. CITATION ACCURACY. The §2 prose makes specific claims attributed to specific papers \
(Du et al. 2023, Madaan et al. 2023, Shinn et al. 2023, Verga et al. 2024, Bai et al. \
2022, Lee et al. 2023, Lu et al. 2024, Yamada et al. 2025, Song et al. 2026, Shumailov \
et al. 2023+2024). Are the attributions consistent with what those papers are actually \
known for? Flag any obviously mis-attributed claim.

2. THE CROSS-VENDOR / WITHIN-VENDOR DISTINCTION. The whole argument is that cross-vendor \
heterogeneity is a different abstraction level than the multi-agent / multi-model \
patterns in the existing literature. Flag any sentence that blurs this distinction.

3. FRAMING OF PRIOR WORK. Each prior approach should be described accurately and without \
straw-manning. Flag any prior approach that's misrepresented to make the paper's \
contribution look bigger.

4. NOVELTY CLAIMS. The paper's contribution is the application of ensemble logic at the \
vendor level for AI-assisted scientific synthesis. Flag any sentence that over-claims \
novelty beyond this specific framing.

5. DRAFTER-VENDOR-FAVORABLE FRAMING. The drafter is Anthropic. Watch for over-citing \
Anthropic-adjacent work (Constitutional AI, RLAIF) or under-citing competing vendors' \
research.

6. THE POLL DISCUSSION (§2.3). The paper now notes that Verga et al.'s PoLL is itself \
cross-vendor (Cohere/OpenAI/Anthropic). Is this framed accurately? Is the relocation of \
the distinction to "abstraction level of application" credible?

Output format — one numbered entry per catch:

### Catch N — [section §X.Y]

**Claim under review:** [paste the specific sentence or passage]

**Verdict:** [Confirmed / Partial / Push-back / Rejected]

**Reasoning:** [1-3 sentences explaining the catch]

**Suggested correction:** [proposed rewrite, or "drop the claim," or "needs additional evidence: <what>"]

If a section is clean and you have no catches, say so explicitly.

---

{SECTIONS}
"""


def main():
    draft = PAPER_DIR / "draft.md"

    sec_4_5 = extract_sections(draft, ["## §4 ", "## §5 "])
    sec_3_6_7 = extract_sections(draft, ["## §3 ", "## §6 ", "## §7 "])
    sec_2 = extract_sections(draft, ["## §2 "])

    jobs = [
        ("deepseek-on-4-5",    "deepseek/deepseek-v4-pro",   PROMPT_1.replace("{SECTIONS}", sec_4_5)),
        ("gemini-on-3-6-7",    "google/gemini-2.5-pro",      PROMPT_2.replace("{SECTIONS}", sec_3_6_7)),
        ("claude-on-2",        "anthropic/claude-opus-4.5",  PROMPT_3.replace("{SECTIONS}", sec_2)),
        ("deepseek-on-2",      "deepseek/deepseek-v4-pro",   PROMPT_3.replace("{SECTIONS}", sec_2)),
    ]

    print(f"\nFiring {len(jobs)} review jobs in parallel:")
    for tag, model, _ in jobs:
        print(f"  [{tag}] → {model}")

    results = {}
    with ThreadPoolExecutor(max_workers=4) as ex:
        future_to_tag = {ex.submit(call_openrouter, model, prompt): tag for tag, model, prompt in jobs}
        for fut in future_to_tag:
            tag = future_to_tag[fut]
            try:
                results[tag] = fut.result()
            except Exception as e:
                results[tag] = {"error": str(e)}

    # Persist each output
    for tag, model, _ in jobs:
        r = results[tag]
        out_path = REVIEWS_DIR / f"{tag}.md"
        if "error" in r:
            out_path.write_text(f"# {tag}\n\n**FAILED:** {r['error']}\n\nlatency: {r.get('latency_s',0):.1f}s\n")
            print(f"  [{tag}] FAILED: {r['error'][:120]}")
        else:
            md = (
                f"# Cross-vendor review — {tag}\n\n"
                f"**Model requested:** `{model}`\n"
                f"**Model returned:** `{r.get('model_returned','?')}`\n"
                f"**Latency:** {r['latency_s']:.1f}s\n"
                f"**Usage:** {r.get('usage',{})}\n\n"
                f"---\n\n{r['content']}\n"
            )
            out_path.write_text(md)
            usage = r.get("usage", {})
            print(f"  [{tag}] OK — {r['latency_s']:.1f}s, "
                  f"in={usage.get('prompt_tokens','?')}, out={usage.get('completion_tokens','?')}")

    print(f"\nAll outputs in: {REVIEWS_DIR}")


if __name__ == "__main__":
    main()
