// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import { isHiddenPath } from './src/lib/pages.ts';

export default defineConfig({
  site: 'https://caio.org.au',
  // Fixed port so this site never collides with Nick's other local Astro sites on 4321.
  server: { port: 4340 },
  integrations: [
    sitemap({ filter: (page) => !isHiddenPath(new URL(page).pathname) }),
  ],
  vite: { plugins: [tailwindcss()] },
});
