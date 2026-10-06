import fs from "node:fs";

const html = fs.readFileSync("index.html", "utf8");
const systemHtml = fs.readFileSync("system.html", "utf8");
const js = fs.readFileSync("src/main.js", "utf8");
const policy = JSON.parse(fs.readFileSync("data/ukrainian/practical-policy.json", "utf8"));
const fixtures = JSON.parse(fs.readFileSync("data/tests/web-fixtures.json", "utf8"));
const adversarial = JSON.parse(fs.readFileSync("data/tests/adversarial-cases.json", "utf8"));
const vite = fs.readFileSync("vite.config.js", "utf8");

for (const x of ["Content-Security-Policy", "src/main.js", 'id="source"', 'id="results"']) {
  if (!html.includes(x)) throw new Error("index missing " + x);
}
for (const x of ["Регістри, шифтери та кластери", "Приголосні: українська ціль", "Голосні: контекст важливіший за знак", "/c/","/h/","/ʋ/","/w/","Валідація складних випадків","ភាសាខ្មែរ","пієса кмае"]) {
  if (!systemHtml.includes(x)) throw new Error("system missing " + x);
}
for (const x of ["NOT_ESTABLISHED", "EVIDENCE_LIMITED", "BA_TO_PA_EXCEPTION", "MULTIPLE_REGISTER_SHIFTERS", "phnom_penh_colloquial", "practical-policy.json", "web-fixtures.json"]) {
  if (!js.includes(x)) throw new Error("web adapter missing " + x);
}
if (js.includes("const CONSONANTS = {") || js.includes("const UA = {") || js.includes("const VOWELS = {")) {
  throw new Error("web adapter still contains duplicated linguistic mapping tables");
}
if (!vite.includes("index.html") || !vite.includes("system.html")) throw new Error("Vite config does not build both public pages");
if (Object.keys(policy.segments).length < 40) throw new Error("Ukrainian policy unexpectedly incomplete");
if (Object.keys(fixtures).length < 16) throw new Error("web fixtures unexpectedly incomplete");
if (!fixtures["ភាសាខ្មែរ"] || fixtures["ភាសាខ្មែរ"].ipa !== "/pʰiəsaː kʰmae/" || fixtures["ភាសាខ្មែរ"].ua !== "пієса кмае") {
  throw new Error("verified Khmer-language fixture missing or inconsistent");
}
if (!Object.hasOwn(policy.segments, "ae")) throw new Error("Khmer /ae/ target mapping missing");
if (policy.segments["kʰ"].default !== "к") throw new Error("canonical /kʰ/ target must be к");
if (fixtures["ខ្មែរ"].ua !== "кмае") throw new Error("lexical /kʰmae/ fixture contradicts canonical /kʰ/ policy");
if (!js.includes("fixture.ua") || !js.includes("mapping_check")) throw new Error("lexical practical-form handling missing");
if (!js.includes("rendered.map") || !js.includes("renderUnknownUnit")) throw new Error("per-unit rendering is missing");
if (!js.includes("Некоректна одиниця більше не робить весь змішаний результат INVALID OR UNSUPPORTED")) throw new Error("mixed-input isolation guard missing");
if (!js.includes("УВАГА: лексична українська форма не збігається")) throw new Error("lexical override contradiction guard missing");
if (!js.includes('mapped.value ?? "⟦НЕВСТАНОВЛЕНО⟧"')) throw new Error("canonical mapping fallback missing");
const forbiddenTerms = ["\u043a\u0445\u043c\u0435\u0440", "\u041a\u0445\u043c\u0435\u0440"];
for (const term of forbiddenTerms) {
  if (html.includes(term) || systemHtml.includes(term) || js.includes(term)) throw new Error("obsolete Ukrainian language-name term remains: " + term);
}

if (Object.keys(adversarial).length < 8) throw new Error("adversarial corpus unexpectedly incomplete");
if (systemHtml.includes("<td>/c, cʰ/</td><td>ч</td>") || systemHtml.includes("<td>/h/</td><td>г</td>")) {
  throw new Error("system page contains stale transcription policy");
}
console.log("web-engine structural tests: PASS");


