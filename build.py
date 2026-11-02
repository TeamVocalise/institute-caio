#!/usr/bin/env python3
"""Generates the ICAIO static draft site from shared header/footer templates."""
from pathlib import Path

OUT = Path(__file__).parent / "site"

NAV = [
    ("about.html", "About"),
    ("enterprise-ai-leadership.html", "Enterprise AI Leadership"),
    ("founding-council.html", "Founding Council"),
    ("agenda.html", "Agenda"),
]
EOI = "express-interest.html"

CITIES = [
    ("sydney", "Sydney", "99b18913-1184-4bd8-ab7e-52b1a8cd9fe3"),
    ("melbourne", "Melbourne", "a320c14d-16af-4671-b448-3b5e62636e67"),
    ("brisbane", "Brisbane", "cf4930dc-10e6-4dd7-8dd7-38dbf3e9bc57"),
    ("canberra", "Canberra", "d7f9fbff-71f1-45ca-b6ad-cf8976799236"),
    ("perth", "Perth", "9df3c06d-5a98-4307-8bf3-ec5a5a28df7b"),
    ("adelaide", "Adelaide", "bf9a6d53-f1bd-4fc2-adbd-67a0f6443ce0"),
]

DOMAINS = [
    ("Ethical AI", "<strong>For Boards:</strong> The role of AI, AGI, ASI and QI in humanity and society, and how organisations determine and define their position."),
    ("Governance", "Responsible AI, risk, assurance, accountability, regulation and board oversight."),
    ("Strategy", "Enterprise AI strategy, portfolio choices, investment and alignment."),
    ("Transformation", "Operating-model and process transformation enabled by AI."),
    ("Value", "Business cases, benefits, productivity, growth and value realisation."),
    ("Capability", "Data, platforms, models, agents, architecture, vendors and organisational capability."),
    ("Adoption", "Workforce, skills, change, behaviours and organisational adoption."),
    ("Operating AI", "The continual management, improvement and optimisation of the operation of AI models, agents and systems, workflows, and outputs."),
]

PRINCIPLES = [
    ("Practitioner-led", "Shaped by executives accountable for enterprise AI."),
    ("Independent", "Vendors and sponsors do not control standards or research."),
    ("Evidence-based", "Grounded in enterprise practice and credible research."),
    ("Responsible", "Focused on value creation while keeping AI governable."),
    ("Collaborative", "Complements rather than attempts to own the entire Australian AI ecosystem."),
    ("Profession-first", "Institutional credibility takes priority over rapid monetisation."),
]

AGENDA5 = [
    ("Professional Charter", "A shared statement of the profession's purpose, principles and responsibilities."),
    ("CAIO Competency Framework", "A framework for the capabilities required to lead enterprise AI."),
    ("Leadership &amp; Accountability Framework", "Clarity on leadership responsibilities, governance and accountability for enterprise AI."),
    ("Enterprise AI Maturity Model", "A basis for assessing organisational progress and identifying priorities for development."),
    ("State of Enterprise AI Leadership in Australia", "A proposed research report examining how the discipline is developing in Australian organisations."),
]

MANDATES = [
    ("Define the profession", "Develop shared accountabilities, competencies and professional standards for enterprise AI leadership."),
    ("Build the executive community", "Bring together practitioners across sectors to exchange experience and help shape the discipline."),
    ("Develop practical knowledge", "Build a Body of Knowledge, frameworks and research grounded in enterprise practice."),
    ("Develop a representative voice", "Create a foundation for enterprise AI leaders to contribute informed perspectives to policy and professional debate."),
]

STAGES = [
    ("Coalition", "Recruit a small number of credible leaders and establish the Founding Council."),
    ("Define", "Define the profession, charter, accountabilities and initial competency framework."),
    ("Evidence", "Conduct research and benchmarking; develop substantive professional knowledge."),
    ("Foundation membership", "Invite an initial, carefully selected cohort of enterprise AI leaders."),
    ("Public launch", "Launch with credible leaders, research and professional frameworks in place."),
]

CUR = ' aria-current="page"'
FP = ' fetchpriority="high"'
ARROW = '<span class="arrow" aria-hidden="true">&rarr;</span>'


def ph(text):
    return f'<span class="placeholder">[{text}]</span>'


