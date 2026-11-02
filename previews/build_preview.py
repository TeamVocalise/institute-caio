"""Build the private homepage wireframe from its reviewed Markdown copy."""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parent.parent
source = (ROOT / 'docs/content/P001-home.md').read_text()
copy = source.split('## Public copy begins')[1].split('## Public copy ends')[0]
parts = re.split(r'\n### \d+\. [^\n]+\n', copy)[1:]
ids = ['home', 'why-now', 'enterprise-ai-leadership', 'domains', 'about', 'founding-council', 'agenda', 'independence', 'get-involved']

def inline(text):
    return html.escape(text).replace('&lt;br&gt;', '<br>')

def render(part):
    blocks = []
    for raw in part.strip().split('\n\n'):
        raw = raw.strip()
        if raw.startswith('Anchor:'):
            continue
        if raw.startswith('Institutional line:'):
            blocks.append('<p class="institution">' + inline(raw.split(': ', 1)[1]) + '</p>')
        elif raw.startswith(('Primary CTA:', 'Secondary CTA:', 'Text link:')):
            match = re.search(r'\*\*(.*?)\*\* → `(.*?)`', raw)
            label, dest = match.groups()
            primary = raw.startswith('Primary')
            attrs = '' if dest.startswith('#') else ' data-destination="' + html.escape(dest) + '"'
            href = dest if dest.startswith('#') else '#preview-destination'
            blocks.append(f'<a class="{"button" if primary else "text-link"}" href="{href}"{attrs}>{inline(label)}</a>')
        elif raw.startswith('# '):
            blocks.append('<h1>' + inline(raw[2:]) + '</h1>')
        elif raw.startswith('## '):
            blocks.append('<h2>' + inline(raw[3:]) + '</h2>')
        elif raw.startswith('#### '):
            blocks.append('<h3>' + inline(raw[5:]) + '</h3>')
        else:
            blocks.append('<p>' + inline(raw) + '</p>')
    return '\n'.join(blocks)

sections = []
for i, (part, ident) in enumerate(zip(parts, ids)):
    body = render(part)
    if ident == 'domains':
        link_at = body.rfind('<a ')
        tail, body = body[link_at:], body[:link_at]
        groups = re.findall(r'(<h3>.*?</h3>\s*<p>.*?</p>)', body, re.S)
        body = '<div class="domain-grid">' + ''.join('<div class="domain">' + group + '</div>' for group in groups) + '</div>' + tail
        sections[-1] = sections[-1].replace('</div></section>', body + '</div></section>')
        continue
    if ident in ('about', 'agenda', 'independence'):
        first = body.index('<h3>')
        link_at = body.rfind('<a ')
        end = link_at if link_at > first else len(body)
        groups = re.findall(r'(<h3>.*?</h3>\s*<p>.*?</p>)', body[first:end], re.S)
        name = {'about': 'mandates', 'agenda': 'agenda-list', 'independence': 'principles'}[ident]
        body = body[:first] + '<div class="' + name + '">' + ''.join('<div>' + group + '</div>' for group in groups) + '</div>' + body[end:]
    sections.append(f'<section id="{ident}" aria-labelledby="heading-{ident}"><div class="container">{body}</div></section>'.replace('<h2>', f'<h2 id="heading-{ident}">', 1).replace('<h1>', f'<h1 id="heading-{ident}">', 1))

css = (ROOT / 'previews/homepage.css').read_text()
output = '''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>ACAIO | Homepage wireframe for review</title><style>''' + css + '''</style></head>
<body><a class="skip" href="#main">Skip to content</a>
<aside class="review-note" aria-label="Preview status"><span><strong>Homepage wireframe</strong> · Draft copy for review · 12 October 2026</span><button type="button" aria-label="Dismiss preview note" onclick="this.parentElement.hidden=true">Dismiss</button></aside>
<header><div class="header-inner"><a class="wordmark" href="#home" aria-label="ACAIO home">ACAIO<span>Australia</span></a><nav class="desktop-nav" aria-label="Main navigation"><a href="#enterprise-ai-leadership">Enterprise AI Leadership</a><a href="#founding-council">Founding Council</a><a href="#agenda">Our Agenda</a><a href="#about">About ACAIO</a></nav><a class="header-cta" href="#preview-destination" data-destination="/get-involved?interest=founding-council" aria-label="Express interest in the Founding Council">Express interest</a><details class="mobile-menu"><summary>Menu</summary><nav aria-label="Mobile navigation"><a href="#enterprise-ai-leadership">Enterprise AI Leadership</a><a href="#founding-council">Founding Council</a><a href="#agenda">Our Agenda</a><a href="#about">About ACAIO</a></nav></details></div></header>
<main id="main">''' + '\n'.join(sections) + '''</main>
<aside id="preview-destination" class="destination" hidden tabindex="-1" aria-labelledby="destination-heading"><div class="container"><h2 id="destination-heading">Planned destination</h2><p id="destination-label"></p><p>This is a homepage review wireframe. The linked page and expression-of-interest form will be developed after the homepage is approved. No information is collected here.</p><button id="back-to-copy" type="button">Return to the homepage</button></div></aside>
<footer><div class="container"><div><a class="wordmark" href="#home">ACAIO</a><p>Association of Chief AI Officers Australia</p><p>Being established for Australia's enterprise AI leaders.</p></div><nav aria-label="Footer navigation"><a href="#independence">Founding principles</a><a href="#get-involved">Get involved</a><a href="#home">Back to top</a></nav></div></footer>
<script>
let originLink;
const destination = document.getElementById('preview-destination');
document.querySelectorAll('[data-destination]').forEach(link => link.addEventListener('click', event => {
 event.preventDefault(); originLink = link; destination.hidden = false;
 document.getElementById('destination-label').textContent = link.textContent.trim() + ' → ' + link.dataset.destination;
 destination.scrollIntoView({block:'center'}); destination.focus({preventScroll:true});
}));
document.getElementById('back-to-copy').addEventListener('click', () => {destination.hidden = true; if(originLink) originLink.focus();});
document.querySelectorAll('.mobile-menu a').forEach(link => link.addEventListener('click', () => {document.querySelector('.mobile-menu').open=false;}));
</script></body></html>'''
(ROOT / 'previews/homepage.html').write_text(output)
print('Built previews/homepage.html from docs/content/P001-home.md')
