# External G2P benchmarks and engine coverage audit — 2026-11-02

## Scope and interpretation

This is a source-backed research audit, not a claim of accuracy for this repository. Results are comparable only when variety, orthographic normalization, IPA convention, syllable segmentation, test split, and scoring policy align. No external dataset is copied into project gold.

## Relevant benchmark evidence

### MekongPhon (Shurtz et al., 2026)

Shurtz, A., Richardson, C., & Richardson, S. D. (2026). “MekongPhon: A Large-Scale Parallel IPA Corpus for Lao and Khmer.” *Proceedings of LREC 2026*, 1650–1658. https://doi.org/10.63317/4bb9rvdshu4z.

The paper abstract reports 1.3 million Khmer orthographic–IPA pairs and a Transformer result below 2% character error rate on held-out test sets (Shurtz et al., 2026). It also reports linguistically informed Lao/Khmer tools outperforming Epitran by 6–71 CER points, trading some accuracy for speed. This is the strongest discovered external IPA-G2P benchmark for Khmer, but its variety, normalization, segmentation, and IPA conventions must be compared with the repository's Phnom Penh-oriented profile before transferring the score.

Reference: https://aclanthology.org/2026.lrec-1.129/

### Khmer G2P research benchmark — 2019

Sar, V., & Tan, T.-P. (2019). “Applying Linguistic G2P Knowledge on a Statistical Grapheme-to-phoneme Conversion in Khmer.” *Procedia Computer Science, 161*, 415–423. https://doi.org/10.1016/j.procs.2019.11.140. The prose reports 1,350 training pairs and 350 test pairs. However, the four test-corpus counts in Table 10 (112 + 97 + 98 + 49) sum to 356, not 350. The abstract reports baseline WER 69.6%, while Table 10 and the conclusion give 69.9%; the reported PER baseline is 23.2% in both places, and the proposed model's PER/WER are 11.1%/51.4%. These are two internal count/metric discrepancies. Preserve both reported values and do not choose one or reconstruct the evaluation set without author clarification or the exact data. The article is published under CC BY-NC-ND 4.0; that licence statement applies to the article and does not establish redistribution rights for the source dictionaries or derived pronunciation data. The experiment is a useful language-specific G2P comparator, but its dataset, normalization, split, phone inventory and dialect must be recovered before comparing its scores with modern engines or this repository (Sar & Tan, 2019).

Reference: https://www.sciencedirect.com/science/article/pii/S1877050919318502

### Khmer G2P / NCKL Dictionary 2022-derived dataset

The public `phonsobon/khmer-G2P` dataset reports 38,629 word-to-pronunciation pairs (37,755 unique words), split by word into train/validation/test. Pronunciation is Khmer-script respelling with syllable separators, not IPA. It preserves multiple accepted readings for some words and documents a standard/NCKL dictionary scope.

This is useful as a lexical pronunciation and syllabification resource, but it is **not** an IPA gold corpus and cannot validate exact phonetic output, contextual speech, or Ukrainian adaptation. It explicitly lacks many names, slang, new loanwords, and running-speech effects.

Reference: https://huggingface.co/datasets/phonsobon/khmer-G2P

## Engine coverage audit

| Engine | Declared Khmer support | What is established | Important gaps / cautions |
|---|---|---|---|
| Epitran | `khm-Khmr` | Package publishes a Khmer-script mapping. | This does not prove correct first/second consonant-series-conditioned vowels, inherent vowels, vowel length/quality, coda realization, register, /r/-loss, or lexical exceptions. Tone handling is not a substitute for Khmer register-conditioned vowel quality. |
| Goruut | Khmer Central | README lists a Central Khmer variety and advertises IPA output. | It does not document the repository's exact Phnom Penh profile or the full register/vowel/coda interactions. README says syllable tokens are not supported and tie bars are not supported. Generic five-level tone output does not establish Khmer register analysis. |
| MekongPhon models/tools | Khmer | Dedicated Khmer orthography–IPA resource and reported held-out CER benchmark. | Verify exact variety, transcription convention, tokenization, and model revision before adoption. |
| NCKL-derived Khmer G2P | Standard Khmer dictionary scope | 38,629 word-to-Khmer-pronunciation pairs, syllable boundaries, multiple readings. | Output is Khmer respelling, not IPA; dictionary scope, not unrestricted sentence pronunciation. |

