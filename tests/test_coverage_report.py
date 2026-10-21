import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "khmer-coverage-audit.json"
SCRIPT = ROOT / "scripts" / "coverage.py"


def test_coverage_report_is_generated_and_in_sync():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    inventory = report["orthographic_inventory"]
    summary = report["coverage_summary"]
    cells = report["dependent_vowel_by_series"]

    assert inventory["dependent_vowel_signs"] > 0
    assert inventory["independent_vowel_signs"] > 0
    assert inventory["expected_dependent_vowel_x_series_cells"] == (
        inventory["dependent_vowel_signs"] * 2
    )
    assert len(cells) == inventory["expected_dependent_vowel_x_series_cells"]
    assert set(summary) >= {
        "source_attested_not_gold_cells",
        "conflicting_cells",
        "not_established_cells",
        "coverage_fraction",
    }
    assert (
        summary["source_attested_not_gold_cells"]
        + summary["conflicting_cells"]
        + summary["not_established_cells"]
        == len(cells)
    )
    assert all(
        cell["status"] in {
            "SOURCE_ATTESTED_NOT_GOLD",
            "CONFLICTING_SOURCE_ANALYSES",
            "NOT_ESTABLISHED",
        }
        for cell in cells.values()
    )
    assert report["source_conflict_case_ids"]
    assert report["interpretation"].find("never gold") >= 0


def test_conflicting_source_cases_are_not_lost_from_coverage_summary():
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    registry = json.loads(
        (ROOT / "data" / "khmer" / "vowel-context-register.json").read_text(encoding="utf-8")
    )
    expected = sorted(
        case["id"]
        for case in registry["cases"]
        if case.get("status") == "CONFLICTING_SOURCE_ANALYSES"
    )
    assert sorted(report["source_conflict_case_ids"]) == expected


def test_coverage_matrix_never_fabricates_ipa_for_unestablished_cells():
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    for cell in report["dependent_vowel_by_series"].values():
        if cell["status"] == "NOT_ESTABLISHED":
            assert cell["ipa_values"] == []
