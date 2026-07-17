#!/usr/bin/env python3
"""Deterministic delta collection and reviewed promotion for evidence radar feeds.

Collection is source-specific and model-free. Only changed records enter a
small, hash-bound packet. A separate context-isolated review may emit active
queue items; raw packets and review output remain short-lived CI artifacts.
"""

from __future__ import annotations

import argparse
import datetime as dt
from functools import lru_cache
import gzip
import hashlib
import html
from html.parser import HTMLParser
from http.cookiejar import CookieJar
import json
import math
import os
from pathlib import Path
import re
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import build_opener, HTTPCookieProcessor, Request


ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
DEFAULT_CONFIG = ROOT / "scripts" / "evidence-radar-config.json"
DEFAULT_STATE = ROOT / "logs" / "evidence-radar-state.json"
DEFAULT_TRIAL_RECORDS = ROOT / "logs" / "evidence-radar-clinical-records.json.gz"
DEFAULT_REVIEW_PROMPT = ROOT / "scripts" / "evidence-radar-review-prompt.md"
USER_AGENT = (
    "OpenEnzymeEvidenceRadar/1.0 "
    "(+https://github.com/brianpabent/open-enzyme; research surveillance)"
)
NCT_RE = re.compile(r"\bNCT\d{8}\b")
QUARTER_RE = re.compile(r"\b(20\d{2})\s+Q([1-4])\b", re.I)
SAFE_KEY_RE = re.compile(r"[^a-z0-9]+")
QUEUE_VERDICTS = {"queue", "monitor", "dismiss"}


class RadarError(RuntimeError):
    """Fail-closed collection or review error."""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def canonical_hash(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def with_hash(value: dict[str, Any], field: str) -> dict[str, Any]:
    payload = {key: item for key, item in value.items() if key != field}
    value[field] = canonical_hash(payload)
    return value


def verify_hash(value: dict[str, Any], field: str) -> None:
    recorded = value.get(field)
    payload = {key: item for key, item in value.items() if key != field}
    if not isinstance(recorded, str) or canonical_hash(payload) != recorded:
        raise RadarError(f"{field} does not match the exact artifact")


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except FileNotFoundError:
        return {}
    except (OSError, json.JSONDecodeError) as exc:
        raise RadarError(f"Cannot read {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RadarError(f"{path} must contain a JSON object")
    return value


def write_json(path: Path, value: object, *, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if compact:
        rendered = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    else:
        rendered = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False)
    path.write_text(rendered + "\n")


def load_compressed_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(gzip.decompress(path.read_bytes()).decode("utf-8"))
    except FileNotFoundError:
        return {}
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RadarError(f"Cannot read compressed JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RadarError(f"{path} must contain a compressed JSON object")
    return value


def write_compressed_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # A fixed gzip timestamp makes an unchanged source snapshot byte-identical,
    # so Git does not receive a new binary object on every monthly no-op run.
    path.write_bytes(gzip.compress(canonical_bytes(value), compresslevel=9, mtime=0))


def trial_records_from_state(state: dict[str, Any], path: Path) -> dict[str, Any]:
    feed = ((state.get("feeds") or {}).get("clinical_trials") or {})
    # One-time migration path for the initial local baseline.
    embedded = feed.get("records")
    records = embedded if isinstance(embedded, dict) else load_compressed_json(path)
    expected = feed.get("records_sha256")
    if expected and canonical_hash(records) != expected:
        raise RadarError("Clinical-trial record store does not match current-state hash")
    expected_count = feed.get("record_count")
    if expected_count is not None and int(expected_count) != len(records):
        raise RadarError("Clinical-trial record store count does not match current state")
    return records


def empty_state() -> dict[str, Any]:
    return {"schema_version": 1, "updated_at": None, "feeds": {}}


def slug(value: str, limit: int = 72) -> str:
    result = SAFE_KEY_RE.sub("-", value.lower()).strip("-")[:limit].rstrip("-")
    return result or "unknown"


def request_json(
    url: str,
    params: dict[str, object] | None = None,
    *,
    headers: dict[str, str] | None = None,
    timeout: int = 90,
    not_found_empty: bool = False,
) -> dict[str, Any]:
    target = url + (("?" + urlencode(params, doseq=True)) if params else "")
    merged_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    merged_headers.update(headers or {})
    last_error: Exception | None = None
    for attempt, delay in enumerate((0, 3, 12), start=1):
        if delay:
            time.sleep(delay)
        try:
            with build_opener().open(Request(target, headers=merged_headers), timeout=timeout) as response:
                value = json.loads(response.read().decode("utf-8"))
            if not isinstance(value, dict):
                raise RadarError(f"Non-object JSON from {url}")
            return value
        except HTTPError as exc:
            if exc.code == 404 and not_found_empty:
                return {}
            last_error = exc
            if exc.code < 500 and exc.code != 429:
                break
        except (URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
            last_error = exc
        if attempt == 3:
            break
    raise RadarError(f"Request failed for {url}: {last_error}")


def corpus_files() -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "index.md"]
    paths.extend(sorted((ROOT / "wiki").rglob("*.md")))
    return [path for path in paths if path.is_file()]


def corpus_nct_ids() -> list[str]:
    found: set[str] = set()
    for path in corpus_files():
        found.update(NCT_RE.findall(path.read_text(errors="replace")))
    return sorted(found)


@lru_cache(maxsize=1)
def corpus_line_index() -> tuple[tuple[str, int, str, str], ...]:
    lines: list[tuple[str, int, str, str]] = []
    for path in corpus_files():
        rel = path.relative_to(ROOT).as_posix()
        for line_number, line in enumerate(path.read_text(errors="replace").splitlines(), start=1):
            rendered = re.sub(r"\s+", " ", line).strip()[:320]
            lines.append((rel, line_number, rendered, line.casefold()))
    return tuple(lines)


def corpus_context(terms: list[str], *, maximum_hits: int = 12) -> dict[str, Any]:
    clean_terms = []
    for term in terms:
        term = re.sub(r"\s+", " ", str(term)).strip()
        if len(term) >= 4 and term.casefold() not in {item.casefold() for item in clean_terms}:
            clean_terms.append(term)
    hits: list[dict[str, object]] = []
    owners: set[str] = set()
    for rel, line_number, rendered, folded in corpus_line_index():
        matched = next((term for term in clean_terms if term.casefold() in folded), None)
        if not matched:
            continue
        hits.append({
            "path": rel,
            "line": line_number,
            "matched_term": matched,
            "text": rendered,
        })
        if rel.startswith("wiki/"):
            owners.add(rel)
        if len(hits) >= maximum_hits:
            return {"hits": hits, "possible_owners": sorted(owners)}
    return {"hits": hits, "possible_owners": sorted(owners)}


def changed_fields(previous: dict[str, Any], current: dict[str, Any]) -> list[str]:
    ignored = {"fingerprint", "source_profiles", "source_url"}
    return sorted(
        key for key in set(previous) | set(current)
        if key not in ignored and previous.get(key) != current.get(key)
    )


def record_fingerprint(record: dict[str, Any]) -> str:
    ignored = {"fingerprint", "source_profiles", "source_url"}
    return canonical_hash({key: value for key, value in record.items() if key not in ignored})


def nested(value: dict[str, Any], *keys: str, default: Any = None) -> Any:
    current: Any = value
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    return default if current is None else current


def normalize_ctg(study: dict[str, Any], profiles: list[str]) -> dict[str, Any]:
    protocol = study.get("protocolSection") or {}
    ident = protocol.get("identificationModule") or {}
    status = protocol.get("statusModule") or {}
    design = protocol.get("designModule") or {}
    conditions = protocol.get("conditionsModule") or {}
    arms = protocol.get("armsInterventionsModule") or {}
    nct_id = ident.get("nctId")
    if not isinstance(nct_id, str) or not NCT_RE.fullmatch(nct_id):
        raise RadarError("ClinicalTrials.gov record is missing a valid NCT ID")
    interventions = sorted({
        str(item.get("name")).strip()
        for item in (arms.get("interventions") or [])
        if isinstance(item, dict) and item.get("name")
    })
    record = {
        "source": "clinicaltrials.gov",
        "registry_id": nct_id,
        "title": ident.get("briefTitle") or ident.get("officialTitle") or "",
        "status": status.get("overallStatus") or "UNKNOWN",
        "study_type": design.get("studyType") or "",
        "phases": sorted(design.get("phases") or []),
        "conditions": sorted(str(item) for item in (conditions.get("conditions") or [])),
        "interventions": interventions,
        "enrollment": nested(design, "enrollmentInfo", "count"),
        "enrollment_type": nested(design, "enrollmentInfo", "type", default=""),
        "first_posted": nested(status, "studyFirstPostDateStruct", "date", default=""),
        "last_update_posted": nested(status, "lastUpdatePostDateStruct", "date", default=""),
        "primary_completion": nested(status, "primaryCompletionDateStruct", "date", default=""),
        "completion": nested(status, "completionDateStruct", "date", default=""),
        "has_results": bool(study.get("hasResults")),
        "source_profiles": sorted(set(profiles)),
        "source_url": f"https://clinicaltrials.gov/study/{nct_id}",
    }
    record["fingerprint"] = record_fingerprint(record)
    return record


def fetch_ctg(config: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, Any], list[dict[str, Any]]]:
    base = str(config["base_url"]).rstrip("/")
    page_size = int(config.get("page_size") or 100)
    version = request_json(f"{base}/version")
    records: dict[str, dict[str, Any]] = {}
    profiles_by_id: dict[str, set[str]] = {}
    raw_by_id: dict[str, dict[str, Any]] = {}
    attempts: list[dict[str, Any]] = []
    for profile in config.get("profiles") or []:
        profile_id = str(profile["id"])
        params = {str(key): value for key, value in (profile.get("params") or {}).items()}
        params.update({"format": "json", "pageSize": page_size, "countTotal": "true"})
        page_token: str | None = None
        count = 0
        try:
            while True:
                request_params = dict(params)
                if page_token:
                    request_params["pageToken"] = page_token
                payload = request_json(f"{base}/studies", request_params)
                for study in payload.get("studies") or []:
                    nct_id = nested(study, "protocolSection", "identificationModule", "nctId")
                    if not isinstance(nct_id, str):
                        continue
                    raw_by_id[nct_id] = study
                    profiles_by_id.setdefault(nct_id, set()).add(profile_id)
                    count += 1
                page_token = payload.get("nextPageToken")
                if not page_token:
                    break
            attempts.append({"source": "ClinicalTrials.gov", "query_id": profile_id, "status": "success", "result_count": count, "error": None})
        except RadarError as exc:
            attempts.append({"source": "ClinicalTrials.gov", "query_id": profile_id, "status": "failed", "result_count": count, "error": str(exc)})

    for nct_id in corpus_nct_ids():
        if nct_id in raw_by_id:
            profiles_by_id[nct_id].add("corpus-tracked-id")
            continue
        try:
            study = request_json(f"{base}/studies/{nct_id}")
            raw_by_id[nct_id] = study
            profiles_by_id.setdefault(nct_id, set()).add("corpus-tracked-id")
        except RadarError as exc:
            attempts.append({"source": "ClinicalTrials.gov", "query_id": f"tracked:{nct_id}", "status": "failed", "result_count": 0, "error": str(exc)})

    for nct_id, study in raw_by_id.items():
        records[f"ctg:{nct_id}"] = normalize_ctg(study, sorted(profiles_by_id[nct_id]))
    snapshot = {
        "data_timestamp": version.get("dataTimestamp"),
        "api_version": version.get("version"),
        "record_count": len(records),
    }
    return records, snapshot, attempts


class HiddenInputParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "input" and values.get("name") and values.get("type") == "hidden":
            self.values[str(values["name"])] = str(values.get("value") or "")


def hidden_inputs(page: str) -> dict[str, str]:
    parser = HiddenInputParser()
    parser.feed(page)
    return parser.values


def strip_markup(value: str) -> str:
    without_tags = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(without_tags)).strip()


def parse_who_results(page: str, profile_id: str) -> tuple[list[dict[str, Any]], int]:
    label_match = re.search(r'id="Label3"[^>]*>(.*?)</span>', page, re.I | re.S)
    total_text = strip_markup(label_match.group(1)) if label_match else ""
    total_match = re.search(r"(\d+)\s+records\s+for\s+(\d+)\s+trials", total_text, re.I)
    total_records = int(total_match.group(1)) if total_match else 0
    records: list[dict[str, Any]] = []
    for row in re.findall(r'<tr\s+valign="top"[^>]*>(.*?)</tr>', page, re.I | re.S):
        id_match = re.search(r'id="GridView1_ctl\d+_Label1"[^>]*>(.*?)</span>', row, re.I | re.S)
        link_match = re.search(r'href="(Trial2\.aspx\?TrialID=([^"&]+))"[^>]*>(.*?)</a>', row, re.I | re.S)
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.I | re.S)
        if not id_match or not link_match or len(cells) < 3:
            continue
        registry_id = strip_markup(id_match.group(1))
        title = strip_markup(link_match.group(3))
        record = {
            "source": "who-ictrp",
            "registry_id": registry_id,
            "title": title,
            "status": strip_markup(cells[0]),
            "registration_date": strip_markup(cells[-2]),
            "has_results": bool(strip_markup(cells[-1])),
            "source_profiles": [profile_id],
            "source_url": f"https://trialsearch.who.int/Trial2.aspx?TrialID={registry_id}",
        }
        record["fingerprint"] = record_fingerprint(record)
        records.append(record)
    return records, total_records


