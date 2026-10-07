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
| /c/ | ть | ть |
| /cʰ/ | ч | ч / тьх |
| /ɲ/ | нь | нь |
| /ŋ/ | нг | нг |
| /r/ | р | — |
| /ʋ/ | в | — |
| /w/ | у | — |
| /h/ | х | х |
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

`npm install` followed by `npm test` and `npm run build`

The structural web test verifies the two-page architecture, canonical research-data imports, explicit unresolved states, and the absence of duplicated linguistic mapping tables in the browser adapter. The production build is generated with Vite.

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


## Latest transcription-audit status — 2026-10-06

The current implementation includes explicit handling for Khmer register shifters (៉ / ៊), the exceptional ប៉ construction, coeng-based clusters and adversarial regression fixtures. The canonical Ukrainian policy currently proposes /c/ → **ть**, /cʰ/ → **ч**, /h/ → **х**, /ʋ/ → **в** and /w/ → **у**. These remain project-specific decisions, not an official Ukrainian standard.

The web explanation and browser adapter have been synchronized with that policy. The browser does not silently invent Phnom Penh /r/-loss phonetics or complete vowel IPA where the research engine has not established them.

The latest GitHub Actions quality and Pages deployment runs for the current main commit completed successfully. This verifies the repository checks and static build/deployment pipeline; it does not constitute linguistic accuracy evidence. No empirical accuracy percentage is claimed.


## Latest lexical-coverage pass — 2026-10-06

The public service's previous `ភាសាខ្មែរ` → `NOT_ESTABLISHED` result was a **coverage gap**, not evidence that the pronunciation was unknown. Current independent references give the phrase as **[pʰiəsaː kʰmae]**. The repository now contains a small provenance-bearing lexical corpus and a dedicated fixture for this common form. The IPA evidence is marked WELL_SUPPORTED; the Ukrainian practical form **пієса кмае** remains explicitly PROPOSED.

The Ukrainian policy was also extended for /ae/, and the browser adapter now distinguishes a corpus-defined lexical Ukrainian form from a mechanical segment-by-segment rendering. This prevents the UI from silently presenting a different practical spelling merely because a phrase contains context-dependent or complex Khmer vowels.


## Adversarial long-input handling — 2026-10-06

The browser adapter evaluates long Khmer inputs **per orthographic unit** rather than assigning one global fallback to the entire input.

- established lexical fixtures remain visible inside mixed/adversarial text;
- unsupported units are marked locally as `NOT_ESTABLISHED`;
- malformed Unicode sequences are marked locally as `INVALID_OR_UNSUPPORTED`;
- `EVIDENCE_LIMITED` is propagated to the overall status without suppressing valid neighboring results;
- lexical Ukrainian overrides are checked against the canonical IPA → Ukrainian policy and cannot silently contradict it;
- misplaced Khmer register shifters are explicitly flagged rather than treated as ordinary vowel/consonant data.

This behaviour is a deliberate research-integrity requirement: one unresolved case must not hide evidence-backed results elsewhere in the same test input.
