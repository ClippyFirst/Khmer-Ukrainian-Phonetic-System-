DEFAULT_CONSONANTS = {'p':'п','pʰ':'п','b':'б','ɓ':'б','t':'т','tʰ':'т','d':'д','ɗ':'д','k':'к','kʰ':'к','c':'ч','cʰ':'ч','ɲ':'нь','ŋ':'нг','r':'р','l':'л','ʋ':'в','w':'в','j':'й','s':'с','h':'г','ʔ':'','m':'м','n':'н'}
DEFAULT_VOWELS = {'i':'і','iː':'і','e':'е','eː':'е','ɛ':'е','ɛː':'е','ɨ':'и','ɨː':'и','a':'а','aː':'а','ɑ':'а','ɑː':'а','o':'о','oː':'о','ɔ':'о','ɔː':'о','u':'у','uː':'у','ə':'е','ɤ':'е'}
COMPATIBILITY_RU = {'pʰ':'пх','tʰ':'тх','kʰ':'кх','cʰ':'ч'}

def map_segment(ipa: str, mode: str = 'default') -> str:
    if mode not in {'default', 'compatibility_ru'}:
        raise ValueError(f"unsupported mapping mode: {mode}")
    mapping = COMPATIBILITY_RU if mode == 'compatibility_ru' else {}
    value = mapping.get(ipa, DEFAULT_CONSONANTS.get(ipa, DEFAULT_VOWELS.get(ipa)))
    if value is None:
        raise ValueError(f"unsupported IPA segment: {ipa}")
    return value

def map_sequence(segments, mode: str = 'default') -> str:
    return ''.join(map_segment(s, mode=mode) for s in segments)

def explain_segment(ipa: str) -> dict:
    return {
        'ipa': ipa,
        'ua_practical': map_segment(ipa),
        'ru_compatibility': map_segment(ipa, 'compatibility_ru'),
        'status': 'proposed'
    }
