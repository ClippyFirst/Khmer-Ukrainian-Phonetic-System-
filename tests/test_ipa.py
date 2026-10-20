from khmer_ua.ipa import render_ipa_profile


def test_careful_profile_preserves_r():
    assert render_ipa_profile("krɑː", "careful_standard") == "krɑː"


def test_phnom_penh_profile_rewrites_word_initial_cluster():
    assert render_ipa_profile("krɑː", "phnom_penh_colloquial") == "kʰɑː"


def test_phnom_penh_profile_rewrites_only_after_explicit_syllable_boundary():
    assert render_ipa_profile("pʰnum.krɑː", "phnom_penh_colloquial") == "pʰnum.kʰɑː"
    assert render_ipa_profile("ˈtrəː", "phnom_penh_colloquial") == "ˈtʰəː"


def test_phnom_penh_profile_does_not_rewrite_unsegmented_medial_match():
    # Without syllable boundaries, the function cannot know that "kr" begins
    # an onset; avoid corrupting an arbitrary IPA substring.
    assert render_ipa_profile("akra", "phnom_penh_colloquial") == "akra"


def test_phnom_penh_profile_does_not_rewrite_coda_r():
    assert render_ipa_profile("ar.krɑː", "phnom_penh_colloquial") == "ar.kʰɑː"
    assert render_ipa_profile("kɑːr", "phnom_penh_colloquial") == "kɑːr"


def test_non_colloquial_profiles_preserve_input():
    assert render_ipa_profile("krɑː", "established_form") == "krɑː"


def test_unknown_profile_is_rejected():
    try:
        render_ipa_profile("krɑː", "unknown")
    except ValueError:
        pass
    else:
        raise AssertionError("unknown profile must raise ValueError")
