import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { convert, parseSyllable, tokenize, getStatusNotice } from "../src/main.js";

const adversarial = "ក គ កា គា កូ គូ កី គី កេ គេ កែ គែ កើ គើ កៅ គៅ ប ប៉ ប៊ ផ ព ត ថ ទ ធ ច ឆ ជ ឈ ស ហ វ";

const serviceHtml = readFileSync(new URL("../index.html", import.meta.url), "utf8");
assert.doesNotMatch(serviceHtml, /source-result|source-card/u, "the original Khmer input must not be duplicated as a fourth output card");
assert.match(serviceHtml, /id="mode-phonetic"/u, "the phonetic mode must be selectable");
assert.match(serviceHtml, /id="mode-romanization"/u, "the romanization mode must be selectable");
assert.match(serviceHtml, /data-method-panel="romanization"/u, "romanization output must be isolated from phonetic output");
assert.match(serviceHtml, /data-method-panel="phonetic"/u, "IPA and phonetic Ukrainian output must be isolated");
assert.match(serviceHtml, /id="ua-romanization-status"/u, "an incomplete romanization-to-Ukrainian crosswalk must be explicit, not silently replaced with phonetic output");
const expectedIpa = "/kɑː/ /kɔː/ /kaː/ /kiə/ /koː/ /kuː/ /kəj/ /kiː/ /keː/ /kei/ /kaeː/ /kɛː/ /kɑːə/ /kəː/ /kau/ /kəu/ /ɓɑː/ /paː/ /ɓɔː/ /pʰɑː/ /pɔː/ /tɑː/ /tʰɑː/ /tɔː/ /tʰɔː/ /cɑː/ /cʰɑː/ /cɔː/ /cʰɔː/ /sɑː/ /hɑː/ /ʋɔː/";
const expectedUa = "ка ко ка кіє ко ку кей кі ке кей кае ке кае ке кау кеу ба па бо п'а по та т'а то т'о тьа ть'а тьо ть'о са га во";

const tokens = tokenize(adversarial);
assert.equal(tokens.filter((token) => /\S/u.test(token)).length, 32, "the 32-unit adversarial block must remain 32 orthographic units");

const result = convert(adversarial, "careful_standard");
assert.ok(result, "adversarial block must produce a result");
assert.equal(result.status, "PROPOSED");
assert.equal(result.ipa, expectedIpa);
assert.equal(result.ua, expectedUa);
assert.equal(result.units.filter((unit) => unit.status !== "PUNCTUATION").length, 32);
assert.ok(result.units.filter((unit) => unit.status !== "PUNCTUATION").every((unit) => unit.status === "PROPOSED"), "no linguistic unit in the 32-item regression block may remain unresolved");

const bySource = Object.fromEntries(result.units.map((unit) => [unit.source, unit]));
assert.deepEqual(
  { ipa: bySource["ប"].ipa, ua: bySource["ប"].ua },
  { ipa: "/ɓɑː/", ua: "ба" },
);
assert.deepEqual(
  { ipa: bySource["ប៉"].ipa, ua: bySource["ប៉"].ua },
  { ipa: "/paː/", ua: "па" },
);
assert.deepEqual(
  { ipa: bySource["ប៊"].ipa, ua: bySource["ប៊"].ua },
  { ipa: "/ɓɔː/", ua: "бо" },
);
assert.deepEqual(
  { ipa: bySource["ផ"].ipa, ua: bySource["ផ"].ua },
  { ipa: "/pʰɑː/", ua: "п'а" },
);

assert.equal(parseSyllable("កx").status, "INVALID_OR_UNSUPPORTED");
assert.deepEqual(parseSyllable("កx").unknown, ["x"]);
assert.equal(parseSyllable("កx").ipa, undefined);
const mixedScriptUnit = convert("កx", "careful_standard");
assert.equal(mixedScriptUnit.status, "INVALID_OR_UNSUPPORTED");
assert.equal(mixedScriptUnit.units.length, 1);
assert.equal(mixedScriptUnit.units[0].status, "INVALID_OR_UNSUPPORTED");
assert.equal(mixedScriptUnit.units[0].ipa, "⟦INVALID_OR_UNSUPPORTED⟧");

