# Khmer phonology and pronunciation model

## Scope

The repository distinguishes a descriptive phonetic inventory from a deterministic orthography-to-IPA algorithm. The latter is incomplete and must not be simulated by guesswork.

Modern Khmer is non-tonal in the core model. Its consonant classes/registers determine vowel realization, and contemporary Phnom Penh speech has additional contextual effects.

## Consonants

The current inventory includes the 33 basic consonant letters and records their principal onset values separately from orthographic class. Foreign/loanword consonant combinations are kept outside the core 33-letter inventory unless separately evidenced.

## Vowels

The descriptive inventory includes short/long plain vowels and complex vowels. The repository does not equate a vowel sign with one IPA vowel: the same written sign can be realized differently after the two consonant classes/registers. Representative documented contrasts include ក /kɑː/ vs គ /kɔː/, and កី /kəj/ vs គី /kiː/.

Chem & Chem's acoustic study specifically investigates the Phnom Penh dialect as a candidate standard variety and reports systematic differences between first- and second-register vowels, including quality and diphthongization differences.

## Syllable structure

A useful descriptive model is C(C)(C)V with complex onsets and restricted codas. Orthographic syllables and phonetic syllables are not identical; stacked consonants can encode cross-syllabic structure. Therefore the current parser is a structural foundation, not a complete phonetic syllabifier.

## /r/-loss

Colloquial Phnom Penh pronunciation can lose /r/ in relevant onset clusters and show associated aspiration, f0, phonation and vowel effects. This is a profile-level phonetic process, not a global spelling rule; see the sources listed in `data/khmer/sources.json` (Wayland 2005; Kirby 2014).

The current `render_ipa_profile()` implementation is intentionally narrower than the full phenomenon: it replaces /r/ with an aspiration marker only for a limited set of stop+/r/+vowel strings at the beginning of the supplied IPA string or after an explicit space, syllable dot, or stress mark. It does not infer syllable boundaries, and leaves an unsegmented medial match such as `akra` unchanged. This boundary restriction prevents blind substring rewriting, but it also means that a word-internal onset is transformed only when the input explicitly marks its boundary.

This is a provisional string-level approximation, not a validated phonological rule set or complete acoustic model. It does not model the full F0, phonation, vowel-quality/diphthongization, or lexical/dialect conditioning. Unit tests establish the implementation's bounded behavior only; they do not establish which lexical environments undergo /r/-loss.

## Glottal stop

The glottal stop is part of the phonetic analysis. In practical Ukrainian output it may be neutralized to zero by project policy, but it remains explicit in the research layer. Independent-vowel constructions commonly involve a glottal onset in pronunciation.

## Open research gap

The next major linguistic artifact should be a versioned matrix:

base series × vowel sign × coda × syllable type × length × stress/profile → phonological vowel → IPA → Ukrainian candidates

That matrix must be built from lexical evidence rather than generated solely from Unicode sign names.
