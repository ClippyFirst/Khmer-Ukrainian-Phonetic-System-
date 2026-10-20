# Khmer vowel coverage matrix and gap register

**Audit date:** 2026-10-20  
**Audited revision at matrix creation:** 6cc30bb48bedb83d86534a5fbff92839e26673dd  
**Evidence pass:** 2026-10-20; source-indexed examples added from Unicode 17.0 Chapter 16 and Richard Ishida's Khmer orthography notes updated 27-Apr-2026  
**Scope:** evidence and coverage audit, not a claim of complete IPA verification.

## Interpretation and status rules

This is a deliberately conservative matrix of evidenced examples and explicit gaps. It is not an exhaustive Cartesian product of Khmer consonants, vowel signs, codas, and dialects. A row is not a claim that every lexeme with the same visible pattern has exactly the same surface IPA.

- DONE_VERIFIED: the specific structural/data claim is checked against repository evidence; it does not imply complete lexical phonetic validation.
- IN_PROGRESS: data exists, but the relevant context matrix or independent adjudication is incomplete.
- TODO: not yet demonstrated in the current corpus.
- BLOCKED: a reliable source/adjudication is needed before assigning a deterministic result.

## Source-indexed evidence added in this pass

The following source claims are grounded in the two cited references, with an important distinction: Unicode is authoritative for encoding and orthographic structure and includes representative pronunciation examples; it is not an acoustic experiment. R12A is a specialist orthography/phonology synthesis, not a substitute for a lexical gold corpus or primary acoustic measurements.

| Evidence ID | Pattern / example | Source statement or IPA shown by source | What this establishes | What it does not establish | Status |
|---|---|---|---|---|---|
| SRC-001 | ក vs គ | R12A: ក /kɑː/ vs គ /kɔː/ | Two inherent-vowel values associated with the two consonant classes | Complete contextual realization of inherent vowels in all lexical items | IN_PROGRESS |
| SRC-002 | កី vs គី | R12A: /kəj/ vs /kiː/ | Same dependent sign U+17B8 may correspond to different vowel outcomes by class | Full vowel-sign × class matrix or dialect-independent surface IPA | IN_PROGRESS |
| SRC-003 | កា vs គា | R12A: /kaː/ vs /kiə/ | U+17B6 has class-conditioned realizations in the cited examples | Generalization to every coda, stress pattern, or lexical environment | IN_PROGRESS |
| SRC-004 | កូរ vs គូរ | Unicode 17.0 gives /koː/ ‘stir’ vs /kuː/ ‘sketch’ | The same written vowel sign U+17BC has different realizations across class/lexeme | A complete /uː/ mapping rule or broad dialect profile | IN_PROGRESS |
| SRC-005 | លង vs ល្ង | Unicode 17.0 gives លង /lɔːŋ/ vs ល្ង /lŋɔ̀ː/ | Changing a plain coda to a coeng/subscript structure can change syllabification and vowel realization | A general deterministic coda rule for all clusters | IN_PROGRESS |
| SRC-006 | ដំ vs ដម | Unicode 17.0 gives ដំ ‘to pound’ /dɔm/ vs ដម ‘nectar’ /dɔːm/ | U+17C6 NIKAHIT can encode a final /m/ pattern with a vowel outcome differing from a similar written consonant-coda pattern | A full phonological analysis for every NIKAHIT combination; Unicode's lexical illustration is not a substitute for independent lexical/acoustic adjudication | IN_PROGRESS |
| SRC-007 | ពាំ vs ពាម | Unicode 17.0 gives ពាំ ‘carry in the beak’ /pɔ̀əm/ vs ពាម ‘mouth of a river’ /pèəm/ | The AA + NIKAHIT sequence is not simply /aːm/; lexical/coda context matters | A general all-words mapping or evidence that IPA conventions are identical across sources | IN_PROGRESS |
| SRC-015 | Register examples differ by source and lexical context | Unicode 17.0 Table 16-7 illustrates ក ‘neck’ [kɔː] and គ ‘mute’ [kɔ̀ː], while R12A gives the simplified inherent-vowel contrast ក /kɑː/ vs គ /kɔː/ | The sources agree that consonant register affects vowel interpretation, but the illustrative forms and transcriptions are not interchangeable | A universal per-register IPA value derived from a single illustrative example; dialect, lexical, and transcription conventions must be reconciled | BLOCKED for universal mapping; retain source-specific examples |
| SRC-008 | U+17C6 NIKAHIT and U+17C7 REAHMUK | R12A says both can represent a syllable coda and affect the nucleus | These marks must be modelled as context-sensitive syllabic components, not plain vowel letters | Specific IPA for every combination without consulting the detailed mapping and lexical sources | IN_PROGRESS |
| SRC-009 | Independent vowels | R12A lists an incomplete set and says independent vowel letters are not interchangeable with QA + vowel-sign spellings word-for-word | Independent-vowel letters require their own inventory and lexical evidence | Automatic equivalence between independent vowels and visually similar spellings | TODO |
| SRC-010 | Vowel length | R12A describes length as distinctive and illustrates distinct short/long signs; Chem (2020) measures duration and reports differences between short/long categories | Length is a meaningful feature in the descriptive layer | That the practical Ukrainian layer must always preserve length; that decision is target-policy work | IN_PROGRESS |
| SRC-013 | Closed syllables and coda effects | Chem (2020), pp. 109–110, reports that coda/final consonants can affect nucleus quality and length; its study compares open/closed contexts | Coda-conditioned vowels must be modelled and tested; this is direct acoustic-study support for GAP-003/GAP-008 | Specific expected IPA for an individual lexeme without matching its context and phonetic profile | IN_PROGRESS |
| SRC-014 | Short diphthongs in closed syllables | Chem (2020), p. 111, reports short diphthongs commonly in syllables closed by /h, k, ʔ/ in its dataset | These coda classes deserve explicit matrix coverage | A universal rule or a mapping for every vowel sign and coda | IN_PROGRESS |
| SRC-011 | Pre-base and circumgraph signs | R12A documents 3 pre-base glyphs and 5 circumgraphs, with visual order distinct from encoded order | Parser must distinguish logical Unicode sequence from rendered placement and phonological order | That visual placement determines the pronunciation by itself | DONE_VERIFIED for structural principle |
| SRC-012 | Register shifters, including ប៉ | Unicode 17.0 documents U+17C9/U+17CA and the exceptional ប៉ use | Register-shifter interpretation has a documented orthographic basis | That every malformed/multiple-shifter sequence has a supported pronunciation | DONE_VERIFIED for cited orthographic principle |

