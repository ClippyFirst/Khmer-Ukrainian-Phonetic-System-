## MekongPhon evidence review — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-MEKONGPHON-001 | PARTIAL (candidate secondary source; rights unresolved) | LREC 2026 paper and PDF; seed lexicon from historical dictionary IPA; two-author 500-entry sample review (97.2% Lao / 99.2% Khmer); sentence expansion by longest-match-first lookup over OPUS; repository snapshot f80f6c1840c4818b51e05f2e00cded4701a5b662 has no declared license/root LICENSE. | May be used for source-located lexical triage only after profile/convention checks. Not independent sentence-level gold; do not import into gold.tsv. Item-level source and derivative rights must be resolved before redistribution. |

## Post-merge provenance checkpoint — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-G2P-PROVENANCE-001 | DONE_VERIFIED (PR-head verified; post-merge push CI not independently surfaced) | PR [#129](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/129) merged as 2138f6f10df875591e846c81fae69c7cfde69bb5. Exact PR-head Quality [41726874329](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726874329), browser [41726874307](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726874307), optional G2P [41726874306](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726874306) all SUCCESS; artifact contents inspected. | Diagnostic report provenance and checksum integrity only; no language accuracy. Gold remains 0; accuracy null. |

## External diagnostic report provenance — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-G2P-PROVENANCE-001 | DONE_VERIFIED (diagnostic reproducibility only) | PR [#129](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/129), exact head 54c6a321c894468a7dd1625192a43f15fd806822; RED [41725130084](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725130084); Quality [41726222759](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726222759) SUCCESS (172 tests + 60 subtests); browser [41726222701](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726222701) SUCCESS; optional G2P [41726222858](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726222858) SUCCESS. Artifact inspected: JSON + .sha256 sidecar + source diagnostic; expires 2027-02-01. | Exact harness SHA-256, corpus hash, engine/version, Python/platform and GitHub event metadata are recorded; report integrity is independently checkable. No linguistic validation: independent adjudicated gold 0; accuracy null. |

## External diagnostic report provenance — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-G2P-PROVENANCE-001 | DONE_VERIFIED (diagnostic reproducibility only) | PR [#129](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/129), current head 0607f7d2ad2ed481f0b75dcd486a2dcaefa31c6c; test-first RED [41725130084](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725130084); exact-head Quality [41725569108](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725569108) SUCCESS (172 tests + 60 subtests), browser [41725569152](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725569152) SUCCESS, optional G2P [41725569100](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725569100) SUCCESS; artifact retained until 2027-02-01. | Report records harness SHA-256, corpus hash, engine/version, Python implementation/version, platform and CI source revision; JSON report has adjacent SHA-256 sidecar. This proves diagnostic provenance/integrity only, not language accuracy or gold agreement. Independent adjudicated gold remains 0; accuracy null. |

# Khmer linguistic completion register — 2026-11-01

