# Khmer linguistic completion register — 2026-11-01

**Baseline:** `main` `7b0a8f8c8661707afd9f0c58a94e2678789adf86`.
**Latest exact-main engineering evidence:** Quality checks [41424887161](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41424887161) and Pages/deployed smoke [41424887132](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41424887132) succeeded.
**Scope:** continue the existing master handoff; this register does not replace it.

## Evidence-based task ledger

| ID | Status | Work remaining | Acceptance |
|---|---|---|---|
| KHM-GOLD-001 | BLOCKED | No independent expert-adjudicated lexical IPA gold exists; `data/benchmark/gold.tsv` contains only its header. | At least two independent qualified Khmer phonetic annotators, adjudication, dialect/profile and IPA convention fixed, stable source/audio locators; frozen held-out split. |
| KHM-PHON-001 | PARTIAL | Complete context-dependent consonant-series × vowel × coda × syllable analysis and word segmentation. | Every supported combination backed by primary sources or adjudication, with shared Python/browser tests and explicit unsupported states. |
| KHM-RLOSS-001 | PARTIAL | Phnom Penh /r/-loss transformation remains profile-dependent and incompletely validated. | Define exact environment/dialect, test positive and negative minimal pairs against source-located expert labels; otherwise withhold. |
| KHM-ROM-001 | PARTIAL | BGN/PCGN 1972 inventories are bounded, but the @gmana ASCII simplifier is not fully conformant; contextual vowel/rime rules and Ukrainian syllable adapter remain incomplete. | Full primary-source context matrix, explicit deviations, independent syllable-level Ukrainian adapter, mixed-text and ambiguity tests. |
| KHM-G2P-001 | DONE_VERIFIED (diagnostic harness only) | Goruut has substantial partial coverage; Khmerphonemizer source concordance is not independent accuracy. | No production promotion absent gold and full source coverage; preserve raw outputs and comparator provenance. |
| KHM-UI-001 | TODO | Manual visual, keyboard, assistive-technology and mobile QA is not established by CI. | Recorded test matrix and deployed-site results. |
| KHM-REL-001 | PARTIAL | Production readiness blocked by lexical gold, contextual phonology and rights for external assets. | All release gates met; no restricted external model/data bundled. |

## Current diagnostic evidence

The latest recorded Goruut 100-row result is 97 outputs, 3 none; 70 complete, 27 partial, 3 unknown/no output; 96 stable, 1 unstable, 1 randomization-flagged input; strict source-attested concordance 6/100. Khmerphonemizer 0.0.3 returned 100 outputs and 100 comparable source labels after the comparator metadata-field correction; 18 strict and 19 limited-notation matches. These are not accuracy. The source IPA labels are generated/source-attested, not independently adjudicated gold. Independent gold remains 0; accuracy remains null.

## Execution order

1. Preserve fail-closed phonetic behavior; romanization must never be used as phonetic fallback.
2. Commission independently double-annotated Khmer lexical/audio IPA, with dialect, register, syllable and source metadata.
3. Complete the contextual orthography-to-IPA matrix, especially inherent vowels, consonant series, codas and syllable boundaries.
4. Validate the Phnom Penh /r/-loss profile separately from the core profile.
5. Finish PCGN contextual romanization and implement its independent Ukrainian syllable adapter.
6. Conduct deployed UI/accessibility QA and asset-rights review.

## External dependencies / blockers

- Qualified Khmer phonetic annotators and adjudicator.
- Permission/provenance for external corpus, dictionary, model and audio resources.
- No local checkout was available to this execution; exact-main GitHub Actions are the engineering evidence. Run documented local release commands in a clean checkout before release.

## Method constraints

Preserve `Khmer orthography → structural/register analysis → Khmer phonology → typed IPA → Ukrainian adaptation`. BGN/PCGN romanization is a separate orthographic route. Source-attested labels, engine agreement and structural fixtures are not gold.

## Open PR reconciliation

