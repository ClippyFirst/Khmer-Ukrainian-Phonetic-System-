# Master execution plan and chat handoff — Khmer → Ukrainian

**Last updated:** 2026-10-20  
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
| KH-VOW-001 | Expand vowel matrix using attested orthographic patterns, register, vowel sign, coda and profile | P0 | IN_PROGRESS | authoritative source extraction | Every row has source, confidence, IPA status, and test or explicit unresolved status; no arbitrary Cartesian product. Initial source-indexed rows are in matrix commit 9b7936c. |
| KH-VOW-002 | Verify vowel-sign inventories and contextual effects against Unicode + specialist phonology + acoustic literature | P0 | IN_PROGRESS | KH-VOW-001 | Orthographic inventory and R12A contextual descriptions reviewed; acoustic study and unresolved source/version differences still need review. Distinguish orthographic evidence from phonetic evidence. |
| KH-CODA-001 | Add coda-conditioned and syllable-structure cases, including NIKAHIT and REAHMUK | P0 | IN_PROGRESS | KH-VOW-001 | Source-indexed contrasts identified; conservative parser tests now assert that NIKAHIT/REAHMUK preserve structure without fabricating IPA (commit 262cffd). The NIKAHIT pairs are present in Unicode 17.0; independent lexical/phonetic adjudication remains open. |
| KH-IPA-001 | Audit parser-to-IPA API boundary and status semantics | P0 | IN_PROGRESS | matrix + model review | Python API contract tests in e4ff446 separate structural success from phonetic success. Browser shows a visible provisional notice for overall PROPOSED results via getStatusNotice(); tests in 9f4d583 cover notice text/status classes. The UI now also renders a per-unit breakdown with source, status, IPA, Ukrainian form and explanatory note using DOM textContent (commits e1a2ba7 and 479eda6). Quality run 209 and Pages run 219 for latest styling commit were queued at last check; verify both. Continue auditing fixture-level claims and per-unit display for long-input usability. |
| KH-TEST-001 | Expand independently adjudicated lexical corpus | P0 | TODO | source review | Multiple vowel series, complex vowels, codas, coeng clusters, shifters, loans/proper names; each item with source/profile/adjudication |
| KH-REG-001 | Check helper register resolver against shifter-aware parser | P1 | IN_PROGRESS | code-path review | Shared resolver implemented and parser/helper regression tests added in commits 37d8e5d, 7d3abf4, b45ecbd2. Python test step passed in Quality run 193; finish checking web/build steps and inspect any remaining call sites before marking complete. |
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

