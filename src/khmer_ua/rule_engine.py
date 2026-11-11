"""Deterministic, rule-based Khmer → IPA → Ukrainian research engine.

No neural inference, remote service, external G2P process, voting, or runtime
model selection is performed. Unsupported structures remain visible through
a separate low-confidence grapheme preview; canonical IPA is never overwritten.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .normalize import normalize_khmer
from .parser import analyze as analyze_structure
from .practical import map_ipa_string

ROOT = Path(__file__).resolve().parents[2]
_FIXTURE_PATH = ROOT / "data" / "tests" / "web-fixtures.json"
with _FIXTURE_PATH.open(encoding="utf-8") as _handle:
    _LEXICON: dict[str, dict[str, Any]] = json.load(_handle)


def _map_ipa(ipa: str) -> tuple[str | None, str | None]:
    """Backward-compatible wrapper around the sole practical IPA adapter."""
    return map_ipa_string(ipa)


def _provisional_preview(structure: Any) -> dict[str, Any] | None:
    """Expose only registered onset IPA; never infer a vowel from an incomplete unit."""
    syllables = structure.phonological_representation.get("syllables", [])
    if not syllables:
        return None
    previews = []
    for unit in syllables:
        base = unit.get("base_consonant")
        onset = unit.get("phonology", {}).get("onset_ipa")
        if not base or not onset:
            previews.append({
                "source": unit.get("raw_text", ""),
                "ipa": None,
                "ukrainian": "?",
                "status": "UNKNOWN",
                "unresolved_graphemes": list(unit.get("raw_text", "")),
            })
            continue
        # A bare consonant with established register has an existing normal
        # inherent-vowel rule. This preview is only for units rejected by that
        # normal path because of subscripts, vowel signs or uncertain structure.
        mapped, unsupported = map_ipa_string(onset)
        rendered = mapped if unsupported is None and mapped is not None else ""
        unresolved = [
            ch for ch in unit.get("raw_text", "")
            if ch != base and ch not in {"\u200c"}
        ]
        previews.append({
            "source": unit.get("raw_text", ""),
            "ipa": onset,
            "ukrainian": rendered + ("?" if unresolved or not rendered else ""),
            "status": "PROVISIONAL" if rendered else "UNKNOWN",
            "unresolved_graphemes": unresolved or ([] if rendered else [base]),
            "warnings": ["CONSONANT_POSITION_OR_RIME_NOT_ESTABLISHED"],
            "evidence": ["unicode17-ch16", "r12a-orthography"],
        })
    if not any(item.get("ipa") for item in previews):
        return None
    return {
        "status": "PROVISIONAL",
        "ipa_preview": " ".join(item["ipa"] or "?" for item in previews),
        "ukrainian_preview": " ".join(item["ukrainian"] for item in previews),
        "syllables": previews,
        "warnings": ["LOW_CONFIDENCE", "TONE_NOT_INFERRED"],
    }


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
                    "rule_trace": ["KHMER_LEXICAL_FIXTURE_WITHHELD"],
                    "reason": fixture.get("note", "The lexical fixture has no established IPA value."),
                    "evidence": fixture.get("evidence", []),
                }
            ipa = raw_ipa.strip().strip("/")
            ukrainian, unsupported = map_ipa_string(ipa)
            return {
                "input": text, "normalized": normalized, "profile": self.profile,
                "engine": self.engine_id, "deterministic": True,
                "ipa": ipa, "ukrainian": ukrainian,
                "status": fixture.get("status", "PROPOSED") if unsupported is None else "NOT_ESTABLISHED",
                "rule_trace": ["KHMER_LEXICAL_FIXTURE", "IPA_TO_UKRAINIAN_LONGEST_MATCH"],
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
                    ukrainian, unsupported = map_ipa_string(ipa)
                    return {
                        "input": text, "normalized": normalized, "profile": self.profile,
                        "engine": self.engine_id, "deterministic": True,
                        "ipa": ipa if unsupported is None else None,
                        "ukrainian": ukrainian,
                        "status": "PROPOSED" if unsupported is None else "NOT_ESTABLISHED",
                        "rule_trace": ["KHMER_REGISTER_SERIES_INHERENT_VOWEL", "IPA_TO_UKRAINIAN_LONGEST_MATCH"],
                        "reason": "Conservative series-based inherent-vowel rule; status remains proposed pending profile-matched adjudication.",
                        "evidence": ["unicode17-ch16", "r12a-orthography"],
                    }

        preview = _provisional_preview(structure)
        return {
            "input": text, "normalized": normalized, "profile": self.profile,
            "engine": self.engine_id, "deterministic": True,
            "ipa": None, "ukrainian": None, "status": "NOT_ESTABLISHED",
            "provisional_ipa": preview["ipa_preview"] if preview else None,
            "provisional_ukrainian": preview["ukrainian_preview"] if preview else None,
            "fallback_status": preview["status"] if preview else "UNKNOWN",
            "fallback_trace": preview["syllables"] if preview else [],
            "rule_trace": ["KHMER_UNSUPPORTED_PATTERN_WITHHELD", "PROVISIONAL_ONSET_IPA_PREVIEW"],
            "reason": "Canonical IPA remains withheld. A separate low-confidence onset-only preview is offered where a registered consonant IPA is available; no vowel, coda or tone is inferred.",
            "structure": structure.phonological_representation,
        }


# Backward-compatible name: this is no longer an ensemble or a model hybrid.
HybridKhmerEngine = RuleBasedKhmerEngine


def create_hybrid_engine() -> RuleBasedKhmerEngine:
    """Compatibility factory returning the deterministic rule engine only."""
    return RuleBasedKhmerEngine()
