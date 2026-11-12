# Khmer romanization → Ukrainian orthographic matrix

**Status:** PARTIAL — the Ukrainian target crosswalk is populated and a provisional runtime adapter is integrated. The upstream Latin-output package remains BGN/PCGN-derived ASCII rather than fully conformant; contextual vowel distinctions lost by that package cannot be reconstructed.
**Primary variety:** contemporary Standard Khmer, Phnom Penh-oriented only where supported.

## Standard selection

Select **BGN/PCGN 1972 Romanization of Khmer (Cambodian)** as the reference romanization profile. It is the strongest defensible choice for a source-backed research table: the UNGEGN Working Group report states that the UN-recommended system was approved in 1972 (Resolution II/10) and is based on the BGN/PCGN 1972 system. The official PCGN guide was checked for validity in October 2017 and contains consonant, subscript, vowel, diacritic and numeral tables.

**National-system scope caveat (verified 2026-11-12):** BGN/PCGN 1972 remains the selected, fully source-located *research crosswalk profile* in this matrix; it must not be described as the current national Cambodian romanization. Cambodia's national report to UNGEGN states that the country's romanized writing system is based on the **1997 transcription system instead of the 1972 transliteration system**, and that the 2019 gazetteer used the 1997 system. The UNGEGN Working Group's 2023 status report independently repeats that the 1997 system replaced the 1972 system in Cambodia. The complete primary 1997 specification has not yet been located and verified, so the existing BGN/PCGN table must not be silently relabelled as that system. The Library of Congress **ALA-LC Khmer Romanization Table (1997 version)** is a separate cataloguing profile and is not evidence that it equals Cambodia's national 1997 system.

Sources:
- Government of Cambodia, *Report on the activities of the standardization of geographical names for the period 2019–2022*, GEGN.2/2023/104/CRP.104, pp. 1–2: https://digitallibrary.un.org/record/4017595/files/GEGN.2_2023_104_CRP.104-EN.pdf
- UNGEGN Working Group on Romanization Systems, *Current status of United Nations romanization systems for geographical names*, GEGN.2/2023/11/CRP.11, p. 2: https://digitallibrary.un.org/record/4018337/files/GEGN.2_2023_11_CRP.11-EN.pdf
- Library of Congress, *Khmer Romanization Table, 1997 version* (ALA-LC): https://www.loc.gov/catdir/cpso/romanization/khmer-1997.pdf


Primary sources:
- UNGEGN, Report on the Current Status of United Nations Romanization Systems for Geographical Names (2013), Khmer section: https://unstats.un.org/unsd/ungegn/working_groups/wg5/documents/wgrr4khmer.pdf
- UK PCGN, Romanization of Khmer (Cambodian), BGN/PCGN 1972 Agreement (checked October 2017): https://assets.publishing.service.gov.uk/media/5ab4e25aed915d78bc23451e/ROMANIZATION_OF_KHMER.pdf

UNGEGN notes that Khmer is an alphasyllabic script, that the romanization requires contextual rules, that word division is not ordinarily indicated, and that the system is generally not reversible. Thus “transliterate everything” means **cover every supported orthographic unit with an explicit table row or an explicit exception state**; it does not mean that the Latin output alone can reconstruct all Khmer code points.

## Existing implementation audit

The current @gmana/km-translit 0.1.2 integration is documented as **BGN/PCGN-derived ASCII**, drops diacritics and is not a fully conformant BGN/PCGN implementation. It is useful as an existing romanization candidate but cannot be called the selected standard implementation or the final complete orthographic mode. It must remain separately labelled until replaced or proven equivalent against the official table.

