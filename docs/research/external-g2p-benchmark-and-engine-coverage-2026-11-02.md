# External G2P benchmarks and engine coverage audit — 2026-11-02

## Scope and interpretation

This is a source-backed research audit, not a claim of accuracy for this repository. Results are comparable only when variety, orthographic normalization, IPA convention, syllable segmentation, test split, and scoring policy align. No external dataset is copied into project gold.

## Relevant benchmark evidence

### MekongPhon (LREC 2026)

Shurtz, Richardson & Richardson, “MekongPhon: A Large-Scale Parallel IPA Corpus for Lao and Khmer”, LREC 2026, pp. 1650–1658, DOI 10.63317/4bb9rvdshu4z.

The paper abstract reports 1.3 million Khmer orthographic–IPA pairs and a Transformer result below 2% character error rate on held-out test sets. It also reports linguistically informed Lao/Khmer tools outperforming Epitran by 6–71 CER points, trading some accuracy for speed. This is the strongest discovered external IPA-G2P benchmark for Khmer, but its variety, normalization, segmentation, and IPA conventions must be compared with the repository's Phnom Penh-oriented profile before transferring the score.

Reference: https://aclanthology.org/2026.lrec-1.129/

### Khmer G2P research benchmark (2019)\n\n“Applying Linguistic G2P Knowledge on a Statistical Grapheme-to-phoneme Conversion in Khmer” (Procedia Computer Science, 2019, DOI 10.1016/j.procs.2019.11.140) reports that adding linguistic vowel tags reduced PER from 23.2% to 11.1% and WER from 69.6% to 51.4% in its experiment. This is a direct language-specific benchmark showing the value of explicit linguistic structure. Its dataset, normalization, split, phone inventory and dialect must be recovered before comparing those numbers with modern engines or this repository.\n\nReference: https://www.sciencedirect.com/science/article/pii/S1877050919318502\n\n### Khmer G2P / NCKL Dictionary 2022-derived dataset

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
