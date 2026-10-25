import pytest

from khmer_ua.ipa import render_ipa_profile


def test_careful_profile_preserves_r():
    assert render_ipa_profile("krɑː", "careful_standard") == "krɑː"


def test_phnom_penh_profile_withholds_ambiguous_r_loss_realization():
    # Kirby (2014) reports several correlates/realizations, not one universal
    # aspiration-only output. Do not collapse that variation to a single IPA.
    for ipa in ("krɑː", "pʰnum.krɑː", "ˈtrəː", "ar.krɑː"):
        with pytest.raises(ValueError, match="multiple source-attested realizations"):
            render_ipa_profile(ipa, "phnom_penh_colloquial")


def test_phnom_penh_profile_withholds_aspirated_stop_r_onsets():
    # Aspiration is part of the IPA segment and must not bypass the profile's
    # ambiguity gate simply because ʰ occurs between the stop and /r/.
    for ipa in ("pʰrɑː", "tʰrɑː", "kʰrɑː", "cʰrɑː"):
        with pytest.raises(ValueError, match="multiple source-attested realizations"):
            render_ipa_profile(ipa, "phnom_penh_colloquial")


def test_phnom_penh_profile_does_not_flag_unsegmented_medial_match():
    # Without an explicit boundary, "kr" may be a substring rather than an onset.
    assert render_ipa_profile("akra", "phnom_penh_colloquial") == "akra"


def test_phnom_penh_profile_does_not_flag_coda_r():
    assert render_ipa_profile("kɑːr", "phnom_penh_colloquial") == "kɑːr"


def test_non_colloquial_profiles_preserve_input():
    assert render_ipa_profile("krɑː", "established_form") == "krɑː"


def test_unknown_profile_is_rejected():
    with pytest.raises(ValueError, match="unsupported pronunciation profile"):
        render_ipa_profile("krɑː", "unknown")
