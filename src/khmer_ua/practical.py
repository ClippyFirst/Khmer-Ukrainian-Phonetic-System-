"""Khmer IPA → Ukrainian practical transcription.

The machine-readable policy is authoritative. This module provides both
segment-level lookup and a whole-IPA longest-match adapter; it does not infer
Khmer pronunciation from spelling and does not use Russian output as fallback.
"""
from __future__ import annotations

import json
import unicodedata
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


def map_ipa_string(ipa: str, mode: str = "default") -> tuple[str | None, str | None]:
    """Render a complete IPA string with longest-match segment recognition.

    IPA length is retained through explicit long-vowel keys in the policy.
    Primary/secondary stress marks and syllable dots are analytical separators
    and are not printed in practical Ukrainian spelling. Spaces are preserved.
    Unknown material withholds the entire result; no character-level fallback
    or Russian-to-Ukrainian conversion is attempted.
    """
    if mode not in {"default", "compatibility_ru"}:
        raise ValueError(f"unsupported mapping mode: {mode}")
    rest = unicodedata.normalize("NFC", ipa.strip())
    if len(rest) > 1 and ((rest[0], rest[-1]) in {("/", "/"), ("[", "]")}):
        rest = rest[1:-1]

    rest = rest.replace("ˈ", "").replace("ˌ", "").replace(".", "")
    output: list[str] = []
    while rest:
        if rest[0].isspace():
            output.append(rest[0])
            rest = rest[1:]
            continue
        segment = next((key for key in _SEGMENT_KEYS if rest.startswith(key)), None)
        if segment is None:
            return None, rest
        entry = SEGMENTS[segment]
        value = entry.get("compatibility_ru") if mode == "compatibility_ru" else entry.get("default")
        if value is None:
            return None, rest
        output.append(value)
        rest = rest[len(segment):]
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
