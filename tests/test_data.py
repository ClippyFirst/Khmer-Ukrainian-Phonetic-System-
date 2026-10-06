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
    allowed_statuses = {"PROPOSED", "EVIDENCE_LIMITED"}
    for fixture in fixtures.values():
        assert fixture["status"] in allowed_statuses
        assert "проєкт" in fixture["note"] or "проєктна" in fixture["note"]
        if fixture["status"] == "PROPOSED":
            assert fixture["ipa"].startswith("/")
            assert fixture["ua"]
        else:
            assert fixture["ipa"] is None
            assert fixture["ua"] is None

def test_fully_supported_fixture_outputs_match_canonical_policy():
    policy = json.loads((ROOT / "data/ukrainian/practical-policy.json").read_text(encoding="utf-8"))
    fixtures = json.loads((ROOT / "data/tests/web-fixtures.json").read_text(encoding="utf-8"))
    segments = sorted(policy["segments"], key=len, reverse=True)

    def render_ipa(ipa):
        text = ipa.strip("/").replace("ˈ", "").replace("ˌ", "").replace(".", "")
        out = []
        i = 0
        while i < len(text):
            if text[i].isspace():
                out.append(text[i]); i += 1; continue
            segment = next((candidate for candidate in segments if text.startswith(candidate, i)), None)
            if segment is None: return None
            out.append(policy["segments"][segment]["default"]); i += len(segment)
        return "".join(out)

    checked = 0
    for fixture in fixtures.values():
        if fixture["status"] != "PROPOSED" or not fixture["ipa"] or not fixture["ua"]: continue
        mapped = render_ipa(fixture["ipa"])
        if mapped is None: continue
        checked += 1
        assert fixture["ua"] == mapped, f'{fixture["source"]}: {fixture["ua"]!r} contradicts canonical policy {mapped!r}'
    assert checked >= 8
