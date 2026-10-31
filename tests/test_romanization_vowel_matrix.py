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

    expected_romanization = {
        ("independent_vowel", "3"): ("ឥ", "ĕ"),
        ("independent_vowel", "4"): ("ឦ", "ei"),
        ("independent_vowel", "7"): ("ឧ", "ŏ / ŭ"),
        ("independent_vowel", "14"): ("ឯ", "ê"),
        ("independent_vowel", "15"): ("ឰ", "ai"),
        ("independent_vowel", "16"): ("ឱ|ឲ", "aô"),
        ("independent_vowel", "17"): ("ឳ", "au"),
        ("independent_vowel", "18"): ("ឪ", "âu"),
        ("independent_vowel", "19"): ("ឫ", "rœ̆"),
        ("independent_vowel", "20"): ("ឬ", "rœ"),
        ("independent_vowel", "21"): ("ឭ", "lœ̆"),
        ("independent_vowel", "22"): ("ឮ", "lœ"),
        ("dependent_vowel", "1"): ("◌", "â / ô; shortened á / ó"),
        ("dependent_vowel", "2"): ("◌ា", "a / éa; shortened ă / eă or oă"),
        ("dependent_vowel", "3"): ("◌ិ", "ĕ / ĭ"),
        ("dependent_vowel", "4"): ("◌ី", "ei / i"),
        ("dependent_vowel", "5"): ("◌ឹ", "œ̆"),
        ("dependent_vowel", "6"): ("◌ឺ", "œ"),
        ("dependent_vowel", "7"): ("◌ុ", "ŏ / ŭ"),
        ("dependent_vowel", "8"): ("◌ូ", "o / u"),
        ("dependent_vowel", "9"): ("◌ួ", "uŏ"),
        ("dependent_vowel", "10"): ("េ◌ើ", "aeu / eu"),
        ("dependent_vowel", "11"): ("េ◌ឿ", "œă"),
        ("dependent_vowel", "12"): ("េ◌ៀ", "iĕ"),
        ("dependent_vowel", "13"): ("េ◌", "é"),
        ("dependent_vowel", "14"): ("ែ◌", "ê"),
        ("dependent_vowel", "15"): ("ៃ◌", "ai / ey"),
        ("dependent_vowel", "16"): ("េ◌ា", "aô / oŭ"),
        ("dependent_vowel", "17"): ("េ◌ៅ", "au / ŏu"),
        ("vowel_diacritic_combination", "1"): ("◌ុ◌ំ", "om / ŭm"),
        ("vowel_diacritic_combination", "2"): ("◌ំ", "âm / um"),
        ("vowel_diacritic_combination", "3"): ("◌ំ឵", "ăm / ŏâm"),
        ("vowel_diacritic_combination", "4"): ("◌ះ", "ăh / eăh"),
        ("vowel_diacritic_combination", "5"): ("◌ុ◌ះ", "ŏh / ŭh"),
        ("vowel_diacritic_combination", "6"): ("េ◌◌ះ", "éh / éh"),
        ("vowel_diacritic_combination", "7"): ("េ◌឵ះ", "aôh / ŏăh"),
        ("vowel_diacritic_combination", "8"): ("◌ំ឵ង", "ăng / eăng"),
    }
    assert len(expected_romanization) == len(rows)
    for row in rows:
        key = (row["table_section"], row["table_row"])
        assert (row["source_units"], row["bgn_pcgn_romanization"]) == expected_romanization[key]


def test_unadjudicated_rows_never_claim_a_ukrainian_candidate():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        if row["ukrainian_status"] == "EVIDENCE_LIMITED":
            assert not row["ukrainian_candidate"]
