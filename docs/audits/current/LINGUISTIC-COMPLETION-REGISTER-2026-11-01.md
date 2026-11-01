# Khmer linguistic completion register — 2026-11-01

**Baseline:** `main` `c0a2b33c86791b6546e1158c62043fd23acc1f60`.
**Latest exact-main engineering evidence:** Quality [41326462947](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41326462947) and Pages/deployed smoke [41326462993](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41326462993) succeeded.
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
