import consonants from "../data/khmer/consonants.json" with { type: "json" };
import signs from "../data/khmer/signs.json" with { type: "json" };
import vowels from "../data/khmer/vowels.json" with { type: "json" };
import practicalPolicy from "../data/ukrainian/practical-policy.json" with { type: "json" };
import fixtures from "../data/tests/web-fixtures.json" with { type: "json" };

const CONSONANTS = Object.fromEntries(consonants.map((item) => [item.char, item]));
const SIGN_BY_CHAR = Object.fromEntries(signs.map((item) => [item.char, item]));
const VOWEL_SIGNS = new Set(signs.filter((item) => ["dependent_vowel", "composite_vowel", "vowel_modifier"].includes(item.kind)).map((item) => item.char));
const INDEPENDENT_VOWELS = new Set(signs.filter((item) => item.kind === "independent_vowel").map((item) => item.char));
const COENG = "្";
const PUNCTUATION = /^\s|^[។៕,!?;:()[\]{}"“”«»]$/u;
const PROFILES = new Set(["careful_standard", "phnom_penh_colloquial", "established_form"]);
const SEGMENTS = Object.keys(practicalPolicy.segments).sort((a, b) => b.length - a.length);

const normalize = (text) => text.normalize("NFC");
const isKhmerConsonant = (char) => Object.hasOwn(CONSONANTS, char);

function tokenize(text) {
  const units = [];
  let current = "";
  for (const char of normalize(text)) {
    if (PUNCTUATION.test(char)) {
      if (current) units.push(current), current = "";
      units.push(char);
      continue;
    }
    if (current && isKhmerConsonant(char) && !current.endsWith(COENG)) {
      units.push(current);
      current = char;
    } else {
      current += char;
    }
  }
  if (current) units.push(current);
  return units;
}

function parseSyllable(raw) {
  if (!raw || !isKhmerConsonant(raw[0])) return { status: "NOT_ESTABLISHED", raw };
  let index = 1;
  const base = raw[0];
  const subscripts = [];
  const vowelSigns = [];
  const unknown = [];

  while (index < raw.length) {
    const char = raw[index];
    if (char === COENG) {
      const sub = raw[index + 1];
      if (!sub || !isKhmerConsonant(sub)) {
        return { status: "NOT_ESTABLISHED", raw, reason: "Malformed coeng sequence." };
      }
      subscripts.push(sub);
      index += 2;
      continue;
    }
    if (VOWEL_SIGNS.has(char)) vowelSigns.push(char);
    else if (!SIGN_BY_CHAR[char]) unknown.push(char);
    index += 1;
  }

  return {
    status: unknown.length ? "EVIDENCE_LIMITED" : "ESTABLISHED_STRUCTURE",
    raw,
    base,
    register: CONSONANTS[base].register,
    subscripts,
    vowelSigns,
    unknown,
  };
}

function renderFixture(fixture, profile) {
  const baseIpa = fixture.ipa.replace(/^\\/|\\/$/g, "");
  const renderedIpa = applyProfile(baseIpa, profile);
  const mapped = mapIpa(renderedIpa);
  return {
    source: fixture.source,
    ipa: `/${renderedIpa}/`,
    ua: mapped.value ?? fixture.ua,
    status: fixture.status,
    note: fixture.note,
    profile,
  };
}

function applyProfile(ipa, profile) {
  if (!PROFILES.has(profile)) throw new Error(`Unsupported pronunciation profile: ${profile}`);
  if (profile !== "phnom_penh_colloquial") return ipa;
  return ipa.replace(/([ptkbdɡc])r(?=[aeiouəɛɔɑɨɤ])/g, "$1ʰ");
}

function mapIpa(ipa) {
  let rest = ipa;
  let value = "";
  while (rest) {
    const segment = SEGMENTS.find((candidate) => rest.startsWith(candidate));
    if (!segment) return { value: null, unsupported: rest };
    const target = practicalPolicy.segments[segment];
    if (target === undefined) return { value: null, unsupported: segment };
    value += target.default;
    rest = rest.slice(segment.length);
  }
  return { value, unsupported: null };
}

function convert(text, profile) {
  const normalized = normalize(text);
  if (!normalized.trim()) return null;
  if (fixtures[normalized]) return renderFixture(fixtures[normalized], profile);

  const units = tokenize(normalized);
  const analyses = units.filter((unit) => !PUNCTUATION.test(unit)).map(parseSyllable);
  const unresolved = analyses.some((item) => item.status !== "ESTABLISHED_STRUCTURE");

  return {
    source: normalized,
    ipa: "⟦NOT_ESTABLISHED⟧",
    ua: "⟦НЕВСТАНОВЛЕНО⟧",
    status: unresolved ? "EVIDENCE_LIMITED" : "NOT_ESTABLISHED",
    note: "Структуру кхмерського запису розпізнано, але повна орфографія → IPA матриця для цього запису ще не встановлена. Система навмисно не вгадує вимову.",
    profile,
    analyses,
    vowelModel: vowels.coverage_policy,
  };
}

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
  issue.hidden = data.status === "PROPOSED";
  if (!issue.hidden) $("issue-text").textContent = data.note;
  live.textContent = "Результат оновлено";
}

source.addEventListener("input", render);
$("profile").addEventListener("change", render);
$("example").addEventListener("click", () => {
  source.value = fixtures["កី"] ? "កី" : Object.keys(fixtures)[0];
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

