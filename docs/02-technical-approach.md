Status: Proposed. Stack basis approved 12 October 2026; hosting and form backend still to be confirmed.

# Technical approach

**Recommendation:** Astro static site with strict TypeScript and Tailwind CSS 4, with content kept as files. This is the default web stack with no departures.

## Stack (as built, 12 October 2026)
- Astro 7.3 (static output), TypeScript strict, Tailwind CSS 4.3 via @tailwindcss/vite, @astrojs/sitemap.
- Design tokens are in `@theme` in src/styles/global.css. Component classes are ported from the approved static draft.
- Content collections: `domains` (src/content/domains.json) and `members` (src/content/members/*.md, sample data). Other institutional lists are in src/data/institution.ts.
- Site config is in src/lib/site.ts (name, routes, navigation, `formationMode`). Hidden pages are in src/lib/pages.ts.
- Every page is noindex while `formationMode` is true. Council member pages are also excluded from the sitemap.

## Departures from the default stack
None.

## Still to confirm
- **Hosting:** Cloudflare (default), deployed from a private TeamVocalise GitHub repo. Not yet set up.
- **Forms:** Web3Forms plus Cloudflare Turnstile (default). The forms are prototypes that validate and never send. The development recipient would be nick@vocalise.com.au, and the production recipient needs explicit approval.
- **Analytics:** none until Nick chooses a configurable integration.
- **Hero images:** the AI-generated drafts are served from public/images/hero/. Replace them with commissioned or licensed photography before launch, and consider astro:assets for optimisation.

## Before launch
- A responsible entity and ABN for the privacy policy and footer.
- A privacy policy covering form data (Privacy Act / APPs).
- Real, consented Council profiles and headshots, and removal of the sample data.
- A social image (1200 × 630 PNG).
- Fonts confirmed (Source Serif 4 and Inter are proposed).
- Nick's approval to turn off `formationMode`.
