import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";
import { renderKhmerRomanizationText, renderLatinWord } from "../src/khmer-romanization-ukrainian.js";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
function parseCsv(text) {
  const lines = text.trimEnd().split(/\r?\n/u);
  const parseLine = (line) => {
    const cells = []; let cell = ""; let quoted = false;
    for (let i = 0; i < line.length; i += 1) {
      const char = line[i];
      if (char === '"' && line[i + 1] === '"' && quoted) { cell += '"' ; i += 1; }
      else if (char === '"' ) quoted = !quoted;
      else if (char === "," && !quoted) { cells.push(cell); cell = ""; }
      else cell += char;
    }
    cells.push(cell);
    assert.equal(quoted, false, "CSV row must have balanced quotes");
    return cells;
  };
  const headers = parseLine(lines.shift());
  return lines.map(line => Object.fromEntries(headers.map((key, index) => [key, parseLine(line)[index] ?? ""])));
}

test("Khmer romanization is rendered separately from phonetic IPA output",()=>{
  const result=renderKhmerRomanizationText("សុខា",()=>"Sokha");
  assert.equal(result.text,"Сок'а");
  assert.equal(result.status,"PROVISIONAL");
  assert.equal(result.unsupported,0);
});

test("non-Khmer Latin text and punctuation pass through unchanged",()=>{
  const result=renderKhmerRomanizationText("Hello សុខា! 42",()=>"Sokha");
  assert.equal(result.text,"Hello Сок'а! 42");
  assert.equal(result.status,"PROVISIONAL");
});

test("longest-match romanization digraphs preserve the matrix distinctions",()=>{
  assert.equal(renderLatinWord("KHM").text,"К'М");
  assert.equal(renderLatinWord("chh").text,"ч'");
  assert.equal(renderLatinWord("ng").text,"нг");
  assert.equal(renderLatinWord("ph").text,"п'");
});

test("unmodelled Latin letters remain explicit rather than silently guessed",()=>{
  const result=renderKhmerRomanizationText("សុខា",()=>"Sokha q");
  assert.equal(result.text,"Сок'а ⟦q⟧");
  assert.equal(result.status,"PARTIAL");
  assert.equal(result.unsupported,1);
});

test("text without Khmer is preserved as passthrough",()=>{
  const result=renderKhmerRomanizationText("Latin 123!",()=>"should not run");
  assert.equal(result.text,"Latin 123!");
  assert.equal(result.status,"PASSTHROUGH");
});

test("ASCII forms represented by the vowel matrix have explicit Ukrainian candidates",()=>{
  const pairs=[
    ["a","а"],["e","е"],["i","і"],["o","о"],["u","у"],["ei","ей"],["ai","ай"],
    ["ey","ей"],["ao","ао"],["au","ау"],["ou","оу"],["ae","ае"],["oe","и"],
    ["roe","ри"],["loe","ли"],["uo","уо"],["aeu","аеу"],["eu","еу"],["oea","иа"],
    ["ie","іє"],["om","ом"],["um","ум"],["am","ам"],["oam","оам"],["ah","аг"],
    ["eah","еаг"],["oh","ог"],["uh","уг"],["eh","ег"],["aoh","аог"],["oah","оаг"],
    ["ang","анг"],["eang","еанг"],
  ];
  for(const [latin,ukrainian] of pairs) assert.equal(renderLatinWord(latin).text,ukrainian,latin);
});

test("every distinct PCGN consonant romanization unit has an explicit Ukrainian candidate",()=>{
  const pairs=[
    ["k","к"],["kh","к'"],["ng","нг"],["ch","ч"],["chh","ч'"],["nh","нь"],
    ["d","д"],["th","т'"],["n","н"],["t","т"],["b","б"],["p","п"],
    ["ph","п'"],["m","м"],["y","й"],["r","р"],["l","л"],["v","в"],
    ["s","с"],["h","г"],["'","ʼ"],["’","ʼ"],
  ];
  for(const [latin,ukrainian] of pairs){
    const result=renderLatinWord(latin);
    assert.equal(result.text,ukrainian,latin);
    assert.equal(result.unsupported,0,latin);
  }
});

test("every canonical PCGN consonant row is executable by the Ukrainian adapter", () => {
  const rows = parseCsv(readFileSync(path.join(root, "data/khmer/romanization_ukrainian.csv"), "utf8"));
  assert.equal(rows.length, 22, "the canonical consonant crosswalk must retain all 22 PCGN rows");
  for (const row of rows) {
    const latinForms = row.romanization.split(",").map(value => value.trim());
    const ukrainianForms = row.ukrainian_candidate.split("/").map(value => value.trim());
    assert.equal(latinForms.length, ukrainianForms.length, `parallel romanization/target forms for PCGN row ${row.table_row}`);
    for (let i = 0; i < latinForms.length; i += 1) {
      const result = renderLatinWord(latinForms[i]);
      assert.equal(result.text, ukrainianForms[i], `PCGN row ${row.table_row}: ${latinForms[i]}`);
      assert.equal(result.unsupported, 0, `PCGN row ${row.table_row}: ${latinForms[i]} must not be unsupported`);
    }
  }
});