def who_open(opener: Any, request: Request, *, timeout: int = 90) -> str:
    last_error: Exception | None = None
    for attempt, delay in enumerate((0, 3, 12), start=1):
        if delay:
            time.sleep(delay)
        try:
            with opener.open(request, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="replace")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = exc
        if attempt == 3:
            break
    raise RadarError(f"WHO ICTRP request failed: {last_error}")


def who_post(opener: Any, url: str, form: dict[str, str]) -> str:
    return who_open(
        opener,
        Request(
            url,
            data=urlencode(form).encode(),
            headers={"User-Agent": USER_AGENT, "Content-Type": "application/x-www-form-urlencoded"},
        ),
    )


def who_import_snapshot(page: str) -> dict[str, str]:
    imports: dict[str, str] = {}
    pattern = re.compile(
        r'<span\s+id="(lbl[^"]+)"[^>]*>.*?<li>(.*?)last data file imported on\s*<b>(.*?)</b>',
        re.I | re.S,
    )
    for label, registry, date_value in pattern.findall(page):
        imports[label] = f"{strip_markup(registry)}|{strip_markup(date_value)}"
    return imports


def fetch_who(config: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, Any], list[dict[str, Any]]]:
    url = str(config["base_url"])
    page_size = int(config.get("page_size") or 100)
    maximum = int(config.get("max_records_per_query") or 2500)
    snapshot_opener = build_opener(HTTPCookieProcessor(CookieJar()))
    home = who_open(snapshot_opener, Request(url, headers={"User-Agent": USER_AGENT}))
    imports = who_import_snapshot(home)
    combined: dict[str, dict[str, Any]] = {}
    attempts: list[dict[str, Any]] = []
    for query in config.get("queries") or []:
        query_id = str(query["id"])
        term = str(query["term"])
        try:
            # The legacy ASP.NET portal keeps search state in its session. A
            # fresh cookie jar and VIEWSTATE per query prevent one query from
            # corrupting the next query's postback state.
            opener = build_opener(HTTPCookieProcessor(CookieJar()))
            query_home = who_open(opener, Request(url, headers={"User-Agent": USER_AGENT}))
            form = hidden_inputs(query_home)
            form.update({"TextBox1": term, "Button1": "Search"})
            page = who_post(opener, url, form)
            size_form = hidden_inputs(page)
            size_form.update({"__EVENTTARGET": "DropDownList1", "__EVENTARGUMENT": "", "DropDownList1": str(page_size)})
            page = who_post(opener, url, size_form)
            page_records, total = parse_who_results(page, query_id)
            if total > maximum:
                raise RadarError(f"WHO query {query_id} returned {total} records; cap is {maximum}")
            pages = max(1, math.ceil(total / page_size))
            records = list(page_records)
            for page_number in range(2, pages + 1):
                page_form = hidden_inputs(page)
                page_form.update({
                    "__EVENTTARGET": "GridView1",
                    "__EVENTARGUMENT": f"Page${page_number}",
                    "DropDownList1": str(page_size),
                })
                page = who_post(opener, url, page_form)
                page_records, _ = parse_who_results(page, query_id)
                records.extend(page_records)
            for record in records:
                # ClinicalTrials.gov is queried directly with richer fields;
                # omit its mirrored ICTRP row so one trial cannot generate two
                # queue candidates for the same registry change.
                if NCT_RE.fullmatch(str(record["registry_id"])):
                    continue
                key = f"who:{record['registry_id']}"
                if key in combined:
                    profiles = set(combined[key]["source_profiles"]) | set(record["source_profiles"])
                    combined[key]["source_profiles"] = sorted(profiles)
                else:
                    combined[key] = record
            attempts.append({
                "source": "WHO ICTRP",
                "query_id": query_id,
                "language": query.get("language"),
                "query": term,
                "status": "success",
                "result_count": len(records),
                "error": None,
            })
        except RadarError as exc:
            attempts.append({
                "source": "WHO ICTRP",
                "query_id": query_id,
                "language": query.get("language"),
                "query": term,
                "status": "failed",
                "result_count": 0,
                "error": str(exc),
            })
    snapshot = {
        "registry_imports": imports,
        "registry_imports_sha256": canonical_hash(imports),
        "record_count": len(combined),
    }
    return combined, snapshot, attempts


