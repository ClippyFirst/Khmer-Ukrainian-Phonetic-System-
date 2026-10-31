import assert from "node:assert/strict";
import { test } from "node:test";
import { khmerToLatin } from "@gmana/km-translit";

test("Khmer romanization returns Latin output for a documented sample", () => {
  const result = khmerToLatin("ខ្មែរ");
  assert.equal(typeof result, "string");
  assert.match(result, /[A-Za-z]/u);
  assert.doesNotMatch(result, /[\u1780-\u17ff]/u);
});

test("the full user greeting sentence keeps spaces and punctuation in Khmer-to-Latin romanization", () => {
  const sentence = "សួស្តី! ខ្ញុំឈ្មោះ សុភា។ ខ្ញុំមកពីប្រទេសកម្ពុជា ហើយខ្ញុំចូលចិត្តរៀនភាសាថ្មីៗ និងអានសៀវភៅ។";
  const romanized = sentence.split(/(\s+)/u).map((part) =>
    /[\u1780-\u17ff]/u.test(part) ? khmerToLatin(part) : part,
  ).join("");
  assert.match(romanized, /[A-Za-z]/u);
  assert.ok(romanized.includes(" "));
  assert.ok(romanized.includes("!"));
  assert.ok(romanized.includes("។"));
});
