import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "khmer" / "vowel-context-register.json"


def test_vowel_context_registry_has_known_statuses_and_source_references():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    sources = data["sources"]
    allowed = {
        "SOURCE_ATTESTED_NOT_GOLD",
        "CONFLICTING_SOURCE_ANALYSES",
        "NOT_ESTABLISHED",
    }
    assert data["schema_version"] == "1.0.0"
    assert data["cases"]
    seen = set()
    for case in data["cases"]:
        assert case["id"] not in seen, case["id"]
        seen.add(case["id"])
        assert case["status"] in allowed, case["id"]
        assert case["ipa_source"] in sources, case["id"]
        assert case["ukrainian_status"] == "NOT_ESTABLISHED", case["id"]
        assert case["ukrainian_adaptation"] is None, case["id"]
        if case["status"] == "CONFLICTING_SOURCE_ANALYSES":
            # Conflicting source conventions must never be silently collapsed
            # into one IPA result or a Ukrainian output.
            assert case["ipa"] is None, case["id"]
            assert len(case.get("alternatives", [])) >= 2, case["id"]
            assert case.get("selection_criterion", "").strip(), case["id"]
            for alternative in case["alternatives"]:
                if "source" in alternative:
                    assert alternative["source"] in sources, case["id"]
        elif case["status"] == "SOURCE_ATTESTED_NOT_GOLD":
            assert case["evidence_level"] == "SOURCE_ATTESTED_NOT_GOLD", case["id"]
            assert case.get("limitations"), case["id"]
