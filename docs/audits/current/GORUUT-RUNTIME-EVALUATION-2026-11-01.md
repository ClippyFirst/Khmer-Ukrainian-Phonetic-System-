# Goruut runtime evaluation — Khmer — 2026-11-01

## Execution

- Upstream: [neurlang/goruut](https://github.com/neurlang/goruut), pinned commit `b224bde02151f8f86d0fe260804e4ca743bda620`.
- Language identifier: `KhmerCentral`; explicitly enabled in `BuiltinDictLanguages`.
- Runtime: Go 1.23.12, HTTP `POST /tts/phonemize/sentence`.
- Test-only checkout; no upstream model/dictionary assets copied into this repository or production bundle.
- Effective config SHA-256: `d2f19f923da8ca089ba9133465018903263f681b57a1177152ab07f2a284225e`.

## Results

1. Eight engineering/source-coverage probes returned syntactically valid `Words` responses (8/8).
2. Six source-attested lexical probes from the repository's existing reference corpus returned 6/6 responses.
3. Strict NFC/outer-whitespace-only concordance with source-attested IPA: 1/6 exact. This is **not accuracy**: the reference rows are source-attested, not independently adjudicated.
4. The one exact match is `ខ្ញុំ` → `kɲom`.
5. Clear incomplete outputs include:
   - `ខ្មែរ`: Goruut `kʰr`; source-attested IPA `kʰmae`.
   - `ភ្នំពេញ`: Goruut `pʰɲ`; source-attested IPA `pʰnum ˈpɨɲ`.
   - `ភាសាខ្មែរ`: Goruut `pʰiəsaːkʰr`; source-attested IPA `pʰiəsaː kʰmae`.
6. The server log repeatedly reports `weights9.bin.zlib: file does not exist`. Successful HTTP responses therefore conceal missing/incomplete phonetic output on several words.

## Interpretation

**Do not integrate Goruut as the Khmer production phonology provider.** The 8/8 API response rate is misleading if read as phonetic success: five of six source-attested comparisons differ, including missing vowel/consonant material in several outputs. This is a raw comparator only. No independent, project-owned, expert-adjudicated Khmer gold exists yet.

## Evidence and artifacts

- Optional runtime workflow: [41308068228](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41308068228) (initial completed source-attested comparison); latest exact-head run is tracked by PR #101.
- Artifact includes engineering probes, source-attested diagnostic, and server log; retention is 30 days.
- Accuracy remains null; independent gold count remains 0.


## Repeatability follow-up — 2026-11-01

Each input was sent three times to the same server:

- Engineering probes: 8/8 had usable outputs; all 8 were identical across all three repetitions.
- Source-attested IPA probes: 6/6 had outputs; all 6 were stable across repetitions. Strict exact concordance remained 1/6 (16.7%), not accuracy and not gold.
- The stable but incomplete forms remain: `ខ្មែរ` → `kʰr` vs source `kʰmae`; `ភ្នំពេញ` → `pʰɲ` vs source `pʰnum ˈpɨɲ`; `ភាសាខ្មែរ` → `pʰiəsaːkʰr` vs source `pʰiəsaː kʰmae`.

Three-repeat evidence: [workflow 41309092017](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41309092017). Effective config SHA-256 `d2f19f923da8ca089ba9133465018903263f681b57a1177152ab07f2a284225e`; source-attested fixture SHA-256 `506d8d1fef6a7ad3568ddca3c6b4f2d88c3ab0edd7ac328204530edcfe186dc6`.

**Disposition:** deterministic output is a positive runtime property, but low source-attested concordance and clearly incomplete outputs block production integration.


## Additional comparator: khmerphonemizer 0.0.3 — 2026-11-01

The existing optional Khmer G2P workflow was run on the same six source-attested lexical entries:

- 6/6 usable outputs; no runtime errors.
- Strict string match with source-reported IPA: 2/6.
- Limited notation-normalized match: 6/6. The diagnostic removes only outer IPA slash wrappers, whitespace, syllable dots and stress marks; it preserves phone symbols, aspiration, length, diacritics and tie bars.
- No independent gold exists, so these are source-attested concordance counts, not accuracy.

The Goruut three-repeat run on the same six entries returned 6/6 outputs, all stable; strict match 1/6 and limited notation-normalized match 3/6. Examples: `ខ្មែរ` is `kʰr` from Goruut versus `kʰmae` from khmerphonemizer and source IPA; `ភ្នំពេញ` is `pʰɲ` from Goruut versus `pʰnumpɨɲ` from khmerphonemizer. This makes khmerphonemizer the stronger comparator on this tiny source-attested sample, but not a validated production engine.

Evidence: [Khmer G2P workflow 41310119616](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41310119616); [Goruut workflow 41310119556](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41310119556). Independent gold remains 0.


## Model-asset warning interpretation

The runtime log warning is not yet causally diagnosed: the pinned Khmer Central language module contains `weights8.bin.zlib`, while the server logs an attempt to open `weights9.bin.zlib`; no such `weights9` asset was found in the pinned repository tree. This may be a shared optional model path, but that has not been proven. The incomplete outputs are independently observed in the raw IPA comparisons.


## Exact-head three-repeat runtime evidence — 2026-11-01

The exact current PR #101 head `eeeede50447c41df30f866bcbf77f56824b40190` was executed in GitHub Actions, including a clean pinned-source Go build and three HTTP requests per input.

- Runtime workflow: [41310808284](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41310808284); artifact [13085376947](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41310808284/artifacts/13085376947); ZIP SHA-256 `34330aac3be84a438a7bdc181d715f12b745cfe6f7e15edcd4be08dcbfeb52da`.
- Engine `b224bde02151f8f86d0fe260804e4ca743bda620`, Go `1.23.12`, language `KhmerCentral`, effective config SHA-256 `d2f19f923da8ca089ba9133465018903263f681b57a1177152ab07f2a284225e`.
- Engineering probes: 8/8 usable and reproducible across all three repetitions.
- Source-attested lexical probes: 6/6 usable and reproducible across all three repetitions. Strict concordance: **1/6 (16.7%)**; limited notation-only diagnostic (removing outer IPA wrappers, whitespace, syllable dots and stress marks while preserving phones, aspiration, length and diacritics): **3/6 (50%)**. Neither measure is accuracy; source rows are not independently adjudicated.
- Critical incomplete outputs are stable: `ខ្មែរ` → `kʰr` vs source-attested `kʰmae`; `ភ្នំពេញ` → `pʰɲ` vs `pʰnum ˈpɨɲ`; `ភាសាខ្មែរ` → `pʰiəsaːkʰr` vs `pʰiəsaː kʰmae`. These are missing vowel/word material, not merely notation differences.
- The server logs `weights9.bin.zlib: file does not exist`; the pinned Khmer Central tree contains `weights8.bin.zlib`, not `weights9.bin.zlib`. Causality is unproven; the incomplete strings are directly visible in the raw response.

**Disposition: reject Goruut as a Khmer production phonology provider; retain only as an optional raw-output comparator.** Independent adjudicated Khmer gold remains 0.


## Upstream cause of nondeterministic dictionary selection — Khmer

Pinned Goruut source explains the instability signal. In [parts_of_speech_selector_service.go](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/repo/services/parts_of_speech_selector_service.go#L168-L205), `SelectE` counts multiple dictionary pronunciations for a word; when more than one exists it increments the escape counters. If the homograph selector has not marked a `preferred` pronunciation, the fallback loop iterates the dictionary mapping and selects a dictionary pronunciation; the upstream source comment explicitly describes this as random selection when no homograph model is available. The [sentence use case](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/usecases/phonemize_usecase.go#L84-L85) exposes those counters as `RandomizationWordsCount` and `RandomizationWordsChoices` in the HTTP response.

The latest artifact had no RandomizationWordsCount / RandomizationWordsChoices metadata on any of the 14 inputs; all 14 were stable across three repetitions. Its problem is different: stable but incomplete dictionary output (e.g. missing vowels), not the homograph-selection instability observed in Lao/Burmese.

This gives a source-level explanation for the observed unstable cases. It does **not** establish that the separate `weights9.bin.zlib` warning causes the selection behavior; that warning remains independently unresolved. The project does not patch Goruut or choose a random pronunciation as acceptable output. Any result carrying these ambiguity counters should remain flagged as non-deterministic/ambiguous for downstream use.


## 100-row MekongPhon source-coverage evaluation — 2026-11-01

The exact PR #101 head `b47522f46b68ab61432a9010cebf23048cae501b` ran the pinned 100-row `khmer_eval.csv` with three Goruut requests per input:

- Runtime workflow: [41311611360](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41311611360); artifact [13085627015](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41311611360/artifacts/13085627015); ZIP SHA-256 `30988a1aae36261f94319286c0815b184f5effb633527f79d07e6011334d19aa`.
- Input SHA-256 `3d93a49c0162b5de4374c51d742fab0d2f5f975251c09664faefc9870535df49`; engine `b224bde02151f8f86d0fe260804e4ca743bda620`; Go `1.23.12`; config SHA-256 `d2f19f923da8ca089ba9133465018903263f681b57a1177152ab07f2a284225e`.
- 97/100 inputs returned at least one phonetic token; 3/100 returned an empty Words array. Of the 97 responses, 96 were stable across three repetitions and one (`ជួត`) was unstable.
- Source coverage was independently re-analysed from `PrePunct`, `CleanWord`, and `PostPunct`. A row counts complete only if these fields reconstruct the original input after NFC/whitespace removal and no letters, combining marks or numbers are relegated to PrePunct/PostPunct. Result: **70/100 complete**, **27/100 partial**, **3/100 no output**. This is a source-preservation check, not a phonetic correctness score.
- 27 partial cases include examples where the engine emits only a suffix or prefix as phonetic output and stores remaining Khmer letters in punctuation fields, e.g. `បេះបិទ` → CleanWord `ទ`, PrePunct `បេះបិ`, Phonetic `t`; `ថួន` → CleanWord `ន`, PrePunct `ថួ`, Phonetic `n`. The API's non-empty Phonetic response therefore substantially overstates usable coverage.
- Strict source-attested concordance: **6/100 (6%)**; limited notation diagnostic: also 6/100. These are not accuracy or gold agreement. The source field is MekongPhon's generated `pron_no_tones`, not independent expert gold.
- The one unstable input `ជួត` carried `RandomizationWordsCount=1`, `RandomizationWordsChoices=2`; the other 99 did not show that metadata.

This 100-row result supersedes any implication that the 6-row sample represents general Khmer coverage. Goruut is rejected as a production Khmer provider. The new harness source-coverage gate is being added so such partial responses cannot be counted as fully usable in future reports.
