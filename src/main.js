import consonants from "../data/khmer/consonants.json" with { type: "json" };
import registers from "../data/khmer/registers.json" with { type: "json" };
import signs from "../data/khmer/signs.json" with { type: "json" };
import vowels from "../data/khmer/vowels.json" with { type: "json" };
import practicalPolicy from "../data/ukrainian/practical-policy.json" with { type: "json" };
import fixtures from "../data/tests/web-fixtures.json" with { type: "json" };
import { khmerToLatin } from "@gmana/km-translit";
import { mapIpa } from "./ukrainian-practical.js";

const CONSONANTS = Object.fromEntries(consonants.map((item) => [item.char, item]));
const SIGN_BY_CHAR = Object.fromEntries(signs.map((item) => [item.char, item]));
const VOWEL_SIGNS = new Set(
  signs
    .filter((item) => ["dependent_vowel", "composite_vowel", "vowel_modifier"].includes(item.kind))
    .map((item) => item.char),
);
const COENG = "្";
const ZWNJ = "\u200C";
const ZWSP = "\u200B";
const SHIFTERS = new Set(["៉", "៊"]);
const SHIFTER_ELIGIBILITY = Object.fromEntries(Object.entries(registers.shifter_eligibility).map(([key, values]) => [key === "muusikatoan" ? "៉" : "៊", new Set(values)]));
const PUNCTUATION = /^\s|^\p{P}$/u;
const PROFILES = new Set(["khmer-pph-careful-citation-v1"]);

const normalize = (text) => text.normalize("NFC");
const isKhmerConsonant = (char) => Object.hasOwn(CONSONANTS, char);

function isSeparator(char) {
  return !char || /\s/u.test(char) || PUNCTUATION.test(char);
}

function startsNewOrthographicSyllable(chars, index) {
  if (!isKhmerConsonant(chars[index]) || index === 0) return false;
  if (chars[index - 1] === COENG) return false;
  if (chars[index + 1] === COENG) return false;
  const previousKind = SIGN_BY_CHAR[chars[index - 1]]?.kind;
  if (["dependent_vowel", "composite_vowel", "vowel_modifier", "sign"].includes(previousKind)) {
    return isSeparator(chars[index + 1]);
  }
  return true;
}

function tokenize(text) {
  const units = [];
  let current = "";
  const chars = [...normalize(text)];
  const fixtureKeys = Object.keys(fixtures).sort((a, b) => [...b].length - [...a].length);

  const flush = () => {
    if (current) {
      units.push(current);
      current = "";
    }
  };

  for (let index = 0; index < chars.length;) {
    const char = chars[index];

    if (char === ZWSP) {
      flush();
      units.push(ZWSP);
      index += 1;
      continue;
    }

    if (PUNCTUATION.test(char)) {
      flush();
      units.push(char);
      index += 1;
      continue;
    }

    const remainder = chars.slice(index).join("");
    const fixtureKey = fixtureKeys.find((key) => {
      if (!remainder.startsWith(key)) return false;
      const next = chars[index + [...key].length];
      return next === undefined || isSeparator(next);
    });

    if (fixtureKey) {
      flush();
      units.push(fixtureKey);
      index += [...fixtureKey].length;
      continue;
    }

    if (current && startsNewOrthographicSyllable(chars, index)) {
      units.push(current);
      current = char;
    } else {
      current += char;
    }
    index += 1;
  }
  flush();
  return units;
}

function resolveRegister(base, raw) {
  const structural = [...raw].filter((char) => char !== ZWNJ);
  const positions = structural.flatMap((char, index) => SHIFTERS.has(char) ? [index] : []);
  if (!positions.length) return { register: base.register, rule: null, status: "ESTABLISHED_STRUCTURE" };
  if (positions.length > 1) return { register: base.register, rule: "MULTIPLE_REGISTER_SHIFTERS", status: "EVIDENCE_LIMITED" };
  if (positions[0] !== 1) return { register: base.register, rule: "MISPLACED_REGISTER_SHIFTER", status: "EVIDENCE_LIMITED" };
  const shifter = structural[positions[0]];
  if (!SHIFTER_ELIGIBILITY[shifter]?.has(base.char)) return { register: base.register, rule: "NON_STANDARD_SHIFTER_USE", status: "EVIDENCE_LIMITED" };
  if (base.char === "ប" && shifter === "៉") return { register: "first", rule: "BA_TO_PA_EXCEPTION", status: "ESTABLISHED_STRUCTURE" };
  if (shifter === "៉" && base.register === "second") return { register: "first", rule: "MUUSIKATOAN", status: "ESTABLISHED_STRUCTURE" };
  if (shifter === "៊" && base.register === "first") return { register: "second", rule: "TRIISAP", status: "ESTABLISHED_STRUCTURE" };
  return { register: base.register, rule: "NON_STANDARD_SHIFTER_USE", status: "EVIDENCE_LIMITED" };
}

