from khmer_ua.validator import validate_khmer_unicode

def test_valid_coeng():
    r=validate_khmer_unicode("ខ្ញុំ")
    assert r["valid"]

def test_invalid_coeng():
    r=validate_khmer_unicode("្")
    assert not r["valid"]
    assert r["errors"][0]["type"]=="malformed_coeng"

def test_discouraged_inherent_vowels_are_flagged():
    r=validate_khmer_unicode("ខ឴")
    assert any(x.get("type")=="discouraged_inherent_vowel_codepoint" for x in r["warnings"])
