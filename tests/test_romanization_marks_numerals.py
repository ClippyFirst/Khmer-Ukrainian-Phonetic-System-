from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/khmer/romanization_marks_numerals.csv"
SOURCE = "https://assets.publishing.service.gov.uk/media/5ab4e25aed915d78bc23451e/ROMANIZATION_OF_KHMER.pdf"
ALLOWED = {"ESTABLISHED", "PROPOSED", "ANALYSIS_DEPENDENT", "EVIDENCE_LIMITED"}


def test_pcgn_diacritics_and_numerals_have_explicit_rows():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 16
    assert sum(row["table_section"] == "diacritical_mark" for row in rows) == 6
    assert sum(row["table_section"] == "numeral" for row in rows) == 10
    assert all(row["source_url"] == SOURCE for row in rows)
    assert all(row["ukrainian_status"] in ALLOWED for row in rows)
    assert all(row["source_units"] and row["source_locator"] and row["note"] for row in rows)
    assert [row["ukrainian_candidate"] for row in rows if row["table_section"] == "numeral"] == list("0123456789")
    expected_marks = {
        "1": "◌៊",
        "2": "◌៉",
        "3": "◌់",
        "4": "◌៌",
        "5": "◌៏",
        "6": "◌៍",
    }
    actual_marks = {
        row["table_row"]: row["source_units"]
        for row in rows
        if row["table_section"] == "diacritical_mark"
    }
    assert actual_marks == expected_marks
    assert [row["source_units"] for row in rows if row["table_section"] == "numeral"] == list("០១២៣៤៥៦៧៨៩")
    silent = next(row for row in rows if row["table_section"] == "diacritical_mark" and row["table_row"] == "6")
    assert silent["bgn_pcgn_romanization"] == "omitted"
    assert silent["ukrainian_status"] == "ESTABLISHED"
