import unicodedata
from .data import CONSONANTS, SIGNS
from .normalize import normalize_khmer

COENG="្"
CONSONANTS_BY_CHAR={x["char"]:x for x in CONSONANTS}
SIGNS_BY_CHAR={x["char"]:x for x in SIGNS}

def validate_khmer_unicode(text: str) -> dict:
    n=normalize_khmer(text)
    errors=[]
    warnings=[]
    for i,ch in enumerate(n):
        cp=ord(ch)
        if 0x1780 <= cp <= 0x17FF and ch not in CONSONANTS_BY_CHAR and ch not in SIGNS_BY_CHAR:
            warnings.append({"index":i,"char":ch,"codepoint":f"U+{cp:04X}","type":"unmodelled_khmer_character"})
        if ch==COENG:
            if i+1>=len(n) or n[i+1] not in CONSONANTS_BY_CHAR:
                errors.append({"index":i,"type":"malformed_coeng"})
    if any(ord(ch) in (0x17B4,0x17B5) for ch in n):
        warnings.append({"type":"discouraged_inherent_vowel_codepoint","codepoints":["U+17B4","U+17B5"]})
    if any(not (unicodedata.category(ch).startswith("L") or 0x1780<=ord(ch)<=0x17FF or ch.isspace() or unicodedata.category(ch).startswith("M") or unicodedata.category(ch).startswith("P")) for ch in n):
        warnings.append({"type":"mixed_or_unexpected_script_content"})
    return {
        "input":text,"normalized":n,"valid":not errors,
        "errors":errors,"warnings":warnings,
        "status":"VALIDATED_STRUCTURE" if not errors else "INVALID_UNICODE_STRUCTURE"
    }
