# Agent instructions — Khmer → Ukrainian research system

## Read before changing code

- Treat [docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md](docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md) as the canonical task ledger and continuation record.
- Reconcile changes with [docs/repository-audit.md](docs/repository-audit.md), [docs/romanization-to-ukrainian-matrix.md](docs/romanization-to-ukrainian-matrix.md), [docs/evidence.md](docs/evidence.md), and the existing source/rule registries before adding modules or data.
- Reuse the current Python/browser parsers, fixtures, data tables and tests. Do not create a parallel engine to avoid extending an existing contract.

## Linguistic and output invariants

The phonetic route is:

`Khmer orthography → structural analysis → Khmer phonology → IPA → Ukrainian target adaptation → Ukrainian practical orthography`.

- IPA is the inspectable boundary between source phonology and Ukrainian adaptation. Do not independently generate phonetic Ukrainian output from Khmer graphemes.
- The BGN/PCGN orthographic romanization route is separate. It must not be used to infer IPA, register, vowel quality or pronunciation, and must not fall back to the IPA adapter.
- Preserve consonant series, coeng/subscript structure, register shifters, syllable boundaries, source spans, spaces, punctuation and Unicode normalization status.
- Every input unit must be represented in output or explicitly marked unsupported/uncertain. Never silently drop source text or invent a complete sentence result.
- Distinguish project Ukrainian proposals from established Khmer phonology and from an official Ukrainian standard. Do not invent IPA, lexical gold, sources, accuracy scores or license permissions.
- Shared structural/regression fixtures are not independently adjudicated lexical IPA gold. Keep accuracy unmeasured while such gold is absent.

## Status and verification

Use `DONE_VERIFIED`, `PARTIAL`, `TODO`, `BLOCKED`, and `DEFERRED` consistently with the master handoff. A test file is not evidence until the relevant test passes on the exact final commit.

Relevant commands (run those configured by the repository):

```bash
python -m pytest -q
npm run check
npm run build
```

Inspect generated artifacts and built relative asset paths when changing data or web code. A green CI run proves only the checks it actually executes; it does not establish linguistic accuracy, expert adjudication, manual visual QA or accessibility unless those checks are explicitly included.

## Branches and review

- Start from current `main` on a clearly named task branch. Preserve unrelated branches and work.
- Inspect open PRs and compare their diffs with current `main` before porting or merging. Do not merge diverged layout snapshots wholesale.
- Prefer focused changes, test-first regressions, root-cause fixes, existing interfaces and the smallest complete diff.
- Update the canonical handoff and audit in place. Do not claim completion while acceptance criteria or external evidence remain open.
- Do not force-push, delete user branches, change repository settings, publish releases, or invent a project license.

## Adopted engineering references

Methodological references only; do not add them as runtime dependencies or copy their repositories wholesale:

- [obra/superpowers](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) — test-first work, explicit plans, root-cause debugging, review and evidence before completion.
- [mattpocock/skills](https://github.com/mattpocock/skills/tree/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa) — behavior-focused tests, clear interfaces, test seams and source-backed research.
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846) — reuse before invention, smallest complete diff, connected-code review and explicit deferred-work accounting.

When these references conflict with the existing project contract or the user's explicit requirements, follow the project contract and user requirements.
