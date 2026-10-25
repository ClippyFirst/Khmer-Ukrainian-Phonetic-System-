import json
from pathlib import Path

_POLICY_PATH = Path(__file__).resolve().parents[2] / "data" / "ukrainian" / "practical-policy.json"
with _POLICY_PATH.open(encoding="utf-8") as _handle:
    POLICY = json.load(_handle)

SEGMENTS = POLICY["segments"]


def map_segment(ipa: str, mode: str = "default") -> str:
    if mode not in {"default", "compatibility_ru"}:
        raise ValueError(f"unsupported mapping mode: {mode}")
    entry = SEGMENTS.get(ipa, {})
    value = entry.get("compatibility_ru") if mode == "compatibility_ru" else entry.get("default")
    if value is None:
        raise ValueError(f"unsupported IPA segment: {ipa}")
    return value


def map_sequence(segments, mode: str = "default") -> str:
    return "".join(map_segment(segment, mode=mode) for segment in segments)


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
