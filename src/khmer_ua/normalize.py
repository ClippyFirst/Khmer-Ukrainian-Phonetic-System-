import unicodedata

KHMER_START, KHMER_END = 0x1780, 0x17FF

def normalize_khmer(text: str) -> str:
    return unicodedata.normalize("NFC", text)

def codepoint_info(text: str) -> list[dict]:
    out=[]
    for ch in text:
        cp=ord(ch)
        out.append({"char":ch,"codepoint":f"U+{cp:04X}","name":unicodedata.name(ch,"UNKNOWN"),
                    "khmer_block":KHMER_START <= cp <= KHMER_END,
                    "category":unicodedata.category(ch)})
    return out
