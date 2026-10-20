# Coda diacritic evidence matrix: NIKAHIT and REAHMUK

**Audit date:** 2026-10-20  
**Primary orthography source:** Richard Ishida, *Khmer (Cambodian) Orthography Notes*, updated 27 April 2026, sections “Nikahit and reahmuk” and “Coda diacritics”.  
**Reference:** https://r12a.github.io/scripts/khmr/km.html  
**Encoding/structural cross-check:** Unicode Consortium, *Khmer Encoding Structure*, TN61: https://www.unicode.org/notes/tn61/utn61-Khmer_Encoding_Structure_V2.pdf

## Scope and rules

This is a source-transcription inventory, not a gold pronunciation corpus. The rhyme labels below reproduce the R12A table for the two consonant classes. They are useful evidence for contextual distinctions but do not by themselves establish a complete orthography-to-IPA algorithm, lexical coverage, or one dialect-independent pronunciation.

R12A explains that U+17C6 NIKAHIT (ំ, approximately coda /m/) and U+17C7 REAHMUK (ះ, approximately coda /h/) can affect the syllable nucleus and are regarded as vowels in Khmer descriptions. The sign names alone must not be treated as a mapping rule.

## REAHMUK: 12 first-series rows

| ID | Encoded rhyme sequence | R12A transcription | Evidence status | Implementation implication |
|---|---|---|---|---|
| RM-A01 | ិះ (U+17B7 + U+17C7) | eh | SOURCE-INDEXED | Keep as contextual rhyme candidate; no universal IPA output yet |
| RM-A02 | េះ (U+17C1 + U+17C7) | eh | SOURCE-INDEXED | Same listed rhyme transcription as RM-A01, distinct spelling |
| RM-A03 | ែះ (U+17C2 + U+17C7) | eh | SOURCE-INDEXED | Do not infer equivalence beyond this source's table |
| RM-A04 | ុះ (U+17BB + U+17C7) | oh | SOURCE-INDEXED | Coda changes expected value from plain vowel-sign reading |
| RM-A05 | ឹះ (U+17B9 + U+17C7) | əh | SOURCE-INDEXED | Preserve vowel-plus-coda context |
| RM-A06 | ើះ (U+17BE + U+17C7) | əh | SOURCE-INDEXED | Same listed rhyme transcription as RM-A05; no broad rule implied |
| RM-A07 | ះ (U+17C7) | ah | SOURCE-INDEXED | REAHMUK-only rhyme listed for first series |
| RM-A08 | ោះ (U+17C4 + U+17C7) | ah | SOURCE-INDEXED | Do not generalize from this row to other classes |
| RM-A09 | ុំ (U+17BB + U+17C6) | om | COMPARATOR | NIKAHIT after U sign; source lists a first-series rhyme |
| RM-A10 | ាំ (U+17B6 + U+17C6) | am | COMPARATOR | NIKAHIT after AA sign; not a REAHMUK form |
| RM-A11 | ំ (U+17C6) | am | COMPARATOR | NIKAHIT alone; source lists a first-series rhyme |
| RM-A12 | ាំង (U+17B6 + U+17C6 + ង) | aŋ | COMPARATOR | NIKAHIT sequence with final NGO; not a REAHMUK form |

## REAHMUK: 9 second-series rows

| ID | Encoded rhyme sequence | R12A transcription | Evidence status | Implementation implication |
|---|---|---|---|---|
| RM-O01 | ិះ (U+17B7 + U+17C7) | ih | SOURCE-INDEXED | Same sequence differs from first-series table; register conditioning matters |
| RM-O02 | េះ (U+17C1 + U+17C7) | ih | SOURCE-INDEXED | Do not collapse with first-series row |
| RM-O03 | ោះ (U+17C4 + U+17C7) | uə̆h | SOURCE-INDEXED | Source lists short complex vowel + /h/ |
| RM-O04 | ុះ (U+17BB + U+17C7) | uh | SOURCE-INDEXED | Keep series-specific value |
| RM-O05 | ំ (U+17C6) | um | COMPARATOR | NIKAHIT control row |
| RM-O06 | ះ (U+17C7) | eə̆h | SOURCE-INDEXED | R12A explicitly describes -eə̆h after a second-series consonant |
| RM-O07 | ាំង (U+17B6 + U+17C6 + ង) | eə̆ŋ | COMPARATOR | NIKAHIT + nasal coda sequence |
| RM-O08 | ាំ (U+17B6 + U+17C6) | oə̆m | COMPARATOR | NIKAHIT named sequence; differs from first-series table |
| RM-O09 | ុំ (U+17BB + U+17C6) | um | COMPARATOR | NIKAHIT sequence; source also notes it as a named sequence |

**Important correction to inventory interpretation:** the R12A panel is titled as a list of rhymes following ɑ-class and ɔ-class consonants, respectively, but it includes both REAHMUK and NIKAHIT combinations. Therefore, the panel's total counts (12 and 9) must not be reported as “12 and 9 REAHMUK rules”. The tables above preserve the source's visible inventory while marking NIKAHIT comparator rows separately. The first-series panel contains eight REAHMUK spellings and four NIKAHIT spellings; the second-series panel contains five REAHMUK spellings and four NIKAHIT spellings. Some forms also occur in named-sequence notes and should be deduplicated by orthographic sequence plus series, not by surface transcription alone.

## NIKAHIT lexical contrasts explicitly illustrated by R12A

| Orthography | Source gloss | Source transcription | What it supports | What it does not support |
|---|---|---|---|---|
| ដំ | to pound | /dɑm/ (source's table convention) | A NIKAHIT form can have a short nucleus | General short-vowel rule for all NIKAHIT forms |
| ដម | nectar | /ɗɑːm/ (source's table convention) | Similar consonant spelling without NIKAHIT can differ in nucleus length/quality | An exhaustive minimal-pair analysis or acoustic measurement |
| ពាំ | carry in the beak | /pɔ̀əm/ | AA + NIKAHIT is not simply /aːm/ | One universal realization for all series or lexical contexts |
| ពាម | mouth of a river | /piəm/ | Related spelling without NIKAHIT differs in the source | Universal mapping of U+17B6 |

R12A's displayed transcription conventions should be retained verbatim in source notes. If converting them to the project's IPA conventions, record that normalization as a separate, reviewable step rather than silently changing the source value.

## Status and next actions

- **Orthographic evidence:** source-indexed and useful for building a context inventory.
- **Phonetic adjudication:** incomplete; no claim of acoustic gold status.
- **Parser:** must preserve U+17C6/U+17C7 and vowel signs as structured elements; should not assign deterministic IPA from the mark alone.
- **Next:** create lexical examples for each supported rhyme, record source/variety/gloss/transcription convention, and independently adjudicate against a suitable dictionary and/or phonetic study before promoting rows to deterministic rules.

## References

1. Ishida, Richard. *Khmer (Cambodian) Orthography Notes*. Updated 27 April 2026. https://r12a.github.io/scripts/khmr/km.html
2. Unicode Consortium. *Khmer Encoding Structure*, Unicode Technical Note #61. https://www.unicode.org/notes/tn61/utn61-Khmer_Encoding_Structure_V2.pdf
3. Chem, Vatho & Chem, Vatho. “The Standard Khmer vowel system: An acoustic study.” *Insight: Cambodia Journal of Basic and Applied Research* 2(2), 2020, pp. 57–88. https://doi.org/10.61945/cjbar.2020.2.2.3
