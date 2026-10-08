from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


radar = load("evidence_radar_test", ROOT / "scripts" / "evidence-radar.py")


class ClinicalTrialCollectionTests(unittest.TestCase):
    def test_clinicaltrials_record_preserves_status_results_and_interventions(self):
        study = {
            "protocolSection": {
                "identificationModule": {"nctId": "NCT01234567", "briefTitle": "A gout trial"},
                "statusModule": {
                    "overallStatus": "RECRUITING",
                    "studyFirstPostDateStruct": {"date": "2026-01-01"},
                    "lastUpdatePostDateStruct": {"date": "2026-07-01"},
                },
                "designModule": {
                    "studyType": "INTERVENTIONAL",
                    "phases": ["PHASE2"],
                    "enrollmentInfo": {"count": 40, "type": "ESTIMATED"},
                },
                "conditionsModule": {"conditions": ["Gout"]},
                "armsInterventionsModule": {
                    "interventions": [{"name": "Experimental uricase"}],
                },
            },
            "hasResults": True,
        }
        record = radar.normalize_ctg(study, ["condition-gout"])
        self.assertEqual("RECRUITING", record["status"])
        self.assertTrue(record["has_results"])
        self.assertEqual(["Experimental uricase"], record["interventions"])
        self.assertEqual(64, len(record["fingerprint"]))

    def test_who_result_parser_keeps_registry_identity_and_evidence_boundary_fields(self):
        page = """
        <span id="Label3"><font>12 records for 10 trials found for: gout</font></span>
        <tr valign="top" style="background-color:#EFF3FB;">
          <td>Recruiting</td><td></td>
          <td><span id="GridView1_ctl03_Label1">ChiCTR2600127702</span></td>
          <td><div></div></td>
          <td><a href="Trial2.aspx?TrialID=ChiCTR2600127702">A gout study</a></td>
          <td>2026-07-06</td><td>&nbsp;</td>
        </tr>
        """
        records, total = radar.parse_who_results(page, "global-gout-en")
        self.assertEqual(12, total)
        self.assertEqual(1, len(records))
        self.assertEqual("ChiCTR2600127702", records[0]["registry_id"])
        self.assertFalse(records[0]["has_results"])
        self.assertEqual("Recruiting", records[0]["status"])

    def test_partial_profile_failure_preserves_complete_source_baseline(self):
        old_ctg = {"source": "clinicaltrials.gov", "registry_id": "NCT00000001", "fingerprint": "old-ctg"}
        old_who = {"source": "who-ictrp", "registry_id": "ChiCTR-old", "fingerprint": "old-who"}
        state = {"schema_version": 1, "feeds": {"clinical_trials": {"last_review": {}}}}
        config = {
            "initial_since": "2026-01-01",
            "clinicaltrials_gov": {"profiles": [{"id": "one"}, {"id": "two"}]},
            "who_ictrp": {"queries": [{"id": "global"}]},
        }
        ctg_attempts = [
            {"source": "ClinicalTrials.gov", "query_id": "one", "status": "success"},
            {"source": "ClinicalTrials.gov", "query_id": "two", "status": "failed"},
        ]
        who_attempts = [{"source": "WHO ICTRP", "query_id": "global", "status": "success"}]
        with (
            patch.object(radar, "fetch_ctg", return_value=({"ctg:NCT00000002": {"fingerprint": "partial"}}, {}, ctg_attempts)),
            patch.object(radar, "fetch_who", return_value=({"who:ChiCTR-new": {"fingerprint": "new"}}, {}, who_attempts)),
        ):
            _, next_state, records = radar.collect_trials(
                state,
                config,
                baseline_only=True,
                old_records={"ctg:NCT00000001": old_ctg, "who:ChiCTR-old": old_who},
            )
        self.assertIn("ctg:NCT00000001", records)
        self.assertNotIn("ctg:NCT00000002", records)
        self.assertIn("who:ChiCTR-new", records)
        self.assertFalse(next_state["feeds"]["clinical_trials"]["last_collection"]["coverage_complete"])

    def test_compressed_trial_store_is_deterministic(self):
        records = {"ctg:NCT01234567": {"fingerprint": "abc", "status": "RECRUITING"}}
        with tempfile.TemporaryDirectory() as tmp:
            one = Path(tmp) / "one.json.gz"
            two = Path(tmp) / "two.json.gz"
            radar.write_compressed_json(one, records)
            radar.write_compressed_json(two, records)
            self.assertEqual(one.read_bytes(), two.read_bytes())
            self.assertEqual(records, radar.load_compressed_json(one))


