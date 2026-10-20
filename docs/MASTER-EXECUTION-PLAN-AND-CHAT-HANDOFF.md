# Master execution plan and chat handoff — Khmer → Ukrainian

**Last updated:** 2026-10-20  
**Repository:** https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-  
**Default branch:** main  
**Last audited base revision:** 6cc30bb48bedb83d86534a5fbff92839e26673dd  
**Current work commit:** 65c474768ef3db9f95573dfe443ee6fc9bcc41d7 (adds the vowel coverage matrix)

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
- docs/audits/2026-10-20-vowel-coverage-matrix.md was added in commit 65c474768ef3db9f95573dfe443ee6fc9bcc41d7. It contains representative evidence-bearing rows and an explicit list of uncovered dimensions. It is intentionally not an exhaustive or fully adjudicated matrix.
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
| KH-VOW-001 | Expand vowel matrix using attested orthographic patterns, register, vowel sign, coda and profile | P0 | IN_PROGRESS | authoritative source extraction | Every row has source, confidence, IPA status, and test or explicit unresolved status; no arbitrary Cartesian product |
| KH-VOW-002 | Verify vowel-sign inventories and contextual effects against Unicode + specialist phonology + acoustic literature | P0 | TODO | KH-VOW-001 | Distinguish orthographic evidence from phonetic evidence and record contradictions |
| KH-CODA-001 | Add coda-conditioned and syllable-structure cases, including NIKAHIT and REAHMUK | P0 | TODO | KH-VOW-001 | Provenance-bearing positive and negative fixtures; conservative unsupported outcomes |
| KH-IPA-001 | Audit parser-to-IPA API boundary and status semantics | P0 | TODO | matrix + model review | No false deterministic IPA; status accurately distinguishes structure from phoneticization |
| KH-TEST-001 | Expand independently adjudicated lexical corpus | P0 | TODO | source review | Multiple vowel series, complex vowels, codas, coeng clusters, shifters, loans/proper names; each item with source/profile/adjudication |
| KH-REG-001 | Check helper register resolver against shifter-aware parser | P1 | TODO | usage search | No inconsistent effective register in any production path; tests prove behaviour |
| KH-PROFILE-001 | Validate colloquial /r/-loss transform scope | P1 | TODO | primary phonetic sources | Explicitly supported environments only, with profile tests; unresolved cases remain unchanged |
| KH-UI-001 | Browser runtime, mobile viewport, accessibility and visual audit | P1 | TODO | stable engine cases | Keyboard/focus, accessible labels/statuses, responsive checks; screenshot inspection where available |
| KH-REL-001 | License, CITATION.cff, release and Zenodo metadata review | P2 | TODO | authorship/license/data provenance decisions | Metadata accurate, source/data licensing checked, reproducible release archive; no invented author claims |
| KH-DOC-001 | Methodology note: “Khmer-to-Ukrainian Transcription: Register-Conditioned Vowels and Conservative IPA Analysis” | P1 | TODO | KH-VOW-001/002, KH-IPA-001 | Clearly separates orthography, phonology, broad IPA, phonetic profile, Ukrainian proposal and limits |

## Next concrete action

Continue with KH-VOW-001 / KH-VOW-002: inspect the full sign and consonant inventories and the exact source descriptions; produce an evidence-indexed list of attested templates before adding any IPA mappings. Then identify the highest-value uncovered contexts and add tests that explicitly mark unsupported cells as unresolved. Avoid speculative runtime changes until source-supported expected outputs are available.

## Work log

### 2026-10-20 — audit continuation
- Reviewed repository tree and metadata, latest commits, existing implementation plan, repository audit, vowel/register/source data, parser, phonology helper, IPA profile helper, validation documentation, lexical corpus, adversarial corpus, package scripts, and CI workflow.
- Confirmed base revision's Quality checks run 177 and Pages deployment run 187 were successful on 2026-10-09.
- Created docs/audits/2026-10-20-vowel-coverage-matrix.md (commit 65c474768ef3db9f95573dfe443ee6fc9bcc41d7).
- No local Python/npm test command was run in this work cycle; the GitHub Actions run for the new commit must be checked before marking its checks verified.
