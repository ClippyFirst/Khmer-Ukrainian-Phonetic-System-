## Engineering gate and corpus-coverage corrections — 2026-11-04

- The shared IPA corpus CLI previously emitted `release_ready: true` after checking only machine-verifiable corpus engineering conditions (adjudicated rows, frozen split minimums, one target-profile signature, one IPA kind and recorded redistributable source rights). It did not evaluate expert approval of the IPA convention, annotator/adjudicator qualifications, blind intake or expert-approved phonological contrast coverage.
- The success payload now reports `engineering_gate_passed: true` and `linguistic_release_readiness: "NOT_ASSESSED_BY_THIS_COMMAND"`. It lists six external acceptance gates not evaluated by this command: versioned expert-approved IPA convention; qualified independent annotators and separate adjudicator; controlled blind annotation/adjudication; expert-approved contrast coverage; independent corpus curator; and independent source-rights/license verification. It no longer emits `release_ready`.
- The engineering gate now separately requires at least **30 distinct adjudicated lexeme groups** by default, in addition to train/dev/test record minima. It reports both the number of distinct adjudicated groups and the configured minimum; repeated records within a single group cannot inflate the group-coverage count. Tests may lower the minimum explicitly for small synthetic fixtures.
- The tag/manual workflow is now named `IPA gold engineering-data gate`, and its minimum-count step explicitly says it is not linguistic release approval.
- Test-first evidence: regression-only commits produced expected Python-test failures on the old implementation (RED runs 41885520797, 41886236752, 41887115621). The final implementation on code-bearing commit `ea5b19cc50dc875c1ca7fdbef334a0ecd88f30f0` has exact-head hosted evidence: 41887446163 + 41887446069; additional push workflow: 41887436748. Exact-head Quality checks and browser smoke passed: Python tests, web checks, production build, and Chromium visible-results smoke.
- Updated `tests/test_ipa_gold_corpus.py` to assert the exact status, six unevaluated gates, absence of the old `release_ready` key, distinct lexeme-group minimums, and positive group minimum validation. No IPA labels, phonological rules, corpus rows, source permissions or generated pronunciation data changed.
- No local checkout or local test execution was available in this connector session; all verification evidence listed here is from hosted GitHub Actions.

## Post-merge handoff audit — 2026-11-04

- The base `main` SHA for this implementation branch was `ba6b90dee1acf00f7c89d3313d71270b713ecca2`. This is an immutable branch-base fact, not a claim that it remains the live `main` head after this implementation PR is merged.
- Previous documentation checkpoint PR #146 had exact head `7c6814fbc6fc26ae4a6479ab4b4edb1c9bac20d4`. Its diff was manually inspected; no CI status/workflow evidence surfaced for that PR head, so its CI remains **NOT VERIFIED**.
- The duplicate follow-up PR #147 was closed unmerged. The replacement implementation PR is #148; it includes the validator, regression tests, workflow-label correction, agent guidance and this handoff update. The branch's code-bearing implementation commit is `1a7474b287a9aa77b1d3ccbfd368d5afac1da15f`; GitHub PR metadata is the source of the eventual merge SHA.
- The exact-head workflow evidence and any still-running steps are recorded in the engineering-gate section above. This document intentionally records immutable branch-base history rather than a self-referential live-main SHA.
- Independent expert-adjudicated IPA gold remains 0; `data/benchmark/gold.tsv` remains header-only; empirical accuracy remains null. The profile confirmation does not substitute for expert convention approval, independent annotators/adjudicator, curator, blind intake, contrast coverage or independently verified source rights.

---


## Exact mainline checkpoint after methodology-gate adoption — 2026-11-04

