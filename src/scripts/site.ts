// Hero rotation, prototype forms, placeholder links and the member scroller.
function initHero(): void {
  const hero = document.querySelector<HTMLElement>('[data-hero]');
  if (!hero) return;
  const slides = Array.from(hero.querySelectorAll<HTMLElement>('.hero-slide'));
  const dots = Array.from(hero.querySelectorAll<HTMLButtonElement>('.hero-dots button'));
  const cityLabel = hero.querySelector<HTMLElement>('.hero-city');
  const pauseBtn = hero.querySelector<HTMLButtonElement>('.hero-pause');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const INTERVAL = 7000;
  let i = 0;
  let timer: number | undefined;
  let playing = !reduce;

  const show = (n: number) => {
    slides[i].classList.remove('is-active');
    dots[i]?.setAttribute('aria-current', 'false');
    i = (n + slides.length) % slides.length;
    const img = slides[i].querySelector('img');
    if (img && img.loading === 'lazy') img.loading = 'eager';
    slides[i].classList.add('is-active');
    dots[i]?.setAttribute('aria-current', 'true');
    if (cityLabel) cityLabel.textContent = slides[i].dataset.city ?? '';
  };
  const stop = () => { if (timer) window.clearInterval(timer); timer = undefined; };
  const label = () => {
    if (!pauseBtn) return;
    pauseBtn.textContent = playing ? 'Pause' : 'Play';
    pauseBtn.setAttribute('aria-pressed', String(!playing));
  };
  const start = () => { stop(); timer = window.setInterval(() => show(i + 1), INTERVAL); playing = true; label(); };

  dots.forEach((d, n) => d.addEventListener('click', () => { show(n); if (playing) start(); }));
  pauseBtn?.addEventListener('click', () => { if (playing) { stop(); playing = false; label(); } else { start(); } });
  document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); else if (playing) start(); });
  window.addEventListener('load', () => slides.forEach((s) => { const im = s.querySelector('img'); if (im) im.loading = 'eager'; }));
  if (playing) start(); else label();
}

function initForms(): void {
  document.querySelectorAll<HTMLFormElement>('form[data-prototype]').forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      const status = form.querySelector<HTMLElement>('.form-status');
      status?.classList.add('show');
      status?.focus();
    });
  });
}

function initPlaceholderLinks(): void {
  document.addEventListener('click', (e) => {
    const target = e.target as Element | null;
    if (target?.closest('a[aria-disabled="true"]')) e.preventDefault();
  });
}

function initScrollers(): void {
  document.querySelectorAll<HTMLButtonElement>('[data-scroll]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const sc = btn.closest('.container')?.querySelector<HTMLElement>('.scroller');
      if (!sc) return;
      const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      sc.scrollBy({ left: Number(btn.dataset.scroll) * sc.clientWidth * 0.8, behavior: reduce ? 'auto' : 'smooth' });
    });
  });
}

function initDirectory(): void {
  const table = document.querySelector<HTMLTableElement>('[data-dir-table]');
  if (!table) return;
  const tbody = table.tBodies[0];
  const rows = Array.from(tbody.rows);
  const search = document.querySelector<HTMLInputElement>('[data-dir-search]');
  const filters = Array.from(document.querySelectorAll<HTMLSelectElement>('[data-dir-filter]'));
  const count = document.querySelector<HTMLElement>('[data-dir-count]');
  const apply = () => {
    const q = (search?.value ?? '').trim().toLowerCase();
    let shown = 0;
    rows.forEach((r) => {
      const matchQ = !q || (r.textContent ?? '').toLowerCase().includes(q);
      const matchF = filters.every((f) => !f.value || r.dataset[f.dataset.dirFilter as string] === f.value);
      r.hidden = !(matchQ && matchF);
      if (!r.hidden) shown++;
    });
    if (count) count.textContent = `${shown} member${shown === 1 ? '' : 's'}`;
  };
  search?.addEventListener('input', apply);
  filters.forEach((f) => f.addEventListener('change', apply));
  table.querySelectorAll<HTMLButtonElement>('[data-sort]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const col = Number(btn.dataset.sort);
      const asc = btn.getAttribute('aria-sort') !== 'ascending';
      table.querySelectorAll('[data-sort]').forEach((b) => b.removeAttribute('aria-sort'));
      btn.setAttribute('aria-sort', asc ? 'ascending' : 'descending');
      const val = (r: HTMLTableRowElement) => r.cells[col].dataset.sortValue ?? r.cells[col].textContent ?? '';
      rows.sort((a, b) => (asc ? 1 : -1) * val(a).localeCompare(val(b), 'en-AU'));
      rows.forEach((r) => tbody.appendChild(r));
    });
  });
}

initDirectory();
initHero();
initForms();
initPlaceholderLinks();
initScrollers();
