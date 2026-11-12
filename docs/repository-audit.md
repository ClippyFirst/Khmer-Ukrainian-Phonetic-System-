# Repository audit — 2026-10-05

## Identity

The repository is a Khmer → Ukrainian research system. The active implementation is Python/data driven and the target is contemporary Khmer with explicit pronunciation-profile separation.

## Inventory decision

| Area | Classification | Action |
|---|---|---|
| README/docs | CORE/DOCUMENTATION | keep and revise |
| data/khmer | CORE/SUPPORTING DATA | keep; correct provenance |
| data/comparative | RESEARCH EVIDENCE | keep |
| data/ukrainian | CORE | keep as proposed policy |
| src/khmer_ua | IMPLEMENTATION | keep; expose new API |
| tests | VALIDATION | keep and expand |
| schemas | SUPPORTING DATA | keep |
| scripts/coverage.py | SUPPORTING/UTILITY | keep until benchmark generation is implemented |
| git/OS/IDE debris | ARTIFACT | none found in tracked tree |
| foreign-language project content | FOREIGN | none found in tracked tree |
| duplicate authoritative mapping tables | TECHNICAL DEBT | reduced by making data/khmer and data/ukrainian the active sources of truth |

## Historical material

The repository history contains useful milestones: initial foundation; orthographic syllable segmentation fix; data-driven register/rule layer; comparative Cyrillic research; Ukrainian practical target layer. These commits remain useful provenance and are not rewritten away.

## Important audit finding

The previous consonant table attached IPA evidence directly to the Unicode source ID. This was too strong: Unicode establishes script structure, not the complete modern phonetic realization. The active table now cites a specialist orthography/phonology reference for phonetic values while retaining Unicode for orthographic structure.

## No destructive cleanup

No unique research dataset or historical analysis was deleted. The repository was small enough that archiving large historical trees would have added complexity without improving the active research workflow.


## Transcription edge-case audit — 2026-10-06

A focused adversarial review found several practical-layer weaknesses that were too easy to miss in ordinary examples:

- register shifters ៉ / ៊ were parsed as generic signs instead of changing the effective register;
- the exceptional ប៉ construction was not represented as the /p/ realization it encodes;
- /c/ had been mapped to Ukrainian ч even though the source phoneme is conventionally represented as [c], making ть a closer Ukrainian practical approximation;
- /h/ had been mapped to г, which is weaker phonetically than х for the source [h];
- /w/ and /ʋ/ were unnecessarily collapsed in the practical policy;
- the representative /kiə/ example was written as «кіа», which was corrected to «кіє» as a more transparent Ukrainian sequence.

The new adversarial corpus includes ខ្ញុំ, សង្គ្រាម, ហើយ, ស៊ី, សញ្ញា, ច្រើន, ប៉ី and a negative multiple-shifter case. These are regression fixtures, not a claim of complete lexical coverage. The parser now explicitly records register-shifter decisions and flags multiple-shifter structures as EVIDENCE_LIMITED.

External evidence used for this review: Unicode Khmer encoding/register documentation; R12A Khmer orthography notes; and the documented Khmer-Russian practical transcription tradition as a comparator. The Ukrainian layer remains a project proposal and still requires an adjudicated Ukrainian corpus before empirical accuracy can be claimed.


## Final consistency pass — 2026-10-06

The web-facing explanation was re-audited against the canonical Ukrainian policy and the adversarial parser work. A stale system-page table was found and removed: the page now agrees with the policy for /c/ → ть, /cʰ/ → ч, /h/ → х, /ʋ/ → в and /w/ → у. The current `src/khmer_ua/ipa.py` contains a regex-based Phnom Penh /r/-loss profile transformation. Its test coverage is minimal and its environments have not been independently validated against a full source-backed matrix; treat this as provisional and audit before expanding it. This is a remaining inconsistency with earlier documentation that said the transformation had been removed.

The web fixture corpus includes Unicode/R12A representative cases for register shifters, coeng clusters, pre-base vowels, long vowels, repeated nyo, coeng-r and the ប៉ exception, plus a negative multiple-shifter case. For representative Unicode examples, the corpus keeps the Unicode 17 IPA forms even where lexical dictionaries provide alternative phonetic analyses.