- Verified `main` head: `a710984637c385797ea800ebd4bc6d7c9b9b5e6f`. The two methodology/completion-gate PRs for this repository are merged; there are no open PRs at this checkpoint. No implementation, linguistic registry, source record, benchmark label, or generated artifact was changed by those PRs.
- Exact-head CI status at checkpoint: Khmer Quality run 41877038265, browser run 41877038233, and Pages deployment run 41877038461 are QUEUED. These runs have not completed; do not record them as successful. Earlier green PR runs are not substitutes for this exact mainline head.
- GitHub branch metadata reports `main` as unprotected (no required status checks). This is a repository governance risk, not changed here; configuring branch protection or rulesets requires an owner decision and is outside this checkpoint.
- Independent expert-adjudicated IPA gold remains 0; `data/benchmark/gold.tsv` remains header-only; empirical accuracy remains null. KHM-GOLD-001 remains BLOCKED (independent adjudicated gold=0; gold.tsv header-only; target profile is already confirmed as contemporary Phnom Penh Khmer, careful citation-form speech (`khmer-pph-careful-citation-v1`); the versioned IPA convention sheet, two independent annotators, third adjudicator, curator, private blind intake and rights-cleared 30 lexeme groups remain required). KHM-PHON-001 and KHM-RLOSS-001 remain PARTIAL; KHM-UI-001 remains PARTIAL pending manual visual, keyboard, assistive-technology and mobile QA. DDD audio and MekongPhon remain candidate evidence only; external dictionary rights/counts remain unresolved.
- Methodology upstream refresh: Unlazy remains at `16671491f6679ad9378f52604d3bc2415b4120c7`; Matt Pocock skills at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`; Ponytail at `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`. Superpowers main has advanced to `22f0b463e7a5e579904dd6211a520321035526f7` (v7.0.2), one commit beyond the project's pinned v7.0.1 snapshot. Its delta is primarily harness/platform integration and skill-helper changes; no runtime dependency or unreviewed copy was imported. Keep the existing pinned reference reproducible unless a project-specific adoption is justified.
- Environment boundary: this checkpoint used GitHub's hosted repository/Actions APIs; no local checkout or local test execution was available. Do not claim local pytest/npm/Playwright results.
- Next actionable work: Continue source-located contextual phonology research and organize the controlled human IPA pilot; do not promote generated/source-attested G2P outputs or orthographic transcripts to gold.

---



## External reference evidence review — MekongPhon (2026-11-04)

- Reviewed the LREC 2026 paper, PDF methodology sections, public MekongPhon repository README/data/pipeline code, and the current repository snapshot.
- The seed lexicon is derived from historical dictionary IPA (Kerr 1972 for Lao; Headley 1977 for Khmer). The paper reports a two-author qualitative review of 500 seed entries: 97.2% Lao and 99.2% Khmer; the authors disclose that both reviewers are proficient second-language speakers, not native speakers.
- The sentence-level corpus is expanded by longest-match-first lexicon lookup over OPUS text, so it is not an independently transcribed sentence-level gold set. Its held-out evaluation is dictionary-seeded and must not be conflated with our blind adjudicated gold.
- The GitHub repository snapshot f80f6c1840c4818b51e05f2e00cded4701a5b662 declares no repository license and contains no root LICENSE. The paper's SEALang “Creative Commons open license” wording does not specify a license version. Rights remain UNKNOWN for redistribution/derivative use pending item-level verification.
- Disposition: retain as a candidate secondary lexical reference and optional external diagnostic; do not import into data/benchmark/records.jsonl or gold.tsv as independent gold. The existing human annotation/adjudication gate remains open.
- Primary evidence: https://aclanthology.org/2026.lrec-1.129.pdf; https://github.com/byu-matrix-lab/MekongPhon/tree/f80f6c1840c4818b51e05f2e00cded4701a5b662.
## Post-merge reconciliation — Khmer G2P diagnostic provenance (2026-11-03)

- PR [#129](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/129) is merged into main as **2138f6f10df875591e846c81fae69c7cfde69bb5**; this is the current mainline checkpoint for this change.
- Exact final PR-head checks on c4741aa4a70e228ea8a5b2af42a5657da0ed4629: Quality [41726874329](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726874329) SUCCESS (172 tests + 60 subtests), browser [41726874307](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726874307) SUCCESS, optional G2P [41726874306](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726874306) SUCCESS. The downloaded artifact contains the JSON report, .json.sha256 sidecar, and separate source diagnostic file; 90-day retention.
- The post-merge push-run result was not available through the connected workflow-run query at this checkpoint; no post-merge CI result is claimed. PR-head verification is the available evidence.
- Research boundary unchanged: independent adjudicated Khmer IPA gold remains 0; empirical accuracy remains null.

## Continuation update — external Khmer G2P report provenance and integrity (2026-11-03)

- **KHMER-G2P-PROVENANCE-001 — DONE_VERIFIED (diagnostic reproducibility only):** scripts/benchmark_g2p.py now embeds an inspectable provenance block with exact harness SHA-256, corpus path/hash, engine name/version, Python version/implementation, platform, and clearly named GitHub event SHA/ref/head-ref fields. It writes an adjacent .json.sha256 sidecar and creates parent directories.
- **Test-first evidence:** regression test added first; expected RED [41725130084](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725130084). Transient integration defects (main output not yet routed through checksum writer; then literal escaped newline) were exposed by CI and corrected.
- **Final exact PR-head verification:** head 54c6a321c894468a7dd1625192a43f15fd806822; Quality [41726222759](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726222759) SUCCESS (172 tests + 60 subtests); browser [41726222701](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726222701) SUCCESS; optional Khmer G2P [41726222858](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41726222858) SUCCESS. Downloaded artifact was inspected and contains the JSON report, its SHA-256 sidecar, and the separate source diagnostic file; 90-day retention expires 2027-02-01.
- **Research boundary:** integrity/reproducibility only. Source-attested IPA remains non-gold; independent adjudicated Khmer IPA gold remains 0 and empirical accuracy remains null. No pronunciation rules, source labels, or accuracy values changed.
- **PR:** [#129](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/129), branch head 54c6a321c894468a7dd1625192a43f15fd806822.

## Continuation update — external Khmer G2P report provenance and integrity (2026-11-03)

- **KHMER-G2P-PROVENANCE-001 — DONE_VERIFIED (diagnostic reproducibility only):** scripts/benchmark_g2p.py now embeds an inspectable provenance block with the exact harness SHA-256, corpus path/hash, external engine name/version, Python version/implementation, platform, and GitHub source revision when running in Actions. The report writer emits an adjacent .json.sha256 digest sidecar and creates parent directories.
- **Test-first evidence:** regression test added first; expected RED on [41725130084](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725130084). A transient integration failure [41725258719](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725258719) exposed that the main path had not yet routed output through the checksum writer; fixed before final verification.
- **Exact implementation-head verification:** Quality [41725569108](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725569108) SUCCESS (172 tests + 60 subtests); browser smoke [41725569152](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725569152) SUCCESS; optional Khmer G2P run [41725569100](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41725569100) SUCCESS. Artifact khmer-phonemizer-raw-output is present and retained until 2027-02-01.
- **Research boundary:** report integrity and reproducibility only. Source-attested IPA remains non-gold; independent adjudicated Khmer IPA gold remains 0 and empirical accuracy remains null. No phonological rules, source labels, or accuracy values changed.
- **PR:** [#129](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/129), branch head 0607f7d2ad2ed481f0b75dcd486a2dcaefa31c6c; pending review/merge at this checkpoint.

## Continuation update — Unicode punctuation token boundaries (2026-11-03)

- **UNICODE-TOKEN-BOUNDARY-001 — DONE_VERIFIED:** browser tokenization now recognizes the Unicode general category `Punctuation`, matching Python's `unicodedata.category(...).startswith("P")` separator contract. Previously, the browser used a hand-maintained punctuation allowlist; punctuation outside it (for example U+3002 IDEOGRAPHIC FULL STOP) could be absorbed into a neighboring Khmer token and incorrectly mark that unit unsupported.
- **Regression:** `tests/web-runtime.test.mjs` exercises `ក។គ`; it checks exact source reconstruction, three distinct units, punctuation status, and that both Khmer neighbors retain their existing IPA/Ukrainian results.
- **PR:** [#126](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/126), squash-merged as `2a2f1c55282e076d6c4e0640d80af1053783bd6b`.
- **Verification on exact PR head `ec38f92efa0a59dd0d887e436a7194ded23c4e23`:** Quality checks [41710399396](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41710399396) SUCCESS; browser smoke [41710399684](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41710399684) SUCCESS. Deterministic web checks and production build also passed in the browser workflow.
- **Scope boundary:** this is a tokenizer parity/source-boundary fix, not a Khmer phonology rule, IPA convention decision, gold-corpus addition, or accuracy result. Independent adjudicated Khmer IPA gold remains 0; empirical accuracy remains null.

# Master execution plan and chat handoff

## Verified mainline checkpoint — Khmer external audio and dictionary research (2026-11-04)

- Current main before this documentation checkpoint: `98e66afecbce5528850e3a6906a8d9522385d3ed`. No open PRs; open human research issue #104 remains.
- PR #134 documented the Khmer Acoustic Model's unreconciled 29,204 vs 33,091 dictionary counts, CC BY-SA 4.0 vs CC BY 4.0 data-license statements, and missing full dictionary in the public tree. Exact-head and post-merge Quality, browser and Pages checks all SUCCESS (runs 41799402432, 41799595059, 41799595047, 41799595094).
- PR #135 registered DDD Khmer ASR Cultural Dataset v3 Part 1: 134.60h, 8 speakers, 13 topics/401 subtopics, CC BY-SA 4.0. PR-head Quality and post-merge Quality/browser/Pages all SUCCESS (41799786264, 41799802512, 41799887156, 41799887167, 41799887180). Use only after profile and share-alike review; city metadata does not establish Phnom Penh.
- PR #137 registered Common Voice 27.0 Khmer: 739 clips/0.98h, 213 validated/0.28h, 15 speakers, 364 validated sentences, accent/gender unreported. CC0-1.0 but no speaker identification or re-hosting/re-sharing. PR-head Quality [41800443113](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800443113), browser [41800443035](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800443035), post-merge Quality [41800575946](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800575946), browser [41800575935](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800575935), Pages [41800575937](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41800575937) SUCCESS.
- Neither audio corpus supplies IPA. Use provider-hosted clips only, no speaker identification/re-hosting, exact word-span/time locators, profile screening, two blind annotations and third-person adjudication. Independent gold remains 0; accuracy remains null. Issue #104 remains blocked on human convention/recruitment/intake and item-level rights/profile review.


## Khmer Common Voice 27 audio checkpoint — 2026-11-04

- Added source `mozilla-common-voice-khmer-27-2026` to `data/khmer/sources.json`: https://mozilladatacollective.com/datasets/cmu5olr5u00xzmh07pfgl3kuw.
- The provider declares CC0-1.0 but prohibits speaker identification and re-hosting/re-sharing. The release contains 739 clips / 0.98h total, 213 validated / 0.28h, 15 speakers and 4,971 sentences (364 validated); 483 unresolved and 43 invalidated. Accent is blank for the disclosed subset; gender is unreported.
- **KHMER-CV27-AUDIO-001 — PARTIAL.** Candidate secondary audio only. Do not infer Phnom Penh/Standard Khmer from locale; use only validated provider-hosted clips, no mirroring, and retain exact word-span/time locators. Blind IPA double annotation and adjudication remain mandatory.
- Keep this separate from DDD's CC BY-SA 4.0 corpus. Neither dataset supplies IPA. Gold remains 0; accuracy remains null.



## Verified mainline checkpoint — Khmer external-source research (2026-11-04)

- Current main: `ccd24f1f53dda8ccf19dbdbac0766ed4509f99e4` (PR #135). No open PRs at checkpoint.
- PR #134 merged as `09640f83141127eeb5c9d201d96671d243d03019`: recorded the Khmer acoustic-model dictionary's conflicting counts (29,204 vs 33,091), conflicting data-license declarations (CC BY-SA 4.0 vs CC BY 4.0), and absence of a full dictionary/release asset in the visible upstream tree. Exact-head Quality [41799402432](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799402432) and post-merge Quality [41799595059](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595059), browser [41799595047](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595047), Pages [41799595094](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799595094) SUCCESS.
- PR #135 merged as `ccd24f1f53dda8ccf19dbdbac0766ed4509f99e4`: registered DDD Khmer ASR Cultural Dataset v3 Part 1 as a candidate audio source, explicitly not IPA gold. PR-head Quality [41799786264](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799786264) and [41799802512](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799802512) SUCCESS; post-merge Quality [41799887156](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887156), browser [41799887167](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887167), Pages [41799887180](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41799887180) SUCCESS.
- Research boundary: DDD provides audio + orthographic transcripts; the 8 speakers and city metadata do not independently establish Phnom Penh phonology. CC BY-SA obligations and exact word-span/time locators remain to be reviewed before pilot use. The Khmer acoustic dictionary remains blocked for reuse. Independent adjudicated IPA gold remains 0; accuracy remains null.


## Khmer audio-backed pilot lead — 2026-11-04

- Added source `ddd-khmer-asr-cultural-v3-part1-2026` to `data/khmer/sources.json`. The provider listing for Version 3 Part 1 reports 134.60 hours, 8 Cambodia-based native speakers (4F/4M), 13 topics, 401 subtopics, origin-city metadata, CC BY-SA 4.0, attribution requirement and a prohibition on speaker identification.
- **KHMER-DDD-AUDIO-001 — PARTIAL.** This is a useful audio+orthographic-transcript candidate for a specialist-run pilot, not IPA gold. City metadata alone does not prove Phnom Penh speech; sentence recordings require explicit word-span/time locators; share-alike obligations need review before publishing derived IPA.
- Keep Version 3 Part 1's 134.60h/8-speaker figures separate from the broader HF card's 727.94h/12-speaker aggregate until provider manifests reconcile them. No speaker identification, audio mirroring or IPA labels are added.
- Acceptance: approve profile and licensing path, curate exact word spans, complete blind double annotation and third-person adjudication. Gold remains 0; accuracy remains null.



## Khmer external dictionary evidence checkpoint — 2026-11-04

- Rechecked `chemvatho/Khmer-acoustic-model` directly. Root README claims 29,204 IPA dictionary entries under CC BY-SA 4.0; `dictionary/README.md` describes a 33,091-entry G2P mapping under CC BY 4.0. The public Git tree currently contains only a six-line sample dictionary and no release asset with the complete data.
- **KHMER-ACOUSTIC-DICT-001 — PARTIAL / BLOCKED for reuse.** The counts and artifact-specific licenses are unreconciled; a full inspectable dictionary and per-entry provenance are unavailable in the public tree. Do not infer data rights from the MIT code license, and do not treat alignment metrics as IPA accuracy.
- Acceptance: obtain a versioned full dictionary and digest, explicit license for each artifact, target dialect and IPA convention, source provenance, and documented annotator/adjudication protocol. Until then, this remains a research lead only; no IPA gold or accuracy claim is added.

 — Khmer → Ukrainian

## Continuation update — strict JSON constants (2026-11-03)

- **JSON-INPUT-003 — DONE_VERIFIED:** JSONL corpus records and the license registry now reject JavaScript-only constants `NaN`, `Infinity`, and `-Infinity` through the JSON decoder's `parse_constant` hook. Diagnostics retain file and line context.
- **Regression coverage:** invalid constants in a corpus JSONL row and in `licenses.json`.
- **Test-first RED:** [41692662080](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41692662080) — exactly the two new regression tests failed before the parser change.
- **Implementation-head CI:** [41694124825](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41694124825) SUCCESS — 171 Python tests + 60 subtests; 3 browser smoke tests (run 41694138503).
- **Scope boundary:** this enforces RFC-compliant JSON syntax only; no corpus labels, license permissions, or gold records were changed.

## Continuation update — duplicate JSON keys in license registry (2026-11-03)

- **JSONL-INPUT-002 — DONE_VERIFIED:** the standalone `data/benchmark/licenses.json` registry is now parsed with the same duplicate-key rejection as JSONL corpus files. Duplicate top-level `licenses` and nested `redistributable` keys fail with path-qualified diagnostics; this prevents last-key-wins ambiguity in redistribution decisions.
- **Regression coverage:** duplicate top-level and nested license-registry JSON keys. Test-first RED: [41690144835](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41690144835); exact implementation-head CI: [41690306190](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41690306190) SUCCESS — 169 Python tests + 54 subtests; 3 browser smoke tests (run 41690316616).
- **Scope boundary:** no license grant is inferred or changed, and no source records or IPA labels are added. Existing rights evidence requirements remain in force.

## Continuation update — duplicate JSON object-key rejection (2026-11-03)

- **JSONL-INPUT-001 — DONE_VERIFIED:** `scripts/ipa_gold_corpus.py` now rejects duplicate JSON object member names at every nesting level. The parser reports the source path and line number instead of allowing Python's default decoder to silently retain only the last value.
- **Regression coverage:** duplicate top-level `record_id` and nested `orthography.text` keys, using otherwise valid corpus records.
- **Test-first RED:** 41687409282.
- **Exact implementation-head verification:** 41687730383 SUCCESS — 167 Python tests + 54 subtests; 3 browser smoke tests.
- **Scope boundary:** this protects annotation/provenance/profile/split input integrity; no linguistic labels, source data, schemas, or gold rows were added or changed. Independent adjudicated gold remains 0; empirical accuracy remains null.

## Continuation update — strict benchmark TSV validation (2026-11-03)

- **Implementation commit:** `46e7eda242f134a792060c3002992bdea42bdb6c` on `fix/heldout-ipa-benchmark-20261103` (PR #123; subsequent documentation commits follow it).
- **DONE_VERIFIED (input integrity):** `read_tsv()` now rejects duplicate column names, blank header names, and nonblank rows with missing or extra fields. Physically blank lines remain ignored; values are not silently padded, truncated, or rewritten.
- **Regression coverage:** duplicate gold and prediction headers, extra gold fields, and short prediction rows. Test-first RED: [41665735912](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41665735912); focused GREEN after implementation: [41665873021](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41665873021).
- **Scope boundary:** this is TSV/input-integrity hardening only. It does not add IPA labels, change linguistic rules, or establish empirical accuracy. Independent adjudicated gold remains 0 and accuracy remains null.

## Current repository state — 2026-11-03 (post-merge)

- **Mainline integration:** benchmark implementation PR #123 was squash-merged as `0f73d006bfc05f6106a3b1e463c2cc7d6471ffae`; the handoff/register reconciliation PR #124 was squash-merged as `ebd8432b4abacecb50e30bae43ff64c42ac4063b`. No open PRs remained at this checkpoint.
- **Held-out benchmark contract:** gold export preserves `split`, `split_seed`, and `split_version`; adjudicated records without a frozen split fail closed; the scorer defaults to `test`; train/dev/all require explicit diagnostic selection; mixed manifest identities and empty prediction files are rejected.
- **Input integrity:** benchmark TSV headers/row widths, whitespace-only identifiers, duplicate JSON object keys, and non-standard JSON constants are rejected with regression coverage.
- **Post-merge exact-main verification:** Post-merge Quality checks, built-site Chromium browser smoke, GitHub Pages deployment, and deployed-site/runtime-asset smoke all passed on the exact `main` head. [workflow](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503253); [browser smoke](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503102); [Pages deployment and deployed smoke](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41707503262)
- **Research boundary:** Independent expert-adjudicated Khmer IPA gold remains 0; `data/benchmark/gold.tsv` is header-only; empirical accuracy remains null. Engineering, browser and deployment checks do not establish pronunciation accuracy.

## Current task ledger and blockers

- **DONE_VERIFIED:** deterministic manifest-wide split identity; export/scorer held-out split integrity; strict TSV and JSON input validation; post-merge exact-main engineering verification.
- **PARTIAL:** The consonant-series × dependent-vowel × coda × syllable-context matrix, automatic word segmentation, contextual /r/-loss profile, and Ukrainian correspondences remain incomplete or evidence-limited.
- **BLOCKED:** Approve a profile-specific IPA convention; recruit two qualified independent Khmer phonetic annotators and a separate adjudicator; clear source/audio rights and establish blinded intake.
- **TODO:** Manual visual, keyboard, screen-reader, responsive and mobile QA on the deployed site remains TODO.

## Historical checkpoints (retained for audit; superseded by the current state above)



- **DONE_VERIFIED (engineering):** independent IPA corpus schemas, runtime validation, deterministic split/rights gates, source/evidence documentation, and the exact-head automated engineering checks recorded in the historical entries below. This is not linguistic validation.
- **DONE_VERIFIED (web output hotfix):** PR #108 removed the stale `source-result` DOM write; current `main` no longer dereferences the absent element. Exact-main Quality, Chromium browser smoke, Pages deployment, and deployed-site asset smoke all passed on merge commit `e9894e5726f5f6aa2510d7d3beed69b2d03fb666`. This verifies the UI regression fix and deployment, not pronunciation accuracy. Manual visual, keyboard, screen-reader and mobile QA remain open.
- **PARTIAL:** source-language phonology, IPA conventions, and Ukrainian target adaptation remain bounded by the language-specific evidence matrices and unresolved cases. PR #107 separately narrows the runtime to the selected Phnom Penh careful-citation profile; it must not be conflated with the isolated UI hotfix.
- **BLOCKED:** the 30-lexeme blind pilot cannot start until the IPA convention is approved, two qualified independent annotators and a separate adjudicator are confirmed, rights-cleared source packets are prepared, and blind intake is arranged. See [issue #104](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/issues/104).
- **TODO:** manual visual, keyboard, assistive-technology and mobile QA on the deployed site; automated Chromium tests do not replace this human QA.
- **Next actionable engineering step:** reconcile PR #107 against post-hotfix `main` without reintroducing the removed DOM write; re-run exact-head tests and inspect the full profile diff before any merge. Separately complete manual keyboard, screen-reader and mobile QA. PR #108 is already merged; no release was published.

No local checkout was available; hosted CI is not local test execution, expert adjudication, manual accessibility QA, or proof that the current public URL has redeployed. Preserve fail-closed behavior and do not create IPA/gold labels from model output or unsupported spelling inference.


## Historical records

The dated entries below are retained as audit history. When a historical status or SHA conflicts with this current checkpoint, the active branch ref, completion register, and exact-head workflow run above are authoritative.

## Historical master handoff snapshot — 2026-10-25

**Last updated:** 2026-10-25  
**Repository:** https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-  
**Default branch:** main  
**Last audited base revision:** 6cc30bb48bedb83d86534a5fbff92839e26673dd  
**Latest implementation commits:** 479eda62aa32172bd6799caa324222c0260a7fc9 (style per-unit evidence breakdown), e1a2ba7304e96fe6afb392c74c0bfebd94531c2b (render per-unit IPA/status/source note safely), 117181206a4ec0b7be8c13e44da9c2f3d22367aa (show provisional-result notice), 9f4d583d469988e970c76d0080f32adfa92020f4 (test notice behaviour). Earlier audited revision: 3907ee710bad5c749805ce00d828c272a01838f9. This handoff update itself is a subsequent documentation commit; re-check main before the next code change. Recent implementation commits: 37d8e5dfb17144ed7c673841d2643fb38a9be9a6 (centralize effective register resolver), 7d3abf49720f05ed3f9f832fad22a105932e74bc (parser uses shared resolver), b45ecbd2a3567727db6c47ffbd56be5b75b4b556 (register regression tests), e4ff44656166d82d9dbb2554cf0d471612e37b4c (API status contract tests). Earlier matrix commits: d5686e6a1e4a8e5edbbf212ae7966305bdc6f1f8 and 9b7936c24b7ec584797d9e47aeb835afd670d091. Recheck latest main SHA and Actions runs before further work.

## Mandatory instructions for the next session

1. Read this document first, then docs/audits/2026-10-20-vowel-coverage-matrix.md and docs/audits/2026-10-20-coda-diacritics-matrix.md, docs/repository-audit.md, docs/superpowers/plans/2026-10-05-khmer-repository-finalization.md, docs/validation.md, docs/phonology.md, data/khmer/vowels.json, data/khmer/registers.json, data/khmer/sources.json, src/khmer_ua/parser.py, src/khmer_ua/phonology.py, src/khmer_ua/ipa.py and the related tests.
2. Check current main SHA, recent commits, CI, Pages workflow, and working tree before editing. This handoff's CI evidence refers to the earlier base revision, not necessarily the newest commit.
3. Continue from the first unresolved P0 below. Do not restart the entire audit unless the repository has materially changed.
4. Do not describe this as a complete IPA engine or claim full IPA verification while the vowel/coda/context matrix and adjudicated lexical corpus are incomplete.
5. After each work cycle, update this handoff and the relevant task/matrix statuses with commit SHA, changed paths, exact checks, results, unresolved issues, and the next action.

## Current evidence and state

- The repository is public, default branch main, and the connected GitHub permissions allow reading and writing.
- The latest commit before this audit was 6cc30bb48bedb83d86534a5fbff92839e26673dd (2026-10-09), message: "fix: classify unknown non-Khmer input as unsupported".
- GitHub Actions workflow runs for that base revision: Quality checks run 177 and Pages deployment run 187 both reported completed/success on 2026-10-09. This is historical CI/deployment evidence, not a test of the newer documentation commit or proof of linguistic completeness.
- The commit status API returned no individual statuses and state pending; prefer the actual Actions workflow runs when reporting workflow results.
- docs/audits/2026-10-20-vowel-coverage-matrix.md was initially added in commit 65c474768ef3db9f95573dfe443ee6fc9bcc41d7 and expanded in commit 9b7936c24b7ec584797d9e47aeb835afd670d091. It now indexes representative vowel, register, coda, NIKAHIT/REAHMUK, independent-vowel and orthographic-layout evidence from Unicode 17.0 Chapter 16 and R12A notes updated 2026-04-27. It remains intentionally non-exhaustive and is not an adjudicated IPA corpus.
- Source review confirms R12A's representative register-conditioned examples (ក vs គ; កី vs គី; កា vs គា), coda-sensitive contrasts (លង vs ល្ង), and that NIKAHIT/REAHMUK can affect both coda and nucleus. Unicode 17 is used as orthographic/illustrative evidence, not acoustic validation. Unicode 17.0 itself includes NIKAHIT contrasts (ដំ vs ដម; ពាំ vs ពាម). These are current-version source examples, but not an independently adjudicated gold corpus. The source-specific discrepancy between Unicode 17 Table 16-7 and R12A's simplified inherent-vowel examples is recorded in matrix commit fe38b18; do not flatten it into a universal mapping.
- Firecrawl research search was unavailable because the connected Firecrawl account reported insufficient credits; do not retry that connector this session. The publisher-hosted Chem (2020) PDF was subsequently reviewed: 21 speakers were screened, then 4 Phnom Penh speakers were selected; 61 lexical items were read three times, with formant and duration measurements. The paper explicitly discusses coda effects on vowel quality and length. This is useful acoustic evidence for prioritizing context, not a complete grapheme-to-IPA mapping.
- The previous plan at docs/superpowers/plans/2026-10-05-khmer-repository-finalization.md still has unchecked tasks, including phonological coverage, corpus, and final audit. Do not infer completion from files existing.
- No file named handoff, CITATION.cff, or LICENSE was found in the audited tree. Recheck before release work; this is an inventory observation, not a recommendation to add a license without deciding terms.
- The working web service is explicitly described by README as production-structured but linguistically coverage-limited.

## Architecture findings

### Implemented at structural level
- NFC normalization and parsing of consonants, coeng/subscript sequences, dependent/independent vowel signs, and format controls.
- Consonant series metadata and eligibility lists for MUUSIKATOAN/TRIISAP.
- Explicit parser outcomes for malformed or unsupported input.
- Register-shifter handling and the special ប៉ case in parser.py.
- Evidence/source registry, proposed Ukrainian mapping policy, representative lexical fixtures, adversarial web fixtures, Python and Node test suites, Vite build and Pages workflow.

### Not established as a complete phonological engine
- parser.analyze() returns phoneticization_not_yet_established rather than deriving complete phonetic output.
- resolve_inherent_vowel() deliberately returns a series label, not a deterministic IPA value.
- data/khmer/vowels.json records a short inventory and a few representative contrasts; it does not enumerate all attested vowel-sign × series × coda/context cases.
- The verified lexical corpus is small and uses Wiktionary sources for several items. Unicode representative examples establish orthographic examples but should not automatically be treated as independent acoustic or lexical IPA validation.
- There is no adjudicated gold corpus and no empirical accuracy score.
- A browser screenshot/pixel audit was not confirmed in the previous handoff/context; current responsive/accessibility behaviour still needs a dedicated check.
- The register helper inconsistency has been addressed in commits 37d8e5d and 7d3abf4: phonology.resolve_effective_register() now owns the shifter rules, parser.decompose_khmer_syllable() calls it, and phonology.resolve_register() applies it to a KhmerSyllable. Regression tests cover MUUSIKATOAN on second-series ង, the ប៉ exception, and an ineligible shifter. Python tests passed in Quality run 193 for commit b45ecbd2; the full workflow was still running at the last check. Recheck final run conclusion before calling the work verified.
- The previous deterministic /r/-loss profile was identified as overconfident because primary phonetic research reports variable aspiration, F0, phonation and vowel effects. The guard is merged as `1cbb5abdef1d7b7ac062199bfebdad14d9fe74b2`; exact-head Quality checks [40215678125](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40215678125) passed Python tests, web checks and site build. This is a fail-closed guard, not a complete profile model.

## Prioritized task register

| ID | Task | Priority | Status | Dependencies | Acceptance / verification |
|---|---|---|---|---|---|
| KH-VOW-001 | Expand vowel matrix using attested orthographic patterns, register, vowel sign, coda and profile | P0 | IN_PROGRESS | authoritative source extraction | Every row has source, confidence, IPA status, and test or explicit unresolved status; no arbitrary Cartesian product. PR #41 merged as `08fe98a88f5e3c0c3a21519b6cdc2024992d2f02`; evidence-gate CI [40210193894](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40210193894) passed source/status/conflict validation. Initial source-indexed rows are in matrix commit 9b7936c. |
| KH-VOW-002 | Verify vowel-sign inventories and contextual effects against Unicode + specialist phonology + acoustic literature | P0 | IN_PROGRESS | KH-VOW-001 | Orthographic inventory and R12A contextual descriptions reviewed; acoustic study and unresolved source/version differences still need review. Distinguish orthographic evidence from phonetic evidence. |
| KH-CODA-001 | Add coda-conditioned and syllable-structure cases, including NIKAHIT and REAHMUK | P0 | IN_PROGRESS | KH-VOW-001 | Source-indexed contrasts identified; conservative parser tests now assert that NIKAHIT/REAHMUK preserve structure without fabricating IPA (commit 262cffd). The NIKAHIT pairs are present in Unicode 17.0; independent lexical/phonetic adjudication remains open. |
| KH-IPA-001 | Audit parser-to-IPA API boundary and status semantics | P0 | IN_PROGRESS | matrix + model review | Python API contract tests in e4ff446 separate structural success from phonetic success. Browser shows a visible provisional notice and per-unit evidence breakdown. The unknown/mixed-script guard from PR #35 was merged into `main` as `a4912d520077f3e0df4e7236ae8784d8245354ff`; exact-main CI [40196341065](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40196341065) passed Python tests, web checks and site build. Follow-up PR #37 is now merged as `e39143cf5d880214765fff8f5a237e58d24ab00b`: browser parsing also rejects unknown material inside a Khmer unit, matching Python. Exact-head CI [40197626232](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40197626232) passed. General IPA generation, vowel/coda context coverage, and independent gold remain open; the overall task stays IN_PROGRESS. |
| KH-TEST-001 | Expand independently adjudicated lexical corpus | P0 | IN_PROGRESS | source review | Source-attested examples are now explicitly distinguished from independently adjudicated gold; build a held-out corpus with profile/audio adjudication before scoring |
| KH-REG-001 | Check helper register resolver against shifter-aware parser | P1 | DONE_VERIFIED | code-path review | PR #39 merged as `a0f5f6a272f10d79d5c383bf717363b5e18b053f`. Shared six-case JSON contract is consumed by Python and browser tests; both runtimes agree on effective register, rule ID and structural status for valid, ineligible and multiple shifters. Exact-head CI [40209903755](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40209903755) passed pytest, web checks and build. | The orthographic register resolver is verified. Inherent-vowel IPA quality, the full vowel/coda context matrix, and colloquial phonetics remain separate IN_PROGRESS research tasks. |
| KH-REG-002 | Verify encoded order of Khmer register shifters around visually prebase vowels | P1 | DONE_VERIFIED | Shared Python/browser fixture now tests `ង៉េ` (base + shifter + vowel sign in encoded order) and rejects `ងេ៉` (shifter after vowel sign). PR #51 merged as `123314b3fbb19e016270e7252fc86a933192cb93`; exact-head Quality checks [40222606376](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40222606376) passed. | Unicode 17.0 Chapter 16 says register shifters are encoded immediately after the base consonant; visual prebase placement must not be mistaken for code-point order. This is orthographic structure validation, not IPA gold. Main CI/Pages for the merge is pending as of this checkpoint. |
| KH-SOURCE-002 | Add source locators to all Khmer rule registry records | P1 | DONE_VERIFIED | PR #53 merged as `8c8c2939b44734bd30b7e63419c96c77e13217d4`; each rule now has a section-level locator, unique rule ID and registered source are validated. Exact-head Quality runs [40223685839](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40223685839) and [40223679988](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40223679988) passed. | Source traceability is improved; it does not resolve the full vowel × register × coda IPA matrix or create independent lexical gold. |
| KH-SOURCE-003 | Validate Khmer rule registry provenance and uncertainty contract | P1 | DONE_VERIFIED | PR #55 merged as `b447124dc429e60825e5da48a4feeecd04e54d4f`; exact-head Quality runs [40225032146](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40225032146) and [40225019704](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40225019704) passed. | Added `tests/test_rule_registry_provenance.py` validating unique IDs, source references, HTTPS records, specific locators, allowed statuses and the context-dependent NIKAHIT/REAHMUK contract. This verifies metadata/provenance only; it does not validate pronunciation accuracy. |
| KH-PROFILE-001 | Remove unsupported deterministic /r/-loss guess | P1 | DONE_VERIFIED | primary source review and exact-head CI | Merged as `1cbb5abdef1d7b7ac062199bfebdad14d9fe74b2`. `render_ipa_profile()` now raises an explicit `ValueError` for boundary-marked /CrV/ candidates under `phnom_penh_colloquial`; exact-head Quality run [40215678125](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40215678125) passed Python tests, web checks and site build. This verifies the fail-closed contract only, not colloquial IPA correctness. |
| KH-PROFILE-002 | Include aspirated IPA stop-/r/ onsets in colloquial uncertainty gate | P1 | DONE_VERIFIED | Exact-head Quality CI after regex and regression update | PR [#49](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/49) merged as `86c63af497ecb728eb8df338bd02ace85cf04a44`; optional IPA aspiration marker `ʰ` is now accepted before `r`, with regressions for `pʰrɑː`, `tʰrɑː`, `kʰrɑː`, and `cʰrɑː`. Exact-head Quality runs [40220444930](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40220444930) and [40220435721](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40220435721) passed. This closes a regex bypass only; it does not establish a complete /r/-loss environment model or gold IPA. |
| KH-UI-001 | Browser runtime, mobile viewport, accessibility and visual audit | P1 | IN_PROGRESS | stable engine cases | Added visible PROPOSED caution and per-unit status/evidence notes with safe text-only DOM construction. Still need keyboard/focus and responsive/browser visual audit; verify latest Quality/Pages workflows. |
| KH-REL-001 | License, CITATION.cff, release and Zenodo metadata review | P2 | TODO | authorship/license/data provenance decisions | Metadata accurate, source/data licensing checked, reproducible release archive; no invented author claims |
| KH-DOC-001 | Methodology note: “Khmer-to-Ukrainian Transcription: Register-Conditioned Vowels and Conservative IPA Analysis” | P1 | TODO | KH-VOW-001/002, KH-IPA-001 | Clearly separates orthography, phonology, broad IPA, phonetic profile, Ukrainian proposal and limits |

## Next concrete action

1. Verify Quality/Pages workflows for the latest coda evidence document commits 343e2ef and 84eb28c; the UI baseline Quality run 210 and Pages run 220 both succeeded for commit 66c6a20.
2. Continue KH-CODA-001: independently verify the R12A rhyme table transcription and build lexical examples for REAHMUK contexts, recording variety, gloss, source transcription, and any normalization to project IPA. Keep source-indexed examples distinct from gold adjudication.
3. Continue KH-IPA-001/KH-UI-001: test the per-unit view with long/mixed input, ensure output remains readable on mobile and accessible to screen readers, and confirm no status is lost in aggregate display. Do not treat browser fixture IPA as an independently adjudicated gold corpus.
4. Review docs/phonology.md and data/khmer/vowels.json against the scope of Chem (2020); preserve source-specific discrepancies. Do not add deterministic vowel mappings merely to make the matrix look full.

## Work log

### 2026-10-20 — audit continuation
- Reviewed repository tree and metadata, latest commits, existing implementation plan, repository audit, vowel/register/source data, parser, phonology helper, IPA profile helper, validation documentation, lexical corpus, adversarial corpus, package scripts, and CI workflow.
- Confirmed base revision's Quality checks run 177 and Pages deployment run 187 were successful on 2026-10-09; these are historical and do not validate newer documentation commits.
- Created initial matrix (commit 65c474768ef3db9f95573dfe443ee6fc9bcc41d7), handoff (commit 03e94ced1a2c319c462d53b681a3d61d348e1525), and plan links (commit b045495275b367c69a8e4c4ed8107faeb4724eb2).
- Expanded the evidence matrix with R12A/Unicode 17 source-indexed examples, coda-sensitive patterns, independent-vowel caveats, and source-version limitations (commit 9b7936c24b7ec584797d9e47aeb835afd670d091).
- Reviewed the publisher-hosted Chem (2020) PDF methods/results and added explicit study-design and coda-effect limitations to the matrix (commit d5686e6a1e4a8e5edbbf212ae7966305bdc6f1f8).
- Added tests/test_coda_marks.py (commit 262cffd76064cbb91c4fbeb83a04d38699e8353a) to guard against presenting deterministic IPA for NIKAHIT/REAHMUK before the coda/nucleus analysis is established.
- Updated the matrix to link GAP-004 to the conservative tests (commit bbf23f33263e17bc53264728cb058ee032589e12).
- Centralized effective register resolution in src/khmer_ua/phonology.py and made parser.py use the same helper (commits 37d8e5d and 7d3abf4). Added tests/test_register_resolution.py for a valid MUUSIKATOAN shift, the ប៉ exception, and an ineligible shifter (commit b45ecbd2). Quality run 193 completed successfully.
- Added tests/test_api_contract.py (commit e4ff446) to assert that structural success does not imply IPA success, and that unsupported/mixed input preserves status and never returns fabricated IPA. Quality run 195 passed; subsequent run 203 also passed the full Quality workflow for handoff commit 555a898.
- Browser audit found that an all-PROPOSED result did not show the caution panel, despite fixture values being explicitly provisional. Added getStatusNotice() and made the panel visible for PROPOSED results (commit 117181206a4ec0b7be8c13e44da9c2f3d22367aa). Added Node regression tests for PROPOSED, NOT_ESTABLISHED, INVALID_OR_UNSUPPORTED and ESTABLISHED_STRUCTURE notice semantics (commit 9f4d583d469988e970c76d0080f32adfa92020f4).
- Added a per-unit browser breakdown in commits 32aa0c4, e1a2ba7 and 479eda6. Each non-punctuation unit displays its source, status, IPA, Ukrainian candidate and note; content is inserted with textContent/createElement, not innerHTML. It is intended to expose mixed-input failures instead of presenting only concatenated output. Latest Quality run 209 and Pages run 219 were queued at last check.
- Opened R12A notes updated 2026-04-27, especially sections on registers, vowels, codas, NIKAHIT/REAHMUK, and independent vowels; reviewed Unicode 17 Chapter 16 for script examples and register shifters. Unicode 17.0 now confirms the explicit NIKAHIT contrasts; independent lexical/phonetic adjudication remains open.
- Firecrawl research search could not run because its connected account reported insufficient credits; no retries were made. No local Python/npm tests were run. Check current Actions/Pages runs for commit 9b7936c before claiming the documentation pipeline is green.

### 2026-10-20 — evidence register and external-engine screening
- Re-checked the latest default-branch workflow state before continuing: Quality run #215 and Pages run #225 completed successfully for commit 14ca4c33d06bdab7039a1022f035ca780391c888. These runs predate the current audit additions and do not validate them.
- Added `data/khmer/vowel-context-register.json` (initial commit 85bfac3; source-form correction b834703). It records source-indexed examples with graphemic structure, base series, register/coda context, IPA source, evidence status, limitations, and Ukrainian adaptation left unset where word-level output is not adjudicated. The register deliberately preserves the Unicode 17 / R12A inherent-vowel example discrepancy instead of collapsing it into a universal mapping.
- Added `tests/test_data_integrity.py` checks for registry fields, unique IDs, source references, conservative Ukrainian-output status, and explicit source conflict (commit 91a05c0). These tests have been committed but have not yet been run locally in this session; await the CI run for the new commit.
- Added `docs/audits/2026-10-20-external-phonemizer-audit.md` (commit 5cac544). Public documentation for `khmerphonemizer` describes word tokenization, phoneme-symbol lists, beam search, and optional lexicon use; the displayed symbols are IPA-like, but their complete IPA convention and exact lexicon/data provenance were not established by this source inspection. Treat it as a candidate comparator, not a gold oracle.
- Screened `chemvatho/Khmer-acoustic-model`: README describes a 29,204-entry IPA-labelled dictionary and reports a separate CC BY-SA 4.0 dictionary license while the code/model is MIT. No dictionary data was copied. The repository's exact entry provenance, phonetic convention, and claimed evaluation metrics were not independently reproduced.
- No external tool was installed or executed; no independent benchmark or accuracy figure is claimed. The current audit used public repository/package documentation only. Local Python/npm tests and browser/mobile visual checks were not run.
- Important audit observation: `data/tests/verified-lexical-corpus.json` currently labels six lexically sourced items `WELL_SUPPORTED`, but their cited sources are primarily Wiktionary pages and no entry-level independent adjudication record is present. The existing name/status should be reviewed in a dedicated follow-up; do not infer that these six entries constitute a phonetic gold corpus.
- Next: inspect CI for the registry/test commits; run Python + Node + build if an execution environment becomes available; then tighten the lexical corpus status semantics and audit the broad `/r/-loss` regex in `src/khmer_ua/ipa.py`. Do not add deterministic vowel rules until each context has adequate evidence.

### 2026-10-20 — lexical evidence-status correction and next phonology audit
- Updated all six entries in `data/tests/verified-lexical-corpus.json` from `ipa_status: WELL_SUPPORTED` to `SOURCE_ATTESTED_NOT_INDEPENDENTLY_ADJUDICATED`, adding an explicit evidence note. Their cited Wiktionary/lexical sources remain useful, but no audio-based or independent multi-source adjudication is recorded. Commit: 1e43292f1cb4abe204e7ac18c01e1e246b73995c.
- Added a data-integrity test forbidding those entries from claiming `WELL_SUPPORTED` absent adjudication (commit 8a32dc545d9fe26d125949b11123e90cabd81951). CI is pending/in progress for this change; no local test execution is claimed.
- The existing filename `verified-lexical-corpus.json` is legacy and now overstates its contents. Do not treat the filename as validation; consider renaming it only in a coordinated change that updates all test and runtime references.
- The current /r/-loss profile in `src/khmer_ua/ipa.py` remains a broad regex over IPA-like strings. It has a small unit test for one cluster, but no independently verified environment matrix. Do not expand its scope; audit the valid onset/coda boundaries against primary phonetic sources before modifying it.
- Next: check the newest Quality and Pages runs; inspect whether the new registry/status tests pass. Then audit the /r/-loss transform with explicit positive, negative and boundary examples and keep it labelled profile-level/provisional unless source-backed environments are verified.

### 2026-10-20 — documentation consistency and release metadata
- Corrected the README's overstatement that the small lexical corpus was independently supported: the cited phrase IPA is now described as source-attested but not independently adjudicated. Removed a stale assertion that the current main revision was green without checking its exact workflow SHA (commit 494ff78f2ff1526606f0c66141439d1587585167).
- Reconciled `docs/repository-audit.md` with the actual `src/khmer_ua/ipa.py`: a regex-based Phnom Penh /r/-loss transform is present and has only minimal unit coverage, contrary to older prose that said it had been removed. It remains an open P1 review item; do not treat the transform as fully validated (commit 402b6cef3c89b22c80d4dc44bc9b8ac7fdce83f2).
- Added repository license/citation metadata gaps to the external-tool audit: `pyproject.toml` declares MIT, but no root LICENSE or CITATION.cff was found in the inspected tree. Do not invent a copyright holder or author list; confirm terms before adding metadata (commit c543a8c9599dcee28afa609185ea83bb788f4cf6).
- CI evidence: Quality #219 succeeded for registry validation commit 91a05c0; Quality #220 succeeded for handoff commit b7fe0038. Quality #221 succeeded for the corpus status-only commit 1e43292. At the last check, Quality #222 for the new anti-overclaim test was still in progress, #223 queued for handoff commit 132c6640, and #224/#225 queued for README/repository-audit corrections. These runs do not cover the later commit c543a8c or the final handoff update; recheck exact SHA-specific runs before claiming final green status. Pages #229 succeeded for registry commit 91a05c0; later Pages runs were queued, pending, or cancelled by newer commits.
- No local Python tests, Node tests, Vite build, browser screenshots, mobile viewport tests, or external package execution were performed in this session. Successful GitHub Actions checks are the only execution evidence available here.
- Next priority: inspect the final SHA's workflow results. If CI passes, continue the P1 /r/-loss environment audit and then the P2 license/citation decisions. The P0 lexical gold corpus remains incomplete: source-attested rows are not independently adjudicated and must not be used for accuracy scoring.

### 2026-10-20 — bounded /r/-loss profile audit
- Checked current main workflow state before this cycle: Quality #227 and Pages #237 passed for handoff commit `f28c18a0`. This is the pre-change revision only.
- Found a concrete implementation risk in `src/khmer_ua/ipa.py`: the regex rewrote any matching `CrV` substring, even without a word/syllable boundary. An arbitrary string such as `akra` could therefore be changed although the function has no syllabification context.
- Changed the transformation to operate only at the beginning of the supplied IPA string or after an explicit space, syllable dot, or stress mark; unsegmented medial matches are preserved. Commit: `8949667a4ce91d71558b4896a12effe64ef1d3c1`.
- Expanded `tests/test_ipa.py` with word-initial, explicit-boundary, unsegmented-medial, coda-/r/, profile-preservation, and unknown-profile cases. Commit: `3d5aed8179134f74bbf23229cf153a6ebfb13d70`.
- Updated `docs/phonology.md` to explicitly label the transform a provisional string-level approximation that does not model full F0, phonation, vowel effects, or lexical conditioning. Commit: `c97c9f56a84cf1876930ddf37b7627a8e4ce8cec`.
- Latest workflow check: Quality #228 (fix commit) and #229 (test commit) were queued; Quality #230 for docs commit was queued. Pages #238 was in progress for the fix commit; #239 pending for tests; #240 queued for docs. Do not claim the latest changes passed until runs for the exact current SHA complete.
- No local Python/Node/browser tests were run. New tests are committed but not yet independently executed in this session.
- Interpretation limit: these tests verify conservative implementation boundaries, not the phonetic truth of any lexical /r/-loss example. The exact conditioning environments and full acoustic consequences still need review against primary phonetic studies and a dialect-labelled corpus.
- Next: re-check CI for current SHA, then continue P0 coda/REAHMUK source-indexing and IPA/status API/UI audit. Keep the independently adjudicated lexical corpus as an open P0; do not claim phonetic accuracy from source-cited fixtures.

### 2026-10-20 — NIKAHIT source conflict captured explicitly
- While continuing the coda audit, found a concrete cross-document/source mismatch for the same form ដំ ‘to pound’: the coda matrix records R12A `/ɗɑm/`, while the vowel matrix and Unicode 17.0 example record `/dɔm/`. This affects both onset notation and vowel quality; it must not be flattened into one source-neutral IPA.
- Updated `data/khmer/vowel-context-register.json` row KHV-007 to `CONFLICTING_SOURCE_ANALYSES`, with both verbatim source transcriptions, source IDs, and a no-selection criterion. Project IPA and Ukrainian output remain unset. Commit: `f2e80c41052b029a084e4cc1d4e5f7a1c62c1cf9`.
- Updated the vowel coverage matrix to flag SRC-006/VOW-014 as conflicting and blocked pending reconciliation; added an explicit discussion of the discrepancy. Commit: `e5fde73d8e4a51c1e3df3594c37809b42b821ca4`.
- Added a data-integrity assertion that the registry preserves both source alternatives without choosing one. Commit: `7d19e61204072e6d84eb02016fc63557d2b30edb`.
- Added the same caveat to the coda matrix. Commit: `aba5f13888d5e2a97dcde96ca436d960e28ad92d`.
- CI at the latest check: Quality #232 (registry conflict) queued; #233 (matrix) queued; #234 (test) queued; #235 (latest coda documentation) queued. Pages runs for intermediate commits were cancelled by newer pushes or remained queued/pending. No claim that the latest data tests have passed. Previously completed Quality #227 / Pages #237 were green only for the pre-implementation handoff revision `f28c18a0`.
- No local Python/Node/build/browser execution is available in this pass. This new conflict guard is committed but not yet independently executed.
- Next: check whether Actions actually runs for the latest SHA; if still blocked/queued, inspect workflow reasons before making more rapid pushes. Then continue the REAHMUK lexical evidence inventory and verify the source-specific transcriptions; do not promote these source examples to gold or runtime mappings.



### 2026-10-20 — REAHMUK lexical source inventory continuation

- Reviewed R12A's published character-detail examples for U+17C7 REAHMUK. The page supplies explicit lexical examples for the short-vowel combinations and for series-conditioned forms such as `សេះ` / `នេះ` and `កោះ` / `គោះ`. This is useful source evidence, but it is not independent audio adjudication.
- Added `data/tests/reahmuk-lexical-examples.json` (commit `f576eedf6145134434757c005982cfe5cbd62987`) with 11 source-indexed forms, glosses, verbatim source transcription strings, rhyme patterns, and limitations. The file explicitly warns that the strings are not normalized to project IPA and must not be used as gold labels.
- Added `tests/test_reahmuk_lexical_examples.py` (initial commit `c3b3bf871b333609b3f1277e66853012562bc90e`, assertion correction `74df5fdfad95313940e08ada2f8077f991bd2809`) to check the schema, provenance status, and a few series-sensitive examples.
- Expanded `docs/audits/2026-10-20-coda-diacritics-matrix.md` with the new inventory and its interpretation limits (commit `1f4755080bf10d1f4b820d52abae699e67b1d29f`).
- CI audit found Quality runs `39488178399` (commit `4f7891a`) and earlier runs `39488143676` / `39488125778` failing at “Run Python tests”; downstream Node/build steps were skipped. The API response exposed the failed step but not its traceback, so the precise failing assertion remains unverified. Do not claim tests pass. Inspect the current run/log or reproduce the workflow locally before more implementation changes.
- No local Python/Node test run or browser test was performed in this cycle.
- **Next:** first retrieve the Python failure traceback or run `python -m pytest` locally and fix the earliest failing assertion; then verify all Python tests, Node checks and build on the same commit. After CI is green, adjudicate a small REAHMUK subset against an independent lexical/audio source; keep the remaining source-indexed forms non-gold.


### 2026-10-20 — Python CI failure diagnosed and fixture corrected

- Retrieved the actual GitHub Actions job log for Quality checks run `39488650161`. Result: **54 passed, 1 failed**. The failure was `tests/test_ipa.py::test_phnom_penh_profile_does_not_rewrite_coda_r`.
- Root cause was a malformed test fixture, not evidence that the bounded regex was wrong: the assertion used `ar.kɑː` but expected `ar.kʰɑː`. There is no `r` after `k` in that input, so the implementation correctly left it unchanged.
- Corrected the input to `ar.krɑː` while retaining the expected output `ar.kʰɑː`; this now tests that the coda `r` before the explicit syllable boundary is preserved while the following onset cluster `kr` is transformed. Commit: `64fc5f8a717e91b39f3970ea20bb42c831ed3d46`.
- The fix is test-only; it does not strengthen the phonetic evidence or change engine behavior. Await CI for this commit before claiming the suite is green.


### 2026-10-20 — CI verification after onset-fixture correction

- Quality checks run [#242](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39488865390) completed **successfully** for commit `64fc5f8a717e91b39f3970ea20bb42c831ed3d46`.
- The job's Python tests, web checks, and site build all completed successfully on that SHA. This resolves the known malformed-fixture failure; it is software-test/build evidence, not independent phonetic validation.
- GitHub Pages deployment run [#252](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39488865332) was still in progress when checked. Verify its final result separately; do not assume a successful deployment from a successful build.


## Continuation update — 2026-10-21 (coverage audit tooling)

**Branch:** `feat/evidence-gated-coverage-audit-2026-10-21`  
**Starting default-branch commit:** `d06a5da7967032cecb0865ca86e5897d32fb90f7`  
**Latest implementation:** see the branch head and CI run; this section is updated as evidence arrives.

### Task ledger

- **DONE_VERIFIED — repository inspection:** Confirmed the default branch head, current source-indexed evidence registry, sign/consonant/register inventories, vowel and coda matrices, README, Python package, web tests, and CI workflow. Existing data and explicit source conflicts were preserved.
- **DONE_VERIFIED — deterministic inventory and generated artifact:** `scripts/coverage.py` builds `reports/khmer-coverage-audit.json` from canonical data, supports `--check` drift validation, validates required input shapes, counts register records correctly, and gives conflicts precedence over non-conflicting rows. The committed report currently contains 32 dependent-sign × series cells (16 dependent signs × two series), 4 source-attested-not-gold cells, 28 not-established cells, and no conflicts inside this narrow matrix. The source registry separately preserves conflicts KHV-007 and KHV-008. These counts describe evidence coverage, not pronunciation accuracy.
- **DONE_VERIFIED — regression coverage added:** `tests/test_coverage_report.py` checks reproducibility, matrix dimensions/status arithmetic, source conflict preservation, and that unresolved cells do not fabricate IPA. GitHub Actions Quality checks run [39570181898](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39570181898) passed on implementation/doc commit `d279c60cb89e6d0bca9e0c38eaf747fdb1143d10`: **58 Python tests passed**, web engine/runtime checks passed, and Vite production build passed. The handoff-only follow-up commit is checked again by CI separately.
- **PARTIAL — phonological evidence coverage:** Source-attested examples remain examples, not gold. The report covers only dependent sign × consonant series; inherent vowels and sign combinations with codas, length, syllabification, register shifters, lexical context, and pronunciation profiles remain separate open dimensions.
- **BLOCKED / evidence-limited:** Do not fill missing cells from Unicode names or structural patterns. KHV-007 and KHV-008 preserve non-equivalent source transcriptions and must not be normalized into one project IPA without source-convention, lexical, and profile reconciliation.
- **TODO — linguistic acceptance:** Build a versioned independently adjudicated corpus and complete the full context matrix; acceptance requires each deterministic output to have scoped provenance and regression coverage, while unsupported contexts must remain explicit.
- **TODO — cross-runtime parity:** Verify Python/browser/shared-data behavior for supported and unresolved cases, including malformed input and source-to-IPA-to-Ukrainian boundaries.
- **TODO — /r/ profile:** Expand positive and negative Phnom Penh /r/-loss environments only with validated lexical and phonological evidence; the current string-level transformation remains provisional.
- **PARTIAL — full verification:** Python tests (including report drift check), browser checks, and production build passed in GitHub Actions. The Pages workflow is restricted to pushes to `main`, so this feature branch has not been deployed; no production deployment is claimed. The local container could not resolve `github.com`, so all execution evidence comes from the repository's CI runner, not local commands.

### Evidence and limitations

The inventory script is not a pronunciation engine. It generates no IPA or Ukrainian output, and it does not promote source-indexed evidence to gold. The generated artifact is committed so CI can detect drift. A green software pipeline validates code/data invariants only; it does not prove phonological completeness or empirical accuracy.

### Branch / PR reconciliation

The repository-scoped open-PR query returned no open PRs at the start of this pass. Work remains on the dedicated continuation branch; no PR was merged, no user branch was deleted, and no release was published.


### Current continuation checkpoint

- **Implementation/code verification commit:** `d279c60cb89e6d0bca9e0c38eaf747fdb1143d10`.
- **Handoff/documentation commit:** this section's latest commit on `feat/evidence-gated-coverage-audit-2026-10-21`; consult the branch head for its exact SHA and CI result.
- **Release classification:** research prototype / evidence-limited preview, not release-ready as a complete Khmer-to-Ukrainian transcription engine. Software tests passing do not close GAP-001–GAP-010 or resolve source conflicts.


## Continuation update — 2026-10-21 (coverage dashboard on site)

- **DONE_VERIFIED — site integration:** `system.html` now contains a responsive evidence-coverage dashboard. `src/coverage.js` imports the committed report as a build-time JSON module, renders all 32 dependent-vowel × series cells, shows the four summary counts, preserves source-conflict IDs, and links to the complete machine-readable report. It uses DOM `textContent` rather than inserting report values as HTML. The existing local-first CSP remains unchanged; the dashboard requires no network requests or analytics.
- **DONE_VERIFIED — site regression guard:** `tests/web-engine.test.mjs` asserts the dashboard mount, adapter, status vocabulary, report dimensions, and report link.
- **DONE_VERIFIED — CI on dashboard commit:** Quality checks [run 39598081311](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39598081311) passed on `976cc5a40c633fee9a43868be980784539172a74`: 58 Python tests, web engine/runtime checks, and Vite production build. An earlier run on intermediate commit `a2c904bee6ef22cd62256e5dd281cdc4fab2b23f` failed because the HTML reference was committed just before the adapter file; the complete subsequent commit passed CI. No unresolved build failure remains at the verified head.
- **DONE_VERIFIED — public deployment (subsequently completed):** PR #1 was merged only after exact-head CI passed and GitHub reported mergeable. The Pages deployment for main commit `7f99f46beb290cfb240ded7438e568f0be0cd4d4` succeeded in run [39598303846](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39598303846). A follow-up fix then made the linked JSON a public static asset.
- **TODO — linguistics:** Dashboard displays existing evidence only; it does not close the vowel/coda/context matrix, establish a gold corpus, or adjudicate KHV-007/KHV-008. Keep release classification as evidence-limited research preview until those acceptance criteria are met.


## Continuation update — 2026-10-21 (public report asset fix)

- **DONE_VERIFIED — identified and fixed static-asset gap:** Vite only publishes files in its public directory; the dashboard's JSON hyperlink would otherwise target a report file that exists in the repository but is not copied to `dist`. The generator now writes both the canonical report and a byte-identical `public/reports/khmer-coverage-audit.json`; `--check` validates both copies, and a new pytest checks byte identity.
- **DONE_VERIFIED — fix branch CI:** Quality checks [run 39598494026](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39598494026) passed on `7754524b104269cd7b1069549c7c07b84680bbde`: Python tests, browser checks, and Vite build all passed.
- **DONE_VERIFIED — public asset merged and deployed:** PR #2 was merged at `48a1e2697ad802c31f21b99a404a10d7ab65b45c`. GitHub Pages run [39598640164](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39598640164) completed successfully, with build and deploy jobs green.


## Final continuation checkpoint — 2026-10-21

- **Live site:** https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/system.html#coverage-audit
- **Public JSON asset:** https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/reports/khmer-coverage-audit.json
- **Last verified deployed main SHA before this documentation-only checkpoint:** `48a1e2697ad802c31f21b99a404a10d7ab65b45c`.
- **Quality checks:** [run 39598640050](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39598640050) passed on the deployed main SHA.
- **Pages deployment:** [run 39598640164](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/39598640164) passed on the deployed main SHA.
- **Task ledger:** Dashboard, generated report, public static report copy, drift checks, regression tests, README, and deployment are `DONE_VERIFIED`. Full phonological/context matrix and independently adjudicated lexical gold corpus remain `TODO/BLOCKED` on evidence; KHV-007 and KHV-008 remain unresolved.
- **Release assessment:** Public research preview is deployed; the project is not certified as a complete or universally accurate Khmer-to-Ukrainian transcription engine.


## Continuation update — external Khmer G2P evidence reconciliation (2026-10-24)

- The optional Khmer Phonemizer 0.0.3 smoke run [40091745346](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40091745346) produced 6/6 outputs with 0 runtime errors. Its report records `independent_gold_count: 0` and `accuracy: null`; do not describe this as a 100% benchmark.
- Corrected the source-attested `ខ្ញុំ` entry: the cited Wiktionary page's standard IPA is `/kɲom/`; `k̥ʰñuṃ` is its separate orthographic/phonemic transcription. The previous `/kʰɲom/` value was not supported by that locator. A regression test now guards this distinction. Source: https://en.wiktionary.org/wiki/ខ្ញុំ
- For `ភ្នំពេញ`, the source gives `/pʰnum ˈpɨɲ/`, including a boundary/space and stress marker. The engine's token output omits those marks. This is an unresolved output-convention/representation difference, not an adjudicated phonological error. Source: https://en.wiktionary.org/wiki/ភ្នំពេញ
- Broader phonetic context: Khmer contrasts plain and aspirated stops (https://aclanthology.org/Y16-1.pdf); colloquial Phnom Penh /CrV/ realizations may differ through aspiration, f0 and phonation (https://doi.org/10.1016/j.wocn.2014.02.001). These papers do not independently adjudicate the candidate outputs for these lexical items.
- Dedicated branch: `fix/khmer-g2p-source-ipa-reconciliation-2026-10-24`. Pending CI. Keep external engine disabled in production and retain the evidence status SOURCE_ATTESTED_NOT_INDEPENDENTLY_ADJUDICATED.


## CI reconciliation note — Khmer source IPA fixture (2026-10-24)

- The first quality run on this evidence correction failed exactly where expected after changing the canonical corpus: `tests/test_data.py::test_verified_corpus_and_web_fixtures_agree_on_ipa` found the web fixture still held `/kʰɲom/` while the source-reconciled corpus now holds `/kɲom/`. The run had 67 passing tests and 1 failing test; this was fixture drift, not a runtime/adapter failure.
- Updated `data/tests/web-fixtures.json` to `/kɲom/`, added the separate orthographic transcription field, and clarified the note. The next quality and optional-G2P workflows are queued on head `a1ffffa821e809b638db328b1f23bc6b6a27bef4`; re-check their final conclusions before merge.
- Acceptance remains: full quality suite green, optional smoke successful, corpus and web fixture IPA aligned, accuracy still null / no independent gold.


## Final checkpoint — G2P source IPA reconciliation merged (2026-10-24)

- **Merged PR:** [#11](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/11), merge commit `35ce7142bf71f7e4cdb1acbb44d94d45ef71693a`.
- **Quality verification:** [run 40093054206](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40093054206) passed after the fixture correction, including Python tests, web-engine/runtime checks and site build. The earlier failures are recorded above: the canonical corpus correction first exposed stale JSON and JavaScript fixture expectations; both were aligned with the cited source.
- **Latest raw-output smoke:** [run 40093054099](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40093054099) passed. `khmerphonemizer==0.0.3`, 6/6 outputs, 0 errors; corpus SHA-256 `4b0fafa4a178c0a3e769ddb168f2115cd1fda0c98919c3bc2d731c13cbe6a7f4`; artifact SHA-256 `89eb762a46da84941bf47c7b26d7b18134270bcdede29bc7f1be8bcd60653f89`.
- **Source correction:** current cited Wiktionary standard IPA for `ខ្ញុំ` is `/kɲom/`; `k̥ʰñuṃ` is kept as separate orthographic/phonemic notation. For `ភ្នំពេញ`, source IPA `/pʰnum ˈpɨɲ/` includes stress/boundary information absent from the external phone-token output. No independent gold corpus exists; report still has `independent_gold_count: 0`, `accuracy: null`.
- **Release status:** research preview / partial prototype, not a complete or empirically accuracy-certified Khmer→Ukrainian engine. External engine remains diagnostic-only.


Authoritative readiness checkpoint — 2026-10-24 12:38 UTC

- Current main HEAD: 8e7209df4ec6c05767a8870368b112774681a151.
- Current-main quality checks: DONE_VERIFIED. Run 40093541363 passed; Pages deployment 40093541446 passed.
- Optional G2P smoke: DONE_VERIFIED as raw-output execution only. Run 40093213224 passed with six outputs, zero runtime errors, no independent gold; artifact SHA-256 89eb762a46da84941bf47c7b26d7b18134270bcdede29bc7f1be8bcd60653f89.
- The cited standard IPA for ខ្ញុំ is /kɲom/; k̥ʰñuṃ remains separately labeled as orthographic/phonemic notation. ភ្នំពេញ still requires an explicit convention for stress and syllable boundaries.
- Remaining TODO/BLOCKED: complete vowel/coda/context matrix, adjudicated lexical IPA corpus, source review for unresolved context-sensitive cases KHV-007/KHV-008. Unicode and external G2P output are not substitutes for acoustic or expert-adjudicated phonetic evidence.
- Readiness: research preview is build/test/deploy verified, not a complete or empirically accuracy-certified transcription engine.


## Browser/Python IPA profile parity correction — 2026-10-24

### Finding
The Python profile adapter in `src/khmer_ua/ipa.py` correctly restricts the Phnom Penh colloquial /r/-loss approximation to an explicit word/syllable boundary (`^|[ .ˈˌ]`). The browser adapter in `src/main.js` instead rewrote every matching `CrV` substring, including an unsegmented medial match. That violated the documented conservative boundary rule and made Python/browser behavior diverge.

### Change prepared
- Updated the browser regex to require the same explicit boundary as the Python implementation and preserve the captured boundary and onset.
- Strengthened `tests/web-engine.test.mjs` to require the boundary-aware pattern and replacement.
- Existing Python behavioral tests cover word-initial and explicitly segmented onset clusters, unsegmented medial matches, and coda /r/.

### Verification boundary
- Change is on PR [#14](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/14), based on main `1977822694cb5ce31fc9cb54ab79446605907738`.
- The browser test is a source-guard test; the existing Python tests are the behavioral reference. Quality workflow [40112562271](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40112562271) passed on the exact PR head `6fcd4442746f091159136e0b2b5ec126224c6e1b`: Python tests, web checks, and site build all succeeded. PR #14 merged as `d5245c0d7ab94de9c1774a705da1a3a7a14617f5`; post-merge quality [40113051028](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40113051028) and GitHub Pages deployment [40113051034](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40113051034) both passed on the merged HEAD.
- This fixes implementation parity; it does not validate the underlying linguistic hypothesis or expand the evidence-backed contexts in which the colloquial rule may apply.


## IPA benchmark harness and external engine protocol — 2026-10-24

- Added `scripts/benchmark_ipa.py`, a standard-library-only harness with strict Unicode NFC exact match, code-point Levenshtein CER (diagnostic only), and explicit missing-prediction accounting. Every independently adjudicated gold row remains in each engine's denominator; omitted outputs cannot inflate accuracy.
- Added `data/benchmark/gold.tsv` and `data/benchmark/predictions.tsv` header templates plus `tests/test_benchmark_ipa.py` covering no-gold behavior, adjudication gating, diacritic preservation, missing rows, and mismatches.
- Added `docs/benchmarking-and-external-ipa.md`; linked the existing `data/external-ipa-renderers.json` inventory to the benchmark protocol. External candidates remain optional and disabled by default.
- PR is open; current CI is queued / not yet verified. Do not merge until hosted tests pass. Local GitHub access is unavailable from the current container due network/DNS failure.
- No adjudicated gold corpus was added and no accuracy score is claimed. Candidate engine language support, actual IPA semantics, exact versions, and model/data licensing still require verification. Registry presence and smoke execution are not evidence of accuracy.
- Required next acceptance: run the repository test suite including the new harness tests; inspect all generated-artifact checks; then populate the gold set only with source-located, independently adjudicated pronunciations and rerun all engines against the same held-out set.


## External IPA/G2P and benchmark continuation — 2026-10-24

- Registry and per-language evidence notes: `data/external-ipa-renderers.json` and `docs/benchmarking-and-external-ipa.md`.
- External outputs are diagnostics only unless compared against a versioned, independently adjudicated gold set. Engineering fixtures and source-attested dictionary entries are not automatically gold.
- Shared harness: `scripts/benchmark_ipa.py`; empty templates at `data/benchmark/gold.tsv` and `data/benchmark/predictions.tsv`; tests at `tests/test_benchmark_ipa.py`.
- External comparator provenance audit PR #20 merged as `f5b6de77b30c2e6c65d94f9a31871d7bddf7a5a4`. Khmer Phonemizer 0.0.3 smoke returned 6 outputs without runtime errors; outputs remain unadjudicated and not directly string-comparable to source IPA. Independent gold remains 0.
- Keep IPA adaptation boundary: source spelling → structural parse → source phonology → typed IPA → Ukrainian adapter. Third-party candidates remain optional and disabled in production.
- Current true blocker: a source-located, independently adjudicated language-specific gold corpus with a documented dialect and IPA convention. Do not report accuracy until it exists.


### Verified status as of 2026-10-24

PR #17 merged as `edf625847029bbc3a043a0c01a09115e263164fb`. Latest quality checks and external smoke passed; 72 tests and 22 subtests passed. Khmer Phonemizer 0.0.3: 6 outputs, 0 runtime errors, independent gold=0, accuracy=null. Durable report: `data/benchmark/runs/external-g2p-smoke-2026-10-24.json`; artifact: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40120003193/artifacts/12569269396.

- Keep IPA adaptation boundary: source spelling → structural parse → source phonology → typed IPA → Ukrainian adapter. Third-party candidates remain optional and disabled in production.
- Current true blocker: a source-located, independently adjudicated language-specific gold corpus with a documented dialect and IPA convention. Do not report accuracy until it exists.


## IPA gold provenance gate — merged 2026-10-24

- PR #21 merged; benchmark scoring now fails closed when an ADJUDICATED row lacks non-empty `gold_ipa`, `source_id`, or `profile`. Regression tests and optional Khmer G2P smoke passed on the merged head. This validates metadata completeness only; it does not validate the phonetic truth of a label.
- Latest successful Khmer Phonemizer 0.0.3 run [40121359605](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40121359605): 6 outputs, 0 runtime errors, 0 independent gold rows, accuracy null. Raw phone-token arrays remain unadjudicated and not directly string-comparable to source IPA without a declared convention.
- Artifact ZIP SHA-256: `3cd5ad913909cd1ff692c192614f354b707f705c1b6a2f1dc7ad971a4baf63a5`.


### Khmer external IPA notation diagnostic — 2026-10-24

- Pinned `khmerphonemizer==0.0.3` run [40128165807](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40128165807) passed with 6/6 outputs and 0 runtime errors. Strict token-join vs source IPA content matches 2/6; a separate notation-only comparison ignoring only slash wrappers, whitespace, syllable dots and stress marks matches 6/6. Aspiration, length, diacritics, tie bars and phone symbols remain significant. These are source-attested comparisons, not accuracy; independent gold count is 0. Artifact ZIP SHA-256: `2cbc7b00d35325e2e97fc98e80efeb9fdfecd477bf5ae5be24c43b6726c33299`.

## Authoritative current-head checkpoint — 2026-10-25

This checkpoint supersedes earlier readiness notes with stale main SHAs or queued-workflow status.

- Current `main`: `cb5331d2b587733180d9a585631dee26d0c370d9`.
- Quality checks [40129501080](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40129501080): `success`; Pages deployment [40129501022](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40129501022): `success`; optional Khmer G2P smoke [40129500995](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40129500995): `success`.
- The evidence registry is synchronized with the latest inspected smoke evidence from run [40128165807](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40128165807): 6 outputs, 0 runtime errors, 0 independent gold, accuracy null. Smoke outputs and notation-normalization agreement remain diagnostics, not adjudicated accuracy.
- Generated report, public report copy, drift checks and software CI are verified. The complete vowel/coda/context matrix, unresolved KHV-007/KHV-008 source-profile reconciliation and independent expert-adjudicated Khmer IPA gold remain PARTIAL/BLOCKED. Do not fill missing evidence from Unicode names or external G2P agreement.

## Latest external-smoke artifact reconciliation — 2026-10-25

- Inspected current-main smoke [40129500995](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40129500995), artifact [12574167928](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40129500995/artifacts/12574167928), SHA-256 `da53268c5d66ba3e2e5682029deb4bd6c2566466fbd920d72a6e3d9cab322f33`. The artifact contains one valid JSON report: khmerphonemizer 0.0.3, 6/6 outputs, 0 runtime errors, corpus SHA-256 `4b0fafa4a178c0a3e769ddb168f2115cd1fda0c98919c3bc2d731c13cbe6a7f4`.
- Source-attested notation diagnostic: 2/6 strict matches, 6/6 after limited normalization of slash wrappers, whitespace, syllable dots and stress only. Do not call this accuracy or gold agreement. Independent gold remains 0; accuracy remains null.
- The external-system registry and benchmarking documentation now reference this latest inspected artifact; earlier run records are retained for provenance.

## Final smoke and trigger-loop checkpoint — 2026-10-25

- After PR #32 narrowed the optional smoke workflow's automatic path filters, current-main smoke [40133705156](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40133705156) passed; inspected artifact [12575459926](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40133705156/artifacts/12575459926), ZIP SHA-256 `ff588e5d6a0e533aa4de7427e4786672f03999c3f7131abb1c89cb828936a677`.
- Report: 6/6 outputs, 0 runtime errors, corpus SHA-256 `4b0fafa4a178c0a3e769ddb168f2115cd1fda0c98919c3bc2d731c13cbe6a7f4`; 2/6 strict source-attested string matches and 6/6 limited notation matches. Independent gold 0, accuracy null.
- Registry and benchmark documentation now point to this final inspected run. Evidence-only updates no longer trigger optional smoke, avoiding a self-referential sequence of new run IDs and registry edits.
- Remaining research blockers unchanged: independently adjudicated Khmer IPA gold, unresolved source/profile conflicts KHV-007/KHV-008, and complete vowel/coda/context evidence. No engine promoted to production.


## Multiple register-shifter uncertainty regression — 2026-10-25

- PR #34: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/34
- Added a runtime test asserting that a syllable with multiple register shifters returns `EVIDENCE_LIMITED` / `MULTIPLE_REGISTER_SHIFTERS`; wired it into both `npm test` and `npm run check`.
- Verification: Quality checks [40192533827](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40192533827) completed successfully on commit `78ec839322ca3211469ff7c0d46639c0d55eb78c`.
- This verifies conservative parser behavior only. The external G2P diagnostic remains 6/6 outputs with 0 runtime errors, but independent gold remains 0 and accuracy remains null. Complete vowel/coda/context evidence and unresolved source/profile conflicts remain open.


## Unknown-character fail-closed correction — 2026-10-25

- Branch: `fix/khmer-reject-unknown-grapheme-material-20261025`; PR [#35](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/35).
- Defect: `decompose_khmer_syllable` recorded an unknown character as `sign_or_unknown` but continued; if the same unit contained a recognized Khmer base consonant, final status could be `ESTABLISHED_STRUCTURE`. Example: mixed-script input `កx`.
- Test-first evidence: [run 40195870960](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40195870960) failed as expected because `analyze("កx")` returned `ESTABLISHED_STRUCTURE`.
- Fix: the parser now returns `INVALID_OR_UNSUPPORTED`, confidence `0.0`, and source-labeled grapheme diagnostics immediately when a character is not in the known Khmer sign registry. This is a structural rejection, not an IPA rule.
- Verification: post-fix exact-head run [40195885161](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40195885161) **passed** Python tests, web checks and site build.
- Linguistic gate remains open: the general orthography-to-IPA pipeline still intentionally withholds IPA; representative register/vowel examples and acoustic literature are not a complete context-conditioned mapping or independent adjudicated lexical gold. Independent gold count remains 0.


## Post-merge checkpoint — 2026-10-25

- Default branch now contains merge commit `a4912d520077f3e0df4e7236ae8784d8245354ff` for the unknown-character structural guard.
- Exact-main workflow [40196341065](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40196341065) passed Python tests, web checks and site build.
- This closes the specific mixed-script false-positive, not the overall KH-IPA-001 task. IPA mapping, source/profile conflicts, vowel/coda context, and independent gold remain unresolved.


## Browser parity: unknown Khmer material — 2026-10-25

- Follow-up inspection after the Python guard merged found the browser parser still downgraded unknown characters to `EVIDENCE_LIMITED`, allowing a recognized base consonant to lend false structural confidence to mixed-script input.
- The browser now returns `INVALID_OR_UNSUPPORTED` with the unknown characters preserved in diagnostics, matching Python's contract. Runtime regression tests cover `parseSyllable("កx")` and ensure the unknown fragment is not treated as established structure.
- Exact-head CI must pass Python tests, web-engine/runtime tests and build checks before this follow-up is merged. The guard is structural only; the broader IPA mapping and independent gold corpus remain open.


## Browser unknown-character guard merged — 2026-10-25

- PR #37 merged to `main` as `e39143cf5d880214765fff8f5a237e58d24ab00b`.
- Exact-head quality workflow [40197626232](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40197626232) passed. The regression verifies `កx` is `INVALID_OR_UNSUPPORTED` end-to-end in the browser, including unit-level status and output withholding.
- This closes a structural parity defect only. The repository still lacks a general source-orthography-to-IPA engine and independent adjudicated gold; do not mark the full IPA task complete.


## Khmer shared register-shifter parity fixture — 2026-10-25

- Added `data/tests/register-shifter-contract.json` with six structural cases: second-series MUUSIKATOAN, the ប៉→ប exception, first-series TRIISAP, two ineligible shifters, and multiple shifters.
- Python and browser-runtime tests consume the same fixture and assert effective register, exact rule ID and structural status. The fixture deliberately contains no IPA gold labels.
- KH-REG-001 remains IN_PROGRESS until exact-head CI passes; even after that, inherent-vowel quality and colloquial phonetics remain separate research tasks.


## Khmer register-resolver verification — 2026-10-25

- Reviewed the Python parser, `resolve_effective_register`, `resolve_register`, browser `resolveRegister`, and all direct tests/call sites. Both implementations remove ZWNJ for shifter-position calculation and preserve the same eligibility, exception, and fail-closed rules.
- PR #39 merged as `a0f5f6a272f10d79d5c383bf717363b5e18b053f`. Exact-head CI [40209903755](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40209903755) passed pytest, web checks and site build; the browser contract test is wired into `npm run check`.
- KH-REG-001 is DONE_VERIFIED for orthographic register resolution only. This does not validate inherent-vowel IPA or phonetic realization.


## Khmer vowel evidence-registry validation — 2026-10-25

- Added a test for `data/khmer/vowel-context-register.json` that checks unique case IDs, known evidence statuses, registered source IDs, and the rule that source-attested/non-gold rows cannot emit Ukrainian output.
- Conflicting source analyses must keep `ipa=null`, retain at least two source-specific alternatives, and state a selection criterion. This prevents incompatible Unicode/R12A examples from silently becoming one project-wide IPA.
- This validates provenance and withholding contracts, not the correctness of any IPA row. Exact-head CI must pass before merge.


- Post-merge evidence-gate checkpoint: PR #41 merged as `08fe98a88f5e3c0c3a21519b6cdc2024992d2f02`; exact-head CI [40210193894](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40210193894) passed. KH-VOW-001 remains IN_PROGRESS because provenance validation does not adjudicate source disagreements or establish the full vowel/coda/context matrix.


## Research and implementation checkpoint — 2026-10-25

- Reviewed the publisher-hosted author manuscript for Kirby (2014), DOI [10.1016/j.wocn.2014.02.001](https://doi.org/10.1016/j.wocn.2014.02.001), alongside Wayland (2005). The source describes several /r/-loss correlates and multiple colloquial realizations; aspiration-only output is not a uniquely determined result from a broad IPA string.
- Branch `fix/khmer-r-loss-profile-fail-closed-20261025` changes `src/khmer_ua/ipa.py` to reject ambiguous deterministic colloquial rendering; `tests/test_ipa.py` now checks the uncertainty boundary; `docs/phonology.md` records the evidence and limitation.
- This is a correctness guard, not added phonological coverage. The full orthography-to-IPA engine and independently adjudicated corpus remain absent; do not increase readiness based on this change alone.
- Exact-head Quality run [40215678125](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40215678125) passed Python tests, web checks and site build for the merged fail-closed profile guard. No local test result is claimed.


- Next profile task: `TODO` — design an alternatives-aware result contract that can represent multiple colloquial realizations with lexical/profile metadata. Do not re-enable a single deterministic aspiration-only output from a broad IPA string.


## Post-merge current-head checkpoint — 2026-10-25

- Current `main` after the colloquial /r/-loss fail-closed correction is `33778677a776fe8bbd51d8789368daac2cda74d9`.
- Current-main Quality checks [40215767648](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40215767648) and Pages deployment [40215767572](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40215767572) passed. The colloquial profile no longer collapses source-attested variable /r/-loss outcomes into an unsupported single aspiration-only rendering.
- Remaining P0 blockers are still substantive: contextual vowel × register × coda derivation, complete phonological IPA generation, and a source-located independently adjudicated lexical/audio gold set. This checkpoint does not raise measured accuracy; gold accuracy remains unmeasured.


## Khmer target-comparator evidence gate — 2026-10-25

- Target-layer review found that `map_segment(..., mode="compatibility_ru")` silently fell back to the Ukrainian default when a segment lacked a Russian comparator entry. For example, Khmer IPA `i` was returned as Russian compatibility `і`, which is a Ukrainian target choice and not an established Russian comparator mapping.
- Removed the fallback. Missing Russian comparator entries now raise from the strict mapper; `explain_segment` exposes `ru_compatibility: null` and `ru_compatibility_status: NOT_ESTABLISHED` while retaining the Ukrainian candidate separately. Added regression coverage.
- This makes target-policy provenance more honest; it does not establish a new IPA mapping or official Ukrainian/Russian standard. Exact-head Quality checks and site build must pass before merge.


## Post-merge target-comparator checkpoint — 2026-10-25

- The Russian comparator fallback correction merged as `894a2628b20c75f54733adcf49b3242625e2803d` via [PR #47](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/47). The earlier conflicted PR #46 was closed as superseded; its branch was left untouched.
- Exact-head Quality checks [40217188087](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40217188087) passed. The change ensures missing Russian comparator entries are `NOT_ESTABLISHED` rather than silently copied from the Ukrainian mapping.
- This fixes target-policy provenance only. Khmer phonological IPA generation and independent gold remain the primary P0 blockers; no empirical accuracy percentage is claimed.


## Aspirated stop-/r/ uncertainty guard — 2026-10-25

- PR [#49](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/49) merged as `86c63af497ecb728eb8df338bd02ace85cf04a44`.
- The previous `/CrV/` candidate regex did not match IPA forms where the aspiration diacritic `ʰ` occurs between the stop and `r`, allowing such forms to bypass the colloquial uncertainty guard. The pattern now accepts an optional `ʰ` and tests the aspirated sequences `pʰrɑː`, `tʰrɑː`, `kʰrɑː`, and `cʰrɑː`.
- Exact-head Quality runs [40220444930](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40220444930) and [40220435721](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40220435721) passed. This verifies a conservative guard, not a complete colloquial phonetic model.
- The broader alternatives-aware profile result contract, contextual vowel/coda IPA, unresolved source/profile reconciliation and independent expert-adjudicated gold remain open.


## Register-shifter encoded-order checkpoint — 2026-10-25

- PR [#51](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/51) merged as `123314b3fbb19e016270e7252fc86a933192cb93`.
- Extended `data/tests/register-shifter-contract.json`, shared by Python and browser tests, with a valid base + shifter + vowel-sign sequence `ង៉េ` and an invalid shifter-after-vowel sequence `ងេ៉`.
- Primary source: Unicode 17.0.0 Chapter 16, Khmer “Consonant Shifters” and “Ordering of Syllable Components”: https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-16/. It states that shifters are encoded immediately after the base consonant even where vowel glyphs are visually reordered. The new fixture is a structural regression contract, not a lexical IPA label.
- Exact-head Quality checks [40222606376](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40222606376) passed. Post-merge main checks [40222854594](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40222854594) and Pages [40222854484](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40222854484) were queued when this checkpoint was authored; verify before claiming the merged head is green.
- The full contextual vowel/coda/register-to-IPA matrix and independent lexical/audio gold remain open.


## Rule source-locator checkpoint — 2026-10-25

- PR [#53](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/53) merged as `8c8c2939b44734bd30b7e63419c96c77e13217d4`.
- Added explicit section-level locators to each canonical `data/khmer/rules.json` record. Orthographic claims cite Unicode 17.0 §16.4 Khmer; NIKAHIT and REAHMUK cite Richard Ishida’s specialist orthography notes.
- Tests now require unique rule IDs, known source IDs and non-empty, non-pending locators. Exact-head Quality runs [40223685839](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40223685839) and [40223679988](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40223679988) passed.
- This closes a source-traceability gap, not the contextual IPA gap. Independent lexical/audio gold remains unavailable; no accuracy claim is added.


## Rule registry provenance contract — 2026-10-25

- PR [#55](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/55) merged as `b447124dc429e60825e5da48a4feeecd04e54d4f`.
- Added `tests/test_rule_registry_provenance.py` for `data/khmer/rules.json` and `data/khmer/sources.json`. It checks unique IDs, registered sources, HTTPS records, section/table/code-point-level locators, required fields and evidence statuses.
- The test explicitly protects the context-dependent status for NIKAHIT and REAHMUK and ensures the register-shifter record remains a script/register claim rather than a complete contextual IPA mapping.
- Exact-head Quality checks [40225032146](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40225032146) and [40225019704](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40225019704) passed. No local tests are claimed.
- First unresolved P0 tasks remain the full vowel × register × coda/profile matrix, source conflict reconciliation, and independently adjudicated lexical/audio gold. This metadata test does not close those tasks.


## Romanization → IPA → Ukrainian result order — 2026-10-29

- Open draft PR [#57](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/57) adds a separate Khmer romanization card before the existing IPA and Ukrainian candidate cards. The original Khmer text remains available as a later source card.
- Romanization engine: `@gmana/km-translit@0.1.2`, MIT, BGN/PCGN-derived ASCII profile. The package explicitly says it drops diacritics and is **not** a fully conformant BGN/PCGN implementation; UI labels it accordingly. This is a separate orthographic romanization output and does not feed IPA or Ukrainian conversion.
- Exact-head CI for `aed14ec04b123d1aff81a5cd11b59eda35c3b961`: [Quality checks run 40780984225](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40780984225) **passed**. Python tests, Node checks, build, and generated-page checks passed. The added romanization test is included in `npm run check`; there is no dedicated browser automation in this repository.
- Status: UI/engine integration **PARTIAL / CI-PASS**. Independent Khmer pronunciation gold remains unavailable; do not treat the Latin output or the existing research IPA/Ukrainian candidate as normative.
- Next acceptance gates: independently inspect mixed-script/punctuation behavior in a browser; expand source-backed romanization fixtures; retain the profile/license notice; keep this PR draft until the owner approves the intended profile and the remaining language-engine evidence gates are reviewed.


## Publication checkpoint — 2026-10-29

This checkpoint supersedes earlier notes in this handoff saying the romanization PR was open/draft.

- PR #57 was merged to main as 875054f3ff31a2cebabd2d23672843791b746142.
- Exact post-merge Quality checks [40782813125](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40782813125) passed.
- Exact post-merge GitHub Pages deployment [40782813148](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40782813148) passed and reported URL: https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/
- Published output order: Khmer romanization → IPA → Ukrainian candidate; the romanization is independent and its upstream profile limitations remain as documented above.
- Remaining linguistic/UI acceptance gates are unchanged: independent Khmer pronunciation gold, broader source-backed romanization fixtures, and manual browser/mobile/accessibility QA. Publication does not mean linguistic completeness.


## Shared Ukrainian target adaptation checkpoint — 2026-10-30

- PR #59 (draft), branch `fix/shared-ukrainian-phonetics-2026-10-30`, applies the common target policy after Khmer IPA: /pʰ tʰ kʰ cʰ/ → п' т' к' ч'; foreign /h/ → г; hard /ɡ/ → ґ; genuine /x/ → х.
- Added explicit target mappings for /t͡s/ → ц, /d͡z/ → дз, /t͡ʃ/ and alveolo-palatal /tɕ/ → ч, /d͡ʒ/ and /dʑ/ → дж, /ʃ/ → ш, /ʒ/ → ж, plus supported palatalized sequences.
- The apostrophe marks aspiration only. It is not an output for /ʔ/ and is not the Ukrainian orthographic apostrophe. Adjacent consonants are not fused into an affricate without a source phonological affricate analysis.
- Updated source-attested lexical practical proposals: `ភាសាខ្មែរ` → `п'ієса к'мае`; `ហើយ` with /h/ → `гаеі`. The Phnom Penh colloquial profile's attested /cʰ/ candidate now outputs ч' rather than neutralizing aspiration.
- Exact-head CI [41076121018](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41076121018) passed Python (82 tests, 25 subtests) and all web checks, including runtime, register-shifter and romanization contracts. Branch head at verification: `677a9191e0614a7c9d9a55a259920689e0d04ec3`.
- Existing PR #58 was left untouched. This PR is still draft and is not merged.

These changes implement project-approved target conventions; they are not a new official Ukrainian standard and do not create new Khmer pronunciation evidence. Existing research blockers remain: contextual vowel/register/coda derivation, complete phonological IPA coverage and independent lexical/audio adjudication. Accuracy remains unmeasured.


## Romanization standard and crosswalk checkpoint — 2026-10-31

- Added [romanization-to-ukrainian-matrix.md](romanization-to-ukrainian-matrix.md) with the standard decision, source citations, initial consonant/subscript and vowel crosswalk, and explicit task ledger.
- Selected BGN/PCGN 1972 as the reference romanization standard. UNGEGN documents its 1972 approval as the UN-recommended Khmer system; the official PCGN guide provides the contextual consonant, subscript, vowel, diacritic and numeral tables.
- Existing @gmana/km-translit 0.1.2 remains a BGN/PCGN-derived ASCII approximation, not the complete standard: it drops diacritics and does not claim full conformance. The current romanization UI is retained but is not upgraded to a full standard implementation by this documentation change.
- Important gap: no independent romanization → Ukrainian syllable adapter exists yet. Do not imply that the romanization card already produces a Ukrainian orthographic-mode result. The current IPA → Ukrainian route remains independent.
- Task statuses: KHM-ROM-STD-001 DONE_VERIFIED (source review); KHM-ROM-ENGINE-001 PARTIAL; KHM-ROM-UA-001 TODO; KHM-ROM-MATRIX-001 PARTIAL; KHM-ROM-TEST-001 TODO; contextual IPA and independent lexical/audio gold remain PARTIAL.
- Branch: work/romanization-matrix-completion-20261031. No runtime code changed in this checkpoint; no new test result is claimed.


## BGN/PCGN Khmer consonant crosswalk checkpoint — 2026-10-31

- Added data/khmer/romanization_ukrainian.csv with the 22 official PCGN 2017 consonant/subscript table rows. Each row carries exact source-unit sequences, BGN/PCGN romanization, Ukrainian candidate/status, official PCGN URL and row-level locator. Row 18 records that ឡ has no subscript form; no extra ឝ row is claimed.
- Added tests/test_romanization_matrix.py. It checks all 22 official row IDs, exact Khmer source-unit sequences, romanization and Ukrainian candidate fields, provenance, locators and evidence statuses. It deliberately does not treat the CSV as a complete vowel/rime inventory.
- Source reconciliation: the first draft used an incorrect row transcription and an ASCII apostrophe. Inspection of the official PCGN 2017 PDF (page 2 table and notes) showed the apostrophe marker is U+2019 and corrected rows include 8/9 (ឋ/ឍ and ថ/ធ), 12/13 (ប and ព), and 18 (ឡ/ល). The data and test now assert the official source, not the earlier draft.
- Exact-head verification: workflow [41229686270](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41229686270) completed successfully: pytest 84 passed / 25 subtests passed; npm run check passed; production build passed.
- KHM-ROM-ONSET-001 is DONE_VERIFIED for the 22-row PCGN consonant/subscript table; this is a bounded consonant-table acceptance, not whole-language romanization coverage. KHM-ROM-MATRIX-001 remains PARTIAL: contextual vowel signs, shortening, anusvara/visarga, diacritics and numerals still need a source-exact data matrix and Ukrainian adjudication.


## Two-method result UI checkpoint — 2026-10-31

- Added an accessible two-button method switch to the service: **Фонетичний** and **За романізацією**. The default remains phonetic.
- The phonetic panel contains IPA, Ukrainian phonetic output, unit-level IPA/UA analysis and phonetic issue notices.
- The romanization panel contains the current BGN/PCGN-derived Latin output and a clearly labelled PARTIAL Ukrainian crosswalk state linked to the canonical research matrix. It does not reuse IPA or the phonetic Ukrainian output as a fallback.
- Test-first RED: workflow [41229998528](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41229998528) failed because the required mode controls/panels did not exist.
- Exact-head GREEN: workflow [41230217547](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41230217547) passed: pytest 84 passed / 25 subtests passed, npm run check and production build.
- The UI now separates the methods, but the Khmer Latin output is still the @gmana ASCII simplifier (diacritics omitted), and the independent syllable-level BGN/PCGN → Ukrainian adapter remains TODO. The romanization tab exposes that limitation rather than pretending it is complete.


## Final repository and Pages checkpoint — 2026-10-31

- Main commit: a351b0f66a608d7b4372e7c7bd0179808488be70 (PR #68, dual-method tabs).
- The final audit register records the source-corrected PCGN 2017 consonant matrix and the separate romanization/phonetic UI contract.
- Main quality workflow [41230505480](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41230505480) passed.
- GitHub Pages deployment [41230505474](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41230505474) succeeded: https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/ .
- Final statuses: KHM-ROM-STD-001 DONE_VERIFIED; KHM-ROM-ONSET-001 DONE_VERIFIED; KHM-ROM-ENGINE-001 PARTIAL; KHM-ROM-MATRIX-001 PARTIAL; KHM-ROM-UA-001 TODO; KHM-ROM-TEST-001 PARTIAL; phonetic independent lexical gold BLOCKED (none supplied/adjudicated).
- The website exposes two separate methods, but the romanization route's Ukrainian result is intentionally PARTIAL. Do not call the romanization mode complete until the full context-sensitive source → BGN/PCGN → Ukrainian syllable matrix and adapter are implemented and tested.


## Romanization evidence inventory continuation — 2026-10-31

- User confirmed the two-method contract: orthographic BGN/PCGN romanization → Ukrainian table adapter is independent from phonetic IPA → Ukrainian adaptation; romanization mode is intended to cover the supported orthographic inventory, while phonetic output may be partial/unsupported.
- Added `data/khmer/romanization_vowels_ukrainian.csv` with **37 source-located PCGN table entries**: 12 independent-character rows, 17 dependent-vowel rows, and 8 vowel + anusvara/visarga combinations. The independent-character column is sparse in the shared 22-row table. The data preserves PCGN alternatives, consonant-series/shortening context, candidate Ukrainian values, and explicit `PROPOSED`, `ANALYSIS_DEPENDENT`, or `EVIDENCE_LIMITED` statuses. Rows without an adjudicated target have an empty candidate; no missing value was guessed.
- Added `data/khmer/romanization_marks_numerals.csv` with all 6 PCGN diacritic rows and 10 numeral rows, plus `tests/test_romanization_marks_numerals.py`. These preserve series-changing and silent-mark behavior and map Khmer numerals to Arabic digits.
- Added `tests/test_romanization_vowel_matrix.py` to verify row counts, unique section/row identifiers, official source URL/locators, allowed evidence statuses, and the no-candidate invariant for `EVIDENCE_LIMITED`.
- Existing 22-row consonant/subscript matrix and its tests are preserved. This expands machine-readable evidence; it does **not** implement the PCGN romanization engine or the BGN/PCGN syllable → Ukrainian runtime adapter.
- Status: KHM-ROM-VOWEL-INVENTORY-001 = implementation added, CI verification pending; KHM-ROM-ENGINE-001 remains PARTIAL; KHM-ROM-UA-001 remains TODO; full context-sensitive vowel coverage and independent Khmer IPA gold remain PARTIAL/BLOCKED.
- Branch: `work/romanization-evidence-completion-20261031`. Changes are isolated from `main`; do not mark the new tests DONE_VERIFIED until the exact PR-head workflow passes.


## PCGN vowel-table source correction — 2026-10-31

- Direct inspection of the official PCGN 1972 PDF (pp. 2–4) corrected the shared vowel table inventory: 12 independent-character entries occupy rows 3, 4, 7, and 14–22; 17 dependent-vowel entries occupy rows 1–17; together these span the shared 22-row table. The earlier draft's 13-item independent list was inaccurate and has been replaced.
- Added all six diacritic rows and ten numeral rows in `data/khmer/romanization_marks_numerals.csv`; notes for series-shifting, shortening, `rC`, positional inherent-vowel behavior and silent `◌៍` are retained as contextual rules, not letter substitutions.
- The first CI attempt [41232327611](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41232327611) exposed a missing `source_url` field in the vowel CSV (86 passed, one failed). The source URL has been inserted into all 37 rows; a fresh exact-head run is required before closing this checkpoint.


## Verified Khmer PCGN orthographic inventory — 2026-10-31

- Exact PR-head workflow [41232468242](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41232468242) checked out merge commit `a1ce5ff` containing head `49f595e4ea030c4b4726ed3335c4bf9d22863271` and passed: pytest **87 passed / 25 subtests passed**, `npm run check` passed (engine, runtime, register-shifter, and romanization checks), and Vite production build passed.
- The first failed attempt [41232327611](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41232327611) exposed the omitted source URL in the vowel CSV; all 37 rows now carry the official PCGN PDF URL and row locator. The exact-head verification branch was created from the corrected tree.
- `KHM-ROM-VOWEL-INVENTORY-001` is `DONE_VERIFIED` for the bounded 37-row source inventory; `KHM-ROM-MARKS-NUMERALS-001` is `DONE_VERIFIED` for six diacritic rows and ten numeral rows. `KHM-ROM-MATRIX-001` remains `PARTIAL`; `KHM-ROM-ENGINE-001` remains `PARTIAL`; `KHM-ROM-UA-001` remains `TODO`.
- This does not establish all contextual BGN/PCGN transformations, nor does it complete the syllable-level BGN/PCGN → Ukrainian adapter. Existing @gmana ASCII output still drops diacritics. No new live Pages deployment was needed for these source-data and test changes; existing Pages site remains https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/.
- Verification PR: [#71](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/71), branch `verify/romanization-evidence-20261031`. PR #70 contains the earlier attempt and is superseded by #71.


## Post-merge main checkpoint — 2026-10-31

- PR #71 merged by squash as `2b8c9d4869c1fa4f179c3a087057e44bf5ef213b`; this is the main-branch implementation merge SHA for the romanization evidence inventory.
- Exact code-verification workflow [41232468242](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41232468242) passed: 87 Python tests + 25 subtests; web checks and Vite production build passed. The exact code-verification run checked out head `49f595e4ea030c4b4726ed3335c4bf9d22863271`; subsequent changes before merge were documentation-only.
- The bounded source inventory and its tests are now on `main`. The overall orthographic matrix and runtime adapter remain incomplete; see the PARTIAL/TODO statuses above.
- No runtime behavior or Pages build inputs changed in this PR; the already deployed GitHub Pages site remains the existing public service. A new Pages deployment was not necessary for these data/documentation-only changes.


## PCGN composite vowel glyph correction — 2026-10-31

- A second visual inspection of the official PCGN PDF (especially page 4) found that some dependent-vowel and anusvara/visarga source glyphs had been simplified in the first CSV draft. The data now preserves the actual table forms, including preposed-vowel sequences (`េ◌ើ`, `េ◌ឿ`, `េ◌ៀ`, `េ◌ា`, `េ◌ៅ`) and the PCGN composite patterns in rows 3, 7 and 8 of the anusvara/visarga table.
- The implicit-vowel row now uses the PCGN placeholder `◌`, whose note defines it as any Khmer consonant or consonant + subscript, rather than the non-graphemic label `inherent vowel`.
- Extended `tests/test_romanization_vowel_matrix.py` to assert exact source glyph sequences for all 17 dependent-vowel and all 8 anusvara/visarga rows, in addition to the full 22-row numbering, source URL, locators and evidence statuses.
- This is a source-faithfulness correction to the bounded inventory; it does not change the BGN/PCGN romanization values or claim that the context-sensitive engine / Ukrainian adapter is complete. Exact-head CI pending.

- This checkpoint supersedes the earlier 38-row / 13-independent-vowel draft count: the source PDF contains **12** independent-character entries, **17** dependent-vowel entries and **8** anusvara/visarga entries, for **37** machine-readable rows. The full shared PCGN vowel table spans row IDs 1–22 across its independent and dependent columns.
- The diacritic/numeral test now asserts all six exact PCGN mark glyphs and all ten Khmer numeral glyphs, not just their counts.


## Exact-head verification blocker for final PCGN glyph correction — 2026-10-31

- Programmatic branch-content validation confirms 37 vowel/rime rows, all 37 official source URLs, all 37 exact source-glyph + BGN/PCGN value pairs, 16 diacritic/numeral rows, and no Ukrainian candidate on any `EVIDENCE_LIMITED` row.
- The latest exact-head Quality checks run [41233203184](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41233203184) remains `queued` (job 124631488043). A local `git clone`/pytest attempt is blocked by the execution environment's DNS error (`Could not resolve host: github.com`). Therefore the new exact-glyph assertions have **not** been reported as passed.
- The matrix records `KHM-ROM-VOWEL-INVENTORY-001` and `KHM-ROM-MARKS-NUMERALS-001` as `PARTIAL` pending exact-head CI. PR #75 contains the correction and is mergeable; merge does not imply CI passed. Re-run/confirm CI after the runner becomes available before promoting these rows to `DONE_VERIFIED`.


## Final main SHA and merged source correction — 2026-10-31

- The corrected PCGN source glyph inventory and exact-row tests were merged by PR #75 as `5959113931c2e08ac279f4e064fa14a669a96f87`; the subsequent ledger correction PR #76 merged as `799d66f2038053e03b3a1c82d33fec7bbef4bfc8`. This is the main head before this final handoff-only update.
- PR #75's exact-head workflow [41233203184](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41233203184) remains queued. The local clone attempt failed with `Could not resolve host: github.com`; no test pass is claimed for the latest exact-glyph assertions. The matrix correctly leaves the bounded vowel and marks/numerals tasks PARTIAL pending CI.
- Remaining acceptance: exact-head CI green; complete context-dependent BGN/PCGN engine; complete romanization-syllable → Ukrainian table and adapter; broader IPA gold and ambiguity tests. No runtime changes or new Pages deployment were made.


## Exact PCGN glyph inventory verification checkpoint — 2026-10-31

- Current main before this documentation checkpoint: `5f3a9184f61d2e6e559cde30767e8c681a995a68`; matrix status update commit: `37990bcaf9550d6d2d45506ae9f56eb7717c2a2f`.
- Previously queued exact-head workflow [41233203184](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41233203184) is now completed with conclusion `success`. Job `test` (ID `124631488043`) completed all steps successfully: Python dependency setup and tests, Node dependency setup, web checks, and site build.
- Updated `docs/romanization-to-ukrainian-matrix.md`: `KHM-ROM-VOWEL-INVENTORY-001` and `KHM-ROM-MARKS-NUMERALS-001` are now `DONE_VERIFIED` as bounded source-table inventories with exact-glyph/romanization assertions; `KHM-ROM-TEST-001` remains `PARTIAL` because broader mixed-script, punctuation, malformed-unit and ambiguity coverage is still outstanding.
- This CI result verifies the bounded PCGN inventory assertions only. It does **not** establish the complete contextual vowel × consonant-series × shortening × coda matrix, a conformant runtime PCGN engine, a complete Ukrainian syllable adapter, or phonetic IPA coverage.
- No runtime code or Pages build inputs changed; no new deployment is required for this documentation-only update. Existing live site: https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/.
- Next implementation priority remains the context-dependent Khmer vowel/rime matrix and a source-aware PCGN engine; do not replace evidence gaps with guessed Ukrainian candidates.


## Final handoff head reconciliation — 2026-10-31

- Audit-register update commit: `a74a33dc77d1180eab32dbe79688442458d65d40`.
- Latest verified mainline documentation commit before this handoff update: `a74a33dc77d1180eab32dbe79688442458d65d40`.
- Matrix, repository audit, and handoff agree that workflow [41233203184](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41233203184) passed exact PCGN glyph and romanization assertions. The bounded inventory tasks are DONE_VERIFIED; the contextual romanization engine, full matrix, Ukrainian syllable adapter and broader adversarial coverage remain open.
- No production runtime or Pages build input changed in this cycle; the prior successful Pages deployment remains the live site evidence.
- Next implementation work must use source-backed contextual PCGN rules and explicit unresolved states. Do not synthesize unsupported Ukrainian candidates or treat the inventory CI as phonetic validation.


## Exact CI log detail and current head — 2026-10-31

- The exact-head workflow [41233203184](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41233203184), job `124631488043`, was inspected at the log level, not only by job conclusion.
- Exact results: `pytest -q` → **87 passed, 25 subtests passed**; `npm run check` → all configured web-engine, runtime, register-shifter and romanization checks passed (including the sample romanization test); `npm run build` → Vite production build succeeded and emitted `index.html`, `system.html`, and the expected asset bundles.
- The CI log contains non-fatal Node `punycode` deprecation and npm install-script warnings; no configured step failed.
- Latest handoff update commit before this section: `27b30e3250c8f8c92899cd50c654b7cca673a32e`. Treat this as a documentation-only checkpoint; no runtime behavior or Pages artifact inputs changed.


## Final audit/handoff synchronization — 2026-10-31

- Repository audit now includes exact CI log counts in commit `c8f9ed80e2ea45f34fa5ac4c86ecf306fc7f0634`.
- Latest verified documentation head before this handoff update: `c8f9ed80e2ea45f34fa5ac4c86ecf306fc7f0634`.
- Exact inventory acceptance evidence: 87 pytest tests + 25 subtests, configured npm checks passed, Vite production build passed. No full linguistic coverage claim is made.
- The master handoff, romanization matrix and repository audit preserve the same remaining acceptance criteria: contextual PCGN rules and engine; independent Ukrainian syllable adapter; wider malformed/mixed-input tests; adjudicated IPA gold. No code or deployment change occurred in this documentation synchronization.


## Open styling PR reconciliation — 2026-10-31

- Rechecked open PR #64 (`design/khmer-layout-20261030`) against current `main` `b4de6b248660b50d320ab24e8d3348fb1226d178`: branch is diverged, 7 commits ahead and 22 behind; merge base is `20e2e6dc296829986e52672d96b8730687aaa42a`. Its changes touch `index.html`, `system.html`, `src/styles/main.css`, and add `tests/test_layout_contract.py`.
- PR #64 remains open and untouched. Do not merge blindly: the CSS and layout-contract test need to be ported onto a fresh branch from current `main`, followed by current Python/web/build and visual/mobile verification. No styling changes were cherry-picked in this checkpoint.
- This is independent from the now-verified PCGN glyph inventory; no new Pages deployment or runtime change is claimed.

 
## Responsive layout merge and verification — 2026-10-31

- PR [#78](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/78) was merged by squash as `3b6e08177f9c90dddb27e787cc7a6deaa015c33e`.
- The PR adds 53 lines of focused responsive CSS overrides in `src/styles/main.css`; existing method-switch, IPA fallback, source-card and status styles were preserved rather than replacing the stylesheet from the diverged PR #64.
- Exact PR-head Quality workflow [41234615041](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41234615041) completed successfully. The sole job passed setup, checkout, Python dependency installation, `pytest -q`, Node dependency installation, `npm run check`, and `npm run build`.
- PR #64 remains open and untouched: its branch is substantially diverged; only the responsive behavior needed here was ported. Do not merge its broader CSS wholesale.
- The merge is UI-only. No Khmer phonological coverage, BGN/PCGN runtime, Ukrainian syllable adapter, or gold IPA corpus is completed by this change. Research prototype status remains unchanged.
- Pages deployment after this merge has not yet been verified. Check the Pages workflow and deployed site before claiming the live site includes this CSS.


## Sentence-level source-preservation regression — 2026-10-31

- Added and merged PR [#80](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/80) as `14113b5d45bbd36e53510b24a6f48f565a54bcd0`.
- The runtime regression passes the supplied Khmer greeting sentence through `convert()` and asserts that the normalized source and the concatenated per-unit source spans are identical, preserving whitespace and punctuation. It also requires an explicit aggregate Ukrainian result or fail-closed marker.
- Exact-head Quality workflow [41238197962](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41238197962) passed Python tests, Node web checks (including the runtime regression), and Vite build.
- This is a segmentation/source-preservation check, not independent IPA gold or a claim that every word in the sentence has an established pronunciation. The aggregate converter remains deliberately fail-closed when any unit is unresolved.
- The latest Pages deployment [41237778259](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41237778259) succeeded for main commit `cb48d4c660d3e7f826c677d871654157914ae59c`; PR #80 adds tests only and does not change the deployed runtime.


### Reconciliation update — open layout PR #64 — 2026-10-31

- Rechecked PR #64 (`design/khmer-layout-20261030`) against current main `6be7a09bb02824cfba2a50f17fdfd16faa5605e8`: diverged, 7 commits ahead and 22 behind; merge base remains `20e2e6dc296829986e52672d96b8730687aaa42a`.
- The branch changes `index.html`, `system.html`, and replaces `src/styles/main.css` wholesale; it also adds `tests/test_layout_contract.py` with assertions coupled to the old CSS implementation. Those exact selectors are not a portable contract for the current stylesheet and need redesign before reuse.
- The responsive layout improvements required for the current interface were already ported in focused PR #78 (`3b6e08177f9c90dddb27e787cc7a6deaa015c33e`) and its exact-head CI passed. No unique engine behavior is present in PR #64.
- PR #64 remains open and untouched; no wholesale CSS replacement or brittle test was ported. The existing IPA/method-switch styles and newer source-aware behavior are preserved.


### Full-sentence fail-closed output contract — 2026-10-31

- PR [#83](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/83) merged as `4a2e29dad27c80f2185db645a3971afe6315e022`.
- The sentence regression now asserts the exact aggregate markers `⟦ВИМОВУ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧` and `⟦ТРАНСКРИПЦІЮ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧` for the supplied greeting. This confirms that the engine preserves the input but does not claim a complete IPA or Ukrainian transcription when lexical units are not established.
- Exact-head Quality workflow [41239297284](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41239297284) passed Python tests, Node web/runtime tests, and Vite build.
- This is an explicit expected limitation, not a successful phonetic result. Supporting the sentence requires source-backed contextual phonology and lexical evidence, not weakening the fail-closed rule.

## Full-sentence romanization integration — 2026-10-31

- Main head: \`076ffaa1523afa7cc9ec9b8c2ca8e3a83cea101f\` (PR #89).
- PR #87 added the supplied full Khmer greeting sentence to the romanization test. Exact-head Quality workflow [41240282424](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41240282424) passed: 87 Python tests + 25 subtests, configured Node web/runtime/romanization checks, and Vite build.
- PR #89 merged the bounded UI integration fix: \`src/main.js\` now passes the complete input string to \`khmerToLatin(data.source)\`, rather than manually splitting on whitespace and invoking the library token by token. This follows the package's documented whole-text contract for preserving whitespace and punctuation, and its handling of the Khmer repetition mark \`ៗ\` ([package documentation](https://www.npmjs.com/package/@gmana/km-translit)).
- The exact regression checks that the sample is converted out of Khmer letters/signs while preserving both Khmer sentence stops, spaces, and the exclamation mark. Exact-head Quality workflow [41241149726](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41241149726) passed Python tests, Node web checks, and the Vite production build.
- This does not solve dictionary-based word segmentation inside unspaced Khmer runs; the library explicitly documents that limitation. Nor does it complete conformant BGN/PCGN 1972 contextual romanization or the independent romanization-to-Ukrainian adapter.
- PR #88 was closed as superseded; it used a stale pre-main branch and an incorrectly escaped Unicode test assertion. PR #64 remains open and untouched because its branch is diverged and replaces the stylesheet wholesale.
- No new Pages deployment is claimed. The site remains a research prototype; contextual PCGN coverage, a source-backed Ukrainian syllable adapter, and independently adjudicated phonetic gold remain open.

## Short mixed-text Khmer romanization regression — 2026-10-31

- PR #92 merged as \`99638ea6758d1553f3853d163c4b42ad8fe0741d\`.
- The supplied short sample \`សួស្តី 123! ភាសាខ្មែរ។\` now has an explicit whole-text romanization test. It verifies conversion of Khmer letters and preservation of ASCII digits, spaces, exclamation mark and Khmer sentence-stop punctuation.
- Exact-head Quality workflow [41242382955](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41242382955) passed Python tests, Node web checks and Vite build.
- This is an input-integrity regression, not BGN/PCGN gold or evidence of complete word segmentation/Ukrainian adaptation. No runtime code changed and no new Pages deployment is claimed.


## Native numerals and mixed Latin sentence regression — 2026-10-31

- PR #94 merged as `48e5d6c05d4a6ade8019c853135b7e2f6d655591`. The sample `២០២៦ ABC-42, សួស្តី។` verifies that Khmer numerals remain visible or are rendered as Arabic digits, ASCII digits and Latin text survive, and spaces/comma/Khmer sentence-stop punctuation are preserved while Khmer letters are romanized.
- Exact PR-head Quality workflows [41242836968](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41242836968) and [41242823462](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41242823462) passed Python tests, Node web checks and Vite build.
- Combined with PR #92's ASCII-number short sentence and PR #89's full Khmer greeting sentence, the romanization route now has explicit coverage for spaces, punctuation, native and ASCII numerals, and mixed Latin text. This is input-integrity evidence only; it does not establish the correct BGN/PCGN numeral rendering, word segmentation inside unspaced runs, complete contextual PCGN conformance, or a Ukrainian romanization adapter.


## Main-head verification after Khmer mixed-text regressions — 2026-10-31

- Current `main` head: `1a6921fc75dd011bc8097f6636b8077fc7c59cff`.
- Exact-main Quality workflow [41243972009](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41243972009) completed successfully. Pages workflow [41243971788](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41243971788) also completed successfully; both build and deploy jobs passed, including the deployed-site/runtime smoke test.
- Main has explicit whole-text romanization regressions for the full Khmer greeting, short mixed-script input, ASCII numbers, native Khmer numerals, Latin text, spaces, commas and Khmer sentence-stop punctuation. The application passes the complete input to the romanization library rather than manually tokenizing by whitespace.
- The full greeting's phonetic route intentionally remains fail-closed where source-backed contextual phonology is missing. The romanization library's documented inability to segment dictionary words within unspaced Khmer runs is not repaired by these tests.
- This verifies whole-text input integrity and deployed artifact behavior, not full BGN/PCGN 1972 conformance, Ukrainian romanization adaptation, or independently adjudicated IPA gold.
- Open PR #64 remains untouched: it is a diverged wholesale layout/CSS rewrite; focused responsive improvements were already ported separately in PR #78. Do not merge #64 without a fresh rebase/port and current browser/visual verification.
- Remaining blockers: source-backed contextual PCGN rules/engine, independent syllable-level romanization → Ukrainian adapter, unspaced word segmentation, broader malformed-input parity and independently adjudicated phonetic gold. Research prototype status remains unchanged.


## Post-merge verification for PR #95 — 2026-10-31

- PR #95 merged as `28a9bbb909ca57735ceca92f262c2de9eeb43396`; it synchronizes current whole-text romanization and deployment evidence without changing application code.
- Exact post-merge Quality workflow [41246343908](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41246343908) passed. Pages deployment [41246343845](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41246343845) also passed, including the deployed-site/runtime smoke test. This is the current verified main head.
- The full/short sentence, mixed-script, native/ASCII numeral, whitespace and punctuation tests remain engineering/input-integrity coverage. The phonetic route remains fail-closed for unsupported contexts; this is not full PCGN conformance, word segmentation, Ukrainian adaptation or independently adjudicated IPA gold.
- PR #64 remains open, diverged by 35 commits behind current main and is not merged. Its 7-commit CSS/layout branch is preserved; focused responsive improvements remain in the merged PR #78.


## Whole-message mixed-script segmentation regression — 2026-11-01

- PR [#97](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/97) merged as `72e4644204c879f905ebaa20dddd2d00b6583d32`.
- Added a canonical adversarial case containing Khmer, Latin identifier, ASCII digits, Khmer numerals and punctuation, tab, CRLF, U+200B and an unsupported symbol.
- The test consumes the canonical fixture, requires exact reconstruction from `segment_syllables()`, confirms a supported Khmer example remains structurally established and confirms the unsupported symbol remains locally invalid/unsupported.
- Exact PR-head Quality checks [41289845696](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41289845696) passed: Python tests, web checks and production build.
- The fixture has `ipa: null` and explicit non-phonological provenance; it is structural/source-integrity evidence, not IPA gold or an accuracy benchmark row.


## Goruut comparator research — 2026-11-01

- Task `KHM-G2P-GORUUT-001`: `PARTIAL` (upstream availability/source triage only; runtime execution and quality validation pending).
- Inspected and pinned upstream Goruut commit `b224bde02151f8f86d0fe260804e4ca743bda620`; upstream README advertises Khmer Central, IPA output, word tokens and tone support, but no syllable tokens or tie bars and no number/date normalization. MIT applies to source code; embedded dictionary/model asset licenses remain unaudited.
- Recorded the candidate and limitations in `docs/benchmarking-and-external-ipa.md`, alongside a triage note for Khmer NLP KCC: its advertised G2P tokens are not established as IPA and its downloaded checkpoint/data need separate license review. PR [#98](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/98); exact PR-head CI [41302072416](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41302072416) passed before this handoff-only follow-up commit.
- No Goruut/KCC runtime invocation or output artifact was produced. Independent gold remains 0; no accuracy or winner claim. Next acceptance: run pinned Goruut in isolated optional CI, audit asset provenance, review Khmer register/inherent-vowel/coda/syllable conventions, and score only independent expert-adjudicated IPA.


## Goruut asset licensing reconciliation — 2026-11-01

- Task `KHMER-CENTRAL-G2P-GORUUT-001` remains `BLOCKED` for runtime execution, not merely PARTIAL: the source-code MIT license does not establish rights for the language-specific lexicon/model assets.
- The pinned Goruut source tree contains embedded files under `dicts/khmer/central/`; Goruut's own data-preparation documentation states these model assets derive from a `lexicon.tsv`. The corresponding separate `neurlang/dataset/khmer/central/` lexicon is present, but dataset repo metadata declares no license, root tree has no LICENSE/COPYING, and the README does not allocate a license/provenance to this language.
- No runtime invocation, output artifact, or quality claim is made. Next acceptance: per-language source/provenance and rights for both lexicon and derived weights, then owner-approved usage decision, followed by isolated pinned execution and independent expert IPA adjudication.
- Detailed evidence and exact upstream paths: `docs/audits/current/GORUUT-ASSET-LICENSE-REVIEW-2026-11-01.md`.


## External corpus/source triage — 2026-11-01

- Task `KHM-MEKONGPHON-001`: `PARTIAL` for discovery and evidence triage; external data import / benchmark gold remains `BLOCKED` pending source-specific rights and expert validation.
- MekongPhon LREC 2026 source triage is PARTIAL: the paper reports 1.3M Khmer orthography–IPA pairs; inspected GitHub main `f80f6c1840c4818b51e05f2e00cded4701a5b662` includes lexicon/train/eval files and a documented SEAlang/OPUS lexicon-based sentence conversion pipeline. Import remains BLOCKED: repository license is undeclared; sentence IPA is generated by greedy dictionary lookup with OOV sentences filtered; the committed split script reserves only 100 lexicon lines (seed 1234). A second lead, chemvatho/Khmer-acoustic-model, claims a 29,204-entry native-validated IPA dictionary and CC BY-SA 4.0 in README, but dictionary/README says CC BY 4.0 and the full dictionary is absent from the current tree (only six sample entries). Resolve rights and availability before use. Gold remains 0.
- No external corpus rows, IPA labels, model weights or audio were copied into the repository. No accuracy score or engine ranking is claimed.
- Full source register and acceptance gates: `docs/audits/current/EXTERNAL-PHONETIC-CORPUS-TRIAGE-2026-11-01.md`.


## KHM-GORUUT-RUNTIME-001 — PARTIAL

- Added an optional, test-only HTTP runtime probe for Goruut at pinned upstream commit `b224bde02151f8f86d0fe260804e4ca743bda620`. It explicitly enables `KhmerCentral` in `BuiltinDictLanguages`, builds the upstream Go binary and records raw JSON responses for source-attested lexical probes plus multiword/punctuation cases. `scripts/benchmark_goruut.py` records commit, language, input SHA-256, raw response, tokens and errors; it does not normalize or score IPA. Existing source-attested IPA remains non-gold. Accuracy=null; independent gold=0. Workflow: `.github/workflows/optional-goruut-runtime.yml`; artifact retention 30 days.
- Acceptance: exact-head optional workflow must pass; inspect raw output for language coverage, unknown-word behavior, punctuation, multiword segmentation, malformed/unicode cases and phonetic output consistency. Keep raw data and errors; do not normalize tone/length/diacritics.
- Status remains PARTIAL until runtime artifacts are inspected and language-specific expert gold exists. The test-only CI checkout is not a production dependency or data import.


## KHM-GORUUT-RUNTIME-001 — PARTIAL (runtime executed; not promoted)

- The pinned Goruut runtime was executed with KhmerCentral enabled (Go 1.23.12). Engineering probes returned 8/8 responses; 6 source-attested IPA probes returned 6/6, but only 1/6 was an exact NFC/whitespace concordance (not accuracy/gold). Clear incomplete outputs: `ខ្មែរ` → `kʰr` vs source `kʰmae`; `ភ្នំពេញ` → `pʰɲ` vs `pʰnum ˈpɨɲ`; `ភាសាខ្មែរ` → `pʰiəsaːkʰr` vs `pʰiəsaː kʰmae`. Server log repeatedly reports missing `weights9.bin.zlib`. Do not promote. Full evidence: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.
- Runtime/build/HTTP availability is verified for the returned probes. Phonetic accuracy, dialect coverage and IPA convention are not verified; independent expert gold remains 0.
- Acceptance to progress: investigate the repeated missing `weights9.bin.zlib` warning and raw outputs; resolve unsupported/empty responses; create a language-specific expert-adjudicated held-out IPA set; rerun and inspect exact artifacts. Production integration remains deferred until those gates pass.


## KHM-GORUUT-RUNTIME-001 — PARTIAL, repeatability evaluated

- Three-repeat re-evaluation: 8/8 engineering outputs and 6/6 source-attested probe outputs were stable across repeats; only 1/6 source-attested IPA rows matched exactly. Stable but incomplete outputs include `ខ្មែរ` → `kʰr` vs `kʰmae` and `ភ្នំពេញ` → `pʰɲ` vs `pʰnum ˈpɨɲ`. Stable execution does not offset the phonetic mismatch. This is not accuracy or gold.
- Production integration remains blocked by insufficient source concordance, missing/unsupported outputs or incomplete phonetic forms. Independent expert gold remains 0.
- Next acceptance: investigate upstream missing-weight warning and language-specific mapping; resolve every no-output and unstable-tone case; commission expert IPA gold; rerun the pinned artifact and retain raw evidence.


## Cross-engine comparator evidence — PARTIAL

- Cross-engine check: khmerphonemizer 0.0.3 returned 6/6 source-attested probes; 2/6 strict IPA strings and 6/6 limited-notation matches. Goruut returned 6/6 stable outputs but only 1/6 strict and 3/6 limited-notation matches. This small source-attested sample favors khmerphonemizer as a comparator, not as proven production phonology. No independent gold exists.
- No external result is accepted as independent gold. Production selection remains blocked pending expert adjudication and repeatable, dialect-scoped validation.


## KHM-GORUUT-RUNTIME-001 — PARTIAL (exact-head evidence recorded)

- Exact PR #101 head `eeeede50447c41df30f866bcbf77f56824b40190` runtime build and HTTP probe passed: [41310808284](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41310808284); artifact SHA-256 `34330aac3be84a438a7bdc181d715f12b745cfe6f7e15edcd4be08dcbfeb52da`.
- Three-repeat results: engineering 8/8 stable; source-attested 6/6 stable; strict concordance 1/6 and limited notation diagnostic 3/6. Stable missing-segment outputs are present; not accuracy, gold=0.
- Missing `weights9.bin.zlib` warning persists; causal relation unknown. Keep as optional comparator only; production promotion rejected.
- Full run evidence and config hash: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.


## Goruut nondeterminism root-cause finding — Khmer

- The latest artifact had no RandomizationWordsCount / RandomizationWordsChoices metadata on any of the 14 inputs; all 14 were stable across three repetitions. Its problem is different: stable but incomplete dictionary output (e.g. missing vowels), not the homograph-selection instability observed in Lao/Burmese.
- Upstream pinned selector counts homographs and falls back to a random dictionary pronunciation when no preferred entry is selected; response counters are `RandomizationWordsCount` and `RandomizationWordsChoices`. See [selector source](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/repo/services/parts_of_speech_selector_service.go#L168-L205).
- Missing `weights9.bin.zlib` is a separate warning; causality is not established.


## KHMER Goruut source-coverage gate — PARTIAL

- Raw runtime evidence was re-analysed using `PrePunct`, `CleanWord`, and `PostPunct`; non-empty phonetic output is not sufficient evidence of complete coverage.
- - Runtime workflow: [41311611360](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41311611360); artifact [13085627015](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41311611360/artifacts/13085627015); ZIP SHA-256 `30988a1aae36261f94319286c0815b184f5effb633527f79d07e6011334d19aa`.
- - Input SHA-256 `3d93a49c0162b5de4374c51d742fab0d2f5f975251c09664faefc9870535df49`; engine `b224bde02151f8f86d0fe260804e4ca743bda620`; Go `1.23.12`; config SHA-256 `d2f19f923da8ca089ba9133465018903263f681b57a1177152ab07f2a284225e`.
- - 97/100 inputs returned at least one phonetic token; 3/100 returned an empty Words array. Of the 97 responses, 96 were stable across three repetitions and one (`ជួត`) was unstable.
- - Source coverage was independently re-analysed from `PrePunct`, `CleanWord`, and `PostPunct`. A row counts complete only if these fields reconstruct the original input after NFC/whitespace removal and no letters, combining marks or numbers are relegated to PrePunct/PostPunct. Result: **70/100 complete**, **27/100 partial**, **3/100 no output**. This is a source-preservation check, not a phonetic correctness score.
- - 27 partial cases include examples where the engine emits only a suffix or prefix as phonetic output and stores remaining Khmer letters in punctuation fields, e.g. `បេះបិទ` → CleanWord `ទ`, PrePunct `បេះបិ`, Phonetic `t`; `ថួន` → CleanWord `ន`, PrePunct `ថួ`, Phonetic `n`. The API's non-empty Phonetic response therefore substantially overstates usable coverage.
- - Strict source-attested concordance: **6/100 (6%)**; limited notation diagnostic: also 6/100. These are not accuracy or gold agreement. The source field is MekongPhon's generated `pron_no_tones`, not independent expert gold.
- - The one unstable input `ជួត` carried `RandomizationWordsCount=1`, `RandomizationWordsChoices=2`; the other 99 did not show that metadata.
- The benchmark harness now has tests for dropped source characters and source letters in punctuation fields; exact-head CI is still pending. No accuracy score or production promotion is claimed.
- Full evidence: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.


## Owner scope decision — temporary test-only use — 2026-11-01

The repository owner explicitly directed that external Goruut assets may be used for temporary verification and comparison without blocking these tests on license review. Accordingly:

- **Test-only execution:** authorized for this research task; do not stop runtime probes because the external asset license is unresolved.
- **No data/model import:** no Goruut dictionary, model weight, or MekongPhon source row is copied into the product runtime or committed as a corpus by this decision.
- **Production packaging or redistribution:** not authorized by this instruction and remains outside this test-only scope; asset provenance/rights must be revisited before any bundling, redistribution, or production deployment.

This is a project scope decision, not a legal conclusion about the upstream assets.


### Khmer source-coverage repeat-run evidence

## Re-run with source-coverage and randomization counters — 2026-11-01

The updated harness completed on PR branch commit `b9f706473e4e03c6e446254703b7e6e09d863cce`: [runtime workflow 41312379618](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41312379618), artifact [13086660287](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41312379618/artifacts/13086660287), ZIP SHA-256 `dd6934c304e802bf5aabbce2802a92c11855e8a0e3d37d05b7ca7f19b12d41e4`.

- The 100-row MekongPhon report independently reproduces **70 complete / 27 partial / 3 no-output** source-coverage results; 96 outputs were repeat-stable, one was unstable. The unstable word carried dictionary-randomization metadata in all three repetitions.
- Strict source-attested concordance remains 6/100, with 6/100 on the limited notation diagnostic. Accuracy remains null; independent gold remains 0.
- The eight engineering probes that were previously described as 8/8 successful responses are now correctly classified as **3 complete and 5 partial**. All eight had non-empty phonetic output, but five did not preserve the full source word through CleanWord/PrePunct/PostPunct.
- The six-row source-attested sample is 3 complete / 3 partial; its strict 1/6 and notation-only 3/6 matches are not accuracy.

This confirms the coverage gate is functioning on a real 100-row run. The current PR head adds an additional empty-phonetic-token guard and associated tests; final exact-head CI remains pending.



## Final Goruut / Khmer G2P PR #101 reconciliation — 2026-11-01

- Final head `1e9cbfdf4f21514e4f39093d51ea3f923133a90a`: repository checks [41313433562](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41313433562), Khmer G2P [41313433619](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41313433619) and Goruut [41313433641](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41313433641) all **PASS**.
- Khmerphonemizer 0.0.3 returned 100/100 outputs, but 0/100 rows were comparable because the input split provided no source IPA labels. This is an availability result only, not accuracy.
- Goruut 100-row results: 97 outputs, 3 no-output; source coverage 70 complete / 27 partial / 3 unknown; 96 stable / 1 unstable; one randomized dictionary input; strict source-attested concordance 6/100. The eight engineering probes had 3 complete and 5 partial outputs. Accuracy remains null, independent gold=0.
- Artifacts: Khmerphonemizer [13086870731](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41313433619/artifacts/13086870731), SHA-256 `86ef634b67dd60ca121cfe11a8549a42e7ee2e4655447851e91a4eefffb7a1b2`; Goruut [13085864084](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41313433641/artifacts/13085864084), SHA-256 `469bd4f9fc0baa3e8366724e43dfcb802427eca3d70c916be1e98ff6d779583d`. Both downloaded archive hashes matched GitHub's digest.
- Runtime-probe code and exact-head CI are **DONE_VERIFIED**. Goruut production use remains rejected. Khmerphonemizer accuracy and production suitability remain **BLOCKED** until an appropriate source IPA set and independent expert adjudication exist. The `weights9.bin.zlib` warning is unresolved; causality is not established.


## Khmer source-IPA comparator correction — 2026-11-01

The previous addendum's statement that the 100-word MekongPhon split lacked IPA was incorrect. The workflow included `pron_no_tones` under `source_reported_ipa`; the benchmark runner read only `ipa`, silently dropping the reference labels. I added a regression test first and observed the intended failure on [41325025559](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325025559): 1 failed, 106 passed, 25 subtests. The minimal fix, `source_ipa_from_metadata`, now supports both field names.

Final head `1a0a8190e60d003b2e48ac29da21ce553822130c` passed repository CI [41325152300](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325152300) and [41325147911](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325147911), plus optional G2P run [41325147987](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325147987). Corrected artifact [13091145662](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325147987/artifacts/13091145662), SHA-256 `b3e2262c5f72d51c770ec88c3cf880387d1aa03ab5bc4beafc85e0551ec1f2f9`, reports 100/100 outputs, 100 comparable source labels, 18 strict matches and 19 limited-notation matches. These are not accuracy: gold=0, accuracy=null.

The earlier 0-comparable count is superseded. The bug was in our report adapter, not absent source data. The fix is a research-harness correction only; no production phonology changed.


## Final Khmer run reconciliation — PR #101

Final-head repository checks [41325417322](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325417322) and [41325414211](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325414211), Goruut [41325417330](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325417330) and corrected Khmerphonemizer [41325417374](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325417374) all passed. Goruut artifact [13090873861](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325417330/artifacts/13090873861): 97/100 outputs, 70 complete / 27 partial / 3 unknown, 96 stable / 1 unstable, 6/100 source-attested exact matches. Khmerphonemizer artifact [13091310659](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325417374/artifacts/13091310659): 100/100 outputs, 100 comparable source labels, 18 strict and 19 limited-notation matches after fixing the dropped `source_reported_ipa` field. Both archive hashes match GitHub digests. These are source concordance only, not accuracy; independent gold=0, accuracy=null.


## Session closeout — 2026-11-01

- PR [#101](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/101) was reviewed and squash-merged into `main` as `211a5273a0bebc8b95bee7c821ec3aa63ebcfa60`; the main branch head was verified to equal that SHA.
- Post-merge quality checks [41326232442](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41326232442) PASS; optional G2P smoke [41326232443](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41326232443) PASS; GitHub Pages build/deploy and deployed-site/runtime smoke test [41326232421](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41326232421) PASS.
- Final PR-head Goruut runtime [41325808140](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325808140) PASS; artifact [13091003881](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325808140/artifacts/13091003881), SHA-256 `079c6e56ad178815bba2159ec4720f538b01071a17cb1d030fcf4d024f8696f2`: 97/100 outputs, 70 complete / 27 partial / 3 unknown, 96 stable / 1 unstable, 1 randomized input, 6/100 strict source-attested matches. The 8 engineering probes had 3 complete / 5 partial.
- Corrected Khmerphonemizer 0.0.3 comparison [41325808089](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325808089) PASS; artifact [13090603852](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41325808089/artifacts/13090603852), SHA-256 `668668bb1a6a3aca45145b0894c83000889695e6d25878d794622fef64e5e5d2`: 100/100 outputs, 100 comparable source labels, 18 strict and 19 limited-notation matches. This follows the test-first fix for the dropped `source_reported_ipa` metadata field (red CI: 1 failed, 106 passed, 25 subtests; final CI passed).
- Goruut test harness and exact-head CI: **DONE_VERIFIED**. Production phonology remains **PARTIAL/BLOCKED**: 27/100 Goruut outputs partial, 3/100 absent; source labels are not independent gold; independent expert Khmer IPA gold remains 0. Khmerphonemizer concordance is diagnostic only. Permanent source-data/model import remains outside the approved test-only scope.
- No local checkout was available; engineering verification is from exact-head and post-merge GitHub Actions. See runtime audit for full evidence and hashes.


## Linguistic completion register — 2026-11-01

- Current verified `main` baseline: `c0a2b33c86791b6546e1158c62043fd23acc1f60`; latest exact-main engineering workflow: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41326462947 (success). See the linked current audit register for the verified status and next acceptance criteria: [Linguistic completion register](audits/current/LINGUISTIC-COMPLETION-REGISTER-2026-11-01.md).
- Reconfirmed `data/benchmark/gold.tsv` contains only its header. Independent expert-adjudicated lexical IPA gold remains **0**; empirical accuracy remains **null**. No external source-attested labels or engine outputs are promoted to gold.
- The register separates implementable repository work from external expert, primary-source and licensing blockers. Preserve existing canonical plans, registries, tests and generated data; do not create parallel corpora or weaken fail-closed behavior.
- No local checkout was available for this pass. GitHub Actions provide exact-main engineering evidence only; they do not prove linguistic accuracy, manual accessibility QA or legal permissions.
## Current master-matrix status override — 2026-11-01

The following current statuses supersede older checkpoint rows above where they conflict; historical evidence remains preserved.

| Task | Current status | Current acceptance boundary |
|---|---|---|
| KH-TEST-001 | BLOCKED | Gold TSV is header-only; independent expert-adjudicated lexical IPA gold=0; accuracy=null. Requires independent annotation, adjudication, profile and source/audio locators. |
| KH-VOW-001 / KH-VOW-002 | PARTIAL | Orthographic/register inventory exists; full context-dependent vowel/rime/series matrix and acoustic/phonetic adjudication remain open. |
| KH-CODA-001 | PARTIAL | Structural cases and fail-closed behavior exist; full coda-conditioned IPA coverage remains open. |
| KH-IPA-001 | PARTIAL | IPA boundary/status contract exists; complete contextual orthography-to-IPA model and gold remain open. |
| KH-PROFILE-001 / KH-PROFILE-002 | PARTIAL | Fail-closed guards are verified; complete Phnom Penh /r/-loss environment model and expert validation remain open. |
| KH-G2P-001 | DONE_VERIFIED (harness only) | Goruut and Khmerphonemizer comparisons are diagnostic; no accuracy claim or production promotion. |
| KH-ROM-001 | PARTIAL | BGN/PCGN bounded inventory exists; full contextual runtime and independent Ukrainian syllable adapter remain open. |
| KH-UI-001 | TODO | Manual deployed visual, keyboard, screen-reader and mobile QA not evidenced by CI. |
| KH-REL-001 | PARTIAL | Release remains blocked by phonological gold and asset-rights review. |


## IPA gold corpus implementation checkpoint — 2026-11-01

### Current task ledger

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-GOLD-SCHEMA-001 | DONE_VERIFIED | Six versioned JSON Schemas; empty JSONL templates; validator and regression tests in exact-head CI |
| IPA-GOLD-DOUBLE-ANNOTATION-001 | PARTIAL | Enforces two distinct annotators and third independent adjudicator; actual blind collection needs qualified human annotators and controlled intake |
| IPA-GOLD-ADJUDICATION-001 | PARTIAL | Agreement/resolved/unresolved semantics and rationale validation implemented; no real adjudicated rows exist |
| IPA-GOLD-SPLIT-001 | DONE_VERIFIED | Deterministic SHA-256 split assignment, preserves frozen assignments, prevents lexeme-group leakage; current manifest empty |
| IPA-GOLD-EXPORT-001 | DONE_VERIFIED | Exports only adjudicated, redistributable rows into existing benchmark TSV; current export has header only |
| IPA-TYPED-BENCHMARK-001 | DONE_VERIFIED | PHONEMIC / PHONETIC_BROAD / PHONETIC_NARROW retained; type mismatch cannot count as exact match |
| IPA-GOLD-RELEASE-GATE-001 | PARTIAL | Tag/manual workflow requires 100/25/25 adjudicated split rows and rights; owner must require the check in release rulesets/procedure |
| KHMER-VOWEL-CONTEXT-001 | PARTIAL | Research workpack requires sign × series × length × coda × profile matrix and source/audio locators |
| KHMER-CODA-001 | PARTIAL | Existing structural cases retained; full coda-conditioned surface IPA and acoustic validation remain open |
| KHMER-R-LOSS-001 | PARTIAL | Wayland & Guion (2005) and Kirby (2014) located; /r/-loss must remain profile/style-conditioned, with matched multi-speaker evidence |
| KHMER-UA-IPA-ADAPTER-001 | PARTIAL | Existing adapter retained; independent expert target review awaits adjudicated surface IPA |

### Evidence boundary

The four JSONL files are empty templates. `gold.tsv` is header-only; independent expert gold=0 and accuracy=null. Wayland & Guion's study describes two Phnom Penh speakers and a specific colloquial /Cr/ environment; it does not justify universal /r/ deletion. No IPA labels were added.

See [IPA gold protocol](docs/ipa-gold-corpus.md), [Khmer phonology workpack](docs/audits/current/PHONOLOGY-RESEARCH-WORKPACK-2026-11-01.md), and [evidence registry](docs/evidence.md).

### Additional rights and export controls

| Task | Status | Acceptance / remaining work |
|---|---|---|
| IPA-GOLD-RIGHTS-001 | DONE_VERIFIED (mechanism) | Approved license registry, per-record rights evidence, rejection of unregistered/non-redistributable licenses; legal verification of future source-specific records remains required |
| IPA-GOLD-PROVENANCE-EXPORT-001 | DONE_VERIFIED | Gold TSV and benchmark rows retain source ID, license ID and rights-evidence locator |
| IPA-GOLD-BLIND-INTAKE-001 | BLOCKED | Requires external controlled intake; public GitHub history cannot provide blind annotation |

The rights registry does not itself grant permission. Each real source still needs its exact license/permission verified by a responsible curator, and share-alike/attribution terms must be honored in distribution.


### 2026-11-01 follow-up — validator and Khmer research evidence

- IPA-GOLD-SCHEMA-001 remains DONE_VERIFIED (mechanism), now with runtime/schema parity checks: closed object properties, mandatory annotation notes, string uncertainty arrays, ISO dates and optional field types.
- IPA-TYPED-BENCHMARK-001 remains DONE_VERIFIED (mechanism): adjudicated gold requires a valid IPA kind; missing/different prediction kinds cannot score as exact matches or enter CER.
- Wayland & Guion (2005) is a two-speaker, 20-item, three-repetition-per-style Phnom Penh study; its /r/-loss findings remain profile- and speech-style-conditioned. Kirby (2014) provides complementary production/perception evidence. Chem & Chem (2020) is a Phnom Penh acoustic vowel source, not yet a complete contextual matrix.
- Independent expert gold remains 0; gold.tsv remains header-only. No IPA entries or universal /r/-loss rule were invented.


### Research artifact — Khmer

- [KHMER vowel × series × coda evidence matrix](docs/audits/current/KHMER-VOWEL-SERIES-CODA-EVIDENCE-MATRIX-2026-11-01.md): specialist ɑ/ɔ-class mappings, Chem (2020) sample/method and coda effects, and missing contextual cells.
- Wayland & Guion's /r/-loss remains restricted to the studied Phnom Penh colloquial profile; no universal deletion rule was introduced.


## 2026-11-01 implementation and verification closeout

- Starting main SHA: c0a2b33c86791b6546e1158c62043fd23acc1f60 (main remains unchanged).
- Implementation branch: feat/ipa-gold-corpus-20261101-review.
- Comprehensive PR: [#103](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/103); PR-head implementation checkpoint SHA: 608d2d92c5e883c095bf0c679b7353bd442ee55c.
- PR CI: [Quality checks](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41337410745) SUCCESS — 136 Python tests + 27 subtests; Khmer register-shifter browser contract, web checks and Vite build passed.
- This branch includes the previous documentation-only PR #102 in full; #102 was closed as superseded after its content was verified in #103. No branch was deleted.
- Legacy PR [#64](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/64) remains open and untouched: it is a divergent legacy CSS/layout patch and was not blindly merged.
- Existing feature branch feat/independent-ipa-gold-corpus-20261101 was left untouched because its history is substantially broader; the narrower review branch is the PR source.
- No local checkout was available; all verification claims above are GitHub Actions evidence, not local command runs.

### Final task ledger

- Corpus schemas/runtime validator, license registry, frozen group-safe splits and typed benchmark: DONE_VERIFIED (implementation and CI only).
- Actual independent expert annotations and adjudicated gold: BLOCKED — no qualified annotators or adjudicated source dataset supplied; gold.tsv remains header-only, gold count 0, accuracy null.
- Full vowel × consonant-series × final matrix and independent /r/-loss replication: PARTIAL/BLOCKED — see the Khmer evidence matrix; Chem's four-speaker Phnom Penh sample and Wayland & Guion's two-speaker /r/-loss sample are profile-limited.
- Release gate: PARTIAL — count, rights, adjudication and split checks exist and fail closed on empty gold; project owner must require the gate in repository rulesets/release procedure, and feature-coverage thresholds require an expert-approved matrix.
- Manual UI/accessibility review: TODO.

**Readiness:** research infrastructure is substantially improved; the language system remains a research prototype, not production/release-ready.


The Khmer evidence matrix now contains the full Ishida phone-to-grapheme mapping table, including stress, coda and final-conditioned variants. Chem's acoustic evidence still does not fill every series × vowel × coda cell, so the language model remains PARTIAL.


## 2026-11-01 final IPA-kind consistency verification

- Added fail-closed cross-annotation consistency: both independent annotations for one record must use the same `ipa.kind`, and a `RESOLVED` adjudicated result must preserve that kind. This prevents phonemic-vs-phonetic representation differences from being misclassified as pronunciation disagreements.
- Regression evidence: both new tests failed against the pre-fix validator on the test-only commit, then passed after the validator change.
- New task `IPA-GOLD-REPRESENTATION-KIND-001`: **DONE_VERIFIED** (mechanism and exact-head CI). Blindness, annotator qualifications and independent adjudicator competence remain external operational evidence, not properties CI can prove.
- Final PR head: `f7f2bf9a471f5fea990c0cf9509d382e3371d17b`; CI run [41338461515](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41338461515) SUCCESS — 139 Python tests + 27 subtests; browser register-shifter contract, web checks and Vite build passed.
- The Khmer matrix remains PARTIAL: full profile × series × stress × coda lexical coverage and an independent broader /r/-loss replication are not available.
- Gold remains zero; `gold.tsv` remains header-only; empirical accuracy remains null. No IPA labels were generated.


## CI action runtime modernization — 2026-11-01

- Status: `DONE_VERIFIED` (CI maintenance only; no Khmer phonology or transcription behavior changed).
- Updated all five workflow files to current Node.js 24-compatible action majors: `actions/checkout@v7`, `actions/setup-python@v7`, `actions/setup-node@v7`, `actions/setup-go@v7`, and `actions/upload-artifact@v7`. Existing Pages actions remain at `configure-pages@v6`, `upload-pages-artifact@v5`, and `deploy-pages@v5`.
- Tested code commit: `61d98b1417a6d0200df4722523e8caeae90269fd`.
- Exact-head verification: [Quality checks 41339636053](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41339636053) SUCCESS; [optional Goruut 41339636042](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41339636042) SUCCESS; [optional G2P smoke 41339636117](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41339636117) SUCCESS.
- Verified workflow coverage: 139 Python tests + 27 subtests, browser register-shifter contract, web checks and Vite production build passed on the exact code commit.
- Local checkout was unavailable; verification evidence is GitHub Actions. The gold corpus remains empty and empirical accuracy remains unmeasured.


## Frozen split-manifest schema parity — 2026-11-01

- Status: `DONE_VERIFIED`.
- Review found that `assign-splits` accepted unknown properties in existing split rows even though the split JSON Schema is closed; the generator could silently discard those fields when rewriting the manifest.
- RED evidence: regression `test_assign_splits_rejects_unknown_properties_in_existing_manifest` failed as expected on test-only commit `3fdfd9559dfc98c43c4c503b9e707f1632ebad07` ([run 41340259859](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340259859)).
- GREEN implementation: shared `SPLIT_PROPERTIES` is now used by both cross-file validation and `assign-splits`; the generator rejects unknown fields instead of dropping them. Code commit: `64851a4572437d9185b47fcff56bde55e4f092c5`.
- Exact-head verification: [PR Quality checks 41340405233](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340405233) SUCCESS and [push checks 41340400309](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340400309) SUCCESS — 140 Python tests + 27 subtests; browser register-shifter contract, web checks and Vite production build passed. Optional Goruut and G2P smoke checks also passed on this head.
- Shared implementation and regression test are byte-identical across Lao, Khmer and Burmese branches. No corpus rows or IPA labels were added; independent gold remains zero and accuracy remains null.


## Product-corpus license eligibility — 2026-11-01

- Status: `DONE_VERIFIED` (policy enforcement; no source corpus or license grant was changed).
- Review found that the license registry accepted `redistributable: true` together with `commercial_use: false/null` or unknown attribution/share-alike terms. That could make a non-commercial or legally incomplete entry eligible for the product corpus if the registry were misconfigured.
- RED evidence: the new runtime and schema-contract tests failed on test-only commit `83cfdc10716eff99f622f5d0e3c9c035bee3b56e` ([run 41340790159](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340790159)).
- GREEN implementation: a redistributable license must explicitly set `commercial_use: true` and boolean `attribution_required` + `share_alike`; the JSON Schema now encodes the same conditional rule. Code/schema commit: `b3104d6815edb3950e13457f7e04bcb8f5f90145`.
- Exact-head verification: [PR Quality checks 41340930079](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340930079) SUCCESS and [push checks 41340925788](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41340925788) SUCCESS — 142 Python tests + 31 subtests; browser register-shifter contract, web checks and Vite production build passed. Optional Goruut and G2P smoke diagnostics also passed.
- This is a conservative product-corpus eligibility rule, not a legal opinion about all uses of these licenses. Each real source still needs human rights review. No IPA gold rows were added; independent gold remains zero and accuracy remains null.


## Release-gate threshold validation — 2026-11-01

- Status: `DONE_VERIFIED`.
- Review found that the CLI accepted zero/negative `--min-train`, `--min-dev` and `--min-test` thresholds. That could let an operator weaken a release gate below a meaningful non-empty split requirement.
- RED evidence: the six invalid threshold cases (0 and -1 for each split) failed as expected on test-only commit `888ce85258e0c42b44e082e06023dbcd96401b96` ([run 41341526589](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41341526589)).
- GREEN implementation: all three minimums must be positive integers. Invalid threshold configuration is added to the gate's aggregated findings rather than raised before corpus checks, preserving diagnostics for other blockers. Final code commit: `38aed74299c898461607407b730085e1b70d565d`.
- Exact-head verification: [PR Quality checks 41341743668](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41341743668) SUCCESS — 143 Python tests + 37 subtests; browser register-shifter contract, web checks and Vite production build passed.
- The configured release-gate defaults remain train=100, dev=25, test=25. No gold rows or IPA labels were added; independent gold remains zero and accuracy remains null.


## Controlled IPA gold acquisition checkpoint — 2026-11-01

- Added `docs/ipa-gold-collection-playbook.md` on `feat/ipa-gold-corpus-20261101-review`. This defines a human-led 30-lexeme process pilot, one predeclared pronunciation profile and IPA convention per corpus version, a curator, two blind independent annotators, and a third independent adjudicator. It sets explicit start/pilot-accepted/benchmark-ready gates and distinguishes pilot data from held-out evaluation.
- This is a protocol/documentation deliverable, not evidence that annotators have been recruited or that any IPA gold has been collected. The four JSONL corpus inputs remain empty; no gold labels or accuracy claims were added.
- External source lead: MekongPhon (LREC 2026) reports 367k Lao and 1.3m Khmer orthography–IPA pairs. It is recorded only as a candidate external reference. Its dataset-specific license, variety/profile, IPA convention, provenance, verification method, and overlap with engine development data must be checked before use. The LREC proceedings CC BY-NC-4.0 notice does not establish the dataset license. https://lrec.elra.info/lrec2026-main-129
- Khmer additional lead: chemvatho/Khmer-acoustic-model reports a 29,204-entry IPA dictionary and states dictionary data are CC BY-SA 4.0, distinct from MIT code/model. Per-entry provenance, dialect, IPA consistency, exact version and actual reuse rights still require inspection before importing. https://github.com/chemvatho/Khmer-acoustic-model
- Lao sampling guidance distinguishes Vientiane from other profiles and preserves lexical tone separately from contextual F0 effects; sources include Yanagimura (2013) and EURPhon profiles. Khmer guidance distinguishes Phnom Penh vowel/coda effects and variable /r/-loss. Burmese guidance keeps competing tone/prosody analyses explicit and requires source-table transcription to be independently checked before annotation.
- Current blockers: recruit/confirm two qualified annotators and one independent adjudicator per language; choose and approve target variety/convention; identify rights-cleared pilot lexemes; test a blind intake channel; verify candidate external datasets before use. Burmese additionally needs specialist approval of its prosodic transcription convention and source extraction. These are human/source/rights dependencies, not additional automation tasks.
- No repository test was run for this documentation-only checkpoint; existing CI evidence belongs to the preceding code head. Re-run exact-head CI after the documentation commits before merge.


## External corpus provenance audit — 2026-11-01

- Inspected https://github.com/byu-matrix-lab/MekongPhon. Its pipeline README describes SEAlang frequency lists, IPA scraping, minor lexicon post-processing, OPUS sentence downloads, lexicon train/eval splits, and trie-based sentence conversion from word-level IPA entries. Treat this as a large external orthography–IPA resource and possible comparator, not automatically as independent sentence-level phonetic gold.
- The upstream repository root LICENSE path was not present in the inspected tree. Dataset-specific redistribution permission, source terms, variety, IPA conventions, human verification/correction process, exact data files and overlap with our engine sources remain unverified. Do not import or redistribute any of it until those are resolved. Proceedings CC BY-NC-4.0 and Apache-2.0 model-card licenses do not license the underlying dataset by implication.
- Khmer Acoustic Model dictionary remains a candidate external comparator only; its README states dictionary CC BY-SA 4.0 and claims native-linguist validation, but per-entry provenance, variety, IPA convention and exact version require inspection.
- Burmese audio lead: Oo et al. (LREC 2020) speech corpus is described as 2,528 utterances from 20 female speakers with manual segmentation, plus G2P/normalization grammars. This is not IPA gold; inspect primary source, audio/transcript rights, consent, variety and metadata before considering it as lawful audio material for expert re-transcription.
- No data files were imported and no IPA labels were added. Corpus remains empty and benchmark accuracy remains null.


## Controlled IPA acquisition documentation CI — 2026-11-01

The documentation-only playbook, corpus-guide and handoff changes at the preceding branch head were checked by GitHub Actions. Khmer: Quality checks 41343502985 SUCCESS; optional Khmer G2P smoke 41343502939 SUCCESS; optional Goruut 41343502878 SUCCESS. No language-engine runtime or gold data changed. This validates the repository state, not the linguistic correctness of future annotations. Pages deployment and release-gate workflow were not run.


## Source acquisition update — 2026-11-01

- **Common Voice v27.0 Khmer:** official catalog lists locale `km`, CC0-1.0, MP3 archive 20.23 MB: https://commonvoice.allizom.org/en/datasets. This is sentence audio/transcript, not IPA. The archive size is not a clip/speaker count; exact manifest and regional coverage need inspection.
- **OpenSLR 42 (SLR42):** official resource page https://openslr.org/42 lists Khmer multi-speaker TTS audio and transcript index, CC BY-SA 4.0; the currently available archive is male-speaker only (866 MB). Provider warns that manual QC does not eliminate all transcript errors.
- Both are supplementary contextual audio, not direct citation-form lexical gold. Confirm Phnom Penh profile coverage before use; preserve exact clip/speaker IDs and time intervals, and independently transcribe audio.
- **Khmer Acoustic Model artifact check:** README claims a 29,204-entry IPA dictionary with native-linguist validation and says dictionary data are CC BY-SA 4.0. However, `dictionary/khmer_ipa.dict` was not found at the documented path in the inspected default branch; only `dictionary/khmer_ipa_sample.dict` (six entries) was available. The sample's space-separated representation and missing item-level provenance/variety convention prevent direct use as project gold. It remains a comparator lead pending a reproducible full artifact and method.
- `KHM-GOLD-001` remains `BLOCKED`; independent gold 0 and accuracy `null`. Next acceptance step: inspect Common Voice/OpenSLR manifests for profile and lexical coverage, recruit Phnom Penh experts, and choose a controlled citation-form protocol. No data imported.


## Common Voice v27.0 exact manifest audit — 2026-11-01

Inspected the official release manifest: https://github.com/common-voice/cv-dataset/blob/main/datasets/scripted-speech/cv-corpus-27.0-2026-09-11.json. Khmer: 739 clips; 213 validated; 15 contributor IDs; 0.28 validated hours (0.98 total). No named accent/variant category; gender metadata is entirely unspecified. Manifest locale checksum: `d1c4bb041744fefb1fa60397217b7cd79bfa2ade4510b11ff9863e9a0dc0392d`.

**Decision:** contextual-audio/process-pilot candidate only. Inspect actual transcripts for the 30 required lexical contrasts and obtain specialist Phnom Penh profile approval before sampling. OpenSLR42 adds male-only contextual audio but does not supply IPA. Neither source substitutes for controlled citation-form elicitation. No data/labels imported; gold 0, accuracy null.


## Final exact-head verification — 2026-11-01

Branch `feat/ipa-gold-corpus-20261101-review`, source-audit content commit `9bb02272d9da77126ac80392e840228aef18d18f`. Khmer exact-head CI: Quality checks [41345111255](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345111255) SUCCESS; optional Goruut [41345111267](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345111267) SUCCESS; optional Khmer G2P [41345111293](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345111293) SUCCESS. Core job passed corpus structure validation, Python tests, Node web checks, and production site build.

These checks validate the committed repository and its automated engineering contracts. They do **not** validate the linguistic correctness of future human annotations, create gold labels, or change the release blocker. Gold remains empty and accuracy remains null.


## Follow-up handoff-head CI — 2026-11-01

The subsequent documentation-only handoff/register state at commit `1800ab775ade8e6c2ac1264c4318da69a07a53c1` was also checked on its exact head: Quality checks [41345362797](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345362797) SUCCESS; optional Goruut [41345362827](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345362827) SUCCESS; optional Khmer G2P [41345362791](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41345362791) SUCCESS. These runs validate the updated documentation and existing automated checks, not future IPA annotations. Any later branch update must be checked again on its new exact head.


## Open-rights state consistency fix — 2026-11-01

- Code review found that a source could pass corpus validation with `rights_status: OPEN` but `redistributable: false`. The export and release gate would later exclude/reject it, but the canonical record itself was contradictory.
- Added a test-first regression. Test-only commit `8e328d06fb13130d878859ca2c297fb154fc0533` failed as expected in the language CI because validation incorrectly returned success for that contradictory state.
- Added the fail-closed Python validation and matching conditional in `schemas/ipa-gold-record.schema.json`; regression also asserts the schema condition. Exact code/schema head: `e624dd59ce7ae1648cf72262e124764769fbc8a2`.
- Exact-head CI [41347973905](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41347973905) passed: 144 Python tests + 37 subtests; web checks and production build passed; optional Goruut and Khmer G2P smoke benchmark passed.
- No external corpus, restricted source data, IPA label or benchmark record was imported or created. Gold remains 0; `gold.tsv` remains header-only; empirical accuracy remains null.

## Exact current-head verification and handoff reconciliation — 2026-11-01

- Verified default branch `main` at `c0a2b33c86791b6546e1158c62043fd23acc1f60`; work branch `feat/ipa-gold-corpus-20261101-review` at `508ed94460e210ff9cc07cc0eaa7815246ee37b2`. GitHub compare reports **83/84/82 commits ahead respectively and 0 behind** (see the repository's PR compare; no main commits need porting at this checkpoint).
- Exact current-head GitHub Actions core run: [41348224247](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41348224247) — SUCCESS. 144 Python tests + 37 subtests; browser register-shifter contract, web checks and Vite production build passed. Optional Goruut KhmerCentral and Khmer G2P diagnostics passed.
- These are hosted CI results. No local checkout or local test execution is claimed. Optional G2P/Goruut/Epitran checks are diagnostics only and do not establish linguistic correctness.
- The current branch contains the open-rights invariant: `rights_status=OPEN` requires `redistributable=true` in both the Python validator and `schemas/ipa-gold-record.schema.json`, with a regression test.
- Independent expert-adjudicated gold remains **0**; `gold.tsv` remains header-only; empirical accuracy remains **null**. Engineering CI does not close human annotation, profile/convention approval, or linguistic validation gates.
- This entry supersedes earlier handoff statements that described the documentation/code checkpoint as awaiting exact-head CI. The PR description may contain older or superseded SHA references; the branch ref and exact-head run above are authoritative.


## IPA gold nested-record contract hardening — 2026-11-01

- Test-first regression run [41352932018](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41352932018) failed as expected: undeclared fields inside orthography, profile, source and rights_evidence passed runtime validation, and the schema left those objects open.
- Runtime fix and schema closure: unknown properties are now rejected at all four nested boundaries. Exact code/schema head `8d6b2c8184dc27a126dfa11420bc5c821c1afeb6`; exact-head core CI [41353055958](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41353055958) SUCCESS (146 pytest tests + 44 subtests; web checks, register-shifter browser contract and production build passed).
- Engineering-only change: no linguistic rules, IPA labels, gold records, source data or accuracy claims added. Independent expert gold remains 0; accuracy remains null. Hosted CI only; no local checkout was available.


## Cross-repository validator cleanup checkpoint — 2026-11-01

- Methodology review: the repository's pinned references in `AGENTS.md` already capture the relevant practices from Superpowers (test-first changes and evidence-gated verification), mattpocock/skills (clear module seams and behavior-focused tests), and Ponytail (small complete diffs and connected-code review). They remain methodology references, not runtime dependencies; no external skill bundle was copied into the product.
- Removed four consecutive duplicate nested-object validation calls from `scripts/ipa_gold_corpus.py` (orthography, profile, source, and rights_evidence). This removes redundant work without changing the contract. The resulting file has the same blob SHA across all three repositories: `a072297e320b4b91a36c59fc90328b6ff98d2a5f`.
- Code commit: `5c5e14d0458f9afd9c154e36975d86d882b67c0f`. - Core PR CI: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354247584 (SUCCESS); core push CI: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354242025 (SUCCESS); optional language diagnostics: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354247560, https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41354247608 (SUCCESS).
- No schema, source data, linguistic rule, IPA label, or gold row changed. Independent expert-adjudicated gold remains 0; accuracy remains null. The next substantive blocker is still qualified target-variety annotation and adjudication, not more validator scaffolding.


### Upstream methodology review — follow-up 2026-11-02

- **mattpocock/skills v1.3.2**: `d1478fcb140db0b93c0c8df17bcfd311844749d0` (released 2026-10-29). Applied the relevant improvements: standards review reads repository standards and reports separately; spec compliance and repository standards are separate review axes; bug-diagnosis RED evidence must prove the intended mutation changed relevant source; issue/PR tracker operations follow repository templates and ownership boundaries.
- **Superpowers 7.0.1** remains pinned at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`; its current workflow guidance reinforces preserving untracked work when worktree cleanup refuses and keeping human-authored report sections genuinely human-authored. The October 20 template changes are included in the reviewed 7.0.1 lineage.
- **Ponytail 5.3.3** remains pinned at `7801d061243d7b753bad0e0b3c057cd250b11755`. Upstream `main` advances to `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`; the inspected post-pin change only adds a README product/logo mention, not engineering-method guidance, so the method pin remains appropriate.
- No upstream skill bundle, code, dependency, dataset, or runtime integration was copied. These instructions are a selective adaptation, not a claim that third-party tools are installed.


