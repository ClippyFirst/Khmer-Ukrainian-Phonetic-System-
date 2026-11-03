"""Conservative IPA adapter for the selected Khmer pronunciation profile.

The project uses one operational profile: contemporary Phnom Penh Khmer,
careful citation-form speech. This adapter preserves supplied IPA and does
not infer colloquial /r/-loss or rewrite segments from spelling.
"""

PROFILES = {"khmer-pph-careful-citation-v1"}


def render_ipa_profile(ipa: str, profile: str = "khmer-pph-careful-citation-v1") -> str:
    """Validate the one selected profile and preserve its source IPA."""
    if profile not in PROFILES:
        raise ValueError(f"unsupported pronunciation profile: {profile}")
    return ipa
