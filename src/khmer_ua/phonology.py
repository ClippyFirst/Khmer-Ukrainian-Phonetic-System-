from .data import CONSONANTS
from .model import KhmerSyllable

def resolve_register(syllable: KhmerSyllable) -> str | None:
    if syllable.base_consonant is None:
        return None
    item=next((x for x in CONSONANTS if x["char"]==syllable.base_consonant),None)
    return item.get("register") if item else None

def resolve_inherent_vowel(syllable: KhmerSyllable) -> str | None:
    # This function deliberately returns a series label, not a fabricated IPA vowel.
    # Exact vowel quality depends on the complete orthographic environment and
    # contemporary phonetic analysis.
    if syllable.vowel_signs or syllable.independent_vowel:
        return None
    return syllable.inherent_vowel