**Benchmark implementation merge:** `0f73d006bfc05f6106a3b1e463c2cc7d6471ffae` (PR #123). **Handoff/register reconciliation merge:** `ebd8432b4abacecb50e30bae43ff64c42ac4063b` (PR #124).
**Latest post-merge exact-main evidence:** [engineering verification](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503253) SUCCESS; [built-site Chromium smoke](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503102) SUCCESS; [Pages/deployed-site smoke](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503262) SUCCESS.
**Open pull requests:** none at this checkpoint.
**Research boundary:** Independent expert-adjudicated Khmer IPA gold remains 0; `data/benchmark/gold.tsv` is header-only; empirical accuracy remains null.
**Scope:** continue the existing master handoff; this register does not replace it.

## Unicode/parser contract correction — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| UNICODE-TOKEN-BOUNDARY-001 | DONE_VERIFIED | PR [#126](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/126), merge `2a2f1c55282e076d6c4e0640d80af1053783bd6b`; exact-head Quality checks [41710399396](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41710399396) SUCCESS and browser smoke [41710399684](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41710399684) SUCCESS. | Browser punctuation segmentation now uses Unicode general category `P`, matching Python; regression covers U+3002 between two valid Khmer units and verifies exact source preservation plus neighbor status/output. This does not establish Khmer pronunciation or gold accuracy. |

**Research boundary unchanged:** no IPA gold labels were added; independent adjudicated gold remains 0 and empirical accuracy remains null.

## Held-out IPA benchmark integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| IPA-BENCH-HELDOUT-001 | DONE_VERIFIED | PR #123 merged as `0f73d006bfc05f6106a3b1e463c2cc7d6471ffae`; exact-main verification [workflow](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503253) SUCCESS; browser smoke [workflow](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503102) SUCCESS; Pages/deployed-site smoke [workflow](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503262) SUCCESS. Export preserves split bucket and frozen manifest seed/version; scoring defaults to held-out test; explicit all-split mode is marked diagnostic; malformed/mixed split metadata and empty predictions fail closed. | Engineering evaluation integrity only. Independent expert-adjudicated Khmer IPA gold remains 0; `data/benchmark/gold.tsv` is header-only; empirical accuracy remains null. No gold rows, IPA labels or accuracy claims were fabricated. |


## Engineering integrity continuation — 2026-11-03

- **TSV-INPUT-001 — DONE_VERIFIED:** benchmark TSV ingestion now rejects duplicate/blank headers and nonblank rows with extra or missing fields; blank physical lines are ignored. Regression cases cover gold/prediction duplicate headers, extra gold cells, and truncated prediction rows.
- **Evidence:** test-first RED [41665735912](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41665735912); focused implementation GREEN [41665873021](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41665873021); implementation commit `46e7eda242f134a792060c3002992bdea42bdb6c`.
- **Acceptance boundary:** input shape is validated before scoring. This does not create adjudicated IPA data or alter language accuracy status (gold 0; accuracy null).

## Strict JSON syntax — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSON-INPUT-003 | DONE_VERIFIED | Reject `NaN`, `Infinity`, and `-Infinity` in JSONL and license registry inputs. RED 41692662080; implementation CI 41694124825 SUCCESS (171 Python tests + 60 subtests; 3 browser smoke tests (run 41694138503)). | Reject non-standard JSON constants before corpus or rights validation; no linguistic labels or license terms changed. |

## License registry JSON integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSONL-INPUT-002 | DONE_VERIFIED | Duplicate top-level and nested keys in `licenses.json` rejected. RED 41690144835; implementation CI 41690306190 SUCCESS (169 Python tests + 54 subtests; 3 browser smoke tests (run 41690316616)). | Rights registry cannot silently apply last-key-wins semantics; no license permission is inferred or broadened. |

## JSONL input integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSONL-INPUT-001 | DONE_VERIFIED | Duplicate top-level and nested JSON object keys are rejected. RED 41687409282; exact implementation-head CI 41687730383 SUCCESS (167 Python tests + 54 subtests; 3 browser smoke tests). | Prevent silent last-key-wins corruption before corpus schema/provenance validation. No linguistic data or accuracy claims added. |

## Evidence-based task ledger

| ID | Status | Work remaining | Acceptance |
|---|---|---|---|
| KHM-GOLD-001 | BLOCKED | No independent expert-adjudicated lexical IPA gold exists; `data/benchmark/gold.tsv` contains only its header. | At least two independent qualified Khmer phonetic annotators, adjudication, dialect/profile and IPA convention fixed, stable source/audio locators; frozen held-out split. |
| KHM-PHON-001 | PARTIAL | Complete context-dependent consonant-series × vowel × coda × syllable analysis and word segmentation. | Every supported combination backed by primary sources or adjudication, with shared Python/browser tests and explicit unsupported states. |
| KHM-RLOSS-001 | PARTIAL | Phnom Penh /r/-loss transformation remains profile-dependent and incompletely validated. | Define exact environment/dialect, test positive and negative minimal pairs against source-located expert labels; otherwise withhold. |
| KHM-ROM-001 | PARTIAL | The Ukrainian target crosswalk now has candidates for all 22 consonant and 37 PCGN vowel/rime rows; the @gmana ASCII simplifier remains non-conformant and the runtime syllable adapter is absent. | Exact-head tests for the full target matrix; separately, full contextual PCGN engine and independent syllable-level adapter. |
| KHM-G2P-001 | DONE_VERIFIED (diagnostic harness only) | Goruut has substantial partial coverage; Khmerphonemizer source concordance is not independent accuracy. | No production promotion absent gold and full source coverage; preserve raw outputs and comparator provenance. |
| KHM-UI-001 | PARTIAL | PR #108 is merged; exact-main Chromium coverage, Pages deployment and deployed-site smoke all pass. Manual visual, keyboard, assistive-technology and mobile QA remain open. | Record human keyboard, screen-reader, responsive/mobile and visual results on the deployed site. |
| KHM-WEB-RESULT-RENDER-001 | DONE_VERIFIED | Removed the invalid `#source-result` dereference in PR #108; exact-main Quality [41641496598](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41641496598), Chromium [41641496582](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41641496582), and Pages/deployed smoke [41641496680](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41641496680) all succeeded. | Keep regression tests and Pages browser gate; manual accessibility QA remains tracked under KHM-UI-001. |
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


## Khmer production browser-output hotfix — 2026-11-03

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| KHM-WEB-RESULT-RENDER-001 | PARTIAL | On current `main` (`7b0a8f8c8661707afd9f0c58a94e2678789adf86`), `src/main.js` dereferences `#source-result` although `index.html` intentionally has no such element; every non-empty render therefore throws before result panels update. PR [#108](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/108) removes only this stale write and adds three Chromium tests. Exact pre-documentation head `aad9ce32378594c0da6651e7fba757ce0dfe40f0`: Quality checks [41533500652](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41533500652) SUCCESS; browser smoke [41533500956](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41533500956) SUCCESS, 3/3. | Fresh CI must pass on the documentation-updated PR head; merge #108; confirm Pages deployment; exercise non-empty input on the published URL and verify no uncaught browser errors. No production fix is claimed before merge/deploy. |

The automated regression verifies: (1) `ក` visibly renders IPA `/kɑː/` and Ukrainian `ка` with no uncaught page error; (2) mixed unsupported input remains visibly withheld; (3) clear returns to the empty state. This is UI engineering evidence only; it does not alter phonology, IPA labels, gold data, or linguistic accuracy. Independent adjudicated gold remains 0 and accuracy remains null.


## New source-level evidence — Phnom Penh Khmer profile and G2P comparators (2026-11-03)

| ID | Status | New evidence | Acceptance / limitation |
|---|---|---|---|
| KHM-PROFILE-SOURCE-001 | PARTIAL | Chem Vatho (2020), DOI [10.61945/cjbar.2020.2.2.3](https://doi.org/10.61945/cjbar.2020.2.2.3), one-page poster; 21 initially recruited, but acoustic results are from four Phnom Penh speakers (2 men, 2 women; 20–50), with reading tasks. F1/F2 and duration reported; normalization/method details and some measurements are internally unclear. | Supports limited vowel-profile context only. Not a representative dialect sample or evidence for consonants, tone, codas, or a complete G2P. Seek stronger multi-speaker primary studies. |
| KHM-PP-DIALECT-SOURCE-001 | PARTIAL | Sakamoto (1968), DOI [10.20495/tak.6.2_290](https://doi.org/10.20495/tak.6.2_290), principally one Phnom Penh informant; records style-sensitive weak syllable behavior and proposed ST/PP correspondences. | Treat as single-informant descriptive analysis; compare with modern multi-speaker evidence before generalizing. Keep the selected careful-citation profile explicit. |
| KHM-G2P-2019-EVIDENCE-001 | PARTIAL | Sar & Tan (2019), DOI [10.1016/j.procs.2019.11.140](https://doi.org/10.1016/j.procs.2019.11.140), reports PER 23.2% → 11.1% after vowel-tag features. | Comparator only until primary-paper split, profile, lexicon provenance, phoneme convention and rights are inspected. Published PER is not this repository's accuracy. |
| KHM-GOLD-PILOT-001 | BLOCKED | No gold labels or adjudications created by this source audit. | Requires profile-specific lexical sampling, frozen IPA convention, two independent qualified annotators, separate adjudicator, source locators and rights-cleared packets. Gold remains 0; accuracy null. |

No source in this audit licenses deterministic colloquial /r/-loss for the careful-citation profile. No IPA values or production phonology changed.


## Manifest-wide split identity — rebased integration — 2026-11-03

**Status: PARTIAL pending exact-head verification of the rebased port.** Ported PR #109's runtime validator/generator invariant and regression tests onto current `main` after the Khmer browser fix and handoff merges. The implementation must be verified on this clean branch before being marked DONE_VERIFIED.

- One frozen `(seed, version)` pair is enforced across the entire manifest; new groups inherit it; explicit conflicting/empty overrides fail; a new identity requires a separate empty input manifest.
- Original PR-head CI [41639679611](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41639679611) succeeded, but does not verify this rebased branch.
- No IPA gold rows were added; adjudicated gold remains 0 and empirical accuracy remains `null`.


## Khmer source evidence and benchmark reconciliation — 2026-11-03

**Status: PARTIAL pending exact-head verification of the clean port.** Ported the source-registry, references, research audit, collection playbook and provenance-test changes from PR #110 onto latest main, preserving PR #112's manifest-wide split protocol while adding the distinct agreement-metric boundary.

- Original PR-head Quality workflow [41640011541](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41640011541) succeeded; this clean port needs fresh exact-head checks.
- Dataset-item rights remain scoped only to those specific DataShare items. No IPA labels imported; independent gold remains 0 and accuracy remains `null`.


## KHM-PROFILE-001 — rebased single careful-citation profile — 2026-11-03

**Status: PARTIAL pending exact-head verification and specialist approval.** Reapplied the single-profile runtime/UI change to the latest main after source-citation integration. Only `khmer-pph-careful-citation-v1` is accepted; deterministic colloquial /r/-loss rewriting is removed.

- The profile is a bounded project decision, not a universal standard. Chem (2020) supports the careful formal-reading elicitation style but not full lexical coverage.
- Original #114 tests passed; the rebased branch needs fresh exact-head CI. Independent gold remains 0 and empirical accuracy remains `null`.


## KHM-AGENT-CONTEXT-001 — glossary and codebase navigation — 2026-11-03

**Status: PARTIAL pending exact-head CI.** Added `GLOSSARY.md`, `docs/agents/codebase-map.md`, `docs/agents/issue-tracker.md` and updated `AGENTS.md` with current code/data-flow and issue-management guidance.

- The map explicitly distinguishes the IPA-first phonetic path from the separate orthographic route and calls out high-risk seams, generated artifacts and fail-closed contracts.
- Documentation/process change only; no linguistic labels or code behavior changed. Independent gold remains 0; accuracy remains `null`.


## Continuation status sync — 2026-11-03

- Current main: `d8419d3099a8047d819a5a71cb5c4ef927db435e`; profile/runtime exact-main Quality 41646838970, Chromium 41646838756 and Pages/deployed smoke 41646838884 all succeeded. The later commit adds agent glossary/map documentation.
- PRs #107 and #114 were closed without merge because their profile/runtime/test changes are byte-identical to main; #108 and #111 were merged. Stale documentation PR #117 was closed after main advanced; this replacement branch is based on current main.
- Engineering improvements are verified; manual accessibility QA remains partial.
- IPA gold remains 0; empirical accuracy remains null. Annotation staffing, convention approval, rights clearance, blind intake and adjudication remain blocked on external human/evidence dependencies.


## KHM-METHOD-REFRESH-001 — methodology upstream snapshots — 2026-11-03

**Status: DONE_VERIFIED (reference audit).** Rechecked upstream default branches and release pins: Superpowers v7.0.1 at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`; mattpocock/skills release v1.3.2 at `d1478fcb140db0b93c0c8df17bcfd311844749d0` and current main snapshot `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`; Ponytail v5.3.3 at `7801d061243d7b753bad0e0b3c057cd250b11755`, with current main `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` adding only a README/product-list note after the method pin.

- These are methodology references, not runtime dependencies. No upstream skill files were copied into the application.
- Remaining linguistic evidence and rights gates are unchanged; gold 0, accuracy null.

## 2026-11-03 — held-out benchmark split enforcement

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-BENCH-SPLIT-001 | DONE_VERIFIED (engineering contract) | Export preserves the frozen group-safe split; scorer defaults to test and requires explicit selection for train/dev/all. Exact-head Quality [41651903776](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41651903776) SUCCESS on `ca53d628ae9a9ea4696fc85f42cdf59bcedfa2d1`. This fixes the evaluation boundary, not linguistic gold. |

Independent gold remains 0 and accuracy remains null. No data labels were fabricated. The split-aware benchmark documentation is in `docs/benchmarking-and-external-ipa.md`.

## Frozen split manifest provenance — 2026-11-03

The export and benchmark now preserve and validate the complete frozen split identity, not only the bucket name: `split`, `split_seed`, and `split_version`. Every adjudicated row must carry non-empty seed/version metadata, and the benchmark rejects a TSV that mixes manifest identities. The report exposes the manifest seed/version and selected scoring split. This makes the evaluated test partition traceable to one exact manifest; it does not create linguistic gold or change the current zero-row accuracy status.


## 2026-11-03 — empty benchmark prediction input

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-BENCH-EMPTY-PREDICTIONS-001 | DONE_VERIFIED (engineering guard) | Header-only prediction TSV previously exited 0 and produced an empty `engines` object. Test-first regression failed on all three language repositories; the scorer now rejects an empty prediction dataset after checking gold and frozen split provenance. Missing individual predictions within a named engine remain denominator-counted. RED: [41655188132](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41655188132). Final exact-head quality checks: [41655492141](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41655492141) SUCCESS; browser smoke: [41655491334](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41655491334) SUCCESS. |


## 2026-11-03 — benchmark identifier validation

| Task | Status | Evidence / acceptance |
|---|---|---|
| IPA-BENCH-IDENTIFIERS-001 | DONE_VERIFIED (engineering guard) | Reject whitespace-only gold IDs, prediction IDs and engine names while preserving non-empty identifiers exactly. Test-first RED: gold-ID run 41660794382; prediction-ID/engine run 41662096875. Final exact-code-head CI: 41662242906 SUCCESS (164 Python tests + 50 subtests; 3 browser smoke tests passed). Browser smoke 41662242611 SUCCESS. No linguistic labels or accuracy claims were added. |

## Verified continuation checkpoint — 2026-11-03 (late session)

- Default branch base: `dcaad206805abaacb2079f60e892e37af2477aac`; continuation branch: `docs/current-state-checkpoint-20261103`.
- Latest mainline work retained: Unicode punctuation token-boundary fix (#126; merged as 2a2f1c55282e076d6c4e0640d80af1053783bd6b) and subsequent docs/audit checkpoint.
- Exact-main CI on the recorded default-branch head: Quality 41710756134; browser smoke 41710756111; Pages deploy 41710756094; all listed runs completed with SUCCESS. These are CI checks for the current implementation and deployment, not phonetic validation.
- Open pull requests: none at checkpoint time. No upstream methodology repository was modified; Superpowers, Matt Pocock Skills and Ponytail remain process references only.
- Engineering task ledger: benchmark split provenance, empty-prediction rejection and whitespace-only identifier validation remain **DONE_VERIFIED** as input-integrity safeguards. The recently merged runtime fix is verified by its own regression/CI; no new linguistic rule is inferred from it.
- Linguistic task ledger: independent adjudicated IPA gold remains **0**; gold export remains header-only and empirical accuracy remains `null`. The profile-specific IPA convention, two independent annotators, separate adjudicator, curator/blind intake and item-level rights review remain **BLOCKED** on external human decisions/resources. No labels or source-derived pronunciations were fabricated.
- Manual deployed-site keyboard, screen-reader, responsive and mobile QA remains **TODO**; automated browser checks do not satisfy these acceptance criteria.
- Local test execution was not available in this connector-only session. Verification evidence is the linked GitHub Actions CI on the exact recorded main SHA; do not report local tests as run.


## Research unblock checkpoint — 2026-11-03

- Prospective language-specific expert/researcher leads and additional candidate resources are recorded in docs/ipa-gold-collection-playbook.md with primary-source links and explicit limits.
- These are leads only: no one has been contacted or recruited; no IPA convention has been approved; no rights have been granted; no IPA labels were generated.
- The 30-item pilot remains BLOCKED until the acceptance conditions in the playbook are met. Candidate lexicon entries, phonetic respellings, model outputs, orthographic transcripts and source descriptions are not gold IPA.
- The next external action is to contact a qualified prospective reviewer and request nominations for two independent annotators plus a separate adjudicator; separately complete item-level rights review and blind-intake dry run.


## Khmer acoustic-model dictionary follow-up — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-ACOUSTIC-DICT-001 | PARTIAL / BLOCKED for reuse | Current upstream root README says 29,204 dictionary entries and CC BY-SA 4.0; `dictionary/README.md` says 33,091 entries and CC BY 4.0 for its G2P mapping. Current public tree contains only a six-line sample dictionary and no full dictionary or release asset. | Request full versioned dictionary + SHA-256, artifact-specific license clarification, dialect/IPA convention, source provenance and independent annotation/adjudication details. No import, training, gold promotion or license inference until resolved. |


## Khmer audio-backed IPA pilot source — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-DDD-AUDIO-001 | PARTIAL (candidate audio source; pilot intake not yet approved) | Mozilla Data Collective Version 3 Part 1 reports 134.60h WAV + transcripts, 8 Cambodia-based native speakers (4F/4M), 13 topics/401 subtopics, origin-city metadata, CC BY-SA 4.0 and no-speaker-identification restriction. Source registered as `ddd-khmer-asr-cultural-v3-part1-2026`. | Verify exact speaker/profile/utterance metadata, select attested word spans with time locators, approve the target profile, review share-alike implications, then commission two blind IPA annotations plus separate adjudication. No IPA labels supplied; no gold import. |


## Post-merge checkpoint — DDD Khmer audio source (2026-11-04)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-DDD-AUDIO-001 | DONE_VERIFIED (source registry and evidence boundary); pilot use remains PARTIAL/BLOCKED | PR #135 merged as `ccd24f1f53dda8ccf19dbdbac0766ed4509f99e4`. PR-head Quality [41799786264](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799786264) and [41799802512](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799802512) SUCCESS; post-merge main Quality [41799887156](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887156), browser [41799887167](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887167), Pages [41799887180](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887180) SUCCESS. | Source record and restrictions verified. Still require profile review, word-span/time locators, CC BY-SA compatibility decision, two blind IPA annotators and adjudicator. No IPA gold added. |

## Post-merge checkpoint — Khmer acoustic dictionary discrepancy (2026-11-04)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-ACOUSTIC-DICT-001 | DONE_VERIFIED (discrepancy documented); reuse remains BLOCKED | PR #134 merged as `09640f83141127eeb5c9d201d96671d243d03019`; exact-head Quality [41799402432](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799402432) SUCCESS; post-merge main Quality [41799595059](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595059), browser [41799595047](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595047), Pages [41799595094](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595094) SUCCESS. | The conflicting 29,204/33,091 counts and CC BY-SA 4.0/CC BY 4.0 claims are recorded; full dictionary and author clarification still required. |


## Common Voice 27.0 Khmer audio source — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-CV27-AUDIO-001 | PARTIAL (secondary audio lead; profile screening required) | Mozilla provider record: CC0-1.0; 739 clips/0.98h total, 213 validated/0.28h, 15 speakers, 4,971 sentences (364 validated); 483 unresolved, 43 invalidated; accent values blank, gender unreported; no speaker identification or re-hosting/re-sharing. | Use provider-hosted validated clips only; approve target variety, select exact word-span/time locators, then double IPA annotate and adjudicate. No audio mirror or gold import. |


## Post-merge checkpoint — Khmer audio sources and corpus evidence (2026-11-04)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-ACOUSTIC-DICT-001 | DONE_VERIFIED (discrepancy documented); reuse remains BLOCKED | PR #134 merged `09640f83141127eeb5c9d201d96671d243d03019`; PR-head Quality [41799402432](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799402432), post-merge Quality [41799595059](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595059), browser [41799595047](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595047), Pages [41799595094](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595094) SUCCESS. | Conflicting counts 29,204/33,091 and CC BY-SA 4.0/CC BY 4.0; no full public dictionary. Reuse blocked pending exact artifact, checksum, rights and provenance. |
| KHMER-DDD-AUDIO-001 | DONE_VERIFIED (source registration); pilot use remains PARTIAL/BLOCKED | PR #135 merged `ccd24f1f53dda8ccf19dbdbac0766ed4509f99e4`; PR-head Quality [41799786264](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799786264), [41799802512](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799802512), post-merge Quality [41799887156](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887156), browser [41799887167](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887167), Pages [41799887180](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887180) SUCCESS. | 134.60h Part 1, 8 speakers, CC BY-SA 4.0; city metadata does not establish Phnom Penh. Word-span/time locators and share-alike review required. |
| KHMER-CV27-AUDIO-001 | DONE_VERIFIED (source registration and restrictions); pilot use remains PARTIAL/BLOCKED | PR #137 merged `98e66afecbce5528850e3a6906a8d9522385d3ed`; PR-head Quality [41800424004](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800424004) and [41800443113](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800443113), browser [41800443035](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800443035), post-merge Quality [41800575946](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800575946), browser [41800575935](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800575935), Pages [41800575937](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800575937) SUCCESS. | CC0-1.0 but no speaker identification or re-hosting/re-sharing; 739 clips/0.98h, only 213 validated/0.28h; 15 speakers, no accent/gender data. Not a standalone benchmark. |


## Language-specific IPA test fixtures — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-IPA-GOLD-FIXTURE-001 | DONE_VERIFIED | PR [#139](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/139) merged as `ed42f9ebfe617d1278949532ecd3d81fad652f7e`; exact-main Quality [41847860271](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41847860271), browser [41847860415](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41847860415), Pages/deployed-site smoke [41847860699](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41847860699) SUCCESS. | Test fixture now uses Khmer script and neutral test profile; regression asserts Khmer Unicode-block and matching profile metadata. This validates test-fixture integrity only, not phonological rules or IPA accuracy. Gold remains 0; accuracy null. |


## External Khmer pronunciation-source triage — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-EXT-IPA-DICT-001 | DONE_VERIFIED (source located and scoped; no import) | Pinned `open-dict-data/ipa-dict` commit `972cd67dd5f96bc5660e28070cde26e3928abcd7`; Khmer file `data/km.txt` (3,286 lines); upstream README attributes Khmer data to aakanee.com Khmer-English Dictionary and CC BY-NC-SA 4.0. Registered as `open-dict-ipa-km-2026`. | External comparator only. Profile, IPA convention and per-entry annotation provenance not established; non-commercial/share-alike restrictions must be reviewed. Not project gold. |
| KHMER-EXT-RESP-001 | DONE_VERIFIED (source located and classified; no import) | PhonSobon Khmer G2P: 38,629 word–pronunciation pairs / 37,755 unique words, split by word; pronunciation is Khmer-script respelling, not IPA. Combined pronunciation dictionary: 39,110 rows and 689 disputed items, including 39 LLM-assisted decisions that require native confirmation. Registered as `phonsobon-khmer-g2p-2026` and `phonsobon-khmer-pronunciation-2026`. | Candidate orthographic/syllabification comparator only; NCKL source rights and commercial/redistribution terms unresolved. No conversion to IPA by assumption. |
| KHMER-ACOUSTIC-DICT-RECHECK-001 | PARTIAL / BLOCKED | Upstream main commit `2714994b41ccf875c5b6f6182b48a72f13632dbf`: README claims 29,204 IPA entries and CC BY-SA 4.0; visible tree has only six sample lines; separate dictionary README says CC BY 4.0 for a 33,091-entry mapping. Registered as `chemvatho-khmer-acoustic-model-2026`. | Obtain full versioned dictionary + digest, reconcile artifact counts and licenses, confirm profile, provenance and annotation/adjudication method. No import. |

**Evidence boundary:** no external data were copied. These source-triage tasks are complete as research records, not as phonological gold. Independent expert-adjudicated Khmer IPA gold remains 0; empirical accuracy remains null.


## IPA gold release-gate profile consistency — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| IPA-GOLD-RELEASE-PROFILE-001 | DONE_VERIFIED (engineering guard) | Shared `scripts/ipa_gold_corpus.py` now rejects adjudicated corpora that mix target-profile identity (`id`, `variety`, `region`, `register`) or IPA kinds. New regression tests cover both failures. PR #141 merged as `4ba59abdc389a797c58216e4e155b8b06408c557`; exact PR-head CI [41870121484](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870121484) SUCCESS; exact PR-head browser smoke [41870121371](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870121371) SUCCESS; post-merge CI [41870545200](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870545200) SUCCESS; Pages [41870545069](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870545069) SUCCESS. | Does not prove profile approval, annotator qualifications, blindness, linguistic contrast coverage, or IPA accuracy. A specialist-reviewed language-specific coverage report remains required before benchmark readiness. |


## Expert recruitment lead revalidation — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-IPA-GOLD-RECRUITMENT-LEADS-001 | PARTIAL | The current UW profile verifies Nielson Hul's Khmer phonetics/voice-quality/sociophonetic research and public institutional email; University of Cologne 2026 profile verifies Vatho Chem's 2025 PhD in Phonetics focused on Central Khmer reduction and dialect fieldwork. Both are prospective reviewer leads only; Chem's relationship to his own acoustic-model resource must be disclosed and he must not be sole adjudicator of its data. | No candidate has been contacted, consented, recruited or approved. Close only after two independent qualified target-variety annotators, separate adjudicator, non-annotating curator, conflict checks, secure blind intake and written role/terms confirmation are documented. |

## Deterministic rule engine — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | PR #152 merged as `913e1b2a117022eb3350c3d1957680f0b5db0661`. Exact main Quality [43018004334](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43018004334), browser [43018004167](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43018004167), and Pages + asset smoke [43018004186](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43018004186) SUCCESS; live site: https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/. | Deterministic rule contract and publication verified. PROPOSED remains a proposal; expert-adjudicated Phnom Penh IPA gold is still required for correctness/accuracy claims. |

## Final deterministic-engine verification — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | Final main head `7585b49fdaac5480940d2511f48961f7690bf6b5`; exact-head Quality [43019207054](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43019207054), browser [43019207032](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43019207032), Pages + smoke [43019207026](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43019207026) SUCCESS. | Deterministic implementation and publication verified. Independent expert-adjudicated Phnom Penh IPA gold remains necessary for broader correctness/accuracy claims. |


## 2026-11-11 — Ukrainian practical adapter continuation

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Whole-IPA longest-match Python adapter integrated after Khmer IPA | DONE_VERIFIED | \`src/khmer_ua/practical.py\`, deterministic engine; quality CI 43094688835 |
| Shared browser adapter with actual yotation, /w/ and affricate tests | DONE_VERIFIED | \`src/ukrainian-practical.js\`, \`src/main.js\`, \`tests/web-engine.test.mjs\`; browser CI 43094688837 |
| Ukrainian target distinctions /h, ɦ/ → г, /ɡ/ → ґ, /x/ → х | DONE_VERIFIED | Policy v2026-11-11.3; note /ɡ/ → ґ is a project choice, while the 2026 standard generally uses г for foreign [g] |
| /w/ → в, syllable-initial /j/ yotation, affricates and /cʰ/ → ть' | DONE_VERIFIED | Machine-readable policy and regression tests |
| Linguistic accuracy of the proposed practical correspondences | PARTIAL | No independent adjudicated text gold set yet |
| Independent text-only Khmer IPA/Ukrainian gold set | BLOCKED | Requires sourced IPA entries, dialect/profile scope, independent annotation/adjudication and held-out evaluation |
| Audio corpus | DEFERRED | Not required for the current text-only scope |


## Practical adapter verification refresh — 2026-11-11

| Work item | Status | Evidence / acceptance |
|---|---|---|
| IPA → Ukrainian Python/browser mapping contract | DONE_VERIFIED (implementation) | Canonical policy v2026-11-11.3; whole-string longest-match adapter; fail-closed unknown IPA; h/g/x, affricates, aspiration, yotation and /w/ target distinctions |
| Expanded browser policy regression coverage | PARTIAL pending exact-head CI | `tests/web-engine.test.mjs` now exercises spaced IPA, h/g/x, affricates, untied consonant sequences, cʰ, yotation and unknown-segment withholding; exact-head Quality [43095329118](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43095329118) and browser [43095329245](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43095329245) are queued |
| Documentation consistency | DONE_VERIFIED | README, system page, implementation, validation and practical transcription specification aligned; /w/ → в corrected in summary table; sole active profile documented |
| Independent text-only Phnom Penh IPA/Ukrainian gold | BLOCKED | No independently sourced/adjudicated text labels available; acceptance requires a rights-cleared held-out text lexicon with dialect/profile scope, independent IPA annotation/adjudication and error/abstention report |
| Audio validation | DEFERRED | Not required for this text-only task |


## Provisional onset IPA fallback — 2026-11-11

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Python onset-only preview for unresolved Khmer units | PARTIAL | Separate provisional_ipa/provisional_ukrainian/fallback_status/fallback_trace; canonical ipa/ukrainian unchanged; regression for កា. Commit 352c22a55f526877dd136a982b2aa5ac03ff3838 |
| Browser onset-only preview | PARTIAL | Same onset IPA → existing adapter → ? behavior; per-unit PROVISIONAL status. Commit 862aa061726b2bae6296199e4b655334bb6f609a |
| Browser regression | PARTIAL | Source-contract assertions added; not yet an executable cross-runtime parity fixture. Commit 660915e4ed1f44eab04258957eee39537883aadd |
| Dedicated grapheme-position evidence registry | TODO | Register primary-source locator, profile, exact position, rule ID, scope and reviewer status for each provisional mapping |
| Exact-head CI and Chromium verification | BLOCKED pending run | Runs 43099931373 and 43099931284 were queued; neither is verified as passed |
| Full provisional vowel/subscript/coeng fallback | TODO | Only consonant onset hints are implemented; require independently sourced positional evidence before extending |


## Verification result — provisional onset preview, 2026-11-11

| Work item | Status | Evidence |
|---|---|---|
| Python fallback implementation and regression | DONE_VERIFIED (engineering behavior) | Exact code/test head dbdb8beafc3454e6bb0be848011f90fb0dea190b; Quality run 43101322383 PASS: 189 tests + 62 subtests |
| Browser preview wiring and source-contract checks | DONE_VERIFIED (engineering behavior) | Quality run 43101322383 web checks PASS; production build PASS |
| Browser visible-result smoke | DONE_VERIFIED | Chromium run 43101322537 PASS |
| Full positional evidence registry and language-wide fallback | TODO / PARTIAL | Current implementation is onset-only and keeps canonical output fail-closed; exact source locators and position-specific inventory still required |
| Functional Python/browser parity fixture | TODO | Current browser assertions are source-contract checks, not shared structured fixture parity |


## Unicode grapheme accounting sweep — 2026-11-12

| Work item | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-UNICODE-ACCOUNTING-001 | DONE_VERIFIED (structural/input accounting) | PR #157 merged as `e9c9d997e6de1029fd0b8fef9e7b6a9cb0020a4f`; exact-head Quality [43184648039](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43184648039) and browser smoke [43184647978](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43184647978) SUCCESS. Exhaustive sweep covers assigned Unicode L/M code points in U+1780–17FF and U+19E0–19FF. | Every tested code point is losslessly retained and traced. Malformed COENG remains visible as invalid structure. Does not imply phonological/IPA coverage or correctness. |
| KHMER-PHONOLOGY-100-001 | PARTIAL / BLOCKED by evidence | Existing vowel × series report remains first-order only; positional coda/profile cells and independent gold remain incomplete. | Requires source-located vowel × series × length × coda × profile evidence, independent expert adjudication, and held-out gold before expanding canonical IPA rules. |


## Khmer unmodelled-letter inventory and trace preservation — 2026-11-12

| Work item | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHMER-UNMODELLED-LETTERS-001 | DONE_VERIFIED (inventory classification only) | PR #159 merged as `d1d184334c806cd21cf2eb875a9c5151ab9e61b3`; exact-head Quality [43186170402](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43186170402) and browser smoke [43186170525](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43186170525) SUCCESS. U+17A3, U+17A4, U+179D, U+179E are explicitly registered as `unmodeled_letter`. | Explicitly accounted for, not pronounced. No IPA or Ukrainian value is assigned. |
| KHMER-TRACE-TAIL-001 | DONE_VERIFIED (source integrity) | Same PR and exact-head CI; regression `កxយ` preserves all graphemes after the unsupported `x`. | Unknown material no longer truncates the detailed parser trace. |


## BGN/PCGN Latin → Ukrainian target matrix — 2026-11-12

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHM-ROM-UA-TARGET-001 | DONE_VERIFIED | Branch `feat/khmer-romanization-ukrainian-matrix-completion-2026-11-12`; exact-head Quality [43221517618](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221517618) and browser smoke [43221517788](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221517788) both SUCCESS; push Quality [43221506380](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221506380) SUCCESS. The final Python suite reported 194 passed + 62 subtests. All 22 consonant and 37 vowel/rime target rows are populated and covered by tests. | Table coverage verified; project orthographic rendering only, not IPA or expert-approved national standard. Runtime adapter and contextual BGN/PCGN engine remain open. |
| KHM-ROM-UA-001 | TODO | No runtime Latin → Ukrainian adapter integrated. | Separate adapter consumes BGN/PCGN string, preserves source/Latin/UA trace and uncertainty, and does not call IPA adapter. |


## Khmer Ukrainian target matrix — post-merge evidence — 2026-11-12

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| KHM-ROM-UA-TARGET-001 | DONE_VERIFIED | Merged PR [#161](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/161), merge `6b0d0e75d794165e5eb935192fab0926e1efca39`; mainline Quality [43221967799](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221967799), browser [43221968144](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221968144), Pages [43221967939](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221967939) all SUCCESS. | 22 consonant + 37 vowel/rime target rows are covered. Runtime adapter and full contextual BGN/PCGN engine remain separate open tasks. |


## Khmer romanization Ukrainian runtime adapter — 2026-11-12

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| KHM-ROM-UA-TARGET-001 | DONE_VERIFIED | 22 consonant + 37 vowel/rime target rows; merged PR #161; prior exact-head matrix CI passed. | No remaining table-row blanks in the inventoried target matrix. |
| KHM-ROM-UA-001 | PARTIAL | PR #164 adds `src/khmer-romanization-ukrainian.js`, app integration, and browser regression `សុខា → Sokha → Сок'а`. Exact-head Quality [43226337969](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337969), browser [43226337956](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337956), push Quality [43226325685](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226325685) SUCCESS. | The current upstream ASCII romanizer drops BGN/PCGN diacritics; contextual vowel variants cannot be reconstructed. Need diacritic-preserving source output or a context-aware source-syllable romanizer before full-standard acceptance. |
| KHM-ROM-ENGINE-001 | PARTIAL | Upstream package documents its ASCII profile as BGN/PCGN-derived, with diacritics dropped and non-conformance. | Implement or adopt a validated, diacritic-preserving BGN/PCGN 1972 engine; test all contextual vowel, coda and shifter cases. |

The adapter is intentionally labelled `PROVISIONAL`. It is orthographic Latin-to-Ukrainian rendering, not IPA or pronunciation transcription.



## Khmer romanization runtime — mainline post-merge verification — 2026-11-12

- PR [#164](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/164) merged as `0ba6107a7e5cb09cca44021669a7401fc125eac4`.
- Mainline Quality [43227360792](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360792), browser smoke [43227360789](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360789), and Pages deployment [43227360801](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360801) all SUCCESS.
- The merged implementation remains deliberately PARTIAL/PROVISIONAL: the upstream ASCII romanizer omits PCGN diacritics; this adapter cannot reconstruct lost contextual vowel distinctions. The IPA route remains separate.