def header(current):
    links = "".join(
        f'<li><a href="{h}"{CUR if h == current else ""}>{t}</a></li>' for h, t in NAV
    )
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<div class="draft-bar" role="note"><strong>Draft for review.</strong> Not a launched website. Forms are not connected and no information is sent.</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="ICAIO home">
      <span class="brand-mark">ICAIO</span>
      <span class="brand-name">Institute of Chief AI Officers</span>
    </a>
    <nav class="nav" aria-label="Main">
      <ul>{links}</ul>
      <a class="btn btn-primary btn-sm" href="{EOI}">Express interest</a>
      <details class="menu">
        <summary>Menu</summary>
        <div class="menu-panel">
          <ul>{links}<li><a href="get-involved.html">Get involved</a></li></ul>
          <a class="btn btn-primary" href="{EOI}">Express interest in the Founding Council</a>
        </div>
      </details>
    </nav>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <span class="brand-mark">ICAIO</span>
        <p>The Institute of Chief AI Officers is being established as an independent, not-for-profit professional institution for executives accountable for enterprise AI.</p>
      </div>
      <div>
        <h2>Explore</h2>
        <ul>
          <li><a href="about.html">About ICAIO</a></li>
          <li><a href="enterprise-ai-leadership.html">Enterprise AI Leadership</a></li>
          <li><a href="founding-council.html">Founding Council</a></li>
          <li><a href="council-members.html">Council members</a></li>
          <li><a href="agenda.html">Proposed agenda</a></li>
        </ul>
      </div>
      <div>
        <h2>Get involved</h2>
        <ul>
          <li><a href="{EOI}">Founding Council expression of interest</a></li>
          <li><a href="register-interest.html">Register interest in ICAIO</a></li>
          <li><a href="#" aria-disabled="true">Privacy policy {ph('to come')}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span>caio.org.au &middot; Draft for review, October 2026</span>
      <span>Structure and operating entity to be confirmed. {ph('Responsible entity and ABN')}</span>
    </div>
  </div>
</footer>
<script src="assets/js/site.js" defer></script>"""


def page(filename, title, description, body, current=None):
    html = f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&display=swap">
<link rel="stylesheet" href="assets/css/site.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23172D36'/%3E%3Ctext x='16' y='22' font-family='Georgia' font-size='16' fill='%23F5F3EC' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E">
</head>
<body>
{header(current or filename)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")


# ---------- Home ----------
def hero():
    slides = []
    for n, (slug, name, fid) in enumerate(CITIES):
        active = " is-active" if n == 0 else ""
        loading = "eager" if n == 0 else "lazy"
        slides.append(
            f'<div class="hero-slide{active}" data-city="{name}">'
            f'<img src="assets/img/hero-{slug}.jpg" data-fallback="https://www.figma.com/api/mcp/asset/{fid}.png" '
            f'alt="" loading="{loading}" decoding="async"{FP if n == 0 else ""}></div>'
        )
    dots = "".join(
        f'<button type="button" aria-label="Show {name}" aria-current="{"true" if n == 0 else "false"}"></button>'
        for n, (_, name, _) in enumerate(CITIES)
    )
    return f"""<section class="hero" data-hero aria-labelledby="hero-title">
  <div class="hero-slides" aria-hidden="true">{''.join(slides)}</div>
  <div class="container">
    <div class="hero-inner">
      <p class="eyebrow">Institute of Chief AI Officers</p>
      <h1 id="hero-title"><span>AI is becoming an enterprise capability.</span> <span class="second">AI leadership must become a professional discipline.</span></h1>
      <p class="lede">ICAIO is being established as an independent, not-for-profit professional institution for executives accountable for enterprise AI in Australian organisations.</p>
      <p class="for">For Chief AI Officers and equivalent leaders with enterprise-wide AI responsibility, whatever their title.</p>
      <div class="actions">
        <a class="btn btn-primary" href="{EOI}">Express interest in the Founding Council {ARROW}</a>
        <a class="btn btn-ghost" href="#enterprise-ai-leadership">Explore Enterprise AI Leadership</a>
      </div>
    </div>
  </div>
  <p class="hero-caption">Illustrative image. Not ICAIO members.</p>
  <div class="hero-meta">
    <span class="hero-city" aria-live="off">{CITIES[0][1]}</span>
    <div class="hero-dots" role="group" aria-label="Choose city view">{dots}</div>
    <button type="button" class="hero-pause" aria-pressed="false">Pause</button>
  </div>
</section>"""


def domains_grid(tile):
    return f'<div class="domain-band">{tile}</div><div class="domains">' + "".join(
        f'<article class="domain"><span class="domain-num">{n:02d}</span><h3>{t}</h3><p>{d}</p></article>'
        for n, (t, d) in enumerate(DOMAINS, 1)
    ) + "</div>"


INTEGRATION = "Enterprise AI leadership integrates these disciplines to convert rapidly evolving AI capability into sustainable organisational performance."


def rows(items, tags=None):
    out = '<ol class="rows">'
    for n, (t, d) in enumerate(items):
        tag = f' <span class="tag">{tags[n]}</span>' if tags and tags[n] else ""
        out += f"<li><h3>{t}{tag}</h3><p>{d}</p></li>"
    return out + "</ol>"


def principles():
    return '<div class="principles">' + "".join(
        f'<div class="principle"><h3>{t}</h3><p>{d}</p></div>' for t, d in PRINCIPLES
    ) + "</div>"


def stages(current=0):
    return '<div class="stages">' + "".join(
        f'<div class="stage{" current" if n == current else ""}"><span class="n">Stage {n+1}</span><h3>{t}</h3><p>{d}</p></div>'
        for n, (t, d) in enumerate(STAGES)
    ) + "</div>"


home = f"""{hero()}