The current romanization card remains independent from IPA → Ukrainian conversion. Its Ukrainian target mapping is now executed by a separate runtime adapter for the current BGN/PCGN-derived ASCII output. Matrix completeness and runtime integration do not establish full BGN/PCGN conformance, reversibility, or pronunciation evidence.

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
| 8 | ឋ / ឍ; corresponding feet | th | т' | PROPOSED |
| 9 | ថ / ធ; corresponding feet | th | т' | PROPOSED |
| 10 | ណ / ន; corresponding feet | n | н | PROPOSED |
| 11 | ត / ទ; corresponding feet | t | т | PROPOSED |
| 12 | ប; corresponding foot | b, p (contextual) | б / п | PROPOSED; map the actual selected Latin output |
| 13 | ព; corresponding foot | p | п | PROPOSED |
| 14 | ផ / ភ; corresponding feet | ph | п' | PROPOSED |
| 15 | ម; corresponding foot | m | м | PROPOSED |
| 16 | យ (no foot) | y | й | PROPOSED |
| 17 | រ; corresponding foot | r | р | PROPOSED |
| 18 | ឡ / ល; foot for ល only | l | л | PROPOSED |
| 19 | វ; corresponding foot | v | в | PROPOSED |
| 20 | ស; corresponding foot | s | с | PROPOSED |
| 21 | ហ; corresponding foot | h | г | PROPOSED |
| 22 | អ; corresponding foot | ’ | ʼ | PROPOSED; retain the glottal-onset marker |

The machine-readable matrix [data/khmer/romanization_ukrainian.csv](../data/khmer/romanization_ukrainian.csv) preserves the exact source sequences, the 22 PCGN table row IDs, the Ukrainian candidate/status, the official URL and row-level locator. The target column now explicitly maps the actual romanized outputs: th → т', contextual b / p → б / п, and the glottal marker ’ → ʼ. These are project orthographic conventions, not IPA claims. PCGN explicitly states that there is no subscript form for ឡ; the row-18 record captures this.


## Vowel matrix: contextual source table, not a one-sign substitution table

The official PCGN guide has separate tables for independent vowels, dependent vowel signs (with â-/ô-series and normal/shortened columns), and vowels with anusvara or visarga. The source inventory reproduces the romanization values and now supplies an explicit project Ukrainian rendering for all 37 rows. Alternative source forms remain alternative target forms; this does not resolve which source variant applies in a particular syllable.

**Independent vowel characters**

PCGN numbers the independent-character column within a shared 22-row table; only the following rows contain independent characters. Blank rows in that column are not additional vowel characters.

| PCGN row | Khmer | BGN/PCGN romanization | Ukrainian candidate | Status |
|---|---|---|---|---|
| 3 | ឥ | ĕ | — | EVIDENCE_LIMITED |
| 4 | ឦ | ei | ей | PROPOSED |
| 7 | ឧ | ŏ / ŭ | о / у | ANALYSIS_DEPENDENT |
| 14 | ឯ | ê | е | PROPOSED |
| 15 | ឰ | ai | ай | PROPOSED |
| 16 | ឱ / ឲ | aô | ао | PROPOSED |
| 17 | ឳ | au | ау | PROPOSED |
| 18 | ឪ | âu | ау | PROPOSED |
| 19 | ឫ | rœ̆ | — | EVIDENCE_LIMITED |
| 20 | ឬ | rœ | — | EVIDENCE_LIMITED |
| 21 | ឭ | lœ̆ | — | EVIDENCE_LIMITED |
| 22 | ឮ | lœ | — | EVIDENCE_LIMITED |

**Dependent vowel characters**

| PCGN row | Khmer sign / structure | BGN/PCGN romanization (â-series / ô-series; normal / shortened as applicable) | Ukrainian candidate | Status |
|---|---|---|---|---|
| 1 | ◌ (any consonant or consonant + foot) | â / ô; shortened á / ó | а / о | ANALYSIS_DEPENDENT |
| 2 | ◌ា | a / éa; shortened ă / eă or oă | а / еа | ANALYSIS_DEPENDENT |
| 3 | ◌ិ | ĕ; shortened ĭ | е | ANALYSIS_DEPENDENT |
| 4 | ◌ី | ei; shortened i | ей / і | ANALYSIS_DEPENDENT |
| 5 | ◌ឹ | œ̆ | — | EVIDENCE_LIMITED |
| 6 | ◌ឺ | œ | — | EVIDENCE_LIMITED |
| 7 | ◌ុ | ŏ / ŭ | о / у | ANALYSIS_DEPENDENT |
| 8 | ◌ូ | o / u | о / у | ANALYSIS_DEPENDENT |
| 9 | ◌ួ | uŏ | уо | PROPOSED |
| 10 | េ◌ើ | aeu / eu | — | EVIDENCE_LIMITED |
| 11 | េ◌ឿ | œă | — | EVIDENCE_LIMITED |
| 12 | េ◌ៀ | iĕ | іє | PROPOSED |
| 13 | េ◌ | é | е | PROPOSED |
| 14 | ែ◌ | ê | е | PROPOSED |
| 15 | ៃ◌ | ai / ey | ай / ей | ANALYSIS_DEPENDENT |
| 16 | េ◌ា | aô / oŭ | ао / оу | ANALYSIS_DEPENDENT |
| 17 | េ◌ៅ | au / ŏu | ау / оу | ANALYSIS_DEPENDENT |