Sources: https://pypi.org/project/epitran/ ; https://github.com/neurlang/goruut ; https://aclanthology.org/2026.lrec-1.129/ ; https://huggingface.co/datasets/phonsobon/khmer-G2P

## Feature coverage required by this project

A meaningful comparator must be evaluated on consonant series and coarticulation; dependent-vowel × series interactions; inherent vowel; vowel quality and length; coda and final-stop realization; register-conditioned vowel patterns; /r/ retention/loss by profile; silent/diacritic orthographic material; syllable boundaries; alternative lexical readings; and uncertainty. Segmental CER alone is insufficient: report vowel-feature and coda confusion, syllable-boundary F1, exact IPA match, and unsupported/error rate.

## Current assessment

- Epitran: useful baseline comparator; **PARTIAL**, not a source of gold.
- Goruut: useful second comparator; **PARTIAL**, with the documented absence of syllable tokens especially relevant to this pipeline.
- MekongPhon: **PRIORITY BENCHMARK / CANDIDATE BASELINE** for IPA-G2P.
- NCKL-derived Khmer G2P: **PRIORITY LEXICAL / SYLLABIFICATION REFERENCE**, not IPA gold.
- This repository: no empirical accuracy claim; adjudicated IPA gold remains governed by the existing blind collection protocol.

## Next reproducible experiment

1. Pin MekongPhon model and dataset revisions, checksums, source provenance, and exact inference commands.
2. Construct a held-out set by lexical group; preserve multiple valid readings as an explicit reference set.
3. Compare model outputs with Epitran and Goruut on identical normalized input.
4. Use NCKL respellings only for a separate syllabification/lexical-reading comparison; do not convert them mechanically into IPA.
5. Report segmental CER, vowel-feature error, coda error, syllable-boundary F1, exact IPA match, alternative-reading acceptance, unsupported/error rate, and runtime.
6. Obtain independent expert adjudication for all disputed IPA forms before changing project rules or gold.

## Evidence limitations

The MekongPhon abstract reports aggregate corpus size and CER but does not prove coverage of every Khmer series × vowel × coda × profile interaction required here. Vendor/project language support lists are not independent linguistic evaluations. No new runtime benchmark was executed in this documentation-only audit.

## Hosted raw-output diagnostics on the audit branch — 2026-11-02

Exact branch-head runs:
- Quality checks: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409092577 (job was still running at the first status check).
- Khmer phonemizer 0.0.3 diagnostic: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409092574 — SUCCESS as a raw-output benchmark. On 100 source-attested MekongPhon examples, engine version 0.0.3 returned 100/100 outputs. Strict string matches=18/100; limited notation-normalized matches=19/100. Independent gold=0; accuracy=null.
- Goruut source snapshot `b224bde` KhmerCentral raw-output probe: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409092578 — SUCCESS as raw-output collection. On the 100-row source-attested diagnostic, exact matches=6/100 (6%); notation-normalized matches=6/100; successful outputs=97, failed=3, complete source coverage=70, partial=27, unknown=3, and 27 unphonemized source fragments. The run logged missing `weights9.bin.zlib`; investigate before treating the runtime as stable.

All results remain `NOT_SCORED_NO_INDEPENDENT_GOLD`. The source-attested MekongPhon rows are not independent expert adjudication for this project's exact Phnom Penh profile. The 100-row concordance counts are diagnostic only and must not be called accuracy. They do show that declared language support is not enough to establish acceptable coverage or correct IPA output.


## Upstream Goruut asset inventory follow-up — 2026-11-02