<section class="section" aria-labelledby="why-now">
  <div class="container split">
    <div><p class="eyebrow">Why now</p><h2 id="why-now">Enterprise accountability needs a professional foundation.</h2></div>
    <div class="body">
      <p>Enterprise AI brings connected decisions about investment, operating models, technology, risk and people. Executives need to bring those decisions together and take responsibility for the outcomes.</p>
      <p>ICAIO is being established to help develop the shared standards, competencies and practices that this accountability requires.</p>
    </div>
  </div>
</section>

<section class="section surface" id="enterprise-ai-leadership" aria-labelledby="eal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Enterprise AI Leadership</p>
      <h2 id="eal">One discipline. Eight connected domains.</h2>
    </div>
    {domains_grid(f'<p>{INTEGRATION}</p><a class="text-link" href="enterprise-ai-leadership.html">Explore the eight domains</a>')}
  </div>
</section>

<section class="section" aria-labelledby="why-acaio">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Why ICAIO</p>
      <h2 id="why-acaio">A professional institution for enterprise AI leadership.</h2>
      <p class="lede">ICAIO's purpose is to professionalise the leadership of artificial intelligence in Australian organisations. Its proposed work has four priorities.</p>
    </div>
    {rows(MANDATES)}
    <p style="margin-top:32px"><a class="text-link" href="about.html">About ICAIO</a></p>
  </div>
</section>

<section class="section on-dark" aria-labelledby="council">
  <div class="container council">
    <div class="body">
      <p class="eyebrow">Founding Council</p>
      <h2 id="council" style="margin-bottom:28px">Help define an emerging profession.</h2>
      <p class="strong">ICAIO is bringing together a Founding Council of senior practitioners to help shape enterprise AI leadership in Australia.</p>
      <p>The proposed Council will help define the profession's accountabilities, competencies, Body of Knowledge and research priorities. Its work will inform the institution as it develops.</p>
      <p>We welcome expressions of interest from executives with enterprise AI accountability across Australian business, government and higher education.</p>
      <div class="notice">The Founding Council is distinct from the legal Board. An expression of interest does not confer Council membership or a director appointment.</div>
      <div class="actions">
        <a class="btn btn-light" href="{EOI}">Express interest in the Founding Council {ARROW}</a>
        <a class="btn btn-ghost" href="founding-council.html">Explore the proposed Council role</a>
      </div>
    </div>
    <aside class="council-aside" aria-label="What the Council may help define">
      <h3>The Council may help define</h3>
      <ul>
        <li>Enterprise AI Leadership</li>
        <li>The CAIO role and accountability framework</li>
        <li>A professional competency framework</li>
        <li>The Body of Knowledge</li>
        <li>Education and professional development requirements</li>
        <li>The research agenda and maturity model</li>
      </ul>
    </aside>
  </div>
</section>

<section class="section" aria-labelledby="agenda">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Initial professional agenda</p>
      <h2 id="agenda">Start with the foundations of professional practice.</h2>
      <p class="lede">The proposed initial agenda focuses on five outputs. Their scope and priorities will be shaped with founding participants.</p>
    </div>
    {rows(AGENDA5)}
    <p style="margin-top:32px"><a class="text-link" href="agenda.html">Explore the proposed agenda</a></p>
  </div>
</section>

<section class="section surface" aria-labelledby="independence">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Independence</p>
      <h2 id="independence">Professional credibility starts with independence.</h2>
      <p class="lede">ICAIO is being developed around six founding principles. The intended model keeps professional standards and research independent of vendor and sponsor control.</p>
    </div>
    {principles()}
  </div>
</section>

<section class="section on-dark closing" aria-labelledby="closing">
  <div class="container">
    <h2 id="closing">Help define the profession.</h2>
    <p class="lede">Bring your experience of enterprise AI accountability to the founding conversation.</p>
    <a class="btn btn-light" href="{EOI}">Express interest in the Founding Council {ARROW}</a>
    <div class="secondary">
      <p>For prospective members, researchers, education providers, partners and others interested in ICAIO's development.</p>
      <a class="btn btn-ghost" href="register-interest.html">Register interest in ICAIO</a>
    </div>
  </div>