## Exact-head verification — methodology refresh 2026-11-02

- Documentation and agent guidance checkpoint: `73e654b5a592cb84ed29b25b03cb95fb5a7e25e0`.
- [Quality checks 41358627128](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41358627128) completed SUCCESS on this exact commit; full quality-check workflow.
- Optional diagnostic runs [41358627194](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41358627194) and [41358627130](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41358627130) also completed SUCCESS. These diagnostics are not accuracy evidence.
- The current branch has one subsequent documentation-only evidence-register commit; its exact-head CI is recorded in the final session report. No engine, linguistic rules, IPA labels, gold records, datasets, or runtime dependencies were changed.


## Adjudication schema/runtime parity correction — 2026-11-02

- Found a real contract mismatch: `schemas/ipa-gold-adjudication.schema.json` requires `final_ipa` (nullable), but the Python validator used `row.get("final_ipa")` and therefore accepted an omitted key for `UNRESOLVED`.
- Test-first evidence: test-only commit `df23f23c573c8311c7c721b02177b65b44117fd7` failed as intended on exact-head PR CI [41407016954](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407016954); the runtime returned success for a malformed adjudication and the new regression failed.
- Fix: `dea7008094314b6a1ae88b1b4868e41552cdd54a` now rejects a missing `final_ipa` property for every decision; unresolved cases must explicitly provide `null`. Exact-head PR CI [41407116467](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407116467) SUCCESS. 147 pytest tests + 44 subtests; web checks and production build passed.
- Optional diagnostic runs: [41407116367](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407116367), [41407116301](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407116301) — SUCCESS.
- This is validator/schema parity only. No linguistic rules, IPA labels, gold records or source datasets changed; independent expert gold remains 0 and accuracy remains null.


