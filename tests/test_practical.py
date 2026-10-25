from khmer_ua.practical import explain_segment, map_sequence

def test_aspiration_default_and_russian_compatibility():
    assert map_sequence(['kʰ', 'a']) == 'ка'
    assert explain_segment('kʰ')['ru_compatibility'] == 'кх'

def test_velar_nasal_is_preserved():
    assert map_sequence(['ŋ', 'a']) == 'нга'

def test_glottal_stop_is_not_fabricated():
    assert map_sequence(['ʔ', 'a']) == 'а'

def test_h_targets_ukrainian_kh():
    assert map_sequence(['h', 'a']) == 'ха'

def test_palatal_nasal_uses_soft_n():
    assert map_sequence(['ɲ', 'o']) == 'ньо'


def test_missing_russian_comparator_does_not_fall_back_to_ukrainian():
    import pytest
    from khmer_ua.practical import map_segment

    with pytest.raises(ValueError, match="unsupported IPA segment"):
        map_segment("i", mode="compatibility_ru")

    explanation = explain_segment("i")
    assert explanation["ua_practical"] == "і"
    assert explanation["ru_compatibility"] is None
    assert explanation["ru_compatibility_status"] == "NOT_ESTABLISHED"