</section>"""

page("index.html", "ICAIO | Enterprise AI Leadership in Australia",
     "ICAIO is being established for Australia's enterprise AI leaders. Explore the proposed professional agenda and express interest in the Founding Council.",
     home, current="index.html")


def page_hero(eyebrow, h1, lede):
    return f"""<section class="page-hero"><div class="container">
  <p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p>
</div></section>"""


SHELL_NOTE = '<div class="callout"><p><strong>Page shell.</strong> Structure and draft content drawn from the project context for review. Full page copy has not yet been written or approved.</p></div>'

# ---------- About ----------
about = page_hero("About ICAIO", "Professionalising the leadership of AI in Australian organisations.",
                  "ICAIO exists to develop the professional standards, capabilities, community, knowledge and practices required by executives responsible for AI strategy, transformation, governance, capability, adoption and value creation.") + f"""
<section class="section"><div class="container split">
  <div><p class="eyebrow">Positioning</p><h2>The professional body for Australia's enterprise AI leaders.</h2></div>
  <div class="prose">
    {SHELL_NOTE}
    <p>ICAIO represents an executive accountability, not only the job title Chief AI Officer. Leaders it is intended for include:</p>
    <ul>
      <li>Chief AI Officers</li>
      <li>Chief Data &amp; AI Officers</li>
      <li>Heads of Enterprise AI</li>
      <li>CIOs, CTOs or CDOs with enterprise AI accountability</li>
      <li>Chief Transformation Officers or equivalent executives with enterprise-wide AI responsibility</li>
    </ul>
  </div>
</div></section>

<section class="section surface"><div class="container split">
  <div><p class="eyebrow">Who is establishing ICAIO</p><h2>Transparent from the start.</h2></div>
  <div class="prose">
    <p>{ph('Founder name, current role and a short statement of why they are establishing ICAIO. To be supplied and approved.')}</p>
    <p>The founder is expected to serve as inaugural executive leader. Any remuneration will be transparent and approved by the Board.</p>
    <h2>Governance commitments</h2>
    <ul>
      <li>An independent Chair, separate from the Founder and executive leadership.</li>
      <li>A Board of approximately five to seven directors with formal governance duties.</li>
      <li>A Founding Council of senior practitioners, distinct from the legal Board.</li>
      <li>Sponsors and vendors do not control professional standards or research.</li>
      <li>Any transaction with a Founder-related entity is disclosed, independently approved on arm's-length terms, with the Founder excluded from the decision.</li>
      <li>Professional standards and frameworks belong to ICAIO.</li>
    </ul>
    <p>{ph('Legal structure, Chair and Board composition: to be confirmed.')}</p>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><p class="eyebrow">How ICAIO is being established</p><h2>Built in stages, with credibility first.</h2>
  <p class="lede">The establishment sequence puts practitioners, frameworks and evidence in place before a public launch.</p></div>
  {stages(0)}
</div></section>

<section class="section surface"><div class="container">
  <div class="section-head"><p class="eyebrow">Founding principles</p><h2>Professional credibility starts with independence.</h2></div>
  {principles()}
</div></section>"""
page("about.html", "About ICAIO | Institute of Chief AI Officers",
     "ICAIO is being established as an independent, not-for-profit professional institution for executives accountable for enterprise AI.", about)

# ---------- Enterprise AI Leadership ----------
eal = page_hero("Enterprise AI Leadership", "One discipline. Eight connected domains.",
                "Enterprise AI leadership integrates these disciplines to convert rapidly evolving AI capability into sustainable organisational performance.") + f"""
<section class="section surface"><div class="container">
  {domains_grid(f'<p>Eight domains, one discipline. Each will be refined with the Founding Council.</p><a class="text-link" href="{EOI}">Help define the discipline</a>')}
</div></section>
<section class="section"><div class="container split">
  <div><p class="eyebrow">Developing the model</p><h2>A discipline to be defined by practitioners.</h2></div>
  <div class="prose">
    {SHELL_NOTE}
    <h2>Why Ethical AI comes first</h2>
    <p>Ethical AI addresses the philosophical role of artificial intelligence as it relates to humanity and society, from today's systems through artificial general intelligence (AGI), artificial superintelligence (ASI) and quantum intelligence (QI).</p>
    <p>It asks organisations to actively define their position on the Gorilla problem: the question, framed by computer scientist Stuart Russell, of how humanity retains control of its future if it creates intelligence greater than its own, much as the gorilla's future now depends on humans.</p>
    <h2>Developing the model</h2>
    <p>The eight domains provide a starting structure. The Founding Council is expected to refine how each domain is described, how they connect, and what competence looks like in each.</p>
    <p>{ph('Per-domain detail: accountabilities, typical decisions, and links to the proposed competency framework. To be developed with the Council.')}</p>
    <p><a class="text-link" href="{EOI}">Help define the discipline</a></p>
  </div>