## Unresolved adjudication positive-path verification — 2026-11-02

- Added explicit positive-path coverage proving that `UNRESOLVED` with a present `final_ipa: null` remains valid; omitted `final_ipa` is rejected by the new runtime guard. Test commit `8111f28c34b7b3d7118d4f428178e4e90591c336`.
- Exact-head PR CI [41407396214](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407396214) SUCCESS. 148 pytest tests + 44 subtests; web checks and production build passed.
- Optional diagnostic runs: [41407396207](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407396207), [41407396326](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41407396326) — SUCCESS.
- No linguistic rules, IPA labels, corpus records, datasets or empirical metrics changed. Independent expert gold remains 0; accuracy remains null.


## External G2P benchmark and engine coverage audit — 2026-11-02

A source-backed audit was added at [docs/research/external-g2p-benchmark-and-engine-coverage-2026-11-02.md](research/external-g2p-benchmark-and-engine-coverage-2026-11-02.md). It separates declared engine language support from verified phonological coverage, records language-specific external benchmark resources, defines a reproducible held-out evaluation protocol, and explicitly does not claim a score for this repository. No external engine output was promoted to IPA gold.

Current key findings:
- Epitran and Goruut both declare this language, but both remain comparators only; their public support lists do not establish complete project-profile coverage.
- The audit records engine-specific limitations and the phonological feature inventory that must be evaluated.
- The next step is a pinned, same-input, held-out benchmark with independent expert references and feature-specific metrics; exact model/dataset versions and provenance must be recorded before execution.

