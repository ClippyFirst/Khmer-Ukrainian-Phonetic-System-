# External phonetic corpus/source triage — Khmer — 2026-11-01

## Candidate: MekongPhon (LREC 2026)

**Disposition: high-priority research lead; NOT imported as gold or training data.** The paper reports 1.3 million Khmer orthography–IPA pairs and sub-2% CER on held-out data. These are paper-reported figures, not results independently reproduced by this repository.

- Paper: https://aclanthology.org/2026.lrec-1.129/
- Project: https://github.com/byu-matrix-lab/MekongPhon
- Inspected upstream main commit: `f80f6c1840c4818b51e05f2e00cded4701a5b662`.
- Files include `data/lexicons/khmer_lexicon.csv`, `data/splits/khmer_train.csv`, `data/splits/khmer_eval.csv`, and a 500-sentence qualitative sample.
- The project repository metadata has `license: null`; its tree has no LICENSE/COPYING file. The LREC proceedings page states CC BY-NC 4.0 for proceedings, but that does not automatically license the separate corpus, source lexicon, OPUS data or trained models.
- The documented pipeline scrapes the SEAlang Khmer dictionary (source filter `headley77`), downloads OPUS parallel text, and applies a greedy lexicon transliterator. Sentences with out-of-lexicon tokens are filtered out. Thus the sentence IPA is dictionary-generated, not an independently hand-transcribed sentence-level reference.
- The committed split script uses `random.seed(1234)` and reserves only 100 lexicon lines for evaluation. This is a held-out lexical split, not evidence of independent expert adjudication or robust dialect-balanced coverage.
- The paper's “verified” claim is worth investigating, but the accessible project README/pipeline does not document annotator identities, adjudication protocol, dialect stratification, or data licensing at the per-entry level.

## Candidate: Khmer Acoustic Model / Khmer IPA dictionary

- Repository: https://github.com/chemvatho/Khmer-acoustic-model
- Its README claims 29,204 IPA entries validated by native Khmer linguists; its data-license section says the pronunciation dictionary is CC BY-SA 4.0.
- However, `dictionary/README.md` separately declares CC BY 4.0 for the grapheme-to-phoneme mapping. These declarations conflict and need author clarification before redistribution or import.
- The current GitHub tree does **not** contain the full 29,204-entry `khmer_ipa.dict`; it contains only `dictionary/khmer_ipa_sample.dict` (six sample lines). The repository's model and dictionary claims therefore cannot yet be reproduced from the visible tree.
- The README also reports 137 hours of audio and alignment metrics, but alignment boundary metrics are not phonetic transcription accuracy metrics.

## Other candidate: Goruut

The source code is MIT, but the corresponding `neurlang/dataset/khmer/central/` lexicon has no declared repository license, and no per-language rights statement was found. Its derived model assets remain blocked pending provenance/license clarification. See `docs/audits/current/GORUUT-ASSET-LICENSE-REVIEW-2026-11-01.md`.

## Acceptance before use

1. Obtain explicit corpus/lexicon/model license terms and provenance for each component (SEAlang, OPUS corpora, dictionary data, derived IPA, model weights).
2. Obtain the MekongPhon paper and inspect annotation/verification protocol, Phnom Penh vs regional dialect profile, IPA conventions and held-out split design.
3. Resolve the Khmer Acoustic Model's CC BY 4.0 vs CC BY-SA 4.0 discrepancy and obtain the complete dictionary with a stable version/digest.
4. Establish whether the 100-word MekongPhon eval split is independently adjudicated; if not, keep it as a comparator split only.
5. Import no rows until each row has a stable source locator, profile, adjudication status and provenance; retain original IPA exactly.

Current independent, project-owned, expert-adjudicated Khmer gold remains 0. No MekongPhon/Goruut/Khmer-Acoustic-Model accuracy claim is added to this repository.


## Test-only Goruut runtime evaluation

Added an optional, test-only HTTP runtime probe for Goruut at pinned upstream commit `b224bde02151f8f86d0fe260804e4ca743bda620`. It explicitly enables `KhmerCentral` in `BuiltinDictLanguages`, builds the upstream Go binary and records raw JSON responses for source-attested lexical probes plus multiword/punctuation cases. `scripts/benchmark_goruut.py` records commit, language, input SHA-256, raw response, tokens and errors; it does not normalize or score IPA. Existing source-attested IPA remains non-gold. Accuracy=null; independent gold=0. Workflow: `.github/workflows/optional-goruut-runtime.yml`; artifact retention 30 days.

The earlier asset-license blocker applies to copying, redistribution and production integration. The owner has authorized use for testing only; therefore the optional CI probe may check out and execute the pinned upstream source transiently. It does not persist upstream assets, does not bundle them, and does not approve a production dependency. Linguistic gold and accuracy remain unestablished.


## Goruut runtime evidence update — 2026-11-01

The pinned Goruut runtime was executed with KhmerCentral enabled (Go 1.23.12). Engineering probes returned 8/8 responses; 6 source-attested IPA probes returned 6/6, but only 1/6 was an exact NFC/whitespace concordance (not accuracy/gold). Clear incomplete outputs: `ខ្មែរ` → `kʰr` vs source `kʰmae`; `ភ្នំពេញ` → `pʰɲ` vs `pʰnum ˈpɨɲ`; `ភាសាខ្មែរ` → `pʰiəsaːkʰr` vs `pʰiəsaː kʰmae`. Server log repeatedly reports missing `weights9.bin.zlib`. Do not promote. Full evidence: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.

Testing-only owner authorization was used to execute the pinned upstream source in ephemeral CI. No external asset was copied into the repository or production artifact. Full report: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.
