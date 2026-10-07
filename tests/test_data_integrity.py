import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_vowel_data_is_valid_and_nonempty():
    data = json.loads((ROOT / "data/khmer/vowels.json").read_text(encoding="utf-8"))
    assert data["inherent_vowels"]
    assert data["plain_vowels"]
    assert data["complex_vowels"]

def test_consonant_phonetic_claims_have_non_unicode_provenance():
    consonants = json.loads((ROOT / "data/khmer/consonants.json").read_text(encoding="utf-8"))
    for row in consonants:
        assert any(source != "unicode17-ch16" for source in row["evidence"]), row["char"]

def test_corpus_cases_are_provenance_bearing():
    cases = json.loads((ROOT / "data/tests/khmer_cases.json").read_text(encoding="utf-8"))
    assert len(cases) >= 8
    for case in cases:
        assert "id" in case
        assert "status" in case or "evidence" in case


def test_register_shifter_eligibility_is_explicit():
    data = json.loads((ROOT / "data/khmer/registers.json").read_text(encoding="utf-8"))
    eligibility = data["shifter_eligibility"]
    assert set(eligibility["muusikatoan"]) >= {"ង","ញ","ន","ម","យ","រ","ល","វ"}
    assert set(eligibility["triisap"]) >= {"ប","ស","ហ","អ"}


def test_shifter_eligibility_references_known_consonants():
    consonants = json.loads((ROOT / "data/khmer/consonants.json").read_text(encoding="utf-8"))
    known = {row["char"] for row in consonants}
    data = json.loads((ROOT / "data/khmer/registers.json").read_text(encoding="utf-8"))
    for shifter, chars in data["shifter_eligibility"].items():
        unknown = set(chars) - known
        assert not unknown, f"{shifter} references consonants absent from canonical inventory: {sorted(unknown)}"
