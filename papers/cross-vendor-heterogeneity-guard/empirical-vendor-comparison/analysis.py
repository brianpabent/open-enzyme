#!/usr/bin/env python3
"""
analysis.py — compute agreement metrics from collected vendor responses.

Reads responses/<prompt-id>/<vendor>.md (one per pair), reads the
hand-curated claims from outputs/claims/<prompt-id>.json (claim extraction
is upstream of this script — see README), and computes:

- per-prompt pairwise agreement matrix (4 vendors -> 6 pairs)
- mean pairwise agreement rate
- disagreement classification breakdown (factual / interpretive / mechanism /
  refusal / not-addressed)
- aggregate stats by task type (factual / mechanism-inference / hypothesis-gen / synthesis / adversarial-review)
- cost + token accounting

Outputs to outputs/agreement-matrix.json, outputs/summary.md.
"""

import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROMPTS_DIR = HERE / "prompts"
RESPONSES_DIR = HERE / "responses"
OUTPUTS_DIR = HERE / "outputs"
CLAIMS_DIR = OUTPUTS_DIR / "claims"

# Pricing fallback (in case run_experiment.py's earlier version recorded
# cost_usd: 0.0000 because the slug didn't match a pricing key).
PRICING_USD_PER_MTOK = {
    "google/gemini-2.5-pro":      (1.25, 5.00),
    "deepseek/deepseek-v4-pro":   (0.435, 0.87),
    "anthropic/claude-opus-4-7":  (15.00, 75.00),
    "anthropic/claude-4.7-opus":  (15.00, 75.00),
    "openai/gpt-5.5":             (3.00, 12.00),
    "openai/gpt-5":               (2.50, 10.00),
}

VENDORS = ["deepseek", "gemini", "openai", "anthropic"]

# Verdict vocabulary for the per-claim agreement coding.
# - "affirm":      vendor's response asserts the same factual/mechanistic content
# - "deny":        vendor's response asserts the opposite or contradicts it
# - "ignore":      vendor's response does not address the claim
# - "disagree":    vendor's response addresses the claim but lands on a different
#                  number / mechanism / framing (substantive disagreement,
#                  short of contradiction)
# - "refusal":     vendor declined the prompt (no content)
VERDICT_VALUES = {"affirm", "deny", "ignore", "disagree", "refusal"}


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    body = text[3:]
    m = re.search(r"^---\s*$", body, re.MULTILINE)
    if not m:
        return {}, text
    fm_raw = body[:m.start()]
    rest = body[m.end():].lstrip("\n")
    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, rest


def load_response(prompt_id, vendor):
    p = RESPONSES_DIR / prompt_id / f"{vendor}.md"
    if not p.exists():
        return None
    text = p.read_text()
    fm, body = parse_frontmatter(text)
    return {"path": str(p), "frontmatter": fm, "body": body}


def cost_of(model_slug, in_tok, out_tok):
    base = model_slug.split(":", 1)[0]
    base = re.sub(r"-\d{8}$", "", base)
    p = PRICING_USD_PER_MTOK.get(base)
    if not p:
        return 0.0
    return in_tok * p[0] / 1_000_000 + out_tok * p[1] / 1_000_000


def fix_cost(fm):
    """If frontmatter cost_usd is 0.0000, recompute from served model + tokens."""
    cost = float(fm.get("cost_usd", 0) or 0)
    if cost > 0:
        return cost
    try:
        served = fm.get("model_served", "")
        in_tok = int(fm.get("input_tokens", 0) or 0)
        out_tok = int(fm.get("output_tokens", 0) or 0)
        return cost_of(served, in_tok, out_tok)
    except Exception:
        return 0.0


def load_prompt_meta(prompt_id):
    p = PROMPTS_DIR / f"{prompt_id}.md"
    text = p.read_text()
    fm, _ = parse_frontmatter(text)
    return fm


def load_claims(prompt_id):
    """Load hand-curated claims + per-vendor verdicts."""
    p = CLAIMS_DIR / f"{prompt_id}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text())