def date_on_or_after(value: object, boundary: str) -> bool:
    if not isinstance(value, str) or not value:
        return False
    return value[:10] >= boundary


def trial_candidate(key: str, previous: dict[str, Any] | None, current: dict[str, Any]) -> dict[str, Any]:
    fields = ["new_record"] if previous is None else changed_fields(previous, current)
    context_terms = [current["registry_id"]]
    context_terms.extend(current.get("interventions") or [])
    context = corpus_context(context_terms)
    digest = canonical_hash({"key": key, "fingerprint": current["fingerprint"], "fields": fields})[:16]
    return {
        "candidate_id": f"trial-{digest}",
        "queue_key": f"radar-trial-{slug(current['source'])}-{slug(current['registry_id'])}",
        "feed": "clinical_trials",
        "change_type": "new" if previous is None else "changed",
        "changed_fields": fields,
        "previous": previous,
        "current": current,
        "corpus_context": context,
        "default_owner": "wiki/gout-clinical-pipeline.md",
        "evidence_boundary": "Registry protocol/status metadata only; not evidence of efficacy.",
    }


def collect_trials(
    state: dict[str, Any],
    config: dict[str, Any],
    *,
    baseline_only: bool,
    old_records: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    old_feed = ((state.get("feeds") or {}).get("clinical_trials") or {})
    old_records = old_records or {}
    ctg_records, ctg_snapshot, ctg_attempts = fetch_ctg(config["clinicaltrials_gov"])
    who_records, who_snapshot, who_attempts = fetch_who(config["who_ictrp"])
    attempts = ctg_attempts + who_attempts
    ctg_profile_ids = {str(item["id"]) for item in config["clinicaltrials_gov"].get("profiles") or []}
    who_profile_ids = {str(item["id"]) for item in config["who_ictrp"].get("queries") or []}
    ctg_status = {
        str(item.get("query_id")): item.get("status")
        for item in attempts
        if item.get("source") == "ClinicalTrials.gov"
    }
    who_status = {
        str(item.get("query_id")): item.get("status")
        for item in attempts
        if item.get("source") == "WHO ICTRP"
    }
    # Fail closed at the source boundary. A partial profile union cannot safely
    # replace the complete prior source baseline: records unique to the failed
    # profile would disappear and later return as false "new" trials.
    ctg_ok = bool(ctg_profile_ids) and all(ctg_status.get(item) == "success" for item in ctg_profile_ids)
    who_ok = bool(who_profile_ids) and all(who_status.get(item) == "success" for item in who_profile_ids)
    records: dict[str, dict[str, Any]] = {}
    if ctg_ok:
        records.update(ctg_records)
        for query_id, status in ctg_status.items():
            if query_id.startswith("tracked:") and status != "success":
                key = "ctg:" + query_id.removeprefix("tracked:")
                if key in old_records:
                    records[key] = old_records[key]
    else:
        records.update({key: value for key, value in old_records.items() if key.startswith("ctg:")})
    if who_ok:
        records.update(who_records)
    else:
        records.update({key: value for key, value in old_records.items() if key.startswith("who:")})

    initial_since = str(config.get("initial_since") or "1970-01-01")
    candidates: list[dict[str, Any]] = []
    if not baseline_only:
        for key, current in sorted(records.items()):
            previous = old_records.get(key)
            if previous and previous.get("fingerprint") == current.get("fingerprint"):
                continue
            if previous is None and old_records:
                candidates.append(trial_candidate(key, None, current))
            elif previous is None and (
                date_on_or_after(current.get("first_posted"), initial_since)
                or date_on_or_after(current.get("registration_date"), initial_since)
                or date_on_or_after(current.get("last_update_posted"), initial_since)
            ):
                candidates.append(trial_candidate(key, None, current))
            elif previous is not None:
                candidates.append(trial_candidate(key, previous, current))

    collected_at = utc_now()
    source_snapshot = {"clinicaltrials_gov": ctg_snapshot, "who_ictrp": who_snapshot}
    next_state = json.loads(json.dumps(state or empty_state()))
    next_state.setdefault("schema_version", 1)
    next_state.setdefault("feeds", {})["clinical_trials"] = {
        "records_file": "logs/evidence-radar-clinical-records.json.gz",
        "records_sha256": canonical_hash(records),
        "record_count": len(records),
        "last_collection": {
            "collected_at": collected_at,
            "baseline_only": baseline_only,
            "config_sha256": canonical_hash(config),
            "source_snapshot": source_snapshot,
            "query_attempts": attempts,
            "record_count": len(records),
            "candidate_count": len(candidates),
            "coverage_complete": all(item["status"] == "success" for item in attempts),
        },
        "last_review": old_feed.get("last_review"),
    }
    packet = {
        "schema_version": 1,
        "feed": "clinical_trials",
        "created_at": collected_at,
        "baseline_only": baseline_only,
        "source_snapshot": source_snapshot,
        "config_sha256": canonical_hash(config),
        "previous_state_sha256": canonical_hash(old_feed),
        "candidate_count": len(candidates),
        "candidates": candidates,
        "red_herring_context": [],
        "query_attempts": attempts,
    }
    with_hash(packet, "packet_sha256")
    next_state["feeds"]["clinical_trials"]["pending_packet_sha256"] = packet["packet_sha256"]
    return packet, next_state, records


def latest_faers_quarter(manifest: dict[str, Any]) -> tuple[int, int]:
    partitions = nested(manifest, "results", "drug", "event", "partitions", default=[])
    quarters = []
    for partition in partitions if isinstance(partitions, list) else []:
        match = QUARTER_RE.search(str((partition or {}).get("display_name") or ""))
        if match:
            quarters.append((int(match.group(1)), int(match.group(2))))
    if not quarters:
        raise RadarError("openFDA download manifest contains no drug-event quarter")
    return max(quarters)


def quarter_key(value: tuple[int, int]) -> str:
    return f"{value[0]}Q{value[1]}"


def parse_quarter(value: str) -> tuple[int, int]:
    match = re.fullmatch(r"(20\d{2})Q([1-4])", value)
    if not match:
        raise RadarError(f"Invalid quarter cursor: {value}")
    return int(match.group(1)), int(match.group(2))


def next_quarter(value: tuple[int, int]) -> tuple[int, int]:
    year, quarter = value
    return (year + 1, 1) if quarter == 4 else (year, quarter + 1)


def quarter_range(start_exclusive: tuple[int, int] | None, end_inclusive: tuple[int, int]) -> list[tuple[int, int]]:
    current = end_inclusive if start_exclusive is None else next_quarter(start_exclusive)
    result = []
    while current <= end_inclusive:
        result.append(current)
        current = next_quarter(current)
    return result


def quarter_dates(value: tuple[int, int]) -> tuple[str, str]:
    year, quarter = value
    start_month = 1 + (quarter - 1) * 3
    start = dt.date(year, start_month, 1)
    end_month = start_month + 2
    if end_month == 12:
        next_month = dt.date(year + 1, 1, 1)
    else:
        next_month = dt.date(year, end_month + 1, 1)
    end = next_month - dt.timedelta(days=1)
    return start.strftime("%Y%m%d"), end.strftime("%Y%m%d")


def fetch_faers_window(config: dict[str, Any], quarters: list[tuple[int, int]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], str | None]:
    reports: dict[str, dict[str, Any]] = {}
    attempts: list[dict[str, Any]] = []
    source_last_updated: str | None = None
    for quarter in quarters:
        start, end = quarter_dates(quarter)
        for event_term in config.get("event_terms") or []:
            search = f'patient.reaction.reactionmeddrapt:"{event_term}" AND receiptdate:[{start} TO {end}]'
            skip = 0
            total = None
            count = 0
            try:
                while total is None or skip < total:
                    payload = request_json(
                        str(config["api_url"]),
                        {"search": search, "limit": int(config.get("page_size") or 1000), "skip": skip},
                        not_found_empty=True,
                    )
                    if not payload:
                        total = 0
                        break
                    meta = payload.get("meta") or {}
                    source_last_updated = str(meta.get("last_updated") or source_last_updated or "") or None
                    total = int(nested(meta, "results", "total", default=0) or 0)
                    maximum = int(config.get("max_reports_per_term_quarter") or 25000)
                    if total > maximum:
                        raise RadarError(f"{event_term} {quarter_key(quarter)} returned {total}; cap is {maximum}")
                    page = payload.get("results") or []
                    for report in page:
                        report_id = str(report.get("safetyreportid") or "")
                        if not report_id:
                            continue
                        version = int(str(report.get("safetyreportversion") or "0") or 0)
                        old_version = int(str((reports.get(report_id) or {}).get("safetyreportversion") or "0") or 0)
                        if report_id not in reports or version >= old_version:
                            reports[report_id] = report
                    count += len(page)
                    if not page:
                        break
                    skip += len(page)
                attempts.append({
                    "source": "openFDA FAERS",
                    "query_id": f"{quarter_key(quarter)}:{event_term}",
                    "query": search,
                    "status": "success",
                    "result_count": count,
                    "error": None,
                })
            except RadarError as exc:
                attempts.append({
                    "source": "openFDA FAERS",
                    "query_id": f"{quarter_key(quarter)}:{event_term}",
                    "query": search,
                    "status": "failed",
                    "result_count": count,
                    "error": str(exc),
                })
    if any(item["status"] != "success" for item in attempts):
        failures = "; ".join(
            f"{item['query_id']}: {item['error']}"
            for item in attempts
            if item["status"] != "success"
        )
        raise RadarError(f"FAERS collection was incomplete; cursor not advanced: {failures}")
    return list(reports.values()), attempts, source_last_updated


def normalized_drug_name(drug: dict[str, Any]) -> str:
    generic = nested(drug, "openfda", "generic_name", default=[])
    value = generic[0] if isinstance(generic, list) and generic else drug.get("medicinalproduct")
    return re.sub(r"\s+", " ", str(value or "UNKNOWN")).strip().upper()


def aggregate_faers(reports: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    wanted = {str(item).casefold() for item in config.get("event_terms") or []}
    aggregates: dict[str, dict[str, Any]] = {}
    for report in reports:
        report_id = str(report.get("safetyreportid") or "")
        duplicate_number = nested(report, "reportduplicate", "duplicatenumb", default="")
        case_key = str(report.get("companynumb") or duplicate_number or report_id)
        patient = report.get("patient") or {}
        report_drugs = [item for item in (patient.get("drug") or []) if isinstance(item, dict)]
        suspect_names = {
            normalized_drug_name(item)
            for item in report_drugs
            if str(item.get("drugcharacterization") or "") == "1"
        }
        suspect_burden = len(suspect_names)
        events = {
            str(item.get("reactionmeddrapt") or "").upper()
            for item in (patient.get("reaction") or [])
            if str(item.get("reactionmeddrapt") or "").casefold() in wanted
        }
        if not report_id or not events:
            continue
        for drug in report_drugs:
            name = normalized_drug_name(drug)
            aggregate = aggregates.setdefault(name, {
                "drug": name,
                "report_ids": set(),
                "case_ids": set(),
                "suspect_ids": set(),
                "informative_suspect_ids": set(),
                "sole_suspect_ids": set(),
                "high_polypharmacy_ids": set(),
                "concomitant_ids": set(),
                "interacting_ids": set(),
                "serious_ids": set(),
                "rechallenge_ids": set(),
                "events": {},
                "countries": set(),
                "products": set(),
                "indications": set(),
                "indication_recorded_ids": set(),
            })
            aggregate["report_ids"].add(report_id)
            aggregate["case_ids"].add(case_key)
            role = str(drug.get("drugcharacterization") or "")
            if role == "1":
                aggregate["suspect_ids"].add(case_key)
                maximum_burden = int(config.get("maximum_suspect_drugs_per_informative_report") or 3)
                if suspect_burden <= maximum_burden:
                    aggregate["informative_suspect_ids"].add(case_key)
                if suspect_burden == 1:
                    aggregate["sole_suspect_ids"].add(case_key)
                if suspect_burden > 10:
                    aggregate["high_polypharmacy_ids"].add(case_key)
            elif role == "2":
                aggregate["concomitant_ids"].add(case_key)
            elif role == "3":
                aggregate["interacting_ids"].add(case_key)
            if str(report.get("serious") or "") == "1":
                aggregate["serious_ids"].add(case_key)
            if str(drug.get("drugrecurreadministration") or "") == "1":
                aggregate["rechallenge_ids"].add(case_key)
            for event in events:
                aggregate["events"].setdefault(event, set()).add(case_key)
            country = report.get("primarysourcecountry") or report.get("occurcountry")
            if country:
                aggregate["countries"].add(str(country))
            product = drug.get("medicinalproduct")
            if product:
                aggregate["products"].add(str(product).strip())
            indication = drug.get("drugindication")
            if indication:
                aggregate["indications"].add(str(indication).strip())
                aggregate["indication_recorded_ids"].add(case_key)

    result = []
    gout_treatments = [str(item).upper() for item in config.get("known_gout_treatments") or []]
    indication_terms = [str(item).upper() for item in config.get("confounding_indication_terms") or []]
    for aggregate in aggregates.values():
        indications = sorted(aggregate["indications"])
        value = {
            "drug": aggregate["drug"],
            "unique_reports": len(aggregate["report_ids"]),
            "unique_cases": len(aggregate["case_ids"]),
            "suspect_reports": len(aggregate["suspect_ids"]),
            "informative_suspect_reports": len(aggregate["informative_suspect_ids"]),
            "sole_suspect_reports": len(aggregate["sole_suspect_ids"]),
            "high_polypharmacy_reports": len(aggregate["high_polypharmacy_ids"]),
            "concomitant_reports": len(aggregate["concomitant_ids"]),
            "interacting_reports": len(aggregate["interacting_ids"]),
            "serious_reports": len(aggregate["serious_ids"]),
            "positive_rechallenge_reports": len(aggregate["rechallenge_ids"]),
            "event_counts": {key: len(ids) for key, ids in sorted(aggregate["events"].items())},
            "countries": sorted(aggregate["countries"])[:20],
            "products": sorted(aggregate["products"])[:20],
            "indications": indications[:20],
            "indication_recorded_cases": len(aggregate["indication_recorded_ids"]),
            "report_ids": sorted(aggregate["report_ids"])[:25],
            "known_gout_treatment": any(term in aggregate["drug"] for term in gout_treatments),
            "matching_confounding_indication_recorded": any(
                term in indication.upper() for indication in indications for term in indication_terms
            ),
        }
        value["score"] = (
            value["sole_suspect_reports"] * 8
            + value["informative_suspect_reports"] * 5
            + value["suspect_reports"]
            + value["interacting_reports"] * 3
            + value["positive_rechallenge_reports"] * 6
            + min(value["serious_reports"], 3)
        )
        result.append(value)
    return sorted(result, key=lambda item: (-item["score"], -item["unique_reports"], item["drug"]))


def faers_candidate(aggregate: dict[str, Any], window: list[str]) -> dict[str, Any]:
    context = corpus_context([aggregate["drug"], *(aggregate.get("products") or [])])
    digest = canonical_hash({"window": window, "aggregate": aggregate})[:16]
    queue_key = f"radar-faers-{slug(aggregate['drug'])}"
    queue_path = ROOT / "synthesis" / "queue" / f"{queue_key}.md"
    existing_queue = None
    if queue_path.is_file():
        existing_text = queue_path.read_text(errors="replace")
        headline = next((line.removeprefix("# ") for line in existing_text.splitlines() if line.startswith("# ")), "")
        existing_queue = {
            "path": queue_path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(existing_text.encode()).hexdigest(),
            "headline": headline,
        }
    return {
        "candidate_id": f"faers-{digest}",
        "queue_key": queue_key,
        "feed": "faers",
        "change_type": "new_reporting_window",
        "changed_fields": ["new_reports"],
        "previous": None,
        "current": aggregate,
        "reporting_window": window,
        "corpus_context": context,
        "default_owner": "wiki/open-questions.md",
        "evidence_boundary": "Unvalidated spontaneous-report association; not causality, incidence, or risk.",
        "existing_queue": existing_queue,
    }


def collect_faers(
    state: dict[str, Any],
    config: dict[str, Any],
    *,
    baseline_only: bool,
    start_after_quarter: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    old_feed = ((state.get("feeds") or {}).get("faers") or {})
    manifest = request_json(str(config["download_manifest_url"]))
    latest = latest_faers_quarter(manifest)
    cursor_raw = old_feed.get("cursor_quarter")
    cursor = parse_quarter(str(cursor_raw)) if cursor_raw else None
    carried_window = old_feed.get("processing_window") or []
    if start_after_quarter:
        cursor = parse_quarter(start_after_quarter)
        quarters = quarter_range(cursor, latest)
    elif carried_window and not baseline_only:
        quarters = [parse_quarter(str(item)) for item in carried_window]
    else:
        quarters = [] if baseline_only else quarter_range(cursor, latest)
    if not cursor and not quarters and not baseline_only:
        quarters = [latest]
    reports: list[dict[str, Any]] = []
    attempts: list[dict[str, Any]] = []
    source_last_updated = None
    if quarters:
        reports, attempts, source_last_updated = fetch_faers_window(config, quarters)
    aggregates = aggregate_faers(reports, config)
    minimum = int(config.get("minimum_suspect_reports") or 2)
    eligible = []
    red_herrings = []
    for aggregate in aggregates:
        qualifies = (
            aggregate["informative_suspect_reports"] >= minimum
            or aggregate["interacting_reports"] >= 1
            or aggregate["positive_rechallenge_reports"] >= 1
        )
        corpus_minimum = int(config.get("minimum_corpus_matched_suspect_reports") or 2)
        if not qualifies and aggregate["informative_suspect_reports"] >= corpus_minimum:
            context = corpus_context([aggregate["drug"], *(aggregate.get("products") or [])], maximum_hits=1)
            qualifies = bool(context["hits"])
        if qualifies and not baseline_only:
            eligible.append(aggregate)
        elif (
            (aggregate["concomitant_reports"] and not aggregate["suspect_reports"])
            or aggregate["high_polypharmacy_reports"]
        ):
            red_herrings.append(aggregate)
    maximum = int(config.get("maximum_review_candidates") or 40)
    window = [quarter_key(item) for item in quarters]
    target_quarter = quarter_key(max(quarters)) if quarters else quarter_key(latest)
    all_candidates = [faers_candidate(item, window) for item in eligible]
    processed = set(old_feed.get("processed_candidate_keys") or []) if carried_window == window else set()
    remaining = [item for item in all_candidates if item["queue_key"] not in processed]
    candidates = remaining[:maximum]
    overflow_count = max(0, len(remaining) - len(candidates))
    monitors = old_feed.get("monitors") if isinstance(old_feed.get("monitors"), dict) else {}
    for candidate in candidates:
        candidate["prior_monitor"] = monitors.get(candidate["queue_key"])
    red_max = int(config.get("maximum_red_herring_examples") or 25)
    collected_at = utc_now()
    drug_event = nested(manifest, "results", "drug", "event", default={})
    source_snapshot = {
        "download_export_date": drug_event.get("export_date") if isinstance(drug_event, dict) else None,
        "api_last_updated": source_last_updated,
        "latest_available_quarter": quarter_key(latest),
        "queried_quarters": window,
    }
    next_state = json.loads(json.dumps(state or empty_state()))
    next_state.setdefault("schema_version", 1)
    next_state.setdefault("feeds", {})["faers"] = {
        "cursor_quarter": old_feed.get("cursor_quarter"),
        "processing_window": window,
        "processed_candidate_keys": sorted(processed),
        "monitors": monitors,
        "pending_overflow_count": overflow_count,
        "pending_advance_cursor_to": target_quarter if overflow_count == 0 else None,
        "last_collection": {
            "collected_at": collected_at,
            "baseline_only": baseline_only,
            "config_sha256": canonical_hash(config),
            "source_snapshot": source_snapshot,
            "explicit_start_after_quarter": start_after_quarter,
            "query_attempts": attempts,
            "report_count": len(reports),
            "drug_count": len(aggregates),
            "candidate_count": len(candidates),
            "eligible_before_cap": len(eligible),
            "eligible_remaining_before_batch": len(remaining),
            "overflow_count": overflow_count,
            "candidate_cap": maximum,
            "source_coverage_complete": all(item.get("status") == "success" for item in attempts),
            "coverage_complete": overflow_count == 0 and all(item.get("status") == "success" for item in attempts),
        },
        "last_review": old_feed.get("last_review"),
    }
    packet = {
        "schema_version": 1,
        "feed": "faers",
        "created_at": collected_at,
        "baseline_only": baseline_only,
        "source_snapshot": source_snapshot,
        "config_sha256": canonical_hash(config),
        "previous_state_sha256": canonical_hash(old_feed),
        "candidate_count": len(candidates),
        "candidates": candidates,
        "prior_monitors": list(monitors.values()),
        "red_herring_context": red_herrings[:red_max],
        "query_attempts": attempts,
        "limitations": [
            "FAERS reports are unvalidated and cannot establish causality, incidence, or risk.",
            "The radar scans newly released receipt-date quarters; late amendments to older receipt dates may not be rediscovered.",
            f"At most {maximum} ranked candidates enter model review per batch; {overflow_count} remain for later exact-window batches.",
        ],
    }
    with_hash(packet, "packet_sha256")
    next_state["feeds"]["faers"]["pending_packet_sha256"] = packet["packet_sha256"]
    return packet, next_state


def estimated_review_cost(packet: dict[str, Any], prompt: str, review_config: dict[str, Any]) -> float:
    input_tokens = (len(prompt) + len(json.dumps(packet, ensure_ascii=False))) / 4
    input_rate = float(review_config.get("estimated_input_usd_per_million_tokens") or 5.0)
    output_rate = float(review_config.get("estimated_output_usd_per_million_tokens") or 20.0)
    output_tokens = int(review_config.get("maximum_output_tokens") or 8000)
    return input_tokens / 1_000_000 * input_rate + output_tokens / 1_000_000 * output_rate


def review_schema() -> dict[str, Any]:
    decision = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "candidate_id": {"type": "string"},
            "verdict": {"type": "string", "enum": sorted(QUEUE_VERDICTS)},
            "rationale": {"type": "string"},
            "headline": {"type": "string"},
            "why_actionable": {"type": "string"},
            "required_action": {"type": "string"},
            "evidence_boundary": {"type": "string"},
            "canonical_owner": {"type": "string"},
        },
        "required": [
            "candidate_id", "verdict", "rationale", "headline", "why_actionable",
            "required_action", "evidence_boundary", "canonical_owner",
        ],
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "schema_version": {"type": "integer", "enum": [1]},
            "reviewed_packet_sha256": {"type": "string"},
            "decisions": {"type": "array", "items": decision},
        },
        "required": ["schema_version", "reviewed_packet_sha256", "decisions"],
    }


