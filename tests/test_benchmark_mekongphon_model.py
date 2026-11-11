import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / "scripts" / "benchmark_mekongphon_model.py"))
build_report = MODULE["build_report"]
codepoint_levenshtein = MODULE["codepoint_levenshtein"]


def test_mekongphon_report_is_source_attested_not_accuracy():
    rows = [
        {"orth": "ក", "pron_no_tones": "ka"},
        {"orth": "ខ", "pron_no_tones": "kʰa"},
    ]
    report = build_report(
        rows,
        ["ka", "kha"],
        model_revision="20e069d384b240da76320e1569958568c12a54bc",
        corpus_sha256="a" * 64,
    )

    assert report["input_count"] == 2
    assert report["successful_outputs"] == 2
    assert report["source_attested_diagnostic"]["strict_matches"] == 1
    assert report["source_attested_diagnostic"]["reference_codepoints"] == 5
    assert report["source_attested_diagnostic"]["character_errors"] == 1
    assert report["source_attested_diagnostic"]["codepoint_cer"] == 0.2
    assert report["independent_gold_count"] == 0
    assert report["accuracy"] is None
    assert report["score_status"] == "SOURCE_ATTESTED_DIAGNOSTIC_NOT_ACCURACY"
    assert "orth" not in report["records"][0]
    assert "reference" not in report["records"][0]
    assert report["records"][1]["raw_output"] == "kha"


def test_mekongphon_report_rejects_prediction_count_mismatch():
    rows = [{"orth": "ក", "pron_no_tones": "ka"}]
    try:
        build_report(rows, [], model_revision="revision", corpus_sha256="a" * 64)
    except ValueError as error:
        assert "one prediction per input" in str(error)
    else:
        raise AssertionError("expected a prediction-count error")


def test_codepoint_levenshtein_counts_insertions_deletions_and_substitutions():
    assert codepoint_levenshtein("kitten", "sitting") == 3
    assert codepoint_levenshtein("ŋ", "n") == 1
    assert codepoint_levenshtein("", "a") == 1
