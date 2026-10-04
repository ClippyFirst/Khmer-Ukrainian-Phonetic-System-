# Khmer → Ukrainian Phonetic-Graphemic Correspondence System

Research-grade, evidence-backed reference implementation for Khmer orthography → Khmer phonology/phonetics → IPA → Ukrainian target correspondence.

> Status: FOUNDATION / EVIDENCE-LIMITED. Unsupported linguistic claims are not fabricated.

## Scope

Primary target: contemporary Standard Khmer with Phnom Penh-oriented pronunciation where evidence permits. Dialectal, historical and competing analyses are explicitly separated.

## Core principle

Khmer orthography → graphemic structure → phonological analysis → surface phonetics → IPA → Ukrainian target → Ukrainian orthography

This is not a Khmer romanization converter and not a character-to-character transliterator.

## Comparative practical-transcription layer

The project now includes the same comparative methodology developed for the Thai → Ukrainian project:

- Russian Khmer practical transcription is used as an evidence-supported comparator.
- Serbian is explicitly marked evidence-limited because a separate authoritative Khmer practical standard was not established in the current search.
- Bulgarian material is used only where it documents Khmer phonetic analysis; a Bulgarian Cyrillic practical standard is not claimed.
- Ukrainian output is generated from the canonical Ukrainian phonetic inventory rather than copied from Russian spelling.
- Aspiration, glottal stop, /ŋ/, /ɲ/, /ʋ~w/, /r/ and the Khmer vowel system are treated as separate source-to-target decisions.
- Phnom Penh /r/-loss is a pronunciation-profile issue, not a universal spelling substitution.

See:
- docs/comparative-cyrillic-systems.md
- docs/ukrainian-practical-transcription.md
- data/comparative/cyrillic_systems.csv
- data/ukrainian/practical_correspondence.csv

## Current scientific status

- Repository audit: completed 2026-10-02.
- Unicode/script foundation: implemented from Unicode Standard 17.0 evidence.
- Khmer register, coeng, inherent-vowel and vowel-sign structures: modelled.
- Comparative Cyrillic evidence layer: implemented.
- Proposed Ukrainian practical target layer: implemented as a research proposal.
- Canonical Ukrainian inventory remains external.
- Full empirical lexical/corpus validation: NOT ESTABLISHED.
- Narrow acoustic transcription for every lexical item: NOT ESTABLISHED.
- No accuracy percentage is claimed without an adjudicated evaluation corpus.

See docs/methodology.md, docs/evidence.md, docs/limitations.md and docs/comparative-cyrillic-systems.md.