**Primary source URLs**

- Unicode Consortium, *The Unicode Standard 17.0.0, Chapter 16: South and Southeast Asian Scripts — Khmer*: https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-16/
- Richard Ishida, *Khmer (Cambodian) Orthography Notes*, updated 27 April 2026: https://r12a.github.io/scripts/khmr/km.html
- Unicode 16.0 Chapter 16 is retained above only where its retrieved text supplied explicit NIKAHIT contrast examples; use Unicode 17.0 as the current normative encoding reference and re-check those specific lexical examples before promoting them to a gold corpus: https://unicode.org/versions/Unicode16.0.0/core-spec/chapter-16/
- Chem, *The Standard Khmer vowel system: An acoustic study* (2020), DOI 10.61945/cjbar.2020.2.2.3: https://www.cjbar.rupp.edu.kh/index.php/cjbar/article/view/36. The paper's Methods (PDF pp. 104–106) reports 21 initial speakers screened and 4 Phnom Penh speakers (2 women, ages 20–50) retained for the acoustic study; 61 lexical items were read three times, with formant and duration measurements. Its discussion explicitly states that coda/final consonants can affect vowel quality and length (PDF pp. 109–110). This supports a contextual research dimension, not a universal grapheme-to-IPA lookup.

## Evidence-bearing representative rows

