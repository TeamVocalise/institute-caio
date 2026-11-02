Status: Draft for review, 13 October 2026.

# New pages: privacy, terms, Acknowledgement of Country, members, supporters, 404

The page copy lives in the Astro files listed below. This note records the sources, decisions and open items.

## P007 Privacy policy: /privacy/ (src/pages/privacy.astro)
- Structured around the Privacy Act 1988 (Cth) and the Australian Privacy Principles. It covers collection, use, disclosure, overseas disclosure, security, retention, access and correction, updates, cookies and complaints, including the OAIC.
- It reflects the decisions to date: Council membership is by invitation, ICAIO may invite executives directly (so it collects information from public sources and referrers), the Chair is involved in appointments, there is no analytics, and spam protection may be used.
- Placeholders: the responsible entity and ABN, the overseas service providers and countries, the privacy contact email and the publication date.
- **Needs legal review before launch.** This is a sound starting draft, not legal advice.

## P008 Terms of use and disclaimer: /terms/ (src/pages/terms.astro)
- Covers formation status (proposed, not incorporated), no professional advice, accuracy and cited forecasts, illustrative images, intellectual property (ICAIO-owned, personal non-commercial use with attribution), submissions, acceptable use, links, liability (preserving rights under the Australian Consumer Law), governing law and changes.
- Placeholders: the responsible entity and ABN, the governing state (Victoria proposed), the contact email and the date.
- **Needs legal review before launch.**

## P009 Acknowledgement of Country: footer, every page
"ICAIO acknowledges the Traditional Custodians of the lands across Australia on which we live and work, and pays respect to Elders past and present. We recognise Aboriginal and Torres Strait Islander peoples' continuing connection to land, waters and culture."
- Nick asked for a "Welcome to Country". A Welcome to Country can only be given by Traditional Owners, so an organisation's website uses an Acknowledgement of Country. The wording is national because ICAIO is a national body.

## P010 Member listing: /members/ (src/pages/members.astro, data in src/content/directory.json)
- A table with search, filters for sector, state and membership, and sortable columns. It is sorted by surname by default. Founding Council members link to their profile pages.
- SAMPLE DATA ONLY: 20 fictional people (the 12 sample Council members plus 8 sample founding members), with a yellow sample banner. The page is hidden from the sitemap.
- Membership categories and eligibility are still OPEN. The page says so.

## P011 Institute supporters: /supporters/ (src/pages/supporters.astro, data in src/content/supporters.json)
- Primary supporters (2 across, larger logos) and secondary supporters (3 across), each with a logo and organisation name, followed by an independence section ("Support without influence") and a "Register interest as a supporter" call to action.
- SAMPLE DATA ONLY: placeholder names and logo boxes, with a yellow sample banner. The page is hidden from the sitemap.
- To add a real supporter, put the logo in public/images/supporters/ and add an entry with tier, name, logo path and URL.
- The sponsorship structure and pricing are still OPEN in the context file.

## 404 page: src/pages/404.astro
"This page could not be found." It links to the main pages and the expression-of-interest call to action.

## Footer changes
- The Explore list now includes "Members". The Get involved list now includes "Institute supporters".
- The footer base now links to the privacy policy and terms of use.
