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


def test_verified_corpus_and_web_fixtures_agree_on_ipa():
    import json
    from pathlib import Path
    fixtures=json.loads((Path("data/tests/web-fixtures.json")).read_text(encoding="utf-8"))
    corpus=json.loads((Path("data/tests/verified-lexical-corpus.json")).read_text(encoding="utf-8"))
    for source, entry in corpus.items():
        assert source in fixtures, f"missing web fixture for verified corpus item: {source}"
        assert fixtures[source]["ipa"] == entry["ipa"], f"IPA mismatch for {source}"

def test_web_lexical_ua_overrides_match_canonical_policy():
    import json
    from pathlib import Path
    fixtures=json.loads((Path("data/tests/web-fixtures.json")).read_text(encoding="utf-8"))
    policy=json.loads((Path("data/ukrainian/practical-policy.json")).read_text(encoding="utf-8"))

    segments=sorted(policy["segments"], key=len, reverse=True)
    def render(ipa):
        text=ipa.strip("/").replace(".", "")
        out=""
        i=0
        while i < len(text):
            if text[i].isspace():
                out += text[i]
                i += 1
                continue
            match=next((s for s in segments if text.startswith(s, i)), None)
            assert match is not None, f"unsupported IPA in fixture policy audit: {text[i:]}"
            out += policy["segments"][match]["default"]
            i += len(match)
        return out

    for source, fixture in fixtures.items():
        if fixture.get("ipa") and fixture.get("ua"):
            assert render(fixture["ipa"]) == fixture["ua"], f"lexical UA override contradicts policy: {source}"