const sourceGuard = fs.readFileSync("src/main.js", "utf8");
if (/const\s+shifter\s*=\s*shifters\[0\]/u.test(sourceGuard)) throw new Error("register-shifter resolver uses an undefined shifters variable");
if (!/const\s+shifter\s*=\s*raw\[positions\[0\]\]/u.test(sourceGuard)) throw new Error("register-shifter resolver is not reading the detected shifter");
if (!sourceGuard.includes("Khmer combining structure cannot begin a standalone orthographic unit.")) throw new Error("malformed leading Khmer combining marks are not rejected");
if (sourceGuard.includes("if (!raw || !isKhmerConsonant(raw[0])) return { status: \"NOT_ESTABLISHED\", raw };")) throw new Error("malformed-leading-unit guard is too permissive");
console.log("adversarial source guards: PASS");

if (!sourceGuard.includes("fixtureKeys = Object.keys(fixtures).sort")) throw new Error("verified lexical spans are not prioritized during tokenization");
if (!sourceGuard.includes("return next === undefined || isSeparator(next)")) throw new Error("fixture span boundary guard missing");
if (!sourceGuard.includes("units.push(fixtureKey)")) throw new Error("fixture span is not preserved as a unit");
console.log("lexical-span tokenization guards: PASS");

if (!sourceGuard.includes('if (/\\s/u.test(rest[0]))')) throw new Error("IPA mapper drops word boundaries");
if (!sourceGuard.includes('value += rest[0]')) throw new Error("IPA mapper does not preserve whitespace");
if (fixtures["ភាសាខ្មែរ"].ua !== "пієса кмае") throw new Error("phrase fixture must use canonical kʰ policy");
console.log("IPA boundary and phrase guards: PASS");


if (!sourceGuard.includes("const invalidCount = items.filter")) throw new Error("aggregate invalid-count guard missing");
if (!sourceGuard.includes("if (invalidCount > 0 && invalidCount === items.length) return \"INVALID_OR_UNSUPPORTED\";")) throw new Error("mixed-input invalid isolation guard missing");
for (const key of ["ក","គ","កូ","គូ","កេ","គេ","កែ","គែ","កើ","គើ","កៅ","គៅ"]) {
  if (!fixtures[key]) throw new Error("representative series fixture missing: " + key);
}
for (const key of ["ប៉", "ប៊", "ប៉ី", "ខ្ញុំ", "សង្គ្រាម", "ហើយ"]) {
  if (!fixtures[key] || fixtures[key].status !== "PROPOSED") throw new Error("BA shifter fixture missing: " + key);
}
if (fixtures["ប៉"].ipa !== "/paː/" || fixtures["ប៉"].ua !== "па") throw new Error("ប៉ fixture must resolve to /paː/ → па");
if (fixtures["ប៊"].ipa !== "/ɓɔː/" || fixtures["ប៊"].ua !== "бо") throw new Error("ប៊ fixture must resolve to /ɓɔː/ → бо");
if (fixtures["ប៉ី"].ipa !== "/pei/" || fixtures["ប៉ី"].ua !== "пей") throw new Error("ប៉ី fixture must resolve to /pəj/ → пей");
if (fixtures["ខ្ញុំ"].ipa !== "/kʰɲom/" || fixtures["ខ្ញុំ"].ua !== "кньом") throw new Error("ខ្ញុំ fixture must resolve to /kɲom/ → кньом");
if (fixtures["សង្គ្រាម"].ipa !== "/sɔŋkrɛəm/" || fixtures["សង្គ្រាម"].ua !== "сонгкреам") throw new Error("សង្គ្រាម fixture must resolve to /sɑŋ.kriəm/ → сангкрієм");
if (fixtures["ហើយ"].ipa !== "/haəi/" || fixtures["ហើយ"].ua !== "хаеі") throw new Error("ហើយ fixture must resolve to /haəj/ → хаей");
if (sourceGuard.includes("const SHIFTER_ELIGIBILITY") === false) throw new Error("Khmer shifter eligibility guard missing");
if (!sourceGuard.includes("base.char not")) throw new Error("Khmer shifter eligibility is not enforced");
for (const key of ["ɓ", "ʋ"]) {
  if (js.includes('"onset_ipa":"' + key + '~')) throw new Error("canonical initial onset remains ambiguous: " + key);
}
if (!js.includes("function deriveDeterministicIpa")) throw new Error("deterministic inherent-vowel derivation missing");
if (!js.includes('status: "PROPOSED"') || !js.includes('const inherent = analysis.register === "first" ? "ɑː" : "ɔː"')) {
  throw new Error("deterministic consonant-unit rendering is incomplete");
}
if (!js.includes('mapping_check: { policy_render: mapped.value, lexical_render: null, agrees: true }')) {
  throw new Error("derived units do not expose policy mapping verification");
}
console.log("mixed-input status and series coverage guards: PASS");
console.log("deterministic consonant-unit guards: PASS");
