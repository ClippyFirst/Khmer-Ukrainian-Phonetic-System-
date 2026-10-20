from khmer_ua.parser import analyze, decompose_khmer_syllable
from khmer_ua.phonology import resolve_register


def test_shared_resolver_applies_muusikatoan_to_second_series():
    syllable = decompose_khmer_syllable("ង៉")
    result = analyze("ង៉")
    assert syllable.register == "first"
    assert resolve_register(syllable) == "first"
    assert result.syllables[0]["register"] == resolve_register(syllable)
    assert result.syllables[0]["phonology"]["register_shifter"] == "MUUSIKATOAN"


def test_shared_resolver_preserves_ba_to_pa_exception():
    syllable = decompose_khmer_syllable("ប៉")
    result = analyze("ប៉")
    assert syllable.register == "first"
    assert resolve_register(syllable) == "first"
    assert result.syllables[0]["phonology"]["onset_ipa"] == "p"
    assert result.syllables[0]["phonology"]["register_shifter"] == "BA_TO_PA_EXCEPTION"


def test_invalid_shifter_does_not_change_register():
    syllable = decompose_khmer_syllable("ក៉")
    result = analyze("ក៉")
    assert resolve_register(syllable) == "first"
    assert result.syllables[0]["register"] == "first"
    assert result.syllables[0]["status"] == "EVIDENCE_LIMITED"
