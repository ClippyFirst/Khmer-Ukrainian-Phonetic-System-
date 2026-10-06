import json
from pathlib import Path
from khmer_ua.parser import decompose_khmer_syllable, segment_syllables

ROOT = Path(__file__).resolve().parents[1]

def test_register_shifters_are_not_ignored():
    assert decompose_khmer_syllable("រ៉ា").register == "first"
    assert decompose_khmer_syllable("ហ៊ិ").register == "second"

def test_ba_muusikatoan_exception_changes_onset():
    s = decompose_khmer_syllable("ប៉ី")
    assert s.register == "first"
    assert s.phonology["register_shifter"] == "BA_TO_PA_EXCEPTION"
    assert s.phonology["onset_ipa"] == "p"

def test_multiple_shifters_are_flagged():
    s = decompose_khmer_syllable("ស៊៉ា")
    assert s.status == "EVIDENCE_LIMITED"
    assert s.phonology["register_shifter"] == "MULTIPLE_REGISTER_SHIFTERS"

def test_known_unicode_cluster_segmentation():
    assert segment_syllables("សង្គ្រាម") == ["សង្គ្រាម"]

def test_known_unicode_cluster_structure():
    s = decompose_khmer_syllable("សង្គ្រាម")
    assert s.base_consonant == "ស"
    assert s.subscripts == ["គ", "រ"]
    assert any(g.text == "ង" and g.kind == "consonant" for g in s.graphemes)
    assert "ា" in s.vowel_signs

def test_adversarial_corpus_has_explicit_provenance():
    cases=json.loads((ROOT/"data/tests/adversarial-cases.json").read_text(encoding="utf-8"))
    assert len(cases) >= 8
    for case in cases.values():
        assert "source_basis" in case
        if case.get("ipa") is not None:
            assert case["ipa"].startswith("/") and case["ipa"].endswith("/")
