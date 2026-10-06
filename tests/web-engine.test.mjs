import fs from "node:fs";

const html = fs.readFileSync("index.html", "utf8");
const system = fs.readFileSync("system.html", "utf8");
const js = fs.readFileSync("src/main.js", "utf8");
const policy = JSON.parse(fs.readFileSync("data/ukrainian/practical-policy.json", "utf8"));
const fixtures = JSON.parse(fs.readFileSync("data/tests/web-fixtures.json", "utf8"));

for (const x of ["Content-Security-Policy", "src/main.js", 'id="source"', 'id="results"']) {
  if (!html.includes(x)) throw new Error("index missing " + x);
}
for (const x of ["Авторська система", "Приголосні: українська ціль", "Голосні: контекст важливіший за знак", "Порівняння з російською практикою"]) {
  if (!system.includes(x)) throw new Error("system missing " + x);
}
for (const x of ["NOT_ESTABLISHED", "phnom_penh_colloquial", "practical-policy.json", "web-fixtures.json"]) {
  if (!js.includes(x)) throw new Error("web adapter missing " + x);
}
if (js.includes("const CONSONANTS = {") || js.includes("const UA = {") || js.includes("const VOWELS = {")) {
  throw new Error("web adapter still contains duplicated linguistic mapping tables");
}
if (Object.keys(policy.segments).length < 40) throw new Error("Ukrainian policy unexpectedly incomplete");
if (Object.keys(fixtures).length < 4) throw new Error("web fixtures unexpectedly incomplete");

console.log("web-engine structural tests: PASS");
