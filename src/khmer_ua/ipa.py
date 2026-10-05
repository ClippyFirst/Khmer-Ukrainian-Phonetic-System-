import re

PROFILES = {"careful_standard", "phnom_penh_colloquial", "established_form"}

def render_ipa_profile(ipa: str, profile: str = "careful_standard") -> str:
    """Apply only documented pronunciation-profile transformations to an IPA string.

    This is deliberately not an orthography-to-IPA engine. The colloquial profile
    models the documented /r/-loss pathway in onset clusters conservatively.
    """
    if profile not in PROFILES:
        raise ValueError(f"unsupported pronunciation profile: {profile}")
    if profile in {"careful_standard", "established_form"}:
        return ipa
    # Conservative placeholder for the documented Phnom Penh /r/-loss pathway:
    # C+r+V -> aspirated C+V. It does not touch standalone /r/ or coda /r/.
    return re.sub(r"([ptkbdɡc])r(?=[^aeiouəɛɔɑɨiuoːː])", r"\1ʰ", ipa)
