# Architecture

unicode normalization
→ graphemes
→ orthographic syllables
→ register / inherent-vowel resolution
→ vowels / clusters / codas
→ Khmer phonology
→ context-sensitive rules
→ surface phonetics / IPA
→ features
→ Ukrainian target adapter
→ Ukrainian orthography

The implementation is data-driven. Linguistic data belongs under data/; Python orchestrates interpretation and validation.

Current foundation:
- Unicode normalization
- conservative orthographic segmentation
- consonant/register metadata
- coeng/subscript recognition
- independent/dependent vowel recognition
- evidence metadata
- CLI/API foundation
- negative tests

Not yet complete:
- full phonological rule engine
- complete IPA realization
- feature-distance ranking
- external Ukrainian inventory adapter
- empirical benchmark
