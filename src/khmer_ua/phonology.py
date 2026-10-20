from .data import CONSONANTS, SHIFTER_ELIGIBILITY
from .model import KhmerSyllable

COENG = "្"
MUUSIKATOAN = "៉"
TRIISAP = "៊"
ZWNJ = "\u200C"


def resolve_effective_register(base: dict, chars: list[str]) -> tuple[str | None, str | None]:
    """Resolve a base consonant's register after eligible Khmer register shifters.

    The return value is (effective_register, rule_id). This resolves only the
    orthographic register layer; it does not predict a vowel's surface IPA.
    """
    register = base.get("register")
    structural = [ch for ch in chars if ch != ZWNJ]
    positions = [i for i, ch in enumerate(structural) if ch in {MUUSIKATOAN, TRIISAP}]
    if not positions:
        return register, None
    if len(positions) > 1:
        return register, "MULTIPLE_REGISTER_SHIFTERS"
    if positions[0] != 1:
        return register, "MISPLACED_REGISTER_SHIFTER"
    shifter = structural[positions[0]]
    if base["char"] not in SHIFTER_ELIGIBILITY.get(shifter, set()):
        return register, "NON_STANDARD_SHIFTER_USE"
    if base["char"] == "ប" and shifter == MUUSIKATOAN:
        return "first", "BA_TO_PA_EXCEPTION"
    if shifter == MUUSIKATOAN and register == "second":
        return "first", "MUUSIKATOAN"
    if shifter == TRIISAP and register == "first":
        return "second", "TRIISAP"
    return register, "NON_STANDARD_SHIFTER_USE"


def resolve_register(syllable: KhmerSyllable) -> str | None:
    """Resolve effective register from the full orthographic syllable.

    Unlike a base-letter lookup, this honours valid register shifters. The
    parser and this helper share the same resolver to prevent divergent rules.
    """
    if syllable.base_consonant is None:
        return None
    item = next((x for x in CONSONANTS if x["char"] == syllable.base_consonant), None)
    if not item:
        return None
    register, rule = resolve_effective_register(item, list(syllable.normalized_text))
    if rule in {"MULTIPLE_REGISTER_SHIFTERS", "MISPLACED_REGISTER_SHIFTER", "NON_STANDARD_SHIFTER_USE"}:
        return item.get("register")
    return register


def resolve_inherent_vowel(syllable: KhmerSyllable) -> str | None:
    # This function deliberately returns a series label, not a fabricated IPA vowel.
    # Exact vowel quality depends on the complete orthographic environment and
    # contemporary phonetic analysis.
    if syllable.vowel_signs or syllable.independent_vowel:
        return None
    return syllable.inherent_vowel
