import unicodedata
from .normalize import normalize_khmer
from .data import CONSONANTS, SIGNS
from .model import KhmerGrapheme, KhmerSyllable, AnalysisResult

COENG="្"
MUUSIKATOAN="៉"
TRIISAP="៊"
INDEPENDENT_VOWELS={x["char"] for x in SIGNS if x.get("kind")=="independent_vowel"}
SHIFTER_ELIGIBILITY={
    MUUSIKATOAN: {"ង","ញ","ន","ម","យ","រ","ល","វ","ឝ"},
    TRIISAP: {"ប","ឞ","ស","ហ","អ"},
}

def _lookup(ch):
    return next((x for x in CONSONANTS if x["char"]==ch), None)

def _starts_new_orthographic_syllable(chars, i):
    """Conservatively split explicit Khmer syllable boundaries."""
    if not _lookup(chars[i]):
        return False
    if i == 0:
        return False
    if chars[i-1] == COENG:
        return False
    if i + 1 < len(chars) and chars[i+1] == COENG:
        return False
    previous_kind = next((x["kind"] for x in SIGNS if x["char"] == chars[i-1]), None)
    if previous_kind in {"dependent_vowel", "composite_vowel", "vowel_modifier", "sign"}:
        j = i + 1
        if j >= len(chars) or chars[j].isspace() or unicodedata.category(chars[j]).startswith("P"):
            return False
    return True

def segment_syllables(text: str) -> list[str]:
    units=[]; current=[]
    chars=list(text)
    i=0
    while i < len(chars):
        ch=chars[i]
        if ch.isspace() or unicodedata.category(ch).startswith("P"):
            if current:
                units.append("".join(current)); current=[]
            units.append(ch); i+=1; continue
        if current and _starts_new_orthographic_syllable(chars, i):
            units.append("".join(current))
            current=[ch]
        else:
            current.append(ch)
        i+=1
    if current:
        units.append("".join(current))
    return units

def _resolve_effective_register(base: dict, chars: list[str]) -> tuple[str | None, str | None]:
    """Resolve register after Khmer register-shifters, including ប៉ exception."""
    register=base.get("register")
    positions=[i for i,ch in enumerate(chars) if ch in {MUUSIKATOAN, TRIISAP}]
    if not positions:
        return register, None
    if len(positions) > 1:
        return register, "MULTIPLE_REGISTER_SHIFTERS"
    if positions[0] != 1:
        return register, "MISPLACED_REGISTER_SHIFTER"
    shifter=chars[positions[0]]
    if base["char"] not in SHIFTER_ELIGIBILITY.get(shifter, set()):
        return register, "NON_STANDARD_SHIFTER_USE"
    if base["char"]=="ប" and shifter==MUUSIKATOAN:
        return "first", "BA_TO_PA_EXCEPTION"
    if shifter==MUUSIKATOAN and register=="second":
        return "first", "MUUSIKATOAN"
    if shifter==TRIISAP and register=="first":
        return "second", "TRIISAP"
    return register, "NON_STANDARD_SHIFTER_USE"

def decompose_khmer_syllable(raw: str) -> KhmerSyllable:
    n=normalize_khmer(raw)
    s=KhmerSyllable(raw_text=raw, normalized_text=n)
    chars=list(n); i=0
    while i<len(chars):
        ch=chars[i]
        if ch==COENG:
            if i+1>=len(chars) or not _lookup(chars[i+1]):
                s.status="INVALID_OR_UNSUPPORTED"
                s.confidence=0.0
                s.sources=["unicode17-ch16"]
                return s
            sub=chars[i+1]
            s.subscripts.append(sub)
            s.graphemes.append(KhmerGrapheme(COENG+sub,"subscript",(f"U+{ord(COENG):04X}",f"U+{ord(sub):04X}")))
            i+=2
            continue
        c=_lookup(ch)
        if c:
            if s.base_consonant is None:
                s.base_consonant=ch
            s.graphemes.append(KhmerGrapheme(ch,"consonant",(f"U+{ord(ch):04X}",)))
        elif ch in INDEPENDENT_VOWELS:
            s.independent_vowel=ch
            s.graphemes.append(KhmerGrapheme(ch,"independent_vowel",(f"U+{ord(ch):04X}",)))
        else:
            kind=next((x["kind"] for x in SIGNS if x["char"]==ch),"sign_or_unknown")
            if kind in {"dependent_vowel","composite_vowel","vowel_modifier"}:
                s.vowel_signs.append(ch)
            s.graphemes.append(KhmerGrapheme(ch,kind,(f"U+{ord(ch):04X}",)))
        i+=1
    if s.base_consonant:
        c=_lookup(s.base_consonant)
        s.register, shifter_rule=_resolve_effective_register(c, chars)
        s.inherent_vowel=("first-series" if s.register=="first" else "second-series" if s.register=="second" else None)
        s.phonology["onset_ipa"]=("p" if s.base_consonant=="ប" and shifter_rule=="BA_TO_PA_EXCEPTION" else c.get("onset_ipa"))
        if shifter_rule:
            s.phonology["register_shifter"]=shifter_rule
        s.sources=["unicode17-ch16"]
        s.status="ESTABLISHED_STRUCTURE" if shifter_rule not in {"MULTIPLE_REGISTER_SHIFTERS", "MISPLACED_REGISTER_SHIFTER"} else "EVIDENCE_LIMITED"
        s.confidence=0.9 if s.status=="ESTABLISHED_STRUCTURE" else 0.6
    elif s.independent_vowel:
        s.sources=["unicode17-ch16"]
        s.status="ESTABLISHED_STRUCTURE"
        s.confidence=0.9
    else:
        s.status="INVALID_OR_UNSUPPORTED"
        s.confidence=0.0
    return s

def analyze(text: str) -> AnalysisResult:
    n=normalize_khmer(text)
    units=segment_syllables(n)
    syllables=[decompose_khmer_syllable(x) for x in units if x.strip()]
    sg=[]
    for s in syllables:
        sg.append({
            "raw_text":s.raw_text,"normalized_text":s.normalized_text,
            "graphemes":[{"text":g.text,"kind":g.kind,"codepoints":g.codepoints} for g in s.graphemes],
            "base_consonant":s.base_consonant,"register":s.register,
            "subscripts":s.subscripts,"vowel_signs":s.vowel_signs,
            "independent_vowel":s.independent_vowel,"inherent_vowel":s.inherent_vowel,
            "phonology":s.phonology,
            "status":s.status,"confidence":s.confidence,"sources":s.sources})
    if not syllables:
        overall_status = "INVALID_OR_UNSUPPORTED"
    elif any(s["status"] == "INVALID_OR_UNSUPPORTED" for s in sg):
        overall_status = "INVALID_OR_UNSUPPORTED"
    elif any(s["status"] == "EVIDENCE_LIMITED" for s in sg):
        overall_status = "EVIDENCE_LIMITED"
    else:
        overall_status = "ESTABLISHED_STRUCTURE"

    return AnalysisResult(text,n,[],sg,{"syllables":sg},{"status":"phoneticization_not_yet_established"},
                          None,[],[],None,[],[],["unicode17-ch16"],
                          min((s.confidence for s in syllables),default=0.0),
                          overall_status)
