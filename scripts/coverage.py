"""Generate an evidence-gated Khmer orthography/IPA coverage inventory.

Run from repository root: python scripts/coverage.py
This audits recorded evidence only; it never infers IPA from Unicode structure.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "khmer"
OUT = ROOT / "reports" / "khmer-coverage-audit.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    signs = load(DATA / "signs.json")
    consonants = load(DATA / "consonants.json")
    registers = load(DATA / "registers.json")
    evidence = load(DATA / "vowel-context-register.json")
    cases = evidence.get("cases", [])
    dependent = [s for s in signs if s.get("kind") == "dependent_vowel"]
    independent = [s for s in signs if s.get("kind") == "independent_vowel"]
    cells = {}
    for sign in dependent:
        for series in ("first", "second"):
            matches = [c for c in cases
                       if (c.get("grapheme_structure") or {}).get("dependent_vowels") == [sign["char"]]
                       and c.get("base_consonant_class") == series]
            attested = [c for c in matches if c.get("ipa") and c.get("status") == "SOURCE_ATTESTED_NOT_GOLD"]
            conflict = [c for c in matches if c.get("status") == "CONFLICTING_SOURCE_ANALYSES"]
            status = "SOURCE_ATTESTED_NOT_GOLD" if attested else (
                "CONFLICTING_SOURCE_ANALYSES" if conflict else "NOT_ESTABLISHED")
            cells[f'{sign["codepoint"]}:{series}'] = {
                "sign": sign["char"], "codepoint": sign["codepoint"], "series": series,
                "status": status, "case_ids": [c.get("id") for c in matches],
                "ipa_values": [c.get("ipa") for c in attested],
                "limitation": ("Examples are not a complete lexical or dialect-normalized rule."
                               if attested else "No exact sign × series IPA evidence; do not infer from Unicode structure.")
            }
    features = Counter()
    for case in cases:
        st = case.get("grapheme_structure") or {}
        features["cases_with_dependent_vowel" if st.get("dependent_vowels") else "cases_without_dependent_vowel"] += 1
        subs = st.get("subscripts")
        if subs and any(subs if isinstance(subs, list) else [subs]):
            features["cases_with_subscript"] += 1
        coda = st.get("coda")
        if coda and any(coda if isinstance(coda, list) else [coda]):
            features["cases_with_coda"] += 1
        if st.get("register_shifter"):
            features["cases_with_register_shifter"] += 1
        text = str(st) + " " + str(case.get("register_condition", ""))
        for feature in ("NIKAHIT", "REAHMUK", "COENG"):
            if feature in text:
                features["cases_mentioning_" + feature.lower()] += 1
        features["cases_" + str(case.get("status", "UNCLASSIFIED")).lower()] += 1
    total = len(cells)
    covered = sum(v["status"] == "SOURCE_ATTESTED_NOT_GOLD" for v in cells.values())
    report = {
        "schema_version": "1.0.0",
        "generated_by": "scripts/coverage.py",
        "evidence_source_file": "data/khmer/vowel-context-register.json",
        "orthographic_inventory": {
            "consonant_records": len(consonants), "register_records": len(registers),
            "dependent_vowel_signs": len(dependent), "independent_vowel_signs": len(independent),
            "expected_dependent_vowel_x_series_cells": total
        },
        "dependent_vowel_by_series": cells,
        "coverage_summary": {
            "source_attested_not_gold_cells": covered,
            "conflicting_cells": sum(v["status"] == "CONFLICTING_SOURCE_ANALYSES" for v in cells.values()),
            "not_established_cells": sum(v["status"] == "NOT_ESTABLISHED" for v in cells.values()),
            "coverage_fraction": round(covered / total, 4) if total else 0,
            "warning": "First-order sign × series coverage only. This does not certify coda, length, syllable, register-shifter, lexical or pronunciation-profile contexts."
        },
        "recorded_case_feature_counts": dict(sorted(features.items())),
        "dimensions_requiring_followup": [
            "inherent vowels × consonant series × lexical context",
            "each dependent vowel × series × length × open/closed syllable",
            "coda identity and coda-conditioned vowel quality",
            "NIKAHIT and REAHMUK, including lexical exceptions/conflicts",
            "COENG clusters and orthographic versus phonetic syllabification",
            "MUUSIKATOAN/TRIISAP and exceptional ប៉ construction",
            "standard versus Phnom Penh /r/-loss profiles with positive and negative examples",
            "/c/ versus /cʰ/ preserved in IPA before target adaptation",
            "independent vowels, rare signs, loanwords, malformed input"
        ],
        "interpretation": "A cell is source-attested only for an exact sign and series match with an IPA value in the existing evidence register. This is SOURCE_ATTESTED_NOT_GOLD, never gold. Other cells remain NOT_ESTABLISHED; this audit generates no pronunciation."
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUT.relative_to(ROOT)), "dependent_signs": len(dependent),
                      "expected_cells": total, "source_attested_not_gold_cells": covered,
                      "not_established_cells": total-covered, "cases_audited": len(cases)},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
