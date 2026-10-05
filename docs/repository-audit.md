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
