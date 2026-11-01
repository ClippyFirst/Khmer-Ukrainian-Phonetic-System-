# Khmer vowel × consonant-series × coda evidence matrix — 2026-11-01

**Profiles:** modern Standard Khmer is not treated as a single self-evident spoken variety. Phnom Penh acoustic evidence and specialist orthographic mapping are separate evidence layers. This is not an adjudicated lexical corpus.

## 1. Orthographic class and inherent-vowel matrix

Richard Ishida's specialist Khmer Orthography Notes (updated 27 April 2026) describe two consonant classes, ɑ-class and ɔ-class. Khmer is non-tonal; class determines vowel-sign selection, while stress, vowel harmony and register-shifter diacritics may also affect output.

| Orthographic input | ɑ-class output | ɔ-class output | Evidence / qualification |
|---|---|---|---|
| Inherent vowel | /ɑː/ | /ɔː/ | Ishida: ក /kɑː/ vs គ /kɔː/ |
| Base consonant + U+17B8 ី | /əj/ | /iː/ | Explicit Ishida class-comparison example |
| Base consonant + U+17B6 ា | /aː/ | /iə/ | Explicit Ishida class-comparison example |
| U+17B7 ិ | /e/ or /ə/ in specified a-class contexts | /i/; stressed syllables may show following glottal closure | Ishida plain-vowel mappings; context-sensitive |
| U+17B9 ឹ | /ə/ | /ɨ/ | Ishida plain-vowel mappings |
| U+17BA ឺ | /əɨ/ | /ɨː/ | Ishida plain-vowel and rhyme mappings |
| U+17C2 ែ | /ae/ | /ɛː/ | Ishida vowel mappings |
| U+17BC ូ | /ou/ | /uː/ | Ishida vowel mappings |
| U+17C4 ោ | /ao/ | /oː/ | Ishida vowel mappings |
| U+17D0 ័ | /a/ in listed a-class environment | coda-conditioned outcomes include /ɨj/ or /oə̆/ in listed o-class environments | Ishida diphthong/rhyme mappings; not one sign/one sound |

Reference: Richard Ishida, [Khmer Orthography Notes](https://r12a.github.io/scripts/khmr/km.html), sections “Consonant registers,” “Post-consonant vowels,” “Diphthongs and rhymes,” “Vowel length,” and “Codas.” The page explicitly identifies stress, vowel harmony and register shifters as additional factors.

## 2. Phnom Penh acoustic vowel inventory: source-reported, not gold

Chem Vatho (2020), “The Standard Khmer vowel system: An acoustic study,” Insight: Cambodia Journal of Basic and Applied Research 2(2), 93–121, [full text PDF](https://www.cjbar.rupp.edu.kh/index.php/cjbar/article/download/36/32), supplies a bounded acoustic dataset.

| Dimension | Reported result | Locator | Limitation |
|---|---|---|---|
| Monophthongs | 21 source-reported categories: 10 long and 11 short | pp. 103–109 | Lexical gaps; some categories omitted from sample |
| Diphthongs | 13 source-reported categories: 10 long and 3 short | pp. 98–105, 110–112 | Earlier analyses differ; retain author's transcription convention |
| Speaker selection | 21 native speakers screened; four selected for acoustic analysis (two female), ages 20–50 | pp. 104–105 | Four-speaker Phnom Penh sample |
| Lexical materials | 168 items in initial screening; final analysis used 61 items, three formal-reading repetitions | pp. 104–105 | Not all phonological contrasts/codas covered |
| Series/register | First-register vowels reported lower/more open and more diphthongized than second-register vowels | abstract and pp. 96–101 | Historical breathy/modal labels are not automatically current phonation |
| Coda effect | Final consonants may modify vowel quality and length; closed syllables generally shorter | pp. 108–112 | No complete coda × series × vowel × length cross-table |
| Short diphthongs | Reported especially in closed contexts such as /-h, -k, -ʔ/ | pp. 110–111 | Source-reported sample, not exhaustive legality rule |

The paper states that “Standard Khmer” has no clear-cut definition and distinguishes Standard Khmer from Phnom Penh speech (pp. 93–96). It reports an acoustic inventory, not a complete lexeme-by-lexeme series × coda matrix. Its IPA-like symbols are the authors' transcription, not project gold.

## 3. Coda inventory and nucleus interaction

| Coda/environment | Evidence-supported statement | State |
|---|---|---|
| Final oral stops /p,t,k/ | Common codas; final realization differs from onset and has no following inherent vowel | SOURCE_REPORTED |
| Final nasals /m,n,ɲ,ŋ/ | Common coda classes; exact preceding-vowel effects need lexical/acoustic rows | SOURCE_REPORTED / PARTIAL |
| Final lateral /l/ | Included among common coda consonants in Ishida's summary | SOURCE_REPORTED |
| U+17C6 ំ | Represents final /-m/ and affects the vowel nucleus | SOURCE_REPORTED |
| U+17C7 ះ | Represents final /-h/ and affects the vowel nucleus | SOURCE_REPORTED |
| U+17CB ់ | Shortens the preceding vowel in the described use | SOURCE_REPORTED |
| Short diphthongs before /-h,-k,-ʔ/ | Reported in Chem's Phnom Penh sample | ACOUSTIC_SAMPLE |
| Every coda × every series × every vowel | No exhaustive source-backed cross-product located | NOT_ESTABLISHED |

Unicode and Ishida describe orthographic representation and mapping logic; Chem supplies a small acoustic sample. Neither source licenses extrapolating all outcomes to every final consonant.

## 4. /r/-loss is a separate profile/style matrix

Wayland & Guion (2005), Mon-Khmer Studies 35:55–82, [full paper](https://rilca.mahidol.ac.th/documents/PublicationMultimedia/MonKhmer/Vol35/wayland2005sound.pdf), compare 20 obstruent+/r/ lexical items from two male Phnom Penh speakers, three repetitions per item in careful-reading and colloquial styles. They report /r/ loss in colloquial tokens, onset aspiration, falling–rising F0 and vowel changes. This supports a conditioned Phnom Penh colloquial pathway, not universal deletion.

Kirby (2014), [Journal of Phonetics DOI](https://doi.org/10.1016/j.wocn.2014.02.001), adds production/perception evidence involving f0, aspiration/VOT, voice quality and vowel quality. Keep cues separate.

## 5. Required future row fields

| Field | Meaning |
|---|---|
| profile | Standard/Phnom Penh/other named variety |
| base_consonant_class | ɑ-class or ɔ-class, including shifter state |
| vowel_sign_sequence | Exact normalized Unicode sequence |
| stress | stressed / unstressed / unknown |
| harmony_context | preceding/following syllable class and trigger |
| nucleus_phonemic | source-backed phonemic value |
| nucleus_phonetic | measured/transcribed surface realization |
| length | short/long and measurement where available |
| coda | phonological coda, distinct from written final grapheme |
| source_locator | page/table/word/audio ID |
| evidence_status | SOURCE_REPORTED, ACOUSTIC_SAMPLE, CONFLICTING, NOT_ESTABLISHED, ADJUDICATED_GOLD |

**Status:** PARTIAL. A class-to-vowel mapping baseline and bounded Phnom Penh acoustic inventory are available. Full contextual cross-table, multi-speaker lexical evidence and independently adjudicated IPA remain outstanding. No gold labels or unverified engine rules were added.
