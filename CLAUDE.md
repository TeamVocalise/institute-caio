# ICAIO website

Website for the Institute of Chief AI Officers (ICAIO), caio.org.au: a formation-stage professional institution for executives accountable for enterprise AI in Australia.

- Brief: docs/brief.md (read first), then ACAIO_PROJECT_CONTEXT.md (strategic source of truth) and WEBSITE_BRIEF.md
- Planning: docs/02-technical-approach.md, docs/04-approved-decisions.md
- Brand (tone, colours, type, look and feel): docs/brand.md. Never use the Vocalise design system.
- Stack: ~/AI-Library/standards/architecture/default-web-stack.md unless docs/02-technical-approach.md says otherwise
- For planning or building, use the website-builder agent.

## Project-specific rules
- Never fabricate members, partners, endorsements, research or statistics. Council members in src/content/members are SAMPLE DATA (sample: true) until real, consented profiles replace them.
- Formation wording is mandatory ("being established", "proposed", "founding").
- site.formationMode in src/lib/site.ts keeps every page noindex. Do not turn it off without Nick's approval.
- Don't reword approved copy. No em dashes in website copy. Australian English.
- Domain content lives in src/content/domains.json; members in src/content/members/*.md; other institutional lists in src/data/institution.ts.
- The static draft in site/ (built by build.py) is superseded by this Astro project and kept only for reference.

## Commands
    npm install
    npm run dev      # http://localhost:4340 (or: astro dev --background)
    npm run build
    npm run check
