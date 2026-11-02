import { test, expect } from "@playwright/test";

test("Khmer input produces visible IPA and Ukrainian result", async ({ page }) => {
  await page.goto("/");
  await page.locator("#source").fill("ក");
  await expect(page.locator("#results")).toBeVisible();
  await expect(page.locator("#ipa-result")).toHaveText("/kɑː/");
  await expect(page.locator("#ua-result")).toHaveText("ка");
  await expect(page.locator("#status")).toHaveText("PROPOSED");
});

test("known lexical phrase is rendered by the browser runtime", async ({ page }) => {
  await page.goto("/");
  await page.locator("#example").click();
  await expect(page.locator("#source")).toHaveValue("ភាសាខ្មែរ");
  await expect(page.locator("#ipa-result")).toHaveText("/pʰiəsaː kʰmae/");
  await expect(page.locator("#ua-result")).toHaveText("п'ієса к'мае");
});

test("unsupported mixed input is visibly withheld", async ({ page }) => {
  await page.goto("/");
  await page.locator("#source").fill("កx");
  await expect(page.locator("#results")).toBeVisible();
  await expect(page.locator("#status")).toHaveText("INVALID OR UNSUPPORTED");
  await expect(page.locator("#ua-result")).toHaveText("⟦ТРАНСКРИПЦІЮ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
});

test("romanization mode does not reuse phonetic Ukrainian output", async ({ page }) => {
  await page.goto("/");
  await page.locator("#source").fill("ក");
  await page.locator("#mode-romanization").click();
  await expect(page.locator("#mode-romanization")).toHaveAttribute("aria-pressed", "true");
  await expect(page.locator("#ua-romanization-panel")).toBeVisible();
  await expect(page.locator("#ua-romanization-status")).toContainText("PARTIAL");
  await expect(page.locator("#ua-romanization-result")).toContainText("МАТРИЦЯ НЕ ЗАВЕРШЕНА");
  await expect(page.locator("#mode-phonetic")).toHaveAttribute("aria-pressed", "false");
});

test("clear control restores the empty state", async ({ page }) => {
  await page.goto("/");
  await page.locator("#source").fill("ក");
  await page.locator("#clear").click();
  await expect(page.locator("#results")).toBeHidden();
  await expect(page.locator("#empty")).toBeVisible();
});
