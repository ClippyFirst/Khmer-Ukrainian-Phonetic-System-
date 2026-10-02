# Methodology

## Research question
How can a Khmer orthographic form be represented as a structured linguistic object and mapped, with explicit evidence and uncertainty, to a Ukrainian phonetic-graphemic target?

## Separation of levels
The project treats Unicode code-point sequence, orthographic grapheme structure, orthographic syllable, Khmer phonological analysis, surface phonetics, IPA, phonetic features, Ukrainian phonological target and Ukrainian orthography as distinct levels.

A Khmer code point is therefore never treated as a direct Ukrainian letter by default.

## Scope
The primary contemporary target is Standard Khmer with Phnom Penh-oriented pronunciation where evidence is available. Historical, dialectal and competing analyses carry explicit metadata.

## Register
Unicode documents two consonant registers and their nominal inherent-vowel series, plus register shifter signs. This is an orthographic/structural fact. The phonetic interpretation of modern register-conditioned vowels is not collapsed into a universal “breathy vs clear” claim. Contemporary acoustic literature shows that Phnom Penh Khmer requires a cautious treatment, while historical literature describes register/phonation differently.

## Evidence policy
Every scientific claim should identify source, scope, analysis status, confidence, and whether it is an implementation assumption.

## Correspondence
Khmer orthography → graphemic analysis → Khmer phonology → surface phonetics → IPA → feature representation → Ukrainian candidate generation → Ukrainian phonological/orthographic constraints → ranked candidates.

The Ukrainian inventory is external to this repository and must not be silently duplicated.

## Validation
No accuracy figure is reported until a genuine gold-standard corpus is assembled and independently adjudicated.
