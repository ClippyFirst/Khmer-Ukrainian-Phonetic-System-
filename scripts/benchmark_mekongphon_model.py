#!/usr/bin/env python3
"""Benchmark the pinned MekongPhon Khmer→IPA model on its source-attested holdout.

The corpus has no independent project adjudication and its upstream repository
snapshot has no declared data license. This runner therefore records a
source-attested diagnostic only, omits source text/reference strings from the
artifact, and never reports accuracy or promotes outputs to gold.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import json
import os
import platform
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODEL_ID = "byumatrixlab/khmer-ipa"
MODEL_REVISION = "20e069d384b240da76320e1569958568c12a54bc"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "mekongphon" / "data" / "splits" / "khmer_eval.csv"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def codepoint_levenshtein(reference: str, hypothesis: str) -> int:
    """Return Levenshtein distance over Unicode code points."""
    if len(reference) < len(hypothesis):
        reference, hypothesis = hypothesis, reference
    previous = list(range(len(hypothesis) + 1))
    for i, left in enumerate(reference, 1):
        current = [i]
        for j, right in enumerate(hypothesis, 1):
            current.append(min(
                current[-1] + 1,
                previous[j] + 1,
                previous[j - 1] + (left != right),
            ))
        previous = current
    return previous[-1]


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"orth", "pron_no_tones"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("MekongPhon CSV must contain orth and pron_no_tones columns")
        rows = list(reader)
    if not rows:
        raise ValueError("MekongPhon evaluation split is empty")
    orthographies = [row["orth"] for row in rows]
    if any(not value.strip() for value in orthographies):
        raise ValueError("MekongPhon evaluation split contains empty orthographies")
    if len(orthographies) != len(set(orthographies)):
        raise ValueError("MekongPhon evaluation split contains duplicate orthographies")
    if any(not row["pron_no_tones"].strip() for row in rows):
        raise ValueError("MekongPhon evaluation split contains empty source IPA labels")
    return rows


def predict(
    orthographies: list[str],
    *,
    model_id: str = MODEL_ID,
    model_revision: str = MODEL_REVISION,
    batch_size: int = 8,
    num_beams: int = 4,
) -> tuple[list[str], dict[str, str]]:
    """Run the upstream model exactly as its model card specifies."""
    if batch_size < 1 or num_beams < 1:
        raise ValueError("batch_size and num_beams must be positive")
    try:
        import torch
        import transformers
        from transformers import AutoTokenizer, EncoderDecoderModel
    except ImportError as exc:
        raise RuntimeError(
            "Optional model dependencies missing; install the pinned benchmark requirements"
        ) from exc

    torch.set_num_threads(1)
    torch.manual_seed(0)
    model = EncoderDecoderModel.from_pretrained(model_id, revision=model_revision)
    encoder_tokenizer = AutoTokenizer.from_pretrained(
        model_id, subfolder="encoder_tokenizer", revision=model_revision
    )
    decoder_tokenizer = AutoTokenizer.from_pretrained(
        model_id, subfolder="decoder_tokenizer", revision=model_revision
    )
    model.to("cpu")
    model.eval()

    predictions: list[str] = []
    started = time.perf_counter()
    for offset in range(0, len(orthographies), batch_size):
        batch = orthographies[offset:offset + batch_size]
        inputs = encoder_tokenizer(
            batch,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128,
        )
        with torch.inference_mode():
            generated = model.generate(
                **inputs,
                max_length=128,
                num_beams=num_beams,
                early_stopping=True,
            )
        predictions.extend(
            decoder_tokenizer.decode(ids, skip_special_tokens=True)
            for ids in generated
        )
    metadata = {
        "torch_version": torch.__version__,
        "transformers_version": transformers.__version__,
        "device": "cpu",
        "batch_size": str(batch_size),
        "num_beams": str(num_beams),
        "inference_elapsed_seconds": f"{time.perf_counter() - started:.6f}",
    }
    return predictions, metadata


def build_report(
    rows: list[dict[str, str]],
    predictions: list[str],
    *,
    model_revision: str,
    corpus_sha256: str,
    runtime: dict[str, str] | None = None,
) -> dict[str, Any]:
    if len(rows) != len(predictions):
        raise ValueError("expected one prediction per input")
    if not rows:
        raise ValueError("cannot benchmark an empty corpus")

    strict_matches = 0
    total_errors = 0
    total_reference_codepoints = 0
    successful_outputs = 0
    records: list[dict[str, Any]] = []

    for index, (row, raw_output) in enumerate(zip(rows, predictions, strict=True), 1):
        orthography = row.get("orth", "")
        reference = row.get("pron_no_tones", "")
        if not orthography.strip() or not reference.strip():
            raise ValueError("every input requires non-empty orthography and source IPA")
        if not isinstance(raw_output, str):
            raise ValueError("every model prediction must be a string")

        normalized_reference = unicodedata.normalize("NFC", reference)
        normalized_output = unicodedata.normalize("NFC", raw_output)
        errors = codepoint_levenshtein(normalized_reference, normalized_output)
        reference_length = len(normalized_reference)
        exact = normalized_reference == normalized_output
        strict_matches += int(exact)
        total_errors += errors
        total_reference_codepoints += reference_length
        successful_outputs += int(bool(raw_output.strip()))

        # Do not redistribute the upstream orthography/reference dataset in CI
        # artifacts. Row order and hashes retain diagnostic traceability.
        records.append({
            "row_index": index,
            "raw_output": raw_output,
            "source_reference_sha256": hashlib.sha256(
                normalized_reference.encode("utf-8")
            ).hexdigest(),
            "strict_source_attested_match": exact,
            "codepoint_edits": errors,
            "reference_codepoints": reference_length,
            "status": "SOURCE_ATTESTED_DIAGNOSTIC_NOT_GOLD",
        })

    cer = (
        total_errors / total_reference_codepoints
        if total_reference_codepoints else None
    )
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "engine": MODEL_ID,
        "engine_revision": model_revision,
        "engine_license": "Apache-2.0 as declared by the model card",
        "corpus": "MekongPhon data/splits/khmer_eval.csv",
        "reference_field": "pron_no_tones (source-reported IPA without tone)",
        "corpus_sha256": corpus_sha256,
        "input_count": len(rows),
        "successful_outputs": successful_outputs,
        "failed_outputs": len(rows) - successful_outputs,
        "source_attested_diagnostic": {
            "strict_matches": strict_matches,
            "character_errors": total_errors,
            "reference_codepoints": total_reference_codepoints,
            "codepoint_cer": cer,
            "normalization": "Unicode NFC only",
            "interpretation": (
                "Concordance with MekongPhon source-reported pron_no_tones labels only. "
                "This is not independent gold or project accuracy."
            ),
        },
        "independent_gold_count": 0,
        "accuracy": None,
        "score_status": "SOURCE_ATTESTED_DIAGNOSTIC_NOT_ACCURACY",
        "runtime": runtime or {},
        "provenance": {
            "harness_path": "scripts/benchmark_mekongphon_model.py",
            "harness_sha256": sha256_file(Path(__file__).resolve()),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "github_event_sha": os.environ.get("GITHUB_SHA"),
            "github_ref": os.environ.get("GITHUB_REF"),
            "github_head_ref": os.environ.get("GITHUB_HEAD_REF"),
        },
        "records": records,
        "limitations": [
            "The MekongPhon source repository snapshot has no declared root license; its data are not copied into this repository or uploaded in this artifact.",
            "The model card reports Apache-2.0 for the model; this does not resolve the separate corpus-data rights.",
            "The 100-row evaluation split is source-attested, not independently adjudicated by this project.",
            "The reference field is pron_no_tones, so this run does not evaluate tone/phonation recovery.",
            "Published under-2% CER is the paper's own held-out result, not this project's measured result.",
            "Agreement with the source labels is a diagnostic, not an accuracy claim.",
        ],
    }


def write_report(path: Path, report: dict[str, Any]) -> str:
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")
    digest = sha256_file(path)
    path.with_suffix(path.suffix + ".sha256").write_text(digest + "\n", encoding="ascii")
    return digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model-id", default=MODEL_ID)
    parser.add_argument("--model-revision", default=MODEL_REVISION)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--num-beams", type=int, default=4)
    args = parser.parse_args()

    rows = load_rows(args.corpus)
    predictions, runtime = predict(
        [row["orth"] for row in rows],
        model_id=args.model_id,
        model_revision=args.model_revision,
        batch_size=args.batch_size,
        num_beams=args.num_beams,
    )
    report = build_report(
        rows,
        predictions,
        model_revision=args.model_revision,
        corpus_sha256=sha256_file(args.corpus),
        runtime=runtime,
    )
    report_sha256 = write_report(args.output, report)
    print(json.dumps({
        "input_count": report["input_count"],
        "successful_outputs": report["successful_outputs"],
        "strict_source_attested_matches": report["source_attested_diagnostic"]["strict_matches"],
        "source_attested_codepoint_cer": report["source_attested_diagnostic"]["codepoint_cer"],
        "independent_gold_count": 0,
        "accuracy": None,
        "report_sha256": report_sha256,
        "output": str(args.output),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
