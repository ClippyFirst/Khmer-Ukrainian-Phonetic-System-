# Khmer romanization → Ukrainian orthographic matrix

**Status:** PARTIAL — a Latin-output package is integrated, but it is not a complete implementation of the selected romanization standard and does not yet produce a Ukrainian result from a canonical syllable crosswalk.
**Primary variety:** contemporary Standard Khmer, Phnom Penh-oriented only where supported.

## Standard selection

Select **BGN/PCGN 1972 Romanization of Khmer (Cambodian)** as the reference romanization profile. It is the strongest defensible choice for a source-backed research table: the UNGEGN Working Group report states that the UN-recommended system was approved in 1972 (Resolution II/10) and is based on the BGN/PCGN 1972 system. The official PCGN guide was checked for validity in October 2017 and contains consonant, subscript, vowel, diacritic and numeral tables.

Primary sources:
- UNGEGN, Report on the Current Status of United Nations Romanization Systems for Geographical Names (2013), Khmer section: https://unstats.un.org/unsd/ungegn/working_groups/wg5/documents/wgrr4khmer.pdf
- UK PCGN, Romanization of Khmer (Cambodian), BGN/PCGN 1972 Agreement (checked October 2017): https://assets.publishing.service.gov.uk/media/5ab4e25aed915d78bc23451e/ROMANIZATION_OF_KHMER.pdf

UNGEGN notes that Khmer is an alphasyllabic script, that the romanization requires contextual rules, that word division is not ordinarily indicated, and that the system is generally not reversible. Thus “transliterate everything” means **cover every supported orthographic unit with an explicit table row or an explicit exception state**; it does not mean that the Latin output alone can reconstruct all Khmer code points.

## Existing implementation audit

The current @gmana/km-translit 0.1.2 integration is documented as **BGN/PCGN-derived ASCII**, drops diacritics and is not a fully conformant BGN/PCGN implementation. It is useful as an existing romanization candidate but cannot be called the selected standard implementation or the final complete orthographic mode. It must remain separately labelled until replaced or proven equivalent against the official table.

The current romanization card is independent from IPA → Ukrainian conversion. It does not yet expose a complete romanization → Ukrainian syllable adapter. The current one-row smoke test only proves that a sample produces Latin letters; it does not prove table coverage, reversibility, standard conformance or Ukrainian conversion.

## Consonant and subscript crosswalk (source-backed romanization; Ukrainian target is a project proposal)

The machine-readable consonant matrix is [data/khmer/romanization_ukrainian.csv](../data/khmer/romanization_ukrainian.csv). It records all 22 official PCGN consonant-table rows plus the special ឝ row, source code-point sequences, BGN/PCGN forms, Ukrainian candidate, evidence status, URL and row locator. The CSV is authoritative for this consonant slice; it is not a complete vowel/rime matrix.

| PCGN table row | Khmer base / subscript forms | BGN/PCGN romanization | Ukrainian candidate | Status |
|---|---|---|---|---|
| 1 | ក / គ; corresponding feet | k | к | PROPOSED |
| 2 | ខ / ឃ; corresponding feet | kh | к' | PROPOSED |
| 3 | ង; corresponding foot | ng | нг | PROPOSED |
| 4 | ច / ជ; corresponding feet | ch | ч | PROPOSED |
| 5 | ឆ / ឈ; corresponding feet | chh | ч' | PROPOSED |
| 6 | ញ; corresponding foot | nh | нь | PROPOSED |
| 7 | ដ / ឌ; corresponding feet | d | д | PROPOSED |
| 8 | ឋ / ឍ; corresponding feet | th | — | ANALYSIS_DEPENDENT |
| 9 | ថ / ធ; corresponding feet | th | — | ANALYSIS_DEPENDENT |
| 10 | ណ / ន; corresponding feet | n | н | PROPOSED |
| 11 | ត / ទ; corresponding feet | t | т | PROPOSED |
| 12 | ប; corresponding foot | b, p (contextual) | — | ANALYSIS_DEPENDENT |
| 13 | ព; corresponding foot | p | п | PROPOSED |
| 14 | ផ / ភ; corresponding feet | ph | п' | PROPOSED |
| 15 | ម; corresponding foot | m | м | PROPOSED |
| 16 | យ (no foot) | y | й | PROPOSED |
| 17 | រ; corresponding foot | r | р | PROPOSED |
| 18 | ឡ / ល; foot for ល only | l | л | PROPOSED |
| 19 | វ; corresponding foot | v | в | PROPOSED |
| 20 | ស; corresponding foot | s | с | PROPOSED |
| 21 | ហ; corresponding foot | h | г | PROPOSED |
| 22 | អ; corresponding foot | ’ | — | EVIDENCE_LIMITED |

The machine-readable matrix [data/khmer/romanization_ukrainian.csv](../data/khmer/romanization_ukrainian.csv) preserves the exact source sequences, the 22 PCGN table row IDs, the Ukrainian candidate/status, the official URL and row-level locator. It intentionally does not invent a Ukrainian output for the contextual b/p row, the th rows or the glottal-onset marker. PCGN explicitly states that there is no subscript form for ឡ; the row-18 record captures this.


## Vowel matrix: contextual source table, not a one-sign substitution table

The official PCGN guide has separate tables for independent vowels, dependent vowel signs (with â-/ô-series and normal/shortened columns), and vowels with anusvara or visarga. The following source inventory reproduces the romanization values and deliberately leaves target values unassigned where a direct Ukrainian orthographic decision has not been reviewed.

**Independent vowel characters**

