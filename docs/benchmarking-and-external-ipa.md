# Khmer: IPA benchmarking and external systems

**Status: benchmark harness added; empirical accuracy remains unmeasured until independently adjudicated gold rows exist.** This is not a claim that candidate engines have been installed, run, licensed for redistribution, or validated for Khmer.

## Required pipeline boundary

source orthography → structural analysis → source-language phonology → typed IPA → ClippyFirst IPA-to-Ukrainian adapter → Ukrainian practical orthography

External engines are comparators or optional upstream IPA providers only. Preserve their raw output separately from any normalized IPA. Do not bypass the ClippyFirst IPA adapter, silently rewrite an engine's proprietary phoneme alphabet as IPA, or treat agreement among engines as ground truth.

## Reproducible benchmark

The standard-library-only harness is scripts/benchmark_ipa.py. It reads tab-separated files:

- Gold columns: id, text, gold_ipa, gold_status, profile, source_id.
- Prediction columns: id, engine, raw_output, ipa, status, version.

Run from the repository root:

python scripts/benchmark_ipa.py --gold data/benchmark/gold.tsv --predictions data/benchmark/predictions.tsv --output reports/ipa-benchmark.json

Only rows with gold_status=ADJUDICATED and non-empty gold IPA enter the denominator. For each engine, every eligible gold row is counted: an absent prediction row or empty IPA is a miss and remains in the denominator. The report provides strict NFC exact match, missing-prediction rate, and code-point Levenshtein CER. NFC and outer whitespace trim are the only normalizations: tone, vowel length, diacritics, and syllable separators remain significant. Code-point CER is a diagnostic, not a feature-weighted phonetic metric. A header-only gold file correctly yields NOT_MEASURED, not a fabricated zero or 100% score. An engine with no predictions for eligible gold rows is not scored; once an engine appears in the prediction file, omitted eligible IDs count as missing.

Stratify gold cases by syllable shape, consonant class/series, vowel type and length, coda, tone/prosody where applicable, morphology, lexical/loanword status, and uncertainty. Report the denominator and source/profile per row. Avoid training/test leakage and use a held-out set for any tuning.

## External candidates (not yet approved for runtime)

- Goruut (support/version must be verified)
- eSpeak NG (language support and IPA mode must be verified)
- Khmer NLP/lexical resources (supporting tools only unless IPA is proven)

These are research leads, not verified availability claims. Before executing a candidate, record the exact release/commit, installation command, language/voice/model identifier, raw output, runtime errors, license for code plus model/dictionary/data, and whether the output is actual IPA or a tool-specific phone alphabet. Do not install or enable a candidate by default merely because it appears here.

## Acceptance gates

1. Build a versioned gold set from cited primary sources with exact page/section/audio locator, dialect/profile, and independent adjudication; Unicode tables alone do not establish pronunciation.
2. Keep raw source output immutable; store conversion rules and normalized output separately.
3. Run the same inputs/profile through ClippyFirst and each available candidate; preserve failed/missing outputs in the denominator report.
4. Evaluate both strict IPA exact match and reviewed feature-level errors (tone, vowel length/quality, onset, coda, syllable boundaries). Do not infer a winner from exact match alone.
5. Run the existing repository test/CI suite and validate the benchmark script on a synthetic fixture; do not publish synthetic scores as language accuracy.
6. Keep candidates optional, pinned, license-reviewed, and fail-closed. A missing tool must never change the core result silently.

## Current evidence status

- Harness baseline: executed successfully in prior main CI. Additional fail-closed validation now requires every ADJUDICATED row to have non-empty IPA, source_id and profile; PR #21 adds regression tests for these gates and must pass CI on its final head.
- Adjudicated language-specific gold rows: not yet established by this document.
- Candidate engine availability, version, licenses, and language-specific output quality: unverified until recorded as run evidence.
- Release status: research prototype; no accuracy claim is authorized by this registry.

## Existing external run evidence (reconciled 2026-10-24)

