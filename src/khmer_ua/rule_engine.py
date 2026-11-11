"""Deterministic, rule-based Khmer → IPA → Ukrainian research engine.

No neural inference, remote service, external G2P process, voting, or runtime
model selection is performed. The engine uses the repository's attested
lexical fixtures and conservative orthographic rules. Unsupported patterns
are withheld instead of guessed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .data import CONSONANTS
from .normalize import normalize_khmer
from .parser import analyze as analyze_structure
from .practical import map_segment

ROOT = Path(__file__).resolve().parents[2]
_FIXTURE_PATH = ROOT / "data" / "tests" / "web-fixtures.json"
with _FIXTURE_PATH.open(encoding="utf-8") as _handle:
    _LEXICON: dict[str, dict[str, Any]] = json.load(_handle)

_SEGMENT_KEYS = tuple(sorted(
    (key for key, value in __import__("json").loads(
        (ROOT / "data" / "ukrainian" / "practical-policy.json").read_text(encoding="utf-8")
    )["segments"].items() if value.get("default") is not None),
    key=len,
    reverse=True,
))


def _map_ipa(ipa: str) -> tuple[str | None, str | None]:
    """Apply the canonical longest-match IPA → Ukrainian segment policy."""
    policy = json.loads((ROOT / "data" / "ukrainian" / "practical-policy.json").read_text(encoding="utf-8"))
    rest = ipa.replace("ˈ", "").replace("ˌ", "").replace(".", "")
    output: list[str] = []
    while rest:
        if rest[0].isspace():
            output.append(rest[0])
            rest = rest[1:]
            continue
        segment = next((key for key in _SEGMENT_KEYS if rest.startswith(key)), None)
        if segment is None:
            return None, rest
        output.append(policy["segments"][segment]["default"])
        rest = rest[len(segment):]
    return "".join(output), None


class RuleBasedKhmerEngine:
    """Deterministic rule/lexicon engine for Phnom Penh careful citation Khmer."""

    profile = "khmer-pph-careful-citation-v1"
    engine_id = "khmer-deterministic-rules-v1"

    def analyze(self, text: str) -> dict[str, Any]:
        normalized = normalize_khmer(text)
        fixture = _LEXICON.get(normalized)
        if fixture is not None:
            raw_ipa = fixture.get("ipa")
            if not raw_ipa:
                return {
                    "input": text, "normalized": normalized, "profile": self.profile,
                    "engine": self.engine_id, "deterministic": True,
                    "ipa": None, "ukrainian": None, "status": fixture.get("status", "EVIDENCE_LIMITED"),
                    "rule_ids": ["KHMER_LEXICAL_FIXTURE_WITHHELD"],
                    "reason": fixture.get("note", "The lexical fixture has no established IPA value."),
                    "evidence": fixture.get("evidence", []),
                }
            ipa = raw_ipa.strip().strip("/")
            ukrainian, unsupported = _map_ipa(ipa)
            return {
                "input": text, "normalized": normalized, "profile": self.profile,
                "engine": self.engine_id, "deterministic": True,
                "ipa": ipa, "ukrainian": ukrainian,
                "status": fixture.get("status", "PROPOSED") if unsupported is None else "NOT_ESTABLISHED",
                "rule_ids": ["KHMER_LEXICAL_FIXTURE", "IPA_TO_UKRAINIAN_LONGEST_MATCH"],
                "reason": fixture.get("note", "") if unsupported is None else f"Unsupported IPA sequence: {unsupported}",
                "evidence": fixture.get("evidence", []),
                "lexical_ua_reference": fixture.get("ua"),
                "lexical_mapping_agrees": ukrainian == fixture.get("ua") if ukrainian is not None else False,
            }

        structure = analyze_structure(normalized)
        if len(structure.syllables) == 1:
            syllable = structure.syllables[0]
            if (
                syllable.get("status") == "ESTABLISHED_STRUCTURE"
                and syllable.get("base_consonant")
                and not syllable.get("subscripts")
                and not syllable.get("vowel_signs")
                and not syllable.get("independent_vowel")
            ):
                onset = syllable.get("phonology", {}).get("onset_ipa")
                register = syllable.get("register")
                if onset and register in {"first", "second"}:
                    vowel = "ɑː" if register == "first" else "ɔː"
                    ipa = onset + vowel
                    ukrainian, unsupported = _map_ipa(ipa)
                    return {
                        "input": text, "normalized": normalized, "profile": self.profile,
                        "engine": self.engine_id, "deterministic": True,
                        "ipa": ipa if unsupported is None else None,
                        "ukrainian": ukrainian,
                        "status": "PROPOSED" if unsupported is None else "NOT_ESTABLISHED",
                        "rule_ids": ["KHMER_REGISTER_SERIES_INHERENT_VOWEL", "IPA_TO_UKRAINIAN_LONGEST_MATCH"],
                        "reason": "Conservative series-based inherent-vowel rule; status remains proposed pending profile-matched adjudication.",
                        "evidence": ["unicode17-ch16", "r12a-orthography"],
                    }

        return {
            "input": text, "normalized": normalized, "profile": self.profile,
            "engine": self.engine_id, "deterministic": True,
            "ipa": None, "ukrainian": None, "status": "NOT_ESTABLISHED",
            "rule_ids": ["KHMER_UNSUPPORTED_PATTERN_WITHHELD"],
            "reason": "The recognized orthographic structure has no sufficiently established deterministic orthography-to-IPA rule in this profile.",
            "structure": structure.phonological_representation,
        }


# Backward-compatible name: this is no longer an ensemble or a model hybrid.
HybridKhmerEngine = RuleBasedKhmerEngine


def create_hybrid_engine(*_args: Any, **_kwargs: Any) -> RuleBasedKhmerEngine:
    """Compatibility factory returning the deterministic rule engine only."""
    return RuleBasedKhmerEngine()
