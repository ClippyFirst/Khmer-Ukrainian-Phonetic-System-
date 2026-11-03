import pytest

from khmer_ua.ipa import render_ipa_profile


def test_selected_phnom_penh_careful_citation_profile_preserves_ipa():
    for ipa in ("krɑː", "pʰnum.krɑː", "ˈtrəː", "ar.krɑː"):
        assert render_ipa_profile(ipa) == ipa
        assert render_ipa_profile(ipa, "khmer-pph-careful-citation-v1") == ipa


@pytest.mark.parametrize("profile", [
    "careful_standard",
    "phnom_penh_colloquial",
    "established_form",
    "unknown",
])
def test_unselected_profiles_are_rejected(profile):
    with pytest.raises(ValueError, match="unsupported pronunciation profile"):
        render_ipa_profile("krɑː", profile)
