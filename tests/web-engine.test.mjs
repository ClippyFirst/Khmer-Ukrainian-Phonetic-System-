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
for (const x of ["Регістри, шифтери та кластери", "Приголосні: українська ціль", "Голосні: контекст важливіший за знак", "/c/","/h/","/ʋ/","/w/","Adversarial validation","ភាសាខ្មែរ","пієса кхмае"]) {
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
if (!fixtures["ភាសាខ្មែរ"] || fixtures["ភាសាខ្មែរ"].ipa !== "/pʰiəsaː kʰmae/" || fixtures["ភាសាខ្មែរ"].ua !== "пієса кхмае") {
  throw new Error("verified Khmer-language fixture missing or inconsistent");
}
if (!Object.hasOwn(policy.segments, "ae")) throw new Error("Khmer /ae/ target mapping missing");
if (!js.includes("fixture.ua") || !js.includes("mapping_check")) throw new Error("lexical practical-form handling missing");
const forbiddenTerms = ["\u043a\u0445\u043c\u0435\u0440", "\u041a\u0445\u043c\u0435\u0440"];
for (const term of forbiddenTerms) {
  if (html.includes(term) || systemHtml.includes(term) || js.includes(term)) throw new Error("obsolete Ukrainian language-name term remains: " + term);
}

if (Object.keys(adversarial).length < 8) throw new Error("adversarial corpus unexpectedly incomplete");
if (systemHtml.includes("<td>/c, cʰ/</td><td>ч</td>") || systemHtml.includes("<td>/h/</td><td>г</td>")) {
  throw new Error("system page contains stale transcription policy");
}
console.log("web-engine structural tests: PASS");
