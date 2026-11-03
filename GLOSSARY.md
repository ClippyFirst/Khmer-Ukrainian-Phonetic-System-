# Khmer → Ukrainian project glossary

This glossary defines repository terms and evidence boundaries. It does not imply that a complete Khmer phoneticizer exists.

| Term | Meaning in this repository |
|---|---|
| **Khmer orthography** | Original Khmer Unicode input, preserved under the repository's normalization contract. |
| **Orthographic unit / syllable candidate** | A parser unit composed from base consonants, coeng/subscript sequences, vowel signs, independent vowels and modifiers. It is not automatically a spoken syllable or word. |
| **Consonant series / register** | The orthographic first/second series classification that conditions Khmer vowel realization. |
| **Register shifter** | MUUSIKATOAN or TRIISAP, interpreted only in documented eligible positions and consonant environments. |
| **Coeng / subscript** | The encoded subscript-consonant sequence. Preserve its order and structural identity. |
| **Inherent-vowel series** | A structural label associated with the effective consonant series. It is not itself an IPA vowel value. |
| **Coda / nucleus context** | Syllable structure that can condition vowel quality and duration. Do not derive complete IPA from an isolated sign or series label. |
| **Structural status** | Result of orthographic decomposition (e.g. established structure, evidence limited, invalid/unsupported). It does not mean phonetic output is established. |
| **Phoneticization status** | Whether the pronunciation is actually supported. Current parser explicitly reports phoneticization as not yet established for general input. |
| **IPA profile adapter** | A validator/renderer for an already supplied IPA string under a selected pronunciation profile. It is not a Khmer orthography-to-IPA engine. |
| **Reference profile** | The bounded pilot target: contemporary Phnom Penh Khmer, careful citation-form speech (khmer-pph-careful-citation-v1). |
| **Colloquial /r/-loss** | A variable, style- and speaker-sensitive pathway; do not rewrite /Cr/ deterministically to one aspirated form without lexical and profile evidence. |
| **BGN/PCGN route** | Separate orthographic romanization. It must not be used as an IPA, register or pronunciation fallback. |
| **Ukrainian practical form** | Project-specific adaptation of supported IPA segments, not an official Ukrainian standard. |
| **Independent IPA gold** | Rights-cleared, source-located, independently annotated and adjudicated IPA records. The corpus remains empty until the human process supplies admissible records. |

## Canonical decisions and evidence

- Architecture and limitations: docs/architecture.md, docs/limitations.md, docs/evidence.md.
- Current execution and blockers: docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md.
- Canonical language data: data/khmer/*.json; target mapping: data/ukrainian/practical-policy.json.
