import assert from "node:assert/strict";
import { test } from "node:test";
import { renderKhmerRomanizationText, renderLatinWord } from "../src/khmer-romanization-ukrainian.js";

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