</div></section>"""
page("enterprise-ai-leadership.html", "Enterprise AI Leadership | ICAIO",
     "The eight domains of enterprise AI leadership: Ethical AI, Governance, Strategy, Transformation, Value, Capability, Adoption and Operating AI.", eal)

# ---------- Founding Council ----------
fc = page_hero("Founding Council", "Help define the emerging profession of enterprise AI leadership in Australia.",
               "ICAIO is assembling a Founding Council of senior practitioners to help establish the profession, rather than endorse an organisation that is already fully designed.") + f"""
<section class="section"><div class="container split">
  <div><p class="eyebrow">The role</p><h2>What the Council may help define.</h2></div>
  <div class="prose">
    {SHELL_NOTE}
    <ul>
      <li>Enterprise AI Leadership and the CAIO role and accountability framework</li>
      <li>A professional competency framework and Body of Knowledge</li>
      <li>Education and professional development requirements</li>
      <li>Designation requirements, if later adopted</li>
      <li>The research agenda and an enterprise AI maturity model</li>
      <li>Governance, accountability, value and performance frameworks</li>
    </ul>
  </div>
</div></section>

<section class="section surface"><div class="container split">
  <div><p class="eyebrow">What to expect</p><h2>A clear, proportionate commitment.</h2></div>
  <div class="prose">
    <ul>
      <li><strong>Size and mix.</strong> Approximately 12 to 20 senior practitioners drawn deliberately across sectors, including financial services, government, healthcare, telecommunications, retail, resources, professional services, technology and higher education.</li>
      <li><strong>Time commitment.</strong> {ph('Format, frequency and expected hours to be confirmed')}</li>
      <li><strong>Personal capacity.</strong> Members take part in a personal capacity and do not represent their employers unless explicitly approved.</li>
      <li><strong>Not a Board seat.</strong> Council membership does not make a person a legal director.</li>
      <li><strong>Remuneration.</strong> {ph('Position to be confirmed')}</li>
      <li><strong>Selection.</strong> {ph('Selection approach and criteria to be confirmed')}</li>
      <li><strong>Next steps.</strong> {ph('What happens after an expression of interest, and response timing')}</li>
    </ul>
    <div class="callout"><p><strong>Founding Council prospectus</strong> {ph('PDF in preparation')}<br><span class="muted">A one-page summary to share with colleagues and employers.</span></p></div>
    <p><a class="btn btn-primary" href="{EOI}">Express interest in the Founding Council {ARROW}</a></p>
  </div>
</div></section>"""
page("founding-council.html", "Founding Council | ICAIO",
     "ICAIO is assembling a Founding Council of senior practitioners to help define enterprise AI leadership in Australia.", fc)

# ---------- Agenda ----------
ALL12 = [
    ("ICAIO Professional Charter", "Initial"), ("Enterprise AI Leadership definition", ""),
    ("CAIO Role &amp; Accountability Framework", ""), ("CAIO Competency Framework", "Initial"),
    ("Enterprise AI Maturity Model", "Initial"), ("AI Leadership &amp; Accountability Framework", "Initial"),
    ("AI Investment, Value &amp; Performance Framework", ""), ("Agentic AI Governance Framework", ""),
    ("AI Workforce &amp; Adoption Framework", ""), ("CAIO, CIO, CTO, CDO and CRO decision-rights model", ""),
    ("State of Enterprise AI Leadership in Australia", "Initial"), ("ICAIO Body of Knowledge", ""),
]
agenda = page_hero("Proposed agenda", "Start with the foundations of professional practice.",
                   "The proposed initial agenda focuses on five outputs. Their scope and priorities will be shaped with founding participants.") + f"""
<section class="section"><div class="container">
  <div class="section-head"><p class="eyebrow">Initial outputs</p><h2>Five proposed starting points.</h2></div>
  {rows(AGENDA5)}
</div></section>
<section class="section surface"><div class="container split">
  <div><p class="eyebrow">The wider programme</p><h2>Potential first-wave professional knowledge.</h2></div>
  <div class="prose">
    {SHELL_NOTE}
    <p>All items are proposed. None has been published.</p>
    <ol class="rows" style="margin-top:24px">{''.join(f'<li><h3 style="font-size:1.1rem">{t}{f" <span class=tag>{g}</span>" if g else ""}</h3><p></p></li>' for t, g in ALL12)}</ol>
  </div>
