# Khmer vowel coverage matrix and gap register

**Audit date:** 2026-10-20  
**Audited revision:** 6cc30bb48bedb83d86534a5fbff92839e26673dd  
**Scope:** evidence and coverage audit, not a claim of complete IPA verification.

## Interpretation and status rules

This is a deliberately conservative matrix of evidenced examples and explicit gaps. It is not an exhaustive Cartesian product of Khmer consonants, vowel signs, codas, and dialects. A row is not a claim that every lexeme with the same visible pattern has exactly the same surface IPA.

- DONE_VERIFIED: the specific structural/data claim is checked against repository evidence; it does not imply complete lexical phonetic validation.
- IN_PROGRESS: data exists, but the relevant context matrix or independent adjudication is incomplete.
- TODO: not yet demonstrated in the current corpus.
- BLOCKED: a reliable source/adjudication is needed before assigning a deterministic result.

## Evidence-bearing representative rows

| ID | Orthography / pattern | Initial / series | Vowel | Coda / context | Current IPA evidence | Ukrainian output | Source / evidence basis | Confidence | Status / test |
|---|---|---|---|---|---|---|---|---|---|
| VOW-001 | ក | ក, first series | inherent | no explicit coda in example | /kɑː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium; specialist description, not independent acoustic recheck | IN_PROGRESS; no dedicated unit test found in current inventory |
| VOW-002 | គ | គ, second series | inherent | no explicit coda in example | /kɔː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS; no dedicated unit test found in current inventory |
| VOW-003 | កី | ក, first series | dependent ី | no coda in example | /kəj/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS; contrast-pair coverage incomplete |
| VOW-004 | គី | គ, second series | dependent ី | no coda in example | /kiː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS; contrast-pair coverage incomplete |
| VOW-005 | កា | ក, first series | dependent ា | no coda in example | /kaː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS |
| VOW-006 | គា | គ, second series | dependent ា | no coda in example | /kiə/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS |
| VOW-007 | ភាសា | lexical; multi-syllable | mixed | lexical phrase context | /pʰiə.saː/ in lexical corpus | PROPOSED | Wiktionary lexical pages in data/tests/verified-lexical-corpus.json | Medium; lexical reference, not a dedicated acoustic source | IN_PROGRESS; lexical corpus fixture exists |
| VOW-008 | ខ្មែរ | lexical; series-conditioned complex vowel | mixed | final lexical environment | /kʰmae/ in lexical corpus | PROPOSED | Wiktionary lexical page cited in data/tests/verified-lexical-corpus.json | Medium | IN_PROGRESS; lexical corpus fixture exists |
| VOW-009 | ស៊ី | TRIISAP/register-sensitive example | second series after shifter | long vowel ៊ី | /siː/ in adversarial fixtures | not adjudicated | Unicode 17 representative example recorded in data/tests/adversarial-cases.json | High for encoded structural example; phonetic status still requires source-layer distinction | IN_PROGRESS; adversarial fixture exists |
| VOW-010 | សង្គ្រាម | coeng cluster and multiple syllabic structure | series-conditioned | complex cluster / final environment | /sɔŋkrɛəm/ in adversarial fixtures | not adjudicated | Unicode 17 representative example recorded in data/tests/adversarial-cases.json | High for fixture provenance; not an independent lexical gold judgment | IN_PROGRESS; adversarial fixture exists |
| VOW-011 | សញ្ញា | repeated ញ / coeng structure | long vowel ា in final syllable | multi-consonant context | /saɲɲaː/ in adversarial fixtures | not adjudicated | Unicode 17 representative example recorded in data/tests/adversarial-cases.json | High for structural test role; IPA needs independent lexical corroboration | IN_PROGRESS; adversarial fixture exists |
| VOW-012 | ខ្ញុំ | subscript cluster + vowel modifier | complex vowel/coda context | final ំ pattern | /kʰɲom/ in lexical and adversarial data | PROPOSED | Wiktionary lexical page and test fixture | Medium | IN_PROGRESS; parser/web fixture exists |

## Coverage dimensions that remain open

| ID | Dimension / gap | Why it matters | Required evidence / acceptance criterion | Priority | Status |
|---|---|---|---|---|---|
| GAP-001 | Full dependent-vowel-sign × consonant-series matrix | A sign cannot be mapped to one fixed vowel value independent of register | Enumerate attested orthographic patterns from authoritative descriptions; each cell includes IPA, source, confidence, and test or explicit unresolved state | P0 | TODO |
| GAP-002 | Independent vowels | They cannot safely inherit rules for dependent signs | Inventory each independent-vowel letter, supported pronunciation/profile, and provenance-bearing fixture | P1 | TODO |
| GAP-003 | Open vs closed syllables / codas | Coda structure can condition vowel quality, length, and syllable analysis | Contrast attested open/closed patterns and record coda-specific evidence; no extrapolation from onset + sign alone | P0 | TODO |
| GAP-004 | NIKAHIT U+17C6 and REAHMUK U+17C7 | These marks interact with the nucleus and/or coda and are not plain vowel letters | Explicit context rows with supported phonological analyses and negative/unsupported examples | P0 | TODO |
| GAP-005 | Vowel length and complex vowels | Current inventory lists categories but does not establish their orthographic distributions | Map attested graphemic patterns to broad IPA with length preserved; document dialect/profile variation | P0 | TODO |
| GAP-006 | Harmony and following-syllable effects | Register assignment may interact with lexical and cross-syllable context | Distinguish productive rules from lexical exceptions; source each claim and add minimal/near-minimal contrasts where available | P1 | TODO |
| GAP-007 | Stress and reduction | A careful citation form cannot be assumed to represent colloquial speech | Keep profile-specific variants separate and cite acoustic/phonetic evidence | P1 | TODO |
| GAP-008 | Final consonants and syllable restrictions | Vowel predictions made before coda analysis may be wrong | Test all attested coda classes relevant to vowel realization; unsupported combinations remain unresolved | P0 | TODO |
| GAP-009 | Ukrainian rendering of vowel contrasts | Current target policy is proposed and may neutralize length/quality | Define explicit practical policy per supported IPA category and record neutralizations as deliberate project decisions | P1 | TODO |
| GAP-010 | Independent adjudication | Wiktionary and Unicode examples are useful but not a substitute for a gold corpus | Add lexical items checked against specialist dictionaries and/or acoustic/phonological primary literature; record adjudication and profile | P0 | TODO |

## Method for completing the matrix

1. Extract the full sign inventory from data/khmer/signs.json and consonant/register inventory from data/khmer/consonants.json.
2. Classify attested orthographic templates using Unicode Standard chapter 16 and the specialist orthography reference. Do not generate arbitrary sign combinations as if they were lexical data.
3. For every template, separate: orthographic analysis; phonological analysis; broad IPA; pronunciation profile; Ukrainian practical form.
4. Mark a cell BLOCKED if no reliable source establishes the relevant pronunciation. Never fill a missing IPA cell from a sign's name or a neighboring example.
5. Add a test ID for every deterministic claim. For unresolved cases, add a test asserting that the implementation does not fabricate IPA.
6. Report coverage as counts of evidenced templates and unresolved templates, not as an accuracy percentage.

## Audit caveat

The current parser decomposes orthographic structure and identifies register-shifter cases, but analyze() explicitly returns phoneticization_not_yet_established. The Python resolve_inherent_vowel() returns only a series label when there is no explicit vowel. The web layer has a small lexical corpus and representative fixtures. These components are valuable foundations but do not amount to a complete deterministic orthography-to-IPA engine.