def openrouter_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if key:
        return key
    env_path = ROOT / ".env"
    if env_path.is_file():
        for line in env_path.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise RadarError("OPENROUTER_API_KEY is required when candidates need review")


def openrouter_review(
    packet: dict[str, Any],
    prompt: str,
    *,
    model: str,
    maximum_output_tokens: int,
) -> tuple[dict[str, Any], dict[str, float]]:
    key = openrouter_key()
    body = {
        "model": model,
        "temperature": 0.1,
        "max_tokens": maximum_output_tokens,
        "messages": [{
            "role": "user",
            "content": prompt + "\n\nEVIDENCE RADAR PACKET\n" + json.dumps(packet, ensure_ascii=False),
        }],
        "response_format": {
            "type": "json_schema",
            "json_schema": {"name": "evidence_radar_review", "strict": True, "schema": review_schema()},
        },
    }
    request = Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/brianpabent/open-enzyme",
            "X-Title": "Open Enzyme evidence radar review",
            "User-Agent": USER_AGENT,
        },
    )
    last_error: Exception | None = None
    response: dict[str, Any] | None = None
    for attempt, delay in enumerate((0, 10, 30), start=1):
        if delay:
            time.sleep(delay)
        try:
            with build_opener().open(request, timeout=900) as raw:
                response = json.loads(raw.read().decode("utf-8"))
            if response.get("choices"):
                break
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            last_error = exc
        if attempt == 3:
            raise RadarError(f"OpenRouter review failed: {last_error}")
    if not response or not response.get("choices"):
        raise RadarError("OpenRouter returned no review choice")
    choice = response["choices"][0]
    if choice.get("finish_reason") == "length":
        raise RadarError("Review output was truncated")
    content = nested(choice, "message", "content", default="")
    if isinstance(content, list):
        content = "".join(str(item.get("text") or "") for item in content if isinstance(item, dict))
    try:
        review = json.loads(str(content))
    except json.JSONDecodeError as exc:
        raise RadarError(f"Reviewer did not return valid JSON: {exc}") from exc
    usage_raw = response.get("usage") or {}
    usage = {
        "input_tokens": float(usage_raw.get("prompt_tokens") or 0),
        "output_tokens": float(usage_raw.get("completion_tokens") or 0),
        "cost_usd": float(usage_raw.get("cost") or 0),
    }
    return review, usage


