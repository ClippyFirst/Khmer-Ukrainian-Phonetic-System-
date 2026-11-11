# Кандидатний гібридний IPA-шар Khmer

HybridKhmerEngine запускає чинний детермінований RuleBasedKhmerEngine і за конфігурацією збирає зовнішні IPA-кандидати. Зовнішні джерела не замінюють правила автоматично.

## Підключення

```python
from khmer_ua import HybridKhmerEngine, make_mekongphon_backend, make_command_backend
engine = HybridKhmerEngine({
    "mekongphon": make_mekongphon_backend(),
    # Goruut / Khmer Phonemizer / Epitran can be supplied via pinned CLI wrapper.
})
result = engine.analyze("ខ្មែរ")
```

Кандидати повертаються в external_candidates із сирим IPA та provenance. Фінальне ipa залишається результатом внутрішнього детермінованого рушія. Голосування не використовується.

## Бенчмарки та рішення

- MekongPhon: 100/100 виходів; 64/100 збіги з source-attested pron_no_tones, CER 12.539%; незалежне gold = 0. Не перевіряє тон/фонацію; незалежність split не встановлена.
- Khmer Phonemizer: 100/100 виходів; 18/100 строгих збігів у тому самому діагностичному наборі; independent gold = 0.
- Goruut: попередній 100-рядковий прогін: 97 виходів, 6/100 строгих збігів, 27 частково неперекладених фрагментів; відсутній upstream asset weights9.bin.zlib.
- Khmer acoustic-model dictionary: BLOCKED — повний файл відсутній, кількість записів і ліцензійні декларації суперечливі.

Це source concordance, не accuracy. MekongPhon — найкращий кандидат для подальшого benchmark-порівняння, але не підтверджений замінник Phnom Penh rule engine.
