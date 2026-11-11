# External IPA renderers and G2P candidates — Khmer

**Status: research registry only.** This document records candidate tools discovered during the ClippyFirst IPA-renderer survey. It does not claim that these tools are integrated, accurate, licensed for redistribution, or accepted as pronunciation gold data.

## Required integration boundary

`source orthography → source-language structure and phonology → typed IPA result → ClippyFirst IPA → Ukrainian adapter → Ukrainian practical orthography`

External systems must be treated as upstream phonetic-result providers or benchmark comparators. They must **not** bypass this repository's IPA-to-Ukrainian adapter or introduce direct source-script-to-Ukrainian fallback. Keep source output, normalized IPA, provenance, dialect/profile, syllable boundaries, tone, length, uncertainty, and competing analyses inspectable.

## Language-specific candidates

### 1. [Khmer Phonemizer](https://github.com/seanghay/khmerphonemizer)

- **Role:** G2P phonemizer
- **Status:** candidate
- **Output/validation:** Open-source MIT project; validate whether output is standard IPA or internal phoneme labels and verify vowel-series/length/coda behavior
- **License:** MIT reported upstream; preserve notices if used
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.

### 2. [ipa-dict](https://github.com/open-dict-data/ipa-dict)

- **Role:** word pronunciation dictionary
- **Status:** benchmark-resource
- **Output/validation:** Khmer (`km`) entries reported; likely useful for word-level comparison, not arbitrary-text G2P; verify transcription breadth
- **License:** Verify current repository and per-source data licenses
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.

### 3. [Goruut](https://github.com/neurlang/goruut)

- **Role:** multilingual IPA phonemizer
- **Status:** candidate
- **Output/validation:** Khmer support is claimed; validate consonant series, vowel quality/length and dialect conventions
- **License:** Verify current upstream license and model/data terms
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.


## Shared IPA display fonts

These fonts render IPA; they do **not** generate pronunciations. Prefer Unicode fonts rather than legacy non-Unicode IPA encodings.

