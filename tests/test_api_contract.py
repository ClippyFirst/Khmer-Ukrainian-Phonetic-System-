from khmer_ua.parser import analyze


def test_structural_success_is_not_reported_as_phonetic_success():
    result = analyze("ក")

    assert result.status == "ESTABLISHED_STRUCTURE"
    assert result.syllables[0]["status"] == "ESTABLISHED_STRUCTURE"
    assert result.phonological_representation["syllables"][0]["register"] == "first"
    assert result.phonetic_representation["status"] == "phoneticization_not_yet_established"
    assert result.ipa is None
    assert result.ukrainian_candidates == []
    assert result.selected_candidate is None


def test_unsupported_input_does_not_acquire_phonetic_output():
    result = analyze("☃")

    assert result.status == "INVALID_OR_UNSUPPORTED"
    assert result.phonetic_representation["status"] == "phoneticization_not_yet_established"
    assert result.ipa is None
    assert result.ukrainian_candidates == []
    assert result.selected_candidate is None


def test_mixed_supported_and_unsupported_input_preserves_per_unit_status():
    result = analyze("ក ☃")

    assert result.status == "EVIDENCE_LIMITED"
    assert result.syllables[0]["status"] == "ESTABLISHED_STRUCTURE"
    assert result.syllables[1]["status"] == "INVALID_OR_UNSUPPORTED"
    assert result.phonetic_representation["status"] == "phoneticization_not_yet_established"
    assert result.ipa is None
