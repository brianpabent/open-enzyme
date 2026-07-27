#!/usr/bin/env python3
"""Fail-closed validation fixtures for comp-049."""

from __future__ import annotations

import copy
import unittest

import analyze


def observation() -> dict[str, object]:
    return {
        "mechanism_id": "FEUA",
        "target_or_endpoint": "fractional urate excretion",
        "effect_polarity": "increase",
        "endpoint_kind": "whole_animal_function",
        "compartment": "renal",
        "measurement_directness": "whole_organism_function",
        "target_attribution": "unattributed_system_function",
        "effect_scope": "reported_in_at_least_one_tested_group",
        "relevant_weaknesses": ["renal_urate_excretion"],
    }


class ValidationContractTests(unittest.TestCase):
    def test_duplicate_declared_weaknesses_fail(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate"):
            analyze.require_string_list(
                ["renal_urate_excretion", "renal_urate_excretion"],
                "gout_weakness",
                "fixture",
            )

    def test_duplicate_scoped_observations_fail(self) -> None:
        item = observation()
        with self.assertRaisesRegex(ValueError, "duplicate"):
            analyze.validate_observation_consistency(
                [item, copy.deepcopy(item)], "fixture"
            )

    def test_conflicting_scoped_polarities_fail(self) -> None:
        first = observation()
        second = copy.deepcopy(first)
        second["effect_polarity"] = "decrease"
        with self.assertRaisesRegex(ValueError, "conflicting"):
            analyze.validate_observation_consistency(
                [first, second], "fixture"
            )

    def test_incompatible_mechanism_compartment_fails(self) -> None:
        item = observation()
        item["compartment"] = "intestinal"
        with self.assertRaisesRegex(ValueError, "incompatible compartment"):
            analyze.validate_observation(item, "fixture")

    def test_incompatible_mechanism_weakness_fails(self) -> None:
        item = observation()
        item["relevant_weaknesses"] = ["urate_production"]
        with self.assertRaisesRegex(ValueError, "incompatible weakness"):
            analyze.validate_observation(item, "fixture")

    def test_no_change_scope_must_match_polarity(self) -> None:
        item = observation()
        item["effect_polarity"] = "no_change"
        with self.assertRaisesRegex(ValueError, "must agree"):
            analyze.validate_observation(item, "fixture")

    def test_feua_is_physiological_function_not_target_attribution(self) -> None:
        item = observation()
        self.assertTrue(
            analyze.observation_matches_weakness_function(
                item, "renal_urate_excretion"
            )
        )
        record = {
            "gout_weakness": ["renal_urate_excretion"],
            "mechanism_observations": [item],
        }
        self.assertEqual(
            analyze.missing_target_attribution_weaknesses(record),
            {"renal_urate_excretion"},
        )


if __name__ == "__main__":
    unittest.main()
