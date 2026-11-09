/* Fachowiec Głogów – ruch strony. Każdy blok w try/catch. */
(function () {
  var d = document.documentElement;
  var RM = false;
  try { RM = matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { }
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var duzy = function () { return matchMedia('(min-width: 861px)').matches; };
  var clamp = function (v, a, b) { return Math.min(b, Math.max(a, v)); };

  /* płynne przewijanie (mysz) */
  var lenis = null;
  try {
    if (!RM && window.Lenis && matchMedia('(hover: hover) and (pointer: fine)').matches) {
      lenis = new Lenis({ lerp: 0.09, smoothWheel: true });
      (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
    }
  } catch (e) { lenis = null; }

  var naScroll = [], tik = false;
  var przelicz = function () { tik = false; naScroll.forEach(function (f) { try { f(); } catch (e) { } }); };
  var zglos = function () { if (!tik) { tik = true; requestAnimationFrame(przelicz); } };
  addEventListener('scroll', zglos, { passive: true });
  addEventListener('resize', zglos, { passive: true });

  requestAnimationFrame(function () { requestAnimationFrame(function () { d.classList.add('go'); }); });

  /* nagłówek chowa się przy przewijaniu w dół */
  try {
    var top = $('.top'), sub = $('.sub'), kcta = $('.kcta'), ost = 0;
    naScroll.push(function () {
      var y = scrollY, ukryj = y > 400 && y > ost && !document.body.classList.contains('m-on');
      top.classList.toggle('hide', ukryj);
      if (sub) sub.classList.toggle('wyzej', ukryj);
      if (kcta) kcta.classList.toggle('on', y > 450);
      ost = y;
    });
  } catch (e) { }

  /* menu mobilne */
  try {
    var b = $('.burger');
    b && b.addEventListener('click', function () {
      var on = !document.body.classList.contains('m-on');
      document.body.classList.toggle('m-on', on); d.classList.toggle('m-on', on);
      b.setAttribute('aria-expanded', String(on));
      if (lenis) on ? lenis.stop() : lenis.start();
    });
  } catch (e) { }

  /* czy salon jest teraz otwarty – z godzin pon.–pt. 9–17 (czas polski) */
  try {
    var teraz = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Warsaw' }));
    var dz = teraz.getDay(), min = teraz.getHours() * 60 + teraz.getMinutes();
    var robocz = dz >= 1 && dz <= 5, otw = robocz && min >= 540 && min < 1020, txt;
    if (otw) txt = 'Salon otwarty teraz · do 17:00';
    else if (robocz && min < 540) txt = 'Zamknięte · otwieramy dziś o 9:00';
    else if (dz >= 1 && dz <= 4) txt = 'Zamknięte · otwieramy jutro o 9:00';
    else txt = 'Zamknięte · otwieramy w poniedziałek o 9:00';
    $$('.status').forEach(function (s) { s.classList.toggle('otw', otw); $('span', s).textContent = txt; });
    $$('.godz tr[data-d]').forEach(function (tr) {
      var z = tr.getAttribute('data-d').split(',').map(Number);
      if (z.indexOf(dz) > -1) tr.classList.add('dzis');
    });
  } catch (e) { }

  /* hero: wejście do salonu przewijane – witryna → wnętrze → ekspozycja */
  try {
    var scrub = $('.scrub');
    if (scrub) {
      var ims = $$('.okno img', scrub), kr = $$('.podpis .kr i', scrub), tyt = $('.podpis b', scrub), opis = $('.podpis span span', scrub), akt = -1;
      var n = ims.length;
      var ustawPodpis = function (i) {
        if (i === akt) return; akt = i;
        tyt.textContent = ims[i].getAttribute('data-t'); opis.textContent = ims[i].getAttribute('data-s');
        kr.forEach(function (k, j) { k.classList.toggle('on', j === i); });
      };
      ustawPodpis(0);
      var wys = function () { scrub.style.height = (duzy() && !RM) ? (innerHeight * (1 + n * 0.55)) + 'px' : ''; };
      wys(); addEventListener('resize', wys);
      naScroll.push(function () {
        if (!duzy() || RM) return;
        var r = scrub.getBoundingClientRect();
        var p = clamp(-r.top / Math.max(1, scrub.offsetHeight - innerHeight), 0, 1);
        var poz = p * (n - 1);                       /* 0..n-1 */
        ims.forEach(function (im, i) {
          var o = i === 0 ? 1 : clamp(poz - (i - 1) - 0.35, 0, 0.3) / 0.3;
          var lok = clamp(poz - i + 1, 0, 2);          /* wjazd w kadr */
          im.style.opacity = o;
          im.style.transform = 'scale(' + (1.12 - lok * 0.06).toFixed(4) + ')';
        });
        ustawPodpis(Math.round(poz));
      });
    }
  } catch (e) { }

  /* odsłanianie */
  try {
    var cele = $$('[data-r], .ods');
    if ('IntersectionObserver' in window && !RM) {
      var io = new IntersectionObserver(function (w) {
        w.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
      }, { rootMargin: '0px 0px -10% 0px', threshold: 0.01 });
      cele.forEach(function (el) { io.observe(el); });
    } else cele.forEach(function (el) { el.classList.add('in'); });
  } catch (e) { $$('[data-r], .ods').forEach(function (el) { el.classList.add('in'); }); }

  /* oferta: zdjęcie płynie za kursorem */
  try {
    var pg = $('.podglad');
    if (pg && !RM && matchMedia('(hover: hover)').matches) {
      var pimg = $$('img', pg), tx = 0, ty = 0, cx = 0, cy = 0, ruch = false;
      var petla = function () {
        cx += (tx - cx) * 0.16; cy += (ty - cy) * 0.16;
        pg.style.left = cx + 'px'; pg.style.top = cy + 'px';
        if (ruch) requestAnimationFrame(petla);
      };
      $$('.oferta a').forEach(function (a, i) {
        a.addEventListener('mouseenter', function (e) {
          if (!ruch) { cx = tx = e.clientX; cy = ty = e.clientY; ruch = true; requestAnimationFrame(petla); }
          pimg.forEach(function (im, j) { im.classList.toggle('on', j === i); });
          pg.classList.add('on');
        });
        a.addEventListener('mousemove', function (e) { tx = e.clientX + 190; ty = e.clientY; });
        a.addEventListener('mouseleave', function () { pg.classList.remove('on'); });
      });
      $('.oferta').addEventListener('mouseleave', function () { setTimeout(function () { ruch = pg.classList.contains('on'); }, 400); });
    }
  } catch (e) { }

  /* spacer po salonie: przewijanie w dół przesuwa tor w bok */
  try {
    var sp = $('.spacer'), tor = $('.tor'), pas = $('.spacer .pasek');
    if (sp && tor) {
      var wymiar = function () {
        if (!duzy() || RM) { sp.style.height = ''; tor.style.transform = ''; return; }
        sp.style.height = (innerHeight + Math.max(0, tor.scrollWidth - innerWidth)) + 'px';
      };
      wymiar(); addEventListener('resize', wymiar); addEventListener('load', wymiar);
      naScroll.push(function () {
        if (!duzy() || RM) return;
        var r = sp.getBoundingClientRect(), dl = tor.scrollWidth - innerWidth;
        var p = clamp(-r.top / Math.max(1, sp.offsetHeight - innerHeight), 0, 1);
        tor.style.transform = 'translate3d(' + (-p * dl).toFixed(1) + 'px,0,0)';
        if (pas) pas.style.setProperty('--p', p.toFixed(3));
      });
    }
  } catch (e) { }

  /* podmenu sekcji: podświetla bieżący blok */
  try {
    var linki = $$('.sub a');
    if (linki.length) {
      var bloki = linki.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
      naScroll.push(function () {
        var akt = 0;
        bloki.forEach(function (bl, i) { if (bl && bl.getBoundingClientRect().top < innerHeight * 0.4) akt = i; });
        linki.forEach(function (a, i) { a.classList.toggle('on', i === akt); });
      });
      linki.forEach(function (a) {
        a.addEventListener('click', function (e) {
          var cel = document.getElementById(a.getAttribute('href').slice(1));
          if (lenis && cel) { e.preventDefault(); lenis.scrollTo(cel, { offset: -130 }); }
        });
      });
    }
  } catch (e) { }

  /* FAQ – płynne rozwijanie */
  try {
    $$('.faq details').forEach(function (det) {
      var s = $('summary', det), o = $('.odp', det);
      s.addEventListener('click', function (ev) {
        if (RM || !o.animate) return;
        ev.preventDefault();
        if (det.open) {
          o.animate([{ height: o.offsetHeight + 'px' }, { height: '0px' }], { duration: 360, easing: 'cubic-bezier(.2,.75,.2,1)' }).onfinish = function () { det.open = false; if (lenis) lenis.resize(); };
        } else {
          det.open = true; var h = o.offsetHeight;
          o.animate([{ height: '0px' }, { height: h + 'px' }], { duration: 440, easing: 'cubic-bezier(.2,.75,.2,1)' }).onfinish = function () { if (lenis) lenis.resize(); };
        }
      });
    });
  } catch (e) { }

  /* realizacje: zakładki + podgląd */
  try {
    var siatka = $('.siatka');
    if (siatka) {
      var figs = $$('figure', siatka);
      $$('.zakl button').forEach(function (bt) {
        bt.addEventListener('click', function () {
          var k = bt.getAttribute('data-f');
          $$('.zakl button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === bt)); });
          figs.forEach(function (f) { f.classList.add('zn'); });
          setTimeout(function () {
            figs.forEach(function (f) { f.classList.toggle('ukr', !(k === 'all' || f.getAttribute('data-k') === k)); });
            requestAnimationFrame(function () { figs.forEach(function (f) { f.classList.remove('zn'); }); });
            if (lenis) lenis.resize();
          }, 240);
        });
      });
      var lb = $('.lb'), li = $('.lb img'), lc = $('.lb figcaption'), idx = 0;
      var wid = function () { return figs.filter(function (f) { return !f.classList.contains('ukr'); }); };
      var pokaz = function (i) { var w = wid(); idx = (i + w.length) % w.length; var im = $('img', w[idx]); li.src = im.getAttribute('data-full'); li.alt = im.alt; lc.textContent = im.alt; };
      var zamk = function () { lb.classList.remove('on'); if (lenis) lenis.start(); };
      figs.forEach(function (f) {
        f.addEventListener('click', function () { pokaz(wid().indexOf(f)); lb.classList.add('on'); if (lenis) lenis.stop(); $('.lb .x').focus(); });
        f.addEventListener('keydown', function (e) { if (e.key === 'Enter') f.click(); });
      });
      $('.lb .x').addEventListener('click', zamk);
      $('.lb .pv').addEventListener('click', function () { pokaz(idx - 1); });
      $('.lb .nx').addEventListener('click', function () { pokaz(idx + 1); });
      lb.addEventListener('click', function (e) { if (e.target === lb) zamk(); });
      addEventListener('keydown', function (e) {
        if (!lb.classList.contains('on')) return;
        if (e.key === 'Escape') zamk(); if (e.key === 'ArrowLeft') pokaz(idx - 1); if (e.key === 'ArrowRight') pokaz(idx + 1);
      });
    }
  } catch (e) { }

  /* formularz (wersja pokazowa) */
  try {
    var f = $('.form form');
    f && f.addEventListener('submit', function (e) { e.preventDefault(); f.parentNode.classList.add('wys'); $('button[type=submit]', f).disabled = true; });
  } catch (e) { }

  /* mapa */
  try {
    var m = $('#mapa');
    if (m && window.L) {
      var ll = [51.6681, 16.0812];
      var mapa = L.map(m, { scrollWheelZoom: false }).setView(ll, 16);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; OpenStreetMap' }).addTo(mapa);
      L.marker(ll).addTo(mapa).bindPopup('<b>Salon Fachowiec Głogów</b><br>ul. 1 Maja 16').openPopup();
    }
  } catch (e) { }

  przelicz();
})();
