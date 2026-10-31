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

| Khmer source unit (base / subscript) | BGN/PCGN romanization | Ukrainian candidate | Status / note |
|---|---|---|---|
| ក / ្ក | k | к | PROPOSED orthographic target |
| ខ / ្ខ | kh | к' | PROPOSED; preserve aspirated series marker |
| ង / ្ង | ng | нг | PROPOSED |
| ច / ្ច | ch | ч | PROPOSED |
| ឆ / ្ឆ | chh | ч' | PROPOSED; aspiration distinction retained |
| ញ / ្ញ | nh | нь | PROPOSED |
| ដ / ្ដ | d | д | PROPOSED |
| ថ / ្ថ | th | т' | PROPOSED; context and consonant series must be retained |
| ទ / ្ទ | th | т' | PROPOSED; BGN/PCGN table has context-specific historical spellings |
| ណ / ្ណ; ន / ្ន | n | н | PROPOSED |
| ត / ្ត | t | т | PROPOSED |
| ប / ្ប | b, p (contextual) | б / п | ANALYSIS_DEPENDENT; BGN/PCGN note 3 governs |
| ត (ô-series foot) / ្ត | p | п | PROPOSED; do not merge with t |
| ផ / ្ផ; ភ / ្ភ | ph | п' | PROPOSED; preserve aspirated distinction |
| ម / ្ម | m | м | PROPOSED |
| យ / ្យ | y | й | PROPOSED |
| រ / ្រ | r | р | PROPOSED; pronunciation-profile effects remain separate |
| ល / ្ល | l | л | PROPOSED |
| វ / ្វ | v | в | PROPOSED |
| ស / ្ស | s | с | PROPOSED |
| ហ / ្ហ | h | г | PROPOSED under the project's Ukrainian target policy; not IPA evidence |
| អ / ្អ | ’ | ’ / explicit onset marker | ANALYSIS_DEPENDENT; retain rather than silently delete |

## Vowel matrix: contextual source table, not a one-sign substitution table

The BGN/PCGN vowel tables explicitly distinguish independent and dependent signs, â-series and ô-series, normal and shortened nuclei, and shortened forms with anusvara/visarga. The full source table must be transcribed into canonical data without flattening the consonant-series context.

| Khmer source vowel structure | BGN/PCGN romanized value | Ukrainian candidate | Status |
|---|---|---|---|
| dependent ា after â-series | â | а | PROPOSED |
| dependent ា after ô-series | ô | о | PROPOSED |
| េ / ែ | œ (table-specific context) | е / є | ANALYSIS_DEPENDENT |
| ិ after â-/ô-series | a / éa | а / еа | ANALYSIS_DEPENDENT |
| ឹ / ឺ | ě / ī | е / і | PROPOSED; length/context review required |
| ូ | o / u | о / у | ANALYSIS_DEPENDENT |
| ួ | uŏ | уо | PROPOSED |
| ៅ | aeu / eu | аеу / еу | ANALYSIS_DEPENDENT |
| ើ | œă / iĕ / é (table row/context) | не встановлено | EVIDENCE_LIMITED until exact sign identity and context are resolved |
| ឯ / ឰ / ឱ / ឪ and related independent forms | ê / ai / aô / au | е / ай / ао / ау | PROPOSED; verify source row and lexical scope |
| NIKAHIT / REAHMUK combinations | BGN/PCGN contextual forms | no global default | EVIDENCE_LIMITED; coda/nucleus context required |

The above is an initial research crosswalk, **not a production mapping table**. Rows with multiple values are not resolved by guessing. The canonical data implementation must preserve the exact Khmer code-point sequence, consonant series, subscript order, vowel category, shortening, coda, diacritics and source locator.

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
| KHM-ROM-MATRIX-001 | PARTIAL | Full consonant/subscript/vowel/diacritic/numeral table in canonical data with provenance |
| KHM-ROM-TEST-001 | TODO | Source-backed tests for all table rows, mixed scripts, punctuation, diacritics, malformed units and ambiguity |
| KHM-IPA-001 | PARTIAL | Existing contextual vowel/register/coda IPA model and independent gold remain incomplete |