No runtime engine benchmark was run in this documentation update. Hosted CI verifies repository engineering, not linguistic correctness or benchmark accuracy.


## External engine smoke evidence — 2026-11-02

Detailed methods, benchmark context, limitations and per-feature acceptance requirements: [external G2P benchmark and engine coverage audit](research/external-g2p-benchmark-and-engine-coverage-2026-11-02.md).

Khmer: khmerphonemizer 0.0.3, 100 source-attested MekongPhon examples, 100 outputs, 18 strict / 19 limited-normalized matches; Goruut 100 rows, 6/100 exact, 97 outputs, 3 failures, 70 complete/27 partial/3 unknown coverage, 27 unphonemized fragments. No independent gold; accuracy=null. Runs: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409092574 and https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409092578.

These are raw-output concordance/coverage diagnostics, not accuracy measurements. All independent gold counts remain zero and accuracy remains null. The missing `weights9.bin.zlib` diagnostic in Goruut's logs is recorded for investigation. Declared language support is not accepted as proof of adequate coverage. No gold labels or production rules were changed based on these runs.


## Benchmark provenance correction — 2026-11-02

Goruut was fetched from upstream source snapshot `b224bde`, not a release tag. The Khmer phonemizer was version 0.0.3. Added the 2019 Khmer G2P paper benchmark (PER 23.2% → 11.1%; WER 69.6% → 51.4%) as separate historical research evidence.

