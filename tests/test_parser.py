from khmer_ua.parser import analyze
from khmer_ua.normalize import normalize_khmer

def test_nfc_is_stable():
    assert normalize_khmer("ខ្ញុំ") == "ខ្ញុំ"

def test_coeng_is_structural():
    r=analyze("ខ្ញុំ")
    s=r.syllables[0]
    assert "ញ" in s["subscripts"]
    assert s["base_consonant"]=="ខ"

def test_register_is_not_character_to_ua_mapping():
    r=analyze("កគ")
    assert r.syllables[0]["register"]=="first"
    assert r.syllables[1]["register"]=="second"

def test_independent_vowel():
    r=analyze("ឥ")
    assert r.syllables[0]["independent_vowel"]=="ឥ"

def test_malformed_sequence_is_not_confident():
    r=analyze("្")
    assert r.confidence==0.0
    assert r.status=="INVALID_OR_UNSUPPORTED"

def test_complex_unicode_examples():
    r=analyze("សង្គ្រាម")
    assert r.syllables[0]["subscripts"] == ["គ","រ"]
