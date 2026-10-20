import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_reahmuk_lexical_examples_preserve_source_evidence_without_claiming_gold():
    data = json.loads(
        (ROOT / "data/tests/reahmuk-lexical-examples.json").read_text(encoding="utf-8")
    )
    assert data["source_id"] == "r12a-orthography"
    assert data["source_url"] == "https://r12a.github.io/scripts/khmr/km.html"
    assert data["evidence_status"] == "SOURCE_ATTESTED_NOT_INDEPENDENTLY_ADJUDICATED"
    assert "not normalized project IPA" in data["transcription_policy"]
    assert len(data["examples"]) >= 8

    required = {
        "id", "orthography", "gloss", "source_transcription",
        "source_description", "base_series", "rhyme_pattern", "source_outcome_label",
    }
    ids = set()
    for row in data["examples"]:
        assert required <= set(row), row.get("id")
        assert row["id"] not in ids
        ids.add(row["id"])
        assert row["source_transcription"]
        assert row["source_outcome_label"]
        assert row["orthography"].endswith("ះ")
    assert any(row["orthography"] == "សេះ" and row["source_outcome_label"] == "eh" for row in data["examples"])
    assert any(row["orthography"] == "នេះ" and row["source_outcome_label"] == "ih" for row in data["examples"])
    assert any(row["orthography"] == "កោះ" and row["source_outcome_label"] == "ah" for row in data["examples"])
    assert any(row["orthography"] == "គោះ" and row["source_outcome_label"] == "uə̆h" for row in data["examples"])
    assert data["limitations"]
