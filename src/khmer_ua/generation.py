import json
from pathlib import Path
from .data import CONSONANTS, SIGNS

def generate_inventory_snapshot() -> dict:
    return {
        "schema_version":"0.1.0",
        "data_version":"2026-10-02-foundation",
        "counts":{
            "consonants":len(CONSONANTS),
            "signs":len(SIGNS)
        },
        "status":"DETERMINISTIC_FOUNDATION"
    }

def write_inventory_snapshot(path: str) -> None:
    Path(path).write_text(json.dumps(generate_inventory_snapshot(),ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
