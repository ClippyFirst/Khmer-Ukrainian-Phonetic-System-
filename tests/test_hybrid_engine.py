from khmer_ua.hybrid import HybridKhmerEngine, combine_candidates, normalize_ipa


def test_consensus_requires_two_distinct_providers():
    candidates = [
        {"provider": "mekongphon", "ipa_normalized": "kʰmae", "ipa_raw": "/kʰmae/", "status": "candidate", "provenance": {}},
        {"provider": "rule-baseline", "ipa_normalized": "kʰmae", "ipa_raw": "kʰmae", "status": "candidate", "provenance": {}},
    ]
    result = combine_candidates(candidates)
    assert result == {"ipa": "kʰmae", "status": "ensemble_consensus", "agreement": 2}


def test_one_provider_never_becomes_consensus():
    result = combine_candidates([
        {"provider": "mekongphon", "ipa_normalized": "kʰmae", "ipa_raw": "kʰmae", "status": "candidate", "provenance": {}}
    ])
    assert result["ipa"] is None
    assert result["status"] == "single_engine_candidate"


def test_duplicate_provider_cannot_cast_two_votes():
    result = combine_candidates([
        {"provider": "model", "ipa_normalized": "kʰmae", "ipa_raw": "kʰmae", "status": "candidate", "provenance": {}},
        {"provider": "model", "ipa_normalized": "kʰmae", "ipa_raw": "/kʰmae/", "status": "candidate", "provenance": {}},
    ])
    assert result["agreement"] == 1
    assert result["ipa"] is None


def test_disagreement_withholds_ipa_and_preserves_candidates():
    engine = HybridKhmerEngine({
        "mekongphon": lambda _: "kʰmae",
        "rule-baseline": lambda _: "kʰmɛː",
    })
    result = engine.analyze("ខ្មែរ")
    assert result["ipa"] is None
    assert result["ipa_status"] == "engine_disagreement"
    assert len(result["candidates"]) == 2


def test_transport_normalization_does_not_remove_phone_diacritics():
    assert normalize_ipa(" /kʰmae/ ") == "kʰmae"
    assert normalize_ipa("kʰmae") != normalize_ipa("kmae")


def test_mekongphon_backend_is_lazy_and_pinned():
    from khmer_ua.hybrid import make_mekongphon_backend

    backend = make_mekongphon_backend()
    assert callable(backend)
    assert backend.__name__ == "predict_one"


def test_command_backend_preserves_ipa_stdout_and_provenance(monkeypatch):
    import subprocess
    from types import SimpleNamespace
    from khmer_ua.hybrid import make_command_backend

    monkeypatch.setattr(subprocess, "run", lambda command, input, **kwargs: SimpleNamespace(stdout="kʰmae\\n", stderr="diagnostic"))
    result = make_command_backend(["khmer-rule"], engine_id="rule-baseline")("ខ្មែរ")
    assert result["ipa"] == "kʰmae"
    assert result["provenance"]["engine"] == "rule-baseline"