| ID | Orthography / pattern | Initial / series | Vowel | Coda / context | Current IPA evidence | Ukrainian output | Source / evidence basis | Confidence | Status / test |
|---|---|---|---|---|---|---|---|---|---|
| VOW-001 | ក | ក, first series | inherent | no explicit coda in example | /kɑː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium; specialist description, not independent acoustic recheck | IN_PROGRESS; test coverage not independently audited in this pass |
| VOW-002 | គ | គ, second series | inherent | no explicit coda in example | /kɔː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS |
| VOW-003 | កី | ក, first series | dependent ី | no coda in example | /kəj/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS; contrast-pair coverage incomplete |
| VOW-004 | គី | គ, second series | dependent ី | no coda in example | /kiː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS; contrast-pair coverage incomplete |
| VOW-005 | កា | ក, first series | dependent ា | no coda in example | /kaː/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS |
| VOW-006 | គា | គ, second series | dependent ា | no coda in example | /kiə/ in current vowel model | not adjudicated | R12A orthography notes, data/khmer/vowels.json | Medium | IN_PROGRESS |
| VOW-007 | ភាសា | lexical; multi-syllable | mixed | lexical phrase context | /pʰiə.saː/ in lexical corpus | PROPOSED | Wiktionary lexical pages in data/tests/verified-lexical-corpus.json | Medium; lexical reference, not a dedicated acoustic source | IN_PROGRESS; lexical corpus fixture exists |
| VOW-008 | ខ្មែរ | lexical; series-conditioned complex vowel | mixed | final lexical environment | /kʰmae/ in lexical corpus | PROPOSED | Wiktionary lexical page cited in data/tests/verified-lexical-corpus.json | Medium | IN_PROGRESS; lexical corpus fixture exists |
| VOW-009 | ស៊ី | TRIISAP/register-sensitive example | second series after shifter | long vowel ៊ី | /siː/ in adversarial fixtures | not adjudicated | Unicode 17.0 representative example recorded in data/tests/adversarial-cases.json | High for orthographic example; not an acoustic validation | IN_PROGRESS; adversarial fixture exists |
| VOW-010 | សង្គ្រាម | coeng cluster and multiple syllabic structure | series-conditioned | complex cluster / final environment | Unicode 17.0 gives /sɔŋkrèəm/; fixture uses /sɔŋkrɛəm/ | not adjudicated | Unicode 17.0 representative example and data/tests/adversarial-cases.json | High for source example; transcription notation differs between source and fixture | IN_PROGRESS; reconcile IPA conventions before gold use |
| VOW-011 | សញ្ញា | repeated ញ / coeng structure | long vowel ា in final syllable | multi-consonant context | /saɲɲaː/ in adversarial fixtures | not adjudicated | Unicode 17.0 representative example recorded in data/tests/adversarial-cases.json | High for structural test role; not an independent lexical gold judgment | IN_PROGRESS |
| VOW-012 | ខ្ញុំ | subscript cluster + vowel modifier | complex vowel/coda context | final ំ pattern | /kʰɲom/ in lexical and adversarial data | PROPOSED | Unicode 17.0 representative example and Wiktionary lexical page | Medium | IN_PROGRESS; parser/web fixture exists |
| VOW-013 | លង vs ល្ង | plain coda vs subscript cluster | inherent / class-conditioned | final /ŋ/ vs initial cluster + nucleus | Unicode 17.0: /lɔːŋ/ vs /lŋɔ̀ː/ | not adjudicated | Unicode 17.0 Chapter 16 | High for cited illustrative contrast; phonetic profile not independently adjudicated | IN_PROGRESS; add paired parser/phonology tests |
| VOW-014 | ដំ vs ដម | NIKAHIT vs consonant coda | composite / inherent | /m/ final | Unicode 17.0: /dɔm/ vs /dɔːm/ | not adjudicated | Unicode 17.0 Chapter 16, §16.4 | Medium; normative script reference's lexical example, not an acoustic gold judgment | IN_PROGRESS; source example verified, runtime mapping remains unadjudicated |
| VOW-015 | ពាំ vs ពាម | AA + NIKAHIT vs AA + consonant coda | composite / class-conditioned | /m/ final | Unicode 17.0: /pɔ̀əm/ vs /pèəm/ | not adjudicated | Unicode 17.0 Chapter 16, §16.4 | Medium; normative script reference's lexical example, not an acoustic gold judgment | IN_PROGRESS; source example verified, runtime mapping remains unadjudicated |

## Coverage dimensions that remain open