- Latest Khmer Phonemizer smoke: [workflow 40119620311](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40119620311), `khmerphonemizer==0.0.3`, 6 outputs, 0 runtime errors, independent gold count 0, accuracy null. Artifact ZIP SHA-256 `df7815f1a5891ed0e3ce947abf7669a47a872ca90027955ef4ac51fce06398b6`. Output is phone-token arrays; word stress and syllable separators in the source-attested IPA are not always represented, so convention mapping must be reviewed before exact-match scoring.
- The [Khmer acoustic model project](https://github.com/chemvatho/Khmer-acoustic-model) advertises a 29,204-entry pronunciation dictionary validated by native linguists; its README distinguishes MIT code/model from CC BY-SA 4.0 dictionary data. This is a promising reference lead, not an integrated or redistributed corpus. Check exact revision, file access, dialect, annotation conventions, source terms and source overlap before adopting it.
- [Goruut](https://github.com/neurlang/goruut) lists Khmer Central; this may not match the target dialect profile, and no run is recorded here.
- Next: independently adjudicate KHV-007/KHV-008 and the vowel-series/coda matrix; do not use source-attested entries as accuracy labels.


## Upstream provenance and output interpretation (checked 2026-10-24)

| Candidate | Verified upstream fact | Evidence boundary / next step |
|---|---|---|
| [khmerphonemizer 0.0.3](https://pypi.org/project/khmerphonemizer/0.0.3/) | PyPI declares MIT and describes a Khmer grapheme-to-phoneme tool; the project cites wikipron, gruut, OpenFst and Phonetisaurus among its references. | Our smoke returned six outputs with zero runtime errors. Preserve the raw phone-token arrays: they are not directly comparable as full strings to a source IPA transcription until token boundaries, syllabification, stress and IPA conventions are reconciled. Review dependency and lexical-data provenance separately. |
| [Goruut](https://github.com/neurlang/goruut) | Upstream README advertises an IPA phone set and Khmer Central support. | Support claim only; no successful Khmer run recorded here. Pin the commit and inspect raw output before adding any accuracy claim. |

The six existing source examples remain unadjudicated and are not gold. Zero independent gold rows means no accuracy percentage is permitted. A MIT code license does not automatically license all upstream lexicon/model material.


## Benchmark metric semantics — 2026-10-24

- `exact_match_rate` is strict string equality after the declared Unicode normalization and is comparable only when the same IPA profile/conventions are used. Tone, length, stress, syllable boundaries, tie bars and other IPA distinctions are not silently removed.
- `character_error_rate` is Levenshtein distance over Unicode code points, not a phoneme/segment error rate. IPA affricates, combining diacritics, length marks and tone symbols can occupy multiple code points; interpret this field as a string-distance diagnostic only.
- A valid score still requires a non-empty independently adjudicated gold set with source locator and profile. Smoke output, engineering fixtures, source-attested but unadjudicated entries, and inter-engine agreement are not accuracy.


## Source-attested notation diagnostic (not accuracy)

The optional Khmer G2P report now retains raw phoneme tokens and adds a separate source-attested notation diagnostic. It compares concatenated tokens against the cited IPA after removing only outer `/.../` wrappers, whitespace, syllable dots, and primary/secondary stress marks (`ˈ`, `ˌ`). Aspiration, length, diacritics, tie bars, and phone symbols remain significant. The report exposes strict and limited-notation counts but always leaves `independent_gold_count = 0` and `accuracy = null`. These comparisons diagnose transcription/segmentation conventions only; cited IPA is not independently adjudicated and is never treated as gold.


## Latest external smoke and source-attested comparison

The latest pinned `khmerphonemizer==0.0.3` run is [40128165807](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40128165807): 6/6 outputs, 0 runtime errors. The source-attested notation diagnostic finds 2/6 strict matches after removing only outer slash wrappers, and 6/6 after additionally ignoring whitespace, syllable dots, and stress marks. This does not establish accuracy or validate the source transcriptions; independent adjudicated gold remains absent. Artifact ZIP SHA-256: `2cbc7b00d35325e2e97fc98e80efeb9fdfecd477bf5ae5be24c43b6726c33299`.
