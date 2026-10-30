from khmer_ua.practical import explain_segment, map_sequence, map_segment


def test_aspiration_is_marked_and_russian_comparator_stays_separate():
    assert map_sequence(['kʰ', 'a']) == "к'а"
    assert map_sequence(['pʰ', 'a']) == "п'а"
    assert map_sequence(['tʰ', 'a']) == "т'а"
    assert map_sequence(['cʰ', 'a']) == "ч'а"
    assert explain_segment('kʰ')['ru_compatibility'] == 'кх'


def test_velar_nasal_is_preserved():
    assert map_sequence(['ŋ', 'a']) == 'нга'


def test_glottal_stop_is_not_aspiration():
    assert map_sequence(['ʔ', 'a']) == 'а'


def test_h_g_and_x_are_distinguished():
    assert map_sequence(['h', 'a']) == 'га'
    assert map_sequence(['ɡ', 'a']) == 'ґа'
    assert map_sequence(['x', 'a']) == 'ха'


def test_affricates_and_fricatives_use_ukrainian_sequences():
    assert map_sequence(['t͡s', 'a']) == 'ца'
    assert map_sequence(['d͡z', 'a']) == 'дза'
    assert map_sequence(['t͡ʃ', 'a']) == 'ча'
    assert map_sequence(['tɕ', 'a']) == 'ча'
    assert map_sequence(['d͡ʒ', 'a']) == 'джа'
    assert map_sequence(['dʑ', 'a']) == 'джа'
    assert map_sequence(['ʃ', 'a']) == 'ша'
    assert map_sequence(['ʒ', 'a']) == 'жа'


def test_palatalization_uses_ukrainian_soft_sign():
    assert map_segment('tʲ') == 'ть'
    assert map_segment('dʲ') == 'дь'
    assert map_segment('nʲ') == 'нь'
    assert map_segment('lʲ') == 'ль'


def test_missing_russian_comparator_does_not_fall_back_to_ukrainian():
    import pytest
    with pytest.raises(ValueError, match="unsupported IPA segment"):
        map_segment("i", mode="compatibility_ru")
    explanation = explain_segment("i")
    assert explanation["ua_practical"] == "і"
    assert explanation["ru_compatibility"] is None
    assert explanation["ru_compatibility_status"] == "NOT_ESTABLISHED"
