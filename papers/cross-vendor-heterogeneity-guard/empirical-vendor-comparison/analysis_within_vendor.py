#!/usr/bin/env python3
"""
analysis_within_vendor.py — compute within-vendor pairwise agreement across
replicates for the intra-vendor variance study.

Reads:
  outputs/claims/<prompt-id>.json        (r1, original)
  outputs/claims/<prompt-id>-r2.json     (r2)
  outputs/claims/<prompt-id>-r3.json     (r3)

For each (prompt, vendor) cell, computes within-vendor pairwise agreement
across the 3 replicates (3 pairs: r1-r2, r1-r3, r2-r3). Aggregates by:
  - per (vendor) cell across all prompts
  - per task type across all (prompt, vendor) cells
  - headline (overall mean across all cells)

Writes:
  outputs/within-vendor-matrix.json
  outputs/within-vendor-summary.md
"""

import collections
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
PROMPTS_DIR = HERE / "prompts"
CLAIMS_DIR = HERE / "outputs" / "claims"
OUTPUTS_DIR = HERE / "outputs"
VENDORS = ["deepseek", "gemini", "openai", "anthropic"]
REPLICATES = [1, 2, 3]


def load_claims(prompt_id, replicate):
    if replicate == 1:
        p = CLAIMS_DIR / f"{prompt_id}.json"
    else:
        p = CLAIMS_DIR / f"{prompt_id}-r{replicate}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text())


def verdicts_for_vendor(claim, vendor):
    v = claim["verdicts"].get(vendor, {})
    return (v.get("verdict", "ignore"), (v.get("alternative", "") or "").strip())


def pair_agree(va_v, va_a, vb_v, vb_a):
    """Return outcome label using same semantics as cross-vendor analysis.py."""
    if va_v == "refusal" or vb_v == "refusal":
        if va_v == vb_v:
            return "agree-both-refused"
        return "skip-refusal-asymmetric"
    if va_v == "ignore" and vb_v == "ignore":
        return "skip-both-ignored"
    if va_v == "ignore" or vb_v == "ignore":
        return "skip-one-ignored"
    if va_v == vb_v:
        if va_v == "disagree":
            if va_a and va_a == vb_a:
                return "agree"
            return "disagree"
        return "agree"
    return "disagree"


