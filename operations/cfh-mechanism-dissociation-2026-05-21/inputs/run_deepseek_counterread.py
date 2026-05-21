#!/usr/bin/env python3
"""
comp-039 Model B counter-read driver — DeepSeek (Chinese-vendor) independent
reading of the same primary sources Model A (Claude) read.

Per the comp-039 brief, Brian (Claude subscription) is Model A. OpenRouter is
invoked ONLY for Model B — a native-Chinese counterread for the Chinese-source
papers (Tian 2014 Houttuynia, Lu 2018 CHCP, Yin 2016 Helicteres, Zhang 2008
luteolin) and a parallel reading for the Western-source rosmarinic acid
papers (Sahu 1999, Englberger 1988, Peake 1991).

The Model B counterread is asked to read the SAME primary sources Model A
read and produce its own CFH-dependence classification. The point is
independent interpretation, not translation — these papers are English-
language. The DeepSeek choice is for the native-Chinese training-depth
advantage on the Chen Daofeng / Fudan / Tian / Yin / Houttuynia subfield.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIB = HERE.parent.parent.parent / "wiki" / "etc" / "experiments" / "lib"
sys.path.insert(0, str(LIB))

from agentic_lit_synthesis import (  # noqa: E402
    load_root_dotenv,
    utc_now_iso,
    write_json,
)


def openrouter_chat_via_curl(api_key, model, messages, temperature=0.1, max_tokens=2000, app_title="Open Enzyme comp-039"):
    """OpenRouter chat via curl - bypasses Python 3.13 cert-bundle issue."""
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    cmd = [
        "curl",
        "--silent",
        "--show-error",
        "--fail",
        "--max-time",
        "240",
        "-H",
        f"Authorization: Bearer {api_key}",
        "-H",
        "Content-Type: application/json",
        "-H",
        "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
        "-H",
        f"X-Title: {app_title}",
        "-d",
        json.dumps(payload),
        "https://openrouter.ai/api/v1/chat/completions",
    ]
    completed = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(f"curl OpenRouter failed: {completed.stderr.strip()}\n{completed.stdout[:500]}")
    data = json.loads(completed.stdout)
    if "choices" not in data:
        raise RuntimeError(f"OpenRouter response missing choices: {data}")
    choice = data["choices"][0]
    message = choice.get("message", {})
    return {
        "model": data.get("model", model),
        "response_id": data.get("id"),
        "created": data.get("created"),
        "text": message.get("content", ""),
        "raw": data,
    }


OUT = HERE.parent / "outputs"


# Source-document text the Model B counterread should reason over.
# These are the verified-from-paper key facts in compact form; the
# counterread is independent reasoning, not translation.

SOURCE_BUNDLE = {
    "rosmarinic_acid": """
Primary sources read:

(1) Sahu A, Rawal N, Pangburn MK. Inhibition of complement by covalent attachment of rosmarinic acid to activated C3b. Biochem Pharmacol 1999;57(12):1439-46. PMID 10353266.
Key abstract claim (verbatim): "reaction of rosmarinic acid with the activated thioester of metastable C3b, resulting in covalent attachment of the inhibitor to the protein." Radioiodination demonstrates covalent incorporation into the thioester-containing alpha'-chain of nascent C3b. IC50 for inhibiting covalent attachment of C3b to cells = 34 microM. Factor H is NOT mentioned in this paper.

(2) Englberger W et al. Rosmarinic acid: a new inhibitor of complement C3-convertase. Int J Immunopharmacol 1988;10(6):729-37. PMID 3198307.
Target: "C3-convertase of the classical complement pathway". Threshold inhibition 1 microM; optimal 5-10 microM (about 70% hemolysis inhibition). Elastase (another serine protease) also weakly inhibited - suggests proteinase active-site interaction. Factor H NOT mentioned.

(3) Peake PW et al. The inhibitory effect of rosmarinic acid on complement involves the C5 convertase. Int J Immunopharmacol 1991;13(7):853-7. PMID 1761351.
Higher-dose mechanism (mM range) involves C5 convertase. Maximum CP lysis inhibition at 2.6 mM. Factor H NOT mentioned.

Structural context: CFH Y402 sits in Sushi/CCP 7 (residues 387-444, UniProt P08603 verified). CCP6-8 is the canonical CRP-binding + host-GAG-binding surface. CFH regulates surface-deposited C3b (decay-acceleration of C3bBb + Factor-I cofactor for C3b -> iC3b cleavage). All these CFH functions act DOWNSTREAM of the C3b thioester reaction that rosmarinic acid covalently quenches.

Question: Does rosmarinic acid's anti-complement mechanism require functional CFH? Classify as CFH-dependent, CFH-independent, or mixed. Predict Y402H carrier interaction direction (+ harm, - protection, 0 null) for incident gout. Justify with binding-site evidence. Identify any disagreements you would have with a Model A read that classifies this as CFH-INDEPENDENT high-confidence.
""",
    "luteolin": """
