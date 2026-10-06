import { defineConfig } from "vite";

export default defineConfig({
  base: "./",
  build: {
    rollupOptions: {
      input: {
        service: "index.html",
        system: "system.html"
      }
    }
  }
});