def main():
    prompts = sorted(p.stem for p in PROMPTS_DIR.glob("*.md"))

    claims_by_prompt = {}
    for pid in prompts:
        claims_by_prompt[pid] = {}
        for r in REPLICATES:
            c = load_claims(pid, r)
            if c is not None:
                claims_by_prompt[pid][r] = c

    per_cell = []

    for pid in prompts:
        cs = claims_by_prompt[pid]
        if 1 not in cs:
            continue
        task_type = cs[1].get("task_type", "unknown")
        claim_ids = [c["id"] for c in cs[1]["claims"]]

        for vendor in VENDORS:
            available = [r for r in REPLICATES if r in cs]
            if len(available) < 2:
                continue

            pair_stats = {}
            for i, ra in enumerate(available):
                for rb in available[i+1:]:
                    n_agree = 0
                    n_disagree = 0
                    n_skip = 0
                    n_refusal_asymm = 0
                    n_both_refused = 0
                    per_claim_outcomes = []
                    pending = False
                    for cid in claim_ids:
                        ca = next((c for c in cs[ra]["claims"] if c["id"] == cid), None)
                        cb = next((c for c in cs[rb]["claims"] if c["id"] == cid), None)
                        if ca is None or cb is None:
                            per_claim_outcomes.append((cid, "skip-missing-claim"))
                            n_skip += 1
                            continue
                        va_v, va_a = verdicts_for_vendor(ca, vendor)
                        vb_v, vb_a = verdicts_for_vendor(cb, vendor)
                        if va_v == "PENDING" or vb_v == "PENDING":
                            per_claim_outcomes.append((cid, "pending"))
                            pending = True
                            continue
                        out = pair_agree(va_v, va_a, vb_v, vb_a)
                        per_claim_outcomes.append((cid, out))
                        if out == "agree":
                            n_agree += 1
                        elif out == "agree-both-refused":
                            n_agree += 1
                            n_both_refused += 1
                        elif out == "disagree":
                            n_disagree += 1
                        elif out == "skip-refusal-asymmetric":
                            n_refusal_asymm += 1
                        else:
                            n_skip += 1
                    if pending:
                        # skip this pair if any claim still pending
                        continue
                    denom = n_agree + n_disagree
                    rate = (n_agree / denom) if denom else None
                    pair_stats[f"r{ra}_vs_r{rb}"] = {
                        "n_agree": n_agree,
                        "n_disagree": n_disagree,
                        "n_skip": n_skip,
                        "n_refusal_asymm": n_refusal_asymm,
                        "n_both_refused": n_both_refused,
                        "agreement_rate": rate,
                        "per_claim": per_claim_outcomes,
                    }
            rates = [v["agreement_rate"] for v in pair_stats.values() if v["agreement_rate"] is not None]
            cell_rate = sum(rates) / len(rates) if rates else None
            per_cell.append({
                "prompt_id": pid,
                "vendor": vendor,
                "task_type": task_type,
                "available_replicates": available,
                "pair_stats": pair_stats,
                "cell_mean_agreement_rate": cell_rate,
                "n_pairs_with_data": len(rates),
            })

    cell_rates = [c["cell_mean_agreement_rate"] for c in per_cell if c["cell_mean_agreement_rate"] is not None]
    headline = sum(cell_rates) / len(cell_rates) if cell_rates else None

    by_vendor = collections.defaultdict(list)
    for c in per_cell:
        if c["cell_mean_agreement_rate"] is not None:
            by_vendor[c["vendor"]].append(c["cell_mean_agreement_rate"])
    by_vendor_means = {v: (round(sum(rs)/len(rs), 3) if rs else None) for v, rs in by_vendor.items()}

    by_task = collections.defaultdict(list)
    for c in per_cell:
        if c["cell_mean_agreement_rate"] is not None:
            by_task[c["task_type"]].append(c["cell_mean_agreement_rate"])
    by_task_means = {t: round(sum(rs)/len(rs), 3) for t, rs in by_task.items()}

    cross_vendor = None
    cvm_path = OUTPUTS_DIR / "agreement-matrix.json"
    if cvm_path.exists():
        cross_vendor = json.loads(cvm_path.read_text())

    # Cross-vendor by vendor: mean of all pairs that include this vendor
    cross_by_vendor = {v: [] for v in VENDORS}
    cross_by_task = collections.defaultdict(list)
    cross_headline_rates = []
    if cross_vendor is not None:
        for pp in cross_vendor.get("per_prompt", []):
            tt = pp.get("task_type", "unknown")
            ag = pp.get("agreement") or {}
            for k, st in ag.items():
                r = st.get("agreement_rate")
                if r is None:
                    continue
                cross_headline_rates.append(r)
                cross_by_task[tt].append(r)
                a, b = k.split("_vs_")
                cross_by_vendor[a].append(r)
                cross_by_vendor[b].append(r)
    cross_headline = (sum(cross_headline_rates)/len(cross_headline_rates)) if cross_headline_rates else None
    cross_by_vendor_means = {v: (round(sum(rs)/len(rs), 3) if rs else None) for v, rs in cross_by_vendor.items()}
    cross_by_task_means = {t: round(sum(rs)/len(rs), 3) for t, rs in cross_by_task.items()}

    out = {
        "headline_within_vendor_agreement_rate": round(headline, 3) if headline is not None else None,
        "headline_cross_vendor_agreement_rate": round(cross_headline, 3) if cross_headline is not None else None,
        "by_vendor_within": by_vendor_means,
        "by_vendor_cross": cross_by_vendor_means,
        "by_task_type_within": by_task_means,
        "by_task_type_cross": cross_by_task_means,
        "n_cells_with_data": len(cell_rates),
        "per_cell": per_cell,
        "vendors": VENDORS,
        "replicates": REPLICATES,
    }
    (OUTPUTS_DIR / "within-vendor-matrix.json").write_text(json.dumps(out, indent=2, default=str))

    lines = []
    lines.append("# Within-vendor agreement summary")
    lines.append("")
    lines.append(f"- Vendors: {', '.join(VENDORS)}")
    lines.append(f"- Replicates configured: {REPLICATES}")
    lines.append(f"- Cells with at least 2 codable replicates: {len(cell_rates)}")
    if headline is not None:
        lines.append(f"- **Headline within-vendor mean agreement rate: {headline:.1%}**")
    if cross_headline is not None:
        lines.append(f"- Headline cross-vendor mean agreement rate (pilot, for comparison): {cross_headline:.1%}")
        lines.append(f"- Within-vendor minus cross-vendor: {(headline - cross_headline):+.1%}")
        # Partition statement
        cross_disagree = 1 - cross_headline
        within_disagree = 1 - headline
        cross_signal = cross_disagree - within_disagree
        lines.append(f"")
        lines.append(f"## Partition of cross-vendor disagreement")
        lines.append(f"- Cross-vendor disagreement rate: {cross_disagree:.1%}")
        lines.append(f"- Within-vendor disagreement rate (temperature noise): {within_disagree:.1%}")
        lines.append(f"- Residual cross-vendor heterogeneity signal: {cross_signal:.1%} ({cross_signal/cross_disagree:.0%} of total cross-vendor disagreement)")
    lines.append("")
    lines.append("## Per-vendor stability")
    lines.append("")
    lines.append("| Vendor | Within-vendor | Cross-vendor | Delta |")
    lines.append("|---|---|---|---|")
    for v in VENDORS:
        w = by_vendor_means.get(v)
        x = cross_by_vendor_means.get(v)
        delta = (w - x) if (w is not None and x is not None) else None
        w_s = f"{w*100:.1f}%" if w is not None else "n/a"
        x_s = f"{x*100:.1f}%" if x is not None else "n/a"
        d_s = f"{delta*100:+.1f}%" if delta is not None else "n/a"
        lines.append(f"| {v} | {w_s} | {x_s} | {d_s} |")
    lines.append("")
    lines.append("## By task type")
    lines.append("")
    lines.append("| Task type | Within-vendor | Cross-vendor |")
    lines.append("|---|---|---|")
    for tt in sorted(set(list(by_task_means.keys()) + list(cross_by_task_means.keys()))):
        w = by_task_means.get(tt)
        x = cross_by_task_means.get(tt)
        w_s = f"{w*100:.1f}%" if w is not None else "n/a"
        x_s = f"{x*100:.1f}%" if x is not None else "n/a"
        lines.append(f"| {tt} | {w_s} | {x_s} |")
    lines.append("")
    lines.append("## Per-cell breakdown")
    lines.append("")
    lines.append("| Prompt | Vendor | Task type | Cell mean | Pairs |")
    lines.append("|---|---|---|---|---|")
    for c in per_cell:
        rate = c["cell_mean_agreement_rate"]
        rate_s = f"{rate*100:.1f}%" if rate is not None else "n/a"
        pair_str = "; ".join(
            f"{k}={(v['agreement_rate']*100):.0f}%" if v['agreement_rate'] is not None else f"{k}=n/a"
            for k, v in c["pair_stats"].items()
        )
        lines.append(f"| {c['prompt_id']} | {c['vendor']} | {c['task_type']} | {rate_s} | {pair_str} |")
    (OUTPUTS_DIR / "within-vendor-summary.md").write_text("\n".join(lines))
    print(f"wrote {OUTPUTS_DIR/'within-vendor-matrix.json'}")
    print(f"wrote {OUTPUTS_DIR/'within-vendor-summary.md'}")
    if headline is not None:
        print(f"headline within-vendor: {headline:.1%}")
    if cross_headline is not None:
        print(f"headline cross-vendor:  {cross_headline:.1%}")
    print(f"by vendor (within): {by_vendor_means}")
    print(f"by vendor (cross):  {cross_by_vendor_means}")


if __name__ == "__main__":
    main()