</div></section>"""
page("agenda.html", "Proposed agenda | ICAIO",
     "The proposed initial professional agenda for enterprise AI leadership in Australia.", agenda)

# ---------- Get involved ----------
sectors = ["Financial services", "Government", "Healthcare", "Telecommunications", "Retail", "Resources",
           "Professional services", "Technology", "Higher education", "Other"]
domain_checks = "".join(
    f'<label class="check"><input type="checkbox" name="domains" value="{t}"> {t}</label>' for t, _ in DOMAINS)
sector_opts = "".join(f"<option>{s}</option>" for s in sectors)
COUNCIL_FORM = f"""  <form class="form" id="council-form" data-prototype novalidate>
    <fieldset>
      <legend>Your details</legend>
      <p class="muted">An expression of interest does not confer Council membership or a director appointment. We will be in touch about next steps. {ph('response timing')}</p>
      <div class="two">
        <div class="field"><label for="n">Full name</label><input id="n" name="name" autocomplete="name" required></div>
        <div class="field"><label for="e">Work email</label><input id="e" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="two">
        <div class="field"><label for="r">Role title</label><input id="r" name="role" autocomplete="organization-title" required></div>
        <div class="field"><label for="o">Organisation</label><input id="o" name="org" autocomplete="organization" required></div>
      </div>
      <div class="field"><label for="s">Sector</label><select id="s" name="sector" required><option value="">Select a sector</option>{sector_opts}</select></div>
      <div class="field"><label for="scope">Scope of your enterprise AI accountability</label><span class="hint" id="scope-hint">For example: enterprise-wide strategy, governance, a portfolio of programs, or team size.</span><textarea id="scope" name="scope" aria-describedby="scope-hint" required></textarea></div>
      <div class="field"><span class="label" id="dom-l">Domains where you could contribute most</span><div class="checks" role="group" aria-labelledby="dom-l">{domain_checks}</div></div>
      <div class="field"><label for="li">LinkedIn profile (optional)</label><input id="li" name="linkedin" type="url" placeholder="https://"></div>
      <input class="hp" type="text" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <label class="check"><input type="checkbox" required> <span>I understand that I would take part in a personal capacity and not as a representative of my employer.</span></label>
      <label class="check"><input type="checkbox" required> <span>I agree to ICAIO storing these details to consider my expression of interest, as described in the privacy policy {ph('to come')}. My details will not be shared with third parties without my consent.</span></label>
      <div class="form-status" tabindex="-1" role="status"><strong>Prototype only.</strong> This form is not connected and nothing was sent.</div>
      <div><button class="btn btn-primary" type="submit">Submit expression of interest {ARROW}</button></div>
    </fieldset>
  </form>"""
GENERAL_FORM = f"""  <form class="form" id="general-form" data-prototype novalidate>
    <fieldset>
      <legend>Your details</legend>
      <div class="two">
        <div class="field"><label for="gn">Full name</label><input id="gn" autocomplete="name" required></div>
        <div class="field"><label for="ge">Email</label><input id="ge" type="email" autocomplete="email" required></div>
      </div>
      <div class="field"><label for="gt">I am interested as a</label><select id="gt" required><option value="">Select one</option><option>Prospective member</option><option>Researcher</option><option>Education provider</option><option>Prospective partner</option><option>Other</option></select></div>
      <div class="field"><label for="gm">Message (optional)</label><textarea id="gm"></textarea></div>
      <label class="check"><input type="checkbox" required> <span>I agree to ICAIO storing these details to contact me about its development. {ph('privacy policy to come')}</span></label>
      <div class="form-status" tabindex="-1" role="status"><strong>Prototype only.</strong> This form is not connected and nothing was sent.</div>
      <div><button class="btn btn-ghost" type="submit">Register interest</button></div>
    </fieldset>
  </form>"""

eoi_body = page_hero("Founding Council", "Express interest in the Founding Council.",
                     "Help define the emerging profession of enterprise AI leadership in Australia. Tell us about your role and where you could contribute.") + f"""
<section class="section"><div class="container">
  {COUNCIL_FORM}
  <p style="margin-top:48px" class="muted">Not applying for the Council? <a class="text-link" href="register-interest.html">Register interest in ICAIO</a></p>
</div></section>"""
page("express-interest.html", "Founding Council expression of interest | ICAIO",
     "Express interest in the ICAIO Founding Council.", eoi_body, current="founding-council.html")

reg_body = page_hero("Register interest", "Register interest in ICAIO.",
                     "For prospective members, researchers, education providers, partners and others interested in ICAIO's development.") + f"""
<section class="section"><div class="container">
  {GENERAL_FORM}
  <p style="margin-top:48px" class="muted">Senior executive with enterprise AI accountability? <a class="text-link" href="{EOI}">Express interest in the Founding Council</a></p>
