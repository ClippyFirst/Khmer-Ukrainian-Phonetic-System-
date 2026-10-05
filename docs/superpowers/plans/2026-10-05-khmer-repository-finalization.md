# Khmer Repository Finalization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Finalize the Khmer → Ukrainian research repository by correcting evidence provenance, formalizing the source-to-IPA-to-Ukrainian pipeline, adding a defensible vowel model, strengthening implementation/tests, and cleaning/documenting the repository without deleting valuable history.

**Architecture:** Keep one authoritative Khmer data layer under `data/khmer/`, a proposed Ukrainian target layer under `data/ukrainian/`, comparative evidence under `data/comparative/`, and small Python modules that consume those data. Preserve the distinction between orthographic structure, phonology, phonetics/IPA, and practical Ukrainian output.

**Tech Stack:** Python 3.11+, setuptools, pytest, JSON/CSV, GitHub.

**Spec:** User-supplied MASTER PROMPT in the conversation.

## Global Constraints
- Do not fabricate linguistic evidence, standards, accuracy, or tests.
- Russian practice is a comparator, not a Ukrainian template.
- Serbian/Bulgarian claims remain evidence-limited unless authoritative standards are verified.
- Canonical Ukrainian phonetic inventory remains external; do not duplicate it.
- Practical output is a project proposal, not an official Ukrainian standard.
- Do not delete unique research evidence merely because it is historical.
- No GitHub Actions or unrelated UI work.

## Review Focus
- Khmer vowel-sign + consonant-series interactions must not be reduced to one-to-one sign mappings.
- /r/-loss must remain pronunciation-profile dependent.
- Unicode/script facts must not be cited as phonetic evidence.
- Aspirated consonants must remain explicit in research representation even when neutralized in practical Ukrainian spelling.
- Unknown/unsupported signs and sequences must fail conservatively rather than silently fabricate IPA.

### Task 1: Evidence and repository integrity
**Files:** modify `data/khmer/consonants.json`, `data/khmer/sources.json`, `docs/evidence.md`, `docs/limitations.md`, `.gitignore`; create `docs/repository-audit.md`.
- [ ] Correct source provenance so Unicode supports orthographic facts, while phonetic IPA claims cite phonetic/phonological literature.
- [ ] Record current tree/history assessment and classify existing artifacts.
- [ ] Verify no accidental foreign/temporary files are present.

### Task 2: Khmer vowel and phonology data model
**Files:** create `data/khmer/vowels.json`, `data/khmer/phonology.json`, `docs/phonology.md`; modify `src/khmer_ua/phonology.py`, `src/khmer_ua/model.py`.
- [ ] Represent vowel signs, independent vowels, inherent-vowel series, contextual dimensions, and evidence/status without pretending every spelling has a unique IPA.
- [ ] Add explicit states for established structure vs analysis-dependent realization.
- [ ] Preserve length and complex-vowel information in research data.

### Task 3: IPA/practical rendering integration
**Files:** modify `src/khmer_ua/practical.py`, `src/khmer_ua/parser.py`, `src/khmer_ua/cli.py`; create `src/khmer_ua/ipa.py`, `tests/test_ipa.py`.
- [ ] Add structured segment rendering rather than raw unvalidated IPA-string mapping.
- [ ] Keep careful and Phnom Penh colloquial profiles distinct.
- [ ] Add conservative handling for unsupported phonetic sequences.
- [ ] Export usable functions through the package only if verified.

### Task 4: Validation corpus and regression coverage
**Files:** create `data/tests/khmer_cases.json`, `tests/test_corpus.py`, `docs/validation.md`; modify existing tests as needed.
- [ ] Cover ordinary syllables, coeng clusters, independent vowels, register shifters, malformed input, /ŋ/, /ɲ/, aspiration, glottal stop, and profile-sensitive /r/.
- [ ] Add provenance/status per test case where linguistic output is asserted.
- [ ] Run the complete suite locally and report exact results.

### Task 5: Documentation consolidation
**Files:** revise `README.md`, `docs/architecture.md`, `docs/methodology.md`, `docs/comparative-cyrillic-systems.md`, `docs/ukrainian-practical-transcription.md`; create `docs/system-specification.md`, `docs/implementation.md`, `docs/references.md`.
- [ ] Make one coherent public research narrative.
- [ ] Clearly separate facts, interpretations, and project decisions.
- [ ] Document the current status, limitations, usage, and data sources.
- [ ] Ensure all internal links point to existing files.

### Task 6: Final audit and release hygiene
**Files:** modify any files required by audit.
- [ ] Verify tree, references, schema consistency, package imports, CLI behavior, tests, and documentation.
- [ ] Review git diff/history for accidental artifacts.
- [ ] Do not claim research-ready if major phonological/empirical gaps remain.
