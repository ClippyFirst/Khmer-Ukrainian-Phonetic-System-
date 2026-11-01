# Controlled IPA gold acquisition — Khmer

**Status:** protocol ready for a human pilot; this document admits no gold labels.  
**Scope:** a controlled Khmer pilot followed by a versioned, independently adjudicated benchmark.

## Evidence boundary

A pronunciation from this repository, G2P, romanizer, dictionary, language model, or annotator memory is not gold merely because it is plausible. Keep source evidence, expert judgments, and engine predictions separate. Never seed an annotation with model output or infer complete IPA from spelling alone.

Choose one target profile before sampling. Recommended initial profile: contemporary Phnom Penh Khmer, careful citation forms, with one approved broad-phonemic or broad-phonetic convention. Do not merge regional, rural, diaspora, or colloquial variants into one undifferentiated score.

## Roles and blindness

1. **Curator:** selects lexemes, checks sources/rights, assigns opaque IDs, prepares packets; does not annotate.
2. **Annotators A and B:** independently transcribe identical packets. They see orthography, disambiguating gloss/context, target variety, and source/audio evidence, but never each other's work or engine predictions.
3. **Adjudicator C:** receives both locked submissions only after both arrive; cannot be A or B; records decision and rationale.
4. **Release maintainer:** validates provenance, rights, schema, split integrity, and export.

Use stable pseudonymous IDs in Git. Keep identity mappings and contact details outside the repository. Never place private audio or personal data in public issues or PRs.

## Pilot sampling

Start with **30 lexeme groups** as a process pilot, not an accuracy benchmark. Select attested items to cover, where supported by the chosen profile and sources:

- first/second consonant series and vowel contrasts they condition;
- short/long vowels, diphthongs, and offglides;
- open vs closed syllables and coda classes;
- stress/prominence and mono- vs disyllabic forms;
- onset /r/ environments, with conservative and documented Phnom Penh variants separately profiled;
- NIKAHIT/REAHMUK contexts that may affect nucleus and coda;
- source disagreements and cases marked uncertain by the engine.

Do not generate a theoretical Cartesian product. Every item must be an attested lexeme with an exact source locator. Record selection rationale and uncovered cells. Keep pilot items out of held-out evaluation if used to revise the engine.

## Khmer convention sheet

Approve a versioned sheet specifying target variety, speaker context, citation vs connected speech, IPA kind, first/second series representation, vowel quality and length, diphthongs/offglides, syllable boundaries, coda realization, stress/prominence, /r/-loss scope, phonation/aspiration/F0, uncertainty, and variant policy.

Chem (2020) provides acoustic evidence on Phnom Penh vowels, duration, and coda effects, but is not a complete orthography-to-IPA lexicon: https://www.cjbar.rupp.edu.kh/index.php/cjbar/article/view/36. Kirby (2014) documents incipient F0-based contrasts and multiple acoustic cues in Phnom Penh speech; do not reduce all colloquial /r/-loss tokens to one categorical replacement: https://www.sciencedirect.com/science/article/pii/S0095447014000163.

## Candidate external references — do not auto-import

### MekongPhon

MekongPhon (LREC 2026) reports 1.3 million Khmer and 367,000 Lao orthography–IPA pairs: https://lrec.elra.info/lrec2026-main-129. It is a candidate external reference, not admitted gold. Verify dataset version/checksum, dataset-specific license, variety, IPA convention, source provenance, verification method, duplicates/variants, and overlap with development sources. The proceedings' CC BY-NC-4.0 license does not establish the dataset's own license.

### Khmer Acoustic Model dictionary

https://github.com/chemvatho/Khmer-acoustic-model reports a 29,204-entry IPA dictionary and native-linguist validation; its README states that dictionary data are CC BY-SA 4.0, distinct from the MIT code/model license. This is promising for external comparison and source discovery, not automatically our gold. Inspect actual dictionary, metadata, exact commit, per-entry provenance, variety/profile, transcription consistency, and rights before using any entry. Do not copy entries just because the repository is public.

## Controlled workflow