PR [#64](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/64) remains open and untouched. Current comparison against `main`: diverged, 7 commits ahead / 46 behind; changes replace the current stylesheet snapshot and add layout-contract tests coupled to that old CSS. The required responsive improvements already exist in focused merged work. Do not merge wholesale; revisit only after a fresh visual audit identifies a concrete missing behavior, then port a minimal change with current-browser tests.


## Independent IPA gold corpus implementation — 2026-11-01

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-GOLD-SCHEMA-001 | DONE_VERIFIED | Record, annotation, adjudication, split and license schemas plus cross-file validator |
| IPA-GOLD-DOUBLE-ANNOTATION-001 | PARTIAL | Two distinct annotators enforced; blind intake requires external controlled collection |
| IPA-GOLD-ADJUDICATION-001 | PARTIAL | Agreement/resolved/unresolved logic and feature-complete IPA comparison; no real adjudicated rows |
| IPA-GOLD-RIGHTS-001 | DONE_VERIFIED (mechanism) | Allowlisted licenses, required rights evidence and rejection of unregistered/non-redistributable licenses; source-by-source legal review still required |
| IPA-GOLD-SPLIT-001 | DONE_VERIFIED | Deterministic hash-based, frozen lexeme-group split and leakage checks |
| IPA-GOLD-EXPORT-001 | DONE_VERIFIED | Rights-filtered typed IPA export retaining source/license/evidence locators |
| IPA-TYPED-BENCHMARK-001 | DONE_VERIFIED | Different or missing IPA kind cannot count as an exact match |
| IPA-GOLD-RELEASE-GATE-001 | PARTIAL | Tag/manual workflow requires 100/25/25 adjudicated train/dev/test; owner must require the check in release rulesets/procedure |

**Current gold:** zero independent expert-adjudicated records; `gold.tsv` remains header-only; accuracy=null. The new schemas, fixtures and source-attested literature are not gold labels. No phonetic data was invented.


**Research evidence artifact:** [Khmer vowel × series × coda evidence matrix](KHMER-VOWEL-SERIES-CODA-EVIDENCE-MATRIX-2026-11-01.md). It records the specialist ɑ/ɔ-class mapping, Chem's four-speaker acoustic sample, coda-conditioned effects and explicit missing cross-product cells.


**2026-11-01 closeout:** PR [#103](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/103) is the comprehensive implementation and research-matrix change. PR CI passed 136 Python tests + 27 subtests, the browser register-shifter contract, web checks and Vite build. Main remains at c0a2b33. Gold remains 0; full contextual matrix and expert adjudication remain blocked.


**Expanded matrix status:** Ishida's full specialist phone-to-grapheme mapping table has been extracted into the Khmer matrix. The remaining gap is not missing orthographic mappings but independent lexical/acoustic coverage for every profile × series × stress × coda cell.


## 2026-11-01 final IPA-kind consistency verification

- Added fail-closed cross-annotation consistency: both independent annotations for one record must use the same `ipa.kind`, and a `RESOLVED` adjudicated result must preserve that kind. This prevents phonemic-vs-phonetic representation differences from being misclassified as pronunciation disagreements.
- Regression evidence: both new tests failed against the pre-fix validator on the test-only commit, then passed after the validator change.
- New task `IPA-GOLD-REPRESENTATION-KIND-001`: **DONE_VERIFIED** (mechanism and exact-head CI). Blindness, annotator qualifications and independent adjudicator competence remain external operational evidence, not properties CI can prove.
- Final PR head: `f7f2bf9a471f5fea990c0cf9509d382e3371d17b`; CI run [41338461515](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41338461515) SUCCESS — 139 Python tests + 27 subtests; browser register-shifter contract, web checks and Vite build passed.
- The Khmer matrix remains PARTIAL: full profile × series × stress × coda lexical coverage and an independent broader /r/-loss replication are not available.
- Gold remains zero; `gold.tsv` remains header-only; empirical accuracy remains null. No IPA labels were generated.


## IPA gold split-manifest runtime/schema parity — 2026-11-01

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| KHM-IPA-SPLIT-STRICT-001 | P1 | DONE_VERIFIED | RED test on commit `3fdfd9559dfc98c43c4c503b9e707f1632ebad07` failed as expected; GREEN code commit `64851a4572437d9185b47fcff56bde55e4f092c5`; exact-head CI [41340405233](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340405233) passed | The split generator and corpus validator share the closed split-field contract; unknown prior-manifest properties are rejected rather than silently dropped. No expert gold is created by this change. |


## Product-corpus license eligibility — 2026-11-01

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| KHM-IPA-LICENSE-ELIGIBILITY-001 | P1 | DONE_VERIFIED | RED tests on `83cfdc10716eff99f622f5d0e3c9c035bee3b56e`; GREEN code/schema commit `b3104d6815edb3950e13457f7e04bcb8f5f90145`; exact-head CI [41340930079](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340930079) passed | Registry and schema fail closed unless a redistributable product-corpus license explicitly permits commercial use and defines attribution/share-alike obligations. Human source-by-source rights review remains required. |


## Release-gate threshold validation — 2026-11-01

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| KHM-IPA-RELEASE-THRESHOLDS-001 | P1 | DONE_VERIFIED | RED test on `888ce85258e0c42b44e082e06023dbcd96401b96`; GREEN code commit `38aed74299c898461607407b730085e1b70d565d`; exact-head CI [41341743668](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41341743668) passed | All split minimums reject zero and negative values; threshold errors aggregate with other release-gate findings. Default minimums remain 100/25/25. |


## Audio-source review update — 2026-11-01

Two audio candidates are now documented in `docs/ipa-gold-collection-playbook.md`:

- Common Voice Scripted Speech v27.0 Khmer: locale `km`, catalogued CC0-1.0, 20.23 MB MP3 archive (https://commonvoice.allizom.org/en/datasets). Exact clip/speaker counts and regional metadata still require manifest inspection.
- OpenSLR 42 (SLR42): multi-speaker Khmer WAV plus transcript line index, CC BY-SA 4.0, with the currently listed archive containing male-speaker audio only (https://openslr.org/42). The provider says recordings are manually quality-checked but may still contain errors.

Neither provides IPA gold. Both are sentence-context sources; neither proves Phnom Penh citation-form coverage. Use them as supplementary audio only unless the exact speaker/profile metadata supports a narrower claim.

The Khmer Acoustic Model README claims 29,204 IPA entries and native-linguist validation, but the documented full dictionary path `dictionary/khmer_ipa.dict` returned 404 in the inspected default branch; only a six-row sample file was retrievable. Its sample uses space-separated symbol sequences, and the README does not specify a project-compatible typed IPA convention or item-level provenance. Keep it as an external comparator lead, not gold.

Status remains `KHM-GOLD-001 = BLOCKED`: no annotations, annotators or adjudications have been created. Independent gold remains 0 and accuracy remains null.


## Common Voice v27.0 manifest verified — 2026-11-01

The official release manifest `cv-corpus-27.0-2026-09-11.json` has been inspected (https://github.com/common-voice/cv-dataset/blob/main/datasets/scripted-speech/cv-corpus-27.0-2026-09-11.json). Khmer metadata: 739 clips, 213 validated clips, 15 contributor IDs, 0.28 validated hours (0.98 total). No named accent/variant category is supplied; gender metadata is entirely unspecified. Locale checksum in the manifest: `d1c4bb041744fefb1fa60397217b7cd79bfa2ade4510b11ff9863e9a0dc0392d`.

The dataset may be sufficient for a process pilot only if 30 required lexical contrasts occur in validated clips. It cannot establish Phnom Penh variety or speaker balance. OpenSLR42 remains an additional male-only contextual-audio source, not IPA gold. Controlled citation-form recordings and expert profile approval remain required. No data imported; `KHM-GOLD-001` remains `BLOCKED`, gold 0, accuracy null.


## Final exact-head verification — 2026-11-01

Branch `feat/ipa-gold-corpus-20261101-review`, source-audit content commit `9bb02272d9da77126ac80392e840228aef18d18f`. Khmer exact-head CI: Quality checks [41345111255](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345111255) SUCCESS; optional Goruut [41345111267](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345111267) SUCCESS; optional Khmer G2P [41345111293](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345111293) SUCCESS. Core job passed corpus structure validation, Python tests, Node web checks, and production site build.

These checks validate the committed repository and its automated engineering contracts. They do **not** validate the linguistic correctness of future human annotations, create gold labels, or change the release blocker. Gold remains empty and accuracy remains null.


## Follow-up handoff-head CI — 2026-11-01

The subsequent documentation-only handoff/register state at commit `1800ab775ade8e6c2ac1264c4318da69a07a53c1` was also checked on its exact head: Quality checks [41345362797](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345362797) SUCCESS; optional Goruut [41345362827](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345362827) SUCCESS; optional Khmer G2P [41345362791](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345362791) SUCCESS. These runs validate the updated documentation and existing automated checks, not future IPA annotations. Any later branch update must be checked again on its new exact head.


## Open-rights redistributability invariant — 2026-11-01

| Task | Status | Evidence / acceptance |
|---|---|---|
| KHM-IPA-RIGHTS-OPEN-001 | DONE_VERIFIED | A test-first regression rejected a source with `rights_status=OPEN` and `redistributable=false`; the runtime validator and record JSON Schema now both require `redistributable=true` for OPEN. Test-only RED commit: `8e328d06fb13130d878859ca2c297fb154fc0533`. Fix/schema code head: `e624dd59ce7ae1648cf72262e124764769fbc8a2`; exact-head CI run [41347973905](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41347973905) passed: 144 Python tests + 37 subtests; web checks and production build passed; optional Goruut and Khmer G2P smoke benchmark passed. |

This is a consistency/eligibility invariant, not a new legal determination. It does not change source licenses, rights evidence, gold labels or measured accuracy. Independent adjudicated gold remains 0; accuracy remains null.

## Exact current-head engineering checkpoint — 2026-11-01

- Current code checkpoint: `508ed94460e210ff9cc07cc0eaa7815246ee37b2`; exact-head core CI [41348224247](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41348224247) **SUCCESS**. 144 Python tests + 37 subtests; browser register-shifter contract, web checks and Vite production build passed. Optional Goruut KhmerCentral and Khmer G2P diagnostics passed.
- The `OPEN` / `redistributable` consistency regression is present in runtime validation, JSON Schema and tests.
- Independent expert gold remains 0 and accuracy remains null. Human annotation/profile/convention gates remain open; CI is not linguistic validation.

 
## Nested IPA record contract closure — 2026-11-01

| Task | Status | Evidence / acceptance |
|---|---|---|
| IPA-GOLD-NESTED-STRICT-001 | DONE_VERIFIED (engineering contract) | Test-first RED: [run 41352932018](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41352932018); GREEN exact-code-head CI: [run 41353055958](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41353055958). Runtime validator and JSON Schema both reject undeclared fields in `orthography`, `profile`, `source` and `source.rights_evidence`. 146 pytest tests + 44 subtests; web checks, register-shifter browser contract and production build passed. |

This closes only the nested-object shape contract. It does not establish the truth of source metadata, rights determinations, speaker profiles, IPA, or expert adjudication. Independent gold remains 0 and accuracy remains null.


## Validator duplicate-call cleanup — 2026-11-01

| Task | Status | Evidence / acceptance |
|---|---|---|
| IPA-GOLD-DUPLICATE-VALIDATION-001 | DONE_VERIFIED | Removed four consecutive duplicate `reject_unknown_properties` calls from nested `orthography`, `profile`, `source`, and `source.rights_evidence` validation. Code commit: `5c5e14d0458f9afd9c154e36975d86d882b67c0f`; Git blob SHA: `a072297e320b4b91a36c59fc90328b6ff98d2a5f`. - Core PR CI: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354247584 (SUCCESS); core push CI: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354242025 (SUCCESS); optional language diagnostics: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354247560, https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354247608 (SUCCESS). |

This is dead-code cleanup only: each contract check remains once; no validation rule, schema, IPA value, phonology rule, or corpus row changed. The shared validator remains identical across Lao, Khmer and Burmese. Hosted CI only; no local checkout or local test command is claimed. Independent expert-adjudicated gold remains 0 and empirical accuracy remains null.


## Methodology source refresh — 2026-11-02

| ID | Status | Evidence / acceptance |
|---|---|---|
| ENGINEERING-METHOD-REFRESH-001 | DONE_VERIFIED | Updated `AGENTS.md` and canonical handoff to pin Superpowers 7.0.1, mattpocock/skills current main, and Ponytail 5.3.3. Exact-head CI on methodology commit `bf506e2a34e3a2523678487fdc5148ab019bd493`: [PR Quality checks 41356374055](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41356374055) and [push Quality checks 41356369054](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41356369054) SUCCESS; 146 tests + 44 subtests; [Goruut 41356374057](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41356374057) and [Khmer G2P 41356374080](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41356374080) SUCCESS. No runtime dependencies or copied skill bundles were added. |



## Methodology source refresh follow-up — 2026-11-02

| ENGINEERING-METHOD-REFRESH-002 | DONE_VERIFIED | Updated `AGENTS.md` and canonical handoff to mattpocock/skills v1.3.2 (`d1478fcb140db0b93c0c8df17bcfd311844749d0`); added two-axis review, genuine-RED evidence, template/ownership, and safe worktree-cleanup guidance. Verified documentation checkpoint `73e654b5a592cb84ed29b25b03cb95fb5a7e25e0`: [Quality checks 41358627128](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41358627128) SUCCESS; optional [41358627194](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41358627194) and [41358627130](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41358627130) SUCCESS. | No third-party code, data, skill bundle, or runtime dependency copied. |

## IPA gold adjudication required-field parity — 2026-11-02

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| IPA-GOLD-ADJUDICATION-FINAL-IPA-001 | P1 | DONE_VERIFIED | A test-first regression demonstrated that an `UNRESOLVED` adjudication with the `final_ipa` property omitted was accepted by the Python runtime even though the JSON Schema requires the property (nullable). Test-only RED commit `df23f23c573c8311c7c721b02177b65b44117fd7`; failing exact-head PR CI [41407016954](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407016954). Runtime fix commit `dea7008094314b6a1ae88b1b4868e41552cdd54a`; exact-head PR CI [41407116467](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407116467) SUCCESS. 147 pytest tests + 44 subtests; web checks and production build passed. |

The validator now requires the `final_ipa` key to be present for every adjudication. `UNRESOLVED` must supply explicit JSON `null`; `AGREEMENT` and `RESOLVED` still require a typed IPA object. No phonology rules, corpus labels, source data or benchmark scores changed. Optional diagnostic runs: [41407116367](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407116367), [41407116301](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407116301). Gold remains 0 and empirical accuracy remains null.


### Unresolved adjudication explicit-null positive-path coverage — 2026-11-02

The regression suite now also proves the valid complementary case: `decision=UNRESOLVED` with an explicitly present `final_ipa: null` is accepted and remains excluded from adjudicated gold. Test commit `8111f28c34b7b3d7118d4f428178e4e90591c336`; exact-head PR CI [41407396214](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407396214) SUCCESS. 148 pytest tests + 44 subtests; web checks and production build passed. Optional diagnostics: [41407396207](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407396207), [41407396326](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407396326) SUCCESS. This does not create IPA labels or change the gold count (still 0) or accuracy (still null).

## External G2P engine coverage audit — 2026-11-02

- **PARTIAL (DONE_VERIFIED diagnostic execution):** Khmer phonemizer 0.0.3 returned 100/100 outputs on a 100-row MekongPhon sample, with 18 strict / 19 limited-normalized matches. Goruut source snapshot `b224bde` achieved 6/100 exact matches, 3 failures, 70 complete / 27 partial / 3 unknown coverage, and 27 unphonemized fragments. See `docs/research/external-g2p-benchmark-and-engine-coverage-2026-11-02.md` and Actions runs 41409092574 / 41409092578.
- **NOT SCORED:** these are source-attested diagnostic concordance counts, not independent gold or accuracy; independent expert-adjudicated IPA gold remains 0.
- **TODO:** investigate series × vowel × coda mismatches and the absent upstream Goruut `weights9.bin.zlib` asset; evaluate MekongPhon model and NCKL-derived Khmer respelling as separate IPA and syllabification baselines.


## Goruut language-bundle asset status correction — 2026-11-02

The previous TODO wording suggesting that this repository can simply recover or fix `weights9.bin.zlib` is superseded. Inspection of the exact upstream Goruut source tree at `b224bde02151f8f86d0fe260804e4ca743bda620` shows no `weights9.bin.zlib` in `dicts/lao/`, `dicts/khmer/central/`, or `dicts/burmese/`; the earlier `weights7` and `weights8` assets are present. This is an upstream language-bundle omission in the pinned snapshot, not a missing project-owned file. Status: **BLOCKED (upstream dependency)**. Acceptance: upstream publishes the asset or documents the expected model-tier fallback, and a controlled same-input comparison plus independent expert IPA gold establishes whether the asset changes relevant language coverage. Do not synthesize weights, download unpinned substitutes, or treat the warning as a failed workflow. See the external-engine research audit and canonical handoff for the evidence.


## Additional Khmer transformer and lexical baseline inventory — 2026-11-02

| ID | Priority | Status | Evidence / acceptance |
|---|---|---|---|
| KHM-MEKONGPHON-TRANSFORMER-001 | P1 | TODO | [`byumatrixlab/khmer-ipa`](https://huggingface.co/byumatrixlab/khmer-ipa) is a 33.6M-parameter BERT encoder–decoder trained from MekongPhon, with 128-token maximum input. Pin immutable revision/checksum, verify variety and IPA conventions, and compare on identical held-out lexical groups with series/register, vowel, length, coda, stress, /r/-loss and boundary diagnostics. Model output is not gold. |
| KHM-ACOUSTIC-LEXICON-001 | P2 | BLOCKED | README reports 29,204 IPA entries, but `dictionary/khmer_ipa.dict` returned GitHub API 404; only the six-entry `dictionary/khmer_ipa_sample.dict` was retrievable. No full lexicon coverage/notation audit can be performed from the sample. Acceptance: publish or expose the full dictionary at a stable inspectable path; then audit notation and orthographic coverage. This is a lexical/forced-alignment resource, not a G2P engine; alignment F1 is not IPA-generation accuracy. |


## Main publication reconciliation — 2026-11-02

Supersedes earlier handoff statements that the review branch was still ahead of `main` and unmerged: PR [#103](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/103) was merged into `main` as `b7e0171f77c08a15b0e55a9cb9fd83a001fff4f7`; this was the repository's current `main` tip at reconciliation. Exact-head engineering workflows on the PR head passed: Quality/tests [41414658963](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41414658963), Khmer G2P [41414658924](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41414658924), and Goruut [41414658926](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41414658926). The Pages workflow is configured to deploy from `main` and includes a deployed-site/runtime-asset smoke test. The public deployment result could not be independently inspected from this session, so deployment status remains **BLOCKED (external verification/network access)**, not claimed successful. No frontend source changes were included in this PR. Independent expert-adjudicated gold remains 0 and accuracy remains null; the project is still a research prototype.


## Current-main UI publication — 2026-11-02

The older design PR [#64](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/64) was not merged because its branch had diverged (7 commits ahead / 178 behind current `main`). Its responsive CSS and cache-busting intent were ported onto a fresh branch from the then-current `main`; PR [#105](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/105) was merged as `18ee0ae46cb98725c7f59c0436611fa50e4581bf`. The current-main CI [41424009124](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41424009124) passed the IPA gold-corpus structure validation, Python tests, JS web checks and Vite build. Added responsive layout contract tests for control wrapping, Ukrainian-result priority, narrow-phone status and coverage overflow. The Pages workflow is configured for pushes to `main`; actual deployment completion and public-site smoke-test result remain **BLOCKED (external verification/network/DNS unavailable in this session)**. This UI change improves presentation only and does not improve linguistic accuracy. Independent adjudicated gold remains 0; accuracy remains null; research-prototype status is unchanged.

### Pages smoke-test compatibility follow-up — 2026-11-02

The cache-busted stylesheet URL introduced by the UI polish exposed an overly strict CSS-link extractor in the deployed-site smoke test. Fixed in PR [#106](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/106), merge `7ee049aae9cc7ff571b21eabe18e962627f192a3`; the extractor now accepts an optional query string. PR CI passed (41424681328). The Pages workflow is now compatible with the deployed CSS URL. The post-merge Pages deployment and live-site smoke-test result are still **BLOCKED for independent verification** because external DNS/network access and a workflow-run listing endpoint were unavailable; do not infer deployment success from a merged PR or a successful pull-request CI run.


## Quality/profile review update — 2026-11-02

- Current main: `7b0a8f8c8661707afd9f0c58a94e2678789adf86`; exact-main Quality [41424887161](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41424887161) and Pages/deployed smoke [41424887132](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41424887132) SUCCESS.
- **KHM-PROFILE-001: DONE_VERIFIED (project decision):** select contemporary Phnom Penh Khmer, careful citation-form speech, project key `khmer-pph-careful-citation-v1`. This is a project-defined annotation profile, not an external standard.
- The selection is supported by the available Chem (2020) careful/formal-reading acoustic sample; colloquial /r/-loss evidence from Wayland & Guion (2005) and Kirby (2014) is kept separate and is not generalized to the chosen careful profile.
- **KHM-GOLD-001 remains BLOCKED:** gold=0, accuracy=null. Recruitment, IPA convention, blind intake, rights-cleared 30-item sample and adjudication remain external requirements.
- Phonology and Ukrainian adaptation remain PARTIAL; the profile decision does not create missing vowel × series × coda rules or gold.



## Engineering-method integration — 2026-11-02

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| ENG-METHODS-001 | DONE_VERIFIED (repository-context integration) | Added GLOSSARY.md, docs/agents/issue-tracker.md and docs/agents/codebase-map.md; linked them from AGENTS.md; refreshed exact upstream method pins. Exact-head CI before handoff closeout: [41468962341](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41468962341) SUCCESS. | Re-check these maps whenever entry points, data ownership or test commands change. This task does not establish linguistic accuracy or independent gold. |

The three references are used as methods, not runtime dependencies: Superpowers for explicit scoped execution and verification; Matt Pocock Skills for domain vocabulary, clear interfaces, source-backed research and two-axis review; Ponytail for real-flow mapping, minimal complete changes and residual-risk reporting. No production code or linguistic labels were changed by this task.


## Benchmark and corpus review — 2026-11-02

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| BENCH-REVIEW-001 | PARTIAL (existing diagnostic evidence reviewed) | Reviewed fixtures, corpus files, gold lifecycle files, benchmark harnesses and external raw-output reports. Exact-head engineering CI: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41469248955 SUCCESS. | Independent expert gold remains 0; resolve profile/convention, rights, held-out split and double-annotation/adjudication blockers before accuracy scoring. |

Comparator concordance is not accuracy. See the dated benchmark review in the canonical master handoff for language-specific results and acceptance criteria.


| BENCH-BYU-KHM-001 | PARTIAL | Inspected MekongPhon at `f80f6c1840c4818b51e05f2e00cded4701a5b662`: lexical split 7,940 train / 100 eval, 0 orthographic overlap; SEAlang `headley77` source path verified. BYU model card declares Apache-2.0 weights, while MekongPhon repository license metadata is null. NCKL-derived 38,629-row Khmer-script G2P lead is not IPA and has commercial-use terms to verify. | Pin exact model/tokenizer revisions and hashes; establish dataset/NCKL rights; confirm Phnom Penh careful-citation compatibility; run 100 lexical OOV cases as external diagnostics only; expert-adjudicate discrepancies. Not gold and not accuracy. |


**Clarification to BENCH-BYU-KHM-001:** the included `data/splits/khmer_train.csv` / `khmer_eval.csv` files are lexicon partitions, not demonstrated model-training manifests. MekongPhon `data/README.md` misdescribes the inspected files as OPUS sentence splits; `pipeline/convert_khmer.py` references different train/full-lexicon paths, and the split script's Khmer invocation is commented out. Exact checkpoint-to-split linkage is unverified. Keep the 100 items as a candidate diagnostic, not a validated model holdout.


## Upstream methodology pin reconciliation — 2026-11-02

| ID | Status | Evidence | Acceptance / limitation |
|---|---|---|---|
| ENG-METHOD-PIN-002 | DONE_VERIFIED (documentation provenance correction) | Corrected `AGENTS.md` and the canonical handoff to distinguish `mattpocock/skills` release v1.3.2 (`d1478fcb140db0b93c0c8df17bcfd311844749d0`) from the latest inspected `main` snapshot (`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`, 2026-10-31). The newer main commit adds the `software-factory` glossary/design skill; no unrelated factory workflow was imported. | Methodology metadata only. No runtime, linguistic rules, corpus, license grants or accuracy metrics changed. Recheck upstream pins when methodology sources are intentionally refreshed. |


## Late-session continuation audit — 2026-11-02

The canonical handoff records the exact PR/base comparison, review-thread state, hosted verification evidence and local-checkout network blocker for this continuation. No new phonological rules, IPA labels, gold records or license claims were introduced. The independent adjudicated IPA gold remains 0 and empirical accuracy remains null. The new handoff-only commit has triggered a fresh exact-head Quality checks workflow; do not treat the prior-head success as verification of the new commit. All expert annotation, source-rights, held-out split and manual accessibility acceptance criteria remain open.


## Public website verification — 2026-11-02

Khmer: DONE_VERIFIED — current-main Pages build/deploy smoke passed (run 41424887132); exact review-head engineering CI is running as 41531158714 at this checkpoint. PARTIAL — pure web-runtime and structural UI tests pass, but no browser-driven input/result assertion or post-deploy interaction test exists. IMPORTANT — selected single-profile runtime/UI correction is in open PR #107 and is not deployed on main yet. BLOCKED — direct live-site access from this runner failed at DNS resolution; this is not evidence of a site outage. TODO — add Chromium tests for visible IPA/UA results, unresolved-unit withholding, mode switching and clear, then add a post-deploy smoke and manual accessibility/mobile QA. See master handoff for evidence and acceptance criteria.

## Browser interaction verification — 2026-11-02

- **DONE_VERIFIED (code correction):** Removed a stale `source-result` DOM write from `src/main.js`. The element is intentionally absent from `index.html` (the source text remains in the input, not as a duplicate output card); the stale dereference would throw on every non-empty browser input before any results could render. The analysis/conversion implementation was restored byte-for-byte from the pre-change branch snapshot, with only this invalid DOM write removed.
- **PARTIAL:** Added pinned Playwright Chromium tests for `ក` → `/kɑː/` → `ка`, the known `ភាសាខ្មែរ` phrase, fail-closed mixed input, separate romanization mode and clear. Added a PR/push browser verification workflow and Pages browser gate. These tests have **not yet run** on this PR head; the workflow is newly introduced on the PR branch and must become active through the repository's normal workflow policy/merge before CI can report a result. Existing deterministic Quality checks passed on the preceding head, not on these new changes.
- **TODO:** obtain a successful exact-head browser workflow run; verify the published Pages deployment; record mobile, keyboard and assistive-technology QA. No linguistic accuracy claim is implied.
