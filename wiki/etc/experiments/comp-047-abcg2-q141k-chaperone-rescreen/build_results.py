#!/usr/bin/env python3
"""
comp-047 final merge + report.

Merges Axis 1 (docking, outputs/results.json) with Axis 2 (empirical ChEMBL
ABCG2 activity, outputs/chembl_axis2.json if present) and the curated control
role tags, then writes:
  outputs/results.json     (re-annotated with axis2 fields + final verdict)
  outputs/controls.md      (control performance — the key validity check)
  outputs/summary.md       (verdict + ranked shortlist + honest limits)

A molecule is a wet-lab CANDIDATE only if it passes BOTH axes:
  Axis 1: fold-selective docking (tier yes/uncertain, not ATP-site-preferring)
  Axis 2: NOT a known/empirical ABCG2 inhibitor or substrate
"""
import json
from pathlib import Path
from datetime import date
from statistics import median

HERE = Path("wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen")


def load_axis2():
    f = HERE / "outputs/chembl_axis2.json"
    if f.exists():
        return json.load(open(f))
    return {}


def fmt(v):
    return f"{v:.2f}" if isinstance(v, (int, float)) else "n/a"


def main():
    res = json.load(open(HERE / "outputs/results.json"))
    meta = res["_meta"]
    R = res["results"]
    axis2 = load_axis2()

    # merge axis2 empirical flags
    for name, row in R.items():
        a2 = axis2.get(name, {})
        row["chembl_abcg2_empirical"] = a2.get("has_activity")  # True/False/None(unqueried)
        row["chembl_best_pchembl"] = a2.get("best_pchembl")
        row["chembl_note"] = a2.get("note")
        # final known-inhibitor = curated OR empirical
        known = bool(row.get("known_inhibitor_flag")) or (a2.get("has_activity") is True)
        row["final_known_abcg2"] = known
        # final verdict: candidate requires fold-selective tier AND not known ABCG2
        tier = row.get("chaperone_tier")
        if tier in ("yes", "uncertain") and not known:
            row["wetlab_candidate"] = tier  # 'yes' or 'uncertain'
        else:
            row["wetlab_candidate"] = "no"

    # ranked shortlist: candidates first (yes>uncertain), by fold_q141k affinity
    def sortkey(kv):
        n, r = kv
        rank_tier = {"yes": 0, "uncertain": 1, "no": 2}[r.get("wetlab_candidate", "no")]
        fq = r.get("fold_q141k_affinity")
        return (rank_tier, fq if isinstance(fq, (int, float)) else 0)

    ordered = sorted(R.items(), key=sortkey)
    candidates = [(n, r) for n, r in ordered if r.get("wetlab_candidate") in ("yes", "uncertain")]

    # re-save annotated results
    json.dump(res, open(HERE / "outputs/results.json", "w"), indent=2)

    # ---- controls.md ----
    cftr = [(n, r) for n, r in R.items() if r.get("role_tag") == "cftr_corrector"]
    inh = [(n, r) for n, r in R.items() if r.get("role_tag") == "abcg2_inhibitor"]
    # overall docking rank (by fold_q141k) for context
    valid = [(n, r) for n, r in R.items() if isinstance(r.get("fold_q141k_affinity"), (int, float))]
    fold_rank = {n: i + 1 for i, (n, r) in enumerate(
        sorted(valid, key=lambda kv: kv[1]["fold_q141k_affinity"]))}
    N = len(valid)

    lines = ["# comp-047 — Control performance (validity check)", "",
             f"Generated {date.today().isoformat()}. N={N} molecules with valid docking.",
             "",
             "Columns: fold@Q141K / fold@WT / transport (Walker A) affinities (kcal/mol, "
             "more negative = stronger); margin = transport − fold@Q141K (>0 = fold-selective); "
             "fold-rank = rank of fold@Q141K among all molecules (1 = strongest fold binder).",
             ""]

    lines.append("## POSITIVE controls — CFTR correctors (must EARN rank, no prior)")
    lines.append("")
    lines.append("| molecule | fold@Q141K | fold@WT | transport | margin | fold-rank | chaperone tier | wetlab candidate |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for n, r in sorted(cftr, key=lambda kv: fold_rank.get(kv[0], 999)):
        lines.append(f"| {n} | {fmt(r.get('fold_q141k_affinity'))} | {fmt(r.get('fold_wt_affinity'))} "
                     f"| {fmt(r.get('transport_affinity'))} | {fmt(r.get('fold_vs_transport_margin'))} "
                     f"| {fold_rank.get(n,'?')}/{N} | {r.get('chaperone_tier')} | {r.get('wetlab_candidate')} |")
    lines.append("")

    lines.append("## NEGATIVE controls — known/empirical ABCG2 inhibitors & substrates (must NOT rank as chaperone)")
    lines.append("")
    lines.append("| molecule | fold@Q141K | transport | margin | fold-rank | chaperone tier | ChEMBL ABCG2 | wetlab candidate |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for n, r in sorted(inh, key=lambda kv: fold_rank.get(kv[0], 999)):
        a2 = "yes" if r.get("chembl_abcg2_empirical") is True else (
            "no" if r.get("chembl_abcg2_empirical") is False else "curated")
        lines.append(f"| {n} | {fmt(r.get('fold_q141k_affinity'))} | {fmt(r.get('transport_affinity'))} "
                     f"| {fmt(r.get('fold_vs_transport_margin'))} | {fold_rank.get(n,'?')}/{N} "
                     f"| {r.get('chaperone_tier')} | {a2} | {r.get('wetlab_candidate')} |")
    lines.append("")

    # validity summary
    inh_top = [n for n, r in inh if r.get("wetlab_candidate") in ("yes", "uncertain")]
    cftr_cand = [n for n, r in cftr if r.get("wetlab_candidate") in ("yes", "uncertain")]
    lines.append("## Validity read-out")
    lines.append("")
    lines.append(f"- Known ABCG2 inhibitors/substrates ranked as chaperone candidates: "
                 f"**{len(inh_top)}** ({inh_top if inh_top else 'none'}). "
                 f"{'PASS — screen correctly rejects inhibitors.' if not inh_top else 'FAIL/PARTIAL — method still confounded; see summary.'}")
    lines.append(f"- CFTR correctors that EARNED a candidate tier from docking: "
                 f"**{len(cftr_cand)}** ({cftr_cand if cftr_cand else 'none'}).")
    (HERE / "outputs/controls.md").write_text("\n".join(lines) + "\n")

    # ---- summary.md ----
    n_yes = sum(1 for n, r in R.items() if r.get("wetlab_candidate") == "yes")
    n_unc = sum(1 for n, r in R.items() if r.get("wetlab_candidate") == "uncertain")
    if n_yes >= 1:
        verdict = "DEFENSIBLE SHORTLIST for wet-lab Q141K trafficking assay"
    elif n_unc >= 1:
        verdict = "INCONCLUSIVE — only weak/uncertain candidates; no high-confidence fold-selective hit"
    else:
        verdict = "NO CREDIBLE CANDIDATES — no molecule is both fold-selective and free of ABCG2 activity"

    s = [f"# comp-047 — Summary", "",
         f"**Generated:** {date.today().isoformat()}  ",
         f"**Method:** AutoDock Vina docking (2 sites × WT/Q141K) + empirical ChEMBL ABCG2 grounding. "
         f"Supersedes comp-032's descriptor/class-prior heuristic.  ",
         f"**Vina:** seed {meta['seed']}, exhaustiveness {meta['exhaustiveness']}, cpu {meta['cpu']}. "
         f"N={len([1 for r in R.values() if isinstance(r.get('fold_q141k_affinity'),(int,float))])} docked.",
         "",
         f"## VERDICT: {verdict}",
         "",
         f"Candidates (fold-selective AND not known ABCG2): **{n_yes} yes**, **{n_unc} uncertain**.",
         "",
         "## Ranked shortlist (candidates only)",
         "",
         "| rank | molecule | drug_class | fold@Q141K | transport | margin | Q141K−WT sel. | ChEMBL ABCG2 | tier |",
         "|---|---|---|---|---|---|---|---|---|"]
    for i, (n, r) in enumerate(candidates[:15], 1):
        a2 = "yes" if r.get("chembl_abcg2_empirical") is True else (
            "no" if r.get("chembl_abcg2_empirical") is False else "unq")
        s.append(f"| {i} | {n} | {r.get('drug_class','')} | {fmt(r.get('fold_q141k_affinity'))} "
                 f"| {fmt(r.get('transport_affinity'))} | {fmt(r.get('fold_vs_transport_margin'))} "
                 f"| {fmt(r.get('q141k_vs_wt_selectivity'))} | {a2} | {r.get('wetlab_candidate')} |")
    if not candidates:
        s.append("| — | (none) | | | | | | | |")
    # ---- Axis 1a raw fold-site ranking (box-choice-robust view) ----
    # Reported ALONGSIDE the tiered verdict so the shortlist is not hostage to the
    # transport-box / margin filter. Shows the strongest fold@Q141K binders with
    # their Axis-2 flag, regardless of margin.
    fold_sorted = sorted(valid, key=lambda kv: kv[1]["fold_q141k_affinity"])
    s += ["",
          "## Raw fold-site ranking (Axis 1a alone — box-choice-robust view)",
          "",
          "Top fold@Q141K binders regardless of transport margin. Use with Axis 2: a strong "
          "fold binder that is a known ABCG2 inhibitor is still disqualified. This table exists "
          "so the shortlist is not hostage to the transport-box choice (see distribution note below).",
          "",
          "| rank | molecule | drug_class | fold@Q141K | transport | margin | known ABCG2? |",
          "|---|---|---|---|---|---|---|"]
    for i, (n, r) in enumerate(fold_sorted[:15], 1):
        s.append(f"| {i} | {n} | {r.get('drug_class','')} | {fmt(r.get('fold_q141k_affinity'))} "
                 f"| {fmt(r.get('transport_affinity'))} | {fmt(r.get('fold_vs_transport_margin'))} "
                 f"| {'yes' if r.get('final_known_abcg2') else 'no'} |")

    # transport-box distribution diagnostic
    tvals = [r["transport_affinity"] for n, r in valid if isinstance(r.get("transport_affinity"), (int, float))]
    fvals = [r["fold_q141k_affinity"] for n, r in valid]
    if tvals:
        s += ["",
              f"**Transport-box distribution diagnostic:** transport affinities span "
              f"{min(tvals):.2f}..{max(tvals):.2f} (median {median(tvals):.2f}); "
              f"fold@Q141K span {min(fvals):.2f}..{max(fvals):.2f} (median {median(fvals):.2f}). "
              f"If the transport (Walker A, apo-monomer) box binds most molecules as strongly as the "
              f"fold box, the margin filter is over-permissive and the verdict should lean on fold-site "
              f"absolute affinity + Axis 2, not margin. See interpretation in controls.md."]

    s += ["",
          "Margin = transport − fold@Q141K (>0 = prefers fold site over ATP site). ",
          "Q141K−WT sel. = fold@WT − fold@Q141K (>0 = binds mutant better than WT — weak chaperone-selectivity proxy). ",
          "See `controls.md` for the validity check and `../README.md` for limitations.",
          "",
          "## Honest limitations (see README for full list)",
          "- **Q141K is a static side-chain substitution**, not a folding-ΔΔG calculation. Docking to a "
          "static modeled mutant is a proxy for a fold-stabilizing interaction, not evidence of folding rescue.",
          "- **Misfolded-state selectivity not modeled** — a true chaperone preferentially stabilizes the "
          "mutant folding intermediate; the WT/Q141K docking delta is a weak surrogate.",
          "- **Apo monomer** — the physiological ATP-bound NBD dimer is not represented; the transport box is "
          "the Walker A P-loop only and tests ATP-competitive binding, NOT the TMD drug/urate cavity where most "
          "clinical ABCG2 inhibitors act. Axis 2 (ChEMBL) is the real inhibitor filter.",
          "- **Vina scores are noisy** (~±1 kcal/mol); use ranks, not absolute affinities. See sensitivity.json."]
    (HERE / "outputs/summary.md").write_text("\n".join(s) + "\n")

    print(f"verdict: {verdict}")
    print(f"candidates: {n_yes} yes, {n_unc} uncertain")
    print(f"neg-control inhibitors ranked as candidates: {inh_top}")
    print(f"cftr correctors earning candidate tier: {cftr_cand}")
    print("wrote outputs/results.json, controls.md, summary.md")


if __name__ == "__main__":
    main()