| ID | Dimension / gap | Why it matters | Required evidence / acceptance criterion | Priority | Status |
|---|---|---|---|---|---|
| GAP-001 | Full dependent-vowel-sign × consonant-series matrix | A sign cannot be mapped to one fixed vowel value independent of register | Enumerate attested orthographic patterns from authoritative descriptions; each cell includes IPA, source, confidence, and test or explicit unresolved state | P0 | IN_PROGRESS; source-indexed representative evidence started, not exhaustive |
| GAP-002 | Independent vowels | They cannot safely inherit rules for dependent signs | Inventory each independent-vowel letter, supported pronunciation/profile, and provenance-bearing fixture | P1 | TODO |
| GAP-003 | Open vs closed syllables / codas | Coda structure can condition vowel quality, length, and syllable analysis | Contrast attested open/closed patterns and record coda-specific evidence; no extrapolation from onset + sign alone | P0 | IN_PROGRESS; Unicode/R12A examples plus Chem (2020) acoustic support for coda effects; lexical mapping remains incomplete |
| GAP-004 | NIKAHIT U+17C6 and REAHMUK U+17C7 | These marks interact with the nucleus and/or coda and are not plain vowel letters | Explicit context rows with supported phonological analyses and negative/unsupported examples | P0 | IN_PROGRESS; source confirms nucleus+coda interaction; tests/test_coda_marks.py guards the conservative API boundary, but the full context table and deterministic mappings are not built |
| GAP-005 | Vowel length and complex vowels | Current inventory lists categories but does not establish their orthographic distributions | Map attested graphemic patterns to broad IPA with length preserved; document dialect/profile variation | P0 | IN_PROGRESS; R12A inventory and Chem (2020) duration/formant study reviewed at abstract/method/results level; full graphemic distribution still incomplete |
| GAP-006 | Harmony and following-syllable effects | Register assignment may interact with lexical and cross-syllable context | Distinguish productive rules from lexical exceptions; source each claim and add minimal/near-minimal contrasts where available | P1 | TODO |
| GAP-007 | Stress and reduction | A careful citation form cannot be assumed to represent colloquial speech | Keep profile-specific variants separate and cite acoustic/phonetic evidence | P1 | TODO |
| GAP-008 | Final consonants and syllable restrictions | Vowel predictions made before coda analysis may be wrong | Test all attested coda classes relevant to vowel realization; unsupported combinations remain unresolved | P0 | IN_PROGRESS; first coda-conditioned contrasts recorded |
| GAP-009 | Ukrainian rendering of vowel contrasts | Current target policy is proposed and may neutralize length/quality | Define explicit practical policy per supported IPA category and record neutralizations as deliberate project decisions | P1 | TODO |
| GAP-010 | Independent adjudication | Wiktionary and Unicode examples are useful but not a substitute for a gold corpus | Add lexical items checked against specialist dictionaries and/or acoustic/phonological primary literature; record adjudication and profile | P0 | TODO |

## Method for completing the matrix

1. Extract the full sign inventory from data/khmer/signs.json and consonant/register inventory from data/khmer/consonants.json.
2. Classify attested orthographic templates using Unicode Standard chapter 16 and the specialist orthography reference. Do not generate arbitrary sign combinations as if they were lexical data.
3. For every template, separate: orthographic analysis; phonological analysis; broad IPA; pronunciation profile; Ukrainian practical form.
4. Mark a cell BLOCKED if no reliable source establishes the relevant pronunciation. Never fill a missing IPA cell from a sign's name or a neighboring example.
5. Add a test ID for every deterministic claim. For unresolved cases, add a test asserting that the implementation does not fabricate IPA. Initial conservative tests for U+17C6 and U+17C7 are in tests/test_coda_marks.py (commit 262cffd76064cbb91c4fbeb83a04d38699e8353a); these tests intentionally do not assign pronunciation values.
6. Report coverage as counts of evidenced templates and unresolved templates, not as an accuracy percentage.
7. Reconcile IPA notation and dialect/profile conventions across Unicode, R12A, lexical dictionaries and acoustic studies before merging source examples into a gold corpus. In particular, don't silently mix Unicode's illustrative transcriptions with a project's broad IPA convention.
8. Treat Chem (2020) as useful but limited acoustic evidence: four selected Phnom Penh speakers and 61 lexical items cannot establish all dialects, all lexical items, or a full orthography-to-IPA mapping. Use its coda and duration findings to prioritize targeted contrasts, not to fill unsupported cells.
9. Keep the Unicode 17.0 NIKAHIT examples as source-indexed lexical illustrations, but do not automatically promote them to the independent gold corpus. The explicit Unicode 16-only source-version blocker is no longer applicable to these two examples; the remaining blocker is independent phonetic/lexical adjudication.

## Audit caveat

The current parser decomposes orthographic structure and identifies register-shifter cases, but analyze() explicitly returns phoneticization_not_yet_established. The Python resolve_inherent_vowel() returns only a series label when there is no explicit vowel. The web layer has a small lexical corpus and representative fixtures. These components are valuable foundations but do not amount to a complete deterministic orthography-to-IPA engine.
