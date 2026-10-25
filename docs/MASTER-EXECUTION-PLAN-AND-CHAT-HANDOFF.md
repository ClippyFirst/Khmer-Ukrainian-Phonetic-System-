# Master execution plan and chat handoff — Khmer → Ukrainian

**Last updated:** 2026-10-24  
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
- ipa.render_ipa_profile() uses a regex for onset-cluster /r/-loss. Verify that its scope is adequately constrained by the cited dialect evidence before treating it as a robust colloquial phonetic model.

## Prioritized task register

| ID | Task | Priority | Status | Dependencies | Acceptance / verification |
|---|---|---|---|---|---|
| KH-VOW-001 | Expand vowel matrix using attested orthographic patterns, register, vowel sign, coda and profile | P0 | IN_PROGRESS | authoritative source extraction | Every row has source, confidence, IPA status, and test or explicit unresolved status; no arbitrary Cartesian product. PR #41 merged as `08fe98a88f5e3c0c3a21519b6cdc2024992d2f02`; evidence-gate CI [40210193894](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40210193894) passed source/status/conflict validation. Initial source-indexed rows are in matrix commit 9b7936c. |
| KH-VOW-002 | Verify vowel-sign inventories and contextual effects against Unicode + specialist phonology + acoustic literature | P0 | IN_PROGRESS | KH-VOW-001 | Orthographic inventory and R12A contextual descriptions reviewed; acoustic study and unresolved source/version differences still need review. Distinguish orthographic evidence from phonetic evidence. |
| KH-CODA-001 | Add coda-conditioned and syllable-structure cases, including NIKAHIT and REAHMUK | P0 | IN_PROGRESS | KH-VOW-001 | Source-indexed contrasts identified; conservative parser tests now assert that NIKAHIT/REAHMUK preserve structure without fabricating IPA (commit 262cffd). The NIKAHIT pairs are present in Unicode 17.0; independent lexical/phonetic adjudication remains open. |
| KH-IPA-001 | Audit parser-to-IPA API boundary and status semantics | P0 | IN_PROGRESS | matrix + model review | Python API contract tests in e4ff446 separate structural success from phonetic success. Browser shows a visible provisional notice and per-unit evidence breakdown. The unknown/mixed-script guard from PR #35 was merged into `main` as `a4912d520077f3e0df4e7236ae8784d8245354ff`; exact-main CI [40196341065](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40196341065) passed Python tests, web checks and site build. Follow-up PR #37 is now merged as `e39143cf5d880214765fff8f5a237e58d24ab00b`: browser parsing also rejects unknown material inside a Khmer unit, matching Python. Exact-head CI [40197626232](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40197626232) passed. General IPA generation, vowel/coda context coverage, and independent gold remain open; the overall task stays IN_PROGRESS. |
| KH-TEST-001 | Expand independently adjudicated lexical corpus | P0 | IN_PROGRESS | source review | Source-attested examples are now explicitly distinguished from independently adjudicated gold; build a held-out corpus with profile/audio adjudication before scoring |
| KH-REG-001 | Check helper register resolver against shifter-aware parser | P1 | DONE_VERIFIED | code-path review | PR #39 merged as `a0f5f6a272f10d79d5c383bf717363b5e18b053f`. Shared six-case JSON contract is consumed by Python and browser tests; both runtimes agree on effective register, rule ID and structural status for valid, ineligible and multiple shifters. Exact-head CI [40209903755](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40209903755) passed pytest, web checks and build. | The orthographic register resolver is verified. Inherent-vowel IPA quality, the full vowel/coda context matrix, and colloquial phonetics remain separate IN_PROGRESS research tasks. |
| KH-PROFILE-001 | Validate colloquial /r/-loss transform scope | P1 | TODO | primary phonetic sources | Explicitly supported environments only, with profile tests; unresolved cases remain unchanged |
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
