import json
from pathlib import Path

from khmer_ua.parser import analyze


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "data" / "tests" / "register-shifter-contract.json"


def test_shared_register_shifter_contract_matches_python_parser():
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert fixture["schema_version"] == 1
    for case in fixture["cases"]:
        result = analyze(case["surface"])
        assert result.syllables, case["id"]
        syllable = result.syllables[0]
        assert syllable["register"] == case["register"], case["id"]
        assert syllable["phonology"].get("register_shifter") == case["rule"], case["id"]
        assert syllable["status"] == case["status"], case["id"]
