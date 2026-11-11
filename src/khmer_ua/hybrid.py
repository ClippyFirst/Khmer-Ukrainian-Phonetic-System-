"""Research hybrid wrapper: deterministic rules remain authoritative.

External G2P systems are integrated as inspectable candidate sources only.
No model voting or automatic IPA promotion is performed without profile-matched
independent adjudication.
"""
from __future__ import annotations
from typing import Any, Callable
from .rule_engine import RuleBasedKhmerEngine

Provider = Callable[[str], str | dict[str, Any]]

PROVIDER_PRIORITY = {
    "mekongphon": 10,
    "khmer-phonemizer": 20,
    "khmer_phonemizer": 20,
    "epitran": 30,
    "goruut": 90,
}
DEFAULT_PROVIDER_PRIORITY = 50


def normalize_ipa_transport(value: str) -> str:
    value = value.strip()
    if value.startswith("/") and value.endswith("/") and len(value) > 1:
        value = value[1:-1]
    elif value.startswith("[") and value.endswith("]") and len(value) > 1:
        value = value[1:-1]
    return " ".join(value.split())

def _candidate(provider_id: str, raw: Any) -> dict[str, Any] | None:
    if isinstance(raw, str):
        ipa, status, provenance = raw, "candidate", {}
    elif isinstance(raw, dict):
        ipa, status, provenance = raw.get("ipa"), raw.get("status", "candidate"), raw.get("provenance", {})
    else:
        return None
    if status in {"error", "unsupported", "not_established", "analysis_dependent"}:
        return None
    if not isinstance(ipa, str) or not normalize_ipa_transport(ipa) or "?" in ipa:
        return None
    return {
        "provider": provider_id, "priority": PROVIDER_PRIORITY.get(provider_id, DEFAULT_PROVIDER_PRIORITY), "ipa_raw": ipa,
        "ipa_transport_normalized": normalize_ipa_transport(ipa),
        "status": status, "provenance": provenance if isinstance(provenance, dict) else {},
        "promotion": "WITHHELD_PENDING_INDEPENDENT_PROFILE_MATCHED_ADJUDICATION",
    }

class HybridKhmerEngine:
    """Run deterministic rules plus optional independent Khmer→IPA candidates."""
    def __init__(self, providers: dict[str, Provider] | None = None,
                 rule_engine: RuleBasedKhmerEngine | None = None):
        self.providers = dict(providers or {})
        self.rule_engine = rule_engine or RuleBasedKhmerEngine()

    def analyze(self, text: str) -> dict[str, Any]:
        result = dict(self.rule_engine.analyze(text))
        candidates, failures = [], []
        normalized = result.get("normalized", text)
        for provider_id, provider in sorted(self.providers.items(), key=lambda item: (PROVIDER_PRIORITY.get(item[0], DEFAULT_PROVIDER_PRIORITY), item[0])):
            try:
                item = _candidate(provider_id, provider(normalized))
                if item is None:
                    failures.append({"provider": provider_id, "reason": "NO_TYPED_COMPLETE_IPA"})
                else:
                    candidates.append(item)
            except Exception as exc:
                failures.append({"provider": provider_id, "reason": type(exc).__name__})
        result.update({
            "hybrid_engine": "khmer-evidence-gated-hybrid-v1",
            "external_candidates": candidates, "backend_failures": failures,
            "external_candidate_count": len(candidates),
            "provider_priority_policy": "lower_number_runs_first_and_orders_candidates; priorities_are_research_triage_only_not_accuracy_or_promotion; unknown_providers_use_default_priority_50",
            "selection_policy": "internal_deterministic_rule_output_is_preserved; external_candidates_are_diagnostic_only; no_voting_or_promotion_without_independent_profile_matched_gold",
        })
        return result

def make_mekongphon_backend(model_id: str = "byumatrixlab/khmer-ipa",
                            revision: str = "20e069d384b240da76320e1569958568c12a54bc",
                            *, num_beams: int = 4) -> Provider:
    """Lazy, pinned CPU inference adapter; torch/transformers stay optional."""
    state: dict[str, Any] = {}
    def predict(text: str) -> dict[str, Any]:
        if not state:
            try:
                import torch
                from transformers import AutoTokenizer, EncoderDecoderModel
            except ImportError as exc:
                raise RuntimeError("Install optional torch and transformers for MekongPhon") from exc
            torch.set_num_threads(1)
            torch.manual_seed(0)
            model = EncoderDecoderModel.from_pretrained(model_id, revision=revision).to("cpu")
            encoder = AutoTokenizer.from_pretrained(model_id, subfolder="encoder_tokenizer", revision=revision)
            decoder = AutoTokenizer.from_pretrained(model_id, subfolder="decoder_tokenizer", revision=revision)
            model.eval()
            state.update(torch=torch, model=model, encoder=encoder, decoder=decoder)
        encoded = state["encoder"]([text], return_tensors="pt", padding=True, truncation=True, max_length=128)
        with state["torch"].inference_mode():
            generated = state["model"].generate(**encoded, max_length=128, num_beams=num_beams, early_stopping=True)
        ipa = state["decoder"].decode(generated[0], skip_special_tokens=True)
        return {"ipa": ipa, "status": "candidate" if ipa.strip() else "unsupported",
                "provenance": {"engine": "byumatrixlab/khmer-ipa", "revision": revision,
                               "device": "cpu", "num_beams": num_beams,
                               "training_split_independence": "NOT_ESTABLISHED",
                               "tone_coverage": "NOT_EVALUATED_BY_pron_no_tones"}}
    return predict

def make_command_backend(command: list[str], *, engine_id: str, revision: str) -> Provider:
    """Adapter for pinned Goruut/Epitran/Khmer Phonemizer CLI wrappers."""
    import subprocess
    def run(text: str) -> dict[str, Any]:
        completed = subprocess.run(command, input=text + "\n", text=True, capture_output=True, check=True)
        ipa = completed.stdout.strip()
        return {"ipa": ipa, "status": "candidate" if ipa else "unsupported",
                "provenance": {"engine": engine_id, "revision": revision, "stderr": completed.stderr}}
    return run

def create_hybrid_engine(providers: dict[str, Provider] | None = None) -> HybridKhmerEngine:
    return HybridKhmerEngine(providers=providers)