**Vowel + anusvara / visarga combinations**

| PCGN row | Source pattern | BGN/PCGN romanization (â-series / ô-series) | Ukrainian candidate | Status |
|---|---|---|---|---|
| 1 | ◌ុ◌ំ | om / ŭm | ом / ум | ANALYSIS_DEPENDENT |
| 2 | ◌ំ | âm / um | ам / ум | ANALYSIS_DEPENDENT |
| 3 | ◌ំ឵ (PCGN composite glyph) | ăm / ŏâm | — | EVIDENCE_LIMITED |
| 4 | ◌ះ | ăh / eăh | — | EVIDENCE_LIMITED |
| 5 | ◌ុ◌ះ | ŏh / ŭh | — | EVIDENCE_LIMITED |
| 6 | េ◌◌ះ | éh / éh | — | EVIDENCE_LIMITED |
| 7 | េ◌឵ះ | aôh / ŏăh | — | EVIDENCE_LIMITED |
| 8 | ◌ំ឵ង | ăng / eăng | — | EVIDENCE_LIMITED |

These are **research candidates**, not a production vowel adapter. The source standard makes vowel rendering depend on consonant series, subscripts, shortening, codas and diacritics. The canonical data implementation must preserve those fields and test each context; a single-sign replacement is not conformant.

## Diacritics and numerals

[data/khmer/romanization_marks_numerals.csv](../data/khmer/romanization_marks_numerals.csv) records all six PCGN diacritical-mark rows and all ten Khmer numeral rows. The marks are not treated as independent letters: PCGN notes specify series changes, shortened-vowel behavior, consonant insertion, positional behavior, and a silent mark that is omitted from romanization. The numeral rows map Khmer digits to their Arabic-digit values. The runtime romanizer must apply these rules contextually rather than concatenate character substitutions.

## Required machine-readable table contract

The next implementation slice should add a canonical registry with at least: source_grapheme, orthographic_unit, consonant_series, subscript_role, romanization, romanization_standard, ukrainian_candidate, ukrainian_status, context, source_id, source_locator, evidence_status and test_id.

Every supported Khmer grapheme/orthographic syllable must either have a complete path:
**Khmer unit → BGN/PCGN romanized syllable → Ukrainian practical syllable**, or a visible exception/unsupported status. Do not use khmerToLatin output as an IPA source, and do not generate Ukrainian output by applying the IPA mapper to the Latin string.

## Task ledger

| ID | Status | Acceptance |
|---|---|---|
| KHM-ROM-STD-001 | DONE_VERIFIED (source review) | BGN/PCGN 1972 selected; UNGEGN approval and PCGN table cited |
| KHM-ROM-ENGINE-001 | PARTIAL | Replace/verify the ASCII simplifier against the full BGN/PCGN table, including diacritics and context |
| KHM-ROM-UA-TARGET-001 | DONE_VERIFIED | All 22 consonant rows and 37 PCGN vowel/rime rows have non-empty Ukrainian project candidates; exact table/provenance and coverage assertions passed on the feature head and merged mainline. This is a project orthographic proposal, not expert-approved standardization. |
| KHM-ROM-UA-001 | PARTIAL | Separate runtime adapter is integrated and tested; current upstream ASCII romanizer drops BGN/PCGN diacritics, so lost contextual vowel distinctions cannot be recovered. Full acceptance requires a diacritic-preserving/context-aware BGN/PCGN source path. |
| KHM-ROM-ONSET-001 | DONE_VERIFIED | All 22 PCGN consonant rows plus special ឝ are in data/khmer/romanization_ukrainian.csv; exact row and provenance tests passed in workflow 41229431196 |
| KHM-ROM-VOWEL-INVENTORY-001 | PARTIAL | 37 source rows now match the PCGN glyphs/romanization values; exact-head workflow 41233203184 passed; all 37 source-glyph/romanization assertions are verified |
| KHM-ROM-MARKS-NUMERALS-001 | PARTIAL | Six exact PCGN diacritic glyphs and ten numeral glyphs are inventoried; exact-glyph tests passed in workflow 41233203184 |
| KHM-ROM-MATRIX-001 | PARTIAL | The target column is complete for the inventoried rows; PCGN consonant-series × vowel × shortening × coda resolution and contextual romanization generation remain incomplete |
| KHM-ROM-TEST-001 | PARTIAL | Exact source-glyph and romanization assertions passed in workflow 41233203184; full mixed-script, punctuation, malformed-unit and ambiguity coverage remains TODO |
| KHM-IPA-001 | PARTIAL | Existing contextual vowel/register/coda IPA model and independent gold remain incomplete |


