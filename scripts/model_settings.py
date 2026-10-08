#!/usr/bin/env python3
"""Offline, versioned model/role settings. Never discovers or invokes models."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Any

REGISTRY_PATH = Path(__file__).with_name("model-settings.json")


class ModelSettingsError(ValueError):
    """Unverified model, incompatible request, or invalid registry/budget."""


def nonnegative(value: Any, name: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ModelSettingsError(f"{name} must be a finite number")
    if not math.isfinite(value) or value < 0 or (positive and value == 0):
        raise ModelSettingsError(f"{name} must be finite and {'positive' if positive else 'nonnegative'}")
    return float(value)


def positive_int(value: Any, name: str) -> int:
    number = nonnegative(value, name, positive=True)
    if int(number) != number:
        raise ModelSettingsError(f"{name} must be an integer")
    return int(number)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ModelSettingsError(f"Duplicate registry key: {key}")
        result[key] = value
    return result


def validate_registry(data: dict[str, Any]) -> None:
    if data.get("schema_version") != 1:
        raise ModelSettingsError("Unsupported model registry schema_version")
    models, roles = data.get("models"), data.get("roles")
    if not isinstance(models, dict) or not models or not isinstance(roles, dict) or not roles:
        raise ModelSettingsError("Model registry requires models and roles")
    for name, spec in models.items():
        if not isinstance(name, str) or not name or not isinstance(spec, dict):
            raise ModelSettingsError("Model entries must be named objects")
        if spec.get("transport") not in {"openrouter_chat", "anthropic_cli"}:
            raise ModelSettingsError(f"Unsupported transport for {name}")
        if not spec.get("sources") or not spec.get("verified_on"):
            raise ModelSettingsError(f"Missing verification provenance for {name}")
        for field in ("context_tokens", "maximum_input_tokens", "maximum_output_tokens"):
            positive_int(spec.get(field), f"{name}.{field}")
        if spec["maximum_input_tokens"] > spec["context_tokens"] or spec["maximum_output_tokens"] > spec["context_tokens"]:
            raise ModelSettingsError(f"Invalid context/output bounds for {name}")
        prices = spec.get("prices_usd_per_million_tokens", {})
        for field in ("input", "output"):
            nonnegative(prices.get(field), f"{name}.price.{field}", positive=True)
        for field, value in prices.items():
            nonnegative(value, f"{name}.price.{field}")
        last_threshold = -1
        for tier in spec.get("pricing_tiers", []):
            threshold = positive_int(tier.get("above_input_tokens"), f"{name}.tier.threshold")
            if threshold <= last_threshold:
                raise ModelSettingsError(f"Unordered pricing tiers for {name}")
            last_threshold = threshold
            for field in ("input", "output"):
                nonnegative(tier.get(field), f"{name}.tier.{field}", positive=True)
        if not isinstance(spec.get("supported_parameters"), list) or not all(isinstance(parameter, str) for parameter in spec["supported_parameters"]):
            raise ModelSettingsError(f"Missing supported parameters for {name}")
        if spec["transport"] == "openrouter_chat":
            if not spec.get("provider_tags") or not spec.get("provider_rate_limits"):
                raise ModelSettingsError(f"Missing verified routing/rate limits for {name}")
            for field, price_field in (("prompt", "input"), ("completion", "output")):
                value = spec["provider_rate_limits"].get(field)
                nonnegative(value, f"{name}.provider.{field}", positive=True)
                if value != prices[price_field]:
                    raise ModelSettingsError(f"Detached provider and planning prices for {name}")
    for name, config in roles.items():
        if not isinstance(config, dict):
            raise ModelSettingsError(f"Role {name} must be an object")
        selected = list((config.get("models") or {}).values())
        if config.get("model") is not None:
            selected.append(config["model"])
        for model in selected:
            if model not in models:
                raise ModelSettingsError(f"Unknown model {model!r} selected by role {name}")
            if models[model]["transport"] != config.get("transport"):
                raise ModelSettingsError(f"Role {name} selects an incompatible model transport")
        for field in ("max_cost_usd", "aggregate_max_cost_usd"):
            if config.get(field) is not None:
                nonnegative(config[field], f"{name}.{field}", positive=True)
        if config.get("aggregate_max_cost_usd", math.inf) < (config.get("max_cost_usd") or 0):
            raise ModelSettingsError(f"Aggregate budget is below per-artifact budget for {name}")
        outputs = config.get("output_tokens")
        for value in (outputs.values() if isinstance(outputs, dict) else [outputs]):
            if value is not None:
                positive_int(value, f"{name}.output_tokens")
                if any(value > models[model]["maximum_output_tokens"] for model in selected):
                    raise ModelSettingsError(f"Role {name} exceeds a selected model's output limit")
        for field in ("minimum_output_tokens", "maximum_output_tokens", "output_tokens_per_candidate", "max_iterations", "workflow_max_iterations"):
            if field in config:
                positive_int(config[field], f"{name}.{field}")
        if "output_token_overhead" in config:
            nonnegative(config["output_token_overhead"], f"{name}.output_token_overhead")
            if not isinstance(config["output_token_overhead"], int):
                raise ModelSettingsError(f"{name}.output_token_overhead must be an integer")
        if "maximum_output_tokens" in config and any(config["maximum_output_tokens"] > models[model]["maximum_output_tokens"] for model in selected):
            raise ModelSettingsError(f"Role {name} exceeds a selected model's output limit")
        if config.get("minimum_output_tokens", 0) > config.get("maximum_output_tokens", math.inf):
            raise ModelSettingsError(f"Role {name} has reversed output limits")
        if "temperature" in config:
            value = nonnegative(config["temperature"], f"{name}.temperature")
            if value > 2:
                raise ModelSettingsError(f"Invalid temperature for {name}")


def load_registry(path: Path = REGISTRY_PATH) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(), object_pairs_hook=_unique_object)
    except (OSError, json.JSONDecodeError) as exc:
        raise ModelSettingsError(f"Cannot load versioned model registry: {exc}") from exc
    if not isinstance(data, dict):
        raise ModelSettingsError("Model registry must be an object")
    validate_registry(data)
    return data


@lru_cache(maxsize=1)
def _registry() -> dict[str, Any]:
    return load_registry()


def registry_sha256() -> str:
    return hashlib.sha256(REGISTRY_PATH.read_bytes()).hexdigest()


def role(name: str) -> dict[str, Any]:
    try:
        return copy.deepcopy(_registry()["roles"][name])
    except KeyError as exc:
        raise ModelSettingsError(f"Unknown model role: {name}") from exc


def model(name: str, *, transport: str | None = None) -> dict[str, Any]:
    try:
        spec = _registry()["models"][name]
    except (KeyError, TypeError) as exc:
        raise ModelSettingsError(f"Unknown or unverified model {name!r}; update model-settings.json before use") from exc
    if transport is not None and spec["transport"] != transport:
        raise ModelSettingsError(f"{name} requires {spec['transport']}, not {transport}")
    return copy.deepcopy(spec)


def token_rates(name: str, input_tokens: float = 0) -> dict[str, float]:
    nonnegative(input_tokens, "input_tokens")
    spec = model(name)
    rates = dict(spec["prices_usd_per_million_tokens"])
    for tier in spec["pricing_tiers"]:
        if input_tokens > tier["above_input_tokens"]:
            rates.update({k: v for k, v in tier.items() if k != "above_input_tokens"})
    return rates


def estimate_cost(name: str, input_tokens: float, output_tokens: float, *, prompt_cache: bool = False) -> float:
    nonnegative(output_tokens, "output_tokens")
    rates = token_rates(name, input_tokens)
    input_rate = rates["input"]
    if prompt_cache:
        input_rate = max(input_rate, rates.get("cache_write_5m", input_rate), rates.get("cache_write_1h", input_rate))
    return (input_tokens * input_rate + output_tokens * rates["output"]) / 1_000_000


def usage_cost(name: str, usage: dict[str, Any], *, prompt_cache: bool = False) -> tuple[float, bool]:
    model(name, transport="openrouter_chat")
    if usage.get("cost") is not None:
        return nonnegative(usage["cost"], "provider usage.cost"), False
    inputs = nonnegative(usage.get("prompt_tokens", 0), "usage.prompt_tokens")
    outputs = nonnegative(usage.get("completion_tokens", 0), "usage.completion_tokens")
    # Without a billed receipt, do not assume cache savings or omit writes.
    return estimate_cost(name, inputs, outputs, prompt_cache=prompt_cache), True


def validate_context(name: str, input_tokens: float, output_tokens: int, *, margin: int = 0) -> None:
    spec = model(name, transport="openrouter_chat")
    nonnegative(input_tokens, "input_tokens")
    nonnegative(margin, "context margin")
    output = positive_int(output_tokens, "max_tokens")
    if output > spec["maximum_output_tokens"]:
        raise ModelSettingsError(f"{name} output {output} exceeds verified limit {spec['maximum_output_tokens']}")
    if input_tokens > spec["maximum_input_tokens"] or input_tokens + output + margin > spec["context_tokens"]:
        raise ModelSettingsError(f"Request estimate exceeds {name}'s verified context/input limit")


def chat_body(body: dict[str, Any], *, margin: int = 0) -> dict[str, Any]:
    """Validate before transport; omit only unsupported sampling defaults.

    Context uses a character/4 planning proxy, not a native-token guarantee.
    Verified rate filters reject more expensive/unsupported provider routes.
    They are unit-price filters, not a total-spend or retry reservation.
    """
    result = copy.deepcopy(body)
    name = result.get("model")
    spec = model(name, transport="openrouter_chat")
    supported = set(spec["supported_parameters"])
    if not isinstance(result.get("messages"), list) or not result["messages"]:
        raise ModelSettingsError("Chat request requires messages")
    for sampler in ("temperature", "top_p", "top_k"):
        if sampler in result and sampler not in supported:
            result.pop(sampler)
    for field in ("tools", "tool_choice", "reasoning", "response_format", "temperature", "top_p", "top_k"):
        if field in result and field not in supported:
            raise ModelSettingsError(f"{name} does not support required parameter {field}")
    if "temperature" in result and nonnegative(result["temperature"], "temperature") > 2:
        raise ModelSettingsError("Invalid temperature")
    if result.get("response_format", {}).get("type") == "json_schema" and "structured_outputs" not in supported:
        raise ModelSettingsError(f"{name} has no verified strict structured-output support")
    if result.get("reasoning", {}).get("effort") not in {None, "none", "minimal", "low", "medium", "high", "xhigh", "max"}:
        raise ModelSettingsError("Invalid reasoning effort")
    result["provider"] = {
        "only": spec["provider_tags"],
        "require_parameters": True,
        "allow_fallbacks": False,
        "max_price": spec["provider_rate_limits"],
    }
    estimate = len(json.dumps(result, ensure_ascii=False)) / 4
    # Long-context pricing is a property of this exact model, not an override
    # of its budget or selection. Use the same tier in routing and planning.
    rates = token_rates(name, estimate)
    result["provider"]["max_price"] = {"prompt": rates["input"], "completion": rates["output"]}
    estimate = len(json.dumps(result, ensure_ascii=False)) / 4
    validate_context(name, estimate, result.get("max_tokens"), margin=margin)
    return result


def workflow_environment(name: str, overrides: dict[str, str] | None = None) -> dict[str, str]:
    config = role(name)
    mapping = config.get("workflow_env", {})
    overrides = overrides or {}
    if set(overrides) - set(mapping):
        raise ModelSettingsError(f"Unsupported workflow override for {name}")
    values: dict[str, str] = {}
    for variable, field in mapping.items():
        value = config[field]
        supplied = overrides.get(variable, "").strip()
        if supplied:
            if field not in {"max_cost_usd", "aggregate_max_cost_usd"}:
                raise ModelSettingsError(f"Workflow cannot override {variable}")
            try:
                value = float(supplied)
            except ValueError as exc:
                raise ModelSettingsError(f"Invalid budget override {variable}") from exc
            nonnegative(value, variable, positive=True)
        if isinstance(value, str):
            model(value)
        values[variable] = str(value)
    if "PER_COMP_CAP" in values and float(values["PER_COMP_CAP"]) > float(values["AGGREGATE_CAP"]):
        raise ModelSettingsError("Per-COMP cap exceeds aggregate cap")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    show = sub.add_parser("role")
    show.add_argument("name")
    show.add_argument("--field")
    env = sub.add_parser("env")
    env.add_argument("name")
    env.add_argument("--override", action="append", default=[])
    args = parser.parse_args()
    if args.command == "check":
        data = load_registry()
        print(f"Model settings valid: {len(data['roles'])} roles, {len(data['models'])} verified models")
    elif args.command == "role":
        value = role(args.name)
        if args.field:
            for key in args.field.split("."):
                value = value[key]
        print(value if isinstance(value, (str, int, float)) else json.dumps(value, sort_keys=True))
    else:
        overrides: dict[str, str] = {}
        for entry in args.override:
            key, separator, value = entry.partition("=")
            if not separator or key in overrides:
                raise ModelSettingsError("Workflow overrides must be unique NAME=value entries")
            overrides[key] = value
        for key, value in workflow_environment(args.name, overrides).items():
            print(f"{key}={value}")


if __name__ == "__main__":
    try:
        main()
    except (ModelSettingsError, KeyError) as exc:
        raise SystemExit(f"model-settings: {exc}") from exc
