import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "benchmark_g2p.py"


def load_module():
    spec = importlib.util.spec_from_file_location("khmer_external_g2p_benchmark", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_benchmark_is_diagnostic_and_never_scores_source_attested_ipa_as_gold(tmp_path):
    module = load_module()
    corpus = {
        "ខ្មែរ": {
            "ipa": "/kʰmae/",
            "evidence_status": "SOURCE_ATTESTED_NOT_INDEPENDENTLY_ADJUDICATED",
            "sources": ["https://example.invalid/source"],
        }
    }
    report = module.build_report(
        corpus,
        [{"input": "ខ្មែរ", "raw_output": ["kʰ", "m", "ae"], "error": None}],
        package="khmerphonemizer",
        version="test",
        corpus_path="fixture.json",
        corpus_sha256="abc",
    )
    assert report["independent_gold_count"] == 0
    assert report["accuracy"] is None
    assert report["successful_outputs"] == 1
    assert "not gold" in report["interpretation"]


def test_phone_tokens_preserve_external_segments_without_ipa_rewriting():
    module = load_module()
    assert module.phoneme_tokens(["kʰ", "m", "ae"]) == ["kʰ", "m", "ae"]
    assert module.phoneme_tokens("kʰmae") == ["kʰmae"]
    assert module.phoneme_tokens(["kʰ", 3]) is None


def test_corpus_loader_requires_a_nonempty_object(tmp_path):
    module = load_module()
    path = tmp_path / "empty.json"
    path.write_text("{}", encoding="utf-8")
    try:
        module.load_corpus(path)
    except ValueError:
        pass
    else:
        raise AssertionError("empty corpus should be rejected")
