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

def test_vowel_context_registry_is_provenance_bearing_and_conservative():
    registry = json.loads((ROOT / "data/khmer/vowel-context-register.json").read_text(encoding="utf-8"))
    assert registry["schema_version"]
    assert registry["cases"]
    sources = registry["sources"]
    required = {
        "id", "orthography", "grapheme_structure", "base_consonant_class",
        "register_condition", "phonological_interpretation", "ipa",
        "ipa_source", "ukrainian_adaptation", "ukrainian_status",
        "evidence_level", "status", "limitations",
    }
    ids = set()
    for row in registry["cases"]:
        assert required <= set(row), row.get("id")
        assert row["id"] not in ids
        ids.add(row["id"])
        assert row["ipa_source"] in sources, row["id"]
        assert row["limitations"], row["id"]
        if row["status"] in {"SOURCE_ATTESTED_NOT_GOLD", "CONFLICTING_SOURCE_ANALYSES"}:
            assert row["ukrainian_adaptation"] is None, row["id"]
            assert row["ukrainian_status"] == "NOT_ESTABLISHED", row["id"]
    conflict = next(row for row in registry["cases"] if row["id"] == "KHV-008")
    assert conflict["status"] == "CONFLICTING_SOURCE_ANALYSES"
    assert conflict["ipa"] is None
    assert len(conflict["alternatives"]) >= 2
    nikahit = next(row for row in registry["cases"] if row["id"] == "KHV-007")
    assert "NIKAHIT" in nikahit["grapheme_structure"]["coda"]

