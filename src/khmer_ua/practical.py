"""Khmer IPA → Ukrainian practical transcription.

The machine-readable policy is authoritative. This module provides both
segment-level lookup and a whole-IPA longest-match adapter; it does not infer
Khmer pronunciation from spelling and does not use Russian output as fallback.
"""
from __future__ import annotations

import json
import unicodedata
import re
from pathlib import Path

_POLICY_PATH = Path(__file__).resolve().parents[2] / "data" / "ukrainian" / "practical-policy.json"
with _POLICY_PATH.open(encoding="utf-8") as _handle:
    POLICY = json.load(_handle)

SEGMENTS = POLICY["segments"]
_SEGMENT_KEYS = tuple(sorted(
    (key for key, value in SEGMENTS.items() if value.get("default") is not None),
    key=len,
    reverse=True,
))

_JOTATED_VOWELS = {
    "a": "я", "aː": "я", "ɑ": "я", "ɑː": "я",
    "e": "є", "eː": "є", "ɛ": "є", "ɛː": "є",
    "i": "ї", "iː": "ї",
    "o": "йо", "oː": "йо", "ɔ": "йо", "ɔː": "йо",
    "u": "ю", "uː": "ю",
    "ɨ": "йи", "ɨː": "йи",
}


def map_segment(ipa: str, mode: str = "default") -> str:
    if mode not in {"default", "compatibility_ru"}:
        raise ValueError(f"unsupported mapping mode: {mode}")
    entry = SEGMENTS.get(ipa, {})
    value = entry.get("compatibility_ru") if mode == "compatibility_ru" else entry.get("default")
    if value is None:
        raise ValueError(f"unsupported IPA segment: {ipa}")
    return value


def map_sequence(segments, mode: str = "default") -> str:
    """Map an already tokenized IPA segment sequence without retokenizing it."""
    return "".join(map_segment(segment, mode=mode) for segment in segments)


def _map_syllable(syllable: str, mode: str) -> tuple[str | None, str | None]:
    rest = syllable
    tokens: list[str] = []
    while rest:
        segment = next((key for key in _SEGMENT_KEYS if rest.startswith(key)), None)
        if segment is None:
            return None, rest
        tokens.append(segment)
        rest = rest[len(segment):]

    output: list[str] = []
    index = 0
    if mode == "default" and len(tokens) > 1 and tokens[0] == "j" and tokens[1] in _JOTATED_VOWELS:
        output.append(_JOTATED_VOWELS[tokens[1]])
        index = 2
    while index < len(tokens):
        output.append(map_segment(tokens[index], mode=mode))
        index += 1
    return "".join(output), None


def map_ipa_string(ipa: str, mode: str = "default") -> tuple[str | None, str | None]:
    """Render a complete IPA string with longest-match segment recognition.

    Spaces are preserved. Stress marks and syllable dots are not printed.
    Syllable-initial /j/ + vowel uses Ukrainian yotated orthography in default
    mode; the Russian comparator mode stays segmental. Unknown material
    withholds the entire practical result.
    """
    if mode not in {"default", "compatibility_ru"}:
        raise ValueError(f"unsupported mapping mode: {mode}")
    rest = unicodedata.normalize("NFC", ipa.strip())
    if len(rest) > 1 and ((rest[0], rest[-1]) in {("/", "/"), ("[", "]")}):
        rest = rest[1:-1]
    rest = rest.replace("ˈ", "").replace("ˌ", "")

    output: list[str] = []
    for part in re.split(r"(\s+|[.·])", rest):
        if not part:
            continue
        if part.isspace():
            output.append(part)
            continue
        if part in {".", "·"}:
            continue
        mapped, unsupported = _map_syllable(part, mode)
        if unsupported is not None:
            return None, unsupported
        output.append(mapped or "")
    return "".join(output), None


def explain_segment(ipa: str) -> dict:
    try:
        russian_value = map_segment(ipa, "compatibility_ru")
        russian_status = "MAPPED"
    except ValueError:
        # Missing comparator evidence must not be filled with the Ukrainian
        # choice and mislabeled as Russian practical transcription.
        russian_value = None
        russian_status = "NOT_ESTABLISHED"
    return {
        "ipa": ipa,
        "ua_practical": map_segment(ipa),
        "ru_compatibility": russian_value,
        "ru_compatibility_status": russian_status,
        "status": POLICY["status"].lower(),
    }