def validate_review(packet: dict[str, Any], review: dict[str, Any]) -> None:
    if review.get("schema_version") != 1:
        raise RadarError("Review schema_version must be 1")
    if review.get("reviewed_packet_sha256") != packet.get("packet_sha256"):
        raise RadarError("Review is not bound to the exact candidate packet")
    candidates = {item["candidate_id"]: item for item in packet.get("candidates") or []}
    decisions = review.get("decisions")
    if not isinstance(decisions, list):
        raise RadarError("Review decisions must be a list")
    decision_ids = [item.get("candidate_id") for item in decisions if isinstance(item, dict)]
    if set(decision_ids) != set(candidates) or len(decision_ids) != len(set(decision_ids)):
        raise RadarError("Review must contain exactly one decision for every candidate")
    for decision in decisions:
        candidate = candidates[decision["candidate_id"]]
        verdict = decision.get("verdict")
        if verdict not in QUEUE_VERDICTS:
            raise RadarError(f"Invalid verdict for {decision['candidate_id']}: {verdict}")
        for field in (
            "rationale", "headline", "why_actionable", "required_action",
            "evidence_boundary", "canonical_owner",
        ):
            value = decision.get(field)
            if not isinstance(value, str) or len(value) > 1600:
                raise RadarError(f"Review field {field} is invalid for {decision['candidate_id']}")
        if verdict == "queue":
            for field in ("headline", "why_actionable", "required_action", "evidence_boundary", "canonical_owner"):
                if not decision[field].strip():
                    raise RadarError(f"Queued decision is missing {field}: {decision['candidate_id']}")
            owner = ROOT / decision["canonical_owner"]
            allowed = set(candidate.get("corpus_context", {}).get("possible_owners") or [])
            allowed.add(candidate.get("default_owner"))
            if decision["canonical_owner"] not in allowed or not owner.is_file():
                raise RadarError(f"Queued decision names an unsupported canonical owner: {decision['canonical_owner']}")
        else:
            if any(decision[field].strip() for field in ("headline", "why_actionable", "required_action", "evidence_boundary", "canonical_owner")):
                raise RadarError(f"Non-queued decision contains queue-only prose: {decision['candidate_id']}")