def pairwise_agreement(claims_for_prompt):
    """
    Given a structure:
        {
          "claims": [
            {
              "id": "...",
              "claim_text": "...",
              "verdicts": {
                "deepseek": {"verdict": "affirm", ...},
                "gemini":   {"verdict": "affirm", ...},
                ...
              }
            },
            ...
          ]
        }
    return:
        {
          (vendor_a, vendor_b): {
            "n_claims": N,
            "n_agree_substantive": int,   # both affirm OR both deny OR both disagree-similarly
            "n_one_ignored": int,         # one addressed, one didn't
            "n_substantive_disagreement": int,
            "n_refusal_involved": int,
            "agreement_rate": float (over claims where BOTH vendors addressed),
          }
        }

    Two vendors AGREE on a claim if they:
      - both "affirm"
      - both "deny"
      - both "disagree" on the same alternative (we mark this by storing
        the alternative in verdicts[v]["alternative"] and comparing strings)
      - both "refusal" (trivially equal)

    They DISAGREE substantively if:
      - one affirm + other deny
      - one affirm + other disagree (different position)
      - one deny + other disagree (different position)
      - both disagree but on different alternatives

    "One-ignored" is excluded from the denominator (it's "not addressed,"
    not disagreement).
    """
    pairs = {}
    for i, va in enumerate(VENDORS):
        for vb in VENDORS[i+1:]:
            stat = {
                "n_claims": 0,
                "n_agree_substantive": 0,
                "n_one_ignored": 0,
                "n_both_ignored": 0,
                "n_substantive_disagreement": 0,
                "n_refusal_involved": 0,
            }
            for claim in claims_for_prompt["claims"]:
                stat["n_claims"] += 1
                ra = claim["verdicts"].get(va, {}).get("verdict", "ignore")
                rb = claim["verdicts"].get(vb, {}).get("verdict", "ignore")
                aa = claim["verdicts"].get(va, {}).get("alternative", "")
                ab = claim["verdicts"].get(vb, {}).get("alternative", "")

                if ra == "refusal" or rb == "refusal":
                    stat["n_refusal_involved"] += 1
                    if ra == rb:
                        stat["n_agree_substantive"] += 1  # both refused
                    continue

                if ra == "ignore" and rb == "ignore":
                    stat["n_both_ignored"] += 1
                    continue
                if ra == "ignore" or rb == "ignore":
                    stat["n_one_ignored"] += 1
                    continue

                # Both addressed substantively
                if ra == rb:
                    if ra == "disagree":
                        if aa.strip() and aa.strip() == ab.strip():
                            stat["n_agree_substantive"] += 1
                        else:
                            stat["n_substantive_disagreement"] += 1
                    else:
                        stat["n_agree_substantive"] += 1
                else:
                    stat["n_substantive_disagreement"] += 1

            denom = stat["n_agree_substantive"] + stat["n_substantive_disagreement"]
            stat["agreement_rate"] = (stat["n_agree_substantive"] / denom) if denom else None
            pairs[f"{va}_vs_{vb}"] = stat
    return pairs


