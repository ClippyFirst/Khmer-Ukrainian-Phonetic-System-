from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class KhmerGrapheme:
    text: str
    kind: str
    codepoints: tuple[str, ...]

@dataclass
class KhmerSyllable:
    raw_text: str
    normalized_text: str
    graphemes: list[KhmerGrapheme] = field(default_factory=list)
    base_consonant: str | None = None
    register: str | None = None
    subscripts: list[str] = field(default_factory=list)
    vowel_signs: list[str] = field(default_factory=list)
    independent_vowel: str | None = None
    inherent_vowel: str | None = None
    coda: str | None = None
    phonology: dict[str, Any] = field(default_factory=dict)
    ipa: str | None = None
    features: list[dict[str, Any]] = field(default_factory=list)
    alternatives: list[dict[str, Any]] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    confidence: float = 0.0
    status: str = "EVIDENCE LIMITED"

@dataclass
class AnalysisResult:
    input: str
    normalized: str
    graphemes: list[dict[str, Any]]
    syllables: list[dict[str, Any]]
    phonological_representation: dict[str, Any]
    phonetic_representation: dict[str, Any]
    ipa: str | None
    features: list[dict[str, Any]]
    ukrainian_candidates: list[dict[str, Any]]
    selected_candidate: dict[str, Any] | None
    rules_applied: list[str]
    alternative_analyses: list[dict[str, Any]]
    sources: list[str]
    confidence: float
    status: str