## Machine-readable vowel inventory

[data/khmer/romanization_vowels_ukrainian.csv](../data/khmer/romanization_vowels_ukrainian.csv) contains **37 source-located PCGN table entries**: 12 independent-character entries, 17 dependent-vowel entries, and 8 vowel-plus-anusvara/visarga entries. The shared PCGN table has 22 row numbers, with a sparse independent-character column; the independent and dependent columns are recorded separately without inventing extra row numbers. Every row now has a Ukrainian candidate. `PROPOSED` marks a single project rendering; `ANALYSIS_DEPENDENT` preserves PCGN alternatives that require source-context resolution. The table remains an inventory of PCGN row forms, not a complete contextual syllable engine.


## Whole-text regression and remaining adapter gap — 2026-10-31

The current main head `1a6921fc75dd011bc8097f6636b8077fc7c59cff` passed Quality [41243972009](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41243972009) and Pages deployment [41243971788](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41243971788). The romanization integration passes the complete source string to the selected library and has regression cases for a full greeting, short mixed-script text, native Khmer numerals, ASCII digits, Latin text, spaces and punctuation. This is input-integrity evidence only. The independent syllable-level romanization → Ukrainian adapter remains TODO; contextual PCGN coverage and unspaced word segmentation remain incomplete. No IPA or Ukrainian gold is inferred from library output.


## Post-merge whole-text verification — 2026-10-31

Current main `28a9bbb909ca57735ceca92f262c2de9eeb43396` passed Quality [41246343908](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41246343908) and Pages [41246343845](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41246343845). The tests confirm the selected romanization library receives the complete input and preserves supported mixed-text boundaries; they do not establish PCGN 1972 conformance or an implemented Ukrainian syllable adapter. The adapter remains TODO.

## Ukrainian target convention for Latin BGN/PCGN input — 2026-11-12

The target column is a **project orthographic adaptation of the Latin romanization string**, not a second pronunciation analysis. It does not use the IPA adapter and must not be described as phonetic Ukrainian transcription. The original BGN/PCGN string remains the source-of-truth display and should be retained alongside the Ukrainian candidate.

- Consonant units: `k → к`, `kh → к'`, `ng → нг`, `ch → ч`, `chh → ч'`, `nh → нь`, `th → т'`, `b → б`, `p → п`, `ph → п'`, `h → г`, `y → й`, `r → р`, `l → л`, `v → в`, `s → с`, `’ → ʼ`.
- Vowels: Latin vowel bases are rendered with the closest stable Ukrainian letter sequence in the matrix (`a → а`, `e/ê/é/ĕ → е`, `i/ĭ → і`, `o/ŏ → о`, `u/ŭ → у`, `œ/œ̆ → и`); diphthong and coda combinations are rendered as explicit sequences in the 37-row CSV.
- PCGN alternatives remain separated by `/` or explanatory context in the candidate field. `ANALYSIS_DEPENDENT` means the source syllable still determines which listed form applies; it does not mean the target cell is blank.
- Diacritical series shifters and shortening marks are contextual source instructions, not independent Latin output letters. They are not emitted as standalone Ukrainian letters. PCGN's silent mark remains omitted. Numerals remain numeric.
- This convention is intentionally **non-reversible** and does not establish Khmer phoneme values. It maps the selected Latin spelling into a stable Ukrainian rendering only.

## Updated acceptance boundary

