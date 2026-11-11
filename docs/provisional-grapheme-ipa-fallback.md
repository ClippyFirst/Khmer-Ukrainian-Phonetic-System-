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
