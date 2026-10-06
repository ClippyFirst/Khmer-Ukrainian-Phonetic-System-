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

The web-facing explanation was re-audited against the canonical Ukrainian policy and the adversarial parser work. A stale system-page table was found and removed: the page now agrees with the policy for /c/ → ть, /cʰ/ → ч, /h/ → х, /ʋ/ → в and /w/ → у. The browser adapter's previous Phnom Penh /r/-loss transformation was also removed because it converted a documented dialect phenomenon into an over-broad automatic rule without modelling its full phonetic consequences.

The web fixture corpus now includes Unicode/R12A representative cases for register shifters, coeng clusters, pre-base vowels, long vowels, repeated nyo, coeng-r and the ប៉ exception, plus a negative multiple-shifter case. The Unicode example ប៉ី is represented as /pei/ rather than the earlier /pəj/ claim.

The system page and web structural tests now explicitly guard against stale transcription mappings. Academic paragraph-logic review of the updated system page returned no issues.

GitHub Actions runs triggered by the new commits currently report failure with zero job records. This is recorded as an execution/infrastructure verification gap, not as evidence that the Python or Node tests themselves failed. Local test execution is likewise unavailable in this environment.
