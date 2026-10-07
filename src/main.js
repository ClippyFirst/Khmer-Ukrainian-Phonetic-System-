import consonants from "../data/khmer/consonants.json" with { type: "json" };
import registers from "../data/khmer/registers.json" with { type: "json" };
import signs from "../data/khmer/signs.json" with { type: "json" };
import vowels from "../data/khmer/vowels.json" with { type: "json" };
import practicalPolicy from "../data/ukrainian/practical-policy.json" with { type: "json" };
import fixtures from "../data/tests/web-fixtures.json" with { type: "json" };

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
const PUNCTUATION = /^\s|^[។៕,!?;:()[\]{}"“”«»]$/u;
const PROFILES = new Set(["careful_standard", "phnom_penh_colloquial", "established_form"]);
const SEGMENTS = Object.keys(practicalPolicy.segments).sort((a, b) => b.length - a.length);

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
    return { status: "NOT_ESTABLISHED", raw };
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

  const register = resolveRegister(base, raw);
  return {
    status: unknown.length ? "EVIDENCE_LIMITED" : register.status,
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

function mapIpa(ipa) {
  let rest = ipa.replace(/[ˈˌ.]/gu, "");
  let value = "";
  while (rest) {
    if (/\s/u.test(rest[0])) {
      value += rest[0];
      rest = rest.slice(1);
      continue;
    }
    const segment = SEGMENTS.find((candidate) => rest.startsWith(candidate));
    if (!segment) return { value: null, unsupported: rest };
    value += practicalPolicy.segments[segment].default;
    rest = rest.slice(segment.length);
  }
  return { value, unsupported: null };
}

function renderIpaProfile(ipa, profile) {
  if (!PROFILES.has(profile)) throw new Error("Unsupported pronunciation profile: " + profile);
  if (profile === "careful_standard" || profile === "established_form") return ipa;
  return ipa.replace(/([ptkbdɡc])r(?=[aeiouəɛɔɑɨɤ])/gu, "$1ʰ");
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
  const mapped = mapIpa(ipa);
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
  if (analysis.subscripts.length || analysis.vowelSigns.length || analysis.unknown.length) return null;
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
    const mapped = mapIpa(profiledIpa);
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
  if (statuses.has("PROPOSED")) return "PROPOSED";
  return "ESTABLISHED_STRUCTURE";
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

  return {
    source: normalized,
    ipa: rendered.map((item) => item.ipa).join(""),
    ua: rendered.map((item) => item.ua).join(""),
    status: combineStatus(linguistic),
    note: `Локальний аналіз: ${resolved.length} одиниць мають зафіксовану IPA та проєктну українську форму; ${unresolved.length} потребують окремого встановлення або перевірки (${notEstablished} не встановлено, ${evidenceLimited} з обмеженою доказовістю, ${invalid} некоректних/непідтримуваних). Некоректна одиниця більше не робить весь змішаний результат INVALID OR UNSUPPORTED; її стан ізольовано на рівні одиниці.${unresolvedNames.length ? ` Невстановлені/проблемні одиниці: ${unresolvedNames.join(" · ")}.` : ""}`,
    profile,
    units: rendered,
    analyses,
    vowelModel: vowels.coverage_policy,
  };
}

export { convert, tokenize, parseSyllable, mapIpa };

if (typeof document !== "undefined") {
  const $ = (id) => document.getElementById(id);
  const source = $("source");
  const results = $("results");
  const empty = $("empty");
  const issue = $("issue");
  const live = $("live");
  
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
    $("source-result").textContent = data.source;
    $("ipa-result").textContent = data.ipa;
    $("ua-result").textContent = data.ua;
    $("status").textContent = data.status.replaceAll("_", " ");
    $("details").textContent = data.note;
    issue.hidden = !["EVIDENCE_LIMITED", "INVALID_OR_UNSUPPORTED", "NOT_ESTABLISHED"].includes(data.status);
    if (!issue.hidden) $("issue-text").textContent = data.note;
    live.textContent = "Результат оновлено";
  }
  
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
        await navigator.clipboard.writeText(element.textContent);
        const old = button.textContent;
        button.textContent = "Скопійовано";
        window.setTimeout(() => { button.textContent = old; }, 900);
      } catch {
        live.textContent = "Не вдалося скопіювати автоматично. Виділіть результат і скопіюйте вручну.";
      }
    });
  });
  
}
