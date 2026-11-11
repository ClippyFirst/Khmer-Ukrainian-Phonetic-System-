"""Evidence-aware ensemble for Khmer → IPA research.

The ensemble never averages phone strings or treats a single model as gold.
Backends are injected so optional third-party engines remain out of the core
runtime dependency set. Only exact agreement between independent backends
produces a consensus IPA value.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable, Iterable

from .parser import analyze

Provider = Callable[[str], str | dict[str, Any]]


def normalize_ipa(value: str) -> str:
    """Normalize only transport notation; preserve phonemic distinctions."""
    value = value.strip()
    if value.startswith("/") and value.endswith("/") and len(value) > 1:
        value = value[1:-1]
    if value.startswith("[") and value.endswith("]") and len(value) > 1:
        value = value[1:-1]
    return " ".join(value.split())


def _candidate(provider_id: str, raw: str | dict[str, Any]) -> dict[str, Any] | None:
    if isinstance(raw, str):
        ipa, status, provenance = raw, "candidate", {}
    elif isinstance(raw, dict):
        ipa = raw.get("ipa")
        status = raw.get("status", "candidate")
        provenance = raw.get("provenance", {})
    else:
        return None
    if not isinstance(ipa, str) or not normalize_ipa(ipa) or "?" in ipa:
        return None
    if status in {"error", "unsupported", "not_established", "analysis_dependent"}:
        return None
    return {
        "provider": provider_id,
        "ipa_raw": ipa,
        "ipa_normalized": normalize_ipa(ipa),
        "status": status,
        "provenance": provenance if isinstance(provenance, dict) else {},
    }


def combine_candidates(candidates: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Return consensus only when at least two distinct backends agree."""
    by_ipa: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in candidates:
        by_ipa[item["ipa_normalized"]].append(item)
    ranked = sorted(by_ipa.items(), key=lambda pair: (-len({x["provider"] for x in pair[1]}), pair[0]))
    if not ranked:
        return {"ipa": None, "status": "no_ipa_candidate", "agreement": 0}
    best_ipa, best = ranked[0]
    votes = len({item["provider"] for item in best})
    if votes >= 2 and (len(ranked) == 1 or votes > len({x["provider"] for x in ranked[1][1]})):
        return {"ipa": best_ipa, "status": "ensemble_consensus", "agreement": votes}
    return {
        "ipa": None,
        "status": "engine_disagreement" if len(ranked) > 1 else "single_engine_candidate",
        "agreement": votes,
    }


class HybridKhmerEngine:
    """Combine internal orthographic analysis with independent Khmer IPA backends."""

    def __init__(self, providers: dict[str, Provider] | None = None):
        self.providers = providers or {}

    def analyze(self, text: str) -> dict[str, Any]:
        structure = analyze(text)
        candidates = []
        failures = []
        for provider_id, provider in self.providers.items():
            try:
                item = _candidate(provider_id, provider(text))
                if item is not None:
                    candidates.append(item)
                else:
                    failures.append({"provider": provider_id, "reason": "empty_or_untyped_ipa"})
            except Exception as exc:  # backend failure must not erase other evidence
                failures.append({"provider": provider_id, "reason": type(exc).__name__, "message": str(exc)})
        decision = combine_candidates(candidates)
        return {
            "input": text,
            "profile": "khmer-pph-careful-citation-v1",
            "structure": structure.to_dict() if hasattr(structure, "to_dict") else structure,
            "ipa": decision["ipa"],
            "ipa_status": decision["status"],
            "agreement": decision["agreement"],
            "candidates": candidates,
            "backend_failures": failures,
            "provenance_policy": "raw_outputs_preserved; no_model_is_gold; two_independent_votes_required",
        }


def create_hybrid_engine(providers: dict[str, Provider] | None = None) -> HybridKhmerEngine:
    return HybridKhmerEngine(providers)
