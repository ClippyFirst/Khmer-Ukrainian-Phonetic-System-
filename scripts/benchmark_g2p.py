#!/usr/bin/env python3
"""Run Khmer Phonemizer as an optional raw-output baseline.

Install separately with: python -m pip install khmerphonemizer
Run: python scripts/benchmark_g2p.py --output artifacts/khmer-g2p.json

This runner is diagnostic only. The repository's source-attested lexical corpus is
not independent gold, so this script deliberately emits no accuracy score.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "data" / "tests" / "verified-lexical-corpus.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_corpus(path: Path) -> dict[str, dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not value:
        raise ValueError(f"Expected a non-empty JSON object in {path}")
    for word, entry in value.items():
        if not isinstance(word, str) or not word or not isinstance(entry, dict):
            raise ValueError("Each corpus entry must map a non-empty word to an object")
    return value


def package_version(name: str) -> str | None:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def phoneme_tokens(value: Any) -> list[str] | None:
    """Extract phone tokens without inventing separators or rewriting IPA."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple)) and all(isinstance(item, str) for item in value):
        return list(value)
    if isinstance(value, tuple) and len(value) == 2:
        candidate = value[1]
        if isinstance(candidate, (list, tuple)) and all(isinstance(item, str) for item in candidate):
            return list(candidate)
    return None


def build_report(
    corpus: dict[str, dict[str, Any]],
    outputs: list[dict[str, Any]],
    *,
    package: str,
    version: str | None,
    corpus_path: str,
    corpus_sha256: str,
) -> dict[str, Any]:
    if len(outputs) != len(corpus):
        raise ValueError("One output record is required for each corpus entry")
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "engine": package,
        "engine_version": version,
        "python_version": platform.python_version(),
        "corpus_path": corpus_path,
        "corpus_sha256": corpus_sha256,
        "input_count": len(corpus),
        "successful_outputs": sum(row.get("error") is None and row.get("raw_output") is not None for row in outputs),
        "failed_outputs": sum(row.get("error") is not None for row in outputs),
        "independent_gold_count": 0,
        "accuracy": None,
        "interpretation": (
            "Raw external output only. Corpus IPA is source-attested but not independently adjudicated; "
            "it is not gold. No accuracy metric is computed."
        ),
        "records": outputs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, default=ROOT / "artifacts" / "external-g2p" / "khmer-phonemizer.json")
    args = parser.parse_args()
    try:
        from khmerphonemizer import phonemize_single
    except ImportError:
        parser.error(
            "Optional dependency missing. Install in a separate environment with "
            "'python -m pip install khmerphonemizer'; core runtime does not depend on it."
        )

    corpus = load_corpus(args.corpus)
    records: list[dict[str, Any]] = []
    for word, metadata in corpus.items():
        started = time.perf_counter()
        try:
            raw = phonemize_single(word)
            tokens = phoneme_tokens(raw)
            error = None if tokens is not None else f"Unexpected output type: {type(raw).__name__}"
        except Exception as exc:
            raw, tokens, error = None, None, f"{type(exc).__name__}: {exc}"
        records.append({
            "input": word,
            "engine": "khmerphonemizer",
            "raw_output": raw,
            "phone_tokens": tokens,
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
            "source_reported_ipa": metadata.get("ipa"),
            "source_evidence_status": metadata.get("evidence_status", "UNSPECIFIED"),
            "source_ids_or_urls": metadata.get("sources", []),
            "comparison_status": "NOT_SCORED_NO_INDEPENDENT_GOLD",
            "error": error,
        })

    report = build_report(
        corpus,
        records,
        package="khmerphonemizer",
        version=package_version("khmerphonemizer"),
        corpus_path=str(args.corpus),
        corpus_sha256=sha256_file(args.corpus),
    )
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps({key: report[key] for key in (
        "engine", "engine_version", "input_count", "successful_outputs",
        "failed_outputs", "independent_gold_count", "accuracy"
    )}, ensure_ascii=False, indent=2))
    print(f"Raw-output report: {args.output}")
    return 0 if report["successful_outputs"] > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
