# Master execution plan and chat handoff — Khmer → Ukrainian

**Last updated:** 2026-10-20  
**Repository:** https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-  
**Default branch:** main  
**Last audited base revision:** 6cc30bb48bedb83d86534a5fbff92839e26673dd  
**Recent audit commits:** 9b7936c24b7ec584797d9e47aeb835afd670d091 (source-indexed matrix expansion), 65c474768ef3db9f95573dfe443ee6fc9bcc41d7 (initial matrix), 03e94ced1a2c319c462d53b681a3d61d348e1525 (handoff), b045495275b367c69a8e4c4ed8107faeb4724eb2 (plan links). Recheck latest main SHA and Actions runs before further work.

## Mandatory instructions for the next session

1. Read this document first, then docs/audits/2026-10-20-vowel-coverage-matrix.md, docs/repository-audit.md, docs/superpowers/plans/2026-10-05-khmer-repository-finalization.md, docs/validation.md, docs/phonology.md, data/khmer/vowels.json, data/khmer/registers.json, data/khmer/sources.json, src/khmer_ua/parser.py, src/khmer_ua/phonology.py, src/khmer_ua/ipa.py and the related tests.
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
- Source review confirms R12A's representative register-conditioned examples (ក vs គ; កី vs គី; កា vs គា), coda-sensitive contrasts (លង vs ល្ង), and that NIKAHIT/REAHMUK can affect both coda and nucleus. Unicode 17 is used as orthographic/illustrative evidence, not acoustic validation. Explicit NIKAHIT minimal contrasts currently found in the retrieved text came from Unicode 16; they are marked blocked pending verification against current sources before being promoted to gold fixtures.
- Firecrawl research search was unavailable because the connected Firecrawl account reported insufficient credits; do not retry that connector this session. R12A links to Chem & Chem (2020) acoustic study DOI 10.61945/cjbar.2020.2.2.3; the primary study still needs a targeted review before acoustic claims are strengthened.
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
- The current parser helper phonology.resolve_register() reads the base consonant's inherent register and does not itself apply shifters. Check whether it is called by production paths and either unify it with parser's effective-register resolver or document/test its narrower contract. Do not patch blindly without usage analysis.
- ipa.render_ipa_profile() uses a regex for onset-cluster /r/-loss. Verify that its scope is adequately constrained by the cited dialect evidence before treating it as a robust colloquial phonetic model.

## Prioritized task register

| ID | Task | Priority | Status | Dependencies | Acceptance / verification |
|---|---|---|---|---|---|
| KH-VOW-001 | Expand vowel matrix using attested orthographic patterns, register, vowel sign, coda and profile | P0 | IN_PROGRESS | authoritative source extraction | Every row has source, confidence, IPA status, and test or explicit unresolved status; no arbitrary Cartesian product. Initial source-indexed rows are in matrix commit 9b7936c. |
| KH-VOW-002 | Verify vowel-sign inventories and contextual effects against Unicode + specialist phonology + acoustic literature | P0 | IN_PROGRESS | KH-VOW-001 | Orthographic inventory and R12A contextual descriptions reviewed; acoustic study and unresolved source/version differences still need review. Distinguish orthographic evidence from phonetic evidence. |
| KH-CODA-001 | Add coda-conditioned and syllable-structure cases, including NIKAHIT and REAHMUK | P0 | IN_PROGRESS | KH-VOW-001 | Source-indexed contrasts identified; add provenance-bearing positive/negative fixtures only after IPA/profile adjudication. Unicode 16 NIKAHIT pairs remain blocked pending current-source verification. |
| KH-IPA-001 | Audit parser-to-IPA API boundary and status semantics | P0 | TODO | matrix + model review | No false deterministic IPA; status accurately distinguishes structure from phoneticization |
| KH-TEST-001 | Expand independently adjudicated lexical corpus | P0 | TODO | source review | Multiple vowel series, complex vowels, codas, coeng clusters, shifters, loans/proper names; each item with source/profile/adjudication |
| KH-REG-001 | Check helper register resolver against shifter-aware parser | P1 | TODO | usage search | No inconsistent effective register in any production path; tests prove behaviour |
| KH-PROFILE-001 | Validate colloquial /r/-loss transform scope | P1 | TODO | primary phonetic sources | Explicitly supported environments only, with profile tests; unresolved cases remain unchanged |
| KH-UI-001 | Browser runtime, mobile viewport, accessibility and visual audit | P1 | TODO | stable engine cases | Keyboard/focus, accessible labels/statuses, responsive checks; screenshot inspection where available |
| KH-REL-001 | License, CITATION.cff, release and Zenodo metadata review | P2 | TODO | authorship/license/data provenance decisions | Metadata accurate, source/data licensing checked, reproducible release archive; no invented author claims |
| KH-DOC-001 | Methodology note: “Khmer-to-Ukrainian Transcription: Register-Conditioned Vowels and Conservative IPA Analysis” | P1 | TODO | KH-VOW-001/002, KH-IPA-001 | Clearly separates orthography, phonology, broad IPA, phonetic profile, Ukrainian proposal and limits |

## Next concrete action

1. Review Chem & Chem (2020) directly and extract the actual sample/dialect, vowel categories, acoustic measurements and conclusions; record which claims it supports rather than relying on the title or secondary summary.
2. Compare R12A's coda-mark pages (especially NIKAHIT/REAHMUK) with Unicode 17.0 and a specialist lexical source. Resolve the Unicode 16 vs 17 provenance of explicit NIKAHIT contrast examples before they become gold fixtures.
3. Inspect the current tests for existing coverage of the newly indexed examples. Add tests only where expected outputs are sourced and unambiguous; otherwise add explicit unresolved/unsupported expectations.
4. Then continue KH-IPA-001 API-boundary review and KH-REG-001 usage search. Do not add deterministic vowel mappings merely to make the matrix look full.

## Work log

### 2026-10-20 — audit continuation
- Reviewed repository tree and metadata, latest commits, existing implementation plan, repository audit, vowel/register/source data, parser, phonology helper, IPA profile helper, validation documentation, lexical corpus, adversarial corpus, package scripts, and CI workflow.
- Confirmed base revision's Quality checks run 177 and Pages deployment run 187 were successful on 2026-10-09; these are historical and do not validate newer documentation commits.
- Created initial matrix (commit 65c474768ef3db9f95573dfe443ee6fc9bcc41d7), handoff (commit 03e94ced1a2c319c462d53b681a3d61d348e1525), and plan links (commit b045495275b367c69a8e4c4ed8107faeb4724eb2).
- Expanded the evidence matrix with R12A/Unicode 17 source-indexed examples, coda-sensitive patterns, independent-vowel caveats, and source-version limitations (commit 9b7936c24b7ec584797d9e47aeb835afd670d091).
- Opened R12A notes updated 2026-04-27, especially sections on registers, vowels, codas, NIKAHIT/REAHMUK, and independent vowels; reviewed Unicode 17 Chapter 16 for script examples and register shifters. Unicode 16 was used only to identify explicit NIKAHIT contrast examples, which remain blocked pending verification against current sources.
- Firecrawl research search could not run because its connected account reported insufficient credits; no retries were made. No local Python/npm tests were run. Check current Actions/Pages runs for commit 9b7936c before claiming the documentation pipeline is green.
