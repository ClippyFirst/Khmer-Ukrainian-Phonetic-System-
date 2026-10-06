import assert from "node:assert/strict";
import { convert, parseSyllable, tokenize } from "../src/main.js";

const adversarial = "ក គ កា គា កូ គូ កី គី កេ គេ កែ គែ កើ គើ កៅ គៅ ប ប៉ ប៊ ផ ព ត ថ ទ ធ ច ឆ ជ ឈ ស ហ វ";
const expectedIpa = "/kɑː/ /kɔː/ /kaː/ /kiə/ /koː/ /kuː/ /kəj/ /kiː/ /keː/ /kei/ /kaeː/ /kɛː/ /kɑːə/ /kəː/ /kau/ /kəu/ /ɓɑː/ /paː/ /ɓɔː/ /pʰɑː/ /pɔː/ /tɑː/ /tʰɑː/ /tɔː/ /tʰɔː/ /cɑː/ /cʰɑː/ /cɔː/ /cʰɔː/ /sɑː/ /hɑː/ /ʋɔː/";
const expectedUa = "ка ко ка кіє ко ку кей кі ке кей кае ке кае ке кау кеу ба па бо па по та та то то тьа ча тьо чо са ха во";

const tokens = tokenize(adversarial);
assert.equal(tokens.length, 32, "the 32-unit adversarial block must remain 32 orthographic units");

const result = convert(adversarial, "careful_standard");
assert.ok(result, "adversarial block must produce a result");
assert.equal(result.status, "PROPOSED");
assert.equal(result.ipa, expectedIpa);
assert.equal(result.ua, expectedUa);
assert.equal(result.units.length, 32);
assert.ok(result.units.every((unit) => unit.status === "PROPOSED"), "no unit in the 32-item regression block may remain unresolved");

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
  { ipa: "/pʰɑː/", ua: "па" },
);

assert.equal(parseSyllable("ក៊").status, "EVIDENCE_LIMITED");
assert.equal(parseSyllable("គ៉").status, "EVIDENCE_LIMITED");
assert.equal(parseSyllable("ក៊").register_rule, "NON_STANDARD_SHIFTER_USE");

const mixed = convert("ក ࿔ គ", "careful_standard");
assert.equal(mixed.status, "EVIDENCE_LIMITED");
assert.equal(mixed.units.find((x) => x.source === "က")?.status, undefined);
const unresolved = mixed.units.find((x) => x.status === "NOT_ESTABLISHED" || x.status === "INVALID_OR_UNSUPPORTED");
assert.ok(unresolved, "mixed input must isolate an unresolved unit rather than hiding neighboring evidence-backed units");
assert.equal(mixed.units.find((x) => x.source === "ក")?.ua, "ка");
assert.equal(mixed.units.find((x) => x.source === "គ")?.ua, "ко");

console.log("web-runtime regression tests: PASS");
