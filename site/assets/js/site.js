// ACAIO draft site: hero rotation and prototype form handling.
(function () {
  // Hero rotation
  var hero = document.querySelector('[data-hero]');
  if (hero) {
    var slides = Array.prototype.slice.call(hero.querySelectorAll('.hero-slide'));
    var dots = Array.prototype.slice.call(hero.querySelectorAll('.hero-dots button'));
    var cityLabel = hero.querySelector('.hero-city');
    var pauseBtn = hero.querySelector('.hero-pause');
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var i = 0, timer = null, playing = !reduce, INTERVAL = 7000;

    // Fallback to the hosted source image if the local file is missing.
    slides.forEach(function (s) {
      var img = s.querySelector('img');
      img.addEventListener('error', function () {
        var fb = img.getAttribute('data-fallback');
        if (fb && img.src.indexOf(fb) === -1) img.src = fb;
      });
    });

    function show(n) {
      slides[i].classList.remove('is-active');
      dots[i] && dots[i].setAttribute('aria-current', 'false');
      i = (n + slides.length) % slides.length;
      var img = slides[i].querySelector('img');
      if (img.loading === 'lazy') img.loading = 'eager';
      slides[i].classList.add('is-active');
      dots[i] && dots[i].setAttribute('aria-current', 'true');
      if (cityLabel) cityLabel.textContent = slides[i].getAttribute('data-city');
    }
    function start() { stop(); timer = setInterval(function () { show(i + 1); }, INTERVAL); playing = true; label(); }
    function stop() { if (timer) clearInterval(timer); timer = null; }
    function label() { if (pauseBtn) pauseBtn.textContent = playing ? 'Pause' : 'Play'; pauseBtn && pauseBtn.setAttribute('aria-pressed', String(!playing)); }

    dots.forEach(function (d, n) { d.addEventListener('click', function () { show(n); if (playing) start(); }); });
    if (pauseBtn) pauseBtn.addEventListener('click', function () { if (playing) { stop(); playing = false; label(); } else { start(); } });
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else if (playing) start(); });

    // Preload the next images after first paint.
    window.addEventListener('load', function () { slides.forEach(function (s) { var im = s.querySelector('img'); im.loading = 'eager'; }); });
    if (playing) start(); else label();
  }

  // Prototype forms: validate, never send.
  Array.prototype.slice.call(document.querySelectorAll('form[data-prototype]')).forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var status = form.querySelector('.form-status');
      status.classList.add('show');
      status.focus();
    });
  });
  // Disabled placeholder links
  document.addEventListener('click', function (e) {
    var dis = e.target.closest('a[aria-disabled="true"]'); if (dis) e.preventDefault();
  });

  // Horizontal member scroller
  Array.prototype.slice.call(document.querySelectorAll('[data-scroll]')).forEach(function (btn) {
    btn.addEventListener('click', function () {
      var sc = btn.closest('.container').querySelector('.scroller');
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      sc.scrollBy({ left: Number(btn.getAttribute('data-scroll')) * sc.clientWidth * 0.8, behavior: reduce ? 'auto' : 'smooth' });
    });
  });
})();
