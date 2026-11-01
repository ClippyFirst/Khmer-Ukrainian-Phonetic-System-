# Khmer phonology research workpack

**Scope:** Standard Khmer with a separately versioned Phnom Penh colloquial profile. Do not collapse careful Standard Khmer and colloquial Phnom Penh speech into one pronunciation rule.

## Evidence already located

1. Ratree P. Wayland & Susan G. Guion (2005), “Sound changes following the loss of /r/ in Khmer: a new tonogenetic mechanism?”, *Mon-Khmer Studies* 35, 55–82. [Full paper](https://rilca.mahidol.ac.th/documents/PublicationMultimedia/MonKhmer/Vol35/wayland2005sound.pdf), DOI [10.15144/MKSJ-35.55](https://doi.org/10.15144/MKSJ-35.55). The acoustic study compares colloquial and careful-reading C₁rVC(V)C forms and reports /r/ loss, onset aspiration, diphthongization of short/long front [a] to [ea], and falling-rising pitch in its Phnom Penh colloquial data. The authors explicitly describe two speakers; do not generalize their sample to all speakers or all contexts.
2. James P. Kirby (2014), “Incipient tonogenesis in Phnom Penh Khmer: Acoustic and perceptual studies,” *Journal of Phonetics* 43, 69–85, DOI [10.1016/j.wocn.2014.02.001](https://doi.org/10.1016/j.wocn.2014.02.001). [Publisher record](https://www.sciencedirect.com/science/article/pii/S0095447014000163). Reports multiple cues associated with colloquial /r/-loss: f0, aspiration/VOT, breathy voice and vowel-quality change; the study includes production and perception evidence.
3. [Standard Khmer Vowel System: An Acoustic Study](https://zenodo.org/records/3377387) reports register-related vowel differences and Phnom Penh acoustic variation. Treat its inventory and measurements as a source to inspect and reconcile, not as an automatically accepted canonical table.
4. Unicode 17 Chapter 16 documents the orthographic consonant series and Khmer script ordering; it does not establish phonetic realization. [Unicode chapter](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-16/).

## Required research matrix

| Workstream | Required matrix | Acceptance evidence |
|---|---|---|
| Vowels | Dependent sign × consonant series × short/long × coda × syllable type × pronunciation profile | Exact source/recording locator per cell; phonemic and phonetic values separated |
| Series/register | Onset series × inherent vowel × dependent vowel × context | Reconcile traditional A/O series labels with phonological register analysis; record historical vs synchronic claims |
| Codas | Final grapheme/cluster × phonological coda × surface realization × preceding vowel | Source-backed inventory, contextual allophones and explicit unknowns |
| /r/-loss | Underlying /Cr/ × speech style × speaker × vowel × coda × acoustic cues | Matched careful/colloquial recordings; /r/ presence/absence, VOT, f0, voice quality, formant trajectory |
| Ukrainian target | Adjudicated surface IPA × Ukrainian output | Preserve aspiration, palatality, register-derived vowel differences and uncertainty without inferring them from script alone |

## Highest-risk questions

1. Which vowel-sign × series × coda cells have direct lexical or acoustic evidence, and which are extrapolations?
2. Which register contrasts remain phonemic in the selected Standard Khmer profile, and which are historical or phonetic descriptions?
3. Does Phnom Penh /r/-loss apply only to particular /Cr/ clusters and colloquial styles? The studies show variation; it must be conditioned, not a blanket rewrite.
4. Are f0, aspiration, breathiness and diphthongization jointly present, optional, speaker-specific, or lexically conditioned?
5. Does the coda alter the vowel realization in a way that the current grapheme-level tables miss?

## Execution order

- [ ] Extract the existing dependent-vowel × series coverage report and reconcile every cell with primary phonological/acoustic sources.
- [ ] Expand the matrix to include length, coda and profile; keep `ATTESTED_EXAMPLE`, `CONFLICTING`, `NOT_ESTABLISHED` and `ADJUDICATED_GOLD` distinct.
- [ ] Re-read Wayland & Guion (2005) and Kirby (2014), record sample size, tasks, speech styles, speaker details and acoustic measurements.
- [ ] Build matched /Cr/ and non-/Cr/ lexical sets, with careful and colloquial speech from multiple speakers.
- [ ] Double-annotate narrow phonetic IPA and acoustic cues; adjudicate disputed /r/, aspiration, breathiness, f0 and vowel trajectories.
- [ ] Only then revise the phonology engine and Ukrainian adaptation rows.

**Current status:** PARTIAL. The current coverage report is a grapheme/series evidence inventory, not a complete phonological matrix or accuracy score. Independent lexical gold remains 0. No new Khmer IPA labels are added in this workpack.
