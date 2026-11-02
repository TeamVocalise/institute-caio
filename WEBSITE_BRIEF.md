# ICAIO Website Brief

## Goal
Create the first public website for the Institute of Chief AI Officers (ICAIO), an emerging independent not-for-profit professional institution for executives accountable for enterprise AI.

Read `ACAIO_PROJECT_CONTEXT.md` before making content, UX, information architecture or design decisions.

## Phase 1 Job To Be Done
A senior enterprise AI executive, board member, government leader or potential Founding Council participant should arrive and understand within roughly 30 seconds:

1. What ICAIO is.
2. Why it needs to exist now.
3. Who it is for.
4. What "Enterprise AI Leadership" means.
5. What ICAIO intends to establish.
6. How they can become involved in the founding phase.

The site must establish credibility without pretending ICAIO is more mature than it is.

## Primary CTA
**Express interest in the Founding Council**

Alternative copy can be tested, e.g.:
- Help shape the profession
- Join the founding conversation
- Express interest

Do not imply automatic appointment to the Council.

## Secondary CTA
**Register interest in ICAIO**

This can capture prospective members, partners, researchers, education providers and other relevant stakeholders.

## Initial Sitemap

### `/`
Home

### `/about`
Purpose, why ICAIO, founding principles, institutional model.

### `/enterprise-ai-leadership`
Define the eight domains:
Ethical AI / Governance / Strategy / Transformation / Value / Capability / Adoption / Operating AI.

### `/founding-council`
Explain why the Council is being formed, proposed composition, expected contribution and expression-of-interest pathway.

### `/agenda`
Initial professional agenda: charter, competency framework, accountability framework, maturity model, benchmarking, research and Body of Knowledge.

### `/insights`
Future home for research, articles and reports. It may initially contain only a small number of high-quality pieces. Never populate it with fake articles.

### `/get-involved`
Short page linking to the two forms below (updated 12 October 2026).

### `/express-interest`
Founding Council expression of interest form.

### `/register-interest`
General interest form.

### `/council-members` and `/council/<name>`
Future-state Founding Council grid and individual profile pages. Sample data only until members are appointed.

Founding Council EOI, general interest, prospective institutional/education partnerships.

## Homepage Content Architecture

### Hero
Working direction:

**Leading Australia's AI transformation.**

Supporting institutional line:
**The Institute of Chief AI Officers**

Draft proposition:
"ICAIO is being established as the professional institution for executives responsible for artificial intelligence strategy, transformation, governance, capability, adoption and value creation across Australian organisations."

Primary CTA: Express interest in the Founding Council
Secondary CTA: Explore Enterprise AI Leadership

### Problem / Context
Headline direction:
**AI is becoming an enterprise capability. AI leadership must become a professional discipline.**

Explain briefly that accountability is emerging faster than agreed professional standards, competencies and operating practices.

### Eight Domains
Create a high-quality visual/component for:
Ethical AI
Governance
Strategy
Transformation
Value
Capability
Adoption
Operating AI

This should be a core reusable component, not a decorative graphic.

### Why ICAIO
Four mandates:
1. Define the profession.
2. Build the executive community.
3. Develop practical knowledge.
4. Represent enterprise AI leadership.

### Founding Phase
Explain that ICAIO is assembling a small Founding Council to help define the profession.

Avoid listing unconfirmed people/logos.

### Initial Agenda
Show a restrained selection of proposed outputs:
- Professional Charter
- CAIO Competency Framework
- AI Leadership & Accountability Framework
- Enterprise AI Maturity Model
- State of Enterprise AI Leadership in Australia

### Independence
Short section:
Practitioner-led / Independent / Evidence-based / Responsible / Collaborative.

### Final CTA
**Help define the profession.**
Expression-of-interest CTA.

## UX / Design Direction
Create a premium Australian institutional aesthetic suitable for:
- major-bank executives
- ASX company leaders
- Commonwealth/state government executives
- board directors
- university leaders

The site should feel more like a contemporary professional institution or serious policy/research organisation than a SaaS product.

Priorities:
- excellent typography
- strong whitespace
- disciplined grid
- restrained motion
- accessible contrast
- fast performance
- responsive layouts
- high-quality editorial hierarchy
- reusable design system

Avoid generic AI stock imagery. Prefer typography, diagrams, data/research visualisation and subtle abstract visual language if imagery is needed.

## Technical Principles
- Use semantic HTML and accessibility best practices.
- Aim for WCAG 2.2 AA.
- Responsive from mobile through large desktop.
- Optimise Core Web Vitals.
- SEO metadata and social sharing metadata.
- Structured content architecture so a CMS can be added or swapped later.
- Forms must have validation, consent language and spam protection.
- Do not expose secrets/API keys client-side.
- Add analytics only through an explicit configurable integration.
- Keep dependencies conservative.
- Document setup and deployment clearly.

## Content Integrity
Never fabricate:
- members
- directors
- partners
- endorsements
- research findings
- statistics
- certification
- accreditation
- government relationships
- university relationships

Use placeholders in development data where required and label them clearly as placeholders.

## Future Capabilities To Allow For
Architecture should be able to grow to support:
- member login
- member directory
- events
- research library
- paid membership
- CPD tracking
- education catalogue
- accredited-provider directory
- certification applications
- benchmarking tools
- corporate memberships
- partner portal

Do not build these in Phase 1 unless separately requested.

## Suggested First Codex Task
1. Read `ACAIO_PROJECT_CONTEXT.md` and this brief.
2. Audit the existing repository before changing anything.
3. Propose the information architecture, component architecture and implementation plan.
4. Identify any existing design system, framework and deployment constraints.
5. Do not start a wholesale rebuild until the plan is presented.
6. Once approved, implement the homepage first as the design-system reference page.
