import { test, expect } from "@playwright/test";

test("Khmer input renders IPA and Ukrainian output without a DOM exception", async ({ page }) => {
  const pageErrors = [];
  page.on("pageerror", error => pageErrors.push(error.message));
  await page.goto("/");
  await page.locator("#source").fill("ក");
  await expect(page.locator("#results")).toBeVisible();
  await expect(page.locator("#ipa-result")).toHaveText("/kɑː/");
  await expect(page.locator("#ua-result")).toHaveText("ка");
  await expect(page.locator("#status")).toHaveText("PROPOSED");
  expect(pageErrors).toEqual([]);
});

test("unsupported mixed input remains visibly withheld", async ({ page }) => {
  await page.goto("/");
  await page.locator("#source").fill("កx");
  await expect(page.locator("#results")).toBeVisible();
  await expect(page.locator("#status")).toHaveText("INVALID OR UNSUPPORTED");
  await expect(page.locator("#ua-result")).toHaveText("⟦ТРАНСКРИПЦІЮ НЕ ВСТАНОВЛЕНО ДЛЯ ЧАСТИНИ ВВОДУ⟧");
});

test("clear control restores the empty state", async ({ page }) => {
  await page.goto("/");
  await page.locator("#source").fill("ក");
  await page.locator("#clear").click();
  await expect(page.locator("#results")).toBeHidden();
  await expect(page.locator("#empty")).toBeVisible();
});
