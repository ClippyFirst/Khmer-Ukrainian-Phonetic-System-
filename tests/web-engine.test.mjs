import fs from "node:fs";
const html=fs.readFileSync("index.html","utf8"), system=fs.readFileSync("system.html","utf8"), js=fs.readFileSync("src/main.js","utf8");
for(const x of ["Content-Security-Policy","src/main.js","id=\"source\"","id=\"results\""]) if(!html.includes(x)) throw new Error("index missing "+x);
for(const x of ["Авторська система","Приголосні: українська ціль","Голосні: контекст важливіший за знак","Порівняння з російською практикою"]) if(!system.includes(x)) throw new Error("system missing "+x);
for(const x of ["EXAMPLES","ipaToUA","NOT_ESTABLISHED","phnom_penh_colloquial"]) if(!js.includes(x)) throw new Error("engine missing "+x);
console.log("web-engine structural tests: PASS");