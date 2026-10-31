import csv
from pathlib import Path

EXPECTED_ROWS = {
    "1": ("k", "к"),
    "2": ("kh", "к'"),
    "3": ("ng", "нг"),
    "4": ("ch", "ч"),
    "5": ("chh", "ч'"),
    "6": ("nh", "нь"),
    "7": ("d", "д"),
    "8": ("th", ""),
    "9": ("th", ""),
    "10": ("n", "н"),
    "11": ("t", "т"),
    "12": ("b,p", ""),
    "13": ("p", "п"),
    "14": ("ph", "п'"),
    "15": ("m", "м"),
    "16": ("y", "й"),
    "17": ("r", "р"),
    "18": ("l", "л"),
    "19": ("v", "в"),
    "20": ("s", "с"),
    "21": ("h", "г"),
    "22": ("’", ""),
    "SPECIAL-1": ("l", "л"),
}


def test_bgn_pcgn_consonant_matrix_covers_the_official_base_and_subscript_rows():
    path = Path(__file__).parents[1] / "data" / "khmer" / "romanization_ukrainian.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    actual = {row["table_row"]: (row["romanization"], row["ukrainian_candidate"]) for row in rows}
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
