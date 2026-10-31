from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/khmer/romanization_vowels_ukrainian.csv"
ALLOWED = {"PROPOSED", "ANALYSIS_DEPENDENT", "EVIDENCE_LIMITED", "NOT_ESTABLISHED"}
EXPECTED = {"independent_vowel": 12, "dependent_vowel": 17, "vowel_diacritic_combination": 8}
SOURCE = "https://assets.publishing.service.gov.uk/media/5ab4e25aed915d78bc23451e/ROMANIZATION_OF_KHMER.pdf"


def test_pcgn_vowel_and_diacritic_crosswalk_is_complete_for_documented_tables():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == sum(EXPECTED.values())
    assert {section: sum(row["table_section"] == section for row in rows) for section in EXPECTED} == EXPECTED
    assert all(row["source_url"] == SOURCE for row in rows)
    assert all(row["source_locator"].startswith("Independent/Dependent Vowel") or row["source_locator"].startswith("Vowel Characters with Anusvara") for row in rows)
    table_rows = {int(row["table_row"]) for row in rows if row["table_section"] in {"independent_vowel", "dependent_vowel"}}
    assert table_rows == set(range(1, 23))
    assert all(row["ukrainian_status"] in ALLOWED for row in rows)
    assert all(row["bgn_pcgn_romanization"] and row["source_units"] and row["note"] for row in rows)
    assert len({(row["table_section"], row["table_row"]) for row in rows}) == len(rows)

    expected_source_units = {
        ("dependent_vowel", "1"): "◌",
        ("dependent_vowel", "2"): "◌ា",
        ("dependent_vowel", "3"): "◌ិ",
        ("dependent_vowel", "4"): "◌ី",
        ("dependent_vowel", "5"): "◌ឹ",
        ("dependent_vowel", "6"): "◌ឺ",
        ("dependent_vowel", "7"): "◌ុ",
        ("dependent_vowel", "8"): "◌ូ",
        ("dependent_vowel", "9"): "◌ួ",
        ("dependent_vowel", "10"): "េ◌ើ",
        ("dependent_vowel", "11"): "េ◌ឿ",
        ("dependent_vowel", "12"): "េ◌ៀ",
        ("dependent_vowel", "13"): "េ◌",
        ("dependent_vowel", "14"): "ែ◌",
        ("dependent_vowel", "15"): "ៃ◌",
        ("dependent_vowel", "16"): "េ◌ា",
        ("dependent_vowel", "17"): "េ◌ៅ",
        ("vowel_diacritic_combination", "1"): "◌ុ◌ំ",
        ("vowel_diacritic_combination", "2"): "◌ំ",
        ("vowel_diacritic_combination", "3"): "◌ំ឵",
        ("vowel_diacritic_combination", "4"): "◌ះ",
        ("vowel_diacritic_combination", "5"): "◌ុ◌ះ",
        ("vowel_diacritic_combination", "6"): "េ◌◌ះ",
        ("vowel_diacritic_combination", "7"): "េ◌឵ះ",
        ("vowel_diacritic_combination", "8"): "◌ំ឵ង",
    }
    for row in rows:
        expected = expected_source_units.get((row["table_section"], row["table_row"]))
        if expected is not None:
            assert row["source_units"] == expected


def test_unadjudicated_rows_never_claim_a_ukrainian_candidate():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        if row["ukrainian_status"] == "EVIDENCE_LIMITED":
            assert not row["ukrainian_candidate"]
