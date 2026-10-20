from khmer_ua.parser import analyze


def test_nikahit_does_not_claim_deterministic_ipa():
    result = analyze("ដំ")
    assert result.status == "ESTABLISHED_STRUCTURE"
    assert result.ipa is None
    assert result.phonetic_representation["status"] == "phoneticization_not_yet_established"
    assert any(
        grapheme["text"] == "ំ" and grapheme["kind"] == "vowel_modifier"
        for grapheme in result.syllables[0]["graphemes"]
    )


def test_reahmuk_does_not_claim_deterministic_ipa():
    result = analyze("កះ")
    assert result.status == "ESTABLISHED_STRUCTURE"
    assert result.ipa is None
    assert result.phonetic_representation["status"] == "phoneticization_not_yet_established"
    assert any(
        grapheme["text"] == "ះ" and grapheme["kind"] == "sign"
        for grapheme in result.syllables[0]["graphemes"]
    )
