# Khmer → Ukrainian practical transcription

## Purpose and pipeline

The practical layer is applied only after source-language analysis:

**Khmer orthography → graphemic/orthographic syllable analysis → Khmer phonology → IPA → Ukrainian target-language adaptation → Ukrainian practical orthography**

This is not character-by-character transliteration. The Ukrainian rendering is a project-specific research proposal, not an officially approved Ukrainian transcription standard.

## Profiles

### `careful_standard`

Default for academic, editorial and reference use.

### `phnom_penh_colloquial`

Optional pronunciation profile. It may model documented /r/-loss and associated aspiration, pitch, voice-quality and vowel effects. It must not overwrite the careful analysis or infer aspiration for every /Cr/ cluster.

### `established_form`

A separately versioned lexicon may override the generic algorithm for conventional Ukrainian exonyms and historically established names. Every override needs provenance and a source; a familiar Ukrainian name is not evidence for a general Khmer rule.

## Ukrainian target correspondences

| IPA | Ukrainian practical form | Notes |
|---|---|---|
| /p, b/ | п, б | Direct practical targets |
| /pʰ, tʰ, kʰ/ | п', т', к' | Aspiration is marked with the project apostrophe |
| /t, d/ | т, д | Direct practical targets |
| /c/ | ть | Preserve the palatal stop rather than converting it to an affricate |
| /cʰ/ | ть' | Palatal stop plus aspiration; do not automatically write ч' |
| /ɲ/ | нь | Palatal nasal |
| /ŋ/ | нг | Keep the velar nasal visible |
| /ʋ/ | в | Labiodental approximant |
| /w, ʋ/ | в | Ukrainian target merges both approximants in practical spelling; IPA preserves the source distinction |
| /j/ | я, є, ї, ю, йо at syllable onset; й elsewhere | Contextual Ukrainian yotation is applied by the IPA adapter |
| /h, ɦ/ | г | Ukrainian target approximation |
| /ɡ/ (ASCII alias /g/) | ґ | Explicit contrast-preserving project choice |
| /x/ | х | Genuine velar fricative; not merged with /h/ |
| /ʔ/ | ∅ | Preserved in IPA/trace, omitted in practical output; not aspiration |

### Affricates and fricatives

| IPA | Ukrainian | Distinction |
|---|---|---|
| /t͡s/ | ц | Explicit affricate |
| /d͡z/ | дз | Explicit voiced affricate |
| /t͡ʃ/ | ч | Postalveolar affricate |
| /d͡ʒ/ | дж | Voiced postalveolar affricate |
| /tɕ, t͡ɕ/ | ч | Alveolo-palatal practical approximation |
| /dʑ, d͡ʑ/ | дж | Voiced alveolo-palatal practical approximation |
| /ʃ/ | ш | Postalveolar fricative |
| /ʒ/ | ж | Voiced postalveolar fricative |

An adjacent /t/ + /s/ sequence is not rewritten as ц unless the source IPA explicitly identifies an affricate /t͡s/. The same rule applies to /d/ + /z/ versus /d͡z/.

The IPA symbols /t͡s/, /d͡z/, /t͡ʃ/ and /d͡ʒ/ are general target-adapter coverage. Their presence in this table does not claim that all are native Khmer phonemes.

## Ukrainian-specific conventions and normative status

The 2026 Ukrainian Orthography is the current state standard (effective 2026-03-28). §122 says foreign [g] is usually adapted with г; it also allows ґ as an imitation of foreign [g] in personal names. This project deliberately selects ґ for IPA /ɡ/ to preserve the distinction requested for this adapter, while /h/ maps to г and /x/ to х. This is a project policy, not a claim that ґ is the only normatively valid rendering of every foreign /g/.

The practical apostrophe after aspirated consonants is a project notation for a source-language feature. It is not the Ukrainian orthographic apostrophe rule and does not replace IPA metadata. A glottal stop /ʔ/ never triggers it.

The 2026 standard's treatment of [h], [g], [w], [θ] and [ð] is target-language guidance, not evidence about Khmer source phonology. See §§122, 124 and 126 of the official standard.

## Vowels

| Khmer IPA | Ukrainian practical form |
|---|---|
| /i, iː/ | і |
| /e, ɛ, ɛː/ | е |
| /ɨ, ɨː/ | и |
| /a, ɑ, ɑː/ | а |
| /o, ɔ, ɔː/ | о |
| /u, uː/ | у |
| /ə, ɤ/ | е |
| attested complex vowels | Ukrainian vowel sequences only where the IPA policy has an explicit entry |

Length and source vowel quality remain available in IPA and the trace; ordinary Ukrainian practical spelling does not double vowels automatically.

## Executable adapter

map_ipa_string() is the single longest-match IPA-string adapter used by the deterministic Khmer engine. It applies Ukrainian yotation to syllable-initial /j/ plus a following vowel and maps /w/ to в (the Russian comparator's у is not copied). It:

- maps multi-codepoint IPA segments before their component characters;
- preserves spaces between IPA chunks;
- removes stress marks and syllable dots from practical spelling while leaving source IPA intact;
- withholds the whole practical result if an IPA segment is unsupported;
- does not fall back to Russian mappings or character-by-character guesses.

Example segment sequences (illustrative adapter tests, not lexical gold labels):

| IPA input | Ukrainian output |
|---|---|
| /kʰaː/ | к'а |
| /cʰa/ | ть'а |
| /ha/ | га |
| /ɡa/ | ґа |
| /xa/ | ха |
| /t͡sa/ | ца |
| /d͡za/ | дза |
| /t͡ʃa/ | ча |
| /d͡ʒa/ | джа |
| /tɕa/ | ча |

## Russian comparison

The Russian practical tables supplied for comparison are useful historical/documentary controls, not the target specification. In particular, Russian /h/ → х is not copied into Ukrainian; the Ukrainian project distinguishes /h/ → г from genuine /x/ → х. Russian spellings such as кх/тх/пх are also not copied; aspiration is represented with the project's apostrophe marker while remaining fully inspectable in IPA.

Reference comparison pages:
- [Khmer–Russian practical transcription](https://ru.wikipedia.org/wiki/Кхмерско-русская_практическая_транскрипция)
- [Official Ukrainian Orthography, 2026 PDF](https://mon.gov.ua/static-objects/mon/sites/1/zagalna%20serednya/Pravopys.2019/ukrayinskii-pravopis-oficiine-vidannia-2026.pdf)

## Validation gate

The system is not an empirically validated Ukrainian standard until the repository contains a sufficiently broad, provenance-bearing Khmer lexical/proper-name corpus with authoritative source IPA, independently adjudicated Ukrainian outputs, Russian comparison outputs, and error analysis by construction class. The current segment-level adapter tests verify deterministic mapping behavior, not real-world phonetic accuracy.
