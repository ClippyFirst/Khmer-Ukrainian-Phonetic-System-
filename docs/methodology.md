# Methodology

## Research question

How can a Khmer orthographic form be represented as a structured linguistic object and mapped, with explicit evidence and uncertainty, to a Ukrainian practical phonetic-graphemic target?

The project uses the term **practical phonetic-graphemic correspondence system** deliberately: the target is Ukrainian Cyrillic, but the mapping is mediated by source-language phonology/phonetics rather than direct character substitution.

## Separation of levels

The project treats Unicode code-point sequence, orthographic grapheme structure, orthographic syllable, Khmer phonological analysis, surface phonetics, IPA, phonetic features, Ukrainian phonological target and Ukrainian orthography as distinct levels.

A Khmer code point is therefore never treated as a direct Ukrainian letter by default.

## Scope

The primary contemporary target is Standard Khmer with Phnom Penh-oriented pronunciation where evidence is available. Historical, dialectal and competing analyses carry explicit metadata.

## Register and vowels

Khmer consonant classes/registers are structural orthographic information that affects vowel realization. This must not be reduced to a single universal phonation label. Modern acoustic work shows substantial first/second-register vowel differences, while historical descriptions use partly different phonetic interpretations.

The canonical vowel model therefore stores:
- source vowel inventory;
- orthographic series;
- length;
- complex-vowel status;
- contextual factors;
- evidence/status.

The full orthography-to-IPA matrix remains a research task.

## Evidence policy

Every scientific claim should identify source, scope, analysis status, and whether it is an implementation assumption.

Unicode is authoritative for script/encoding structure but is not silently used as evidence for modern phonetic realization.

## Correspondence

Khmer orthography → graphemic analysis → Khmer phonology → surface phonetics → IPA → feature representation → Ukrainian candidate generation → Ukrainian phonological/orthographic constraints → practical output.

The Ukrainian inventory is external to this repository and must not be silently duplicated.

## Comparative methodology

Russian practical transcription is used as a comparator. For each divergence the project asks whether the divergence is caused by:
- Khmer phonology;
- Russian phonology;
- Russian orthography;
- historical convention;
- practical editorial convention.

Only the source-language fact is portable automatically. A Russian spelling choice is not automatically evidence for Ukrainian spelling.

## Validation

No accuracy figure is reported until a genuine gold-standard corpus is assembled and independently adjudicated.
