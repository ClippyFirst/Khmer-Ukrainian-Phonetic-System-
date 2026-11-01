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
