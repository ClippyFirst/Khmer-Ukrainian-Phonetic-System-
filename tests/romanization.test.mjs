import assert from "node:assert/strict";
import { test } from "node:test";
import { khmerToLatin } from "@gmana/km-translit";

test("Khmer romanization returns Latin output for a documented sample", () => {
  const result = khmerToLatin("ខ្មែរ");
  assert.equal(typeof result, "string");
  assert.match(result, /[A-Za-z]/u);
  assert.doesNotMatch(result, /[\u1780-\u17ff]/u);
});

test("the short Khmer mixed-text sample preserves ASCII digits and punctuation", () => {
  const sentence = "សួស្តី 123! ភាសាខ្មែរ។";
  const romanized = khmerToLatin(sentence);
  assert.match(romanized, /[A-Za-z]/u);
  assert.doesNotMatch(romanized, /[\u1780-\u17d3\u17d6-\u17ff]/u);
  assert.ok(romanized.includes("123"));
  assert.ok(romanized.includes(" "));
  assert.ok(romanized.includes("!"));
  assert.ok(romanized.includes("។"));
});

test("the full user greeting sentence keeps spaces and punctuation in Khmer-to-Latin romanization", () => {
  const sentence = "សួស្តី! ខ្ញុំឈ្មោះ សុភា។ ខ្ញុំមកពីប្រទេសកម្ពុជា ហើយខ្ញុំចូលចិត្តរៀនភាសាថ្មីៗ និងអានសៀវភៅ។";
  const romanized = khmerToLatin(sentence);
  assert.match(romanized, /[A-Za-z]/u);
  assert.doesNotMatch(romanized, /[\u1780-\u17d3\u17d6-\u17ff]/u, "Khmer letters and signs must be converted; Khmer punctuation is intentionally preserved");
  assert.equal((romanized.match(/។/gu) ?? []).length, 2, "both Khmer sentence stops must be preserved");
  assert.ok(romanized.includes(" "));
  assert.ok(romanized.includes("!"));
  assert.ok(romanized.includes("។"));
});


test("Khmer romanization preserves Khmer numerals, ASCII numbers, mixed Latin text and punctuation",()=>{
  const source="២០២៦ ABC-42, សួស្តី។";
  const romanized=khmerToLatin(source);
  assert.match(romanized,/[A-Za-z]/u);
  assert.ok(romanized.includes("២០២៦")||romanized.includes("2026"),"Khmer numerals must remain visible or be rendered as Arabic digits");
  assert.ok(romanized.includes("ABC-42"),"mixed Latin and ASCII numerals must be preserved");
  assert.ok(romanized.includes(","));
  assert.ok(romanized.includes("។"));
  assert.ok(romanized.includes(" "));
  assert.doesNotMatch(romanized,/[ក-៓៖-៟៪-៿]/u,"unsupported Khmer letters/signs must not leak into the romanized output");
});
