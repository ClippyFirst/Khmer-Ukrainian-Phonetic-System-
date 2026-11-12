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
    assert r.syllables[0]["status"]=="INVALID_OR_UNSUPPORTED"
    assert r.status=="INVALID_OR_UNSUPPORTED"

def test_complex_unicode_examples():
    r=analyze("សង្គ្រាម")
    assert r.syllables[0]["subscripts"] == ["គ","រ"]


def test_unknown_non_khmer_material_does_not_pass_as_established_structure():
    r = analyze("កx")

    assert r.syllables[0]["status"] == "INVALID_OR_UNSUPPORTED"
    assert r.status == "INVALID_OR_UNSUPPORTED"
    assert r.confidence == 0.0


def test_every_assigned_khmer_letter_and_mark_has_a_lossless_parser_record():
    import unicodedata

    from khmer_ua.parser import decompose_khmer_syllable, segment_syllables

    ranges = ((0x1780, 0x17FF), (0x19E0, 0x19FF))
    tested = 0
    for start, end in ranges:
        for codepoint in range(start, end + 1):
            char = chr(codepoint)
            if unicodedata.category(char)[0] not in {"L", "M"}:
                continue
            units = segment_syllables(char)
            assert "".join(units) == char, f"source lost for U+{codepoint:04X}"
            assert len(units) == 1
            parsed = decompose_khmer_syllable(units[0])
            assert "".join(item.text for item in parsed.graphemes) == char
            assert [cp for item in parsed.graphemes for cp in item.codepoints] == [
                f"U+{codepoint:04X}"
            ]
            tested += 1
    assert tested > 0


def test_unmodelled_khmer_letter_is_traced_as_unknown_not_as_ipa():
    from khmer_ua.parser import decompose_khmer_syllable

    # U+17F9 is a Khmer symbol rather than a consonant or vowel phoneme.
    parsed = decompose_khmer_syllable(chr(0x17F9))
    assert parsed.graphemes
    assert parsed.graphemes[0].codepoints == ("U+17F9",)
    assert parsed.status == "INVALID_OR_UNSUPPORTED"
