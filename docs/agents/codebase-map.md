# Codebase map — Khmer → Ukrainian

**Audit basis: current main after browser hotfix, manifest-wide split identity, source-evidence reconciliation and single careful-citation profile integration; navigation map, not a claim of complete Khmer phonology.

## User-facing entry points

- Python public API: src/khmer_ua/__init__.py exports analyze, normalize_khmer, render_ipa_profile and Ukrainian segment/sequence mapping.
- CLI: src/khmer_ua/cli.py; analyze and related commands currently expose structural analysis and explicit not-established states.
- Browser instrument: src/main.js; canonical JSON registries are imported from data/khmer/ and bundled by Vite.

## Current Python flow

~~~text
CLI / Python API
  └─ parser.analyze
       ├─ normalize_khmer
       ├─ segment_syllables / decompose_khmer_syllable
       ├─ phonology.resolve_effective_register
       │    └─ orthographic series / shifter rules only
       └─ AnalysisResult
            └─ phoneticization_not_yet_established
~~~

The current ipa.render_ipa_profile accepts an IPA string that already exists and validates its selected profile; it does not generate Khmer IPA from orthography. practical.map_sequence maps supplied IPA segments to the Ukrainian target policy. Do not present these functions as a complete source-to-IPA chain.

## Browser flow

src/main.js independently tokenizes and structurally parses Khmer input, resolves register shifters, preserves uncertainty, and maps only supplied/fixture-backed phonetic data. Python/browser parity is tested; keep both implementations aligned when structural contracts change.

## Data and generated-artifact ownership

- Khmer structural registries: data/khmer/*.json.
- Ukrainian target policy: data/ukrainian/practical-policy.json.
- Source and contextual evidence: data/khmer/sources.json, docs/audits/current/.
- Gold lifecycle/scorer: scripts/ipa_gold_corpus.py, scripts/benchmark_ipa.py, data/benchmark/.

## High-risk seams

1. Coeng/subscript and register-shifter encoded order: parser + shared Python/browser contract.
2. Effective register: phonology.resolve_effective_register is the shared Python rule owner; do not duplicate or bypass it.
3. Inherent vowel × consonant series × vowel sign × coda/context: structural labels must not be promoted to IPA without evidence.
4. Phnom Penh /r/-loss: preserve multiple/uncertain realizations; never blanket-rewrite /Cr/.
5. IPA profile ID: the task branch selects khmer-pph-careful-citation-v1; reject legacy/unsupported profile IDs.
6. Gold ingestion: only independent adjudicated, rights-eligible, held-out IPA may be scored.

## Verification

- Python: python -m pytest -q.
- Browser: npm run check; production build: npm run build.
- Inspect generated artifacts and built relative asset paths after relevant changes.
- A green engineering suite does not prove complete Khmer phoneticization, expert adjudication or manual accessibility QA.