function parseSyllable(raw) {
  if (!raw) return { status: "NOT_ESTABLISHED", raw };
  if (!isKhmerConsonant(raw[0])) {
    if (raw[0] === COENG || SHIFTERS.has(raw[0])) {
      return { status: "INVALID_OR_UNSUPPORTED", raw, reason: "Khmer combining structure cannot begin a standalone orthographic unit." };
    }
    if (SIGN_BY_CHAR[raw[0]]) return { status: "NOT_ESTABLISHED", raw, reason: "Відомий знак без базового приголосного; його вимову окремо не встановлено." };
    return { status: "INVALID_OR_UNSUPPORTED", raw, reason: "Немає підтримуваного кмерського базового приголосного або відомого знака." };
  }
  let index = 1;
  const base = raw[0];
  const subscripts = [];
  const vowelSigns = [];
  const unknown = [];
  const graphemes = [{ text: base, kind: "consonant" }];

  while (index < raw.length) {
    const char = raw[index];
    if (char === ZWNJ) {
      graphemes.push({ text: char, kind: "format_control" });
      index += 1;
      continue;
    }
    if (char === COENG) {
      const sub = raw[index + 1];
      if (!sub || !isKhmerConsonant(sub)) {
        return { status: "INVALID_OR_UNSUPPORTED", raw, reason: "Malformed coeng sequence." };
      }
      subscripts.push(sub);
      graphemes.push({ text: COENG + sub, kind: "subscript" });
      index += 2;
      continue;
    }
    if (VOWEL_SIGNS.has(char)) vowelSigns.push(char);
    else if (!SIGN_BY_CHAR[char]) unknown.push(char);
    graphemes.push({ text: char, kind: SIGN_BY_CHAR[char]?.kind ?? "unknown" });
    index += 1;
  }

  // Unknown characters must not inherit a supported structural status from
  // the recognized base consonant. Match the Python parser's fail-closed rule.
  if (unknown.length) {
    return {
      status: "INVALID_OR_UNSUPPORTED", raw, base, subscripts, vowelSigns,
      unknown, graphemes,
      reason: "Unknown character(s) inside Khmer orthographic unit.",
    };
  }
  const register = resolveRegister(CONSONANTS[base], raw);
  return {
    status: register.status,
    raw,
    base,
    register: register.register,
    register_rule: register.rule,
    subscripts,
    vowelSigns,
    unknown,
    graphemes,
    inherent_vowel: register.register === "first" ? "first-series" : register.register === "second" ? "second-series" : null,
    onset_ipa: base === "ប" && register.rule === "BA_TO_PA_EXCEPTION" ? "p" : CONSONANTS[base].onset_ipa,
  };
}

function renderIpaProfile(ipa, profile) {
  if (!PROFILES.has(profile)) throw new Error("Unsupported pronunciation profile: " + profile);
  // The selected profile is contemporary Phnom Penh careful citation speech.
  // Colloquial /r/-loss is variable and must never be synthesized by a
  // deterministic spelling/IPA regex in this single-profile workflow.
  return ipa;
}

