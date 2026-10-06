from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "khmer"

def load_json(name: str):
    with (DATA / name).open(encoding="utf-8") as f:
        return json.load(f)

CONSONANTS = load_json("consonants.json")
SIGNS = load_json("signs.json")
EVIDENCE = load_json("sources.json")
REGISTERS = load_json("registers.json")
SHIFTER_ELIGIBILITY = {
    "៉": set(REGISTERS["shifter_eligibility"]["muusikatoan"]),
    "៊": set(REGISTERS["shifter_eligibility"]["triisap"]),
}

FIRST_REGISTER = {x["char"] for x in CONSONANTS if x.get("register") == "first"}
SECOND_REGISTER = {x["char"] for x in CONSONANTS if x.get("register") == "second"}
