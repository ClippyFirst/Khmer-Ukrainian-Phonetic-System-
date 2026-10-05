# System specification

## Purpose

Map Khmer orthographic input through linguistically explicit intermediate representations to a practical Ukrainian Cyrillic output.

## Pipeline

Khmer Unicode → normalization → grapheme structure → orthographic syllable → consonant class/register and vowel interpretation → phonology → pronunciation profile / IPA → Ukrainian target → practical Ukrainian orthography.

## Output modes

- research: preserve source IPA/phonological distinctions where established;
- practical: use the proposed Ukrainian target policy;
- compatibility_ru: expose selected Russian-compatible forms for comparison;
- established_form: allow provenance-bearing lexical overrides.

## Core policy

The system is not a character-to-character transliterator. A written Khmer vowel sign is interpreted in context, especially consonant class/register, syllable structure and coda environment.

## Current limitations

The full vowel matrix and corpus-derived candidate ranking are not yet complete. Unsupported sequences must remain explicitly unresolved.
