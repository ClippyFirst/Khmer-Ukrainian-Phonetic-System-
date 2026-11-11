# Provisional Khmer grapheme-to-IPA fallback

Status: design contract; implementation pending.

## Purpose

Mirror the Lao hybrid's typed, low-confidence grapheme fallback without weakening the Khmer engine's established orthography-to-IPA path. This is a rendering-coverage feature, not a claim that every grapheme has a context-free pronunciation.

## Required pipeline

Khmer grapheme cluster / recognized positional unit → provisional IPA token(s) → the existing IPA-to-Ukrainian adapter → Ukrainian text with a visible `?` uncertainty marker.

Never map Khmer code points directly to Ukrainian letters. Provisional IPA must be typed `PROVISIONAL`, carry source grapheme, positional role, rule ID and evidence, and must not be counted as supported IPA in benchmarks.

## Eligibility and limits

- Reuse parser-confirmed base-consonant identity and already registered onset IPA hints only.
- A consonant's inherent-vowel class/series must not be inferred from a naked code point when the parser has not established the relevant series.
- Vowel signs, subscripts, coeng, independent vowels, register shifts and diacritics may be emitted as provisional IPA only when a source-backed, positional rule explicitly covers the complete grapheme unit.
- Do not infer tone from incomplete orthographic structure.
- Unknown or non-core signs remain explicit unknown markers; do not silently drop them.
- Keep full-confidence IPA/Ukrainian fields unchanged. Expose fallback separately, e.g. `provisional_ipa`, `provisional_ukrainian`, `fallback_status`, and `fallback_trace`.

## Confidence and rendering contract

- `SUPPORTED`: normal engine path only.
- `UNCERTAIN`: structurally complete IPA with a known uncertainty.
- `PROVISIONAL`: grapheme-position hint, low confidence; append `?` to the Ukrainian rendering of the affected unresolved unit.
- `UNKNOWN`: no registered IPA hint; render `?` only, with the source grapheme preserved in trace.

Provisional values must not be promoted to canonical `ipa`, and must be excluded from IPA accuracy scoring. Browser and Python must return the same text and trace.

## Acceptance

1. Source registry entries for each fallback rule include language variety, grapheme/position, IPA hint, scope, primary source and review status.
2. Parser tests cover consonant series, vowel signs, subscripts/coeng, independent vowels, punctuation, mixed scripts and unknown symbols.
3. Python and browser parity tests cover the same fixtures.
4. Tests assert that unsupported marks remain visible as uncertainty and no tone is invented.
5. Full CI and built-site Chromium tests pass.
6. Report rendering coverage separately from supported IPA coverage and phonetic accuracy.

## Current evidence boundary

The existing engine's partial Khmer parser and the practical IPA adapter are not themselves a source-backed grapheme fallback inventory. Do not manufacture IPA hints from the Ukrainian practical table. Until positional Khmer rules are registered and sourced, unsupported constructions remain `UNKNOWN`.


## Implementation checkpoint — 2026-11-11

A minimal onset-only fallback is now implemented in the Python rule engine and browser engine.

- Reuses the parser's registered base-consonant onset IPA and the existing IPA → Ukrainian adapter.
- Keeps canonical ipa and ukrainian fields withheld when the full unit is unresolved.
- Exposes provisional_ipa, provisional_ukrainian, fallback_status and fallback_trace in Python; browser units carry PROVISIONAL, an onset-only IPA display and a visible ?.
- Does not infer vowel, coda, subscripts, coeng realization or tone.
- Added Python regression for កា and browser source-contract assertions.

Status: PARTIAL, not DONE_VERIFIED. The current hint is an onset-position consonant only, not a full grapheme inventory. The parser's current evidence IDs are reused; a dedicated rule registry with per-entry primary-source locators, explicit positional scope and reviewer status is still required. Browser tests currently assert the fallback contract in source; they do not yet execute a Python/JavaScript parity fixture against identical structured results.

Implementation commits: 61e0246cf34e0319f72c9b04c5926b6e3b3ad1f5 (Python engine), 352c22a55f526877dd136a982b2aa5ac03ff3838 (Python regression), 862aa061726b2bae6296199e4b655334bb6f609a (browser), 660915e4ed1f44eab04258957eee39537883aadd (browser regression). Exact-head CI runs 43099931373 and 43099931284 were queued at the last check; neither is recorded as passed.


## Scope correction — 2026-11-11

The fallback is a separate diagnostic preview, not a replacement for canonical IPA or Ukrainian output. The browser keeps the canonical unresolved marker in the main result and shows the onset-only preview in per-unit analysis details. The regression fixture is a consonant with an unresolved coeng/subscript structure (ក្ក), not ကា: the latter already follows the existing inherent-vowel rule and must not be treated as unresolved.
