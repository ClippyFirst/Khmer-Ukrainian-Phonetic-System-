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


## Verified evidence extraction — 2026-11-01

### Independent /r/-loss study: scope and limits

Wayland & Guion (2005), *Mon-Khmer Studies* 35:55–82, [full paper](https://rilca.mahidol.ac.th/documents/PublicationMultimedia/MonKhmer/Vol35/wayland2005sound.pdf), directly compares careful-reading and colloquial Phnom Penh pronunciations. The sample is two male native speakers from Phnom Penh, 20 lexical items beginning with an obstruent + /r/ cluster, and three repetitions of each item in each style. The study measured VOT or affricate frication, F0 at five vowel positions, and F1/F2. It reports colloquial falling–rising F0 contours, increased onset aspiration, and vowel changes including /a, aː/ → [ea] and /ɔː/ → [ɔə] in the examined items. The paper itself cautions that its proposed aerodynamic explanation lacks direct aerodynamic data.

**Implementation boundary:** these findings justify a Phnom Penh colloquial profile with a conditional /Cr/ pathway and separate reading/colloquial outputs. They do not justify deleting every orthographic or underlying /r/, nor a universal Khmer tone rule. The two-speaker, 20-item sample is a research anchor, not sufficient lexical coverage or independent gold for the project.

### Vowel and register evidence

Chem & Chem (2020), “The Standard Khmer vowel system: An acoustic study,” [publisher record](https://www.cjbar.rupp.edu.kh/index.php/cjbar/article/view/36), is an acoustic description focused on Phnom Penh. Its authors note that “standard Khmer” is not sharply defined. Use it to populate source-located vowel measurements only after extracting its actual tables and reconciling short/long vowels, series and coda context; do not convert its abstract into a complete inventory.

Kirby (2014), *Journal of Phonetics* 43:69–85, [DOI](https://doi.org/10.1016/j.wocn.2014.02.001), adds production and perception evidence for f0, aspiration/VOT, voice quality and vowel-quality cues. These are interacting cues, not a licence to encode /r/-loss as a single replacement segment.

**Status update:** /r/-loss evidence is now more precisely scoped and method-documented; independent multi-speaker replication, full vowel × series × length × coda coverage, and IPA adjudication remain PARTIAL/BLOCKED. No Khmer IPA labels or engine rules were added.


### Additional extraction: Chem (2020) full text

The full article is now linked in the source registry. Its methods report 21 native speakers in initial screening (168 lexical items, two repetitions), then four selected Phnom Penh speakers (two female) for acoustic analysis of 61 lexical items, repeated three times in formal reading (pp. 104–105). It reports 21 monophthong categories (10 long, 11 short) and 13 diphthongs (10 long, 3 short; pp. 103–105). It reports coda effects on vowel quality and duration, with closed syllables generally shorter; short diphthongs occur in sample contexts with /-h, -k, -ʔ/ (pp. 108–112).

This materially improves the vowel evidence baseline, but does not fill the complete consonant-series × vowel-sign × coda cross-table. The article itself notes that Standard Khmer is not sharply defined, and the four-speaker sample is not a universal norm. The published transcription and measured tokens remain source evidence, not adjudicated project gold.

See the new [Khmer vowel × series × coda evidence matrix](KHMER-VOWEL-SERIES-CODA-EVIDENCE-MATRIX-2026-11-01.md), which separates Ishida's specialist orthographic mappings from Chem's bounded acoustic sample.
