# Evidence and provenance

The repository separates **script/orthographic evidence** from **phonological and phonetic evidence**. A Unicode specification can establish how Khmer is encoded and structured; it does not, by itself, establish the IPA realization of a consonant or vowel.

## Source hierarchy

1. peer-reviewed experimental phonetics/phonology;
2. specialist grammars and monographs;
3. specialist orthography/phonology references;
4. Unicode Standard for encoding and script structure;
5. authoritative dictionaries/corpora and geographic-name standards;
6. practical-transcription references;
7. general web explanations.

A lower-level source cannot silently override a higher-level source.

## Current core sources

- Unicode 17.0 Chapter 16 — script and encoding structure: consonant inventory, coeng, register classes, vowel signs and independent vowels.
- Ishida (2026) — modern orthography, register-conditioned vowel behavior, syllable structure and IPA-oriented descriptive inventory.
- Chem & Chem (2020) — acoustic evidence for the Phnom Penh/standard Khmer vowel system.
- Henderson (1952) — historically important description of register/pronunciation.
- Wayland et al. (2005) and Kirby (2014) — contemporary evidence on /r/-loss and associated phonetic changes.
- UNGEGN — comparative Khmer romanization/transliteration reference.
- Russian practical transcription — comparative convention only; its present repository record is explicitly secondary until primary source scans are verified.

## Claim statuses

- ESTABLISHED
- WELL_SUPPORTED
- ANALYSIS_DEPENDENT
- DIALECT_DEPENDENT
- UNCERTAIN
- DISPUTED
- NOT_ESTABLISHED

## Evidence rule

Every machine-readable phonetic claim should carry a provenance ID. Orthographic facts and phonetic analyses must not share a source label merely because the source mentions both topics.


## Verified lexical corpus — 2026-10-06

A first small cross-source lexical corpus has now been added at `data/tests/verified-lexical-corpus.json`. It is intentionally separate from the proposed Ukrainian target layer. The initial entries include `ភាសាខ្មែរ`, `ខ្មែរ`, `ភាសា`, `ខ្ញុំ`, `ភ្នំពេញ` and `កម្ពុជា`.

For `ភាសាខ្មែរ`, independent current references converge on **[pʰiəsaː kʰmae]** / **/pʰiəsaː kʰmae/**. The IPA claim is therefore marked WELL_SUPPORTED, while the Ukrainian form remains PROPOSED. The corpus must not be read as evidence that the Ukrainian form is normative.

The browser fixture for `ភាសាខ្មែរ` now uses this lexical evidence rather than requiring the incomplete general orthography → IPA engine to reconstruct the phrase from scratch. This is an explicit lexical coverage layer, not a bypass that changes the research architecture.
