# Khmer → Ukrainian Phonetic-Graphemic Correspondence System

Research-grade reference implementation for developing a **Ukrainian practical system for transmitting Khmer in Ukrainian Cyrillic**.

> **Status: FOUNDATION / EVIDENCE-LIMITED.** The repository explicitly distinguishes established script facts, linguistic analyses, project decisions and unresolved cases.

## What this project is

The active research pipeline is:

**Khmer orthography → graphemic structure → phonology → surface phonetics / IPA → Ukrainian target → Ukrainian orthography**

It is **not** a Khmer character-to-character transliterator and it is not primarily a Khmer romanization converter.

The practical Ukrainian layer is a project proposal. It is not an official Ukrainian national standard.

## Scope

Primary variety: contemporary Standard Khmer, with Phnom Penh-oriented pronunciation where evidence supports it.

The project separates:

- orthographic structure;
- phonological interpretation;
- phonetic/IPA realization;
- pronunciation profiles;
- practical Ukrainian representation;
- established lexical forms.

## Current methodology

The repository follows the research architecture established for the broader Asian-language → Ukrainian project family:

1. reconstruct source orthography;
2. identify the source phonological structure;
3. model contextual phonetic realization;
4. compare existing practical transcription traditions;
5. derive Ukrainian candidates from the Ukrainian target inventory;
6. select practical Ukrainian spellings using explicit constraints;
7. validate against a provenance-bearing corpus.

Russian Khmer practical transcription is a **comparator**, not a template for Ukrainian. Serbian and Bulgarian evidence is retained only at the strength actually established.

## Current Ukrainian policy

Examples of the proposed practical target layer:

| Khmer IPA | Ukrainian default | Russian-compatible alternative |
|---|---|---|
| /p/ | п | — |
| /pʰ/ | п | пх |
| /t/ | т | — |
| /tʰ/ | т | тх |
| /k/ | к | — |
| /kʰ/ | к | кх |
| /c/ | ч | ть |
| /cʰ/ | ч | ч / тьх |
| /ɲ/ | нь | нь |
| /ŋ/ | нг | нг |
| /r/ | р | — |
| /ʋ~w/ | в | у / в by source tradition |
| /h/ | г | х |
| /ʔ/ | ∅ | context-dependent |

These are **project decisions**, not claims of official Ukrainian usage. Aspiration remains explicit in the research/IPA layer even when it is neutralized in default practical spelling.

## Vowels

Khmer has a substantially richer vowel system than Ukrainian, and a written vowel sign can have different realizations after first- and second-series consonants. The repository therefore does not use a simple sign → vowel-letter table.

The current evidence-backed vowel model records:

- first/second-series inherent vowels;
- short/long vowel distinctions;
- complex vowels;
- series-conditioned realization;
- vowel harmony as an analysis-dependent factor;
- stress/reduction as a pronunciation-profile factor;
- coda effects such as NIKAHIT and REAHMUK.

The complete lexical vowel-sign × context → IPA matrix is still an open research task.

## Repository structure

- data/khmer/ — Khmer orthographic and phonological evidence.
- data/comparative/ — Russian/Serbian/Bulgarian/Ukrainian comparative material.
- data/ukrainian/ — proposed Ukrainian target policy.
- data/tests/ — provenance-bearing validation cases.
- schemas/ — machine-readable schemas.
- src/khmer_ua/ — implementation.
- tests/ — regression tests.
- docs/ — methodology, system specification, implementation, validation and references.

## Use

Install the package in a Python 3.11+ environment and run the test suite with pytest.

The public API exposes:

- analyze()
- render_ipa_profile()
- map_segment()
- map_sequence()
- explain_segment()

The current parser intentionally returns an explicit NOT ESTABLISHED state instead of inventing IPA where the complete source-language analysis is not implemented.

## Research status

Implemented:

- Unicode normalization;
- conservative Khmer grapheme parsing;
- coeng/subscript recognition;
- consonant class/register metadata;
- independent/dependent vowel recognition;
- structural Unicode validation;
- comparative Cyrillic research layer;
- proposed Ukrainian practical target layer;
- pronunciation-profile abstraction;
- evidence registry and provenance-bearing test corpus.

Not yet established:

- complete orthography-to-IPA conversion for every Khmer vowel combination;
- corpus-calibrated Ukrainian candidate ranking;
- empirical accuracy;
- a normative Ukrainian Khmer transcription standard.

## Documentation

- docs/methodology.md
- docs/phonology.md
- docs/system-specification.md
- docs/comparative-cyrillic-systems.md
- docs/ukrainian-practical-transcription.md
- docs/implementation.md
- docs/validation.md
- docs/evidence.md
- docs/references.md
- docs/limitations.md
- docs/repository-audit.md

## Research integrity

No accuracy percentage is reported without an adjudicated gold-standard corpus.

When evidence is insufficient, the system records **EVIDENCE LIMITED**, **ANALYSIS DEPENDENT**, **DIALECT DEPENDENT**, or **NOT ESTABLISHED** rather than fabricating a result.