def run_review(
    packet: dict[str, Any],
    config: dict[str, Any],
    *,
    model_override: str | None,
    max_cost_override: float | None,
) -> dict[str, Any]:
    verify_hash(packet, "packet_sha256")
    review_config = config["review"]
    model = model_override or str(review_config["model"])
    maximum_cost = max_cost_override if max_cost_override is not None else float(review_config["max_cost_usd"])
    if not packet.get("candidates"):
        review = {
            "schema_version": 1,
            "reviewed_packet_sha256": packet["packet_sha256"],
            "decisions": [],
        }
        usage = {"input_tokens": 0.0, "output_tokens": 0.0, "cost_usd": 0.0}
    else:
        prompt = DEFAULT_REVIEW_PROMPT.read_text()
        projected = estimated_review_cost(packet, prompt, review_config)
        if projected > maximum_cost:
            raise RadarError(f"Projected review cost ${projected:.4f} exceeds cap ${maximum_cost:.4f}")
        review, usage = openrouter_review(
            packet,
            prompt,
            model=model,
            maximum_output_tokens=int(review_config.get("maximum_output_tokens") or 8000),
        )
        if usage["cost_usd"] <= 0:
            usage["cost_usd"] = (
                usage["input_tokens"] / 1_000_000 * float(review_config.get("estimated_input_usd_per_million_tokens") or 5.0)
                + usage["output_tokens"] / 1_000_000 * float(review_config.get("estimated_output_usd_per_million_tokens") or 20.0)
            )
        if usage["cost_usd"] > maximum_cost:
            raise RadarError(f"Actual review cost ${usage['cost_usd']:.4f} exceeds cap ${maximum_cost:.4f}")
    validate_review(packet, review)
    review["reviewed_at"] = utc_now()
    review["reviewer_model"] = model
    review["usage"] = usage
    with_hash(review, "review_sha256")
    return review


def queue_source_delta(candidate: dict[str, Any]) -> str:
    current = candidate["current"]
    if candidate["feed"] == "clinical_trials":
        lines = [
            f"- Registry: `{current['registry_id']}` ({current['source']})",
            f"- Change: {candidate['change_type']} — {', '.join(candidate['changed_fields'])}",
            f"- Reported status: {current.get('status') or 'unknown'}",
            f"- Title: {current.get('title') or 'untitled'}",
            f"- Intervention(s): {', '.join(current.get('interventions') or []) or 'not supplied in the compact record'}",
            f"- Results posted: {'yes' if current.get('has_results') else 'no'}",
            f"- Source: {current['source_url']}",
        ]
        return "\n".join(lines)
    return "\n".join([
        f"- Drug identity: {current['drug']}",
        f"- Released reporting window: {', '.join(candidate.get('reporting_window') or [])}",
        f"- Unique reports: {current['unique_reports']}",
        f"- Deduplicated case keys: {current['unique_cases']}",
        f"- Suspect / concomitant / interacting: {current['suspect_reports']} / {current['concomitant_reports']} / {current['interacting_reports']}",
        f"- Informative suspect / sole suspect / high-polypharmacy: {current['informative_suspect_reports']} / {current['sole_suspect_reports']} / {current['high_polypharmacy_reports']}",
        f"- Positive rechallenge fields: {current['positive_rechallenge_reports']}",
        f"- Event terms: {json.dumps(current['event_counts'], sort_keys=True)}",
        f"- Indication fields captured: {current['indication_recorded_cases']} of {current['unique_cases']} deduplicated drug-case rows",
        f"- Matching gout/hyperuricemia indication recorded: {str(current['matching_confounding_indication_recorded']).lower()} (missing or blank indication fields remain unknown)",
        f"- Known gout-treatment identity: {str(current['known_gout_treatment']).lower()}",
        "- Source: https://open.fda.gov/apis/drug/event/",
    ])


