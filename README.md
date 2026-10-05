# Khmer → Ukrainian Phonetic-Graphemic Correspondence System

Research-grade reference implementation for developing a **Ukrainian practical system for transmitting Khmer in Ukrainian Cyrillic**.

> **Status: RESEARCH FOUNDATION + LOCAL WEB SERVICE.** The repository explicitly distinguishes established script facts, linguistic analyses, project decisions and unresolved cases. The web service is deliberately conservative: it exposes supported phoneticizations and marks uncovered forms instead of silently guessing.

## What this project is

The active research pipeline is:

**Khmer orthography → graphemic structure → phonology → surface phonetics / IPA → Ukrainian target → Ukrainian orthography**

It is **not** a Khmer character-to-character transliterator and it is not primarily a Khmer romanization converter.

The practical Ukrainian layer is a project proposal. It is not an official Ukrainian national standard.

## Web service

The repository now contains the two-page public web layer:

- `index.html` — the Khmer → Ukrainian service.
- `system.html` — explanation of the author's practical transcription system.

The visual direction is intentionally based on **Cambodia's blue, red and white national palette**, used as controlled accents within an editorial, typographic research-tool design. The structure follows the user's established Chinese service pattern while keeping Khmer-specific linguistic logic independent.

The browser service is:

- static and local-first;
- free of runtime API dependencies;
- free of analytics/telemetry;
- Unicode-safe for Khmer and Ukrainian;
- explicit about `PROPOSED`, `EVIDENCE_LIMITED` and `NOT_ESTABLISHED` states;
- backed by the repository's research policy rather than duplicated UI-only correspondence tables.

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

- `data/khmer/` — Khmer orthographic and phonological evidence.
- `data/comparative/` — Russian/Serbian/Bulgarian/Ukrainian comparative material.
- `data/ukrainian/` — proposed Ukrainian target policy.
- `data/tests/` — provenance-bearing validation cases.
- `schemas/` — machine-readable schemas.
- `src/khmer_ua/` — implementation.
- `tests/` — regression tests.
- `docs/` — methodology, system specification, implementation, validation and references.
- `index.html` / `system.html` — static web service.

## Web development

The web layer is dependency-light and uses native browser APIs. The included structural check can be run with:

`npm test`

It verifies the presence of the two-page architecture, the real browser engine adapter, explicit unresolved states, and the documented pronunciation profiles.

The web requirements are frozen in:

- `docs/superpowers/specs/2026-10-05-khmer-web-service-requirements.md`

## Python package

Install the package in a Python 3.11+ environment and run the research test suite with pytest.

The public API exposes:

- `analyze()`
- `render_ipa_profile()`
- `map_segment()`
- `map_sequence()`
- `explain_segment()`

The current research parser intentionally returns an explicit NOT ESTABLISHED state instead of inventing IPA where the complete source-language analysis is not implemented.

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
- evidence registry and provenance-bearing test corpus;
- two-page static web service;
- conservative browser adapter with explicit unresolved states;
- Cambodia-oriented visual design system;
- structural web tests.

Still not established as a complete linguistic engine:

- complete orthography-to-IPA conversion for every Khmer vowel combination;
- corpus-calibrated Ukrainian candidate ranking;
- empirical accuracy;
- a normative Ukrainian Khmer transcription standard.

Accordingly, the web service is **production-structured but linguistically coverage-limited**. It must not be marketed as a complete automatic Khmer transliterator until the full orthography → IPA matrix and adjudicated corpus are completed.

## Documentation

- `docs/methodology.md`
- `docs/phonology.md`
- `docs/system-specification.md`
- `docs/comparative-cyrillic-systems.md`
- `docs/ukrainian-practical-transcription.md`
- `docs/implementation.md`
- `docs/validation.md`
- `docs/evidence.md`
- `docs/references.md`
- `docs/limitations.md`
- `docs/repository-audit.md`
- `docs/superpowers/specs/2026-10-05-khmer-web-service-requirements.md`

## Research integrity

No accuracy percentage is reported without an adjudicated gold-standard corpus.

When evidence is insufficient, the system records **EVIDENCE LIMITED**, **ANALYSIS DEPENDENT**, **DIALECT DEPENDENT**, or **NOT ESTABLISHED** rather than fabricating a result.