The system page and web structural tests now explicitly guard against stale transcription mappings. Academic paragraph-logic review of the updated system page returned no issues.

Pipeline status is revision-specific. Check the latest Quality and Pages workflow runs before asserting a green build; successful CI remains separate from linguistic accuracy validation.


## External IPA and benchmark audit — 2026-10-24

- The Python/browser profile-boundary correction and fail-closed gold-provenance gate are merged; ADJUDICATED rows require non-empty IPA, source_id and profile.
- Khmer Phonemizer 0.0.3 completed 6 probes with 0 runtime errors in [run 40121359605](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/40121359605). The report records raw phone-token arrays, but they are not directly string-comparable to source IPA until tokenization, syllabification, stress and notation conventions are reconciled.
- Independent gold count remains 0 and accuracy is null. Do not promote source-attested but unadjudicated examples into the score denominator. The remaining acceptance gate is a representative, source-located, independently adjudicated Khmer corpus and expert review of the Phnom Penh /r/-loss profile.
- Latest smoke artifact ZIP SHA-256: `3cd5ad913909cd1ff692c192614f354b707f705c1b6a2f1dc7ad971a4baf63a5`.


## Ukrainian target-policy audit — 2026-10-30

**Status: DONE_VERIFIED for the scoped target-policy change; broader Khmer phonology remains PARTIAL.**

- The canonical practical policy now marks aspirated IPA with an ASCII apostrophe after the Ukrainian base consonant, including the existing colloquial /cʰ/ profile.
- /h/ maps to г, /ɡ/ to ґ, and genuine /x/ to х. The policy does not equate foreign /h/ phonetically with Ukrainian /ɦ/.
- Ukrainian affricate mappings include /t͡s/ → ц, /d͡z/ → дз, /t͡ʃ/ and /tɕ/ → ч, /d͡ʒ/ and /dʑ/ → дж. Supported palatalization is kept explicit; sequences are not automatically fused.
- /ʔ/ is not aspiration and does not generate the marker.
- Python tests passed (82 tests, 25 subtests); the complete web check workflow passed in [41076121018](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41076121018).
- Draft PR #59 carries the changes; PR #58 is not modified. No merge or deployment was performed.
- No new pronunciation source or gold label was fabricated. Existing independent lexical/audio adjudication remains absent; this target-policy change does not increase accuracy evidence.


## Final romanization / dual-method audit — 2026-10-31

- PR #65 records BGN/PCGN 1972 as the selected reference profile, supported by UNGEGN and the official PCGN guide. It is not represented as a reversible or official Cambodian national orthography.
- PR #66's first data draft was superseded by PR #67 after direct PCGN 2017 PDF reconciliation. The canonical data file now contains exactly the 22 official consonant/subscript rows, with exact source units and the U+2019 apostrophe marker; row 18 notes that ឡ has no subscript form. Tests validate exact source sequences, romanization values, source locators and uncertainty statuses.
- PR #68 adds separate phonetic and romanization tabs. Phonetic remains IPA-first. Romanization displays the current BGN/PCGN-derived Latin output and an explicit PARTIAL Ukrainian state; no phonetic fallback is permitted.
- Main quality workflow [41230505480](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41230505480) passed on a351b0f66a608d7b4372e7c7bd0179808488be70.
- Pages deployment [41230505474](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41230505474) succeeded at https://clippyfirst.github.io/Khmer-Ukrainian-Phonetic-System-/ and deployed a351b0f66a608d7b4372e7c7bd0179808488be70.
- Remaining: the @gmana ASCII simplifier is not fully conformant to PCGN 1972; the contextual vowel/shortening/coda/diacritic/numeral matrix is not yet canonical machine-readable data; the independent syllable-level romanization → Ukrainian adapter is not implemented; independent lexical IPA gold remains 0. This is still a research prototype, not a validated production transcription standard.


## Romanization inventory CI reconciliation — 2026-10-31

