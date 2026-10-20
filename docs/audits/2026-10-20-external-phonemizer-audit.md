# External Khmer phonemizer and IPA-data audit

**Audit date:** 2026-10-20  
**Scope:** suitability as a comparator for the conservative Khmer→Ukrainian analysis pipeline; this is a source/repository inspection, not an executed benchmark.

## Decision

**Do not replace the structural parser with an external phonemizer.** Treat `khmerphonemizer` as a candidate differential comparator only after pinning a version and checking its packaged lexicon/dependencies. No external package is currently added to runtime dependencies. The repository's own structural analysis must continue to expose consonant series, COENG/subscript structure, vowel signs, register shifters, coda marks, and uncertainty independently of any G2P result.

## Candidate A: `seanghay/khmerphonemizer`

Sources:
- Repository / README: https://github.com/seanghay/khmerphonemizer/
- PyPI package: https://pypi.org/project/khmerphonemizer/
- README's cited related work includes WikiPron, Gruut, OpenFst and Phonetisaurus.

What the public documentation establishes:
- The package calls itself a Khmer grapheme-to-phoneme system and returns tokenized words plus lists of phoneme symbols.
- It exposes beam-search parameters and `use_lexicon=True` by default; `use_lexicon=False` is therefore necessary for a separate lexicon-off comparison, but does not by itself establish how training data or model weights were built.
- The README reports an MIT license for the package and references external projects/data.
- Its published example contains symbols such as `c`, `ĕ`, `ɨ`, and segmented phoneme lists. These are IPA-like and partly use IPA characters, but the output format alone does not prove that every symbol, length, stress, boundary, or diacritic follows a single explicitly documented IPA convention. For instance, the project must establish what `c` means in the package's inventory rather than assuming it equals IPA [c] in every release.
- The README references WikiPron and other tools, but the accessible summary does not fully establish the exact lexicon snapshot, licenses of each bundled data component, or per-entry provenance.

Limitations for this project:
- A G2P output is not a phonetic gold label; it can encode the tool's model/lexicon conventions and dialect.
- A beam-search alternative is not automatically a linguistically meaningful alternative analysis unless the model defines it that way.
- Package-level MIT licensing does not, on its own, prove every embedded lexicon/model/data asset is separately licensed for redistribution under the same terms.

**Decision:** candidate comparator only. Before a reproducible benchmark, pin the release and hash; inspect the wheel/sdist and dependency tree; identify and license-audit every bundled dictionary/model; run with lexicon on and off; preserve raw symbol strings; document the symbol inventory and profile; never use its outputs as independent gold labels.

## Candidate B: Khmer acoustic-model pronunciation dictionary

Source: https://github.com/chemvatho/Khmer-acoustic-model/

The README describes a 29,204-entry pronunciation dictionary, an acoustic model trained on 137+ hours, and a pronunciation inventory labelled IPA. The repository's main code/model is described as MIT, but the README separately labels the pronunciation dictionary **CC BY-SA 4.0**. The data license must therefore be assessed separately from the code license before copying or redistributing entries.

This is a potentially valuable **external comparison source**, but it is not a turnkey orthography-to-IPA oracle:
- A pronunciation dictionary gives word-level pronunciations, not an explicit derivation from each Unicode grapheme and context.
- It represents the project's chosen phoneme inventory and annotation conventions. Its inventory includes symbols that require convention checking (for example `-c`, `tɕh`, and diphthong notation); do not normalize these to IPA by visual guess.
- The repository's README includes placeholder-looking setup/Colab URLs and reports model-evaluation metrics that should be checked against the actual versioned artifacts before relying on them. This audit has not independently reproduced those metrics.
- The README says the dictionary is validated by native linguists, but this inspection did not verify the identity, annotation protocol, coverage, dialect labels, or entry-level evidence.

**Decision:** inspect as a source-indexed comparison corpus only after downloading the actual licensed dictionary, checking its headers and data license, preserving the original transcription, mapping its symbol conventions explicitly, and recording lexical overlaps with this project's examples. Do not silently import the dictionary or relabel its entries as project gold.

## Reproducible comparison protocol (not yet executed)

1. Freeze a benchmark manifest with source text, lexical identity/gloss, dialect/profile, source URL and version, raw source transcription, normalized project transcription, and adjudication status.
2. Split lexical items into development and held-out sets before tuning any project rules. Do not use Unicode illustrative examples as if they were independent acoustic judgments.
3. Include contrasting first-/second-series vowels, open/closed syllables, NIKAHIT/REAHMUK, COENG clusters, register shifters, independent vowels, colloquial /r/-loss environments, malformed inputs, and out-of-vocabulary items.
4. Run `khmerphonemizer` with lexicon enabled and disabled, recording the package version and all output tokens exactly. If comparing a dictionary, preserve its original symbol conventions as a separate field.
5. Normalize only documented IPA conventions; score disagreements only against independently adjudicated references. Report exact-match and segment-level measures with denominators and uncertainty; do not publish a numeric accuracy until this exists.
6. Keep structural parsing metrics separate from IPA accuracy and Ukrainian adaptation. A correct segmentation does not prove correct phonetics; a matching Ukrainian string does not prove a correct IPA analysis.
7. Keep Ukrainian adaptation as a separate proposed layer. If the phonetic result is not established, the final Ukrainian word output must remain unavailable or explicitly provisional.

## Current outcome

- No external dependency added.
- No claim that either candidate was executed locally or benchmarked in this pass.
- No lexicon copied into this repository.
- The machine-readable `data/khmer/vowel-context-register.json` stores source-attested examples and preserves source disagreement; it deliberately leaves word-level Ukrainian adaptations unset.
- Next acceptance gate: run a pinned tool against a held-out, independently adjudicated corpus and publish the exact manifest, license audit, commands, raw outputs, and score calculations.

## Repository licensing and citation metadata

- `pyproject.toml` declares the project license as MIT, but the repository tree inspected for this audit did not contain a root `LICENSE` or `CITATION.cff`. This is a release-readiness inconsistency, not proof that the source has no copyright owner.
- Do not create a copyright notice or author list by inference. Before release, confirm the intended rights holder/contributor wording, add the full license text consistent with the chosen terms, and add a `CITATION.cff` containing only verified author/title/version/repository metadata.
- Keep code, reference transcriptions, dictionaries, model weights, and research examples as separate provenance/licensing classes. A permissive code license does not automatically relicense upstream text or lexicons.
- The current audit did not verify all source/data licenses (including Unicode materials, R12A content, Wiktionary-derived transcriptions, or the Chem (2020) paper's reuse terms). Record each actual license/terms URL before redistributing substantial extracted datasets.