Primary sources read:

(1) Zhang T, Chen DF. Anticomplementary principles of a Chinese multiherb remedy for the treatment and prevention of SARS. J Ethnopharmacol 2008;117(2):351-61. PMID 18400428 / PMC7126446. Full text read.
Key results: luteolin tested in matched sheep-erythrocyte (CP, guinea pig serum) and rabbit-erythrocyte (AP, 1:10 NHS) hemolytic assay. "luteolin was found to have most strong anticomplementary activity with CH50 value of 0.19 mM. ... AP50 values of less than 1 mM [actually 0.17 mM]." Mechanism attribution: 4'-OH on flavonoid B-ring is essential for activity. Paper does NOT identify a specific complement-cascade target for luteolin. CFH / Factor H not mentioned.

(2) Pieroni A et al. In vitro anti-complementary activity of flavonoids from olive (Olea europaea L.) leaves. Farmaco 1996;51(11):765-8. PMID 8941947. Class-level convergence.

Additional context: luteolin is documented elsewhere (comp-013) to be XO IC50 = 550 nM and downregulates URAT1 expression - it has multiple gout-relevant modes beyond complement.

Structural context: CFH Y402 sits in Sushi/CCP 7 (residues 387-444 of P08603). CCP6-8 is the canonical CRP-binding + host-GAG-binding surface. The AMD-paradox mechanism (AREDS-zinc + DHA) operates via zinc-induced complement inactivation that requires CFH-CRP-bridging which Y402H performs poorly.

Question: Does luteolin's anti-complement mechanism require functional CFH? Classify as CFH-dependent / CFH-independent / mixed. Predict Y402H carrier interaction direction (+/-/0) for incident gout. Justify with binding-site evidence. Identify any disagreements with a Model A read that classifies this as CFH-INDEPENDENT (Medium confidence due to mechanism site ambiguity).
""",
    "houttuynia_cordata_polysaccharide": """
Primary sources read:

(1) Tian L et al. Anti-complementary constituents of Houttuynia cordata and their targets in complement activation cascade. J Ethnopharmacol 2014. PMID 24423008.
Abstract claim: "the glycoside moieties may be necessary to block C3 and C4 components."

(2) Lu Y et al. Beneficial effects of Houttuynia cordata polysaccharides on "two-hit" acute lung injury and endotoxic fever in rats associated with anti-complementary activities. Acta Pharm Sin B 2018;8(2):218-227. PMID 29719782 / PMC5925397. Full text read.
Polysaccharide fraction = CHCP. Complement-depleted-sera mapping verbatim: "C2-depleted and C9-depleted sera also restored the hemolysis markedly (72.82±10.61% for C2 and 63.21±2.27% for C9). However, CHCP nearly abolished the hemolysis when C3- or C4-depleted serum was added (9.29±1.69% for C3, 12.34±1.39% for C4). For C5, the hemolysis was only partly restored (44.54±3.92%). These results suggested that CHCP mainly block C3 and C4, and may interact with C5."

(3) Xu YY et al. Houttuynia cordata Thunb. polysaccharides ameliorates lipopolysaccharide-induced acute lung injury in mice. J Ethnopharmacol 2015;173:81-90. PMID 26190353 / PMC7127486. Full text read.
HCP at 40, 80, 160 mg/kg PO reduced C3d deposition in lung tissue (immunohistochemistry), reduced TLR4 expression, suppressed C5a-induced macrophage chemotaxis, reduced NLRP3-axis cytokines (IL-1beta, TNF-alpha, IL-6). Multi-target: complement + TLR4 + NLRP3 axis.

(4) Yu 2026 PMC12937656 reports computational TLR4-MD2 docking model (orthogonal CP1 mechanism).
(5) Cheng 2014 HCP-1 paper reports structure-dependent caveat (within-class polysaccharide heterogeneity).

CFH / Factor H is NOT mentioned in any of these primary sources.

Structural context: CFH Y402 sits in Sushi/CCP 7 (residues 387-444, P08603). CFH is alternative-pathway-specific (decay-acceleration of C3bBb + Factor-I cofactor for C3b -> iC3b). CFH does NOT regulate C4 (which is classical-pathway-only). Pectic polysaccharide binding mode is adsorptive surface contact, structurally distinct from CFH's CCP-fold protein recognition.

Question: Does HCP / CHCP's anti-complement mechanism require functional CFH? Classify as CFH-dependent / CFH-independent / mixed. Predict Y402H carrier interaction direction (+/-/0) for incident gout. Justify with binding-target evidence. Identify any disagreements with a Model A read that classifies this as CFH-INDEPENDENT (High confidence).
""",
    "helicteres_benzofuran_lignans": """
