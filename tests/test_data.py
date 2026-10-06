import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_canonical_ukrainian_policy_is_complete():
    policy = json.loads((ROOT / "data/ukrainian/practical-policy.json").read_text(encoding="utf-8"))
    assert policy["status"] == "PROPOSED"
    for segment in ("p", "pʰ", "t", "tʰ", "k", "kʰ", "ɲ", "ŋ", "h", "ʔ", "i", "əj"):
        assert segment in policy["segments"]
        assert "default" in policy["segments"][segment]
        assert "compatibility_ru" in policy["segments"][segment]


def test_web_fixtures_have_explicit_status_and_provenance_note():
    fixtures = json.loads((ROOT / "data/tests/web-fixtures.json").read_text(encoding="utf-8"))
    assert fixtures
    for fixture in fixtures.values():
        assert fixture["status"] == "PROPOSED"
        assert fixture["ipa"].startswith("/")
        assert fixture["ua"]
        assert "проєкт" in fixture["note"] or "проєктна" in fixture["note"]
