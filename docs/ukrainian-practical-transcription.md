# Proposed Ukrainian practical transcription layer

## Pipeline

Khmer orthography → grapheme/orthographic syllable analysis → Khmer phonology → conservative IPA → Ukrainian feature candidates → Ukrainian orthography.

The output is not produced by Khmer-character substitution.

## Profiles

### careful_standard
Default for academic, editorial and reference use.

### phnom_penh_colloquial
Optional pronunciation profile. It may model documented /r/-loss and its associated aspiration, pitch and vowel effects. It must never overwrite the careful analysis.

### established_form
A separately versioned lexicon can override the generic algorithm for conventional Ukrainian exonyms and historically established names.

## Candidate ranking

1. IPA feature distance to the canonical Ukrainian inventory.
2. Ukrainian phonotactic legality.
3. Ukrainian orthographic legality.
4. Preservation of source onset/coda role.
5. Preservation of source contrasts where Ukrainian can represent them.
6. Independently documented Ukrainian usage.
7. Readability.

No probability is assigned without a calibrated corpus.

## Core correspondences

| Khmer | Ukrainian |
|---|---|
| /p/ | п |
| /pʰ/ | п |
| /b, ɓ/ | б |
| /t/ | т |
| /tʰ/ | т |
| /d, ɗ/ | д |
| /k/ | к |
| /kʰ/ | к |
| /c/ | ть |
| /cʰ/ | ч |
| /ɲ/ | нь |
| /ŋ/ | нг |
| /r/ | р |
| /l/ | л |
| /ʋ/ | в |
| /w/ | у |
| /j/ | й |
| /s/ | с |
| /h/ | х |
| /ʔ/ | ∅ |

## Vowel reduction

| Khmer | Ukrainian |
|---|---|
| /i, iː/ | і |
| /e, ɛ, ɛː/ | е |
| /ɨ, ɨː/ | и |
| /a, ɑ, ɑː/ | а |
| /o, ɔ, ɔː/ | о |
| /u, uː/ | у |
| /ə, ɤ/ | е/и by context |
| complex vowels | Ukrainian vowel sequences when supported |

Length remains available in the research layer and is not normally doubled in practical Ukrainian spelling.

## Research versus practical output

Example:

Khmer /kʰaː/

research IPA: /kʰaː/
UA phonological target: /ka/
practical: ка
Russian compatibility candidate: кха

The Russian candidate is not silently promoted to the Ukrainian default.

Example:

Khmer /ŋaː/

research IPA: /ŋaː/
UA target: /ŋaː/
practical: нга

Example:

Khmer /ʔa/

research IPA: /ʔa/
UA target: /a/
practical: а

The glottal stop remains inspectable even though it is not printed.

## Established forms

Conventional names such as Камбоджа must be stored as provenance-bearing lexical overrides. They are not evidence for a generic Khmer orthography-to-Ukrainian rule.

## Validation gate

Before describing the system as an empirically validated Ukrainian standard, the repository must contain:
- versioned Khmer lexical/proper-name corpus;
- source pronunciation or authoritative IPA;
- independently adjudicated Ukrainian outputs;
- Russian comparison outputs;
- error analysis by construction class;
- separate evaluation of careful versus Phnom Penh colloquial profiles.
