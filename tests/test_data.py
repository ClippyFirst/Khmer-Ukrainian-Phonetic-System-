import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_canonical_ukrainian_policy_is_complete():
    policy = json.loads((ROOT / "data/ukrainian/practical-policy.json").read_text(encoding="utf-8"))
    assert policy["status"] == "PROPOSED"
    for segment in ("p", "pʰ", "t", "tʰ", "k", "kʰ", "c", "cʰ", "ɲ", "ŋ", "h", "ʔ", "i", "əj", "iə", "uə"):
        assert segment in policy["segments"]
        assert "default" in policy["segments"][segment]
    assert policy["segments"]["c"]["default"] == "ть"
    assert policy["segments"]["cʰ"]["default"] == "ч"
    assert policy["segments"]["h"]["default"] == "х"
    assert policy["segments"]["w"]["default"] == "у"
    assert all("compatibility_ru" in policy["segments"][segment] for segment in ("pʰ", "tʰ", "kʰ", "ɲ", "ŋ", "h", "c", "cʰ"))


def test_web_fixtures_have_explicit_status_and_provenance_note():
    fixtures = json.loads((ROOT / "data/tests/web-fixtures.json").read_text(encoding="utf-8"))
    assert fixtures
    for fixture in fixtures.values():
        assert fixture["status"] == "PROPOSED"
        assert fixture["ipa"].startswith("/")
        assert fixture["ua"]
        assert "проєкт" in fixture["note"] or "проєктна" in fixture["note"]
