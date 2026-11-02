// Institutional content drawn from ACAIO_PROJECT_CONTEXT.md. Edit here, not in components.

export const principles = [
  { title: 'Practitioner-led', text: 'Shaped by executives accountable for enterprise AI.' },
  { title: 'Independent', text: 'Vendors and sponsors do not control standards or research.' },
  { title: 'Evidence-based', text: 'Grounded in enterprise practice and credible research.' },
  { title: 'Responsible', text: 'Focused on value creation while keeping AI governable.' },
  { title: 'Collaborative', text: 'Complements rather than attempts to own the entire Australian AI ecosystem.' },
  { title: 'Profession-first', text: 'Institutional credibility takes priority over rapid monetisation.' },
];

export const mandates = [
  { title: 'Define the profession', text: 'Develop shared accountabilities, competencies and professional standards for enterprise AI leadership.' },
  { title: 'Build the executive community', text: 'Bring together practitioners across sectors to exchange experience and help shape the discipline.' },
  { title: 'Develop practical knowledge', text: 'Build a Body of Knowledge, frameworks and research grounded in enterprise practice.' },
  { title: 'Develop a representative voice', text: 'Create a foundation for enterprise AI leaders to contribute informed perspectives to policy and professional debate.' },
];

export const initialAgenda = [
  { title: 'Professional Charter', text: "A shared statement of the profession's purpose, principles and responsibilities." },
  { title: 'CAIO Competency Framework', text: 'A framework for the capabilities required to lead enterprise AI.' },
  { title: 'AI Leadership & Accountability Framework', text: 'Clarity on leadership responsibilities, governance and accountability for enterprise AI.' },
  { title: 'Enterprise AI Maturity Model', text: 'A basis for assessing organisational progress and identifying priorities for development.' },
  { title: 'State of Enterprise AI Leadership in Australia', text: 'A proposed research report examining how the discipline is developing in Australian organisations.' },
];

/** Potential first-wave professional knowledge, grouped for the Agenda page. All proposed; none published. */
export const agendaGroups = [
  {
    title: 'Foundations',
    text: 'The shared definition and statement of the profession.',
    items: [
      { title: 'ICAIO Professional Charter', initial: true, domains: [] },
      { title: 'Enterprise AI Leadership definition', initial: false, domains: [] },
      { title: 'ICAIO Body of Knowledge', initial: false, domains: [] },
    ],
  },
  {
    title: 'Roles and accountability',
    text: 'Who is accountable for what, and how decisions are shared across the executive team.',
    items: [
      { title: 'CAIO Role & Accountability Framework', initial: false, domains: ['Governance'] },
      { title: 'AI Leadership & Accountability Framework', initial: true, domains: ['Governance'] },
      { title: 'CAIO, CIO, CTO, CDO and CRO decision-rights model', initial: false, domains: ['Governance', 'Strategy'] },
    ],
  },
  {
    title: 'Capability and maturity',
    text: 'What competence looks like for leaders, and maturity for organisations.',
    items: [
      { title: 'CAIO Competency Framework', initial: true, domains: [] },
      { title: 'Enterprise AI Maturity Model', initial: true, domains: [] },
    ],
  },
  {
    title: 'Domain frameworks',
    text: 'Practical frameworks for specific domains of Enterprise AI Leadership.',
    items: [
      { title: 'Ethical AI Position Framework', initial: false, domains: ['Ethical AI'] },
      { title: 'AI Investment, Value & Performance Framework', initial: false, domains: ['Value'] },
      { title: 'Agentic AI Governance Framework', initial: false, domains: ['Governance', 'Operating AI'] },
      { title: 'AI Workforce & Adoption Framework', initial: false, domains: ['Adoption'] },
    ],
  },
  {
    title: 'Evidence',
    text: 'Research into how the discipline is developing in Australian organisations.',
    items: [
      { title: 'State of Enterprise AI Leadership in Australia', initial: true, domains: [] },
    ],
  },
];

export const stages = [
  { title: 'Coalition', text: 'Recruit a small number of credible leaders and establish the Founding Council.' },
  { title: 'Define', text: 'Define the profession, charter, accountabilities and initial competency framework.' },
  { title: 'Evidence', text: 'Conduct research and benchmarking; develop substantive professional knowledge.' },
  { title: 'Foundation membership', text: 'Invite an initial, carefully selected cohort of enterprise AI leaders.' },
  { title: 'Public launch', text: 'Launch with credible leaders, research and professional frameworks in place.' },
];

/** Hero images: AI-generated, illustrative. Replace with commissioned photography before launch. */
export const heroCities = [
  { slug: 'sydney', name: 'Sydney' },
  { slug: 'melbourne', name: 'Melbourne' },
  { slug: 'brisbane', name: 'Brisbane' },
  { slug: 'canberra', name: 'Canberra' },
  { slug: 'perth', name: 'Perth' },
  { slug: 'adelaide', name: 'Adelaide' },
];

export const sectors = [
  'Financial services', 'Government', 'Healthcare', 'Telecommunications', 'Retail', 'Resources',
  'Professional services', 'Technology', 'Higher education', 'Other',
];

export const councilMayDefine = [
  'Enterprise AI Leadership',
  'The CAIO role and accountability framework',
  'A professional competency framework',
  'The Body of Knowledge',
  'Education and professional development requirements',
  'The research agenda and maturity model',
];
