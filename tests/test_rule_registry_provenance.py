"""Keep the machine-readable Khmer rule registry source-traceable.

These checks validate evidence metadata only. They do not establish that a
phonological rule is empirically correct or that the source covers every
lexical environment.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "khmer"


def test_rule_registry_has_unique_ids_valid_sources_and_specific_locators():
    rules = json.loads((DATA / "rules.json").read_text(encoding="utf-8"))
    sources = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))
    assert rules
    source_ids = [source["id"] for source in sources]
    assert len(source_ids) == len(set(source_ids)), "source IDs must be unique"
    source_by_id = {source["id"]: source for source in sources}

    rule_ids = [rule["rule_id"] for rule in rules]
    assert len(rule_ids) == len(set(rule_ids)), "rule IDs must be unique"
    for rule in rules:
        rid = rule["rule_id"]
        assert rule["source"] in source_by_id, (rid, rule["source"])
        assert rule["domain"] in {"orthography", "orthography_to_phonology", "phonology", "target_adaptation"}, rid
        assert rule["input"].strip(), (rid, "input is empty")
        assert rule["output"].strip(), (rid, "output is empty")
        assert rule["source_locator"].strip(), (rid, "source locator is empty")
        assert rule["status"] in {
            "ESTABLISHED", "WELL_SUPPORTED", "ANALYSIS_DEPENDENT",
            "DIALECT_DEPENDENT", "CONTEXT_DEPENDENT", "UNCERTAIN",
            "DISPUTED", "NOT_ESTABLISHED", "UNSUPPORTED",
        }, (rid, rule["status"])
        source = source_by_id[rule["source"]]
        assert source["url"].startswith("https://"), (rid, source["url"])
        # The rule must not point only to a generic source title; its locator
        # must identify a section, table, code point, or equivalent scope.
        locator = rule["source_locator"].lower()
        assert any(token in locator for token in (
            "§", "section", "table", "u+", "chapter", "page", "pp.",
        )), (rid, rule["source_locator"])


def test_register_rule_does_not_claim_a_complete_contextual_ipa_mapping():
    rules = json.loads((DATA / "rules.json").read_text(encoding="utf-8"))
    by_id = {rule["rule_id"]: rule for rule in rules}
    for rule_id in ("R-NIKAHIT", "R-REAHMUK"):
        rule = by_id[rule_id]
        assert rule["status"] != "ESTABLISHED"
        assert "requires_context" in rule["output"]
    # The register-shifter row documents a script/register distinction, not a
    # deterministic vowel/IPA realization for every lexical environment.
    shifter = by_id["R-REGISTER-SHIFTER"]
    assert shifter["output"] == "register_change"
    assert shifter["source_locator"].endswith("Table 16-6")


def test_kirby_2015_phnom_penh_audio_resources_have_scoped_rights_and_limits():
    sources = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))
    by_id = {source["id"]: source for source in sources}

    audio = by_id["kirby2015-audio"]
    assert audio["doi"] == "10.7488/ds/321"
    assert audio["license"] == "CC BY 4.0"
    assert "16" in audio["scope"] and "speakers" in audio["scope"]
    assert "ipa gold" in audio["limitations"].lower() and "not" in audio["limitations"].lower()

    supplementary = by_id["kirby2015-supplementary"]
    assert supplementary["doi"] == "10.7488/ds/319"
    assert supplementary["license"] == "CC BY 4.0"
    assert "anonymised" in supplementary["scope"].lower()
    assert "ipa gold" in supplementary["limitations"].lower() and "not" in supplementary["limitations"].lower()


def test_transcription_agreement_method_sources_are_not_misrepresented_as_khmer_gold():
    sources = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))
    by_id = {source["id"]: source for source in sources}

    cucchiarini = by_id["cucchiarini1996-agreement"]
    assert cucchiarini["doi"] == "10.3109/02699209608985167"
    assert "percentage agreement" in cucchiarini["scope"].lower()
    assert "not a khmer-specific" in cucchiarini["limitations"].lower()

    oller = by_id["oller-ramsdell2006-weighted-reliability"]
    assert oller["doi"] == "10.1044/1092-4388(2006/100)"
    assert "eight coders" in oller["scope"].lower()
    assert "does not implement" in oller["limitations"].lower() and "exact algorithm" in oller["limitations"].lower()


def test_woznica_thesis_is_scoped_as_multi_region_evidence_not_phnom_penh_gold():
    sources = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))
    by_id = {source["id"]: source for source in sources}
    thesis = by_id["woznica2013"]
    assert thesis["year"] == 2013
    assert thesis["url"] == "https://repozytorium.amu.edu.pl/items/07609606-333b-4603-95f3-3cb14c1eb083"
    assert "80" in thesis["scope"] and "speakers" in thesis["scope"]
    assert "not statistically representative" in thesis["limitations"].lower()
    assert "not a Phnom Penh-only" in thesis["limitations"]