1. Curator freezes the pilot list and records source provenance and rights before annotation.
2. Curator generates opaque IDs and two separate packets with identical evidence and conventions, excluding model output and competing IPA.
3. A and B submit separately. Curator timestamps and locks both before either sees the other.
4. C reviews both locked submissions and source packet. C records AGREEMENT, RESOLVED, or UNRESOLVED. RESOLVED requires final IPA and written evidence-based rationale; do not force agreement.
5. Curator validates schema, cross-file links, duplicates, rights, and blindness checklist. Unresolved items remain outside gold.
6. Export only rights-cleared adjudicated items. Keep restricted source material external; store exact locators/checksums where permitted.
7. Freeze a versioned manifest before benchmarking.

## Annotation packet

Include opaque record ID; target profile; orthography and NFC form; gloss/minimal context; source title/provider/version/page/entry/audio locator; rights evidence; lawful audio access and recording context; pseudonymous speaker ID; IPA kind and convention-sheet version; literal IPA, syllable boundaries, tone if relevant, length, phonation, confidence, uncertainty, and comments.

## Acceptance gates

- **Pilot can start:** variety and convention sheet approved; two qualified annotators and independent adjudicator confirmed; rights-cleared packets ready; blind intake dry-run passed.
- **Pilot accepted:** 30 items have two independent submissions; all disagreements adjudicated or explicitly unresolved; provenance/rights complete; blindness evidenced; validation passes.
- **Benchmark-ready:** expanded stratified corpus; frozen train/dev/test manifest; no lexeme leakage; held-out test untouched during tuning; coverage report for series × vowel × stress × coda, with /r/-loss variants separately profiled; rights and reproducibility review passed.

Existing numeric thresholds (100 train / 25 dev / 25 test) are minimum engineering gates, not a statistical sufficiency guarantee. Coverage and independent review remain mandatory.

## Current blockers

- **BLOCKED:** qualified Khmer annotators and independent adjudicator have not been recruited/confirmed.
- **BLOCKED:** item-level rights and per-entry provenance for candidate dictionaries are not verified.
- **BLOCKED:** MekongPhon dataset license, variety, and annotation methodology are unverified.
- **TODO:** inspect actual Khmer Acoustic Model dictionary and metadata under an exact commit.
- **TODO:** approve Phnom Penh convention sheet and freeze the 30-item pilot.
- **TODO:** complete a blind dry-run with one non-gold practice item.

## References

- Shurtz, Richardson & Richardson (2026), MekongPhon, LREC 2026: https://lrec.elra.info/lrec2026-main-129
- Chem et al. (2026), Khmer Acoustic Model and dictionary: https://github.com/chemvatho/Khmer-acoustic-model
- Chem (2020), The Standard Khmer vowel system: https://www.cjbar.rupp.edu.kh/index.php/cjbar/article/view/36
- Kirby (2014), Incipient tonogenesis in Phnom Penh Khmer: https://www.sciencedirect.com/science/article/pii/S0095447014000163


## External IPA resources — repository inspection, 2026-11-01

MekongPhon source repository: https://github.com/byu-matrix-lab/MekongPhon. Its README describes data/ as lexicons, OPUS downloads, sampled sentences and splits. pipeline/README.md describes SEAlang frequency lists → IPA scraping → minor lexicon post-processing → OPUS sentence download → lexicon train/eval split → trie-based lexicon lookup to convert sentences, filtering out-of-lexicon sentences. Therefore its sentence IPA is generated through a word-lexicon lookup pipeline and should not be presumed independent sentence-level phonetic transcription. The root LICENSE path was not present in the inspected repository. No dataset-specific redistribution license was verified. The LREC proceedings CC BY-NC-4.0 notice and the paper's “verified” description do not establish data reuse rights or item-level human adjudication. Do not import/redistribute until exact files, variety, IPA convention, correction/verification process, source terms, split construction and license are verified with the maintainers.

Separate candidate: https://github.com/chemvatho/Khmer-acoustic-model reports a 29,204-entry IPA dictionary and says dictionary data are CC BY-SA 4.0, distinct from the MIT code/model. Its README claims validation by native Khmer linguists, but per-entry source provenance, dialect/profile, transcription conventions and exact release must still be audited. Treat as an external comparator/source-discovery lead, not our gold.
