# Гібридний кхмерський IPA-рушій

`khmer_ua.HybridKhmerEngine` — дослідницький ансамбль над наявними структурним аналізатором і зовнішніми Khmer→IPA рушіями. Він не замінює парсер, профіль вимови або український адаптер.

## Склад

- Внутрішній `analyze()` — структурна основа: нормалізація, графемна структура, серія приголосного, підрядкові приголосні та статус аналізу. Структурний результат не видається за IPA.
- `make_mekongphon_backend()` — готовий lazy/cached CPU-адаптер закріпленої моделі `byumatrixlab/khmer-ipa` (torch/transformers потрібні лише під час виклику).
- `make_mekongphon_rule_backend()` — завантажує upstream `rb_khm_to_ipa.py` за локальним шляхом, перевіряє SHA-256 і викликає `khmer2ipa()` без копіювання коду в репозиторій (потрібні upstream-залежності `khmer-nltk` і `tqdm`).
- `make_command_backend()` — додатковий універсальний адаптер для правилового CLI G2P, який приймає один рядок на stdin і повертає IPA у stdout.
- `rule-baseline` — окремий правиловий кандидат; його вихід також передається через backend-функцію.
- Інші незалежні Khmer→IPA реалізації можуть бути додані окремими backend-ами.

## Контракт backend-а

```python
def my_backend(text: str) -> dict:
    return {"ipa": "…", "status": "candidate", "provenance": {"engine": "name", "revision": "pinned-revision"}}
```

Підключення:

```python
from khmer_ua import create_hybrid_engine, make_mekongphon_backend, make_mekongphon_rule_backend
engine = create_hybrid_engine({
    "mekongphon": make_mekongphon_backend(),
    "rule-baseline": make_mekongphon_rule_backend("mekongphon/training/baselines/rb_khm_to_ipa.py"),
})
result = engine.analyze("ខ្មែរ")
```

## Правило злиття

- Зберігаються сирі IPA-виходи, назви backend-ів і provenance.
- Нормалізуються лише зовнішні `/…/` або `[…]` обгортки та пробіли. Довгота, аспірація, тони, діакритики й межі не видаляються.
- Однаковий вихід від двох незалежно названих backend-ів дає `ensemble_consensus`.
- Один голос дає `single_engine_candidate`; різні рядки дають `engine_disagreement`.
- Без консенсусу поле `ipa` залишається `null`. Це навмисний запобіжник, а не помилка.
- Ідентичні назви backend-а не дають додаткових голосів.

## Межі

Правиловий baseline є евристичним upstream експериментом (зокрема його коментарі прямо вказують на спрощене поводження з діакритиками), тому його голос не слід трактувати як рівноцінну експертну анотацію. Ансамбль не доводить незалежність навчальних даних двох моделей і не створює gold. Два backend-и можуть успадковувати той самий словник або ті самі помилки. `ensemble_consensus` означає лише збіг реалізацій, а не експертно підтверджену вимову. Перед передачею результату в IPA→український адаптер слід окремо перевірити профіль, тон/довготу/фонation та сегментацію. Невизначений результат не можна підміняти романізацією.