The detailed research audit is authoritative for engine versions, benchmark limitations, and measured diagnostic values. Do not describe the Goruut run as release-pinned; it used the captured upstream source revision stated above.


## Verification checkpoint for the 2026-11-02 external-engine audit

Research audit and completion register are now updated. Last register commit before this handoff update: `85f7537cfa59fe839fad11076f692a70770f1709`.

Quality checks, Khmer G2P diagnostic and Goruut raw-output workflows passed on the same code state before the final register-only documentation commit: https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409309736, 41409309726, 41409309834.

The commits after those workflow runs changed only research-audit / handoff / completion-register documentation, not executable code. Do not treat hosted diagnostic jobs as gold evaluation: all independent gold counts remain zero. The current review branch remains ahead of `main` and has not been merged.


## Final exact-head CI reconciliation — 2026-11-02

The previously pending final-head hosted workflows have now completed successfully on this repository's recorded review-branch head `86980925a7dc9eda745268b2bd1fb081d1a82713`. Runs: [Quality 41409583877](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409583877); [Khmer G2P 41409583886](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409583886); [Goruut 41409583865](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41409583865). All listed jobs and steps report SUCCESS. This closes the CI-status uncertainty from the preceding checkpoint; it does not close linguistic validation or gold-data acceptance.

A follow-up inspection of the pinned Goruut source tree at `b224bde02151f8f86d0fe260804e4ca743bda620` confirms that the language-specific dictionary directories for Lao, Khmer Central and Burmese do not contain `weights9.bin.zlib`; the available language assets include the earlier weight files. Therefore the recurring log warning is consistent with an absent upstream language asset in that snapshot, not evidence that our checkout step failed to fetch an existing file. The server still starts and returns outputs, but the precise model-quality impact of the missing file is not established by this probe. Keep it recorded as an upstream model-bundle coverage limitation; do not patch or synthesize model weights locally.

