# Khmer → Ukrainian Web Service — Product & Design Requirements

## 1. Product definition

A static, browser-local web service for converting Khmer text into a research-grounded Ukrainian practical transcription. The web layer is a presentation and interaction layer over the research engine in this repository; it must not invent phonetic rules in UI code.

The product has exactly two public pages:

1. **Service** — the main Khmer → Ukrainian converter.
2. **The system** — an explanation of the author's Ukrainian practical transcription system, its methodology, evidence, decisions, limitations, and comparison with existing traditions.

The Chinese project `ClippyFirst/chinese-for-ukrainians` is the structural reference: compact static architecture, clear input/output workspace, independent copyable outputs, explicit issue states, local-first operation, and a research-backed data layer. The Khmer project must not copy Chinese linguistic assumptions.

## 2. Intended user outcome

A Ukrainian reader should be able to paste Khmer text and quickly obtain:
- Khmer source preserved exactly;
- a structured pronunciation/IPA representation when established by the engine;
- the proposed Ukrainian practical rendering;
- transparent warnings when the engine cannot establish a result;
- a direct route to the second page explaining why the Ukrainian form is what it is.

The service is not a machine translator and does not translate Khmer meaning into Ukrainian.

## 3. Scientific/product boundary

Canonical pipeline:

Khmer orthography
→ graphemic/syllabic analysis
→ phonology
→ surface phonetics / IPA
→ Ukrainian target
→ Ukrainian practical orthography

The UI must never imply that Khmer letters map one-to-one onto Ukrainian letters.

Evidence states must remain visible in the engine and UI:
- ESTABLISHED
- WELL_SUPPORTED
- PROPOSED
- EVIDENCE_LIMITED
- NOT_ESTABLISHED
- LEXICAL_OVERRIDE

No fabricated IPA, confidence percentage, or empirical accuracy score is permitted.

## 4. Page 1 — Service

### Primary hierarchy

1. Header / identity
2. Short statement of purpose
3. Large Khmer input field
4. One primary conversion action (with live conversion permitted if it remains clear)
5. Result area
6. Issue/uncertainty area when needed
7. Short link to methodology/system page
8. GitHub/source footer

### Input

- Unicode-safe Khmer textarea.
- Preserve whitespace, punctuation, Latin text, numbers and emoji.
- Character count.
- Clear/example controls.
- No account, upload, analytics or runtime backend.
- The default experience should be immediately usable without configuration.

### Output

The result should expose, in a visually ordered but compact form:
- Khmer source / parsed span status where useful;
- IPA/pronunciation profile when established;
- Ukrainian practical transcription;
- optional structured explanation for selected segments/rules;
- copy controls for each principal output.

When a segment or word cannot be phoneticized reliably, preserve the source and show an explicit unresolved state rather than silently guessing.

### Profiles

The implementation may expose pronunciation profile selection only where the research engine has evidence for a meaningful distinction, e.g. careful Standard Khmer versus a documented Phnom Penh-oriented profile. The UI must not imply that one profile is universally correct.

### Examples

Examples must be provenance-bearing test fixtures or documented lexical items. Do not use invented examples presented as validated Khmer pronunciation.

## 5. Page 2 — The author's system

Purpose: make the research system understandable to a Ukrainian reader without turning the page into an academic paper.

Required sections:
- What the system is and is not.
- Why a new Ukrainian system is proposed.
- Full pipeline.
- How Khmer orthography is interpreted.
- Consonant correspondence principles.
- Vowel/context model.
- Dependent and independent vowels.
- Register effects.
- Coda and cluster handling.
- /r/ pronunciation profiles.
- /ʔ/ and other neutralization decisions.
- Ukrainian target inventory relationship (linked to the canonical Ukrainian inventory, not duplicated).
- Comparison with Russian practical transcription.
- Evidence-limited areas.
- Examples showing source → IPA → Ukrainian.
- Version/status and repository link.

The page must clearly distinguish source facts from authorial design decisions.

## 6. Visual language

Country identity: Cambodia.

Use the Cambodian flag palette as the brand basis:
- deep blue;
- red;
- white.

These are accents and identity markers, not a mandate to make the whole page saturated. The default visual direction should remain editorial, typographic, functional and research-oriented.

Avoid:
- generic AI/SaaS landing-page gradients;
- excessive rounded cards;
- glassmorphism;
- decorative metric cards;
- fake dashboards;
- unnecessary illustrations;
- excessive shadows;
- national-symbol clip art.

Prefer:
- strong typographic hierarchy;
- restrained grid;
- generous whitespace;
- precise borders/dividers;
- editorial documentation feel;
- Khmer script as authentic typographic material;
- red/blue as controlled functional accents;
- high contrast and accessible focus states.

## 7. Responsive/accessibility requirements

- Desktop-first web application, fully usable on mobile.
- Keyboard navigation.
- Visible focus.
- Semantic headings and labels.
- Screen-reader announcements for conversion/copy/issue state.
- No information conveyed by color alone.
- Reduced-motion support.
- No horizontal overflow at narrow widths.
- Khmer and Ukrainian text must render correctly with appropriate Unicode fonts/fallbacks.

## 8. Technical architecture

Static frontend, analogous to the Chinese service.

Suggested structure:

/
├── index.html                 # Service
├── system.html                # Author's system
├── src/
│   ├── main.js
│   ├── system.js
│   ├── styles/
│   │   └── main.css
│   └── app/
│       ├── convert.js
│       ├── ui.js
│       ├── clipboard.js
│       └── engine-adapter.js
├── data/
├── scripts/
├── tests/
└── docs/

The research engine remains the source of truth. The web adapter consumes structured results; it must not duplicate linguistic tables.

## 9. Runtime/privacy

- Local browser processing where technically feasible.
- No runtime API required for core conversion.
- No analytics/telemetry.
- No user text sent to a server.
- Safe DOM rendering through text APIs.
- Strict CSP appropriate for static deployment.
- No eval or dynamic code execution.

## 10. Acceptance criteria

The product is considered ready only when all are true:

- Both pages exist and are navigable.
- Page 1 performs real Khmer → Ukrainian conversion through the research engine.
- Page 2 accurately explains the implemented system.
- All principal outputs are copyable.
- Unsupported/unresolved cases are explicit.
- Research data and UI do not diverge.
- Core examples are covered by automated tests.
- Responsive/accessibility checks pass.
- Static production build succeeds.
- No runtime network dependency is required for conversion.
- Documentation explains local development and deployment.
- Final UI has been visually inspected against the approved design direction.
- Claims of linguistic coverage match the actual implemented engine.

## 11. Construction sequence

1. Freeze these product/design requirements.
2. Complete/verify the Khmer research engine required by the service.
3. Define the structured web adapter contract.
4. Generate and select the visual direction.
5. Build Page 1.
6. Build Page 2.
7. Integrate real engine data.
8. Add tests and accessibility QA.
9. Run production build and release checks.
10. Perform final research/UI audit and document the release.

## 12. Explicit non-goals

- Translation.
- OCR.
- Speech recognition.
- User accounts.
- Cloud database.
- Runtime analytics.
- Invented phoneticization for uncovered forms.
- Pretending that the proposed Ukrainian system is an official national standard.