</div></section>"""
page("register-interest.html", "Register interest | ICAIO",
     "Register interest in the Institute of Chief AI Officers.", reg_body)

gi = page_hero("Get involved", "Join the founding conversation.",
               "Choose the option that fits you.") + f"""
<section class="section"><div class="container">
  <div class="choices">
    <a class="choice" href="{EOI}"><span class="eyebrow">For senior executives</span><h2>Founding Council expression of interest</h2><p>For executives accountable for enterprise AI who want to help define the profession.</p><span class="text-link">Express interest</span></a>
    <a class="choice" href="register-interest.html"><span class="eyebrow">For everyone else</span><h2>Register interest in ICAIO</h2><p>For prospective members, researchers, education providers, partners and others.</p><span class="text-link">Register interest</span></a>
  </div>
</div></section>"""
page("get-involved.html", "Get involved | ICAIO",
     "Express interest in the ICAIO Founding Council or register interest in ICAIO.", gi)

# ---------- Founding Council members (future state, SAMPLE DATA ONLY) ----------
# Every person below is fictional placeholder content. Replace with approved, consented profiles.
MEMBERS = [
    # (first, surname, council title, job title, organisation, tags, statement)
    ("Jane", "Doe", "Founding Council Chair", "Chief AI Officer", "Major defence technology company",
     ["Cyber security", "Defence technology", "Governance"],
     "Jane Doe brings extensive experience in the application of AI in the domains of Cyber Security and Defence Technologies."),
    ("John", "Smith", "Founding Council Member", "Chief Data &amp; AI Officer", "National logistics group",
     ["Robotics", "Logistics", "Operating AI"],
     "John Smith brings significant expertise in the application of AI in robotics and logistics management."),
    ("Jan", "Citizen", "Deputy Chair", "Head of Enterprise AI", "Commonwealth government agency",
     ["Public sector", "Ethical AI", "Policy"],
     "Jan Citizen brings deep experience in the responsible use of AI in public administration and citizen services."),
    ("Sam", "Sample", "Founding Council Member", "Chief AI Officer", "Major Australian bank",
     ["Financial services", "Risk", "Value"],
     "Sam Sample brings extensive experience in scaling AI across lending, fraud detection and customer operations."),
    ("Alex", "Example", "Founding Council Member", "Chief Information Officer", "Metropolitan health service",
     ["Healthcare", "Clinical AI", "Adoption"],
     "Alex Example brings significant expertise in the safe adoption of AI in clinical and hospital settings."),
    ("Pat", "Specimen", "Founding Council Member", "Chief Technology Officer", "National telecommunications provider",
     ["Telecommunications", "Networks", "Capability"],
     "Pat Specimen brings extensive experience in applying AI to network operations and customer experience."),
    ("Chris", "Template", "Founding Council Member", "Chief Transformation Officer", "National retail group",
     ["Retail", "Transformation", "Customer"],
     "Chris Template brings significant expertise in AI-enabled transformation of retail and supply operations."),
    ("Morgan", "Draft", "Founding Council Member", "Head of AI", "Global resources company",
     ["Resources", "Autonomous operations", "Safety"],
     "Morgan Draft brings extensive experience in autonomous and predictive AI across mining operations."),
    ("Taylor", "Model", "Founding Council Member", "Pro Vice-Chancellor, Digital", "Research-intensive university",
     ["Higher education", "Research", "Skills"],
     "Taylor Model brings significant expertise in AI research translation and workforce capability."),
    ("Robin", "Prototype", "Founding Council Member", "Partner, AI &amp; Data", "Professional services firm",
     ["Professional services", "Strategy", "Assurance"],
     "Robin Prototype brings extensive experience advising boards on AI strategy and assurance."),
    ("Jamie", "Mock", "Founding Council Member", "Chief AI Officer", "Australian technology company",
     ["Technology", "Agentic AI", "Platforms"],
     "Jamie Mock brings significant expertise in building and operating agentic AI platforms at scale."),
    ("Casey", "Demo", "Founding Council Member", "Chief Digital Officer", "Energy and utilities group",
     ["Energy", "Infrastructure", "Governance"],
     "Casey Demo brings extensive experience in applying AI to critical infrastructure and the energy transition."),
]

HEADSHOT = ('<svg viewBox="0 0 160 200" role="img" aria-label="Headshot placeholder" class="headshot-svg">'
            '<rect width="160" height="200" fill="#DCE3DF"/>'
            '<circle cx="80" cy="78" r="34" fill="#B5C3BF"/>'
            '<path d="M18 200c4-46 30-70 62-70s58 24 62 70z" fill="#B5C3BF"/></svg>')


def member_slug(first, last):
    return f"{first}-{last}".lower()


def member_card(m):
    first, last, ctitle, job, org, tags, statement = m
    slug = member_slug(first, last)
    tag_html = "".join(f"<li>{t}</li>" for t in tags)
    return f"""<article class="member">
  <a class="headshot" href="council-{slug}.html" tabindex="-1" aria-hidden="true">{HEADSHOT}</a>
  <div class="member-body">
    <h3 class="member-name"><a href="council-{slug}.html">{first} <span class="surname">{last}</span></a></h3>
    <p class="member-council">{ctitle}</p>
    <p class="member-role">{job}<br><span>{org}</span></p>
    <ul class="member-tags" aria-label="Expertise">{tag_html}</ul>
    <p class="member-statement">{statement}</p>
    <div class="member-links">
      <a class="text-link" href="council-{slug}.html">Full profile</a>
      <a href="#" class="member-ext" aria-disabled="true">LinkedIn {ph('link')}</a>
    </div>
  </div>
