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

## Latest smoke artifact refresh — 2026-10-25

The current-main optional smoke [40129500995](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40129500995) succeeded; inspected artifact [12574167928](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40129500995/artifacts/12574167928), ZIP SHA-256 `da53268c5d66ba3e2e5682029deb4bd6c2566466fbd920d72a6e3d9cab322f33`. JSON reports schema 1.1, `khmerphonemizer==0.0.3`, Python 3.12.15, corpus SHA-256 `4b0fafa4a178c0a3e769ddb168f2115cd1fda0c98919c3bc2d731c13cbe6a7f4`, six inputs, six outputs, zero runtime errors, independent gold 0 and accuracy null. Source-attested comparison has 2/6 strict matches and 6/6 after limited removal of slash wrappers, whitespace, syllable dots and stress marks only. This is notation concordance, not accuracy; aspiration, length, diacritics, tie bars and phone symbols remain significant. Registry now records this as latest run while preserving previous runs.

## Final current-main smoke after trigger-scope fix — 2026-10-25

After merging the workflow trigger-scope fix, current-main optional smoke [40133705156](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40133705156) passed. Inspected artifact [12575459926](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40133705156/artifacts/12575459926), ZIP SHA-256 `ff588e5d6a0e533aa4de7427e4786672f03999c3f7131abb1c89cb828936a677`. Report schema 1.1; khmerphonemizer 0.0.3; Python 3.12.15; corpus SHA-256 `4b0fafa4a178c0a3e769ddb168f2115cd1fda0c98919c3bc2d731c13cbe6a7f4`; 6 inputs, 6 outputs, 0 errors, gold 0, accuracy null. Source-attested notation diagnostic remains 2/6 strict and 6/6 after limited removal of wrappers, whitespace, syllable dots and stress. This is not accuracy.

The optional smoke workflow now excludes evidence-registry and benchmark-document paths from automatic push triggers; manual dispatch and executable input/script/workflow changes still run it. This prevents evidence-only registry updates from retriggering a new smoke run.


## Goruut comparator — upstream verified, execution pending (2026-11-01)

**Disposition: ADD AS AN OPTIONAL RAW-OUTPUT COMPARATOR; NOT APPROVED AS A PRODUCTION PHONOLOGY PROVIDER.**

- Upstream repository: https://github.com/neurlang/goruut
- Pinned upstream source commit inspected: `b224bde02151f8f86d0fe260804e4ca743bda620` (2026-10-02; pin this commit rather than `@latest`).
- Upstream README explicitly lists **Khmer Central** support and advertises an IPA phone set, word-level tokens, punctuation preservation and tonal phones. It explicitly says syllable tokens are not provided, tie bars are not supported, and numbers/dates are unsupported and should be written as words. Khmer Central must not be assumed to represent every Khmer dialect/register used by this project.
- The upstream source-code repository contains an MIT license. This verifies the code license only; the license and provenance of each embedded dictionary, model, training corpus and generated language asset have not yet been audited. Do not redistribute those assets or treat the MIT code license as clearing them.
- Upstream requires Go 1.22 or newer. Advertised Khmer Central support is not evidence of accuracy for Khmer vowel registers, inherent vowels, register shifters, codas, lexical exceptions or the project's target dialect profile.

**Additional Khmer candidate triage:** `khmer-nlp-kcc` advertises a learned Khmer G2P method returning phone-token arrays, but those tokens are not established as IPA; the model checkpoint is downloaded on first use and its weights/data licensing must be audited independently of the MIT code license. Keep it as a research lead, not a directly scoreable IPA engine. The existing `khmerphonemizer==0.0.3` remains the pinned runnable baseline; its token-array output and source-attested IPA comparisons are not accuracy evidence.

**Benchmark treatment:** run Goruut only in a disposable optional CI job; preserve raw response, errors, exact upstream commit, language identifier, Go version, corpus hash and output artifact. Keep raw output separate from any IPA normalization. Do not synthesize syllable boundaries or tie bars, strip tone, or convert output to target Ukrainian without an explicit reviewed mapping. Its lack of syllable tokens/tie-bar support and number/date handling must be reported as representational limitations, not silently repaired.

**Acceptance before promotion:** (1) successful pinned execution on the same source-located Khmer inputs as existing comparators; (2) inspect exact raw output and errors; (3) audit licenses/provenance for Khmer dictionary/model assets; (4) review register, vowel quality, inherent-vowel deletion, coda, syllabification, dialect and IPA conventions against independent expert-adjudicated IPA; (5) score only held-out ADJUDICATED gold. Current independent gold count remains 0, so no accuracy or engine ranking is available.

Upstream evidence: https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/README.md ; https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/LICENSE ; https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/go.mod ; https://github.com/rinabuoy/khmer-nlp-kcc


## Goruut language-asset license gate — 2026-11-01

The language-specific embedded files in Goruut's pinned source tree are derived from separate language lexicons: its own `dicts/README.md` describes `lexicon.tsv` as word-to-IPA training data and the generated model files as embedded assets. The corresponding Khmer Central lexicon directory is `neurlang/dataset/khmer/central/`. The dataset repository metadata has no declared license (`license: null`), its root tree contains no LICENSE/COPYING file, and its README's partial license inventory does not assign a license/provenance to this language directory. Therefore the Goruut source MIT license is insufficient to clear the lexicon or derived model. Runtime execution and artifact retention remain BLOCKED pending per-language provenance/license clarification and owner-approved use terms. Full review: `docs/audits/current/GORUUT-ASSET-LICENSE-REVIEW-2026-11-01.md`.
