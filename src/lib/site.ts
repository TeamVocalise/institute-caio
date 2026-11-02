export const site = {
  name: 'Institute of Chief AI Officers',
  shortName: 'ICAIO',
  domain: 'caio.org.au',
  description:
    "ICAIO is being established for Australia's enterprise AI leaders. Explore the proposed professional agenda and express interest in the Founding Council.",
  /** Formation site: every page is noindex until the public launch (Stage 5). */
  formationMode: true,
};

export const routes = {
  eoi: '/express-interest/',
  register: '/register-interest/',
  getInvolved: '/get-involved/',
  councilMembers: '/council-members/',
};

export const mainNav = [
  { href: '/about/', label: 'About' },
  { href: '/enterprise-ai-leadership/', label: 'Enterprise AI Leadership' },
  { href: '/founding-council/', label: 'Founding Council' },
  { href: '/agenda/', label: 'Agenda' },
];

export const footerExplore = [
  { href: '/about/', label: 'About ICAIO' },
  { href: '/enterprise-ai-leadership/', label: 'Enterprise AI Leadership' },
  { href: '/founding-council/', label: 'Founding Council' },
  { href: '/council-members/', label: 'Council members' },
  { href: '/members/', label: 'Members' },
  { href: '/agenda/', label: 'Proposed agenda' },
];
