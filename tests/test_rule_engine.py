from khmer_ua.rule_engine import RuleBasedKhmerEngine
from khmer_ua.hybrid import HybridKhmerEngine


def test_lexical_fixture_uses_fixed_ipa_and_ukrainian_policy():
    result = RuleBasedKhmerEngine().analyze("ខ្មែរ")
    assert result["ipa"] == "kʰmae"
    assert result["ukrainian"] == "к'мае"
    assert result["deterministic"] is True
    assert result["engine"] == "khmer-deterministic-rules-v1"


def test_known_negative_fixture_withholds_ipa():
    result = RuleBasedKhmerEngine().analyze("ស៊៉ា")
    assert result["ipa"] is None
    assert result["status"] == "EVIDENCE_LIMITED"


def test_rule_fallback_is_repeatable_and_explicitly_proposed():
    engine = RuleBasedKhmerEngine()
    first = engine.analyze("ឆ")
    second = engine.analyze("ឆ")
    assert first == second
    assert first["ipa"] == "cʰɑː"
    assert first["status"] == "PROPOSED"
    assert "KHMER_REGISTER_SERIES_INHERENT_VOWEL" in first["rule_trace"]


def test_unknown_mixed_material_is_not_guessed():
    result = RuleBasedKhmerEngine().analyze("កx")
    assert result["ipa"] is None
    assert result["status"] == "NOT_ESTABLISHED"


def test_hybrid_wraps_rule_engine_without_changing_final_ipa():
    baseline = RuleBasedKhmerEngine().analyze("ខ្មែរ")
    result = HybridKhmerEngine().analyze("ខ្មែរ")
    assert result["ipa"] == baseline["ipa"]
    assert result["ukrainian"] == baseline["ukrainian"]
    assert result["external_candidates"] == []


def test_hybrid_factory_accepts_candidates_but_does_not_promote_them():
    from khmer_ua import create_hybrid_engine
    baseline = RuleBasedKhmerEngine().analyze("ខ្មែរ")
    result = create_hybrid_engine({"external-model": lambda _: "kʰmae"}).analyze("ខ្មែរ")
    assert result["ipa"] == baseline["ipa"]
    assert result["external_candidates"][0]["provider"] == "external-model"
    assert result["external_candidates"][0]["promotion"].startswith("WITHHELD")