</article>"""


def mini_card(m):
    first, last, ctitle, job, org, tags, statement = m
    slug = member_slug(first, last)
    return f"""<li class="mini">
  <a href="council-{slug}.html">
    <span class="headshot">{HEADSHOT}</span>
    <span class="mini-name">{first} {last}</span>
    <span class="member-council">{ctitle}</span>
    <span class="mini-role">{job}<br>{org}</span>
  </a>
</li>"""


members_sorted = sorted(MEMBERS, key=lambda m: (m[1].lower(), m[0].lower()))
council_members = f"""<div class="sample-bar" role="note"><strong>Future-state sample.</strong> The Founding Council has not been appointed. Every name, role, organisation and statement on this page is fictional placeholder content.</div>
""" + page_hero("Founding Council", "The Founding Council.",
               "Senior practitioners from across Australian business, government and higher education, helping define the emerging profession of enterprise AI leadership. Members take part in a personal capacity.") + f"""
<section class="section"><div class="container">
  <div class="members">{''.join(member_card(m) for m in members_sorted)}</div>
  <div class="callout" style="margin-top:56px"><p>The Founding Council is distinct from the legal Board. Council members do not represent their employers unless explicitly approved.</p></div>
</div></section>"""
page("council-members.html", "Founding Council members | ICAIO",
     "Members of the ICAIO Founding Council.", council_members, current="founding-council.html")

SAMPLE_BAR = '<div class="sample-bar" role="note"><strong>Future-state sample.</strong> The Founding Council has not been appointed. This profile is fictional placeholder content.</div>'

for m in members_sorted:
    first, last, ctitle, job, org, tags, statement = m
    slug = member_slug(first, last)
    tag_html = "".join(f"<li>{t}</li>" for t in tags)
    others = "".join(mini_card(o) for o in members_sorted if o is not m)
    body = f"""{SAMPLE_BAR}
<section class="profile-page"><div class="container">
  <p class="back"><a href="council-members.html">&larr; All Council members</a></p>
  <div class="profile-layout">
    <div class="headshot">{HEADSHOT}</div>
    <div class="profile-main">
      <p class="eyebrow">{ctitle}</p>
      <h1>{first} {last}</h1>
      <p class="profile-role">{job}, {org}</p>
      <ul class="member-tags" aria-label="Expertise">{tag_html}</ul>
      <p class="profile-statement">{statement}</p>
      <h2>AI for good</h2>
      <p>{ph(f"{first} {last}'s personal statement on AI for good, written and approved by the member")}</p>
      <h2>Background</h2>
      <p>{ph('Career summary, board and advisory roles, and publications')}</p>
      <h2>Contribution to the Founding Council</h2>
      <p>{ph('Domains and working groups the member contributes to')}</p>
      <p class="actions"><a class="btn btn-primary btn-sm" href="#" aria-disabled="true">LinkedIn profile</a>
      <a class="btn btn-ghost btn-sm" href="#" aria-disabled="true">Corporate executive profile</a></p>
    </div>
  </div>
</div></section>
<section class="section surface others"><div class="container">
  <div class="others-head">
    <h2 id="others-h">Other Council members</h2>
    <div class="scroll-btns"><button type="button" class="scroll-btn" data-scroll="-1" aria-label="Scroll to previous members">&larr;</button><button type="button" class="scroll-btn" data-scroll="1" aria-label="Scroll to more members">&rarr;</button></div>
  </div>
  <ul class="scroller" role="list" tabindex="0" aria-labelledby="others-h">{others}</ul>
</div></section>"""
    page(f"council-{slug}.html", f"{first} {last} | Founding Council | ICAIO", f"{first} {last}, {ctitle}, ICAIO Founding Council.", body, current="founding-council.html")


print("built", sorted(p.name for p in OUT.glob("*.html")))