function renderFixture(fixture, profile) {
  if (!PROFILES.has(profile)) throw new Error("Unsupported pronunciation profile: " + profile);
  if (!fixture.ipa) {
    return {
      source: fixture.source,
      ipa: "⟦EVIDENCE_LIMITED⟧",
      ua: "⟦НЕВСТАНОВЛЕНО⟧",
      status: fixture.status,
      note: fixture.note,
      profile,
      mapping_check: null,
    };
  }

  const sourceIpa = fixture.ipa.replace(/^\//, "").replace(/\/$/, "");
  const ipa = renderIpaProfile(sourceIpa, profile);
  const mapped = mapIpa(ipa, practicalPolicy);
  const agrees = mapped.value !== null && mapped.value === fixture.ua;

  if (!agrees) {
    return {
      source: fixture.source,
      ipa: "/" + ipa + "/",
      ua: mapped.value ?? "⟦НЕВСТАНОВЛЕНО⟧",
      status: "EVIDENCE_LIMITED",
      note: "УВАГА: лексична українська форма не збігається з канонічною IPA → українська політикою. Суперечливий override не використовується; показано канонічний результат політики.",
      profile,
      mapping_check: { policy_render: mapped.value, lexical_render: fixture.ua ?? null, agrees: false },
    };
  }

  return {
    source: fixture.source,
    ipa: "/" + ipa + "/",
    ua: mapped.value,
    status: fixture.status,
    note: fixture.note + " Профіль: " + profile + ".",
    profile,
    mapping_check: fixture.ua ? { policy_render: mapped.value, lexical_render: fixture.ua, agrees: true } : null,
  };
}

function deriveDeterministicIpa(analysis) {
  if (analysis.status === "INVALID_OR_UNSUPPORTED") return null;
  if (analysis.subscripts?.length || analysis.vowelSigns?.length || analysis.unknown?.length) return null;
  if (analysis.register_rule === "MULTIPLE_REGISTER_SHIFTERS" || analysis.register_rule === "MISPLACED_REGISTER_SHIFTER" || analysis.register_rule === "NON_STANDARD_SHIFTER_USE") return null;

  const onset = analysis.onset_ipa;
  if (!onset || onset.includes("~")) return null;

  const inherent = analysis.register === "first" ? "ɑː" : "ɔː";
  return onset + inherent;
}

function renderUnknownUnit(unit, profile) {
  const analysis = parseSyllable(unit);
  if (analysis.status === "INVALID_OR_UNSUPPORTED") {
    return {
      source: unit,
      ipa: "⟦INVALID_OR_UNSUPPORTED⟧",
      ua: "⟦НЕПІДТРИМУЄТЬСЯ⟧",
      status: "INVALID_OR_UNSUPPORTED",
      note: analysis.reason ?? "Некоректна або непідтримувана Unicode-послідовність.",
      analysis,
      profile,
    };
  }

  const derivedIpa = deriveDeterministicIpa(analysis);
  if (derivedIpa) {
    const profiledIpa = renderIpaProfile(derivedIpa, profile);
    const mapped = mapIpa(profiledIpa, practicalPolicy);
    if (mapped.value !== null) {
      return {
        source: unit,
        ipa: "/" + profiledIpa + "/",
        ua: mapped.value,
        status: "PROPOSED",
        note: "Вимову виведено з документованої структури: базовий приголосний + встановлений регістр/шифтер + притаманна голосна серії. Українська форма є проєктною; результат не є лексичним винятком.",
        analysis,
        profile,
        mapping_check: { policy_render: mapped.value, lexical_render: null, agrees: true },
      };
    }
  }

  // Last-resort onset-only IPA: the source grapheme is never mapped
  // directly to Ukrainian and no vowel/coda/tone is inferred.
  if (analysis.onset_ipa && analysis.status !== "INVALID_OR_UNSUPPORTED" && !analysis.unknown?.length) {
    const onsetIpa = renderIpaProfile(analysis.onset_ipa, profile);
    const onsetMapping = mapIpa(onsetIpa, practicalPolicy);
    if (onsetMapping.value !== null) {
      return {
        source: unit,
        ipa: "/" + onsetIpa + "/ [PROVISIONAL]",
        ua: onsetMapping.value + "?",
        status: "PROVISIONAL",
        note: "Низька достовірність: показано лише зареєстровану IPA-підказку початкового приголосного. Голосну, підрядкові приголосні, фіналь і тон не виведено; ? позначає невстановлену частину.",
        analysis,
        profile,
        provisional_ipa: onsetIpa,
        unresolved_graphemes: [...unit].slice(1),
        fallback_trace: [{ source: unit, position: "onset", ipa: onsetIpa, rule_id: "KHMER-PREVIEW-ONSET-IPA-V1", certainty: "PROVISIONAL" }],
      };
    }
  }

  return {
    source: unit,
    ipa: "⟦NOT_ESTABLISHED⟧",
    ua: "⟦НЕВСТАНОВЛЕНО⟧",
    status: analysis.status === "EVIDENCE_LIMITED" ? "EVIDENCE_LIMITED" : "NOT_ESTABLISHED",
    note: "Структуру запису розпізнано, але для цієї одиниці немає достатньо встановленої орфографія → IPA моделі. Система не вгадує вимову.",
    analysis,
    profile,
  };
}

function combineStatus(items) {
  const statuses = new Set(items.map((item) => item.status));
  const invalidCount = items.filter((item) => item.status === "INVALID_OR_UNSUPPORTED").length;
  if (invalidCount > 0 && invalidCount === items.length) return "INVALID_OR_UNSUPPORTED";
  if (invalidCount > 0 || statuses.has("EVIDENCE_LIMITED")) return "EVIDENCE_LIMITED";
  if (statuses.has("NOT_ESTABLISHED")) return "NOT_ESTABLISHED";
  if (statuses.has("PROVISIONAL")) return "PROVISIONAL";
  if (statuses.has("PROPOSED")) return "PROPOSED";
  return "ESTABLISHED_STRUCTURE";
}

function getStatusNotice(data) {
  if (!data) return "";
  if (data.status === "PROVISIONAL") {
    return "Показано лише низькодостовірні IPA-підказки відомих початкових приголосних. Знак ? позначає невстановлену частину; голосні, фіналі й тон не вгадуються.";
  }
  if (data.status === "PROPOSED") {
    return "Результат має статус PROPOSED: IPA та українське читання є дослідницькими пропозиціями для цих записів, а не підтвердженою універсальною моделлю. Перевіряйте джерела й лексичний контекст перед використанням.";
  }
  if (data.status === "EVIDENCE_LIMITED" || data.status === "NOT_ESTABLISHED") {
    return data.note;
  }
  if (data.status === "INVALID_OR_UNSUPPORTED") {
    return "Ввід не підтримується повністю. Перегляньте статус кожної одиниці та не використовуйте маркери непідтвердженого результату як вимову.";
  }
  return "";
}

function convert(text, profile) {
  const normalized = normalize(text);
  if (!normalized.trim()) return null;

  const units = tokenize(normalized);
  const rendered = units.map((unit) => {
    if (unit === ZWSP) return { source: unit, ipa: " ", ua: " ", status: "PUNCTUATION", note: "U+200B ZERO WIDTH SPACE трактовано як невидиму межу слова.", profile };
    if (PUNCTUATION.test(unit)) return { source: unit, ipa: unit, ua: unit, status: "PUNCTUATION", note: "", profile };
    const fixture = fixtures[unit];
    return fixture ? renderFixture(fixture, profile) : renderUnknownUnit(unit, profile);
  });

  const linguistic = rendered.filter((item) => item.status !== "PUNCTUATION");
  const analyses = linguistic.map((item) => item.analysis).filter(Boolean);
  const resolved = linguistic.filter((item) => item.status === "PROPOSED");
  const unresolved = linguistic.filter((item) => item.status !== "PROPOSED");
  const unresolvedNames = unresolved.map((item) => item.source).filter(Boolean).slice(0, 12);
  const evidenceLimited = linguistic.filter((item) => item.status === "EVIDENCE_LIMITED").length;
  const notEstablished = linguistic.filter((item) => item.status === "NOT_ESTABLISHED").length;
  const invalid = linguistic.filter((item) => item.status === "INVALID_OR_UNSUPPORTED").length;
  // Keep aggregate output honest: unresolved units must not be concatenated
  // with partial candidates in a way that resembles a complete transcription.
  // Per-unit diagnostics remain available for research and inspection.
  const aggregateUnresolved = linguistic.some((item) =>
    !["PROPOSED", "PROVISIONAL", "ESTABLISHED_STRUCTURE"].includes(item.status)
    || /⟦/.test(item.ipa)
    || /⟦/.test(item.ua)
  );

  return {
    source: normalized,
    ipa: aggregateUnresolved ? "⟦ВИМОВУ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧" : rendered.map((item) => item.ipa).join(""),
    ua: aggregateUnresolved ? "⟦ТРАНСКРИПЦІЮ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧" : rendered.map((item) => item.ua).join(""),
    status: combineStatus(linguistic),
    note: `Локальний аналіз: ${resolved.length} одиниць мають зафіксовану IPA та проєктну українську форму; ${unresolved.length} потребують окремого встановлення або перевірки (${notEstablished} не встановлено, ${evidenceLimited} з обмеженою доказовістю, ${invalid} некоректних/непідтримуваних). Некоректна одиниця більше не робить весь змішаний результат INVALID OR UNSUPPORTED; її стан ізольовано на рівні одиниці.${unresolvedNames.length ? ` Невстановлені/проблемні одиниці: ${unresolvedNames.join(" · ")}.` : ""}`,
    profile,
    units: rendered,
    analyses,
    vowelModel: vowels.coverage_policy,
  };
}

export { convert, tokenize, parseSyllable, mapIpa, getStatusNotice };

if (typeof document !== "undefined") {
  const $ = (id) => document.getElementById(id);
  const source = $("source");
  const romanizationResult = $("romanization-result");
  const results = $("results");
  const empty = $("empty");
  const issue = $("issue");
  const live = $("live");
  const modePhonetic = $("mode-phonetic");
  const modeRomanization = $("mode-romanization");
  const outputMethodNote = $("output-method-note");

  function setOutputMode(mode) {
    document.querySelectorAll("[data-method-panel]").forEach((panel) => {
      panel.hidden = panel.dataset.methodPanel !== mode;
    });
    modePhonetic.classList.toggle("is-active", mode === "phonetic");
    modePhonetic.setAttribute("aria-pressed", String(mode === "phonetic"));
    modeRomanization.classList.toggle("is-active", mode === "romanization");
    modeRomanization.setAttribute("aria-pressed", String(mode === "romanization"));
    outputMethodNote.textContent = mode === "phonetic"
      ? "Фонетичний режим: детерміновані правила орфографія → IPA → українська адаптація; непідтверджені форми не вгадуються."
      : "Романізаційний режим: Khmer → BGN/PCGN-похідний латинський запис → окрема українська матриця. Український результат PARTIAL; фонетичний результат не використовується як fallback.";
  }

  function render() {
    $("count").textContent = `${[...source.value].length} символів`;
    const data = convert(source.value, $("profile").value);
    if (!data) {
      results.hidden = true;
      issue.hidden = true;
      empty.hidden = false;
      return;
    }
    empty.hidden = true;
    results.hidden = false;
    romanizationResult.textContent = khmerToLatin(data.source);
    $("ipa-result").textContent = data.ipa;
    $("ua-result").textContent = data.ua;
    $("status").textContent = data.status.replaceAll("_", " ");
    $("details").textContent = data.note;
    const unitDetails = $("unit-details");
    unitDetails.replaceChildren();
    const unitHeading = document.createElement("h3");
    unitHeading.textContent = "Одиничний аналіз";
    unitDetails.append(unitHeading);
    data.units.filter((unit) => unit.status !== "PUNCTUATION").forEach((unit) => {
      const card = document.createElement("article");
      card.className = "unit-detail";
      const heading = document.createElement("div");
      heading.className = "unit-detail-heading";
      const sourceLabel = document.createElement("strong");
      sourceLabel.className = "unit-source";
      sourceLabel.lang = "km";
      sourceLabel.textContent = unit.source;
      const statusLabel = document.createElement("span");
      statusLabel.className = "unit-status";
      statusLabel.textContent = unit.status.replaceAll("_", " ");
      heading.append(sourceLabel, statusLabel);
      const values = document.createElement("p");
      values.className = "unit-values";
      values.textContent = "IPA: " + unit.ipa + " · Українська: " + unit.ua;
      const note = document.createElement("p");
      note.className = "unit-note";
      note.textContent = unit.note || "Окремого пояснення для цієї одиниці немає.";
      card.append(heading, values, note);
      unitDetails.append(card);
    });
    unitDetails.hidden = data.units.every((unit) => unit.status === "PUNCTUATION");
    const notice = getStatusNotice(data);
    issue.hidden = !notice;
    if (!issue.hidden) {
      $("issue-text").textContent = notice;
      $("issue").querySelector("strong").textContent =
        data.status === "PROPOSED" ? "Результат попередній" : "Результат потребує обережності";
    }
    live.textContent = "Результат оновлено";
  }
  
  modePhonetic.addEventListener("click", () => setOutputMode("phonetic"));
  modeRomanization.addEventListener("click", () => setOutputMode("romanization"));
  setOutputMode("phonetic");
  source.addEventListener("input", render);
  $("profile").addEventListener("change", render);
  $("example").addEventListener("click", () => {
    source.value = fixtures["ភាសាខ្មែរ"] ? "ភាសាខ្មែរ" : Object.keys(fixtures)[0];
    render();
    source.focus();
  });
  $("clear").addEventListener("click", () => {
    source.value = "";
    render();
    source.focus();
  });
  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const element = $(button.dataset.copy);
      try {
        const copyText = "value" in element ? element.value : element.textContent;
        await navigator.clipboard.writeText(copyText);
        const old = button.textContent;
        button.textContent = "Скопійовано";
        window.setTimeout(() => { button.textContent = old; }, 900);
      } catch {
        live.textContent = "Не вдалося скопіювати автоматично. Виділіть результат і скопіюйте вручну.";
      }
    });
  });
  
}
