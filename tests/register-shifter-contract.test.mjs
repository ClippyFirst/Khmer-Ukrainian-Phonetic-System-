import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { parseSyllable } from "../src/main.js";

const fixture = JSON.parse(
  readFileSync(new URL("../data/tests/register-shifter-contract.json", import.meta.url), "utf8")
);

assert.equal(fixture.schema_version, 1);
for (const item of fixture.cases) {
  const result = parseSyllable(item.surface);
  assert.equal(result.register, item.register, item.id);
  assert.equal(result.register_rule, item.rule, item.id);
  assert.equal(result.status, item.status, item.id);
}
console.log("Shared Khmer register-shifter contract passed in browser runtime");
