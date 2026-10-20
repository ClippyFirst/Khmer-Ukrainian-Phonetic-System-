import re

PROFILES = {"careful_standard", "phnom_penh_colloquial", "established_form"}

# This deliberately only rewrites a cluster at the start of the supplied IPA
# string or after an explicit word/syllable boundary. Without syllabification
# metadata, rewriting every matching substring can corrupt medial/coda sequences.
_R_LOSS_ONSET = re.compile(r"(^|[ .ˈˌ])([ptkbdɡc])r(?=[aeiouəɛɔɑɨɤ])")


def render_ipa_profile(ipa: str, profile: str = "careful_standard") -> str:
    """Apply limited, explicitly bounded pronunciation-profile transformations.

    This is not an orthography-to-IPA engine. The Phnom Penh colloquial profile
    approximates a documented /r/-loss pathway in eligible onset clusters, but
    only when a word/syllable boundary is explicit. It intentionally leaves
    unsegmented medial strings unchanged because this function has no syllabifier
    or lexical context. This profile remains provisional, not a complete acoustic
    model of aspiration, f0, phonation, or vowel effects.
    """
    if profile not in PROFILES:
        raise ValueError(f"unsupported pronunciation profile: {profile}")
    if profile in {"careful_standard", "established_form"}:
        return ipa
    return _R_LOSS_ONSET.sub(lambda match: f"{match.group(1)}{match.group(2)}ʰ", ipa)