assert.equal(parseSyllable("ក៊").status, "EVIDENCE_LIMITED");
assert.equal(parseSyllable("គ៉").status, "EVIDENCE_LIMITED");
assert.equal(parseSyllable("ក៊").register_rule, "NON_STANDARD_SHIFTER_USE");

const mixed = convert("ក ☃ គ", "careful_standard");
assert.equal(mixed.status, "EVIDENCE_LIMITED");
assert.equal(mixed.ipa, "⟦ВИМОВУ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
assert.equal(mixed.ua, "⟦ТРАНСКРИПЦІЮ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
const unresolved = mixed.units.find((x) => x.status === "NOT_ESTABLISHED" || x.status === "INVALID_OR_UNSUPPORTED");
assert.ok(unresolved, "mixed input must isolate an unresolved unit rather than hiding neighboring evidence-backed units");
assert.equal(mixed.units.find((x) => x.source === "ក")?.ua, "ка");
assert.equal(mixed.units.find((x) => x.source === "គ")?.ua, "ко");

console.log("web-runtime regression tests: PASS");


// Cross-profile and Unicode-format regression coverage.
const careful = convert("ច្រើន", "careful_standard");
const colloquial = convert("ច្រើន", "phnom_penh_colloquial");
const established = convert("ច្រើន", "established_form");
assert.equal(careful.ipa, "/craən/");
assert.equal(careful.ua, "тьраен");
assert.equal(colloquial.ipa, "⟦ВИМОВУ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
assert.equal(colloquial.units.find((unit) => unit.source === "ច្រើន")?.ipa, "/cʰaən/", "unit-level IPA remains inspectable while aggregate output fails closed");
assert.equal(colloquial.status, "EVIDENCE_LIMITED");
assert.equal(colloquial.ua, "⟦ТРАНСКРИПЦІЮ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
assert.equal(colloquial.units.find((unit) => unit.source === "ច្រើន")?.ua, "ть'аен", "unit-level candidate remains inspectable while aggregate output fails closed");
assert.equal(established.ipa, "/craən/");

const zwnj = parseSyllable("ប\u200C៊");
assert.equal(zwnj.register, "second", "ZWNJ must not disrupt register-shifter resolution");
assert.equal(zwnj.register_rule, "TRIISAP");
assert.equal(zwnj.status, "ESTABLISHED_STRUCTURE");

const zeroWidthBoundary = convert("ក\u200Bគ", "careful_standard");
assert.equal(zeroWidthBoundary.ipa, "/kɑː/ /kɔː/");
assert.equal(zeroWidthBoundary.ua, "ка ко");
assert.equal(zeroWidthBoundary.status, "PROPOSED");

const mixedZeroWidth = tokenize("ក\u200Bគ");
assert.deepEqual(mixedZeroWidth, ["ក", "\u200B", "គ"]);

assert.throws(() => convert("ក", "unsupported_profile"), /Unsupported pronunciation profile/);
assert.equal(convert("   ", "careful_standard"), null);


const proposedNotice = getStatusNotice(convert("ក", "careful_standard"));
assert.match(proposedNotice, /PROPOSED/u);
assert.match(proposedNotice, /дослідницькими пропозиціями/u);
assert.equal(getStatusNotice({ status: "ESTABLISHED_STRUCTURE", note: "structure only" }), "");
assert.equal(
  getStatusNotice({ status: "NOT_ESTABLISHED", note: "not enough evidence" }),
  "not enough evidence",
);
assert.match(
  getStatusNotice({ status: "INVALID_OR_UNSUPPORTED", note: "unsupported" }),
  /не підтримується повністю/u,
);

const greetingSentence = "សួស្តី! ខ្ញុំឈ្មោះ សុភា។ ខ្ញុំមកពីប្រទេសកម្ពុជា ហើយខ្ញុំចូលចិត្តរៀនភាសាថ្មីៗ និងអានសៀវភៅ។";
const greetingResult = convert(greetingSentence, "careful_standard");
assert.equal(greetingResult.source, greetingSentence.normalize("NFC"));
assert.equal(greetingResult.units.map((unit) => unit.source).join(""), greetingSentence.normalize("NFC"));
assert.ok(greetingResult.units.length > 0);
assert.equal(greetingResult.ipa, "⟦ВИМОВУ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
assert.equal(greetingResult.ua, "⟦ТРАНСКРИПЦІЮ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
console.log("full Khmer sentence integrity: PASS");