- [Charis SIL](https://software.sil.org/charis/) — Recommended font candidate for readable IPA and combining diacritics. License: SIL Open Font License; verify current release metadata.
- [Doulos SIL](https://software.sil.org/doulos/) — IPA-focused font candidate; verify combining-diacritic rendering in target browsers. License: SIL Open Font License; verify current release metadata.
- [DejaVu Sans](https://dejavu-fonts.github.io/) — Broad Unicode/IPA fallback candidate; test exact glyph coverage on target devices. License: DejaVu license; retain upstream notices.

For the live browser UI, use a CSS font stack with an IPA-capable primary font and system fallbacks; test combining diacritics, tie bars, length marks, stress marks, tone marks, and syllable boundaries on Windows, Linux, and mobile. Do not add binary fonts to this repository until the exact font release, license notices, and distribution strategy are reviewed.

## Acceptance gates before runtime integration

1. Record the upstream commit/version, exact license, model/dictionary licenses, and source provenance.
2. Pin the dependency or provide a reproducible adapter installation procedure; no unpinned network downloads at runtime.
3. Store the external raw output separately from any normalized IPA.
4. Add language-specific conversion tests for Unicode, tones, vowel length, syllable boundaries, diacritics, unsupported input, and malformed output.
5. Compare each candidate against the same versioned, independently reviewed gold set. Report exact-match and feature-level errors separately; do not treat agreement between tools as ground truth.
6. Confirm that only a validated typed IPA result reaches the existing ClippyFirst Ukrainian adapter.
7. Keep optional tools optional: a missing third-party dependency must not break the core engine or silently trigger a fallback.

## Machine-readable registry

The companion `data/external-ipa-renderers.json` is the canonical candidate inventory for this repository. Every entry currently has `verified_in_repo: false` and `enabled_by_default: false` until an implementation and its verification evidence are committed.


## Source-script display fonts (not IPA engines)

These resources are relevant to the UI's display of the source writing system; they do not generate IPA and must not be treated as phonemizers.

- [Inter Font Extensions](https://github.com/grab/inter-font-extensions) — May improve display of the source scripts in interfaces; does not generate IPA and is not a replacement for an IPA-capable Latin font. License: Verify current upstream font and repository license.
- [Padauk](https://software.sil.org/padauk/) — Useful for Myanmar-script text shaping and coverage; not an IPA transcription engine. License: SIL Open Font License; verify current release metadata.
- [Busra](https://software.sil.org/busra/) — Khmer-script display font only; not an IPA transcription engine. License: SIL Open Font License; verify current release metadata.
- [Mondulkiri](https://software.sil.org/mondulkiri/) — Khmer-script display font only; not an IPA transcription engine. License: SIL Open Font License; verify current release metadata.


## Optional raw-output benchmark runner

`scripts/benchmark_g2p.py` can call the upstream [Khmer Phonemizer](https://github.com/seanghay/khmerphonemizer) API after a separate installation of `khmerphonemizer`. It records raw phone tokens, timing, package version, corpus hash, source-reported IPA, and per-record errors. The repository's lexical corpus is source-attested but not independently adjudicated, so the report hard-codes `independent_gold_count: 0` and `accuracy: null`. It is a diagnostic comparison tool, not an accuracy benchmark. The package remains optional and is not imported by the production runtime.


### First optional smoke run (2026-10-24)

Two smoke runs completed successfully. The first and the reproducible rerun both used `khmerphonemizer==0.0.3` and produced **6/6** raw outputs with **0 runtime errors**. The rerun records a repository-relative corpus path. Its report explicitly recorded `independent_gold_count: 0` and `accuracy: null`; this verifies API execution only, not phonetic accuracy. [First run](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40091599475) · [Pinned reproducible rerun and artifact](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40091745346).

A manual inspection of raw output highlights follow-up questions rather than scored errors: for `ខ្ញុំ`, the engine returned `k ɲ o m` while the corpus source reports `/kʰɲom/`; for `ភ្នំពេញ`, the source-reported form includes stress and a syllable boundary (`/pʰnum ˈpɨɲ/`) that are not encoded in the engine's phone-token list. Since the corpus is not independently adjudicated and output conventions differ, these are **unresolved diagnostic differences**, not accuracy labels.

## Additional Khmer G2P candidates — 2026-11-11

### BYU MATRIX / MekongPhon neural IPA model

- Model: [byumatrixlab/khmer-ipa](https://huggingface.co/byumatrixlab/khmer-ipa), a 33.6M-parameter BERT encoder–decoder with separate Khmer-input and IPA-output tokenizers.
- Model revision pinned in the optional CI workflow: `20e069d384b240da76320e1569958568c12a54bc`.
- The model card declares Apache-2.0. This does **not** settle the license of the MekongPhon training/evaluation corpus; the inspected corpus repository snapshot has no declared root license.
- The upstream MekongPhon repository also contains an experimental rule-based baseline at [training/baselines/rb_khm_to_ipa.py](https://github.com/byu-matrix-lab/MekongPhon/blob/f80f6c1840c4818b51e05f2e00cded4701a5b662/training/baselines/rb_khm_to_ipa.py). It is a separate experimental implementation, not the neural model; its root license and phonetic conventions require clarification before reuse.

### PhonSobon / NCKL pronunciation respeller

- [PhonSobon Khmer G2P](https://huggingface.co/phonsobon/khmer-g2p) is a 7.46M-parameter character Transformer. Its output is a **Khmer-script pronunciation respelling with syllable separators**, not IPA. The model card reports 83.37% validation word accuracy at epoch 150; no test result is reported there.
- The related [dataset](https://huggingface.co/datasets/phonsobon/khmer-G2P) contains 38,629 word-to-respelling pairs (37,755 unique words): 34,770 train, 1,939 validation and 1,920 test. All readings of a word are kept in one split.
- The labels are NCKL/Phnom Penh prescribed word pronunciations, not running-speech IPA and not a source for tone/phonation validation.
- The model card declares MIT, but the dataset card attributes its source to the NCKL Khmer Dictionary 2022 and asks users to check NCKL terms before commercial use. The dataset is therefore recorded as a research lead only; no data are copied into this repository and no production/commercial use is authorized by this audit.

Neither the PhonSobon respeller nor the MekongPhon rule-based baseline is enabled in the runtime. The neural IPA model is an optional comparator only; it does not replace the project's phonological analysis or IPA adapter.

MekongPhon provenance qualifier: the paper reports 1,314,779 sentence pairs expanded by longest-match lexicon lookup over OPUS from an 8,026-entry seed lexicon; a 500-entry sample was reviewed by two proficient L2 speakers, not native target-variety annotators. Its under-2% CER is therefore a source-reported dictionary-seeded result, not independent sentence-level adjudication or this project's gold accuracy.
