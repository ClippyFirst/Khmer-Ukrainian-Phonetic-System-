from khmer_ua.ipa import render_ipa_profile

def test_careful_profile_preserves_r():
    assert render_ipa_profile("krɑː", "careful_standard") == "krɑː"

def test_phnom_penh_profile_does_not_delete_every_r():
    assert render_ipa_profile("krɑː", "phnom_penh_colloquial") == "kʰɑː"

def test_unknown_profile_is_rejected():
    try:
        render_ipa_profile("krɑː", "unknown")
    except ValueError:
        pass
    else:
        raise AssertionError("unknown profile must raise ValueError")
