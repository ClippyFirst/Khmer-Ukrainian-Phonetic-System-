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
    value = entry.get(mode) if mode == "compatibility_ru" else entry.get("default")
    if mode == "compatibility_ru" and value is None:
        value = entry.get("default")
    if value is None:
        raise ValueError(f"unsupported IPA segment: {ipa}")
    return value


def map_sequence(segments, mode: str = "default") -> str:
    return "".join(map_segment(segment, mode=mode) for segment in segments)


def explain_segment(ipa: str) -> dict:
    return {
        "ipa": ipa,
        "ua_practical": map_segment(ipa),
        "ru_compatibility": map_segment(ipa, "compatibility_ru"),
        "status": POLICY["status"].lower(),
    }