The warning for `weights9.bin.zlib` was checked against the exact Goruut source snapshot used in the optional probes (`b224bde02151f8f86d0fe260804e4ca743bda620`). The upstream Git tree has no such file in the language-specific dictionary directories: `dicts/lao/`, `dicts/khmer/central/`, and `dicts/burmese/`. Each directory does contain earlier model assets (including the `weights7` and `weights8` files). The warning therefore reflects an asset absent from this pinned upstream snapshot, not a failed checkout of a file that exists in the repository. The probe still completed and returned raw outputs. The impact of this absent asset on ranking, coverage, or accuracy is not quantified; treat it as a model-bundle limitation and do not create substitute weights or infer a quality delta without upstream implementation evidence and a valid gold set.


## Additional Khmer transformer and lexical resources — 2026-11-02

### BYU MATRIX Lab Khmer-to-IPA checkpoint

The [`byumatrixlab/khmer-ipa`](https://huggingface.co/byumatrixlab/khmer-ipa) model card describes a 33.6M-parameter BERT encoder–decoder with separate character-level Khmer and IPA tokenizers, maximum sequence length 128, and best evaluation loss 0.1736 at checkpoint 26000 (approximately 11 epochs). The model card links its training code/data pipeline to MekongPhon. It is a priority neural G2P baseline alongside the existing `khmerphonemizer` smoke comparator, not an adjudicated reference. The card does not establish that its output convention, variety, treatment of consonant series/register, vowel length, diphthongs, coda, stress, /r/-loss, or long-input behaviour matches this project's target profile. Pin the model revision and checksum before a repeatable run; report raw output and feature-specific diagnostics, not only character error.

### Khmer acoustic-model pronunciation dictionary

[chemvatho/Khmer-acoustic-model](https://github.com/chemvatho/Khmer-acoustic-model) reports a 29,204-entry IPA pronunciation dictionary and a 137.01-hour speech corpus. This is a lexical-resource/forced-alignment asset, not a grapheme-to-phoneme engine. Its README reports phoneme-level alignment F1 0.360 and word-level alignment F1 0.120; these are alignment metrics, not IPA generation accuracy. The published inventory and sample dictionary require notation/profile review before use as a comparator: the README lists forms such as `-c`, `tɕh`, and parenthesized `(f)`, which need explicit interpretation rather than automatic normalization to project IPA. A next diagnostic may measure orthographic lexicon coverage and preserve dictionary IPA verbatim; it must not treat dictionary presence or forced-alignment scores as G2P correctness.

**Assessment:** Khmer neural checkpoint = PRIORITY BASELINE / NOT YET PROFILE-VERIFIED; acoustic-model dictionary = useful coverage resource / NOT A G2P ENGINE. Neither changes independent gold (0) or empirical accuracy (null).


### Full Khmer dictionary availability check — 2026-11-02

The README points to `dictionary/khmer_ipa.dict` and reports 29,204 entries, but fetching that exact path from the repository's `main` branch returned GitHub API 404. The only dictionary file successfully retrieved for inspection was `dictionary/khmer_ipa_sample.dict`, which contains six entries. Therefore the claimed 29,204-entry inventory remains an upstream README claim, not an independently inspected corpus in this audit. No lexicon coverage percentage can be calculated from the six-entry sample. **BLOCKED:** repeat the coverage/notation audit when the full dictionary is accessible at a stable repository path or another inspectable source.

## Follow-up research and execution — 2026-11-11

### Additional engine/resource findings

1. **BYU MATRIX MekongPhon Khmer IPA model** — [model card](https://huggingface.co/byumatrixlab/khmer-ipa). A 33.6M-parameter BERT encoder–decoder with separate character-level Khmer and IPA tokenizers. Model card license: Apache-2.0. The MekongPhon corpus repository snapshot has no declared root license, so the model license is not treated as permission to redistribute the corpus.
2. **MekongPhon rule-based baseline** — [rb_khm_to_ipa.py](https://github.com/byu-matrix-lab/MekongPhon/blob/f80f6c1840c4818b51e05f2e00cded4701a5b662/training/baselines/rb_khm_to_ipa.py). A separate experimental rule-based IPA baseline with consonant/register and vowel assignment logic. Not executed in this pass; upstream root license and convention scope need clarification.
3. **PhonSobon Khmer G2P** — [model](https://huggingface.co/phonsobon/khmer-g2p) and [dataset](https://huggingface.co/datasets/phonsobon/khmer-G2P). The 7.46M character Transformer produces NCKL Khmer-script respelling with syllable separators, not IPA. The model card reports 83.37% validation word accuracy at epoch 150; no test result is reported. The dataset has 38,629 pairs / 37,755 unique words, split 34,770 / 1,939 / 1,920. Dataset terms point back to NCKL Khmer Dictionary 2022 and require rights clarification before commercial use. It is an auxiliary respelling/syllabification resource, not an IPA benchmark.

### MekongPhon model execution

Historical one-time CI diagnostic [42997945391](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/42997945391), artifact [13844243674](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/42997945391/artifacts/13844243674), pinned model revision `20e069d384b240da76320e1569958568c12a54bc`, corpus commit `f80f6c1840c4818b51e05f2e00cded4701a5b662`.

| Measurement | Result |
|---|---:|
| Evaluation rows | 100 |
| Successful model outputs | 100 |
| Strict matches against `pron_no_tones` | 64 |
| Character edits | 80 |
| Reference code points | 638 |
| Source-attested codepoint CER | 12.539% |
| Independent project gold | 0 |
| Accuracy | null |

The same CI run executed Khmer Phonemizer 0.0.3 on the same source split: 100/100 outputs, 18 strict matches and 19 after limited notation normalization. Both are source-attested diagnostics only. The neural model's result does not reproduce the paper's abstract-level under-2% CER; the model checkpoint, test split and normalization used in the publication have not yet been reconciled with this 100-row `pron_no_tones` run. Do not compare the numbers as if they were the same benchmark.

### Evidence and acceptance boundary

- The model is **SMOKE_VERIFIED** in optional CI, not production-integrated.
- The artifact omits raw source rows/reference strings; it records the corpus hash, per-row reference hashes, raw predictions and runtime/model provenance.
- No source labels were promoted to independent gold; no accuracy is claimed.
- `pron_no_tones` does not test tone/phonation; a target-variety gold set and expert review are still required.
- PhonSobon dataset data are not copied or used in CI because commercial/redistribution rights are unresolved.

MekongPhon provenance qualifier: the paper reports 1,314,779 sentence pairs expanded by longest-match lexicon lookup over OPUS from an 8,026-entry seed lexicon; a 500-entry sample was reviewed by two proficient L2 speakers, not native target-variety annotators. Its under-2% CER is therefore a source-reported dictionary-seeded result, not independent sentence-level adjudication or this project's gold accuracy.

## Khmer acoustic-model lexicon: evidence blocker — 2026-11-11

The [Khmer-acoustic-model repository](https://github.com/chemvatho/Khmer-acoustic-model/tree/2714994b41ccf875c5b6f6182b48a72f13632dbf/dictionary) remains a potential IPA lexicon source, but it is **not currently an ingestible benchmark**:

- Root README advertises 29,204 IPA entries and says dictionary data are CC BY-SA 4.0.
- `dictionary/README.md` instead states 33,091 entries and CC BY 4.0.
- The inspected main-branch tree at commit `2714994b41ccf875c5b6f6182b48a72f13632dbf` contains only `dictionary/khmer_ipa_sample.dict` (144 bytes), not the advertised full dictionary. No release asset was found.
- The paper/model's MAE and F1 results evaluate forced alignment, not grapheme-to-phoneme conversion.

The registry now marks this source `BLOCKED_METADATA_AND_FULL_DICTIONARY_ABSENT`. Do not copy, benchmark, or redistribute it until the full file, entry count, provenance and authoritative data license are supplied.

The 100-row `khmer_eval.csv` file's exact membership relative to the downloaded checkpoint's training split has not been independently verified; this is an additional reason not to treat the run as an independent held-out accuracy estimate.