class FaersCollectionTests(unittest.TestCase):
    def test_report_level_drug_roles_are_not_misattributed(self):
        reports = [{
            "safetyreportid": "1",
            "serious": "1",
            "primarysourcecountry": "US",
            "patient": {
                "reaction": [{"reactionmeddrapt": "Gout"}],
                "drug": [
                    {
                        "drugcharacterization": "2",
                        "medicinalproduct": "CLOMID",
                        "openfda": {"generic_name": ["CLOMIPHENE CITRATE"]},
                    },
                    {
                        "drugcharacterization": "1",
                        "medicinalproduct": "OTHER DRUG",
                    },
                ],
            },
        }]
        config = {
            "event_terms": ["GOUT"],
            "known_gout_treatments": [],
            "confounding_indication_terms": [],
            "maximum_suspect_drugs_per_informative_report": 3,
        }
        values = {item["drug"]: item for item in radar.aggregate_faers(reports, config)}
        self.assertEqual(0, values["CLOMIPHENE CITRATE"]["suspect_reports"])
        self.assertEqual(1, values["CLOMIPHENE CITRATE"]["concomitant_reports"])
        self.assertEqual(1, values["OTHER DRUG"]["suspect_reports"])
        self.assertEqual(1, values["OTHER DRUG"]["sole_suspect_reports"])

    def test_many_co_suspects_do_not_count_as_informative_support(self):
        reports = [{
            "safetyreportid": "poly",
            "patient": {
                "reaction": [{"reactionmeddrapt": "Gout"}],
                "drug": [
                    {"drugcharacterization": "1", "medicinalproduct": name}
                    for name in ("A DRUG", "B DRUG", "C DRUG", "D DRUG")
                ],
            },
        }]
        config = {
            "event_terms": ["GOUT"],
            "known_gout_treatments": [],
            "confounding_indication_terms": [],
            "maximum_suspect_drugs_per_informative_report": 3,
        }
        values = radar.aggregate_faers(reports, config)
        self.assertTrue(all(item["suspect_reports"] == 1 for item in values))
        self.assertTrue(all(item["informative_suspect_reports"] == 0 for item in values))

    def test_company_case_number_collapses_duplicate_report_ids(self):
        reports = []
        for report_id in ("one", "two"):
            reports.append({
                "safetyreportid": report_id,
                "companynumb": "SAME-CASE",
                "patient": {
                    "reaction": [{"reactionmeddrapt": "Gout"}],
                    "drug": [{"drugcharacterization": "1", "medicinalproduct": "EXAMPLE"}],
                },
            })
        config = {
            "event_terms": ["GOUT"],
            "known_gout_treatments": [],
            "confounding_indication_terms": [],
            "maximum_suspect_drugs_per_informative_report": 3,
        }
        value = radar.aggregate_faers(reports, config)[0]
        self.assertEqual(2, value["unique_reports"])
        self.assertEqual(1, value["unique_cases"])
        self.assertEqual(1, value["suspect_reports"])

    def test_quarter_cursor_advances_without_replaying_old_windows(self):
        self.assertEqual([(2026, 1), (2026, 2)], radar.quarter_range((2025, 4), (2026, 2)))
        self.assertEqual([], radar.quarter_range((2026, 2), (2026, 2)))

    def test_candidate_overflow_keeps_cursor_and_exact_window_backlog(self):
        manifest = {"results": {"drug": {"event": {
            "export_date": "2026-07-01",
            "partitions": [{"display_name": "2026 Q1"}],
        }}}}
        aggregates = []
        for index in range(45):
            aggregates.append({
                "drug": f"TEST DRUG {index:02d}",
                "unique_reports": 2,
                "unique_cases": 2,
                "suspect_reports": 2,
                "informative_suspect_reports": 2,
                "sole_suspect_reports": 2,
                "high_polypharmacy_reports": 0,
                "concomitant_reports": 0,
                "interacting_reports": 0,
                "serious_reports": 0,
                "positive_rechallenge_reports": 0,
                "event_counts": {"GOUT": 2},
                "countries": [],
                "products": [],
                "indications": [],
                "indication_recorded_cases": 0,
                "report_ids": [f"r{index}"],
                "known_gout_treatment": False,
                "matching_confounding_indication_recorded": False,
                "score": 26,
            })
        config = {
            "download_manifest_url": "https://example.test/download.json",
            "minimum_suspect_reports": 2,
            "maximum_review_candidates": 40,
        }
        state = {"schema_version": 1, "feeds": {"faers": {"cursor_quarter": "2025Q4"}}}
        attempts = [{"source": "openFDA FAERS", "query_id": "GOUT:2026Q1", "status": "success"}]
        with (
            patch.object(radar, "request_json", return_value=manifest),
            patch.object(radar, "fetch_faers_window", return_value=([], attempts, "2026-04-01")),
            patch.object(radar, "aggregate_faers", return_value=aggregates),
        ):
            packet, next_state = radar.collect_faers(state, config, baseline_only=False)
        feed = next_state["feeds"]["faers"]
        self.assertEqual(40, packet["candidate_count"])
        self.assertEqual(5, feed["pending_overflow_count"])
        self.assertEqual("2025Q4", feed["cursor_quarter"])
        self.assertEqual(["2026Q1"], feed["processing_window"])
        self.assertFalse(feed["last_collection"]["coverage_complete"])