def main():
    OUTPUTS_DIR.mkdir(exist_ok=True)
    CLAIMS_DIR.mkdir(exist_ok=True)

    prompts = sorted(p.stem for p in PROMPTS_DIR.glob("*.md"))

    # Per-prompt summary: response metadata + claim file presence
    per_prompt = []
    total_cost = 0.0
    for prompt_id in prompts:
        meta = load_prompt_meta(prompt_id)
        responses = {}
        for v in VENDORS:
            r = load_response(prompt_id, v)
            if r is None:
                responses[v] = {"status": "MISSING"}
                continue
            fm = r["frontmatter"]
            status = fm.get("status", "ok")
            cost = fix_cost(fm) if status == "ok" else 0.0
            total_cost += cost
            responses[v] = {
                "status": status,
                "model_served": fm.get("model_served", ""),
                "input_tokens": int(fm.get("input_tokens", 0) or 0),
                "output_tokens": int(fm.get("output_tokens", 0) or 0),
                "cost_usd": round(cost, 4),
                "latency_seconds": float(fm.get("latency_seconds", 0) or 0),
                "finish_reason": fm.get("finish_reason", ""),
                "response_sha": fm.get("response_sha256_12", ""),
                "body_chars": len(r["body"]) if r["body"] else 0,
            }

        claims = load_claims(prompt_id)
        agreement = pairwise_agreement(claims) if claims else None

        per_prompt.append({
            "prompt_id": prompt_id,
            "task_type": meta.get("task_type", "unknown"),
            "responses": responses,
            "claims_loaded": claims is not None,
            "n_claims": (len(claims["claims"]) if claims else 0),
            "agreement": agreement,
        })

    # Aggregate metrics
    aggregate = {
        "total_prompts": len(prompts),
        "vendors": VENDORS,
        "total_cost_usd": round(total_cost, 4),
        "pairwise_means": {},
        "by_task_type": {},
    }

    # Pairwise mean agreement rate across all prompts with claims
    pair_rates = collections.defaultdict(list)
    for pp in per_prompt:
        if not pp["agreement"]:
            continue
        for pair_key, stat in pp["agreement"].items():
            if stat["agreement_rate"] is not None:
                pair_rates[pair_key].append(stat["agreement_rate"])
    for pair_key, rates in pair_rates.items():
        aggregate["pairwise_means"][pair_key] = {
            "n_prompts": len(rates),
            "mean_agreement_rate": round(sum(rates) / len(rates), 3) if rates else None,
        }

    # By task type
    task_buckets = collections.defaultdict(list)  # task_type -> list of (pair_key, rate)
    for pp in per_prompt:
        if not pp["agreement"]:
            continue
        for pair_key, stat in pp["agreement"].items():
            if stat["agreement_rate"] is not None:
                task_buckets[pp["task_type"]].append(stat["agreement_rate"])
    for tt, rates in task_buckets.items():
        aggregate["by_task_type"][tt] = {
            "n_data_points": len(rates),
            "mean_agreement_rate": round(sum(rates) / len(rates), 3) if rates else None,
            "min": round(min(rates), 3) if rates else None,
            "max": round(max(rates), 3) if rates else None,
        }

    # Refusal counts per vendor
    aggregate["refusals_by_vendor"] = {v: 0 for v in VENDORS}
    aggregate["empties_by_vendor"] = {v: 0 for v in VENDORS}
    aggregate["ok_by_vendor"] = {v: 0 for v in VENDORS}
    for pp in per_prompt:
        for v, r in pp["responses"].items():
            status = r.get("status", "")
            if status == "ok":
                aggregate["ok_by_vendor"][v] += 1
            elif status in ("EMPTY", "empty", "ERROR", "error"):
                # Distinguish refusals from other failures via finish_reason
                fr = r.get("finish_reason", "")
                if fr == "stop":  # native_finish_reason: refusal mapped to stop
                    aggregate["refusals_by_vendor"][v] += 1
                else:
                    aggregate["empties_by_vendor"][v] += 1

    out = {
        "per_prompt": per_prompt,
        "aggregate": aggregate,
    }

    (OUTPUTS_DIR / "agreement-matrix.json").write_text(json.dumps(out, indent=2))

    # Human-readable summary
    lines = []
    lines.append("# Empirical vendor-comparison summary\n")
    lines.append(f"- Prompts: {len(prompts)}")
    lines.append(f"- Vendors: {', '.join(VENDORS)}")
    lines.append(f"- Total cost: ${aggregate['total_cost_usd']}")
    lines.append(f"- Per-vendor responses: {aggregate['ok_by_vendor']}")
    lines.append(f"- Per-vendor refusals: {aggregate['refusals_by_vendor']}")
    lines.append(f"- Per-vendor empties (other): {aggregate['empties_by_vendor']}")
    lines.append("")
    lines.append("## Pairwise mean agreement rate (across all prompts with claim coding)\n")
    lines.append("| Vendor A | Vendor B | n_prompts | mean agreement |")
    lines.append("|---|---|---|---|")
    for pair_key, m in aggregate["pairwise_means"].items():
        a, b = pair_key.split("_vs_")
        rate_str = f"{m['mean_agreement_rate']:.1%}" if m["mean_agreement_rate"] is not None else "n/a"
        lines.append(f"| {a} | {b} | {m['n_prompts']} | {rate_str} |")
    lines.append("")
    lines.append("## By task type\n")
    lines.append("| Task type | n data points | mean agreement | min | max |")
    lines.append("|---|---|---|---|---|")
    for tt, st in aggregate["by_task_type"].items():
        m = f"{st['mean_agreement_rate']:.1%}" if st["mean_agreement_rate"] is not None else "n/a"
        mn = f"{st['min']:.1%}" if st["min"] is not None else "n/a"
        mx = f"{st['max']:.1%}" if st["max"] is not None else "n/a"
        lines.append(f"| {tt} | {st['n_data_points']} | {m} | {mn} | {mx} |")
    lines.append("")
    lines.append("## Per-prompt breakdown\n")
    for pp in per_prompt:
        lines.append(f"### {pp['prompt_id']}  (task: {pp['task_type']})")
        lines.append(f"- Claims loaded: {pp['claims_loaded']}  ({pp['n_claims']} claims)")
        for v in VENDORS:
            r = pp["responses"].get(v, {})
            status = r.get("status", "MISSING")
            cost = r.get("cost_usd", 0)
            lat = r.get("latency_seconds", 0)
            chars = r.get("body_chars", 0)
            lines.append(f"  - {v}: status={status}, cost=${cost:.4f}, latency={lat:.1f}s, body_chars={chars}")
        if pp["agreement"]:
            for pair_key, stat in pp["agreement"].items():
                r = stat["agreement_rate"]
                r_str = f"{r:.1%}" if r is not None else "n/a"
                lines.append(f"  - {pair_key}: agreement={r_str}  (agree={stat['n_agree_substantive']}, disagree={stat['n_substantive_disagreement']}, refusals={stat['n_refusal_involved']})")
        lines.append("")
    (OUTPUTS_DIR / "summary.md").write_text("\n".join(lines))
    print(f"wrote {OUTPUTS_DIR/'agreement-matrix.json'}")
    print(f"wrote {OUTPUTS_DIR/'summary.md'}")
    print(f"Total cost: ${aggregate['total_cost_usd']}")


if __name__ == "__main__":
    main()
