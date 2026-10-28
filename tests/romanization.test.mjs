import assert from "node:assert/strict";
import { test } from "node:test";
import { khmerToLatin } from "@gmana/km-translit";

test("Khmer romanization returns Latin output for a documented sample", () => {
  const result = khmerToLatin("ខ្មែរ");
  assert.equal(typeof result, "string");
  assert.match(result, /[A-Za-z]/u);
  assert.doesNotMatch(result, /[\u1780-\u17ff]/u);
});
