import { defineCollection } from 'astro:content';
import { file, glob } from 'astro/loaders';
import { z } from 'astro/zod';

/** The Enterprise AI Leadership domains, in display order. */
const domains = defineCollection({
  loader: file('src/content/domains.json'),
  schema: z.object({
    order: z.number(),
    name: z.string(),
    audience: z.string().optional(),
    description: z.string(),
    /** Draft detail for the Enterprise AI Leadership page, to be refined with the Founding Council. */
    accountabilities: z.array(z.string()).default([]),
    keyQuestion: z.string().optional(),
  }),
});

/** Founding Council members. SAMPLE DATA ONLY until members are appointed and consent. */
const members = defineCollection({
  loader: glob({ pattern: '**/*.md', base: 'src/content/members' }),
  schema: z.object({
    sample: z.boolean().default(true),
    firstName: z.string(),
    surname: z.string(),
    councilTitle: z.string(),
    jobTitle: z.string(),
    organisation: z.string(),
    tags: z.array(z.string()),
    statement: z.string(),
    aiForGood: z.string().optional(),
    contribution: z.string().optional(),
    linkedin: z.url().optional(),
    corporateProfile: z.url().optional(),
    headshot: z.string().optional(),
  }),
});

/** Institute member listing. SAMPLE DATA ONLY: fictional placeholders until real members join and consent. */
const directory = defineCollection({
  loader: file('src/content/directory.json'),
  schema: z.object({
    firstName: z.string(),
    surname: z.string(),
    membership: z.string(),
    jobTitle: z.string(),
    organisation: z.string(),
    sector: z.string(),
    state: z.string(),
    profile: z.string().optional(),
    /** Optional LinkedIn profile URL. Shown as an icon in the member listing. */
    linkedin: z.url().optional(),
  }),
});

/** Institute supporters. SAMPLE DATA ONLY until supporters are confirmed. Logos go in public/images/supporters/. */
const supporters = defineCollection({
  loader: file('src/content/supporters.json'),
  schema: z.object({
    tier: z.enum(['primary', 'secondary']),
    name: z.string(),
    logo: z.string().optional(),
    url: z.url().optional(),
  }),
});

export const collections = { domains, members, directory, supporters };
