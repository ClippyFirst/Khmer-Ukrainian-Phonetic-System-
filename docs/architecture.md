# Architecture

The active architecture is:

Khmer Unicode
→ normalization
→ orthographic graphemes
→ orthographic-syllable structure
→ consonant class/register + vowel-sign analysis
→ source phonology
→ contextual phonetics / IPA
→ Ukrainian target candidates
→ Ukrainian practical orthography.

## Authoritative layers

- data/khmer/: Khmer linguistic and orthographic data.
- data/comparative/: external practical-transcription comparisons.
- data/ukrainian/: project-specific Ukrainian target policy.
- schemas/: machine-readable structural contracts.
- src/khmer_ua/: deterministic implementation.
- tests/: regression and structural validation.
- docs/: methodology and public specification.

There is deliberately no copied Ukrainian phonetic inventory: the canonical Ukrainian inventory is an external dependency.

## Important boundary

Orthographic parsing can be deterministic even when phonetic realization is not. A parser result such as "second-series consonant + vowel sign" is therefore not equivalent to an IPA claim.

## Current implementation status

Implemented:
- Unicode normalization;
- conservative grapheme parsing;
- coeng/subscript recognition;
- consonant register metadata;
- independent/dependent vowel recognition;
- structural validation;
- comparative Cyrillic layer;
- proposed Ukrainian target renderer.

Not yet complete:
- full lexical orthography-to-IPA engine;
- exhaustive vowel-sign matrix;
- corpus-derived candidate ranking;
- empirical Ukrainian benchmark.
