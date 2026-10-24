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


def test_khnhom_source_ipa_is_not_confused_with_orthographic_transcription():
    corpus = load_module().load_corpus(ROOT / "data" / "tests" / "verified-lexical-corpus.json")
    entry = corpus["ខ្ញុំ"]
    assert entry["ipa"] == "/kɲom/"
    assert entry["orthographic_transcription"] == "k̥ʰñuṃ"
    assert "not independently adjudicated" in entry["source_convention_note"].lower()

def test_source_ipa_notation_diagnostic_preserves_phonetic_distinctions():
    module = load_module()
    corpus = {
        "word": {
            "ipa": "/pʰiə.saː/",
            "evidence_status": "SOURCE_ATTESTED_NOT_INDEPENDENTLY_ADJUDICATED",
            "sources": ["https://example.invalid/source"],
        }
    }
    report = module.build_report(
        corpus,
        [{
            "input": "word",
            "raw_output": ["pʰ", "i", "ə", "s", "aː"],
            "phone_tokens": ["pʰ", "i", "ə", "s", "aː"],
            "source_reported_ipa": "/pʰiə.saː/",
            "error": None,
        }],
        package="khmerphonemizer",
        version="test",
        corpus_path="fixture.json",
        corpus_sha256="abc",
    )
    assert report["source_attested_diagnostic"]["strict_string_matches"] == 0
    assert report["source_attested_diagnostic"]["limited_notation_normalized_matches"] == 1
    assert report["independent_gold_count"] == 0
    assert report["accuracy"] is None
    assert report["records"][0]["source_ipa_diagnostic"]["status"] == "MATCH_AFTER_LIMITED_NOTATION_REMOVAL_NOT_GOLD"
    # Length and aspiration must remain contrastive in this diagnostic.
    assert module.source_ipa_comparison_key("/pʰaː/") != module.source_ipa_comparison_key("/pa/")
    assert module.source_ipa_comparison_key("/ta/") != module.source_ipa_comparison_key("/tʰa/")
