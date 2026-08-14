import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://gregjackson.design',
  build: {
    // Emit /about-me/index.html so URLs match the WordPress site exactly
    format: 'directory',
  },
});