Primary source read:

(1) Yin X, Lu Y, Cheng ZH, Chen DF. Anti-Complementary Components of Helicteres angustifolia. Molecules 2016;21(11):1506. PMID 27834928 / PMC6273495. Full text read.

Depletion-rescue target identification (verbatim): "compound [4] regained the hemolytic capacity of C5-depleted serum, and compound [5] regained the hemolytic capacity of C4- and C5-depleted sera. These findings suggested that compound [4 = machicendonal] probably acted on C1q, C2, C3, C4 and C9, while compound [5 = dihydrodehydrodiconiferyl alcohol] interacted with the C1q, C2, C3 and C9 components of the complement."

CH50 values verified: Compound 4 (machicendonal) CH50 = 0.040 ± 0.009 mM (40 μM), AP50 = 0.105 ± 0.015 mM (105 μM). Compound 5 (dihydrodehydrodiconiferyl alcohol) CH50 = 0.009 ± 0.002 mM (9 μM), AP50 = 0.021 ± 0.003 mM (21 μM).

CFH / Factor H NOT mentioned anywhere in the paper.

Replication status: comp-018 Phase 2 (2026-05-17) verdict = INCONCLUSIVE. No independent group has reproduced Yin 2016 CH50 9/40 μM benzofuran lignan finding on a matched assay format. Structurally-adjacent benzofuran lignans (Styrax japonica egonol, Min 2004 PMID 15643559) are 3.7× weaker.

Structural context: CFH Y402 sits in Sushi/CCP 7 (residues 387-444, P08603). CFH does NOT regulate C1q, C2, C4, or C9 (CFH is AP-specific, acting on C3b and the C3bBb convertase). Multi-target lignan pattern (C1q + C2 + C3 + C4/C9) is structurally orthogonal to CFH's CCP6-8 binding surface.

Question: Does Helicteres benzofuran lignan anti-complement mechanism require functional CFH? Classify as CFH-dependent / CFH-independent / mixed. Predict Y402H carrier interaction direction (+/-/0) for incident gout. Justify with binding-target evidence. Identify any disagreements with a Model A read that classifies this as CFH-INDEPENDENT (Medium confidence due to single-anchor replication risk, NOT due to mechanism uncertainty).
""",
}


def main():
    load_root_dotenv(HERE)
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set in env or .env")
    model_b = "deepseek/deepseek-chat"

    system = (
        "You are Model B (DeepSeek, Chinese-vendor native-Chinese-trained "
        "scientific model) in a two-model independent cross-check protocol "
        "for Open Enzyme (open-source biotech research). You will be given a "
        "compact bundle of primary-source facts (already extracted by Model A "
        "from the literature) and asked to independently classify a compound's "
        "CFH-dependence (CFH-dependent / CFH-independent / mixed), predict its "
        "Y402H × incident-gout interaction direction, and identify disagreements "
        "with a stated Model A classification. Be rigorous, evidence-grounded, "
        "and explicit about confidence and uncertainty. Use the binding-site / "
        "target-identification evidence as the load-bearing input. Where you "
        "disagree with Model A, say so clearly with the mechanistic reason."
    )

    instruction = (
        "Return JSON ONLY (no prose preamble) with this exact schema:\n"
        "{\n"
        '  "classification": "CFH-dependent" | "CFH-independent" | "mixed",\n'
        '  "confidence": "High" | "Medium" | "Low",\n'
        '  "predicted_y402h_direction": "negative (protective greater in carriers)" | '
        '"positive (carriers do worse - AMD paradox transfers)" | "null" | "uncertain",\n'
        '  "key_binding_site_evidence": "...",\n'
        '  "agreement_with_model_a": "agree" | "disagree" | "partial",\n'
        '  "disagreements": ["..."],\n'
        '  "load_bearing_uncertainties": ["..."],\n'
        '  "recommended_falsification_test": "..."\n'
        "}"
    )

    for candidate, source_text in SOURCE_BUNDLE.items():
        print(f"--- {candidate}: invoking Model B (DeepSeek) ---")
        prompt = source_text + "\n\n" + instruction
        response = openrouter_chat_via_curl(
            api_key,
            model_b,
            [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
            max_tokens=2000,
        )
        artifact = {
            "candidate": candidate,
            "role": "native_chinese_counter_read_model_b",
            "model_requested": model_b,
            "model_returned": response["model"],
            "response_id": response["response_id"],
            "created_at_utc": utc_now_iso(),
            "text": response["text"],
            "raw_usage": response["raw"].get("usage"),
        }
        out = OUT / f"{candidate}-deepseek-counterread-2026-05-21.json"
        write_json(out, artifact)
        print(f"  wrote: {out}")
        print(f"  usage: {artifact['raw_usage']}")


if __name__ == "__main__":
    main()