- Latest repository head before this audit update: `ec75558c862666f38496cdbc02443e3885bf5202`.
- The exact-head PCGN inventory workflow [41233203184](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41233203184) completed successfully. Its `test` job completed Python tests, web checks and the site build without a failed step.
- The 37-row vowel-source inventory and 16-row marks/numerals inventory now have exact source-glyph/romanization test evidence. Their bounded inventory tasks are `DONE_VERIFIED`; the complete context-dependent vowel/rime matrix and runtime semantics remain `PARTIAL`.
- The broader romanization test task remains `PARTIAL`: mixed-script, punctuation, malformed-unit and ambiguity coverage still requires explicit acceptance tests. The BGN/PCGN runtime implementation and independent romanization → Ukrainian syllable adapter remain incomplete.
- This run does not change phonetic evidence: independent lexical IPA gold remains 0, the contextual source-to-IPA algorithm is incomplete, and no accuracy metric is justified.
- No runtime code or Pages build inputs changed in the inventory/documentation checkpoint. The live Pages deployment evidence remains the earlier successful deployment recorded above; this checkpoint did not trigger a new deployment.
- Next work should prioritize the official PCGN context rules and the source-aware vowel/rime × consonant-series × shortening × coda representation. Ukrainian candidates must remain unassigned where the evidence does not support them.


### Exact workflow log verification detail — 2026-10-31

Workflow [41233203184](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41233203184), job 124631488043, was inspected directly:
- pytest -q: **87 passed, 25 subtests passed**.
- npm run check: all configured web-engine, runtime, register-shifter and romanization checks passed.
- npm run build: Vite production build passed, emitting the service and methodology pages plus asset bundles.
- Non-fatal warnings: Node punycode deprecation and npm install-script advisory. No workflow step failed.
- This is exact-head software verification of the bounded inventory, not evidence of full PCGN contextual coverage or phonetic accuracy.

 
### Responsive layout merge — 2026-10-31

- PR #78 merged as `3b6e08177f9c90dddb27e787cc7a6deaa015c33e`; 53 CSS override lines added to `src/styles/main.css`.
- Exact-head CI [41234615041](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41234615041) passed Python tests, configured web checks and Vite production build.
- Existing IPA/method-switch styling was preserved. PR #64 remains open and unmerged because its branch is diverged and its stylesheet replacement risks regressing newer UI.
- This is UI verification only. Contextual PCGN runtime, complete vowel/rime matrix, independent Ukrainian adapter, and adjudicated phonetic gold remain incomplete. No Pages deployment is claimed here.


### Sentence-level source-preservation regression — 2026-10-31

- PR #80 merged as `14113b5d45bbd36e53510b24a6f48f565a54bcd0`; exact-head Quality CI [41238197962](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41238197962) passed Python tests, Node runtime/web checks, and Vite build.
- The supplied Khmer sentence is now covered by a regression that reconstructs the complete normalized source from rendered engine units, including spaces and punctuation.
- The check does not add IPA or Ukrainian lexical gold. Full contextual Khmer phonology, BGN/PCGN runtime, independent romanization-to-Ukrainian adapter, and adjudicated corpus remain incomplete.
- Pages deployment [41237778259](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41237778259) succeeded on `cb48d4c660d3e7f826c677d871654157914ae59c`; no deployment is attributed to the test-only PR.


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

## Full-sentence Khmer romanization integration — 2026-10-31

