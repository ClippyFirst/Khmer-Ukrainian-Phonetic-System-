from khmer_ua.hybrid import HybridKhmerEngine, normalize_ipa_transport
from khmer_ua.rule_engine import RuleBasedKhmerEngine

def test_external_candidate_is_preserved_but_not_promoted():
    result = HybridKhmerEngine({"mekongphon": lambda _: {"ipa": "kʰmae"}}).analyze("ខ្មែរ")
    assert result["external_candidates"][0]["ipa_raw"] == "kʰmae"
    assert result["external_candidates"][0]["promotion"].startswith("WITHHELD")
    assert result["selection_policy"].startswith("internal_deterministic_rule_output")

def test_partial_candidate_is_rejected():
    result = HybridKhmerEngine({"partial": lambda _: "k?mae"}).analyze("ខ្មែរ")
    assert result["external_candidates"] == []
    assert result["backend_failures"][0]["reason"] == "NO_TYPED_COMPLETE_IPA"

def test_backend_failure_does_not_erase_internal_result():
    result = HybridKhmerEngine({"broken": lambda _: (_ for _ in ()).throw(RuntimeError())}).analyze("ខ្មែរ")
    assert result["backend_failures"][0]["reason"] == "RuntimeError"
    assert "ipa" in result

def test_transport_normalization_preserves_phone_features():
    assert normalize_ipa_transport("/kʰmae/") == "kʰmae"
    assert normalize_ipa_transport("kʰmae") != normalize_ipa_transport("kmae")

def test_command_backend_preserves_candidate_and_revision(monkeypatch):
    import subprocess
    from types import SimpleNamespace
    from khmer_ua.hybrid import make_command_backend
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: SimpleNamespace(stdout="kʰmae\\n", stderr=""))
    candidate = make_command_backend(["goruut"], engine_id="goruut", revision="PINNED")("ខ្មែរ")
    assert candidate["ipa"] == "kʰmae"
    assert candidate["provenance"]["revision"] == "PINNED"
