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
    assert all(row["source_locator"].startswith("Independent Vowel") or row["source_locator"].startswith("Dependent Vowel") or row["source_locator"].startswith("Vowels with Anusvara") for row in rows)
    assert all(row["ukrainian_status"] in ALLOWED for row in rows)
    assert all(row["bgn_pcgn_romanization"] and row["source_units"] and row["note"] for row in rows)
    assert len({(row["table_section"], row["table_row"]) for row in rows}) == len(rows)


def test_unadjudicated_rows_never_claim_a_ukrainian_candidate():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        if row["ukrainian_status"] == "EVIDENCE_LIMITED":
            assert not row["ukrainian_candidate"]