def queue_markdown(candidate: dict[str, Any], decision: dict[str, Any], packet: dict[str, Any], review: dict[str, Any]) -> str:
    current = candidate["current"]
    source_ids = [current.get("registry_id")] if candidate["feed"] == "clinical_trials" else current.get("report_ids") or []
    frontmatter = [
        "---",
        "type: evidence-radar",
        f"feed: {candidate['feed']}",
        f"source_ids: {json.dumps(source_ids, ensure_ascii=False)}",
        f"source_snapshot: {json.dumps(packet['source_snapshot'], sort_keys=True, ensure_ascii=False)}",
        f"reviewed_packet_sha256: {packet['packet_sha256']}",
        f"review_sha256: {review['review_sha256']}",
        f"canonical_owner: {decision['canonical_owner']}",
        "---",
        "",
    ]
    body = [
        f"# {decision['headline'].strip()}",
        "",
        "## Why action remains open",
        "",
        decision["why_actionable"].strip(),
        "",
        "## Source delta",
        "",
        queue_source_delta(candidate),
        "",
        "## Required action",
        "",
        decision["required_action"].strip(),
        "",
        "## Evidence boundary",
        "",
        decision["evidence_boundary"].strip(),
        "",
        f"Apply any supported change in [{decision['canonical_owner']}](../../{decision['canonical_owner']}) and delete this queue file in the same commit. Git is the archive.",
        "",
    ]
    return "\n".join(frontmatter + body)


def apply_review(
    packet: dict[str, Any],
    next_state: dict[str, Any],
    review: dict[str, Any],
    state_path: Path,
    *,
    next_trial_records_path: Path | None = None,
    trial_records_path: Path | None = None,
) -> list[Path]:
    verify_hash(packet, "packet_sha256")
    verify_hash(review, "review_sha256")
    validate_review(packet, review)
    feed = packet["feed"]
    feed_state = nested(next_state, "feeds", feed)
    if not isinstance(feed_state, dict) or feed_state.get("pending_packet_sha256") != packet["packet_sha256"]:
        raise RadarError("Next state is not bound to the exact candidate packet")
    decisions = {item["candidate_id"]: item for item in review["decisions"]}
    trial_records: dict[str, Any] | None = None
    if feed == "clinical_trials":
        if next_trial_records_path is None or trial_records_path is None:
            raise RadarError("Clinical-trial apply requires the exact next compressed record store")
        trial_records = load_compressed_json(next_trial_records_path)
        if canonical_hash(trial_records) != feed_state.get("records_sha256"):
            raise RadarError("Next clinical-trial record store does not match reviewed state")
        if len(trial_records) != feed_state.get("record_count"):
            raise RadarError("Next clinical-trial record count does not match reviewed state")
    for candidate in packet.get("candidates") or []:
        if decisions[candidate["candidate_id"]]["verdict"] != "queue":
            continue
        path = ROOT / "synthesis" / "queue" / f"{candidate['queue_key']}.md"
        if path.exists():
            raise RadarError(f"Refusing to overwrite unresolved queue item: {path.relative_to(ROOT)}")
    written: list[Path] = []
    for candidate in packet.get("candidates") or []:
        decision = decisions[candidate["candidate_id"]]
        if decision["verdict"] != "queue":
            continue
        path = ROOT / "synthesis" / "queue" / f"{candidate['queue_key']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(queue_markdown(candidate, decision, packet, review))
        written.append(path)
    counts = {verdict: 0 for verdict in sorted(QUEUE_VERDICTS)}
    for decision in review["decisions"]:
        counts[decision["verdict"]] += 1
    previous_review = feed_state.get("last_review") if isinstance(feed_state.get("last_review"), dict) else {}
    reporting_window = packet.get("source_snapshot", {}).get("queried_quarters") or []
    if feed == "faers" and previous_review.get("reporting_window") == reporting_window:
        cumulative_counts = {
            verdict: int((previous_review.get("decision_counts") or {}).get(verdict, 0)) + counts[verdict]
            for verdict in sorted(QUEUE_VERDICTS)
        }
        cumulative_cost = float(previous_review.get("cost_usd") or 0) + float(review["usage"]["cost_usd"])
    else:
        cumulative_counts = counts
        cumulative_cost = float(review["usage"]["cost_usd"])
    monitors = feed_state.get("monitors") if isinstance(feed_state.get("monitors"), dict) else {}
    for candidate in packet.get("candidates") or []:
        decision = decisions[candidate["candidate_id"]]
        key = candidate["queue_key"]
        if decision["verdict"] == "monitor":
            current = candidate.get("current") or {}
            monitors[key] = {
                "key": key,
                "subject": current.get("drug") or current.get("registry_id"),
                "candidate_id": candidate["candidate_id"],
                "reporting_window": candidate.get("reporting_window") or [],
                "rationale": decision["rationale"].strip(),
                "last_seen": review["reviewed_at"],
                "current_fingerprint": current.get("fingerprint") or canonical_hash(current),
            }
        else:
            monitors.pop(key, None)
    feed_state["monitors"] = monitors

    if feed == "faers":
        processed = set(feed_state.get("processed_candidate_keys") or [])
        processed.update(item["queue_key"] for item in packet.get("candidates") or [])
        overflow = int(feed_state.pop("pending_overflow_count", 0) or 0)
        advance_to = feed_state.pop("pending_advance_cursor_to", None)
        if overflow == 0 and advance_to:
            feed_state["cursor_quarter"] = advance_to
            feed_state.pop("processing_window", None)
            feed_state.pop("processed_candidate_keys", None)
        else:
            feed_state["processed_candidate_keys"] = sorted(processed)

    if feed == "clinical_trials":
        assert next_trial_records_path is not None and trial_records_path is not None and trial_records is not None
        trial_records_path.parent.mkdir(parents=True, exist_ok=True)
        trial_records_path.write_bytes(next_trial_records_path.read_bytes())

    feed_state.pop("pending_packet_sha256", None)
    feed_state["last_review"] = {
        "reviewed_at": review["reviewed_at"],
        "packet_sha256": packet["packet_sha256"],
        "review_sha256": review["review_sha256"],
        "reviewer_model": review["reviewer_model"],
        "reporting_window": reporting_window,
        "batch_decision_counts": counts,
        "decision_counts": cumulative_counts,
        "batch_cost_usd": review["usage"]["cost_usd"],
        "cost_usd": cumulative_cost,
    }
    next_state["updated_at"] = review["reviewed_at"]
    # This current-state registry is not a human narrative and can contain a
    # few thousand compact fingerprints. One-line canonical JSON keeps it out
    # of token-heavy diffs while Git still records exact revisions.
    write_json(state_path, next_state, compact=True)
    return written


