"""Conservative pronunciation-profile adapter for Khmer IPA.

The colloquial Phnom Penh /r/-loss pathway is variable and cannot be
deterministically rendered from an IPA string alone. Until the API can retain
alternative analyses and source/profile metadata, matching input is rejected
rather than silently rewritten to one possible realization.
"""

import re

PROFILES = {"careful_standard", "phnom_penh_colloquial", "established_form"}

# Detect a possible stop-/r/ onset at the start of the input or after an
# explicit word/syllable boundary. The optional aspiration marker matters:
# IPA forms such as /pʰrV/, /tʰrV/ and /kʰrV/ must hit the same uncertainty
# boundary as /prV/, /trV/ and /krV/. This is a trigger, not a rewrite rule.
_R_LOSS_ONSET_CANDIDATE = re.compile(r"(^|[ .ˈˌ])([ptkbdɡc])(?:ʰ)?r(?=[aeiouəɛɔɑɨɤ])")


def render_ipa_profile(ipa: str, profile: str = "careful_standard") -> str:
    """Return IPA only when the selected profile has a deterministic rendering.

    Kirby (2014) and Wayland (2005) describe several possible correlates of
    colloquial Phnom Penh /r/-loss, including variable aspiration, F0, phonation
    and vowel effects. The input string alone does not select a unique variant.
    """
    if profile not in PROFILES:
        raise ValueError(f"unsupported pronunciation profile: {profile}")
    if profile == "phnom_penh_colloquial" and _R_LOSS_ONSET_CANDIDATE.search(ipa):
        raise ValueError(
            "Phnom Penh /r/-loss has multiple source-attested realizations; "
            "a unique IPA output requires lexical/profile evidence and an "
            "alternatives-aware result contract."
        )
    return ipa