| PCGN row | Khmer | BGN/PCGN romanization | Ukrainian candidate | Status |
|---|---|---|---|---|
| 1 | ឥ | ĕ | — | EVIDENCE_LIMITED |
| 2 | ឦ | ei | ей | PROPOSED |
| 3 | ឧ | ŏ / ŭ | о / у | ANALYSIS_DEPENDENT |
| 4 | ឨ | âu | ау | PROPOSED |
| 5 | ឩ | rœ̆ | — | EVIDENCE_LIMITED |
| 6 | ឬ | rœ | — | EVIDENCE_LIMITED |
| 7 | ឭ | lœ̆ | — | EVIDENCE_LIMITED |
| 8 | ឮ | lœ | — | EVIDENCE_LIMITED |
| 9 | ឯ | ê | е | PROPOSED |
| 10 | ឰ | ai | ай | PROPOSED |
| 11 | ឱ / ឲ | aô | ао | PROPOSED |
| 12 | ឳ | au | ау | PROPOSED |
| 13 | ឪ | âu | ау | PROPOSED |

**Dependent vowel characters**

| PCGN row | Khmer sign / structure | BGN/PCGN romanization (â-series / ô-series; normal / shortened as applicable) | Ukrainian candidate | Status |
|---|---|---|---|---|
| 1 | inherent vowel | â / ô; shortened á / ó | а / о | PROPOSED |
| 2 | ◌ា | a / éa; shortened ă / eă or oă | а / еа | ANALYSIS_DEPENDENT |
| 3 | ◌ិ | ĕ; shortened ĭ | е | ANALYSIS_DEPENDENT |
| 4 | ◌ី | ei; shortened i | ей / і | ANALYSIS_DEPENDENT |
| 5 | ◌ឹ | œ̆ | — | EVIDENCE_LIMITED |
| 6 | ◌ឺ | œ | — | EVIDENCE_LIMITED |
| 7 | ◌ុ | ŏ / ŭ | о / у | ANALYSIS_DEPENDENT |
| 8 | ◌ូ | o / u | о / у | ANALYSIS_DEPENDENT |
| 9 | ◌ួ | uŏ | уо | PROPOSED |
| 10 | ◌ើ | aeu / eu | — | EVIDENCE_LIMITED |
| 11 | ◌ឿ | œă | — | EVIDENCE_LIMITED |
| 12 | ◌ៀ | iĕ | іє | PROPOSED |
| 13 | ◌េ | é | е | PROPOSED |
| 14 | ◌ែ | ê | е | PROPOSED |
| 15 | ◌ៃ | ai / ey | ай / ей | ANALYSIS_DEPENDENT |
| 16 | ◌ោ | aô / oŭ | ао / оу | ANALYSIS_DEPENDENT |
| 17 | ◌ៅ | au / ŏu | ау / оу | ANALYSIS_DEPENDENT |

**Vowel + anusvara / visarga combinations**

| PCGN row | Source pattern | BGN/PCGN romanization (â-series / ô-series) | Ukrainian candidate | Status |
|---|---|---|---|---|
| 1 | ◌ុ◌ំ | om / ŭm | ом / ум | ANALYSIS_DEPENDENT |
| 2 | ◌ំ | âm / um | ам / ум | ANALYSIS_DEPENDENT |
| 3 | ◌ំ (shortened pattern) | ăm / ŏâm | — | EVIDENCE_LIMITED |
| 4 | ◌ះ | ăh / eăh | — | EVIDENCE_LIMITED |
| 5 | ◌ុ◌ះ | ŏh / ŭh | — | EVIDENCE_LIMITED |
| 6 | ◌េ◌ះ | éh / éh | — | EVIDENCE_LIMITED |
| 7 | ◌េ◌ះ (series/context variant) | aôh / ŏăh | — | EVIDENCE_LIMITED |
| 8 | ◌ំ◌ង | ăng / eăng | — | EVIDENCE_LIMITED |

These are **research candidates**, not a production vowel adapter. The source standard makes vowel rendering depend on consonant series, subscripts, shortening, codas and diacritics. The canonical data implementation must preserve those fields and test each context; a single-sign replacement is not conformant.

## Required machine-readable table contract

The next implementation slice should add a canonical registry with at least: source_grapheme, orthographic_unit, consonant_series, subscript_role, romanization, romanization_standard, ukrainian_candidate, ukrainian_status, context, source_id, source_locator, evidence_status and test_id.

Every supported Khmer grapheme/orthographic syllable must either have a complete path:
**Khmer unit → BGN/PCGN romanized syllable → Ukrainian practical syllable**, or a visible exception/unsupported status. Do not use khmerToLatin output as an IPA source, and do not generate Ukrainian output by applying the IPA mapper to the Latin string.

## Task ledger

| ID | Status | Acceptance |
|---|---|---|
| KHM-ROM-STD-001 | DONE_VERIFIED (source review) | BGN/PCGN 1972 selected; UNGEGN approval and PCGN table cited |
| KHM-ROM-ENGINE-001 | PARTIAL | Replace/verify the ASCII simplifier against the full BGN/PCGN table, including diacritics and context |
| KHM-ROM-UA-001 | TODO | Implement an independent syllable-level romanization → Ukrainian adapter |
| KHM-ROM-ONSET-001 | DONE_VERIFIED | All 22 PCGN consonant rows plus special ឝ are in data/khmer/romanization_ukrainian.csv; exact row and provenance tests passed in workflow 41229431196 |
| KHM-ROM-MATRIX-001 | PARTIAL | Full vowel/context/diacritic/numeral table in canonical data with provenance; consonant slice alone is not full coverage |
| KHM-ROM-TEST-001 | TODO | Source-backed tests for all table rows, mixed scripts, punctuation, diacritics, malformed units and ambiguity |
| KHM-IPA-001 | PARTIAL | Existing contextual vowel/register/coda IPA model and independent gold remain incomplete |
