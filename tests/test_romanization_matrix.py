import csv
from pathlib import Path

EXPECTED_ROWS = {
    "1": ("ក|គ|្ក|្គ", "k", "к"),
    "2": ("ខ|ឃ|្ខ|្ឃ", "kh", "к'"),
    "3": ("ង|្ង", "ng", "нг"),
    "4": ("ច|ជ|្ច|្ជ", "ch", "ч"),
    "5": ("ឆ|ឈ|្ឆ|្ឈ", "chh", "ч'"),
    "6": ("ញ|្ញ", "nh", "нь"),
    "7": ("ដ|ឌ|្ដ|្ឌ", "d", "д"),
    "8": ("ឋ|ឍ|្ឋ|្ឍ", "th", ""),
    "9": ("ថ|ធ|្ថ|្ធ", "th", ""),
    "10": ("ណ|ន|្ណ|្ន", "n", "н"),
    "11": ("ត|ទ|្ត|្ទ", "t", "т"),
    "12": ("ប|្ប", "b,p", ""),
    "13": ("ព|្ព", "p", "п"),
    "14": ("ផ|ភ|្ផ|្ភ", "ph", "п'"),
    "15": ("ម|្ម", "m", "м"),
    "16": ("យ", "y", "й"),
    "17": ("រ|្រ", "r", "р"),
    "18": ("ឡ|ល|្ល", "l", "л"),
    "19": ("វ|្វ", "v", "в"),
    "20": ("ស|្ស", "s", "с"),
    "21": ("ហ|្ហ", "h", "г"),
    "22": ("អ|្អ", "’", ""),
}


def test_bgn_pcgn_consonant_matrix_covers_the_official_base_and_subscript_rows():
    path = Path(__file__).parents[1] / "data" / "khmer" / "romanization_ukrainian.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    actual = {
        row["table_row"]: (row["source_units"], row["romanization"], row["ukrainian_candidate"])
        for row in rows
    }
    assert actual == EXPECTED_ROWS
    assert len(rows) == len(EXPECTED_ROWS)


def test_khmer_romanization_matrix_preserves_provenance_and_uncertainty():
    path = Path(__file__).parents[1] / "data" / "khmer" / "romanization_ukrainian.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    allowed = {"PROPOSED", "ANALYSIS_DEPENDENT", "EVIDENCE_LIMITED"}
    assert all(row["ukrainian_status"] in allowed for row in rows)
    assert all(row["source_url"].startswith("https://") for row in rows)
    assert all(row["source_locator"].strip() for row in rows)
    assert all(row["source_units"].strip() for row in rows)
    assert all(row["ukrainian_candidate"] for row in rows if row["ukrainian_status"] == "PROPOSED")
    assert {row["table_row"] for row in rows} == {str(i) for i in range(1, 23)}
