"""Evidence-aware ensemble for Khmer → IPA research.

The ensemble never averages phone strings or treats a single model as gold.
Backends are injected so optional third-party engines remain out of the core
runtime dependency set. Only exact agreement between independent backends
produces a consensus IPA value.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict
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
            "structure": asdict(structure),
            "ipa": decision["ipa"],
            "ipa_status": decision["status"],
            "agreement": decision["agreement"],
            "candidates": candidates,
            "backend_failures": failures,
            "provenance_policy": "raw_outputs_preserved; no_model_is_gold; two_independent_votes_required",
        }


def make_mekongphon_backend(
    model_id: str = "byumatrixlab/khmer-ipa",
    revision: str = "20e069d384b240da76320e1569958568c12a54bc",
    *,
    num_beams: int = 4,
) -> Provider:
    """Create a lazy, cached CPU backend for the pinned MekongPhon model."""
    state: dict[str, Any] = {}

    def predict_one(text: str) -> dict[str, Any]:
        if not state:
            try:
                import torch
                from transformers import AutoTokenizer, EncoderDecoderModel
            except ImportError as exc:
                raise RuntimeError("Install optional torch and transformers to use MekongPhon") from exc
            torch.set_num_threads(1)
            torch.manual_seed(0)
            model = EncoderDecoderModel.from_pretrained(model_id, revision=revision).to("cpu")
            encoder = AutoTokenizer.from_pretrained(model_id, subfolder="encoder_tokenizer", revision=revision)
            decoder = AutoTokenizer.from_pretrained(model_id, subfolder="decoder_tokenizer", revision=revision)
            model.eval()
            state.update(torch=torch, model=model, encoder=encoder, decoder=decoder)
        torch = state["torch"]
        encoded = state["encoder"]([text], return_tensors="pt", padding=True, truncation=True, max_length=128)
        with torch.inference_mode():
            generated = state["model"].generate(**encoded, max_length=128, num_beams=num_beams, early_stopping=True)
        ipa = state["decoder"].decode(generated[0], skip_special_tokens=True)
        return {
            "ipa": ipa,
            "status": "candidate" if ipa.strip() else "unsupported",
            "provenance": {"engine": "byumatrixlab/khmer-ipa", "revision": revision, "num_beams": num_beams, "device": "cpu"},
        }

    return predict_one


def make_command_backend(command: list[str], *, engine_id: str) -> Provider:
    """Wrap a one-line command-line G2P that reads orthography on stdin and emits IPA on stdout."""
    import subprocess

    def run(text: str) -> dict[str, Any]:
        completed = subprocess.run(command, input=text + "\n", text=True, capture_output=True, check=True)
        ipa = completed.stdout.strip()
        return {"ipa": ipa, "status": "candidate" if ipa else "unsupported",
                "provenance": {"engine": engine_id, "command": command, "stderr": completed.stderr}}

    return run



def make_mekongphon_rule_backend(source_path: str) -> Provider:
    """Load the pinned upstream rule baseline without copying its source into this repo."""
    import hashlib
    import importlib.util
    from pathlib import Path

    path = Path(source_path).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location("mekongphon_khmer_rule_baseline", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load MekongPhon rule baseline: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    khmer2ipa = getattr(module, "khmer2ipa", None)
    if not callable(khmer2ipa):
        raise AttributeError("pinned MekongPhon rule baseline has no callable khmer2ipa")

    def run(text: str) -> dict[str, Any]:
        ipa = khmer2ipa(text, output="ipa")
        return {
            "ipa": ipa,
            "status": "candidate" if isinstance(ipa, str) and ipa.strip() else "unsupported",
            "provenance": {
                "engine": "MekongPhon rule-based Khmer→IPA baseline",
                "source_commit": "f80f6c1840c4818b51e05f2e00cded4701a5b662",
                "source_path": str(path),
                "source_sha256": digest,
                "output_mode": "ipa",
            },
        }

    return run

def create_hybrid_engine(providers: dict[str, Provider] | None = None) -> HybridKhmerEngine:
    return HybridKhmerEngine(providers)
