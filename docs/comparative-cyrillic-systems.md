# Khmer → Ukrainian: comparative Cyrillic transcription methodology

## Scope

This layer reproduces the comparative logic developed for the Thai project without copying Thai-specific rules:

source orthography → source phonology/phonetics → IPA → existing practical traditions → Ukrainian phonological target → Ukrainian practical orthography.

The Russian practical tradition is a comparator, not the Ukrainian target. Serbian and Bulgarian are included only where evidence exists.

## Russian practical tradition

The documented Russian system is unusually useful as a comparator because it is positional and explicitly handles aspiration, complex onsets, velar nasal, palatal consonants, vowels and diphthongs. It uses forms such as пх, тх and кх for aspirated onsets, нг for /ŋ/, нь for /ɲ/, and gives special rules for glottal stop and clusters. Its cited basis includes the 1967 instructions for Cambodian geographical names and Serdyuchenko's Russian transcription tradition.

Useful properties:
- distinguishes onset and coda behavior;
- exposes /ŋ/ as нг;
- explicitly represents aspiration;
- treats clusters rather than blindly substituting letters.

Problems for direct Ukrainian copying:
- /ʔ/ is rendered as к in some final contexts, which is not phonetic identity;
- /w/ may be rendered as у, collapsing a consonantal glide into a vowel;
- /c/ and /cʰ/ are adapted through Russian orthographic resources rather than Ukrainian phonological targets;
- Russian vowel choices are approximations, not evidence of Ukrainian equivalence;
- conventional exonyms must not be confused with a productive algorithm.

## Serbian

A separate authoritative Serbian Khmer practical-transcription standard was not established in the present evidence search. Serbian therefore has status evidence-limited. Individual Serbian spellings may be collected later from maps, academic works or editorial sources, but they must not be promoted to a Serbian standard without a primary source.

## Bulgarian

A Bulgarian-language International Linguistics Olympiad problem provides explicit Latin phonetic transcription of Khmer material and distinguishes short/long vowels and sounds such as /ŋ/ and /c/. This is useful evidence that Bulgarian academic material can represent Khmer phonetics, but it is not a Bulgarian Cyrillic practical-transcription standard.

## Proposed Ukrainian target policy

The canonical Ukrainian inventory is external and comes from ClippyFirst/Ukrainian-Phonetic-Inventory.

| Khmer IPA | UA default | Alternative | Reason |
|---|---|---|---|
| /p/ | п | — | direct target |
| /pʰ/ | п | пх | Ukrainian has no phonemic aspiration contrast; Russian compatibility form retained |
| /b, ɓ/ | б | — | nearest voiced bilabial target |
| /t/ | т | — | direct target |
| /tʰ/ | т | тх | aspiration kept in IPA, not default spelling |
| /d, ɗ/ | д | — | nearest voiced coronal target |
| /k/ | к | — | direct target |
| /kʰ/ | к | кх | aspiration kept in IPA, not default spelling |
| /c/ | ч | — | commonly realized as [t͡ʃ] |
| /cʰ/ | ч | чх | same practical affricate target |
| /ɲ/ | нь | — | Ukrainian has /nʲ/ and the orthographic sequence нь |
| /ŋ/ | нг | — | transparent Ukrainian digraph |
| /r/ | р | ∅ | careful/standard versus documented Phnom Penh loss |
| /l/ | л | — | direct target |
| /ʋ~w/ | в | — | Ukrainian /ʋ/ is the closest target inventory representation |
| /j/ | й | — | direct target |
| /s/ | с | — | direct target |
| /h/ | г | х | Ukrainian /ɦ/ is structurally closer than /x/; this is a target approximation |
| /ʔ/ | ∅ | ʼ | no independent Ukrainian glottal-stop grapheme |

### Why aspiration is not automatically written as х

The research representation must retain /kʰ/, /pʰ/, /tʰ/ and /cʰ/ explicitly. The practical Ukrainian default does not need to create a Ukrainian consonant cluster merely to expose aspiration, because aspiration is not a contrastive feature in the Ukrainian inventory.

Thus:

/kʰaː/ → IPA /kʰaː/ → Ukrainian target /ka/ → практичне ка.

Forms such as кха remain compatibility candidates, especially when comparing with Russian practice or when a future conservative foreign-pronunciation mode is requested.

### Why /ŋ/ remains нг

Unlike aspiration, velar nasality has no single Ukrainian grapheme. The transparent digraph нг exposes the place of articulation and prevents systematic collapse of /ŋ/ into /n/.

### Why /ʔ/ is zero by default

Khmer glottal stop is a real source-level segment in the phonological/phonetic analysis, but Ukrainian practical orthography has no dedicated glottal-stop letter. It therefore remains visible in the research/IPA layer and is normally zero in the practical string. A visible apostrophe is an explicit scholarly/editorial mode, not the default.

## Vowels

Khmer has a much richer vowel system than Ukrainian. Contemporary Phnom Penh acoustic work reports a large inventory and shows that vowel quality is affected by syllable structure and dialect.

Initial practical reduction:

- /i, iː/ → і
- /e, ɛ, ɛː/ → е
- /ɨ, ɨː/ → и
- /a, ɑ, ɑː/ → а
- /o, ɔ, ɔː/ → о
- /u, uː/ → у
- /ə, ɤ/ → е or и, selected by feature ranking and context
- complex vowels remain sequences where Ukrainian can represent them without inventing a false monophthong.

The /ɨ/ → и decision is a target-inventory decision, not a claim that Khmer /ɨ/ and Ukrainian /ɪ/ are identical.

## Phnom Penh /r/

Do not implement /r/ → ∅ globally.

In careful/standard pronunciation /r/ remains part of the source analysis. In colloquial Phnom Penh Khmer, /r/ in onset clusters can be lost and replaced by aspiration, f0 contour, phonation and/or diphthongization. This is documented as an active sound-change phenomenon.

The engine therefore needs at least:
- pronunciation_profile=careful_standard
- pronunciation_profile=phnom_penh_colloquial

The default practical profile remains careful/standard unless the caller explicitly selects colloquial Phnom Penh.

## Tone

Khmer is not treated as a lexical tone language in the core standard model. The Phnom Penh /r/-loss phenomenon can create emerging f0 contrasts, but these belong to the phonetic/dialect layer. The default Ukrainian spelling therefore does not invent tone diacritics.

## Status

Russian: evidence-supported comparator.
Serbian: evidence-limited; no separate normative system established.
Bulgarian: academic phonetic evidence, not a Cyrillic practical standard.
Ukrainian: proposed research layer, not an official standard and not yet empirically validated.

No accuracy percentage is assigned without a versioned adjudicated corpus.