def resolve_path(raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else ROOT / path


def status_summary(state: dict[str, Any]) -> dict[str, Any]:
    summary: dict[str, Any] = {"schema_version": 1, "updated_at": state.get("updated_at"), "feeds": {}}
    for feed_name, feed in sorted((state.get("feeds") or {}).items()):
        collection = feed.get("last_collection") or {}
        attempts = collection.get("query_attempts") or []
        failures = [
            {
                "source": item.get("source"),
                "query_id": item.get("query_id"),
                "error": item.get("error"),
            }
            for item in attempts
            if item.get("status") != "success"
        ]
        review = feed.get("last_review") or {}
        summary["feeds"][feed_name] = {
            "collected_at": collection.get("collected_at"),
            "baseline_only": collection.get("baseline_only"),
            "coverage_complete": collection.get("coverage_complete"),
            "source_snapshot": collection.get("source_snapshot"),
            "record_count": collection.get("record_count", collection.get("report_count", 0)),
            "candidate_count": collection.get("candidate_count", 0),
            "review_backlog_count": collection.get("overflow_count", 0),
            "source_failures": failures,
            "reviewed_at": review.get("reviewed_at"),
            "decision_counts": review.get("decision_counts") or {},
            "review_cost_usd": review.get("cost_usd", 0.0),
            "monitor_count": len(feed.get("monitors") or {}),
        }
        if feed_name == "faers":
            summary["feeds"][feed_name]["cursor_quarter"] = feed.get("cursor_quarter")
            summary["feeds"][feed_name]["processing_window"] = feed.get("processing_window") or []
    return summary


def validate_state(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if state.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    feeds = state.get("feeds")
    if not isinstance(feeds, dict):
        return errors + ["feeds must be an object"]
    unknown = sorted(set(feeds) - {"clinical_trials", "faers"})
    if unknown:
        errors.append("unknown feeds: " + ", ".join(unknown))
    for name, feed in feeds.items():
        if not isinstance(feed, dict):
            errors.append(f"{name} must be an object")
            continue
        if "pending_packet_sha256" in feed:
            errors.append(f"{name} contains unapplied pending_packet_sha256")
        collection = feed.get("last_collection")
        review = feed.get("last_review")
        if not isinstance(collection, dict):
            errors.append(f"{name}.last_collection must be an object")
            continue
        if not isinstance(review, dict):
            errors.append(f"{name}.last_review must be an object")
        attempts = collection.get("query_attempts")
        if not isinstance(attempts, list):
            errors.append(f"{name}.last_collection.query_attempts must be a list")
            attempts = []
        statuses = {item.get("status") for item in attempts if isinstance(item, dict)}
        if not statuses.issubset({"success", "failed", "partial"}):
            errors.append(f"{name} has an invalid query status")
        if collection.get("coverage_complete") is True and statuses - {"success"}:
            errors.append(f"{name} claims complete coverage despite a failed or partial query")
        if int(collection.get("overflow_count", 0) or 0) > 0 and collection.get("coverage_complete") is True:
            errors.append(f"{name} claims complete coverage despite an undisposed review backlog")
        if name == "clinical_trials":
            embedded_records = feed.get("records") if isinstance(feed.get("records"), dict) else None
            if feed.get("records_file") != "logs/evidence-radar-clinical-records.json.gz" and embedded_records is None:
                errors.append("clinical_trials record-store path is missing")
            if not isinstance(feed.get("records_sha256"), str) and embedded_records is None:
                errors.append("clinical_trials record-store hash is missing")
            stored_count = len(embedded_records) if embedded_records is not None else feed.get("record_count")
            if stored_count != collection.get("record_count"):
                errors.append("clinical_trials record_count does not match latest collection")
        if name == "faers":
            try:
                parse_quarter(str(feed.get("cursor_quarter")))
            except RadarError as exc:
                errors.append(str(exc))
            overflow = int(collection.get("overflow_count", 0) or 0)
            if overflow > 0 and not feed.get("processing_window"):
                errors.append("faers review backlog is missing its exact processing window")
            if feed.get("processing_window") and not isinstance(feed.get("processed_candidate_keys"), list):
                errors.append("faers processing window is missing reviewed candidate keys")
            if not isinstance(feed.get("monitors", {}), dict):
                errors.append("faers monitors must be an object")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    subparsers = parser.add_subparsers(dest="command", required=True)

    collect = subparsers.add_parser("collect", help="Collect one deterministic source delta")
    collect.add_argument("--feed", choices=("clinical_trials", "faers"), required=True)
    collect.add_argument("--state", default=str(DEFAULT_STATE))
    collect.add_argument("--work-dir", required=True)
    collect.add_argument("--baseline-only", action="store_true")
    collect.add_argument("--start-after-quarter", help="FAERS recovery/backfill cursor such as 2025Q4")
    collect.add_argument("--trial-records", default=str(DEFAULT_TRIAL_RECORDS))

    review_parser = subparsers.add_parser("review", help="Review an exact candidate packet")
    review_parser.add_argument("--packet", required=True)
    review_parser.add_argument("--output", required=True)
    review_parser.add_argument("--model")
    review_parser.add_argument("--max-cost-usd", type=float)
    review_parser.add_argument("--prepare-only", action="store_true")

    apply_parser = subparsers.add_parser("apply", help="Apply reviewed state and active queue items")
    apply_parser.add_argument("--packet", required=True)
    apply_parser.add_argument("--next-state", required=True)
    apply_parser.add_argument("--review", required=True)
    apply_parser.add_argument("--state", default=str(DEFAULT_STATE))
    apply_parser.add_argument("--trial-records", default=str(DEFAULT_TRIAL_RECORDS))
    apply_parser.add_argument("--next-trial-records")

    status_parser = subparsers.add_parser("status", help="Print compact read-only feed status")
    status_parser.add_argument("--state", default=str(DEFAULT_STATE))
    status_parser.add_argument("--trial-records", default=str(DEFAULT_TRIAL_RECORDS))

    check_parser = subparsers.add_parser("check", help="Validate the current compact feed state")
    check_parser.add_argument("--state", default=str(DEFAULT_STATE))
    check_parser.add_argument("--trial-records", default=str(DEFAULT_TRIAL_RECORDS))

    args = parser.parse_args()
    config = load_json(resolve_path(args.config))
    if config.get("schema_version") != 1:
        raise RadarError("Evidence-radar config schema_version must be 1")

    if args.command in {"status", "check"}:
        state = load_json(resolve_path(args.state)) or empty_state()
        errors = validate_state(state)
        if ((state.get("feeds") or {}).get("clinical_trials")):
            try:
                trial_records_from_state(state, resolve_path(args.trial_records))
            except RadarError as exc:
                errors.append(str(exc))
        if errors:
            raise RadarError("; ".join(errors))
        if args.command == "check":
            print(f"Evidence-radar state validation passed for {len(state.get('feeds') or {})} feed(s)")
            return
        print(json.dumps(status_summary(state), indent=2, sort_keys=True, ensure_ascii=False))
        return

    if args.command == "collect":
        state_path = resolve_path(args.state)
        state = load_json(state_path) or empty_state()
        if state.get("schema_version") != 1:
            raise RadarError("Evidence-radar state schema_version must be 1")
        if args.feed == "clinical_trials":
            if args.start_after_quarter:
                raise RadarError("--start-after-quarter applies only to FAERS")
            old_records = trial_records_from_state(state, resolve_path(args.trial_records))
            packet, next_state, next_trial_records = collect_trials(
                state,
                config["clinical_trials"],
                baseline_only=args.baseline_only,
                old_records=old_records,
            )
        else:
            packet, next_state = collect_faers(
                state,
                config["faers"],
                baseline_only=args.baseline_only,
                start_after_quarter=args.start_after_quarter,
            )
        work = resolve_path(args.work_dir)
        work.mkdir(parents=True, exist_ok=True)
        packet_path = work / f"{args.feed}-packet.json"
        next_state_path = work / f"{args.feed}-next-state.json"
        write_json(packet_path, packet)
        write_json(next_state_path, next_state)
        if args.feed == "clinical_trials":
            next_records_path = work / "clinical_trials-records.json.gz"
            write_compressed_json(next_records_path, next_trial_records)
            print(f"NEXT_TRIAL_RECORDS={next_records_path}")
        print(f"PACKET={packet_path}")
        print(f"NEXT_STATE={next_state_path}")
        print(f"CANDIDATE_COUNT={packet['candidate_count']}")
        print(f"PACKET_SHA256={packet['packet_sha256']}")
        return

    if args.command == "review":
        packet = load_json(resolve_path(args.packet))
        if args.prepare_only:
            verify_hash(packet, "packet_sha256")
            review_config = config["review"]
            prompt = DEFAULT_REVIEW_PROMPT.read_text()
            projected = 0.0 if not packet.get("candidates") else estimated_review_cost(packet, prompt, review_config)
            cap = args.max_cost_usd if args.max_cost_usd is not None else float(review_config["max_cost_usd"])
            result = {
                "candidate_count": packet.get("candidate_count", 0),
                "packet_sha256": packet["packet_sha256"],
                "projected_cost_usd": round(projected, 6),
                "max_cost_usd": cap,
                "within_cap": projected <= cap,
            }
            print(json.dumps(result, sort_keys=True))
            if projected > cap:
                raise RadarError(f"Projected review cost ${projected:.4f} exceeds cap ${cap:.4f}")
            return
        review = run_review(packet, config, model_override=args.model, max_cost_override=args.max_cost_usd)
        output = resolve_path(args.output)
        write_json(output, review)
        print(f"REVIEW={output}")
        print(f"REVIEW_SHA256={review['review_sha256']}")
        print(f"ACTUAL_COST_USD={review['usage']['cost_usd']:.6f}")
        return

    packet = load_json(resolve_path(args.packet))
    next_state = load_json(resolve_path(args.next_state))
    review = load_json(resolve_path(args.review))
    next_trial_records = resolve_path(args.next_trial_records) if args.next_trial_records else None
    paths = apply_review(
        packet,
        next_state,
        review,
        resolve_path(args.state),
        next_trial_records_path=next_trial_records,
        trial_records_path=resolve_path(args.trial_records),
    )
    print(f"QUEUE_ITEMS={len(paths)}")
    for path in paths:
        print(f"QUEUE_FILE={path.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except RadarError as exc:
        raise SystemExit(f"evidence-radar: {exc}") from exc