- PR #87 merged as \`7d058faaf02ebf542fedc8b186d11a88c5318ec4\`; exact-head Quality CI [41240282424](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41240282424) passed Python (87 + 25 subtests), Node checks and Vite build.
- PR #89 merged as \`076ffaa1523afa7cc9ec9b8c2ca8e3a83cea101f\`; exact-head Quality CI [41241149726](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41241149726) passed the same configured gates.
- Runtime now passes the whole input directly to \`khmerToLatin\`; test coverage checks the exact greeting sentence, full conversion of Khmer letters/signs, and preservation of spaces, \`!\`, and both \`។\` punctuation marks. The package documents whole-text whitespace/punctuation handling and repetition-mark behavior: https://www.npmjs.com/package/@gmana/km-translit.
- The test does not claim word segmentation inside unspaced Khmer runs, complete PCGN 1972 conformance, or an independent Ukrainian adapter. Those remain PARTIAL/TODO; independent lexical IPA gold remains 0.
- PR #88 was closed as superseded due its stale base and incorrectly escaped regex. PR #64 remains open and unmerged; no CSS replacement was ported. No post-merge Pages deployment is claimed.

## Short Khmer mixed-text romanization regression — 2026-10-31

- PR #92 merged as \`99638ea6758d1553f3853d163c4b42ad8fe0741d\`; exact-head Quality workflow [41242382955](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41242382955) passed Python, Node web checks and Vite build.
- The short sample \`សួស្តី 123! ភាសាខ្មែរ។\` verifies that ASCII digits, spaces, \`!\` and Khmer \`។\` survive the whole-text romanizer while Khmer letters convert. Tests only; no runtime or Pages input changed. Not linguistic gold.


## Native numerals and mixed Latin preservation — 2026-10-31

- PR #94 merged as `48e5d6c05d4a6ade8019c853135b7e2f6d655591`; exact PR-head Quality checks [41242836968](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41242836968) and [41242823462](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41242823462) passed.
- `២០២៦ ABC-42, សួស្តី។` verifies preservation or explicit Arabic rendering of Khmer numerals, ASCII digits, Latin text, spaces, comma and Khmer sentence-stop punctuation while converting Khmer letters. This is not PCGN numeral gold or proof of complete word segmentation/UA adaptation.
- PR #92 covers ASCII-number mixed text; PR #89 covers a full greeting sentence. Tests only; no runtime or Pages input changed.


### Main-head CI and Pages verification — 2026-10-31

- Current main `1a6921fc75dd011bc8097f6636b8077fc7c59cff` passed Quality workflow [41243972009](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41243972009) and Pages deployment [41243971788](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41243971788). The deploy job's deployed-site/runtime smoke test passed.
- Whole-text romanization coverage on main includes full/short sentences, native and ASCII numerals, Latin mixed text, whitespace and Khmer punctuation. The phonetic route continues to withhold unsupported contextual analyses rather than substituting romanization or guesses.
- PR #64 remains open and unmerged because its branch is diverged and its stylesheet replacement is broader than the focused responsive change already merged in PR #78.
- These checks establish software/build/deployment integrity, not full PCGN conformance or independent pronunciation accuracy. The Ukrainian romanization adapter and independent IPA gold remain incomplete.


### Post-merge PR #95 main and Pages verification — 2026-10-31

- PR #95 merged as `28a9bbb909ca57735ceca92f262c2de9eeb43396`. Exact-main Quality [41246343908](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41246343908) and Pages deployment [41246343845](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41246343845) passed; deployed-site/runtime smoke test succeeded.
- This is documentation-only synchronization. Whole-text romanization regression coverage remains bounded engineering evidence; contextual PCGN implementation and the independent syllable-level Ukrainian adapter remain incomplete.
- PR #64 remains open and untouched; current compare is 7 commits ahead / 35 behind, with changes limited to the old layout/CSS snapshot and its test.


## Whole-message mixed-script segmentation regression — 2026-11-01

- PR [#97](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/97) merged as `72e4644204c879f905ebaa20dddd2d00b6583d32`.
- Added a canonical adversarial case containing Khmer, Latin identifier, ASCII digits, Khmer numerals and punctuation, tab, CRLF, U+200B and an unsupported symbol.
- The test consumes the canonical fixture, requires exact reconstruction from `segment_syllables()`, confirms a supported Khmer example remains structurally established and confirms the unsupported symbol remains locally invalid/unsupported.
- Exact PR-head Quality checks [41289845696](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41289845696) passed: Python tests, web checks and production build.
- The fixture has `ipa: null` and explicit non-phonological provenance; it is structural/source-integrity evidence, not IPA gold or an accuracy benchmark row.


## Current-head reconciliation — 2026-11-01

- Audit baseline: `c0a2b33c86791b6546e1158c62043fd23acc1f60`; exact-main CI: Quality 41326462947; Pages 41326462993; latest check completed successfully.
- The canonical gold TSV currently has a header only. Independent adjudicated IPA gold = 0; accuracy is not measured and must remain null.
- Current language-specific unresolved tasks and acceptance criteria are recorded in [LINGUISTIC-COMPLETION-REGISTER-2026-11-01.md](audits/current/LINGUISTIC-COMPLETION-REGISTER-2026-11-01.md). This register does not replace historical audit evidence.
- CI success is limited to configured engineering checks. It does not establish expert phonetic correctness, production readiness, manual accessibility QA or rights to redistribute third-party assets.


## Independent IPA gold corpus audit — 2026-11-01

The repository now has a standard-library JSONL validator, five versioned JSON Schemas, a source-license registry, independent annotation/adjudication records, deterministic split manifests, a typed IPA export into the existing benchmark and a tag/manual gold release gate. The corpus files remain empty and `gold.tsv` remains header-only. This is infrastructure completion, not scientific completion: independent expert gold=0, accuracy=null, and production readiness remains blocked.

Blind annotation cannot be guaranteed in a public Git repository. Two submissions must be collected separately in a controlled channel and merged only after both are locked. Every future source still requires a human-verified license/permission locator; a registry entry is not itself a grant of rights.


## 2026-11-01 closeout

The independent IPA gold-corpus implementation and Khmer evidence matrix are in [PR #103](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/pull/103). PR CI passed 136 Python tests + 27 subtests, browser register-shifter contract, web checks and Vite build. The source-backed matrices do not establish every vowel × series × coda cell; independent gold remains 0. Main was not changed. Legacy PR #64 remains untouched.


## CI action runtime audit — 2026-11-01

All five workflows now use current Node.js 24-compatible action majors. Exact-head checks passed: [Quality checks 41339636053](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41339636053), [Goruut 41339636042](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41339636042), and [G2P smoke 41339636117](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/41339636117). CI maintenance does not establish phonological accuracy or expert gold.


## PR integration reconciliation — 2026-11-03

- PR #108 merged the browser result-rendering hotfix; exact-main Quality, Chromium and Pages/deployed-site smoke passed.
- PR #112 merged the manifest-wide split identity invariant and separate-manifest acceptance; exact PR-head Quality/browser checks passed, followed by exact-main Quality, browser and Pages/deployed-site smoke.
- PR #113 merged source registry, external corpus triage, bibliography and provenance-test updates; exact PR-head Quality and browser checks passed.
- PR #115 merged the single careful-citation profile and removed deterministic colloquial /r/-loss rewriting; exact PR-head Quality and browser checks passed, followed by main Quality, Chromium and Pages/deployed-site smoke.
- PR #116 merged the glossary, codebase map and agent guidance. PRs #107 and #114 were superseded by these scoped integrations; neither broad profile branch was merged wholesale.
- Independent adjudicated IPA gold remains 0 and empirical accuracy remains null. CI verifies engineering and deployed assets, not pronunciation accuracy or manual accessibility.


## Romanization implementation audit — mainline 2026-11-12

### Standard-scope correction: Cambodian national 1997 profile

The Cambodian national report to UNGEGN (GEGN.2/2023/104/CRP.104) says the national romanized writing system is based on the 1997 transcription system instead of the 1972 transliteration system; the UNGEGN Working Group's status report (GEGN.2/2023/11/CRP.11) corroborates that replacement. The project BGN/PCGN 1972 matrix is still a valid, fully source-backed research crosswalk, but it must not be represented as the current national Cambodian system. The primary 1997 national specification is not yet available in the inspected sources. The similarly dated ALA-LC Khmer 1997 table is a distinct library-cataloguing profile, not a substitute. Track this as EVIDENCE_LIMITED pending primary-source retrieval and a profile decision.


The current orthographic romanization path is integrated end to end for the available source output: BGN/PCGN-derived ASCII Latin → separate Ukrainian orthographic adapter. The 22-row consonant target matrix and 37-row vowel/rime target matrix are populated and tested. PR #164 added the adapter; PR #165 records post-merge evidence. Current main is `a86a59cf082d547563b45374ced9dfb45c5cd8db`; exact-head Quality [43228414756](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414756), browser [43228414938](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414938), and Pages [43228414646](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43228414646) passed.

Acceptance remains PARTIAL: the current `@gmana/km-translit` ASCII profile drops BGN/PCGN diacritics, so the Ukrainian adapter cannot reconstruct contextual distinctions already lost upstream. The output is correctly marked PROVISIONAL. This orthographic route does not use IPA. Draft G2P PR #153 remains open and untouched; it is not a dependency of this work. No pronunciation accuracy, IPA gold, or official Ukrainian-standard claim is made.

The 2025 UNGEGN Asia South-East Division report (GEGN.2/2025/73/CRP.73, p. 3) confirms the October 2023 Cambodian national gazetteer uses the 1997 transcription system: https://unstats.un.org/unsd/ungegn/sessions/4th_session_2025/documents/GEGN.2_2025_73_CRP73_item4a.pdf


## Test-discovery audit — 2026-11-12

The Khmer orthographic adapter's unit test file existed but was omitted from both `npm test` and `npm run check`; browser smoke covered only a single example. PR #167 fixed this by wiring the unit suite into both commands and asserting every distinct PCGN consonant romanization token. It merged as `f0485892f5d4b16e5fbe0ded6f8e083d8b044f4b`. Exact-main Quality [43250158336](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43250158336) and browser [43250158628](https://github.com/ClippyFirst/Khmer-Ukrainian-Phonetic-System-/actions/runs/43250158628) passed. Remaining coverage limitations are recorded in KHM-ROM-TEST-001.


## Evidence conflict update — Cambodian 1997 transcription system — 2026-11-12

The Cambodia national report (GEGN.2/2023/104/CRP.104) and UNGEGN 2025 regional report (GEGN.2/2025/73/CRP.73) say national gazetteers used the 1997 transcription system. The UK PCGN's May 2026 *Cambodia Toponymic Factfile* (pp. 1–2) says the system has not yet been implemented consistently and awaits evidence of consistent official use. The 2023 Gazetteer primary table is now located (pp. vii–viii); its foreword states departmental use but provisional status pending formal National Commission approval. The statements are compatible as provisional use versus consistent national implementation. Keep KHM-ROM-NATIONAL-1997-001 EVIDENCE_LIMITED until formal adoption evidence and source reuse rights are resolved. BGN/PCGN 1972 remains the project's current source-located research profile; ALA-LC 1997 remains a distinct cataloguing profile.


## Primary Khmer 1995/1997 table located — 2026-11-12

The Ministry's *Gazetteer of Cambodia* (October 2023), pp. vii–viii, contains the “Romanized System for Khmer” table labelled “Prepared by Geography Department, 1995. Last modification 1997”. The foreword states that the system had been used by the Geography Department, would be submitted to the National Committee for consideration/adoption, and that this Gazetteer is a provisional release pending National Commission approval. This reconciles the Cambodia/UNGEGN gazetteer-use reports with PCGN's May 2026 statement that the system is not yet implemented consistently: provisional departmental use is documented, but formal adoption/consistent nationwide implementation remains unproven. Original PDF copyright © 2023 by the Geography Department; ODC's record says no license is given for the PDF. Keep KHM-ROM-NATIONAL-1997-001 EVIDENCE_LIMITED until adoption evidence and reuse rights are resolved. Do not relabel BGN/PCGN 1972 rows.


## Khmer romanization matrix/runtime parity — 2026-11-12

A second test-discovery gap was identified after the adapter suite was wired into `npm test`: the consonant test still duplicated all 22 source rows as a hard-coded array. That could pass while the canonical CSV changed independently. The test now parses `data/khmer/romanization_ukrainian.csv` and exercises each row's romanization/target pair, including both contextual `b,p` alternatives and the U+2019 marker. This is a source-of-truth parity safeguard, not linguistic adjudication. Vowel coverage remains limited to the 33 ASCII candidates that the current upstream package can emit; diacritic/contextual PCGN output is still lost upstream.
