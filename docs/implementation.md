# Implementation

## Package

The package is khmer_ua, with a CLI entry point khmer-ua.

## Data flow

normalize.py performs Unicode NFC normalization.

parser.py performs conservative orthographic decomposition into consonants, coeng/subscripts, vowel signs and independent vowels.

phonology.py resolves structural register/inherent-vowel metadata without inventing IPA.

ipa.py applies pronunciation-profile transformations to already established IPA. It is intentionally not an orthography-to-IPA oracle.

practical.py maps IPA segments to the proposed Ukrainian practical layer and can expose selected Russian-compatible alternatives.

validator.py checks structural Unicode/coeng integrity.

## Determinism

The current implementation is deterministic and dependency-free. Linguistic uncertainty is represented as status/limitations rather than random or probabilistic output.

## API

    from khmer_ua import analyze, render_ipa_profile, map_sequence
    result = analyze("ខ្មែរ")
    ipa = render_ipa_profile("krɑː", "careful_standard")
    ua = map_sequence(["kʰ", "a"])

The example IPA is illustrative of the API and must not be read as a claim that the parser currently derives that IPA automatically.

## CLI

khmer-ua analyze TEXT
khmer-ua syllables TEXT
khmer-ua ipa TEXT
khmer-ua transliterate TEXT

At present the ipa command prints NOT ESTABLISHED when no IPA engine result exists. Other placeholder commands must not be presented as complete generators.
