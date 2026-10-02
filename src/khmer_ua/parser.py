import unicodedata
from .normalize import normalize_khmer
from .data import CONSONANTS, SIGNS
from .model import KhmerGrapheme, KhmerSyllable, AnalysisResult

COENG="្"
INDEPENDENT_VOWELS={x["char"] for x in SIGNS if x.get("kind")=="independent_vowel"}

def _lookup(ch):
    return next((x for x in CONSONANTS if x["char"]==ch), None)

def segment_syllables(text: str) -> list[str]:
    units=[]; current=[]
    chars=list(text)
    i=0
    while i < len(chars):
        ch=chars[i]
        if ch.isspace() or unicodedata.category(ch).startswith("P"):
            if current: units.append("".join(current)); current=[]
            units.append(ch); i+=1; continue
        if current and _lookup(ch) and not (i>0 and chars[i-1]==COENG):
            units.append("".join(current)); current=[ch]
        else:
            current.append(ch)
        i+=1
    if current: units.append("".join(current))
    return units

def decompose_khmer_syllable(raw: str) -> KhmerSyllable:
    n=normalize_khmer(raw)
    s=KhmerSyllable(raw_text=raw, normalized_text=n)
    chars=list(n); i=0
    while i<len(chars):
        ch=chars[i]
        if ch==COENG and i+1<len(chars):
            sub=chars[i+1]
            s.subscripts.append(sub)
            s.graphemes.append(KhmerGrapheme(COENG+sub,"subscript",(f"U+{ord(COENG):04X}",f"U+{ord(sub):04X}")))
            i+=2; continue
        c=_lookup(ch)
        if c:
            if s.base_consonant is None: s.base_consonant=ch
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
        s.register=c.get("register")
        s.inherent_vowel=c.get("inherent_vowel")
        s.sources=["unicode17-ch16"]
        s.status="ESTABLISHED_STRUCTURE"
        s.confidence=0.9
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
            "status":s.status,"confidence":s.confidence,"sources":s.sources})
    return AnalysisResult(text,n,[],sg,{"syllables":sg},{"status":"phoneticization_not_yet_established"},
                          None,[],[],None,[],[],["unicode17-ch16"],
                          min((s.confidence for s in syllables),default=0.0),
                          "ESTABLISHED_STRUCTURE" if syllables else "INVALID_OR_UNSUPPORTED")
