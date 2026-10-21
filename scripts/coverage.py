"""Generate a deterministic, evidence-gated Khmer vowel coverage inventory.

Run from the repository root:
    python scripts/coverage.py
    python scripts/coverage.py --check

The inventory reports evidence already present in the canonical registry. It never
infers pronunciation from Unicode names or structure and never labels examples gold.
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "khmer"
OUT = ROOT / "reports" / "khmer-coverage-audit.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_report(signs, consonants, registers, evidence):
    """Build the report from canonical data without modifying or adjudicating it."""
    if not isinstance(signs, list) or not isinstance(consonants, list):
        raise ValueError("signs.json and consonants.json must contain JSON arrays")
    if not isinstance(registers, dict) or not isinstance(registers.get("registers"), list):
        raise ValueError("registers.json must contain a 'registers' array")
    if not isinstance(evidence, dict) or not isinstance(evidence.get("cases"), list):
        raise ValueError("vowel-context-register.json must contain a 'cases' array")

    cases = evidence["cases"]
    dependent = [s for s in signs if s.get("kind") == "dependent_vowel"]
    independent = [s for s in signs if s.get("kind") == "independent_vowel"]
    cells = {}
    for sign in dependent:
        if not sign.get("char") or not sign.get("codepoint"):
            raise ValueError(f"Dependent vowel lacks char/codepoint: {sign!r}")
        for series in ("first", "second"):
            matches = [
                case for case in cases
                if (case.get("grapheme_structure") or {}).get("dependent_vowels") == [sign["char"]]
                and case.get("base_consonant_class") == series
            ]
            conflicts = [case for case in matches if case.get("status") == "CONFLICTING_SOURCE_ANALYSES"]
            attested = [
                case for case in matches
                if case.get("ipa") and case.get("status") == "SOURCE_ATTESTED_NOT_GOLD"
            ]
            # Conflict takes precedence: never hide a disagreement behind another row.
            status = (
                "CONFLICTING_SOURCE_ANALYSES" if conflicts else
                "SOURCE_ATTESTED_NOT_GOLD" if attested else
                "NOT_ESTABLISHED"
            )
            cells[f'{sign["codepoint"]}:{series}'] = {
                "sign": sign["char"],
                "codepoint": sign["codepoint"],
                "series": series,
                "status": status,
                "case_ids": [case.get("id") for case in matches],
                "ipa_values": [] if conflicts else sorted({case["ipa"] for case in attested}),
                "conflicting_case_ids": [case.get("id") for case in conflicts],
                "limitation": (
                    "Source-attested examples are not gold and do not establish a universal rule."
                    if status == "SOURCE_ATTESTED_NOT_GOLD" else
                    "Conflicting analyses are retained; no single value is selected."
                    if status == "CONFLICTING_SOURCE_ANALYSES" else
                    "No exact sign × series IPA evidence; do not infer from Unicode structure."
                ),
            }

    features = Counter()
    source_statuses = Counter()
    for case in cases:
        structure = case.get("grapheme_structure") or {}
        features[
            "cases_with_dependent_vowel" if structure.get("dependent_vowels")
            else "cases_without_dependent_vowel"
        ] += 1
        for field, feature in (("subscripts", "cases_with_subscript"), ("coda", "cases_with_coda")):
            value = structure.get(field)
            if value and any(value if isinstance(value, list) else [value]):
                features[feature] += 1
        if structure.get("register_shifter"):
            features["cases_with_register_shifter"] += 1
        source_text = json.dumps(structure, ensure_ascii=False) + " " + str(case.get("register_condition", ""))
        for marker in ("NIKAHIT", "REAHMUK", "COENG"):
            if marker in source_text:
                features["cases_mentioning_" + marker.lower()] += 1
        status = str(case.get("status", "UNCLASSIFIED"))
        source_statuses[status] += 1
        features["cases_" + status.lower()] += 1

    total = len(cells)
    status_counts = Counter(cell["status"] for cell in cells.values())
    conflict_cases = [case for case in cases if case.get("status") == "CONFLICTING_SOURCE_ANALYSES"]
    return {
        "schema_version": "1.0.0",
        "generated_by": "scripts/coverage.py",
        "evidence_source_file": "data/khmer/vowel-context-register.json",
        "orthographic_inventory": {
            "consonant_records": len(consonants),
            "register_records": len(registers["registers"]),
            "register_shifter_records": len(registers.get("shifters", [])),
            "dependent_vowel_signs": len(dependent),
            "independent_vowel_signs": len(independent),
            "expected_dependent_vowel_x_series_cells": total,
        },
        "dependent_vowel_by_series": cells,
        "coverage_summary": {
            "source_attested_not_gold_cells": status_counts["SOURCE_ATTESTED_NOT_GOLD"],
            "conflicting_cells": status_counts["CONFLICTING_SOURCE_ANALYSES"],
            "not_established_cells": status_counts["NOT_ESTABLISHED"],
            "coverage_fraction": round(status_counts["SOURCE_ATTESTED_NOT_GOLD"] / total, 4) if total else 0,
            "warning": (
                "First-order sign × series coverage only. This does not certify coda, length, "
                "syllable, register-shifter, lexical or pronunciation-profile contexts."
            ),
        },
        "source_registry_status_counts": dict(sorted(source_statuses.items())),
        "source_conflict_case_ids": [case.get("id") for case in conflict_cases],
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
            "independent vowels, rare signs, loanwords, malformed input",
        ],
        "interpretation": (
            "A cell is source-attested only for an exact sign and series match with an IPA value "
            "in the existing evidence register. This is SOURCE_ATTESTED_NOT_GOLD, never gold. "
            "Other cells remain NOT_ESTABLISHED; this audit generates no pronunciation. "
            "Conflicts elsewhere in the source registry are listed separately and are not "
            "misrepresented as dependent-vowel matrix conflicts."
        ),
    }


def render_report():
    return json.dumps(
        build_report(
            load(DATA / "signs.json"),
            load(DATA / "consonants.json"),
            load(DATA / "registers.json"),
            load(DATA / "vowel-context-register.json"),
        ),
        ensure_ascii=False,
        indent=2,
    ) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the committed report is missing or stale")
    args = parser.parse_args(argv)
    try:
        rendered = render_report()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"coverage audit input error: {error}", file=sys.stderr)
        return 2

    if args.check:
        if not OUT.exists():
            print(f"coverage report missing: {OUT.relative_to(ROOT)}", file=sys.stderr)
            return 1
        if OUT.read_text(encoding="utf-8") != rendered:
            print(f"coverage report is stale: run python scripts/coverage.py and review the diff", file=sys.stderr)
            return 1
        print(f"coverage report current: {OUT.relative_to(ROOT)}")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8")
    report = json.loads(rendered)
    summary = report["coverage_summary"]
    print(json.dumps({
        "output": str(OUT.relative_to(ROOT)),
        "dependent_signs": report["orthographic_inventory"]["dependent_vowel_signs"],
        "expected_cells": report["orthographic_inventory"]["expected_dependent_vowel_x_series_cells"],
        "source_attested_not_gold_cells": summary["source_attested_not_gold_cells"],
        "conflicting_cells": summary["conflicting_cells"],
        "not_established_cells": summary["not_established_cells"],
        "source_conflict_case_ids": report["source_conflict_case_ids"],
        "cases_audited": sum(report["source_registry_status_counts"].values()),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
