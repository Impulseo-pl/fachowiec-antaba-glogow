/* Antaba – ruch strony. Każdy blok w try/catch, żeby jeden błąd nie zatrzymał reszty. */
(function () {
  var d = document.documentElement;

  var RM = false;
  try { RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { }
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var desktop = function () { return window.matchMedia('(min-width: 821px)').matches; };

  /* płynne przewijanie (tylko mysz) */
  var lenis = null;
  try {
    if (!RM && window.Lenis && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      lenis = new window.Lenis({ lerp: 0.085, smoothWheel: true });
      var raf = function (t) { lenis.raf(t); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
      if (d.classList.contains('intro-on')) lenis.stop();
    }
  } catch (e) { lenis = null; }

  /* jedna pętla dla efektów zależnych od przewinięcia */
  var naScroll = [], tik = false;
  var przelicz = function () { tik = false; for (var i = 0; i < naScroll.length; i++) { try { naScroll[i](); } catch (e) { } } };
  var zglos = function () { if (!tik) { tik = true; requestAnimationFrame(przelicz); } };
  window.addEventListener('scroll', zglos, { passive: true });
  window.addEventListener('resize', zglos, { passive: true });

  /* start: intro (raz na sesję) albo zjazd kurtyny po przejściu z innej podstrony */
  var heroGo = function () { requestAnimationFrame(function () { requestAnimationFrame(function () { d.classList.add('hero-go'); }); }); };
  var kurtyna = $('.kurtyna');
  try {
    var przyszedl = false;
    try { przyszedl = sessionStorage.getItem('an_kurtyna') === '1'; sessionStorage.removeItem('an_kurtyna'); } catch (e) { }
    if (d.classList.contains('intro-on')) {
      try { sessionStorage.setItem('an_intro', '1'); } catch (e) { }
      requestAnimationFrame(function () { requestAnimationFrame(function () { d.classList.add('intro-gra'); }); });
      var koniec = function () {
        if (!d.classList.contains('intro-on') || d.classList.contains('intro-out')) return;
        d.classList.add('intro-out');
        setTimeout(heroGo, 250);
        setTimeout(function () { d.classList.remove('intro-on', 'intro-gra', 'intro-out'); if (lenis) lenis.start(); }, 950);
      };
      setTimeout(koniec, RM ? 50 : 2100);
      $('.intro') && $('.intro').addEventListener('click', koniec);
    } else if (przyszedl && kurtyna && !RM) {
      kurtyna.classList.add('zasunieta');
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          kurtyna.classList.remove('zasunieta'); kurtyna.classList.add('otwiera');
          setTimeout(heroGo, 200);
          setTimeout(function () { kurtyna.classList.remove('otwiera'); }, 800);
        });
      });
    } else { heroGo(); }
  } catch (e) { d.classList.remove('intro-on'); heroGo(); }

  /* kurtyna przy wyjściu na inną podstronę */
  try {
    document.addEventListener('click', function (ev) {
      var a = ev.target.closest && ev.target.closest('a');
      if (!a || RM || !kurtyna) return;
      if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey || ev.button) return;
      var href = a.getAttribute('href') || '';
      if (a.target === '_blank' || /^(tel:|mailto:|#|https?:)/.test(href)) return;
      var u = new URL(a.href, location.href);
      if (u.origin !== location.origin) return;
      if (u.pathname === location.pathname) return;
      ev.preventDefault();
      try { sessionStorage.setItem('an_kurtyna', '1'); } catch (e) { }
      kurtyna.classList.remove('otwiera'); kurtyna.classList.add('zamyka');
      setTimeout(function () { location.href = a.href; }, 620);
    });
    window.addEventListener('pageshow', function (e) { if (e.persisted && kurtyna) kurtyna.className = 'kurtyna'; });
  } catch (e) { }

  /* nagłówek: tło po zjechaniu, chowanie przy przewijaniu w dół */
  try {
    var top = $('.top'), ostatni = 0;
    naScroll.push(function () {
      var y = window.scrollY;
      top.classList.toggle('solid', y > 40);
      top.classList.toggle('ukryj', y > 500 && y > ostatni && !document.body.classList.contains('menu-on'));
      ostatni = y;
      var k = $('.kom-cta'); if (k) k.classList.toggle('on', y > 500);
    });
  } catch (e) { }

  /* menu mobilne */
  try {
    var b = $('.burger');
    b && b.addEventListener('click', function () {
      var on = !document.body.classList.contains('menu-on');
      document.body.classList.toggle('menu-on', on); d.classList.toggle('menu-on', on);
      b.setAttribute('aria-expanded', on ? 'true' : 'false');
      if (lenis) on ? lenis.stop() : lenis.start();
    });
  } catch (e) { }

  /* odsłanianie przy przewijaniu */
  try {
    var cele = $$('[data-r], .odslon, .ln-wrap');
    if ('IntersectionObserver' in window && !RM) {
      var io = new IntersectionObserver(function (wpisy) {
        wpisy.forEach(function (w) { if (w.isIntersecting) { w.target.classList.add('in'); io.unobserve(w.target); } });
      }, { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });
      cele.forEach(function (el) { io.observe(el); });
    } else { cele.forEach(function (el) { el.classList.add('in'); }); }
  } catch (e) { $$('[data-r], .odslon, .ln-wrap').forEach(function (el) { el.classList.add('in'); }); }

  /* hero: lekka paralaksa zdjęć za skrzydłami */
  try {
    var hImgs = $$('.drzwi img');
    if (hImgs.length && !RM) naScroll.push(function () {
      var y = window.scrollY; if (y > window.innerHeight) return;
      hImgs.forEach(function (im, i) { im.style.transform = 'scale(1.08) translateY(' + (y * (0.06 + i * 0.03)) + 'px)'; });
    });
  } catch (e) { }

  /* przeglądarka typów drzwi: aktywny typ = widoczne zdjęcie */
  try {
    var typy = $$('.typ'), fots = $$('.typy-fot img'), lic = $('.typy-fot .lic');
    if (typy.length && fots.length) {
      var ustaw = function (i) {
        typy.forEach(function (t, j) { t.classList.toggle('on', j === i); });
        fots.forEach(function (f, j) { f.classList.toggle('on', j === i); });
        if (lic) lic.textContent = fots[i].getAttribute('data-podpis') || '';
      };
      ustaw(0);
      naScroll.push(function () {
        if (!desktop()) return;
        var srodek = window.innerHeight * 0.5, best = 0;
        typy.forEach(function (t, j) { if (t.getBoundingClientRect().top < srodek) best = j; });
        ustaw(best);
      });
    }
  } catch (e) { }

  /* proces: pasek wypełnia się z przewijaniem */
  try {
    var pr = $('.proces');
    if (pr) naScroll.push(function () {
      var r = pr.getBoundingClientRect(), h = window.innerHeight;
      var p = Math.min(1, Math.max(0, (h * 0.85 - r.top) / (h * 0.6)));
      pr.style.setProperty('--p', p.toFixed(3));
    });
  } catch (e) { }

  /* galeria pozioma przypięta do przewijania */
  try {
    var poz = $('.poziom'), tor = $('.tor');
    if (poz && tor) {
      var wymiar = function () {
        if (!desktop() || RM) { poz.style.height = ''; tor.style.transform = ''; return; }
        var dl = tor.scrollWidth - window.innerWidth;
        poz.style.height = (window.innerHeight + Math.max(0, dl)) + 'px';
      };
      wymiar(); window.addEventListener('resize', wymiar);
      window.addEventListener('load', wymiar);
      naScroll.push(function () {
        if (!desktop() || RM) return;
        var r = poz.getBoundingClientRect(), dl = tor.scrollWidth - window.innerWidth;
        var p = Math.min(1, Math.max(0, -r.top / Math.max(1, poz.offsetHeight - window.innerHeight)));
        tor.style.transform = 'translate3d(' + (-p * dl).toFixed(1) + 'px,0,0)';
      });
    }
  } catch (e) { }

  /* FAQ: płynne rozwijanie */
  try {
    $$('.faq details').forEach(function (det) {
      var s = $('summary', det), o = $('.odp', det);
      s.addEventListener('click', function (ev) {
        if (RM || !o.animate) return;
        ev.preventDefault();
        if (det.open) {
          var a = o.animate([{ height: o.offsetHeight + 'px' }, { height: '0px' }], { duration: 380, easing: 'cubic-bezier(.22,.8,.2,1)' });
          a.onfinish = function () { det.open = false; };
        } else {
          det.open = true; var h = o.offsetHeight;
          o.animate([{ height: '0px' }, { height: h + 'px' }], { duration: 450, easing: 'cubic-bezier(.22,.8,.2,1)' });
        }
      });
    });
  } catch (e) { }

  /* realizacje: filtr + podgląd */
  try {
    var siatka = $('.siatka');
    if (siatka) {
      var figs = $$('figure', siatka);
      $$('.filtry button').forEach(function (bt) {
        bt.addEventListener('click', function () {
          var k = bt.getAttribute('data-f');
          $$('.filtry button').forEach(function (x) { x.setAttribute('aria-pressed', x === bt ? 'true' : 'false'); });
          figs.forEach(function (f) { f.classList.add('znika'); });
          setTimeout(function () {
            figs.forEach(function (f) {
              var pokaz = k === 'all' || f.getAttribute('data-k') === k;
              f.classList.toggle('ukryte', !pokaz);
            });
            requestAnimationFrame(function () { figs.forEach(function (f) { f.classList.remove('znika'); }); });
            if (lenis) lenis.resize();
          }, 260);
        });
      });
      var lb = $('.lb'), lbImg = $('.lb img'), lbCap = $('.lb figcaption'), idx = 0;
      var widoczne = function () { return figs.filter(function (f) { return !f.classList.contains('ukryte'); }); };
      var pokaz = function (i) {
        var w = widoczne(); idx = (i + w.length) % w.length;
        var im = $('img', w[idx]);
        lbImg.src = im.getAttribute('data-full'); lbImg.alt = im.alt; lbCap.textContent = im.alt;
      };
      figs.forEach(function (f) {
        f.addEventListener('click', function () { pokaz(widoczne().indexOf(f)); lb.classList.add('on'); if (lenis) lenis.stop(); $('.lb .zamk').focus(); });
        f.addEventListener('keydown', function (e) { if (e.key === 'Enter') f.click(); });
      });
      var zamknij = function () { lb.classList.remove('on'); if (lenis) lenis.start(); };
      $('.lb .zamk').addEventListener('click', zamknij);
      $('.lb .poprz').addEventListener('click', function () { pokaz(idx - 1); });
      $('.lb .nast').addEventListener('click', function () { pokaz(idx + 1); });
      lb.addEventListener('click', function (e) { if (e.target === lb) zamknij(); });
      document.addEventListener('keydown', function (e) {
        if (!lb.classList.contains('on')) return;
        if (e.key === 'Escape') zamknij(); if (e.key === 'ArrowLeft') pokaz(idx - 1); if (e.key === 'ArrowRight') pokaz(idx + 1);
      });
    }
  } catch (e) { }

  /* formularz (demo) */
  try {
    var form = $('.form form');
    form && form.addEventListener('submit', function (e) {
      e.preventDefault();
      form.parentNode.classList.add('wyslany');
      form.querySelector('button[type=submit]').disabled = true;
    });
  } catch (e) { }

  /* mapa */
  try {
    var m = $('#mapa');
    if (m && window.L) {
      var ll = [51.6681, 16.0812];
      var mapa = L.map(m, { scrollWheelZoom: false }).setView(ll, 15);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; OpenStreetMap' }).addTo(mapa);
      L.marker(ll).addTo(mapa).bindPopup('<b>Salon Fachowiec Antaba</b><br>ul. 1 Maja 16, Głogów').openPopup();
    }
  } catch (e) { }

  przelicz();
})();
