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
    for rule in rules:
        if rule["rule_id"] in {"R-NIKAHIT", "R-REAHMUK", "R-REGISTER-SHIFTER"}:
            assert rule["status"] != "ESTABLISHED" or rule["domain"] == "orthography"
            if rule["domain"] == "orthography_to_phonology":
                assert any(word in rule["output"] for word in ("requires_context", "register_change"))