class ReviewAndQueueContractTests(unittest.TestCase):
    def packet(self, candidate_count: int = 1) -> dict:
        packet = {
            "schema_version": 1,
            "feed": "faers",
            "created_at": "2026-07-17T12:00:00Z",
            "source_snapshot": {"latest_available_quarter": "2025Q4"},
            "candidate_count": 1,
            "candidates": [{
                "candidate_id": "faers-abc",
                "queue_key": "radar-faers-example",
                "feed": "faers",
                "current": {
                    "drug": "EXAMPLE",
                    "unique_reports": 2,
                    "unique_cases": 2,
                    "suspect_reports": 2,
                    "informative_suspect_reports": 2,
                    "sole_suspect_reports": 2,
                    "high_polypharmacy_reports": 0,
                    "concomitant_reports": 0,
                    "interacting_reports": 0,
                    "positive_rechallenge_reports": 0,
                    "event_counts": {"GOUT": 2},
                    "known_gout_treatment": False,
                    "matching_confounding_indication_recorded": False,
                    "indication_recorded_cases": 0,
                    "report_ids": ["1", "2"],
                },
                "reporting_window": ["2025Q4"],
                "change_type": "new_reporting_window",
                "changed_fields": ["new_reports"],
                "corpus_context": {"hits": [], "possible_owners": []},
                "default_owner": "wiki/open-questions.md",
            }],
            "red_herring_context": [],
            "query_attempts": [],
        }
        if candidate_count != 1:
            candidate = packet["candidates"][0]
            packet["candidates"] = [
                {**candidate, "candidate_id": f"faers-{index}", "queue_key": f"radar-faers-{index}"}
                for index in range(candidate_count)
            ]
            packet["candidate_count"] = candidate_count
        return radar.with_hash(packet, "packet_sha256")

    def config(self) -> dict:
        config = radar.load_json(radar.DEFAULT_CONFIG)
        config["review"] = radar.review_settings(config["review"])
        return config

    def review(self, packet: dict) -> dict:
        return {
            "schema_version": 1,
            "reviewed_packet_sha256": packet["packet_sha256"],
            "decisions": [{
                "candidate_id": candidate["candidate_id"],
                "verdict": "monitor",
                "rationale": "Retain for later source verification.",
                "headline": "", "why_actionable": "", "required_action": "",
                "evidence_boundary": "", "canonical_owner": "",
            } for candidate in packet["candidates"]],
        }

    def prepare(self, packet: dict, *, cap: float | None = None) -> dict:
        with tempfile.TemporaryDirectory() as tmp:
            packet_path = Path(tmp) / "packet.json"
            output_path = Path(tmp) / "review.json"
            radar.write_json(packet_path, packet)
            argv = ["evidence-radar.py", "review", "--packet", str(packet_path),
                    "--output", str(output_path), "--prepare-only"]
            if cap is not None:
                argv.extend(["--max-cost-usd", str(cap)])
            stdout = io.StringIO()
            with patch.object(sys, "argv", argv), patch.object(radar, "openrouter_review") as call, redirect_stdout(stdout):
                try:
                    radar.main()
                finally:
                    call.assert_not_called()
                    self.assertFalse(output_path.exists())
            return json.loads(stdout.getvalue())

    def test_76_candidate_preflight_and_request_share_the_scaled_output_budget(self):
        packet = self.packet(76)
        original_hash = packet["packet_sha256"]
        # Exercise transport with an explicit mock-only budget; production stays $0.75.
        prepared = self.prepare(packet, cap=1.25)
        self.assertEqual(23552, prepared["maximum_output_tokens"])
        self.assertTrue(prepared["within_cap"])
        response = {
            "choices": [{"finish_reason": "stop", "message": {"content": json.dumps(self.review(packet))}}],
            "usage": {"prompt_tokens": 1000, "completion_tokens": 9000, "cost": 0.275},
        }
        with patch.object(radar, "openrouter_key", return_value="test-key"), patch.object(radar, "build_opener") as opener:
            opener.return_value.open.return_value.__enter__.return_value.read.return_value = json.dumps(response).encode()
            review = radar.run_review(packet, self.config(), model_override=None, max_cost_override=1.25)
        request = opener.return_value.open.call_args.args[0]
        self.assertEqual(prepared["maximum_output_tokens"], json.loads(request.data)["max_tokens"])
        self.assertEqual(1, opener.return_value.open.call_count)
        self.assertEqual(original_hash, packet["packet_sha256"])
        self.assertEqual(original_hash, review["reviewed_packet_sha256"])
        self.assertEqual(76, len(review["decisions"]))
        radar.verify_hash(review, "review_sha256")
        self.assertAlmostEqual(
            prepared["projected_cost_usd"],
            radar.estimated_review_cost(packet, radar.DEFAULT_REVIEW_PROMPT.read_text(), self.config()["review"]),
            places=6,
        )

    def test_scaled_output_cost_defers_before_any_model_call(self):
        packet = self.packet(76)
        config = self.config()
        input_tokens = (len(radar.DEFAULT_REVIEW_PROMPT.read_text()) + len(json.dumps(packet, ensure_ascii=False))) / 4
        # This cap admitted the old request but cannot fund the scaled allowance.
        old_projection = (
            radar.model_settings.estimate_cost(config["review"]["model"], input_tokens, 8000)
        )
        cap = old_projection + 0.001
        with self.assertRaisesRegex(radar.RadarError, "Projected review cost"):
            self.prepare(packet, cap=cap)
        with patch.object(radar, "openrouter_review") as call:
            with self.assertRaisesRegex(radar.RadarError, "Projected review cost"):
                radar.run_review(packet, config, model_override=None, max_cost_override=cap)
            call.assert_not_called()

    def test_verified_prices_and_default_cap_defer_the_76_candidate_packet(self):
        config = self.config()
        self.assertEqual("openai/gpt-5.5", config["review"]["model"])
        self.assertEqual(0.75, config["review"]["max_cost_usd"])
        self.assertEqual((5.0, 30.0), radar.review_token_rates(config["review"]))
        self.assertEqual((5.0, 30.0), radar.review_token_rates({}))
        packet = self.packet(76)
        with self.assertRaisesRegex(radar.RadarError, "Projected review cost"):
            self.prepare(packet)
        with patch.object(radar, "openrouter_review") as call:
            with self.assertRaisesRegex(radar.RadarError, "Projected review cost"):
                radar.run_review(packet, config, model_override=None, max_cost_override=None)
            call.assert_not_called()

    def test_usage_fallback_uses_the_same_verified_output_price(self):
        packet = self.packet()
        usage = {"input_tokens": 1000, "output_tokens": 8000, "cost_usd": 0.0}
        with patch.object(radar, "openrouter_review", return_value=(self.review(packet), usage)):
            review = radar.run_review(packet, self.config(), model_override=None, max_cost_override=None)
        self.assertAlmostEqual(0.245, review["usage"]["cost_usd"])

    def test_corrected_fallback_price_rejects_usage_the_old_price_admitted(self):
        packet = self.packet(30)
        review = self.review(packet)
        # $0.70 at the stale output price; $0.80 at the verified standard price.
        usage = {"input_tokens": 100000, "output_tokens": 10000, "cost_usd": 0.0}
        with patch.object(radar, "openrouter_review", return_value=(review, usage)):
            with self.assertRaisesRegex(radar.RadarError, "Actual review cost"):
                radar.run_review(packet, self.config(), model_override=None, max_cost_override=None)
        self.assertNotIn("review_sha256", review)

    def test_output_floor_and_allowed_ceiling_boundaries(self):
        config = self.config()["review"]
        for count, expected in ((15, 8000), (16, 8192), (109, 32000)):
            with self.subTest(candidates=count):
                self.assertEqual(expected, radar.review_output_tokens(self.packet(count), config))

    def test_invalid_output_budget_configuration_stops_before_a_model_call(self):
        for field, value in (
            ("minimum_output_tokens", 0), ("minimum_output_tokens", 32001),
            ("maximum_output_tokens", 0), ("maximum_output_tokens", None),
            ("output_tokens_per_candidate", 0), ("output_token_overhead", -1),
            ("output_token_overhead", "invalid"), ("maximum_output_tokens", float("inf")),
        ):
            with self.subTest(field=field, value=value):
                config = self.config()
                config["review"][field] = value
                with patch.object(radar, "openrouter_review") as call:
                    with self.assertRaisesRegex(radar.RadarError, "Invalid review output-token budget"):
                        radar.run_review(self.packet(), config, model_override=None, max_cost_override=None)
                    call.assert_not_called()

    def test_small_and_empty_packets_keep_the_floor_and_zero_cost(self):
        small = self.prepare(self.packet())
        self.assertEqual(8000, small["maximum_output_tokens"])
        empty = self.packet(0)
        prepared = self.prepare(empty, cap=0.0)
        self.assertEqual(0, prepared["maximum_output_tokens"])
        self.assertEqual(0.0, prepared["projected_cost_usd"])
        with patch.object(radar, "openrouter_review") as call:
            review = radar.run_review(empty, self.config(), model_override=None, max_cost_override=0.0)
            call.assert_not_called()
        self.assertEqual([], review["decisions"])
        self.assertEqual(0.0, review["usage"]["cost_usd"])
        radar.verify_hash(review, "review_sha256")

    def test_output_ceiling_defers_instead_of_clipping_a_large_packet(self):
        packet = self.packet(110)
        with self.assertRaisesRegex(radar.RadarError, "Required review output.*exceeds ceiling"):
            self.prepare(packet)
        with patch.object(radar, "openrouter_review") as call:
            with self.assertRaisesRegex(radar.RadarError, "Required review output.*exceeds ceiling"):
                radar.run_review(packet, self.config(), model_override=None, max_cost_override=None)
            call.assert_not_called()

    def test_truncated_response_never_writes_a_review_or_retries(self):
        packet = self.packet(76)
        response = {
            # Even parseable JSON is rejected when the provider reports truncation.
            "choices": [{"finish_reason": "length", "message": {"content": json.dumps(self.review(packet))}}],
            "usage": {"prompt_tokens": 1000, "completion_tokens": 23552, "cost": 0.71156},
        }
        with tempfile.TemporaryDirectory() as tmp:
            packet_path = Path(tmp) / "packet.json"
            output_path = Path(tmp) / "review.json"
            radar.write_json(packet_path, packet)
            argv = ["evidence-radar.py", "review", "--packet", str(packet_path), "--output", str(output_path),
                    "--max-cost-usd", "1.25"]
            with (
                patch.object(sys, "argv", argv),
                patch.object(radar, "openrouter_key", return_value="test-key"),
                patch.object(radar, "build_opener") as opener,
            ):
                opener.return_value.open.return_value.__enter__.return_value.read.return_value = json.dumps(response).encode()
                with self.assertRaisesRegex(radar.RadarError, "Review output was truncated"):
                    radar.main()
            self.assertEqual(1, opener.return_value.open.call_count)
            self.assertFalse(output_path.exists())

    def test_scaled_output_does_not_relax_review_binding_or_coverage(self):
        packet = self.packet(30)
        for invalid in ("hash", "coverage", "duplicate"):
            with self.subTest(invalid=invalid):
                review = self.review(packet)
                if invalid == "hash":
                    review["reviewed_packet_sha256"] = "wrong"
                elif invalid == "coverage":
                    review["decisions"].pop()
                else:
                    review["decisions"].append(review["decisions"][0])
                with patch.object(radar, "openrouter_review", return_value=(review, {"cost_usd": 0.01})) as call:
                    with self.assertRaises(radar.RadarError):
                        radar.run_review(packet, self.config(), model_override=None, max_cost_override=None)
                    call.assert_called_once()
                self.assertNotIn("review_sha256", review)

    def test_actual_usage_still_cannot_exceed_the_configured_cap(self):
        packet = self.packet(30)
        review = self.review(packet)
        with patch.object(radar, "openrouter_review", return_value=(review, {"cost_usd": 0.751})):
            with self.assertRaisesRegex(radar.RadarError, "Actual review cost"):
                radar.run_review(packet, self.config(), model_override=None, max_cost_override=None)
        self.assertNotIn("review_sha256", review)

    def test_changed_packet_is_rejected_before_any_model_call(self):
        packet = self.packet(76)
        packet["candidates"][0]["candidate_id"] = "changed"
        with patch.object(radar, "openrouter_review") as call:
            with self.assertRaisesRegex(radar.RadarError, "packet_sha256 does not match"):
                radar.run_review(packet, self.config(), model_override=None, max_cost_override=None)
            call.assert_not_called()

    def test_review_must_cover_every_candidate_and_bind_exact_packet(self):
        packet = self.packet()
        review = {
            "schema_version": 1,
            "reviewed_packet_sha256": packet["packet_sha256"],
            "decisions": [],
        }
        with self.assertRaises(radar.RadarError):
            radar.validate_review(packet, review)

    def test_noncausal_boundary_is_written_to_active_queue(self):
        packet = self.packet()
        review = {
            "schema_version": 1,
            "reviewed_packet_sha256": packet["packet_sha256"],
            "reviewed_at": "2026-07-17T12:01:00Z",
            "reviewer_model": "test",
            "usage": {"cost_usd": 0.0},
            "decisions": [{
                "candidate_id": "faers-abc",
                "verdict": "queue",
                "rationale": "Worth checking.",
                "headline": "FAERS lead — example and gout",
                "why_actionable": "Two reports justify source verification.",
                "required_action": "Reopen the reports and look for chronology and dechallenge.",
                "evidence_boundary": "This is an unvalidated spontaneous-report association, not causality or incidence.",
                "canonical_owner": "wiki/open-questions.md",
            }],
        }
        radar.with_hash(review, "review_sha256")
        next_state = {
            "schema_version": 1,
            "feeds": {"faers": {"pending_packet_sha256": packet["packet_sha256"]}},
        }
        original_root = radar.ROOT
        try:
            with tempfile.TemporaryDirectory() as tmp:
                radar.ROOT = Path(tmp)
                (radar.ROOT / "wiki").mkdir()
                (radar.ROOT / "wiki" / "open-questions.md").write_text("# Open questions\n")
                state = radar.ROOT / "logs" / "evidence-radar-state.json"
                written = radar.apply_review(packet, next_state, review, state)
                text = written[0].read_text()
                self.assertIn("not causality or incidence", text)
                self.assertIn("delete this queue file in the same commit", text)
                saved = json.loads(state.read_text())
                self.assertNotIn("pending_packet_sha256", saved["feeds"]["faers"])
        finally:
            radar.ROOT = original_root

    def test_monitor_retains_subject_and_rationale_in_compact_state(self):
        packet = self.packet()
        review = {
            "schema_version": 1,
            "reviewed_packet_sha256": packet["packet_sha256"],
            "reviewed_at": "2026-07-17T12:01:00Z",
            "reviewer_model": "test",
            "usage": {"cost_usd": 0.0},
            "decisions": [{
                "candidate_id": "faers-abc",
                "verdict": "monitor",
                "rationale": "Retain for another released quarter.",
                "headline": "",
                "why_actionable": "",
                "required_action": "",
                "evidence_boundary": "",
                "canonical_owner": "",
            }],
        }
        radar.with_hash(review, "review_sha256")
        next_state = {"schema_version": 1, "feeds": {"faers": {
            "pending_packet_sha256": packet["packet_sha256"],
            "pending_overflow_count": 0,
            "pending_advance_cursor_to": "2025Q4",
            "processing_window": ["2025Q4"],
        }}}
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state.json"
            radar.apply_review(packet, next_state, review, state)
            saved = json.loads(state.read_text())
        monitor = saved["feeds"]["faers"]["monitors"]["radar-faers-example"]
        self.assertEqual("EXAMPLE", monitor["subject"])
        self.assertEqual("Retain for another released quarter.", monitor["rationale"])

    def test_existing_unresolved_queue_item_is_never_overwritten(self):
        packet = self.packet()
        review = {
            "schema_version": 1,
            "reviewed_packet_sha256": packet["packet_sha256"],
            "reviewed_at": "2026-07-17T12:01:00Z",
            "reviewer_model": "test",
            "usage": {"cost_usd": 0.0},
            "decisions": [{
                "candidate_id": "faers-abc", "verdict": "queue", "rationale": "Open action.",
                "headline": "New headline", "why_actionable": "Actionable.",
                "required_action": "Verify it.", "evidence_boundary": "Noncausal.",
                "canonical_owner": "wiki/open-questions.md",
            }],
        }
        radar.with_hash(review, "review_sha256")
        next_state = {"schema_version": 1, "feeds": {"faers": {
            "pending_packet_sha256": packet["packet_sha256"],
        }}}
        original_root = radar.ROOT
        try:
            with tempfile.TemporaryDirectory() as tmp:
                radar.ROOT = Path(tmp)
                (radar.ROOT / "wiki").mkdir()
                (radar.ROOT / "wiki" / "open-questions.md").write_text("# Open\n")
                queue = radar.ROOT / "synthesis" / "queue" / "radar-faers-example.md"
                queue.parent.mkdir(parents=True)
                queue.write_text("existing unresolved action\n")
                with self.assertRaises(radar.RadarError):
                    radar.apply_review(packet, next_state, review, radar.ROOT / "state.json")
                self.assertEqual("existing unresolved action\n", queue.read_text())
        finally:
            radar.ROOT = original_root


class WorkflowContractTests(unittest.TestCase):
    def test_radar_is_delta_review_not_full_synthesis(self):
        workflow = (ROOT / ".github" / "workflows" / "evidence-radar.yml")
        if not workflow.exists():
            self.skipTest("workflow added in the same implementation batch")
        text = workflow.read_text()
        self.assertIn("evidence-radar.py collect", text)
        self.assertIn("evidence-radar.py review", text)
        self.assertIn("--prepare-only", text)
        self.assertIn("Review budget exhausted", text)
        self.assertNotIn("distributed-synthesis.py", text)
        self.assertNotIn("fresh-synthesis.py", text)


if __name__ == "__main__":
    unittest.main()
