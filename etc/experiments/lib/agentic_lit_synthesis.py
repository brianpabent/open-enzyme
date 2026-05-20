"""
experiments/lib/agentic_lit_synthesis.py

Small stdlib helper layer for agentic literature-synthesis comp-NNN runs.

Secrets stay in the repo-root .env file (gitignored). Experiment folders commit
only non-secret model-role config and run artifacts.
"""

import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
NCBI_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
NCBI_EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
DEFAULT_LOCAL_CURL_ALLOWED_SUFFIXES = (
    ".baidu.com",
    ".cnki.net",
    ".cnki.com.cn",
    ".chinaxiv.org",
    ".wanfangdata.com.cn",
    ".wanfangdata.com",
    ".wanfang.com.cn",
    ".cqvip.com",
    ".sinomed.ac.cn",
    ".chictr.org.cn",
    ".medresman.org",
    ".nstl.gov.cn",
    ".sdyyzz.cn",
    ".jst.go.jp",
    ".nii.ac.jp",
    ".j-global.jst.go.jp",
    ".kci.go.kr",
    ".riss.kr",
    ".dbpia.co.kr",
    ".koreascience.kr",
)


def utc_now_iso():
    """Return a compact UTC timestamp for provenance."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def find_repo_root(start):
    """
    Walk upward from start until a repo marker is found.
    Works from experiment folders and from shared library callers.
    """
    path = Path(start).resolve()
    if path.is_file():
        path = path.parent
    for candidate in [path, *path.parents]:
        if (candidate / ".git").exists() or (candidate / "CLAUDE.md").exists():
            return candidate
    return path


def load_root_dotenv(start):
    """
    Load KEY=VALUE pairs from repo-root .env without overriding shell env.
    No value is printed or returned except via os.environ.
    """
    env_path = find_repo_root(start) / ".env"
    if not env_path.exists():
        return None

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value
    return env_path


def read_json(path):
    with open(path) as f:
        return json.load(f)


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def safe_filename(text, max_len=120):
    """Make a stable filesystem-safe name from a URL or title."""
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("_")
    return (cleaned or "fetch")[:max_len]


LANGUAGE_NATIVE_QUERY_RULES = {
    "zh": {
        "label": "Chinese",
        "sources": ["CNKI", "WanFang", "CQVIP", "SinoMed", "ChiCTR", "NSTL"],
        "required_frames": [
            "mechanism_native",
            "species_original_language",
            "traditional_formula",
            "traditional_pathology",
        ],
        "mechanism_terms": {
            "URAT1": ["URAT1", "尿酸盐转运蛋白1", "尿酸转运体1", "SLC22A12"],
            "ABCG2": ["ABCG2", "乳腺癌耐药蛋白", "尿酸排泄"],
            "XO": ["黄嘌呤氧化酶", "XOD", "XO"],
            "NLRP3": ["NLRP3炎症小体", "NLRP3 炎症小体", "白细胞介素1β"],
            "complement": ["补体", "抗补体", "C3转化酶", "C5a"],
            "butyrate": ["丁酸", "短链脂肪酸", "SCFA"],
            "HDAC": ["组蛋白去乙酰化酶", "HDAC", "HDAC6"],
        },
        "pathology_terms": {
            "gout": ["痛风", "高尿酸血症", "痹证", "湿热痹"],
            "hyperuricemia": ["高尿酸血症", "痛风"],
            "inflammation": ["炎症", "抗炎", "炎症小体"],
            "complement": ["补体激活", "抗补体"],
            "microbiome": ["肠道菌群", "肠道微生物", "代谢物"],
        },
        "example_formulas": ["四妙散", "白虎加桂枝汤", "乌梅丸", "藿香正气"],
    },
    "ja": {
        "label": "Japanese",
        "sources": ["J-STAGE", "CiNii", "J-GLOBAL", "J-RCT"],
        "required_frames": [
            "mechanism_native",
            "species_original_language",
            "traditional_formula",
            "traditional_pathology",
        ],
        "mechanism_terms": {
            "URAT1": ["URAT1", "尿酸トランスポーター", "SLC22A12"],
            "ABCG2": ["ABCG2", "BCRP", "尿酸排泄"],
            "XO": ["キサンチンオキシダーゼ", "キサンチン酸化酵素"],
            "NLRP3": ["NLRP3インフラマソーム", "IL-1β"],
            "complement": ["補体", "抗補体", "C3転換酵素", "C5a"],
            "butyrate": ["酪酸", "短鎖脂肪酸"],
            "HDAC": ["ヒストン脱アセチル化酵素", "HDAC", "HDAC6"],
        },
        "pathology_terms": {
            "gout": ["痛風", "高尿酸血症"],
            "hyperuricemia": ["高尿酸血症", "痛風"],
            "inflammation": ["炎症", "抗炎症"],
            "complement": ["補体活性化", "抗補体"],
            "microbiome": ["腸内細菌叢", "腸内細菌", "代謝物"],
        },
        "example_formulas": ["防風通聖散", "越婢加朮湯", "桂枝茯苓丸"],
    },
    "ko": {
        "label": "Korean",
        "sources": ["KISS", "RISS", "DBpia", "KoreaScience", "KCI"],
        "required_frames": [
            "mechanism_native",
            "species_original_language",
            "traditional_formula",
            "traditional_pathology",
        ],
        "mechanism_terms": {
            "URAT1": ["URAT1", "요산 수송체", "SLC22A12"],
            "ABCG2": ["ABCG2", "BCRP", "요산 배설"],
            "XO": ["잔틴 산화효소", "xanthine oxidase"],
            "NLRP3": ["NLRP3 인플라마좀", "IL-1β"],
            "complement": ["보체", "항보체", "C3 전환효소", "C5a"],
            "butyrate": ["부티르산", "단쇄지방산"],
            "HDAC": ["히스톤 탈아세틸화효소", "HDAC", "HDAC6"],
        },
        "pathology_terms": {
            "gout": ["통풍", "고요산혈증"],
            "hyperuricemia": ["고요산혈증", "통풍"],
            "inflammation": ["염증", "항염증"],
            "complement": ["보체 활성화", "항보체"],
            "microbiome": ["장내미생물", "장내 세균", "대사체"],
        },
        "example_formulas": ["사묘산", "방풍통성산"],
    },
}


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)] if str(value).strip() else []


def _dedupe_keep_order(values):
    seen = set()
    output = []
    for value in values:
        key = value.strip()
        if not key or key in seen:
            continue
        seen.add(key)
        output.append(key)
    return output


def native_terms(language, mechanisms=None, pathologies=None):
    """Return native-language mechanism/pathology terms for a scan."""
    rules = LANGUAGE_NATIVE_QUERY_RULES[language]
    mechanism_terms = []
    for mechanism in _as_list(mechanisms):
        mechanism_terms.extend(rules["mechanism_terms"].get(mechanism, [mechanism]))
    pathology_terms = []
    for pathology in _as_list(pathologies):
        pathology_terms.extend(rules["pathology_terms"].get(pathology, [pathology]))
    return {
        "mechanisms": _dedupe_keep_order(mechanism_terms),
        "pathologies": _dedupe_keep_order(pathology_terms),
    }


def build_language_native_query_plan(
    scope,
    mechanisms=None,
    species=None,
    formulas=None,
    pathologies=None,
    languages=("zh", "ja", "ko"),
    western_queries=None,
    natural_product_scope=True,
    required_frames=None,
):
    """
    Build query framings for non-English lit scans using native-language terms.

    This codifies the 2026-05-19 query-framing discipline:
    mechanism-name-only English queries are insufficient for TCM / Kampo /
    Korean medicine / medicinal-mushroom domains. Search by native mechanism
    term + original-language species/formula/pathology frames.
    """
    framings = []
    if western_queries:
        framings.append({
            "type": "western_mechanism",
            "language": "en",
            "queries": _dedupe_keep_order(_as_list(western_queries)),
            "rationale": "Western/PubMed mechanism-name frame; retained as one frame, not the whole scan.",
        })

    for language in languages:
        rules = LANGUAGE_NATIVE_QUERY_RULES[language]
        terms = native_terms(language, mechanisms=mechanisms, pathologies=pathologies)
        mechanism_terms = terms["mechanisms"] or _as_list(mechanisms)
        pathology_terms = terms["pathologies"] or _as_list(pathologies)

        mechanism_queries = []
        for mechanism in mechanism_terms:
            if pathology_terms:
                mechanism_queries.extend(f"{mechanism} {pathology}" for pathology in pathology_terms)
            else:
                mechanism_queries.append(mechanism)
        framings.append({
            "type": "mechanism_native",
            "language": language,
            "sources": rules["sources"],
            "queries": _dedupe_keep_order(mechanism_queries),
            "rationale": "Native-language mechanism/pathology query; avoids English-only mechanism vocabulary.",
        })

        species_queries = []
        for item in _as_list(species):
            if mechanism_terms:
                species_queries.extend(f"{item} {mechanism}" for mechanism in mechanism_terms[:3])
            if pathology_terms:
                species_queries.extend(f"{item} {pathology}" for pathology in pathology_terms[:3])
            if not mechanism_terms and not pathology_terms:
                species_queries.append(item)
        if species_queries:
            framings.append({
                "type": "species_original_language",
                "language": language,
                "sources": rules["sources"],
                "queries": _dedupe_keep_order(species_queries),
                "rationale": "Species/common-name anchoring catches traditional-name-indexed papers mechanism queries miss.",
            })

        formula_queries = []
        for formula in _as_list(formulas):
            if pathology_terms:
                formula_queries.extend(f"{formula} {pathology}" for pathology in pathology_terms[:4])
            if mechanism_terms:
                formula_queries.extend(f"{formula} {mechanism}" for mechanism in mechanism_terms[:3])
            if not pathology_terms and not mechanism_terms:
                formula_queries.append(formula)
        if formula_queries:
            framings.append({
                "type": "traditional_formula",
                "language": language,
                "sources": rules["sources"],
                "queries": _dedupe_keep_order(formula_queries),
                "rationale": "Formula-name anchoring catches clinical and materia-medica papers not indexed by target mechanism.",
            })

        if pathology_terms:
            framings.append({
                "type": "traditional_pathology",
                "language": language,
                "sources": rules["sources"],
                "queries": _dedupe_keep_order(pathology_terms),
                "rationale": "Original pathology framing catches papers that do not use Western mechanism labels.",
            })

    return {
        "scope": scope,
        "natural_product_scope": natural_product_scope,
        "query_framing_protocol": "mechanism + species_original_language + traditional_formula + traditional_pathology",
        "required_query_frames": _dedupe_keep_order(required_frames or LANGUAGE_NATIVE_QUERY_RULES["zh"]["required_frames"]),
        "created_at_utc": utc_now_iso(),
        "framings": framings,
        "notes": [
            "Do not treat zero hits from English mechanism queries as evidence of absence in non-English corpora.",
            "Fetch firewall-sensitive East Asian sources through local_curl_fetch(), not hosted model/web fetch.",
            "Translate load-bearing non-English source text with translate_source_two_model().",
        ],
    }


def audit_query_strategy_language_framing(query_strategy, languages=("zh", "ja", "ko")):
    """
    Check whether a query-strategy artifact includes native-language frames.

    Returns a machine-readable audit that comp runners can fail on, warn on, or
    commit as provenance. Set natural_product_scope=false in the strategy when
    the rule does not apply.
    """
    if query_strategy.get("natural_product_scope") is False:
        return {
            "verdict": "not_applicable",
            "reason": "query_strategy declares natural_product_scope=false",
            "missing": [],
        }

    framings = query_strategy.get("framings", [])
    framing_types = {framing.get("type") for framing in framings}
    queries_by_language = {language: [] for language in languages}
    for framing in framings:
        language = framing.get("language")
        if language in queries_by_language:
            queries_by_language[language].extend(framing.get("queries", []))

    missing = []
    required_types = set(query_strategy.get(
        "required_query_frames",
        LANGUAGE_NATIVE_QUERY_RULES["zh"]["required_frames"],
    ))
    missing_types = sorted(required_types - framing_types)
    for framing_type in missing_types:
        missing.append({
            "type": "missing_framing",
            "framing": framing_type,
            "note": "Natural-product / traditional-medicine scans need this frame unless explicitly out of scope.",
        })

    cjk_pattern = re.compile(r"[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]")
    for language, queries in queries_by_language.items():
        if not queries:
            missing.append({
                "type": "missing_language_queries",
                "language": language,
                "note": "No query strings tagged for this language.",
            })
        elif not any(cjk_pattern.search(query) for query in queries):
            missing.append({
                "type": "missing_original_script",
                "language": language,
                "note": "Queries exist but do not include Chinese/Japanese/Korean script terms.",
            })

    return {
        "verdict": "needs_revision" if missing else "adequate",
        "missing": missing,
        "required_protocol": "mechanism + species_original_language + traditional_formula + traditional_pathology",
    }


def extract_json_object(text):
    """
    Parse a JSON object from a model response.
    Accepts either raw JSON or a fenced ```json block.
    """
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    else:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            text = text[start:end + 1]
    return json.loads(text)


class OpenRouterClient:
    """Minimal OpenRouter chat-completions client using only urllib."""

    def __init__(self, api_key=None, app_title="Open Enzyme comp-NNN"):
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "OPENROUTER_API_KEY is not set. Put it in the repo-root .env "
                "or export it in the shell before running analyze.py."
            )
        self.app_title = app_title

    def chat(self, model, messages, temperature=0.2, max_tokens=4096):
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            OPENROUTER_CHAT_URL,
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/brianpabent/open-enzyme",
                "X-Title": self.app_title,
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenRouter HTTP {exc.code}: {detail}") from exc

        data = json.loads(raw)
        choice = data["choices"][0]
        message = choice.get("message", {})
        text = message.get("content", "")
        return {
            "model": data.get("model", model),
            "response_id": data.get("id"),
            "created": data.get("created"),
            "text": text,
            "raw": data,
        }


def role_model(config, role):
    """Return the configured model name for a role."""
    value = config["roles"][role]
    if isinstance(value, dict):
        env_name = value.get("env")
        if env_name and os.environ.get(env_name):
            return os.environ[env_name]
        return value["model"]
    return value


def host_allowed_for_local_curl(hostname, allowed_suffixes=None):
    """
    Return True only when hostname matches the explicit local-curl allowlist.

    This protects against blindly curling arbitrary model-proposed URLs while
    still supporting Brian's firewall-whitelisted academic domains.
    """
    if not hostname:
        return False
    host = hostname.lower().rstrip(".")
    allowed = allowed_suffixes or DEFAULT_LOCAL_CURL_ALLOWED_SUFFIXES
    for suffix in allowed:
        suffix = suffix.lower()
        bare = suffix[1:] if suffix.startswith(".") else suffix
        if host == bare or host.endswith(suffix):
            return True
    return False


def local_curl_fetch(url, output_dir, allowed_suffixes=None, timeout_seconds=90, allow_insecure_tls=False):
    """
    Fetch a URL via the local machine's curl binary and write provenance.

    Why curl instead of model/web fetch: Chinese academic sources may only be
    reachable from Brian's whitelisted laptop network path; hosted model fetches
    can egress from vendor servers and hit the firewall differently.

    Returns a provenance dict. Raises ValueError for non-allowlisted hosts.
    """
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError(f"local_curl_fetch only supports http/https URLs: {url}")
    if not host_allowed_for_local_curl(parsed.hostname, allowed_suffixes):
        raise ValueError(f"Host is not in local-curl allowlist: {parsed.hostname}")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    query_hash = ""
    if parsed.query:
        import hashlib
        query_hash = "_" + hashlib.sha256(parsed.query.encode("utf-8")).hexdigest()[:12]
    stem = safe_filename(f"{parsed.netloc}{parsed.path}{query_hash}") or "fetch"
    body_path = output_dir / f"{stem}.html"
    meta_path = output_dir / f"{stem}.provenance.json"

    cmd = [
        "curl",
        "--location",
        "--silent",
        "--show-error",
        "--fail",
        "--max-time",
        str(timeout_seconds),
        "--user-agent",
        "OpenEnzyme-lit-synthesis/1.0",
        "--output",
        str(body_path),
        "--write-out",
        "%{http_code} %{content_type} %{url_effective}",
        url,
    ]
    if allow_insecure_tls:
        cmd.insert(1, "--insecure")
    completed = subprocess.run(cmd, capture_output=True, text=True, check=False)
    provenance = {
        "url": url,
        "fetched_at_utc": utc_now_iso(),
        "method": "local_curl",
        "network_path": "local_machine",
        "hostname": parsed.hostname,
        "allowed_suffixes": list(allowed_suffixes or DEFAULT_LOCAL_CURL_ALLOWED_SUFFIXES),
        "returncode": completed.returncode,
        "allow_insecure_tls": allow_insecure_tls,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "body_path": str(body_path),
        "note": (
            "Fetched with local curl so firewall-whitelisted Chinese / Asian "
            "academic domains use the laptop network path, not model-vendor egress."
        ),
    }
    write_json(meta_path, provenance)
    if completed.returncode != 0:
        raise RuntimeError(f"curl failed for {url}; provenance written to {meta_path}")
    return provenance


def translation_models_for_language(config, language):
    """
    Return two independent translation model configs for a language.

    Config shape:
      {
        "translation": {
          "pairs": {
            "zh": {
              "model_a": {"model": "deepseek/...", "temperature": 0.0},
              "model_b": {"model": "openai/...", "temperature": 0.0},
              "referee": {"model": "anthropic/...", "temperature": 0.0}
            }
          }
        }
      }
    """
    pairs = config.get("translation", {}).get("pairs", {})
    if language in pairs:
        return pairs[language]
    if "default" in pairs:
        return pairs["default"]
    raise KeyError(f"No translation model pair configured for language: {language}")


def _model_name_from_role(role_config):
    env_name = role_config.get("env")
    if env_name and os.environ.get(env_name):
        return os.environ[env_name]
    return role_config["model"]


def translate_source_two_model(
    client,
    source_text,
    language,
    source_id,
    config,
    output_dir,
    target_language="English",
):
    """
    Translate non-English source text with two independent models, then produce
    an annotated translation that preserves science-relevant disagreements.

    This implements the Open Enzyme translation protocol:
    - two independent vendors / model families;
    - for Chinese, include a native-language-strong model such as DeepSeek;
    - disagreements that affect evidence tier, mechanism, dose, route, stats,
      or scientific hedging are surfaced inline, not silently resolved.

    Returns a dict with paths to raw and annotated artifacts.
    """
    pair = translation_models_for_language(config, language)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    base = safe_filename(source_id)

    system = (
        "You are translating scientific source material for Open Enzyme. "
        "Preserve scientific nuance, hedging, units, dose route, statistics, "
        "mechanism language, and study-design details. Do not summarize."
    )
    user = (
        f"Translate this {language} scientific text into {target_language}. "
        "Return the translation only, preserving paragraph structure.\n\n"
        f"SOURCE_ID: {source_id}\n\n{source_text}"
    )

    translations = {}
    for label in ("model_a", "model_b"):
        role = pair[label]
        model = _model_name_from_role(role)
        response = client.chat(
            model,
            [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=role.get("temperature", 0.0),
            max_tokens=role.get("max_tokens", 6000),
        )
        translations[label] = {
            "model": response["model"],
            "response_id": response["response_id"],
            "text": response["text"],
        }

    referee_role = pair.get("referee", pair["model_b"])
    referee_model = _model_name_from_role(referee_role)
    referee_prompt = f"""Compare two independent translations of the same scientific source.

Produce an annotated English translation. Where both translations agree, write
clean English. Where they disagree in a way that could affect scientific
interpretation, preserve both readings inline using:
{{Model A: "..." | Model B: "..."}}

Add [TRANSLATION-DISAGREEMENT] before any sentence where the disagreement affects:
- evidence-tier judgment;
- mechanism mapping;
- dose, route, units, statistics, or sample size;
- study design;
- scientific hedging such as inhibits / modulates / may / suggests.

Do not silently choose one model's interpretation for load-bearing claims.

SOURCE_ID: {source_id}

MODEL A ({translations['model_a']['model']}):
{translations['model_a']['text']}

MODEL B ({translations['model_b']['model']}):
{translations['model_b']['text']}

Return JSON only:
{{
  "source_id": "{source_id}",
  "language": "{language}",
  "annotated_translation": "...",
  "disagreement_notes": [
    {{"category": "dose | mechanism | evidence_tier | hedging | statistics | study_design | other", "note": "..."}}
  ],
  "load_bearing_disagreement": true
}}"""
    referee_response = client.chat(
        referee_model,
        [
            {"role": "system", "content": system},
            {"role": "user", "content": referee_prompt},
        ],
        temperature=referee_role.get("temperature", 0.0),
        max_tokens=referee_role.get("max_tokens", 6000),
    )
    annotated = extract_json_object(referee_response["text"])

    artifact = {
        "source_id": source_id,
        "language": language,
        "created_at_utc": utc_now_iso(),
        "protocol": "two_model_independent_translation_with_inline_disagreements",
        "models": translations,
        "referee": {
            "model": referee_response["model"],
            "response_id": referee_response["response_id"],
        },
        "annotated": annotated,
    }
    artifact_path = output_dir / f"{base}.translation-crosscheck.json"
    markdown_path = output_dir / f"{base}.annotated-translation.md"
    write_json(artifact_path, artifact)
    markdown_path.write_text(
        "# Annotated Translation\n\n"
        f"**Source:** {source_id}\n\n"
        f"**Language:** {language}\n\n"
        f"**Protocol:** two independent models + inline disagreement annotation\n\n"
        f"{annotated.get('annotated_translation', '')}\n\n"
        "## Disagreement Notes\n\n"
        + "\n".join(
            f"- **{item.get('category', 'other')}:** {item.get('note', '')}"
            for item in annotated.get("disagreement_notes", [])
        )
        + "\n"
    )
    return {
        "artifact_path": str(artifact_path),
        "markdown_path": str(markdown_path),
        "load_bearing_disagreement": annotated.get("load_bearing_disagreement"),
    }


def _urlopen_json(url, params, timeout=60):
    query = urllib.parse.urlencode(params)
    full_url = f"{url}?{query}"
    try:
        with urllib.request.urlopen(full_url, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError:
        completed = subprocess.run(
            ["curl", "--location", "--silent", "--show-error", "--fail", "--max-time", str(timeout), full_url],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(f"curl fallback failed for {url}: {completed.stderr.strip()}")
        return json.loads(completed.stdout)


def pubmed_search(query, retmax=10, mindate=None, maxdate=None):
    """Return PMIDs for a PubMed title/abstract/citation search."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": str(retmax),
        "sort": "relevance",
    }
    if mindate or maxdate:
        params["datetype"] = "pdat"
        if mindate:
            params["mindate"] = mindate
        if maxdate:
            params["maxdate"] = maxdate
    data = _urlopen_json(NCBI_ESEARCH_URL, params)
    return data.get("esearchresult", {}).get("idlist", [])


def pubmed_fetch_records(pmids):
    """Fetch compact title/abstract/DOI metadata for a PMID list."""
    if not pmids:
        return []
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    }
    query = urllib.parse.urlencode(params)
    full_url = f"{NCBI_EFETCH_URL}?{query}"
    try:
        with urllib.request.urlopen(full_url, timeout=120) as response:
            xml_text = response.read().decode("utf-8", errors="replace")
    except urllib.error.URLError:
        completed = subprocess.run(
            ["curl", "--location", "--silent", "--show-error", "--fail", "--max-time", "120", full_url],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(f"curl fallback failed for PubMed efetch: {completed.stderr.strip()}")
        xml_text = completed.stdout

    root = ET.fromstring(xml_text)
    records = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or ""
        title = "".join(article.find(".//ArticleTitle").itertext()).strip() if article.find(".//ArticleTitle") is not None else ""
        abstract_parts = [
            "".join(node.itertext()).strip()
            for node in article.findall(".//Abstract/AbstractText")
        ]
        journal = article.findtext(".//Journal/Title") or ""
        year = (
            article.findtext(".//JournalIssue/PubDate/Year")
            or article.findtext(".//ArticleDate/Year")
            or ""
        )
        doi = ""
        for node in article.findall(".//ArticleId"):
            if node.attrib.get("IdType") == "doi":
                doi = (node.text or "").strip()
                break
        records.append({
            "pmid": pmid,
            "title": title,
            "abstract": "\n".join(part for part in abstract_parts if part),
            "journal": journal,
            "year": year,
            "doi": doi,
            "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
        })
    return records


def fetch_pubmed_snapshot(query_strategy, retmax_per_query=10, pause_seconds=0.34):
    """
    Run all committed PubMed-style queries and return a dated PMID snapshot.
    This is discovery metadata, not full-text verification.
    """
    query_results = []
    pmid_to_queries = {}
    for framing in query_strategy.get("framings", []):
        for query in framing.get("queries", []):
            pmids = pubmed_search(query, retmax=retmax_per_query)
            query_results.append({
                "framing": framing.get("type", ""),
                "query": query,
                "pmids": pmids,
            })
            for pmid in pmids:
                pmid_to_queries.setdefault(pmid, []).append(query)
            time.sleep(pause_seconds)

    records = pubmed_fetch_records(sorted(pmid_to_queries)) if pmid_to_queries else []
    for record in records:
        record["matched_queries"] = pmid_to_queries.get(record["pmid"], [])

    return {
        "fetched_at_utc": utc_now_iso(),
        "retmax_per_query": retmax_per_query,
        "query_results": query_results,
        "records": records,
        "limitations": [
            "PubMed snapshot contains title/abstract/citation metadata only.",
            "Final GREEN verdicts require full text, protocol PDFs, vendor validation docs, or method-comparison data.",
        ],
    }