`KHM-ROM-UA-TARGET-001` is complete as a table-coverage task. `KHM-ROM-UA-001` remains open until an independent runtime adapter consumes BGN/PCGN Latin output, preserves source text and uncertainty, and passes whole-message tests. `KHM-ROM-ENGINE-001` remains partial because the current package is not fully conformant with BGN/PCGN 1972. No pronunciation or lexical accuracy claim follows from these matrix changes.


## Runtime adapter — 2026-11-12

The romanization panel now sends the existing `@gmana/km-translit` Latin output through `src/khmer-romanization-ukrainian.js`. The adapter preserves non-Khmer runs and punctuation, uses longest-match Latin units, and leaves unknown Latin fragments visible as `⟦…⟧`. It does not call the IPA adapter.

**Acceptance status: PARTIAL, not DONE_VERIFIED as a full BGN/PCGN implementation.** The npm package documents that its BGN/PCGN-derived ASCII profile drops the standard's diacritics; its output is explicitly non-conformant. Once those marks and contextual distinctions have been discarded, the Ukrainian adapter cannot reconstruct the exact PCGN vowel choice. Therefore its output is labelled `PROVISIONAL`, not a validated full-standard conversion. The 37-row matrix remains the reference for context-rich PCGN forms; no phonetic interpretation is implied.

- Runtime module: `src/khmer-romanization-ukrainian.js`
- Runtime tests: `tests/romanization-ukrainian.test.mjs` and the browser test in `tests/browser/site.spec.js`.
- Exact PR-head Quality [43226337969](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337969), browser smoke [43226337956](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337956), and push Quality [43226325685](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226325685) passed on `1fa869c524bac5effc98411b71e47e458ad584ae`.

`KHM-ROM-UA-001` is now PARTIAL: the current ASCII output has a usable Ukrainian display adapter, but full acceptance requires a diacritic-preserving BGN/PCGN source romanizer or a separate contextual syllable adapter consuming the full PCGN representation. `KHM-ROM-ENGINE-001` remains PARTIAL. See the package's own scope statement: https://www.npmjs.com/package/%40gmana/km-translit.



Exact PR-head Quality [43226337969](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337969), browser smoke [43226337956](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337956), and push Quality [43226325685](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226325685) passed on code head `1fa869c524bac5effc98411b71e47e458ad584ae`. Quality reports 194 Python tests + 62 subtests; browser Chromium smoke passed.


## Khmer romanization runtime — mainline post-merge verification — 2026-11-12

- PR [#164](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/164) merged as `0ba6107a7e5cb09cca44021669a7401fc125eac4`.
- Mainline Quality [43227360792](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360792), browser smoke [43227360789](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360789), and Pages deployment [43227360801](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360801) all SUCCESS.
- The merged implementation remains deliberately PARTIAL/PROVISIONAL: the upstream ASCII romanizer omits PCGN diacritics; this adapter cannot reconstruct lost contextual vowel distinctions. The IPA route remains separate.


## Mainline ledger reconciliation — 2026-11-12

- Verified current `main`: `a86a59cf082d547563b45374ced9dfb45c5cd8db`.
- `KHM-ROM-UA-TARGET-001`: DONE_VERIFIED — 22 consonant rows and 37 vowel/rime rows have non-empty Ukrainian project candidates; matrix tests passed and changes are merged (PR #161; synchronization PR #163).
- `KHM-ROM-UA-001`: PARTIAL — PR #164 integrates `src/khmer-romanization-ukrainian.js` into the separate romanization panel. Foreign text and punctuation are preserved, unknown Latin fragments remain visible, and no IPA fallback is used. The UI labels output PROVISIONAL.
- Exact mainline verification on current head: Quality [43228414756](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414756), browser smoke [43228414938](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414938), and Pages deployment [43228414646](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414646) all SUCCESS.
- `KHM-ROM-ENGINE-001`: PARTIAL — the selected package emits BGN/PCGN-derived ASCII and drops diacritics. Acceptance requires a validated diacritic-preserving, context-aware BGN/PCGN 1972 romanizer and tests for series, vowel, shortening, coda and shifter environments.
- Historical TODO entries above describe earlier checkpoints; this section records current mainline state. Ukrainian candidates remain project orthographic proposals, not IPA or an expert-approved Ukrainian standard.