The current review branch remains ahead of `main` and 0 commits behind; no PR was merged and no release was published. Independent expert-adjudicated gold remains 0; empirical accuracy remains null. All external-engine scores remain diagnostic concordance only.


## Final audit-register correction checkpoint — 2026-11-02

The completion register now supersedes the stale action item to locally recover/fix Goruut `weights9.bin.zlib`: the pinned upstream source tree does not publish that file for the three language bundles. The issue is therefore **BLOCKED (upstream dependency)** pending upstream publication or documentation of the intended fallback, not a project-owned file repair. No synthetic weights or substitute model assets were introduced.

The immediately preceding exact-head verification completed successfully on the pre-register-correction commits; the register correction itself changes documentation only. Previous runs: [Khmer Quality 41411555459](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41411555459); [Goruut 41411555448](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41411555448); [Khmer G2P 41411555592](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41411555592). Current branch commit before this handoff checkpoint: `afe5a2b3becc6438362cd9a11ac47b4bc9dc5698`. The handoff update will trigger fresh branch CI; do not treat these preceding run IDs as verification of the new handoff commit.


## Additional Khmer model and dictionary resources discovered — 2026-11-02

A follow-up source search found [`byumatrixlab/khmer-ipa`](https://huggingface.co/byumatrixlab/khmer-ipa), a 33.6M-parameter BERT encoder–decoder trained from the MekongPhon pipeline, and [`chemvatho/Khmer-acoustic-model`](https://github.com/chemvatho/Khmer-acoustic-model), which reports a 29,204-entry IPA dictionary. The former is a priority neural G2P baseline; the latter is a lexical/forced-alignment resource, not a G2P engine. Its reported F1 values (0.360 phoneme alignment; 0.120 word alignment) are not IPA-generation accuracy. Status: **PARTIAL / BLOCKED for full lexicon coverage**. The README reports 29,204 entries, but `dictionary/khmer_ipa.dict` returned GitHub API 404; only the six-row `dictionary/khmer_ipa_sample.dict` was retrievable. The full lexicon's notation and coverage therefore remain unverified. Pin the model revision/checksum, verify dialect and IPA conventions, audit unusual inventory symbols, and measure lexicon coverage only when the full dictionary is accessible. Retain raw predictions. Gold remains 0; accuracy remains null.


## Main publication reconciliation — 2026-11-02

Supersedes earlier handoff statements that the review branch was still ahead of `main` and unmerged: PR [#103](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/103) was merged into `main` as `b7e0171f77c08a15b0e55a9cb9fd83a001fff4f7`; this was the repository's current `main` tip at reconciliation. Exact-head engineering workflows on the PR head passed: Quality/tests [41414658963](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41414658963), Khmer G2P [41414658924](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41414658924), and Goruut [41414658926](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41414658926). The Pages workflow is configured to deploy from `main` and includes a deployed-site/runtime-asset smoke test. The public deployment result could not be independently inspected from this session, so deployment status remains **BLOCKED (external verification/network access)**, not claimed successful. No frontend source changes were included in this PR. Independent expert-adjudicated gold remains 0 and accuracy remains null; the project is still a research prototype.


## Current-main UI publication — 2026-11-02

The older design PR [#64](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/64) was not merged because its branch had diverged (7 commits ahead / 178 behind current `main`). Its responsive CSS and cache-busting intent were ported onto a fresh branch from the then-current `main`; PR [#105](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/105) was merged as `18ee0ae46cb98725c7f59c0436611fa50e4581bf`. The current-main CI [41424009124](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41424009124) passed the IPA gold-corpus structure validation, Python tests, JS web checks and Vite build. Added responsive layout contract tests for control wrapping, Ukrainian-result priority, narrow-phone status and coverage overflow. The Pages workflow is configured for pushes to `main`; actual deployment completion and public-site smoke-test result remain **BLOCKED (external verification/network/DNS unavailable in this session)**. This UI change improves presentation only and does not improve linguistic accuracy. Independent adjudicated gold remains 0; accuracy remains null; research-prototype status is unchanged.

### Pages smoke-test compatibility follow-up — 2026-11-02

The cache-busted stylesheet URL introduced by the UI polish exposed an overly strict CSS-link extractor in the deployed-site smoke test. Fixed in PR [#106](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/106), merge `7ee049aae9cc7ff571b21eabe18e962627f192a3`; the extractor now accepts an optional query string. PR CI passed (41424681328). The Pages workflow is now compatible with the deployed CSS URL. The post-merge Pages deployment and live-site smoke-test result are still **BLOCKED for independent verification** because external DNS/network access and a workflow-run listing endpoint were unavailable; do not infer deployment success from a merged PR or a successful pull-request CI run.


## Focused scholarly source audit — 2026-11-03

A targeted full-text review in the Undermind workspace and a parallel Consensus synthesis were added to the research evidence base. See the durable [cross-language research note](https://app.undermind.ai/projects/4f071406-bdb4-4fd1-b93f-71b9d5ec661d?path=/Research%20brief%20for%20three%20active%20engineering-research%20repositories%20that%20convert%20L.md) and the [Khmer practical transcription comparison](https://app.undermind.ai/projects/4f071406-bdb4-4fd1-b93f-71b9d5ec661d?path=/Khmer%20Cyrillic%20practical%20transcription%20comparison).

- Chem Vatho (2020), [Standard Khmer vowel system: An acoustic study](https://doi.org/10.61945/cjbar.2020.2.2.3), is a one-page poster. Although 21 speakers were initially recruited, the reported acoustic results concern four Phnom Penh speakers (2 men, 2 women; ages 20–50) reading lexical items. It reports F1/F2 and duration but has unclear/inconsistent timing details, no stated formant normalization, and reported token/measurement gaps. It does not establish a representative standard, consonant system, tone inventory or coda inventory.
- Sakamoto (1968), [The standard Khmer language and its Phnom Penh dialect](https://doi.org/10.20495/tak.6.2_290), relies principally on one Phnom Penh informant born in 1945. It records style-sensitive weak-syllable realization and proposes specific PP/ST correspondences, but these remain largely single-speaker analyses, not population-level rules.
- This reinforces the project's careful-citation profile as a bounded project decision rather than a universally established standard. The four-speaker vowel study does not validate every consonant, register, coda or colloquial process. Keep the removed deterministic colloquial /r/-loss rule removed; do not reintroduce it from general descriptions.
- Consensus identified Khmer G2P studies including Sar & Tan (2019), DOI [10.1016/j.procs.2019.11.140], reporting PER reduction from 23.2% to 11.1% after vowel-tag linguistic features. This is a published system result, not independent gold for this repository; its split, lexicon provenance, profile and rights must be checked in the primary paper before any benchmark reuse. Sok & Adams (2016) describes Thrax-based word transcription, but is not itself evidence that the current project has an adjudicated benchmark.

Independent expert-adjudicated gold remains 0; accuracy remains null. The source audit changes no IPA label or phonology rule. The Khmer browser hotfix is still separate from linguistic research and must be merged/deployed independently before production repair is claimed.


## Post-hotfix integration checkpoint — 2026-11-03

- PR [#108](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/108) merged by squash as `e9894e5726f5f6aa2510d7d3beed69b2d03fb666`.
- The merged change removes exactly one invalid DOM dereference from `src/main.js`; `index.html` intentionally has no `#source-result` element. A post-merge source inspection confirms the render path no longer writes to that absent element.
- Exact `main` push workflows all completed successfully: Quality checks [41641496598](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41641496598), Chromium browser smoke [41641496582](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41641496582), and GitHub Pages build/deploy plus deployed-site smoke [41641496680](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41641496680). The Pages run's build, Chromium production-preview test, deploy and deployed runtime-asset smoke steps all succeeded.
- The PR's exact pre-merge head `e8ef5ea727758c3339d016fb2636c1108e1549f4` also passed Quality [41536753767](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41536753767) and browser [41536753931](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41536753931); all steps in both job summaries succeeded.
- The browser regression covers visible IPA/Ukrainian output for `ក`, withholding mixed unsupported input, and clear/reset. This is UI behavior only; no phonology rule, IPA label, or gold row was introduced.
- PR [#107](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/107) is now 95 commits ahead / 1 behind and reports non-mergeable after the isolated hotfix landed. It contains the same one-line DOM correction plus a broad profile change; do not merge wholesale. Reconcile against new `main`, retain the already-merged hotfix, and re-run all relevant checks.
- Independent adjudicated IPA gold remains 0; empirical accuracy remains `null`. The repository remains a research prototype, not a linguistically validated release.


## Rebased Khmer split-manifest correction — 2026-11-03

- Rebased the substantive changes from prior PR [#109](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/109) onto current `main` after PRs #108 and #111; this branch deliberately excludes the already-merged browser hotfix and does not reintroduce its obsolete DOM write.
- Enforces one manifest-wide `(seed, version)` identity across all lexeme groups, preserves the identity when extending an existing manifest, rejects conflicting and empty explicit CLI overrides, and adds an acceptance test for creating a new versioned manifest from a separate empty `--splits` input.
- Prior exact-head CI [41639679611](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41639679611) succeeded on the original PR head, but this rebased port requires its own exact-head tests before merge.
- No linguistic gold rows or phonological labels are added. Independent adjudicated gold remains 0; accuracy remains `null`.


## Khmer source evidence and benchmark reconciliation — 2026-11-03

- Ported the source registry, references, external-corpus triage, controlled collection playbook, benchmark audit and provenance tests from prior PR [#110](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/110) onto current `main` after PR #112 merged. The IPA corpus protocol was merged carefully: the existing manifest-wide split instructions are preserved and the agreement-metric boundary is added separately.
- The MekongPhon record is an external benchmark lead, not project gold. Kirby's 2015 DataShare items are scoped to the specific audio/supplementary resources and their item-level CC BY 4.0 declarations; Praat TextGrids and measurements are not independent lexical IPA gold. Cucchiarini and Oller/Ramsdell are methodological sources, not Khmer-specific scoring algorithms. Woźnica's multi-region thesis is not treated as Phnom Penh-only evidence.
- Original PR-head Quality workflow [41640011541](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41640011541) succeeded; this clean port requires its own exact-head CI. No external IPA labels imported; independent adjudicated gold remains 0 and accuracy remains `null`.


## Single careful-citation profile integration — rebased 2026-11-03

- Rebased the narrow profile/runtime change onto the latest main after Khmer source-evidence PR #113 merged. This branch excludes the already-merged browser hotfix and all unrelated broad PR #107 changes.
- The service exposes only `khmer-pph-careful-citation-v1`, a bounded project profile for contemporary Phnom Penh careful citation-form speech. The adapter preserves supplied IPA; it does not synthesize colloquial /r/-loss or rewrite /Cr/ clusters.
- The project profile decision is supported as an elicitation target by Chem (2020)'s small formal-reading sample, but it is not a national standard or a claim of full lexical coverage. Independent adjudicated gold remains 0 and accuracy remains `null`.
- Original #114 exact-head Quality and Chromium workflows succeeded, but this rebase requires fresh exact-head checks.


## Khmer agent context and glossary — 2026-11-03

- Added the project glossary, current codebase/data-flow map and issue-tracker instructions, and updated `AGENTS.md` to route future work through the canonical handoff and verified maps.
- The codebase map reflects the current main after the browser hotfix, manifest-wide split fix, source-evidence reconciliation and single careful-citation profile. It distinguishes parser structure, source-language phonology, typed IPA, Ukrainian adaptation, generated browser data and the separate romanization path.
- These are navigation and process aids, not linguistic evidence or a replacement for expert review. No runtime rules or gold labels changed. Exact-head CI required.


## Current repository continuation checkpoint — 2026-11-03

- Verified default branch `main` at `d8419d3099a8047d819a5a71cb5c4ef927db435e`.
- Latest exact-main CI for profile/runtime commit `1dc07f9c43972f547ac7a56adb9ed949155bacf1`: Quality 41646838970 SUCCESS; Chromium 41646838756 SUCCESS; Pages/deployed-site 41646838884 SUCCESS. The subsequent glossary/codebase-map documentation commit is d8419d3.
- PR reconciliation: PRs #107 and #114 were closed without merge as superseded; their profile/runtime/test changes are already byte-identical to main. PRs #108 and #111 were merged earlier. The attempted documentation sync PR #117 was closed because main advanced while the docs-only branch was open; this branch is based on the latest main. No runtime changes are involved.
- Current engineering state: main includes the single operational profile `khmer-pph-careful-citation-v1`, no deterministic colloquial /r/-loss rewrite, the manifest-wide split fix, source-evidence reconciliation, browser hotfix, and project glossary/codebase map. The profile remains a bounded project elicitation decision pending specialist approval and does not establish a complete phonological model.
- Linguistic evidence boundary: independent adjudicated IPA gold remains 0; gold export remains header-only; empirical accuracy remains null. CI verifies engineering behavior only.
- Human/research blockers remain: approve the versioned IPA convention; recruit two qualified independent annotators and a separate adjudicator; establish blinded intake; verify source-specific data rights; collect and adjudicate a profile-specific pilot; complete deployed-site manual keyboard, screen-reader, responsive and mobile QA.
- No gold labels, source-derived IPA guesses, phonological rules, or benchmark scores were created in this checkpoint.


## Upstream methodology reference refresh — 2026-11-03

- `obra/superpowers` current `main` remains `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`, release v7.0.1. The inspected upstream guidance reinforces protecting untracked work, re-reading evidence rather than treating reruns as proof, bounded waits, and explicit review/finish accounting. Apply relevant practices; do not import the external repository as a runtime dependency.
- `mattpocock/skills` current `main` is `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`; the latest commit adds a software-factory glossary and example runs. The immutable release reference remains v1.3.2 at `d1478fcb140db0b93c0c8df17bcfd311844749d0`; distinguish release pin from current-main snapshot.
- `DietrichGebert/ponytail` current `main` is `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`, release v5.3.3 at `7801d061243d7b753bad0e0b3c057cd250b11755`. The post-pin upstream change inspected is a README/product-list addition, not a methodology change.
- No upstream skill files were copied into product/runtime code. These are traceable method references only.

## Continuation — held-out IPA benchmark correction (2026-11-03)

- Base `main`: `3809f0de9b77253a08985bb90e18e7308bdda412`; work branch: `fix/heldout-ipa-benchmark-20261103`.
- Finding: the frozen split manifest existed, but the gold TSV export discarded split identity and the scorer included all adjudicated rows. This could allow train/dev examples into a purported independent evaluation.
- Implemented: export now requires a frozen assignment and emits `split`; the gold TSV header includes the field; benchmark validation requires a valid split, defaults to `test`, and supports explicit `--split train|dev|all` for non-held-out diagnostics. Reports identify the selected split and distinguish all adjudicated rows from the scored denominator.
- Exact code/test-head verification: [Quality run 41651903776](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41651903776) SUCCESS on `ca53d628ae9a9ea4696fc85f42cdf59bcedfa2d1`, including Python, web checks and Vite build.
- **IPA-BENCH-SPLIT-001 — DONE_VERIFIED (engineering contract).** Independent expert-adjudicated gold remains 0; `gold.tsv` remains header-only; empirical accuracy remains `null`. No phonetic labels were added.
- Still blocked: two qualified independent annotators, a separate adjudicator, approved IPA convention, controlled blind intake and source-specific rights evidence. Manual visual/keyboard/screen-reader/mobile QA remains TODO.

**Final review:** self-review performed against the complete branch diff and matching implementation across all three repositories (no subagent reviewer is available). The split/export/scoring contract, fail-closed paths, report denominator, tests and docs were inspected; no Critical/Important defect was identified. PR remains open for owner review; no shared-branch merge was performed.

## Frozen split manifest provenance — 2026-11-03

The export and benchmark now preserve and validate the complete frozen split identity, not only the bucket name: `split`, `split_seed`, and `split_version`. Every adjudicated row must carry non-empty seed/version metadata, and the benchmark rejects a TSV that mixes manifest identities. The report exposes the manifest seed/version and selected scoring split. This makes the evaluated test partition traceable to one exact manifest; it does not create linguistic gold or change the current zero-row accuracy status.


## Empty prediction dataset guard — 2026-11-03

A further benchmark review found that a header-only prediction TSV exited successfully and emitted a report with no engine entries. This could be mistaken for a completed evaluation even though no engine had been evaluated. Added a regression test and a fail-closed CLI guard requiring at least one prediction row. The guard runs after gold/split-manifest validation so existing malformed-manifest diagnostics remain specific. This does not change the treatment of missing rows within a named engine: those remain in its denominator. Exact-head verification: RED: [41655188132](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41655188132). Final exact-head quality checks: [41655492141](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41655492141) SUCCESS; browser smoke: [41655491334](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41655491334) SUCCESS. The benchmark guard is DONE_VERIFIED as an engineering input-integrity check; no gold rows or accuracy claims were added.


## Continuation — whitespace-only benchmark identifiers (2026-11-03)

A code review found that truthiness-only identifier checks accepted whitespace-only gold IDs, prediction IDs and engine names. Such values could create visually empty keys and make malformed prediction rows look like a named engine. Validation now rejects identifiers whose trimmed value is empty while preserving non-empty identifiers verbatim for exact matching. Regression tests cover each field separately.

- Test-first RED for whitespace-only gold IDs: [workflow run 41660794382](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41660794382) FAILED on the new regression as expected.
- Test-first RED for prediction engine/ID fields: [workflow run 41662096875](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41662096875).
- Final exact-code-head verification: [workflow run 41662242906](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41662242906) SUCCESS; 164 Python tests + 50 subtests; 3 browser smoke tests passed; browser smoke [41662242611](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41662242611) SUCCESS.
- Verified implementation commit: `02807605a78fee4c7ab25cd51315e4343940a3c1`; exact-code-head CI [workflow run 41662242906](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41662242906) SUCCESS.
- **IPA-BENCH-IDENTIFIERS-001 — DONE_VERIFIED (engineering input-integrity guard).** No linguistic labels, gold records or accuracy claims were added.

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


## One-pass continuation checkpoint — 2026-11-04

- Current default branch: `main`; verified head `9e688e0118382f8e990e8758c53a5c7ec8877a78` (latest commit after PR #138).
- Open PR query on 2026-11-04 returned none. Latest relevant merges: #131–#138. #131–#133 reconcile MekongPhon provenance, scale and dictionary-seeded evaluation limits; #134 records unresolved Khmer Acoustic Model dictionary count/license discrepancies; #135 registers DDD audio candidate constraints; #137 registers Common Voice 27 Khmer audio limits; #136/#138 reconcile merges and verification.
- Exact-head hosted verification for PR #137: Quality checks 41800443113 SUCCESS and Khmer browser smoke 41800443035 SUCCESS. PR #138 is a documentation-only post-merge checkpoint. The current main combined-status endpoint returned no status entries; this is not evidence of a failed or successful main push run.
- Preserved evidence boundary: DDD Part 1 lists 134.60h and 8 speakers under CC BY-SA 4.0 with attribution and no-speaker-identification restrictions; Common Voice 27 reports 739 clips (213 validated; 0.28 validated hours; 15 speakers) but no IPA or reliable accent identification. Neither source is IPA gold. MekongPhon remains dictionary-seeded and dataset rights are unresolved.
- Task ledger: source registrations and provenance reconciliation **DONE_VERIFIED**; independent adjudicated Khmer IPA gold **BLOCKED** (0 records; gold export header-only; accuracy null); expert approval of target variety/profile and IPA convention, two independent annotators, separate adjudicator, item-level rights and blind intake **BLOCKED**; manual keyboard/screen-reader/mobile QA **TODO**.
- Khmer Acoustic Model dictionary remains blocked pending author clarification and an inspectable versioned full corpus; conflicting dictionary counts and CC BY/CC BY-SA statements must not be treated as cleared.
- No runtime phonology or Ukrainian mapping changes were made in the latest source-evidence merges. No orthographic transcript or G2P respelling is promoted to IPA.
- The initial checkpoint commit was documentation-only; a subsequent test-only change now uses Khmer script and a neutral test profile in the IPA-corpus fixtures. Hosted CI results for the final head are recorded separately; local tests were not run in this connector session. Hosted CI evidence above is tied to the exact PR head, not a claim of fresh local verification.


## Hosted verification update — 2026-11-04

- Draft PR #139 exact head `3889739aecf0221c7cf1e26be59f025838a914ed`: Quality checks [41844573271](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41844573271) **SUCCESS** and browser smoke [41844573296](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41844573296) **SUCCESS**.
- Quality job completed IPA gold corpus structure validation, Python tests, web checks and site build. Browser smoke completed successfully.
- This verifies the docs-only PR head and the repository's current CI contract. It does not establish phonological accuracy or clear the Khmer Acoustic Model / MekongPhon rights questions; the evidence and expert-review blockers above remain unchanged.


## Test-fixture correction — 2026-11-04

- Review found that the shared IPA-corpus validator test file used Lao orthography and a Lao-specific profile description even in the Khmer and Burmese repositories. This did not affect production validation, but made the fixtures misleading and weakened language-specific test coverage.
- The test fixtures now use the repository's script (Lao / Khmer / Myanmar), neutral `test-<language>` profile identifiers and `Test fixture (<language>)` variety labels. A regression test asserts the fixture characters fall within the corresponding Unicode block and that profile metadata matches the repository language.
- This is a test-harness correction only. It does not validate language phonology, IPA correctness, or script-specific parser behavior; the production validator still intentionally validates corpus structure rather than imposing a single script restriction on all orthographic records.


## Final test-fixture PR verification — 2026-11-04

- Test and handoff changes were present at head `ff656632cb3323612f5c7f647a069c821aceaa48` when the following hosted checks completed: Quality checks [41847143845](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41847143845) **SUCCESS**; browser smoke [41847143819](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41847143819) **SUCCESS**.
- The successful checks include the language-specific IPA-corpus fixture regression, repository data validation, language-specific Python test suite, web build/reproducibility checks and Chromium browser checks where configured.
- Exact job steps were inspected; every reported step completed with `success`. These are engineering/structural checks, not a linguistic accuracy benchmark. No local tests were run in this connector session.


## External Khmer pronunciation-source research continuation — 2026-11-04

- Created dedicated branch `research/khmer-external-pronunciation-audit-20261104` from main `09f439dc12e078c72a00038c0583b03803ee054a`.
- Added four external resource records to `data/khmer/sources.json`: pinned IPA-Dict Khmer, PhonSobon Khmer G2P, PhonSobon combined pronunciation dictionary, and Chem Vatho's Khmer Acoustic Model. Each record distinguishes source format, scope, provenance, rights and whether it is eligible for gold.
- Extended `docs/audits/current/EXTERNAL-PHONETIC-CORPUS-TRIAGE-2026-11-01.md` with source-level findings and explicit no-import decisions.
- Extended the existing linguistic completion register with `KHMER-EXT-IPA-DICT-001`, `KHMER-EXT-RESP-001`, and `KHMER-ACOUSTIC-DICT-RECHECK-001`.
- Added `test_external_pronunciation_sources_preserve_format_and_rights_boundaries` to `tests/test_data_integrity.py`. It guards against silently reclassifying Khmer-script respelling as IPA, treating non-commercial sources as unrestricted, or treating a missing/contradictory external dictionary as an approved source.
- External research evidence: IPA-Dict's pinned revision `972cd67dd5f96bc5660e28070cde26e3928abcd7` has 3,286 lines in `data/km.txt`; its README attributes Khmer data to aakanee.com and CC BY-NC-SA 4.0. PhonSobon Khmer G2P reports 38,629 pairs / 37,755 unique words and explicitly says the pronunciation field is Khmer-script respelling, not IPA; source content remains NCKL-owned and commercial terms must be checked. The combined dictionary reports 39,110 rows and flags 39 LLM-assisted decisions for native-speaker confirmation. Chem Vatho's current main `2714994b41ccf875c5b6f6182b48a72f13632dbf` claims 29,204 IPA entries but exposes only a six-line sample; root README and dictionary README disagree on CC BY-SA 4.0 vs CC BY 4.0 and on dictionary/mapping counts.
- No external source data were copied; no license was inferred; no IPA or Ukrainian output was fabricated. The IPA-Dict resource is non-commercial/share-alike, PhonSobon resources remain rights-limited/unresolved and Khmer-script respelling, and the acoustic-model dictionary remains blocked pending a full artifact and clarified terms.
- Acceptance boundary: this closes source discovery/triage documentation only. It does not close `KHM-GOLD-001`; independent expert-adjudicated Khmer IPA gold remains 0 and empirical accuracy remains null.
- Validation: pending hosted CI for this branch/PR. No local checkout or local test execution was available through the connector session.


## Final Khmer external-source PR verification — 2026-11-04

- PR #140 head after the regression assertion correction: `3fd741b420eb217f2fe0d24087642dbbf866c687`.
- The first Quality run [41849845861](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41849845861) exposed one test-only case-sensitive assertion mismatch (`NOT project gold` vs the source note's `Not project gold`); 173 tests and 60 subtests passed, one new assertion failed. The assertion was corrected to compare case-insensitively; no source classification or production behavior was changed.
- Corrected-head Quality [41850630303](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41850630303) **SUCCESS**; corrected-head browser smoke [41850630166](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41850630166) **SUCCESS**. The Python suite, web checks, production build and Chromium browser smoke completed successfully.
- Source records continue to distinguish IPA-Dict's non-commercial/share-alike Khmer IPA, PhonSobon's Khmer-script respelling (not IPA), and the incomplete/licensing-conflicted Khmer Acoustic Model dictionary. No third-party data were copied.
- This verifies source-registry and rights-boundary engineering only. Independent expert-adjudicated Khmer IPA gold remains 0; empirical accuracy remains null.
- No local tests were run; hosted CI logs were inspected.


## IPA gold release-gate profile consistency — 2026-11-04

- Found a concrete gap in the shared `scripts/ipa_gold_corpus.py`: the release gate checked adjudicated-record counts, frozen splits and source redistribution rights, but did not enforce the playbooks' one-target-profile / one-IPA-convention requirement. A mixed-variety or mixed-kind corpus could therefore pass the numeric/rights gate and be scored as one benchmark.
- Added regression tests first for mixed profile and mixed IPA kind in each of the three repositories. The first Lao test run failed on both new cases as expected; after adjusting the fixture to populate all three deterministic split buckets, the regression remained targeted. The Khmer and Burmese exact-head runs subsequently passed; final run IDs and merge evidence are recorded below.
- Added shared gate checks: one signature across adjudicated records (`profile.id`, `variety`, `region`, `register`) and exactly one adjudicated IPA kind. Per-record speaker/audio IDs are deliberately excluded from target-profile identity.
- Updated the corpus documentation and completion register. The checks do not replace approved convention sheets, human reviewer qualifications, blind annotation evidence, or language-specific contrast-coverage reports. The gate still does not calculate contrast coverage from free-text phonological metadata.
- No IPA labels, pronunciation rules, Ukrainian mappings, source data, or benchmark scores were added. Independent adjudicated gold remains 0 in all three projects.


## Final release-gate profile guard verification — 2026-11-04

- TDD RED evidence on the pre-fix implementation: Lao [41868595591](https://github.com/ClippyFirst/Lao-Ukrainian-Phonetic-System/actions/runs/41868595591), Khmer [41868607839](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41868607839), and Burmese [41868623352](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41868623352). In each repository both new regression cases failed because the old CLI returned `{"release_ready": true, ...}` for a corpus deliberately mixing target profiles and/or IPA kinds despite meeting train/dev/test minimums.
- GREEN after the shared validator fix:
  - Lao Verify [41868752376](https://github.com/ClippyFirst/Lao-Ukrainian-Phonetic-System/actions/runs/41868752376) **SUCCESS**; 172 Python tests and 4 browser tests passed; data/evidence audit, optional G2P CLI, generated-data reproducibility and Chromium built-site checks also passed.
  - Khmer Quality [41868942150](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41868942150) **SUCCESS**; 176 tests and 60 subtests passed, plus browser runtime contract and site build checks.
  - Burmese tests [41868956132](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41868956132) **SUCCESS**; 167 tests and 64 subtests passed, generated web data stayed current, npm tests and 54 built-site browser tests passed.
- Final documentation/register/handoff commits also passed their subsequent push CI: Lao [41869194865](https://github.com/ClippyFirst/Lao-Ukrainian-Phonetic-System/actions/runs/41869194865), Khmer [41869262079](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41869262079), and Burmese [41869342234](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41869342234). Exact final PR-head runs are tracked in the PRs.
- The Burmese execution status matrix was updated in the same branch. Lao and Khmer have no separate execution-matrix file; their canonical handoff and linguistic completion register were updated.
- This verifies an engineering fail-closed guard only. The CLI still does not calculate language-specific contrast coverage, and human convention approval, blind workflow evidence, expert adjudication and rights review remain required. No linguistic data or rules changed.
- No local checkout/tests were available in this connector session; all test claims above refer to inspected hosted GitHub Actions logs.


## Mainline merge verification — IPA gold release-profile guard — 2026-11-04

- PR #141 merged to `main` as `4ba59abdc389a797c58216e4e155b8b06408c557`; current main was confirmed at the same SHA immediately after merge.
- Exact PR-head verification: [41870121484](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870121484) **SUCCESS** (177 tests; 60 subtests).
- Exact PR-head browser smoke: [41870121371](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870121371) **SUCCESS**. Post-merge Quality [41870545200](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870545200) **SUCCESS** and Pages [41870545069](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870545069) **SUCCESS**. A duplicate post-merge browser workflow [41870545028](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41870545028) was still installing Chromium at this checkpoint; the exact merged tree had already passed the PR-head browser smoke.
- The branch was based on latest main with zero commits behind at merge; no conflicting PRs were present. The exact diff was reviewed and merged with an expected-head SHA guard.
- The release guard is now on main. Independent expert-adjudicated gold remains 0; this work does not establish phonetic accuracy or benchmark readiness.


## Expert recruitment lead revalidation — 2026-11-04

- Branch: `research/expert-recruitment-leads-20261104`, based on main immediately before this research pass.
- Rechecked official institutional and publication sources for prospective expert reviewers/referral routes; appended a dated, qualification-limited section to `docs/ipa-gold-collection-playbook.md` and added `KHMER-IPA-GOLD-RECRUITMENT-LEADS-001` to the existing completion register.
- Candidate fit is limited to the evidence actually published: no availability, willingness, native target-variety competence, role independence or consent is inferred. No one was contacted. Public institutional emails are included only where published by the institution/research journal.
- The pilot remains blocked on actual recruitment, versioned convention approval, two independent target-variety annotators, separate adjudicator, non-annotating curator, source/item rights and secure blind intake. No IPA labels or gold data were added.
- Hosted CI pending for this branch; no local checkout/tests were available in this connector session.


## Final expert-lead research PR verification — 2026-11-04

- Exact PR head: `f60e682bb423d951cd4c5b5649ecedbe490dbb10`; Quality [41872769175](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41872769175) **SUCCESS** and browser smoke [41872769410](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41872769410) **SUCCESS**. Inspected steps: independent corpus validation, Python suite, deterministic web checks, production build, Chromium install and visible-results smoke all passed.
- The update only improves recruitment evidence. Chem's relationship to his acoustic-model resource is explicitly recorded as a potential conflict; no recruitment, IPA labels, gold data or production phonology changed.
- No local checkout or local tests were available; these results refer only to the hosted GitHub Actions runs linked above.
- The human pilot remains blocked on actual invitations/consent, approved versioned IPA convention, two qualified independent target-variety annotators, separate adjudicator, curator, item-level rights and secure blind intake.


## Agent completion-methodology update — 2026-11-04

- Added the missing Unlazy completion-gate discipline to `AGENTS.md`, pinned to upstream `Leonxlnx/unlazy@16671491f6679ad9378f52604d3bc2415b4120c7`. The update adopts observable acceptance items, evidence-bound manual gates, exact-final-commit re-verification, scoped task decomposition and explicit non-successful handoff for blockers.
- Kept the existing master handoff/status vocabulary and GitHub Actions as canonical. No second ledger framework, Unlazy checker/hooks, runtime dependency, or linguistic behavior was introduced.
- Also retained the existing Superpowers, Matt Pocock and Ponytail methodology references. Their use is constrained by project-specific IPA, source-rights, privacy and fail-closed requirements.
- Documentation PR: #143. Exact-head CI evidence: 41876110596 (Quality SUCCESS), 41876110636 (browser smoke SUCCESS). The PR has been merged to main; post-merge workflow/deployment checks are still being observed where applicable.
- This is an engineering-process improvement only. It does not resolve the external blockers: expert recruitment and approved IPA conventions, independent adjudicated gold, item-level redistribution rights, and controlled blind annotation intake. No people were contacted and no IPA labels or corpus data were added.

## Deterministic rule-engine replacement — 2026-11-11

- Replaced the model-consensus design with RuleBasedKhmerEngine in src/khmer_ua/rule_engine.py; the legacy HybridKhmerEngine name is only a compatibility alias. There is no provider injection, model vote, network call or external runtime in the active engine.
- Runtime path: NFC normalization → Khmer structure/register analysis → exact versioned lexical IPA fixtures or narrowly scoped inherent-vowel rule → longest-match IPA → Ukrainian policy. Unsupported structures are withheld.
- Website copy now explicitly identifies the deterministic local rule path and links to docs/DETERMINISTIC-RULE-ENGINE.md.
- PR [#152](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/152) merged to main as `913e1b2a117022eb3350c3d1957680f0b5db0661` from branch release/deterministic-rule-engine-2026-11-11. Exact main Quality [43018004334](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43018004334), browser smoke [43018004167](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43018004167), and Pages deployment + post-deploy asset smoke [43018004186](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43018004186) all SUCCESS.
- Published service: https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/
- Engineering task DONE_VERIFIED; linguistic coverage remains PARTIAL/PROPOSED. Determinism is verified; phonetic correctness beyond the covered rules/lexical fixtures still requires expert-adjudicated Phnom Penh gold.

## Final deterministic-engine verification — 2026-11-11

- Post-merge hardening on main head `7585b49fdaac5480940d2511f48961f7690bf6b5`: legacy factory now rejects external provider injection; execution trace is named `rule_trace`, not a fabricated evidence-rule identifier.
- Exact-head Quality [43019207054](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43019207054), browser smoke [43019207032](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43019207032), and Pages deployment + asset smoke [43019207026](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43019207026) all SUCCESS.
- Live service: https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/. The Python rule engine and published browser runtime are deterministic and do not use model consensus.
- Remaining linguistic acceptance: independent adjudicated Phnom Penh IPA gold and expanded contextual vowel/coda coverage; no blanket accuracy claim.


## 2026-11-11 continuation — Ukrainian practical transcription

### Repository state
- Starting default-branch SHA: \`2fe36aa1eb64cc47fb60ab1b37561f40d57202a7\`.
- Verified implementation SHA: \`e7b52ae3921b17fb9d0c400eaad913c8c78d2b50\`.
- Final verification branch: \`feat/khmer-ukrainian-practical-adapter-final-2026-11-11\`.
- Draft PR: [#156](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/156), open, not merged.
- Earlier drafts #154 and #155 were closed as superseded; their branches were retained.
- No main-branch modification and no Pages deployment/publication.

### Implemented
- \`src/khmer_ua/practical.py\` now provides the whole-IPA longest-match adapter \`map_ipa_string()\`; \`RuleBasedKhmerEngine\` calls it after IPA derivation. Unknown IPA withholds the complete practical result.
- \`src/ukrainian-practical.js\` is the shared browser adapter imported by \`src/main.js\`; browser and Python adapter behavior is tested against the same machine-readable policy.
- Policy version: \`2026-11-11.3\`.
- Ukrainian-specific choices: /h, ɦ/ → г; /ɡ/ (ASCII /g/) → ґ as a contrast-preserving project choice; /x/ → х; /w, ʋ/ → в; explicit /t͡s, d͡z, t͡ʃ, d͡ʒ/ → ц, дз, ч, дж; /tɕ, dʑ/ → ч, дж as practical approximations; /cʰ/ → ть'.
- Syllable-initial /j/ + transparent vowel uses Ukrainian я/є/ї/ю/йо; /j/ elsewhere remains й. Russian comparator /w/ → у is not copied into Ukrainian.
- The 2026 Ukrainian Orthography is target-language guidance, not evidence about Khmer phonology. It generally uses г for foreign [g] and permits ґ as imitation in personal names; /ɡ/ → ґ remains an explicit project policy.
- Public system page, README, policy documentation, fixture audit and regression tests were updated. Work was text-only; no audio was used.

### Verification evidence
- Quality workflow [43094688835](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43094688835): SUCCESS; 187 Python tests + 62 subtests; deterministic web checks, policy/data validation and production build passed.
- Browser workflow [43094688837](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43094688837): SUCCESS; Chromium 3/3.
- The browser adapter runtime tests exercise yotation, /w/, affricates, whitespace, and fail-closed unknown IPA.

### Task ledger
| Work item | Status | Evidence / acceptance |
|---|---|---|
| Whole-IPA Python adapter integrated after deterministic IPA | DONE_VERIFIED | \`src/khmer_ua/practical.py\`, \`src/khmer_ua/rule_engine.py\`, quality CI |
| Browser adapter shares the canonical policy and passes runtime mapping tests | DONE_VERIFIED | \`src/ukrainian-practical.js\`, \`src/main.js\`, \`tests/web-engine.test.mjs\`, browser/build CI |
| Ukrainian h/g/x, affricates, /w/ and /j/ target conventions documented | DONE_VERIFIED | \`data/ukrainian/practical-policy.json\`, public \`system.html\`, regression tests |
| Empirical correctness of Khmer IPA → Ukrainian target correspondences | PARTIAL | Rules are explicit and deterministic; independent adjudicated gold is still absent |
| Independent text-only Khmer IPA/Ukrainian gold set | BLOCKED | Requires rights-cleared text lexical sources with provenance plus independent native/expert adjudication; acceptance: non-overlapping held-out set, per-phenomenon labels, adjudication record, CER/PER and coverage/abstention report |
| Audio validation | DEFERRED | Explicitly outside this text-only task |

### Next genuine blocker
Create the independent text-only Khmer IPA/Ukrainian adjudication set. Do not promote the proposed correspondences to validated accuracy claims until that evidence exists.

## Verification refresh — Ukrainian practical transcription, 2026-11-11

- Latest implementation branch: `feat/khmer-ukrainian-practical-adapter-final-2026-11-11`; current PR #156 remains open/draft and unmerged. Main remains unchanged at `2fe36aa1eb64cc47fb60ab1b37561f40d57202a7`.
- The canonical Python adapter, browser adapter and target policy are unchanged at the verified implementation baseline; subsequent changes expanded tests and synchronized README, system/implementation/validation documentation and completion records.
- Expanded adapter checks cover /h, ɦ, ɡ, g, x; explicit affricates; plain consonant sequences; /cʰ/ → ть'; /j/ yotation; whitespace and unsupported IPA. No audio was used or required.
- Exact-head quality run [43095329118](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43095329118) and browser smoke [43095329245](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43095329245) are queued with no jobs started at this refresh. Do not report these final runs as passed.
- The independent text-only Phnom Penh IPA/Ukrainian gold set remains BLOCKED by missing independently sourced and adjudicated text labels. This blocks empirical accuracy claims, not deterministic adapter implementation. Audio annotation is DEFERRED by scope.


## Provisional grapheme IPA fallback — continuation 2026-11-11

- Added `docs/provisional-grapheme-ipa-fallback.md` defining the Lao-style `PROVISIONAL` grapheme → IPA → existing Ukrainian adapter contract, visible `?` uncertainty, Python/browser parity and benchmark separation.
- This is a design/acceptance document only, not an implementation claim. Current Khmer parser/practical adapter still withholds unsupported constructions. Implementation is BLOCKED pending a source-backed, positional Khmer grapheme-to-IPA inventory; no context-free letter readings or vowel/tone guesses may be fabricated.


## Provisional onset fallback implementation — 2026-11-11

- Python and browser now expose a separate PROVISIONAL onset-only IPA preview for unresolved units when the existing parser has a registered base-consonant onset IPA.
- The same IPA → Ukrainian adapter is used; the affected Ukrainian unit receives ?. Canonical ipa/ukrainian remain withheld.
- No vowel, coda, subscript/coeng realization or tone is inferred.
- Python regression and browser source-contract regression were added.
- Status: PARTIAL. Dedicated per-grapheme positional source registry, executed browser parity fixtures, exact-head CI and Chromium verification remain outstanding.
- Exact head at this update: 660915e4ed1f44eab04258957eee39537883aadd. Quality and browser workflows 43099931373 / 43099931284 were queued, not passed.


## Final continuation snapshot — 2026-11-11 23:00 +02:00

- Current PR #156 head: ffeb3ee3a46898f1fdf6ab5ac455972bb59f327a. Draft, open, unmerged. Main baseline remains 2fe36aa1eb64cc47fb60ab1b37561f40d57202a7.
- Implemented Python and browser onset-only PROVISIONAL fallback. It uses registered consonant onset IPA → existing IPA adapter → Ukrainian text plus ?. Canonical fields remain withheld.
- Exact-head CI is NOT verified. Earlier quality/browser runs 43100166075 and 43100166123 were queued on head 30f2dc5ee6be90cd75205c742d73f3af41f1523b; the subsequent status-priority correction is at ffeb3ee3a46898f1fdf6ab5ac455972bb59f327a and no workflow run was returned for that exact head.
- Local test execution was unavailable: public GitHub clone attempt failed because the execution environment could not resolve github.com. No tests are claimed passed on the new fallback.
- Remaining: execute Python/Node/Chromium tests on the exact head; add functional shared Python/browser fixtures; register source-backed positional fallback evidence; expand only where vowel/subscript/coeng evidence is explicit. Keep the independent text-only adjudicated gold set BLOCKED and audio DEFERRED.


## Fallback scope clarification — 2026-11-11

The browser preview is separate from canonical output. The onset-only test fixture is ក្ក (known base plus unresolved coeng/subscript), not កា, which is handled by the existing inherent-vowel rule. Exact-head tests after this correction still need completion.


## Verified implementation result — 2026-11-11

- Code/test head dbdb8beafc3454e6bb0be848011f90fb0dea190b.
- Quality workflow 43101322383 PASS: 189 Python tests, 62 subtests, web checks and production build.
- Browser smoke 43101322537 PASS: deterministic web checks, production build and Chromium visible-result check.
- Browser keeps canonical IPA/Ukrainian withholding intact and shows a separate onset-only preview in per-unit details.
- Linguistic feature remains PARTIAL: positional primary-source registry and functional shared Python/browser parity fixtures remain TODO. Independent adjudicated gold remains BLOCKED; audio DEFERRED.


## Complete Unicode grapheme-accounting sweep — 2026-11-12

- PR [#157](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/157) merged as `e9c9d997e6de1029fd0b8fef9e7b6a9cb0020a4f`.
- Added an exhaustive runtime sweep over every assigned Unicode letter and combining mark (general categories L/M) in Khmer U+1780–17FF and Khmer Symbols U+19E0–19FF. Each tested code point must survive segmentation and appear in the parser's grapheme trace with its exact U+ identifier.
- The sweep exposed an early-return trace-loss defect for malformed U+17D2 COENG. The parser now retains the malformed coeng and all remaining code points as `invalid_sequence_component`; it does not invent a pronunciation.
- Added a negative control for U+17F9, which remains explicitly unsupported rather than receiving synthetic IPA.
- Exact PR-head verification: Quality [43184648039](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43184648039) SUCCESS; browser smoke [43184647978](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43184647978) SUCCESS. These runs cover the exact tested branch head `fcae948d8ae30bc0ad606ef4ae4071fffb68be08`.
- **Status:** structural/input accounting for the tested Unicode L/M set is DONE_VERIFIED. This is not 100% Khmer phonological coverage, 100% IPA coverage, or pronunciation accuracy. Vowel × series × length × coda × profile evidence and independent adjudicated gold remain PARTIAL/BLOCKED. Post-merge main workflows were still running at this documentation checkpoint; no post-merge result is claimed.


## Explicitly unmodelled Khmer letters and lossless trace tail — 2026-11-12

- PR [#159](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/159) merged as `d1d184334c806cd21cf2eb875a9c5151ab9e61b3`.
- Added explicit `unmodeled_letter` inventory records, with no IPA, for U+17A3 KHMER INDEPENDENT VOWEL QAQ, U+17A4 QAA, U+179D SHA and U+179E SSO. They remain unsupported by the selected modern Khmer phonology profile until appropriate evidence exists.
- Fixed a second parser trace-loss path: encountering an unknown or explicitly unmodelled code point now preserves the entire remaining source tail as trace components rather than returning after the first unknown code point.
- Regression coverage includes all four unmodelled letters and a mixed sequence `កxយ`, ensuring later graphemes remain present after the unknown `x`.
- Exact PR-head Quality [43186170402](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43186170402) SUCCESS and browser smoke [43186170525](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43186170525) SUCCESS on `b62b9beef65ccfd546c39b05578d0a9f80f48083`.
- **Status:** explicit inventory classification and lossless tail trace are DONE_VERIFIED. The four letters remain phonologically NOT_ESTABLISHED; no pronunciation has been fabricated. Complete positional Khmer IPA and independent gold remain PARTIAL/BLOCKED.



## Ukrainian romanization-target matrix completion — 2026-11-12

- Base `main` at start: `e249adb736c57501300cb27322eed7ea27ab901a`; task branch: `feat/khmer-romanization-ukrainian-matrix-completion-2026-11-12`.
- Updated `data/khmer/romanization_ukrainian.csv`: all 22 PCGN consonant rows now have an explicit Ukrainian target, including `th → т'`, the contextual romanized outputs `b → б` / `p → п`, and the PCGN glottal marker `’ → ʼ`.
- Updated `data/khmer/romanization_vowels_ukrainian.csv`: all 37 official PCGN vowel/rime rows now have a non-empty target rendering. Contextual alternatives remain visible as alternatives and carry `ANALYSIS_DEPENDENT`; no IPA or pronunciation value was inferred.
- Expanded `tests/test_romanization_matrix.py` and `tests/test_romanization_vowel_matrix.py` to require complete target-column coverage and the project orthographic status/notes.
- Updated `docs/romanization-to-ukrainian-matrix.md` with the target convention and a separate acceptance gate. `KHM-ROM-UA-TARGET-001` is DONE_VERIFIED: exact-head Quality [43221517618](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221517618) and browser smoke [43221517788](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221517788) both SUCCESS; push Quality [43221506380](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221506380) SUCCESS. The final Python suite reported 194 passed + 62 subtests. Runtime adapter `KHM-ROM-UA-001` remains TODO, BGN/PCGN engine `KHM-ROM-ENGINE-001` remains PARTIAL, and contextual syllable resolution remains PARTIAL.
- This is a letter-level rendering of Latin BGN/PCGN strings into Ukrainian, not phonetic transcription. The upstream `@gmana/km-translit` output remains a BGN/PCGN-derived ASCII simplifier and does not yet implement the full contextual standard. No IPA labels, source phonology, gold data, or pronunciation accuracy claims changed.
- No local checkout/runtime was available through this connector session. Exact-head GitHub Actions Quality and browser smoke workflows passed on commit `91736b45c32ad5a812f71b97e7594a2f7a8da1bc`; Quality: 194 Python tests + 62 subtests, Node checks and build; browser smoke also passed. The latest follow-up commits are documentation-only.


## Post-merge mainline verification — romanization target matrix — 2026-11-12

- PR #161 merged into `main` as `6b0d0e75d794165e5eb935192fab0926e1efca39`.
- Mainline Quality [43221967799](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221967799), browser smoke [43221968144](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221968144), and Pages deployment [43221967939](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221967939) all SUCCESS on the merge commit.
- Exact feature-head tests [43221517618](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221517618) and browser smoke [43221517788](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43221517788) also passed on `91736b45c32ad5a812f71b97e7594a2f7a8da1bc`: 194 Python tests + 62 subtests, Node checks, build and Chromium smoke.
- `KHM-ROM-UA-TARGET-001` is DONE_VERIFIED. `KHM-ROM-UA-001` remains TODO (runtime Latin-to-Ukrainian adapter); `KHM-ROM-ENGINE-001` remains PARTIAL (the upstream ASCII romanizer is not fully conformant with contextual BGN/PCGN 1972). No IPA or pronunciation claim is implied.


## Khmer romanization → Ukrainian runtime adapter — 2026-11-12

- Started from `main` `3930c8055bcbd6f6747336ad7dce09c9f695f31e`; implementation branch `feat/romanization-to-ukrainian-runtime-2026-11-12`; PR [#164](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/164).
- Added `src/khmer-romanization-ukrainian.js` and wired it to the existing `khmerToLatin` output and the separate “За романізацією” panel. It maps the current Latin result to Ukrainian, preserves non-Khmer text and punctuation, and marks unknown Latin fragments `⟦…⟧`.
- Browser regression: `សុខា → Sokha → Сок'а`; phonetic IPA output remains hidden in romanization mode. Matrix token coverage is tested for consonants and vowel forms.
- **Evidence boundary:** npm package `@gmana/km-translit` documents that its ASCII BGN/PCGN-derived profile drops the standard diacritics and is not fully conformant. The adapter therefore reports `PROVISIONAL`; it cannot recover contextual PCGN vowel distinctions lost upstream. This is not a complete PCGN runtime.
- Exact-head Quality [43226337969](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337969), browser [43226337956](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337956), and push Quality [43226325685](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226325685) SUCCESS on `1fa869c524bac5effc98411b71e47e458ad584ae`.
- `KHM-ROM-UA-001`: PARTIAL (runtime display adapter works for current ASCII profile; full diacritic/context coverage is blocked by upstream romanizer output loss). `KHM-ROM-UA-TARGET-001`: DONE_VERIFIED. `KHM-ROM-ENGINE-001`: PARTIAL. No IPA or pronunciation claim is made.



Exact-head Quality [43226337969](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337969), browser [43226337956](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226337956), and push Quality [43226325685](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43226325685) SUCCESS on code head `1fa869c524bac5effc98411b71e47e458ad584ae`. Quality: 194 Python tests + 62 subtests; web checks and production build passed; Chromium visible-results smoke passed.


## Khmer romanization runtime — mainline post-merge verification — 2026-11-12

- PR [#164](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/164) merged as `0ba6107a7e5cb09cca44021669a7401fc125eac4`.
- Mainline Quality [43227360792](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360792), browser smoke [43227360789](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360789), and Pages deployment [43227360801](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43227360801) all SUCCESS.
- The merged implementation remains deliberately PARTIAL/PROVISIONAL: the upstream ASCII romanizer omits PCGN diacritics; this adapter cannot reconstruct lost contextual vowel distinctions. The IPA route remains separate.


## Romanization mainline reconciliation — 2026-11-12

### New research blocker: Cambodian national 1997 profile

The national report submitted by Cambodia to UNGEGN (GEGN.2/2023/104/CRP.104) says the romanized writing system used in Cambodia is based on the 1997 transcription system rather than the 1972 transliteration system; it also reports the 2019 gazetteer used the 1997 system. The UNGEGN Working Group status report (GEGN.2/2023/11/CRP.11) independently records that the 1997 system replaced the 1972 system. Therefore BGN/PCGN 1972 remains a source-backed project research profile only, not a claim about the current national Cambodian profile. The complete primary 1997 specification remains unlocated. Do not substitute the Library of Congress ALA-LC Khmer 1997 table; it is a different cataloguing profile. Acceptance: obtain the national 1997 table, source-locate its rows, compare against the existing BGN/PCGN matrix, and decide whether a second profile is required.


- Current `main`: `a86a59cf082d547563b45374ced9dfb45c5cd8db`.
- Preserved merged sequence: target-matrix completion PR #161 (`6b0d0e75d794165e5eb935192fab0926e1efca39`); matrix synchronization PR #163 (`3930c8055bcbd6f6747336ad7dce09c9f695f31e`); provisional runtime PR #164 (`0ba6107a7e5cb09cca44021669a7401fc125eac4`); post-merge evidence PR #165 (current mainline checkpoint).
- Current-head CI: Quality [43228414756](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414756), browser [43228414938](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414938), Pages [43228414646](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414646): all SUCCESS.
- Current ledger: target matrix DONE_VERIFIED (22 consonant + 37 vowel/rime rows); runtime PARTIAL (independent adapter integrated, provisional); source romanizer PARTIAL (ASCII profile loses PCGN diacritics and contextual vowel distinctions); contextual whole-standard BGN/PCGN implementation remains open.
- Open draft research PR #153 remains untouched. It is a separate G2P/provider integration, not a dependency of the romanization adapter.
- No local checkout was available in this connector-only session; verification cited here is hosted GitHub Actions on exact current `main`. No local pytest/npm/Playwright execution is claimed.

The 2025 UNGEGN Asia South-East Division report (GEGN.2/2025/73/CRP.73, p. 3) confirms the October 2023 national gazetteer also uses the 1997 transcription system: https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_73_CRP73_item4a.pdf


## Post-runtime test closeout — 2026-11-12

- Latest implementation mainline commit: `f0485892f5d4b16e5fbe0ded6f8e083d8b044f4b` (PR #167, test execution coverage; merged).
- Corrected a real test-discovery gap: `tests/romanization-ukrainian.test.mjs` is now run by both `npm test` and `npm run check`. Added coverage for all 22 distinct PCGN consonant romanization tokens; the existing suite covers the 33 ASCII vowel candidates, unsupported units, passthrough and status behavior.
- Exact-main Quality [43250158336](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43250158336) and browser smoke [43250158628](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43250158628) passed on the implementation commit. Pages deployment was checked separately in run [43250158415](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43250158415).
- Remaining acceptance: source-matrix→runtime parity for every row, marks/numerals, real-package corpus tests, diacritic-preserving BGN/PCGN, and a separate evidence-gated decision on Cambodia's national 1997 system. Do not promote PROPOSED mappings or provisional output.
