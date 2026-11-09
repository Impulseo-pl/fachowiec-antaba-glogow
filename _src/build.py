# Generator dema v2: Salon Fachowiec Głogów (ANTABA Artur Słubowski). Uruchamiaj z katalogu repo: python _src/build.py
# Treść oparta na https://grupafachowiec.eu/salon/glogow/ + Oferteo (montaże, opinie) + wizytówka.
import json, os, html, datetime
BASE = 'https://impulseo-pl.github.io/fachowiec-antaba-glogow/'
TODAY = datetime.date.today().isoformat()
FOTO = {f['slug']: f for f in json.load(open('_src/foto.json', encoding='utf-8'))}
FOTO.update({f['slug']: f for f in json.load(open('_src/salon.json', encoding='utf-8'))})
FOTO['deski-drewniane-poglad'] = dict(slug='deski-drewniane-poglad', cat='', alt='Drewniane deski – zdjęcie poglądowe', w=1600, h=1182, sizes=[900, 1600])
LICZNIK = open('_src/licznik.js', encoding='utf-8').read().strip()
TEL1, TEL1H = '781 790 030', '+48781790030'
TEL2, TEL2H = '695 898 059', '+48695898059'
MAIL = 'aslubowski@wp.pl'
e = html.escape

def img(slug, pre, sizes='(max-width: 860px) 100vw, 50vw', eager=False, cls='', alt=None, extra=''):
    f = FOTO[slug]
    src = ', '.join(f'{pre}img/{slug}-{s}.webp {s}w' for s in f['sizes'])
    mid = f['sizes'][-1] if f['sizes'][-1] <= 900 else f['sizes'][1]
    h = round(f['h'] * mid / f['w'])
    a = e(alt if alt is not None else f['alt'])
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="{pre}img/{slug}-{mid}.webp" srcset="{src}" sizes="{sizes}" width="{mid}" height="{h}" alt="{a}" {load}{extra}>'

def full(slug, pre=''):
    f = FOTO[slug]; return f'{pre}img/{slug}-{f["sizes"][-1]}.webp'

I_TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
I_STR = '<svg class="s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
I_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'

NAV = [('', 'Start'), ('podlogi-i-sciany/', 'Podłogi i ściany'), ('drzwi/', 'Drzwi'), ('realizacje/', 'Realizacje'), ('kontakt/', 'Kontakt')]

FIRMA = {
    "@type": ["HomeAndConstructionBusiness", "Store"], "@id": BASE + "#firma",
    "name": "Salon Fachowiec Głogów – podłogi, ściany, drzwi",
    "alternateName": ["Fachowiec Antaba", "Antaba Głogów", "ANTABA Artur Słubowski"],
    "legalName": "ANTABA Artur Słubowski", "founder": {"@type": "Person", "name": "Artur Słubowski"},
    "foundingDate": "2017", "taxID": "6931112891", "url": BASE, "logo": BASE + "assets/logo-fachowiec.svg", "image": [BASE + full('salon-fachowiec-glogow-1-maja-16'), BASE + full('salon-glogow-wnetrze-ekspozycja'), BASE + "og.jpg"],
    "telephone": TEL1H, "email": MAIL, "priceRange": "$$",
    "description": "Salon Grupy Fachowiec w Głogowie: panele podłogowe laminowane, winylowe i drewniane, panele ścienne, deski tarasowe, drzwi wewnętrzne i zewnętrzne. Doradztwo, próbki, pomiar, transport i montaż.",
    "brand": [{"@type": "Brand", "name": n} for n in ["DRE", "Porta", "Erkado", "Gerda", "KMT", "KR Center", "Swiss Krono", "Gerflor"]],
    "parentOrganization": {"@type": "Organization", "name": "Grupa Fachowiec", "url": "https://grupafachowiec.eu/"},
    "address": {"@type": "PostalAddress", "streetAddress": "ul. 1 Maja 16", "postalCode": "67-200", "addressLocality": "Głogów", "addressRegion": "dolnośląskie", "addressCountry": "PL"},
    "geo": {"@type": "GeoCoordinates", "latitude": 51.6681, "longitude": 16.0812},
    "hasMap": "https://www.openstreetmap.org/?mlat=51.6681&mlon=16.0812#map=18/51.6681/16.0812",
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"}],
    "areaServed": [{"@type": "City", "name": "Głogów"}, {"@type": "City", "name": "Sława"}, {"@type": "City", "name": "Wschowa"},
                   {"@type": "State", "name": "dolnośląskie"}, {"@type": "State", "name": "lubuskie"}, {"@type": "State", "name": "wielkopolskie"}],
    "contactPoint": [{"@type": "ContactPoint", "telephone": TEL1H, "contactType": "sales", "availableLanguage": "pl"},
                     {"@type": "ContactPoint", "telephone": TEL2H, "contactType": "customer service", "description": "Montaż i pomiary", "availableLanguage": "pl"}],
    "sameAs": ["https://grupafachowiec.eu/salon/glogow/", "https://www.facebook.com/p/Antaba-100055216734311/", "https://www.oferteo.pl/antaba-artur-slubowski/firma/2932520"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Oferta salonu", "itemListElement": [
        {"@type": "OfferCatalog", "name": n, "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Product", "name": x}} for x in xs]} for n, xs in [
            ("Podłogi", ["Panele podłogowe laminowane", "Podłogi winylowe LVT", "Podłogi drewniane"]),
            ("Drzwi", ["Drzwi wewnętrzne", "Drzwi łazienkowe", "Drzwi zewnętrzne", "Drzwi przesuwne"]),
            ("Ściany", ["Panele ścienne"]), ("Deski tarasowe", ["Deski tarasowe"]), ("Akcesoria", ["Listwy przypodłogowe", "Podkłady", "Klamki"])]]},
    "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in ["Pomiar", "Transport", "Montaż podłóg", "Montaż drzwi", "Doradztwo", "Próbki materiałów"]],
}

def ld(url, title, desc, crumbs, extra=None):
    g = [FIRMA,
         {"@type": "WebSite", "@id": BASE + "#strona", "url": BASE, "name": "Salon Fachowiec Głogów", "inLanguage": "pl-PL", "publisher": {"@id": BASE + "#firma"}},
         {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": "pl-PL",
          "isPartOf": {"@id": BASE + "#strona"}, "about": {"@id": BASE + "#firma"}, "dateModified": TODAY}]
    if crumbs:
        g.append({"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (u, n) in enumerate(crumbs)]})
    g += extra or []
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False) + '</script>'

def faq_ld(url, items):
    return {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def faq_html(items):
    return '<div class="faq" data-r>' + ''.join(f'<details><summary>{e(q)}<i aria-hidden="true"></i></summary><div class="odp"><p>{e(a)}</p></div></details>' for q, a in items) + '</div>'

def okr(crumbs, pre):
    li = [f'<li aria-current="page">{e(n)}</li>' if i == len(crumbs) - 1 else f'<li><a href="{(pre + u) or "./"}">{e(n)}</a></li>' for i, (u, n) in enumerate(crumbs)]
    return f'<nav class="okr" aria-label="Okruszki"><ol>{"".join(li)}</ol></nav>'

GODZ = '''<table class="godz"><tbody><tr data-d="1,2,3,4,5"><td>Poniedziałek – piątek</td><td>9:00–17:00</td></tr><tr data-d="6,0"><td>Sobota – niedziela</td><td>nieczynne</td></tr></tbody></table>'''
STATUS = '<p class="status fade"><i></i><span>Pon.–pt. 9:00–17:00</span></p>'

def page(path, title, desc, body, crumbs=None, extra_ld=None, leaflet=False):
    pre = '' if path in ('', '404/') else '../' * path.count('/')
    L = lambda u: (pre + u) or './'
    url = BASE + ('' if path == '404/' else path)
    nav = ''.join(f'<a href="{L(u)}"{" aria-current=page" if u == path else ""}>{n}</a>' for u, n in NAV)
    lf = ('<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="">', '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>') if leaflet else ('', '')
    brand = f'<a class="brand" href="{L("")}" aria-label="Salon Fachowiec Głogów – strona główna"><img src="{pre}assets/logo-fachowiec.svg" width="178" height="29" alt="Fachowiec"><span><b>Głogów</b>ul. 1 Maja 16</span></a>'
    doc = f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{'noindex' if path == '404/' else 'index, follow, max-image-preview:large'}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:locale" content="pl_PL"><meta property="og:site_name" content="Salon Fachowiec Głogów">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="PL-DS"><meta name="geo.placename" content="Głogów"><meta name="geo.position" content="51.6681;16.0812"><meta name="ICBM" content="51.6681, 16.0812">
<meta name="theme-color" content="#2a2e32">
<link rel="icon" href="{BASE if path == '404/' else pre}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@500;700;800&family=Red+Hat+Text:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/styles.css">{lf[0]}
<script>document.documentElement.classList.add("js")</script>
<script>{LICZNIK}</script>
{ld(url, title, desc, [('', 'Start')] + crumbs if crumbs else None, extra_ld)}
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
<header class="top">
 <div class="wrap">
  {brand}
  <nav class="nav" aria-label="Menu główne">{nav}</nav>
  <a class="tel" href="tel:{TEL1H}"><small>Sprzedaż i doradztwo</small><b>{TEL1}</b></a>
  <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="mnav"><i></i><i></i><i></i></button>
 </div>
</header>
<nav class="mnav" id="mnav" aria-label="Menu mobilne">{''.join(f'<a href="{L(u)}">{n}</a>' for u, n in NAV)}<div class="mt">Sprzedaż i doradztwo<a href="tel:{TEL1H}">{TEL1}</a></div></nav>
<main id="tresc">
{body(pre)}
</main>
<footer class="stopka">
 <div class="wrap">
  <div>{brand}<p>Salon Grupy Fachowiec w Głogowie. Podłogi, panele ścienne i drzwi z doradztwem, pomiarem, transportem i montażem.</p></div>
  <div><h2>Salon</h2><address>ul. 1 Maja 16<br>67-200 Głogów<br><br>pon.–pt. 9:00–17:00<br>sob.–niedz. nieczynne</address></div>
  <div><h2>Kontakt</h2><ul><li>Sprzedaż: <a href="tel:{TEL1H}">{TEL1}</a></li><li>Montaż i pomiary: <a href="tel:{TEL2H}">{TEL2}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="https://www.facebook.com/p/Antaba-100055216734311/" target="_blank" rel="noopener">Facebook</a></li></ul></div>
  <div><h2>Oferta</h2><ul><li><a href="{pre}podlogi-i-sciany/#laminowane">Panele podłogowe</a></li><li><a href="{pre}podlogi-i-sciany/#winylowe">Podłogi winylowe</a></li><li><a href="{pre}podlogi-i-sciany/#sciany">Panele ścienne</a></li><li><a href="{pre}drzwi/#wewnetrzne">Drzwi wewnętrzne</a></li><li><a href="{pre}drzwi/#zewnetrzne">Drzwi zewnętrzne</a></li></ul></div>
  <div class="dol"><span>Salon prowadzi ANTABA Artur Słubowski · NIP 693-111-28-91</span><span>Fachowiec – sieć salonów Grupy Fachowiec</span></div>
 </div>
</footer>
<div class="kcta"><a class="btn btn-or" href="tel:{TEL1H}">{I_TEL}Zadzwoń</a><a class="btn btn-gh" style="background:var(--graf-2)" href="{L('kontakt/')}">Jak dojechać</a></div>
{lf[1]}<script src="{pre}assets/lenis.min.js" defer></script><script src="{pre}assets/app.js" defer></script>
</body>
</html>
'''
    doc = doc.replace('ul. 1 Maja 16', 'ul. 1 Maja 16').replace('1 Maja', '1 Maja')
    out = '404.html' if path == '404/' else (path + 'index.html' if path else 'index.html')
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    open(out, 'w', encoding='utf-8').write(doc)

def cta_b(pre, h, p):
    return f'<div class="cta-b" data-r><div><h2>{h}</h2><p>{p}</p></div><div class="cta"><a class="btn btn-or" href="tel:{TEL1H}">{I_TEL}{TEL1}</a><a class="btn btn-gh" href="{pre}kontakt/">Jak dojechać</a></div></div>'

def portal(pre, slugs, eager=False):
    ims = ''.join(img(s, pre, '(max-width: 860px) 100vw, 52vw', eager=(eager and i == 0), extra=f' data-t="{e(t)}" data-s="{e(o)}"') for i, (s, t, o) in enumerate(slugs))
    kr = ''.join('<i></i>' for _ in slugs) if len(slugs) > 1 else ''
    s0 = slugs[0]
    return f'<div class="portal"><div class="okno">{ims}</div><div class="podpis"><span><b>{e(s0[1])}</b><span>{e(s0[2])}</span></span><span class="kr" aria-hidden="true">{kr}</span></div></div>'

USLUGI = [('04-set-square', 'Pomiar', 'Mierzymy pomieszczenia i otwory drzwiowe na miejscu.'),
          ('05-delivery-truck', 'Transport', 'Dowozimy zakupione podłogi i drzwi pod wskazany adres.'),
          ('06-tools', 'Montaż', 'Układamy podłogi i montujemy drzwi w ustalonym terminie.'),
          ('01-chat', 'Doradztwo specjalistów', 'Dobieramy materiał do pomieszczenia i sposobu użytkowania.'),
          ('02-ruler-and-pencil', 'Próbki materiałów', 'Porównasz dekory na żywo, w dziennym świetle.'),
          ('03-shopping-cart', 'Szeroki asortyment', 'Podłogi, ściany, drzwi, tarasy i akcesoria w jednym miejscu.')]

OPINIE = [('A. I.', '2018', 'Usługa wykonana perfekcyjnie – doradztwo, wybór, uzgodniony czas wykonania usługi, fachowość, ceny przyzwoite, duży wybór, fachowa obsługa.'),
          ('T.', '2024', 'Super doradztwo, bardzo miła Pani, kompetentna. Duży wybór drzwi, super montażyści, fachowo podchodzą do swojej pracy. Wykonanie na 5+, bez uwag.')]

# ================= START =================
def start(pre):
    usl = ''.join(f'<div class="usl" data-r="{i+1}"><img src="{pre}assets/ikony/{ik}.svg" alt="" width="60" height="46"><h3>{h}</h3><p>{t}</p></div>' for i, (ik, h, t) in enumerate(USLUGI))
    oferta = [('Podłogi', 'Panele laminowane, podłogi winylowe LVT i deska drewniana.', 'podlogi-i-sciany/#laminowane', 'panele-swiss-krono-glogow'),
              ('Drzwi', 'Wewnętrzne, łazienkowe, przesuwne, do mieszkań i zewnętrzne.', 'drzwi/', 'ekspozycja-drzwi-wewnetrznych'),
              ('Ściany', 'Panele ścienne i listwy – ściana bez kucia i tynkowania.', 'podlogi-i-sciany/#sciany', 'listwy-i-panele-wzorniki'),
              ('Deski tarasowe', 'Kompozytowe i drewniane, z legarami i akcesoriami.', 'podlogi-i-sciany/#tarasowe', 'deski-drewniane-poglad'),
              ('Akcesoria', 'Listwy przypodłogowe, podkłady, progi, klamki.', 'podlogi-i-sciany/#akcesoria', 'klamki-akcesoria-drzwi')]
    of = ''.join(f'<li><a href="{pre}{u}"><h3>{h}</h3><p>{t}</p><span class="ar" aria-hidden="true">{I_STR}</span>{img(s, pre, "100vw", cls="mini", alt="")}</a></li>' for h, t, u, s in oferta)
    pg = ''.join(f'<img src="{pre}img/{s}-{FOTO[s]["sizes"][0]}.webp" alt="" loading="lazy">' for *_, s in oferta)
    spacer = [('salon-glogow-wnetrze-ekspozycja', 'Wejście', 'Drzwi po lewej, podłogi po prawej – tak wita salon.'),
              ('ekspozycja-drzwi-dre-glogow', 'Ekspozycja DRE', 'Drzwi wewnętrzne w grafitowych portalach.'),
              ('drzwi-porta-szklane-loft', 'Porta', 'Skrzydła przeszklone w czarnej ramie i z lustrem.'),
              ('panele-swiss-krono-glogow', 'Panele Swiss Krono', 'Wzorniki paneli laminowanych do przejrzenia deska po desce.'),
              ('panele-winylowe-gerflor-glogow', 'Winyle Gerflor', 'Podłogi winylowe obok paneli – porównasz je od razu.'),
              ('drzwi-zewnetrzne-ekspozycja-glogow', 'Drzwi zewnętrzne', 'Modele z pochwytami i przeszkleniem.'),
              ('listwy-przypodlogowe-wzornik', 'Listwy i panele', 'Listwy dobierzesz do podłogi na miejscu.'),
              ('klamki-akcesoria-drzwi', 'Klamki', 'Stojak z klamkami w kilku wykończeniach.'),
              ('stanowisko-doradcy-fachowiec', 'Doradca', 'Tu ustalisz pomiar, transport i termin montażu.')]
    tor = ''.join(f'<figure>{img(s, pre, "40vw")}<figcaption><b>{t}</b>{o}</figcaption></figure>' for s, t, o in spacer)
    mont = ['drzwi-wewnetrzne-dab-czarna-oscieznica', 'drzwi-zewnetrzne-dwuskrzydlowe-antracyt', 'drzwi-szklane-loft-czarna-rama']
    return f'''
<section class="wejscie scrub" aria-labelledby="h1">
 <div class="wejscie-in">
  <div>
   {STATUS}
   <h1 id="h1" class="fade d1">Podłogi i drzwi w Głogowie z montażem</h1>
   <p class="lead fade d2">Salon Grupy Fachowiec przy ul. 1 Maja 16. Markowe podłogi, panele ścienne i drzwi – z doradztwem, pomiarem, transportem i montażem.</p>
   <div class="cta fade d3"><a class="btn btn-or" href="tel:{TEL1H}">{I_TEL}Zadzwoń: {TEL1}</a><a class="btn btn-gh" href="{pre}kontakt/">Jak dojechać {I_STR}</a></div>
   <dl class="adres fade d4"><dt>Adres</dt><dd>ul. 1 Maja 16, Głogów</dd><dt>Godziny</dt><dd>pon.–pt. 9:00–17:00</dd><dt>Montaż i pomiary</dt><dd><a href="tel:{TEL2H}">{TEL2}</a></dd></dl>
  </div>
  <div class="fade d2">
   {portal(pre, [('salon-fachowiec-glogow-1-maja-16', 'ul. 1 Maja 16', 'Witryna salonu w centrum Głogowa'), ('salon-glogow-wnetrze-ekspozycja', 'Wnętrze salonu', 'Drzwi i podłogi na jednej ekspozycji'), ('ekspozycja-drzwi-dre-glogow', 'Ekspozycja drzwi', 'DRE, Porta, Erkado, Gerda i inni')], eager=True)}
   <p class="przewin" aria-hidden="true"><i></i>Przewiń, żeby wejść do środka</p>
  </div>
 </div>
</section>

<section class="uslugi" aria-label="Usługi salonu">{usl}</section>

<section class="sek sek-w" aria-labelledby="of-h">
 <div class="wrap">
  <div class="naglowek" data-r><span class="etyk">Poznaj naszą ofertę</span><h2 id="of-h">Na podłogę, na ścianę i do drzwi</h2><p class="lead">Pięć działów, jeden salon. Wszystko obejrzysz na ekspozycji przy 1 Maja, zanim cokolwiek zamówisz.</p></div>
  <ul class="oferta">{of}</ul>
 </div>
 <div class="podglad" aria-hidden="true">{pg}</div>
</section>

<section class="spacer" aria-labelledby="sp-h">
 <div class="spacer-in">
  <div class="wrap"><div class="naglowek"><span class="etyk" style="color:#ff8a4c">Zdjęcia z salonu w Głogowie</span><h2 id="sp-h">Spacer po salonie</h2></div></div>
  <div class="pasek" aria-hidden="true"><i></i></div>
  <div class="tor">{tor}</div>
 </div>
</section>

<section class="sek" aria-labelledby="red-h">
 <div class="wrap red">
  <figure class="fot ods">{img('stanowisko-doradcy-fachowiec', pre, '(max-width: 860px) 100vw, 45vw')}<figcaption>Stanowisko doradcy w salonie przy ul. 1 Maja 16</figcaption></figure>
  <div>
   <span class="etyk" data-r>Salon Grupy Fachowiec w Głogowie</span>
   <h2 id="red-h" data-r>Podłoga to decyzja na lata. Lepiej podjąć ją na żywo</h2>
   <p class="lead" data-r>Podłoga ma pasować do wnętrza, ale przede wszystkim wytrzymać codzienne użytkowanie. Dlatego w salonie możesz ją zobaczyć, dotknąć i porównać z innymi.</p>
   <h3 data-r>Laminat, winyl czy drewno?</h3>
   <p data-r>Doradcy pomogą dobrać materiał do pomieszczenia i sposobu użytkowania: odporność na ścieranie i wilgoć, sposób montażu, ogrzewanie podłogowe. Prawdziwy odcień, struktura i to, jak deska odbija światło, trudno ocenić ze zdjęcia – na ekspozycji widać to od razu.</p>
   <h3 data-r>Drzwi dobrane do podłogi</h3>
   <p data-r>Podłoga i drzwi to elementy jednej aranżacji. Nie muszą być w tym samym kolorze – ciekawy efekt daje też kontrast. Przy drzwiach wewnętrznych liczy się wygląd, konstrukcja, sposób otwierania, przeszklenie i akustyka. Zewnętrzne mają izolować i chronić, a przy okazji pasować do elewacji.</p>
   <h3 data-r>Od zakupu do montażu</h3>
   <p data-r>Zakup to jeden etap remontu. Równie ważne są transport i montaż, bo od nich zależy, jak podłoga i drzwi będą wyglądać za kilka lat. Szczegóły realizacji ustalisz z doradcą w salonie.</p>
   <p data-r><a class="ul" href="{pre}podlogi-i-sciany/">Podłogi i panele ścienne</a> &nbsp;·&nbsp; <a class="ul" href="{pre}drzwi/">Drzwi wewnętrzne i zewnętrzne</a></p>
  </div>
 </div>
</section>

<section class="sek sek-w" aria-labelledby="mk-h" style="padding-top:clamp(60px,7vw,100px);padding-bottom:clamp(60px,7vw,100px)">
 <div class="wrap">
  <div class="naglowek" data-r><span class="etyk">Na ekspozycji</span><h2 id="mk-h">Marki, które obejrzysz na miejscu</h2></div>
  <div class="marki" data-r><span>DRE</span><span>Porta</span><span>Erkado</span><span>Gerda</span><span>KMT</span><span>KR Center</span><span>Swiss Krono</span><span>Gerflor</span></div>
  <p class="marki-nota" data-r>Na podstawie ekspozycji w salonie. Dostępność konkretnych modeli potwierdzi doradca.</p>
 </div>
</section>

<section class="sek" aria-labelledby="mo-h">
 <div class="wrap mont">
  <div>
   <span class="etyk" data-r>Montaż robi nasza ekipa</span>
   <h2 id="mo-h" data-r>Montujemy drzwi od 2017 roku</h2>
   <p data-r>Salon prowadzi firma ANTABA Artura Słubowskiego. Sprzedajemy i montujemy drzwi wewnętrzne, przesuwne, do mieszkań i zewnętrzne – zawsze po pomiarze.</p>
   {''.join(f'<blockquote class="cyt" data-r><p>„{e(t)}”</p><cite>{a} · opinia na Oferteo, {r}</cite></blockquote>' for a, r, t in OPINIE)}
   <p data-r><a class="ul" href="{pre}realizacje/">Zobacz zdjęcia z montaży</a></p>
  </div>
  <div class="mont-fot">{''.join(f'<figure class="ods">{img(s, pre, "(max-width: 560px) 50vw, 20vw")}</figure>' for s in mont)}</div>
 </div>
</section>

<section class="sek sek-o" style="padding:clamp(56px,6vw,84px) 0" aria-labelledby="bz-h">
 <div class="wrap bez">
  <div data-r><h2 id="bz-h">Byłeś już u nas i masz wybrane produkty?</h2><p>Zamów je telefonicznie lub mailowo, bez ponownej wizyty w salonie.</p></div>
  <div class="cta" data-r="2"><a class="btn btn-or" href="tel:{TEL1H}">{I_TEL}{TEL1}</a><a class="btn btn-dk" href="mailto:{MAIL}">{I_MAIL}{MAIL}</a></div>
 </div>
</section>

<section class="sek dk" aria-labelledby="dj-h">
 <div class="wrap kon">
  <div data-r>
   <span class="etyk">Jak dojechać</span>
   <h2 id="dj-h">ul. 1 Maja 16, Głogów</h2>
   {GODZ}
   <div class="tels"><small>Sprzedaż i doradztwo</small><a href="tel:{TEL1H}">{TEL1}</a><small>Montaż i pomiary</small><a href="tel:{TEL2H}">{TEL2}</a></div>
  </div>
  <div id="mapa" role="region" aria-label="Mapa dojazdu do salonu" data-r="2"></div>
 </div>
</section>'''

# ================= PODŁOGI I ŚCIANY =================
FAQ_P = [
    ('Panele winylowe czy laminowane – które lepsze?', 'To zależy od pomieszczenia. Laminat jest twardy i odporny na ścieranie, dobry do salonu i sypialni. Winyl jest cieplejszy w dotyku, cichszy i lepiej znosi wilgoć, dlatego częściej trafia do kuchni i przedpokoju. W salonie porównasz oba na wzornikach.'),
    ('Jakie panele na ogrzewanie podłogowe?', 'Zarówno panele laminowane, jak i winylowe mogą leżeć na ogrzewaniu podłogowym, jeśli producent dopuszcza taki montaż. Sprawdzamy to w parametrach konkretnego modelu i dobieramy właściwy podkład.'),
    ('Panele winylowe czy laminowane do kuchni?', 'Do kuchni częściej polecamy winyl, bo lepiej znosi wilgoć. Przy każdym modelu sprawdzamy jednak, czy producent dopuszcza go do pomieszczeń o podwyższonej wilgotności.'),
    ('Czy mogę zobaczyć próbki przed zakupem?', 'Tak. W salonie przy ul. 1 Maja 16 są wzorniki paneli laminowanych, podłóg winylowych i listew. Odcień i struktura wyglądają na żywo inaczej niż na zdjęciu.'),
    ('Czy montujecie podłogi?', 'Tak, oferujemy profesjonalny montaż. Zapytaj doradcę w salonie lub zadzwoń – ustalimy pomiar pomieszczeń i dogodny termin.'),
    ('Czy mogę zamówić panele bez ponownej wizyty?', 'Tak. Jeśli byłeś już w salonie i masz wybrane produkty, zamówisz je telefonicznie lub mailowo.'),
]

def blok(pre, id_, etyk, h, txt, pkt, fots, prod='', odw=False):
    fs = ''.join(f'<figure class="ods">{img(s, pre, "(max-width: 860px) 50vw, 24vw")}<figcaption>{e(FOTO[s]["alt"])}</figcaption></figure>' for s in fots)
    fbox = f'<div class="fots{" jedno" if len(fots) == 1 else ""}">{fs}</div>' if fots else ''
    p = ''.join(f'<li>{x}</li>' for x in pkt)
    st = '' if fots else ' style="grid-template-columns:1fr;max-width:860px"'
    return f'<section class="blok{" odw" if odw else ""}" id="{id_}" aria-labelledby="{id_}-h"{st}><div><span class="etyk" data-r>{etyk}</span><h2 id="{id_}-h" data-r>{h}</h2><div data-r>{txt}</div><ul class="pk" data-r>{p}</ul>{f"<p class=producenci data-r>{prod}</p>" if prod else ""}</div>{fbox}</section>'

def sub(items):
    return '<nav class="sub" aria-label="Na tej stronie"><div class="wrap">' + ''.join(f'<a href="#{i}">{n}</a>' for i, n in items) + '</div></nav>'

def podlogi(pre):
    bl = ''.join([
        blok(pre, 'laminowane', 'Podłogi', 'Panele podłogowe laminowane', '<p>Twarde, odporne na ścieranie i dostępne w wielu wzorach i kolorach – od dekorów inspirowanych naturalnym drewnem po wyraziste wzory do nowoczesnych wnętrz. Dobry wybór do salonu, sypialni i pokoju dziecka.</p>',
             ['Dekory drewna i kamienia', 'Różne klasy ścieralności', 'Podkłady i listwy do kompletu'], ['panele-swiss-krono-glogow', 'wzornik-paneli-podlogowych'], 'Na ekspozycji m.in. <b>Swiss Krono</b>.'),
        blok(pre, 'winylowe', 'Podłogi', 'Podłogi winylowe LVT', '<p>Cieplejsze w dotyku i cichsze od laminatu, pasują do praktycznie każdego stylu. Sprawdzają się w kuchni i przedpokoju. Przy pomieszczeniach o podwyższonej wilgotności zawsze sprawdzamy parametry i przeznaczenie konkretnego produktu.</p>',
             ['Wersje klejone i na zatrzask', 'Na ogrzewanie podłogowe – zgodnie z kartą produktu', 'Dekory drewna i kamienia'], ['panele-winylowe-gerflor-glogow', 'wzorniki-podlog-salon'], 'Na ekspozycji m.in. <b>Gerflor</b>.', True),
        blok(pre, 'drewniane', 'Podłogi', 'Podłogi drewniane', '<p>Naturalne drewno do wnętrz, które mają być przytulne na lata. Każda deska ma inne usłojenie, dlatego warto ją obejrzeć na żywo i porozmawiać z doradcą o wykończeniu i pielęgnacji.</p>',
             ['Deski warstwowe i lite', 'Wykończenie olejowane lub lakierowane', 'Listwy w kolorze podłogi'], []),
        blok(pre, 'sciany', 'Ściany', 'Panele ścienne', '<p>Efektowna ściana za łóżkiem, telewizorem albo w przedpokoju bez kucia i tynkowania. Panele i listwy dobierzesz w salonie razem z podłogą, żeby całość tworzyła jedną aranżację.</p>',
             ['Panele dekoracyjne i lamele', 'Listwy ścienne i przypodłogowe', 'Montaż na klej lub system listew'], ['listwy-i-panele-wzorniki'], '', True),
        blok(pre, 'tarasowe', 'Tarasy', 'Deski tarasowe', '<p>Kompozytowe, które nie wymagają olejowania, i drewniane dla miłośników naturalnego materiału. Doradzimy też legary i sposób montażu.</p>',
             ['Deski kompozytowe', 'Deski drewniane', 'Legary, klipsy i listwy maskujące'], ['deski-drewniane-poglad']),
        blok(pre, 'akcesoria', 'Akcesoria', 'Listwy, podkłady i klamki', '<p>Wszystko, czego potrzeba do wykończenia podłogi i drzwi: listwy przypodłogowe, progi, podkłady pod panele, klamki i wkładki.</p>',
             ['Listwy przypodłogowe i progi', 'Podkłady pod panele', 'Klamki i akcesoria do drzwi'], ['klamki-akcesoria-drzwi', 'listwy-przypodlogowe-wzornik'], '', True),
    ])
    tab = '''<div class="tw" data-r><table class="t"><caption>Panele laminowane a podłogi winylowe</caption>
<thead><tr><th scope="col">Cecha</th><th scope="col">Panele laminowane</th><th scope="col">Podłogi winylowe</th></tr></thead><tbody>
<tr><th scope="row">Wilgoć</th><td>Ograniczona odporność, zależy od modelu</td><td>Lepiej ją znoszą – kuchnia, przedpokój</td></tr>
<tr><th scope="row">W dotyku</th><td>Twarde i chłodniejsze</td><td>Cieplejsze i bardziej sprężyste</td></tr>
<tr><th scope="row">Akustyka</th><td>Głośniejsze, warto dobrać dobry podkład</td><td>Cichsze przy chodzeniu</td></tr>
<tr><th scope="row">Ogrzewanie podłogowe</th><td>Tak, jeśli dopuszcza producent</td><td>Tak, jeśli dopuszcza producent</td></tr>
<tr><th scope="row">Gdzie najczęściej</th><td>Salon, sypialnia, pokój dziecka</td><td>Kuchnia, przedpokój, poddasze</td></tr>
</tbody></table></div><p class="t-nota" data-r>Ostatecznie decydują parametry konkretnego modelu – sprawdzimy je z Tobą w salonie.</p>'''
    return f'''
<section class="ph" aria-labelledby="h1"><div class="wrap">
 <div>{okr([('', 'Start'), ('podlogi-i-sciany/', 'Podłogi i ściany')], pre)}<h1 id="h1">Panele podłogowe i ścienne w Głogowie</h1><p class="lead">Panele laminowane, podłogi winylowe i drewniane, panele ścienne i deski tarasowe. Wzorniki na ekspozycji, doradztwo i montaż.</p><a class="btn btn-or" href="tel:{TEL1H}">{I_TEL}{TEL1}</a></div>
 {portal(pre, [('panele-swiss-krono-glogow', 'Ekspozycja podłóg', 'Wzorniki paneli w salonie przy ul. 1 Maja 16')], eager=True)}
</div></section>
{sub([('laminowane', 'Laminowane'), ('winylowe', 'Winylowe'), ('drewniane', 'Drewniane'), ('sciany', 'Ściany'), ('tarasowe', 'Tarasowe'), ('akcesoria', 'Akcesoria'), ('roznice', 'Laminat czy winyl'), ('faq', 'Pytania')])}
<div class="wrap">{bl}</div>
<section class="sek sek-w" id="roznice" aria-labelledby="ro-h" style="scroll-margin-top:120px"><div class="wrap">
 <div class="naglowek" data-r><span class="etyk">Najczęstsze pytanie w salonie</span><h2 id="ro-h">Panele winylowe czy laminowane?</h2></div>
 {tab}
</div></section>
<section class="sek" id="faq" aria-labelledby="fq-h" style="scroll-margin-top:120px"><div class="wrap">
 <div class="naglowek" data-r><h2 id="fq-h">Pytania o podłogi</h2></div>
 {faq_html(FAQ_P)}
 <div style="margin-top:56px">{cta_b(pre, 'Przyjdź po próbki', 'Salon przy ul. 1 Maja 16 w Głogowie, pon.–pt. 9:00–17:00.')}</div>
</div></section>'''

# ================= DRZWI =================
FAQ_D = [
    ('Co to znaczy, że drzwi są bezprzylgowe?', 'Skrzydło drzwi bezprzylgowych po zamknięciu licuje z ościeżnicą – nie ma wystającego zakładu (przylgi), a zawiasy są ukryte. Przylgowe mają zakład nachodzący na ościeżnicę i widoczne zawiasy.'),
    ('Drzwi przylgowe czy bezprzylgowe – co wybrać?', 'Przylgowe są prostsze i zwykle tańsze, dobrze sprawdzają się w klasycznych wnętrzach. Bezprzylgowe dają gładką płaszczyznę i pasują do nowoczesnych aranżacji. W salonie zobaczysz oba rozwiązania obok siebie.'),
    ('Czym różnią się drzwi łazienkowe?', 'Drzwi do łazienki mają otwory wentylacyjne – tuleje lub podcięcie – i zwykle zamek z blokadą WC. Dobierzemy je w tym samym wzorze co pozostałe drzwi w mieszkaniu.'),
    ('Czy przed zamówieniem robicie pomiar?', 'Tak. Montaż poprzedzamy pomiarem otworów u klienta, dzięki czemu zamawiamy właściwe wymiary skrzydeł i ościeżnic.'),
    ('Czy montujecie drzwi kupione w innym sklepie?', 'Pomiar, transport i montaż wykonujemy dla produktów kupionych w naszym salonie. Wtedy odpowiadamy za całość – od wyboru modelu po regulację.'),
    ('Czy dojeżdżacie poza Głogów?', 'Tak. Pracujemy w województwach dolnośląskim, lubuskim i wielkopolskim, m.in. w Sławie i Wschowie. Zadzwoń, a potwierdzimy dojazd.'),
]

def drzwi(pre):
    bl = ''.join([
        blok(pre, 'wewnetrzne', 'Drzwi wewnętrzne', 'Drzwi wewnętrzne do pokoi', '<p>Gładkie, frezowane, ramiakowe i z przeszkleniem – w bieli, okleinach drewnopodobnych, szarościach i z czarną ościeżnicą. Przy wyborze warto uwzględnić wygląd, konstrukcję, sposób otwierania, przeszklenie i właściwości akustyczne.</p>',
             ['Przylgowe i bezprzylgowe', 'Ościeżnice regulowane i stałe', 'Klamki i wkładki do kompletu'], ['ekspozycja-drzwi-dre-glogow', 'drzwi-porta-szalwia-biale'], 'Na ekspozycji m.in. <b>DRE</b>, <b>Porta</b> i <b>Erkado</b>.'),
        blok(pre, 'lazienkowe', 'Drzwi wewnętrzne', 'Drzwi łazienkowe', '<p>Z tulejami lub podcięciem wentylacyjnym i zamkiem z blokadą. W tym samym wzorze co reszta drzwi w mieszkaniu, żeby korytarz wyglądał spójnie.</p>',
             ['Tuleje lub podcięcie wentylacyjne', 'Zamek z blokadą WC', 'Wzór jak pozostałe drzwi'], ['drzwi-wewnetrzne-biale-z-tulejami'], '', True),
        blok(pre, 'rewersyjne', 'Drzwi wewnętrzne', 'Rewersyjne, ukryte i łamane', '<p>Drzwi, które mają zlewać się ze ścianą albo zmieścić tam, gdzie zwykłe skrzydło blokuje przejście. Przy tych modelach o efekcie decydują milimetry, dlatego zaczynamy od pomiaru.</p>',
             ['Rewersyjne – skrzydło licuje ze ścianą', 'Ukryte – do pomalowania na kolor ściany', 'Łamane – do wąskich korytarzy i spiżarni'], ['drzwi-wewnetrzne-biale-trzy-frezy', 'drzwi-wewnetrzne-jasne-ekspozycja']),
        blok(pre, 'szklane', 'Drzwi wewnętrzne', 'Drzwi szklane i loftowe', '<p>Szkło w czarnej ramie ze szprosami doświetla przedpokój i oddziela kuchnię, nie zamykając przestrzeni.</p>',
             ['Skrzydła całoszklane', 'Rama ze szprosami w stylu loft', 'Szkło przezroczyste i matowe'], ['drzwi-porta-szklane-loft', 'drzwi-szklane-loft-czarna-rama'], '', True),
        blok(pre, 'przesuwne', 'Drzwi wewnętrzne', 'Drzwi przesuwne', '<p>Skrzydło przesuwa się wzdłuż ściany albo chowa w niej, zamiast otwierać się w pokój. Do garderoby, małej łazienki i między salonem a kuchnią.</p>',
             ['Systemy naścienne', 'Systemy chowane w ścianie', 'Skrzydła pełne i przeszklone'], ['drzwi-przesuwne-grafit-i-skrzydlowe', 'drzwi-przesuwne-biale-przeszklone']),
        blok(pre, 'mieszkania', 'Drzwi wejściowe', 'Drzwi do mieszkania w bloku', '<p>Drzwi wejściowe do mieszkania dobierzemy do wymiaru otworu i do drzwi wewnętrznych. Po pomiarze nasza ekipa je zamontuje.</p>',
             ['Wizjer i zamki', 'Wyciszenie od klatki schodowej', 'Kolory pasujące do drzwi wewnętrznych'], ['drzwi-do-mieszkania-zloty-dab-intarsje', 'drzwi-do-mieszkania-szary-dab-wizjer'], '', True),
        blok(pre, 'zewnetrzne', 'Drzwi wejściowe', 'Drzwi zewnętrzne z montażem', '<p>Drzwi zewnętrzne powinny zapewniać izolację i bezpieczeństwo, a ich stylistyka może uzupełnić elewację. Osadzamy je w stanie surowym i w wykończonych domach.</p>',
             ['Jedno- i dwuskrzydłowe', 'Z przeszkleniem i pochwytem', 'Montaż z regulacją okuć'], ['drzwi-zewnetrzne-ekspozycja-glogow', 'drzwi-zewnetrzne-dwuskrzydlowe-antracyt'], 'Na ekspozycji m.in. <b>Gerda</b>, <b>KMT</b> i <b>KR Center</b>.'),
    ])
    tab = '''<div class="tw" data-r><table class="t"><caption>Rodzaje drzwi wewnętrznych</caption>
<thead><tr><th scope="col">Rodzaj</th><th scope="col">Jak wygląda</th><th scope="col">Zawiasy</th><th scope="col">Kiedy wybrać</th></tr></thead><tbody>
<tr><th scope="row">Przylgowe</th><td>Skrzydło nachodzi zakładem na ościeżnicę</td><td>Widoczne</td><td>Klasyczne wnętrza, rozsądny budżet</td></tr>
<tr><th scope="row">Bezprzylgowe</th><td>Skrzydło licuje z ościeżnicą</td><td>Ukryte</td><td>Nowoczesne aranżacje</td></tr>
<tr><th scope="row">Rewersyjne</th><td>Od strony otwierania licuje ze ścianą</td><td>Ukryte</td><td>Ościeżnica ma zniknąć z jednej strony</td></tr>
<tr><th scope="row">Przesuwne</th><td>Skrzydło jedzie po szynie lub chowa się w ścianie</td><td>Brak – wózki i prowadnica</td><td>Mało miejsca na otwieranie</td></tr>
</tbody></table></div>'''
    return f'''
<section class="ph" aria-labelledby="h1"><div class="wrap">
 <div>{okr([('', 'Start'), ('drzwi/', 'Drzwi')], pre)}<h1 id="h1">Drzwi w Głogowie z pomiarem i montażem</h1><p class="lead">Drzwi wewnętrzne, łazienkowe, przesuwne, do mieszkań i zewnętrzne. Ekspozycja w salonie przy ul. 1 Maja 16, a montaż robi nasza ekipa – od 2017 roku.</p><a class="btn btn-or" href="tel:{TEL2H}">{I_TEL}Pomiar: {TEL2}</a></div>
 {portal(pre, [('ekspozycja-drzwi-wewnetrznych', 'Ekspozycja drzwi', 'Grafitowe portale z drzwiami w salonie')], eager=True)}
</div></section>
{sub([('wewnetrzne', 'Wewnętrzne'), ('lazienkowe', 'Łazienkowe'), ('rewersyjne', 'Rewersyjne i ukryte'), ('szklane', 'Szklane'), ('przesuwne', 'Przesuwne'), ('mieszkania', 'Do mieszkań'), ('zewnetrzne', 'Zewnętrzne'), ('roznice', 'Różnice'), ('faq', 'Pytania')])}
<div class="wrap">{bl}</div>
<section class="sek sek-w" id="roznice" aria-labelledby="ro-h" style="scroll-margin-top:120px"><div class="wrap">
 <div class="naglowek" data-r><span class="etyk">Przylgowe, bezprzylgowe, rewersyjne</span><h2 id="ro-h">Czym różnią się drzwi wewnętrzne</h2></div>
 {tab}
</div></section>
<section class="sek" id="faq" aria-labelledby="fq-h" style="scroll-margin-top:120px"><div class="wrap">
 <div class="naglowek" data-r><h2 id="fq-h">Pytania o drzwi</h2></div>
 {faq_html(FAQ_D)}
 <div style="margin-top:56px">{cta_b(pre, 'Wybrałeś drzwi? Zmierzymy otwory', 'Pomiary i montaż: ' + TEL2 + '.')}</div>
</div></section>'''

# ================= REALIZACJE =================
KAT = [('salon', 'Salon'), ('wew', 'Wewnętrzne'), ('mie', 'Do mieszkań'), ('zew', 'Zewnętrzne'), ('prz', 'Przesuwne')]
MONT = ['drzwi-wewnetrzne-dab-czarna-oscieznica', 'drzwi-zewnetrzne-dwuskrzydlowe-antracyt', 'drzwi-szklane-loft-czarna-rama', 'drzwi-do-mieszkania-zloty-dab-intarsje',
        'drzwi-przesuwne-grafit-i-skrzydlowe', 'drzwi-wewnetrzne-dab-czarne-oscieznice-para', 'drzwi-zewnetrzne-czarne-cztery-szyby', 'drzwi-wewnetrzne-biale-czarne-oscieznice',
        'drzwi-dwuskrzydlowe-dab-czarna-rama-szprosy', 'drzwi-do-mieszkania-szary-dab-wizjer', 'drzwi-wewnetrzne-okleina-drewno-przeszklenia', 'drzwi-przesuwne-biale-przeszklone',
        'drzwi-zewnetrzne-ciemny-orzech-z-przeszkleniem', 'drzwi-wewnetrzne-biale-ramiakowe-glogow', 'drzwi-do-mieszkania-ciemne-z-aplikacja', 'drzwi-wewnetrzne-biale-trzy-frezy',
        'drzwi-wewnetrzne-biale-z-tulejami', 'drzwi-wewnetrzne-biale-frezowane-komplet', 'drzwi-wewnetrzne-biale-z-niebieskim-paskiem']
SALON = [f['slug'] for f in json.load(open('_src/salon.json', encoding='utf-8')) if f['slug'] != 'fachowiec-logo-salon']
WSZ = []
for i in range(max(len(MONT), len(SALON))):
    if i < len(MONT): WSZ.append(MONT[i])
    if i < len(SALON) and i % 2 == 0: WSZ.append(SALON[i])
WSZ += [s for s in SALON if s not in WSZ]

def realizacje(pre):
    ile = {k: sum(1 for s in WSZ if FOTO[s]['cat'] == k) for k, _ in KAT}
    bt = f'<button type="button" data-f="all" aria-pressed="true">Wszystkie<sup>{len(WSZ)}</sup></button>' + ''.join(f'<button type="button" data-f="{k}" aria-pressed="false">{n}<sup>{ile[k]}</sup></button>' for k, n in KAT)
    figs = ''.join(f'<figure data-k="{FOTO[s]["cat"]}" tabindex="0">{img(s, pre, "(max-width: 600px) 100vw, (max-width: 1100px) 50vw, 25vw", extra=f" data-full={chr(34)}{full(s, pre)}{chr(34)}")}<figcaption>{e(FOTO[s]["alt"])}</figcaption></figure>' for s in WSZ)
    ar = lambda p: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="{p}"/></svg>'
    return f'''
<section class="ph" aria-labelledby="h1"><div class="wrap">
 <div>{okr([('', 'Start'), ('realizacje/', 'Realizacje')], pre)}<h1 id="h1">Montaż drzwi w Głogowie – realizacje i salon</h1><p class="lead">{len(MONT)} montaży drzwi z Głogowa i okolic, sfotografowanych telefonem na budowie i w mieszkaniach klientów, oraz {len(SALON)} zdjęć ekspozycji w salonie.</p></div>
 {portal(pre, [('drzwi-wewnetrzne-dab-czarne-oscieznice-para', 'Po montażu', 'Drzwi w jasnym dębie z czarnymi ościeżnicami')], eager=True)}
</div></section>
<section class="sek" aria-label="Galeria" style="padding-top:clamp(40px,5vw,70px)"><div class="wrap">
 <div class="zakl" role="group" aria-label="Filtruj zdjęcia">{bt}</div>
 <div class="siatka">{figs}</div>
 <div style="margin-top:64px">{cta_b(pre, 'Chcesz takie drzwi u siebie?', 'Przyjdź do salonu albo zadzwoń – zaczniemy od pomiaru.')}</div>
</div></section>
<div class="lb" role="dialog" aria-modal="true" aria-label="Podgląd zdjęcia"><button class="pv" aria-label="Poprzednie">{ar('M15 5l-7 7 7 7')}</button><figure><img alt=""><figcaption></figcaption></figure><button class="nx" aria-label="Następne">{ar('M9 5l7 7-7 7')}</button><button class="x" aria-label="Zamknij">{ar('M6 6l12 12M18 6L6 18')}</button></div>'''

def realizacje_ld():
    u = BASE + 'realizacje/'
    return [{"@type": "ImageGallery", "@id": u + "#galeria", "name": "Realizacje i salon – Fachowiec Głogów", "url": u,
             "associatedMedia": [{"@type": "ImageObject", "contentUrl": BASE + full(s), "caption": FOTO[s]['alt']} for s in WSZ]}]

# ================= KONTAKT =================
def kontakt(pre):
    return f'''
<section class="ph" aria-labelledby="h1"><div class="wrap">
 <div>{okr([('', 'Start'), ('kontakt/', 'Kontakt')], pre)}<h1 id="h1">Salon przy ul. 1 Maja 16 w Głogowie</h1>{STATUS.replace(' fade', '')}<p class="lead">Wpadnij obejrzeć podłogi i drzwi na żywo albo zadzwoń i umów pomiar.</p></div>
 {portal(pre, [('salon-fachowiec-glogow-1-maja-16', 'Wejście do salonu', 'Witryna z logo Fachowiec, ul. 1 Maja 16')], eager=True)}
</div></section>
<section class="sek jasne" aria-label="Dane kontaktowe"><div class="wrap">
 <div class="kgrid">
  <div class="dane" data-r>
   <h2>Zadzwoń lub napisz</h2>
   <ul class="tl"><li><span>Sprzedaż i doradztwo</span><a href="tel:{TEL1H}">{TEL1}</a></li><li><span>Montaż i pomiary</span><a href="tel:{TEL2H}">{TEL2}</a></li><li><span>E-mail</span><a href="mailto:{MAIL}" style="font-size:clamp(20px,2vw,26px)">{MAIL}</a></li></ul>
   <h2 style="font-size:22px">Godziny otwarcia</h2>
   {GODZ}
   <address style="font-style:normal">Salon Fachowiec Głogów<br>ul. 1 Maja 16, 67-200 Głogów<br><a class="ul" href="https://www.google.com/maps/dir/?api=1&amp;destination=51.6681,16.0812" target="_blank" rel="noopener">Wyznacz trasę</a></address>
  </div>
  <div class="form" data-r="2">
   <h2>Skontaktuj się z nami</h2>
   <p style="color:var(--muted)">Napisz, czego potrzebujesz – odpowiemy w godzinach pracy salonu.</p>
   <form>
    <div class="p2"><div class="pole"><label for="f-n">Imię i nazwisko</label><input id="f-n" name="imie" autocomplete="name" required></div>
    <div class="pole"><label for="f-t">Telefon</label><input id="f-t" name="telefon" type="tel" autocomplete="tel" required></div></div>
    <div class="p2"><div class="pole"><label for="f-e">Adres e-mail</label><input id="f-e" name="email" type="email" autocomplete="email"></div>
    <div class="pole"><label for="f-s">Temat</label><select id="f-s" name="temat"><option>Podłogi</option><option>Drzwi wewnętrzne</option><option>Drzwi zewnętrzne</option><option>Panele ścienne</option><option>Deski tarasowe</option><option>Pomiar i montaż</option><option>Zamówienie wybranych produktów</option></select></div></div>
    <div class="pole"><label for="f-w">Wiadomość</label><textarea id="f-w" name="wiadomosc" placeholder="Np. 5 drzwi wewnętrznych i panele do 3 pokoi, Głogów"></textarea></div>
    <label class="zg"><input type="checkbox" required><span>Wyrażam zgodę na kontakt w sprawie zapytania. Administratorem danych jest ANTABA Artur Słubowski, prowadząca salon Fachowiec Głogów.</span></label>
    <button class="btn btn-or" type="submit">Wyślij wiadomość {I_STR}</button>
   </form>
   <p class="ok" role="status">Dziękujemy! To wersja pokazowa – po wdrożeniu wiadomość trafi na {MAIL}.</p>
  </div>
 </div>
 <div id="mapa" role="region" aria-label="Mapa dojazdu" style="margin-top:clamp(50px,7vw,90px)"></div>
 <div class="dojazd">
  <div data-r><h3>Salon</h3><p>ul. 1 Maja 16, 67-200 Głogów. Witryna z logo Fachowiec, wejście od ulicy.</p></div>
  <div data-r="2"><h3>Obszar montażu</h3><p>Głogów i okolice, m.in. Sława i Wschowa – województwa dolnośląskie, lubuskie i wielkopolskie.</p></div>
  <div data-r="3"><h3>Zamówienie bez wizyty</h3><p>Masz już wybrane produkty? Zamów je telefonicznie lub mailowo.</p></div>
 </div>
</div></section>'''

def nie_ma(pre):
    return f'<section class="ph"><div class="wrap" style="min-height:60vh"><div><h1 id="h1">Tej strony nie ma w salonie</h1><p class="lead">Adres nie istnieje albo się zmienił.</p><a class="btn btn-or" href="{BASE}">Strona główna</a></div></div></section>'

# ================= generowanie =================
page('', 'Podłogi i drzwi Głogów z montażem – salon Fachowiec, ul. 1 Maja 16', 'Salon Fachowiec w Głogowie: panele podłogowe, podłogi winylowe, panele ścienne, drzwi wewnętrzne i zewnętrzne. Doradztwo, pomiar, transport i montaż. Tel. 781 790 030.', start, leaflet=True)
page('podlogi-i-sciany/', 'Panele podłogowe Głogów – laminowane, winylowe, ścienne', 'Panele laminowane, podłogi winylowe LVT i drewniane, panele ścienne, deski tarasowe w Głogowie. Wzorniki w salonie przy ul. 1 Maja 16, doradztwo i montaż.', podlogi,
     crumbs=[('podlogi-i-sciany/', 'Podłogi i ściany')], extra_ld=[faq_ld(BASE + 'podlogi-i-sciany/', FAQ_P)])
page('drzwi/', 'Drzwi Głogów – wewnętrzne i zewnętrzne z montażem', 'Drzwi wewnętrzne, łazienkowe, przesuwne, do mieszkań i zewnętrzne w Głogowie. Ekspozycja DRE, Porta, Erkado. Pomiar i montaż od 2017 roku.', drzwi,
     crumbs=[('drzwi/', 'Drzwi')], extra_ld=[faq_ld(BASE + 'drzwi/', FAQ_D)])
page('realizacje/', 'Montaż drzwi Głogów – realizacje i zdjęcia salonu Fachowiec', 'Zdjęcia montażu drzwi w Głogowie i okolicach oraz ekspozycji salonu Fachowiec przy ul. 1 Maja 16.', realizacje,
     crumbs=[('realizacje/', 'Realizacje')], extra_ld=realizacje_ld())
page('kontakt/', 'Kontakt – salon Fachowiec Głogów, ul. 1 Maja 16', 'Salon Fachowiec, ul. 1 Maja 16, 67-200 Głogów. Pon.–pt. 9:00–17:00. Sprzedaż: 781 790 030, montaż i pomiary: 695 898 059.', kontakt,
     crumbs=[('kontakt/', 'Kontakt')], leaflet=True)
page('404/', 'Nie znaleziono strony – salon Fachowiec Głogów', 'Strona nie istnieje.', nie_ma)
s = open('404.html', encoding='utf-8').read()
for a in ['assets/', 'favicon.svg', 'kontakt/', 'podlogi-i-sciany/', 'drzwi/', 'realizacje/', 'img/']:
    s = s.replace(f'href="{a}', f'href="{BASE}{a}').replace(f'src="{a}', f'src="{BASE}{a}')
s = s.replace('href="./"', f'href="{BASE}"')
open('404.html', 'w', encoding='utf-8').write(s)

urls = ['', 'podlogi-i-sciany/', 'drzwi/', 'realizacje/', 'kontakt/']
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
for u in urls:
    ims = ''.join(f'<image:image><image:loc>{BASE}{full(x)}</image:loc></image:image>' for x in WSZ) if u == 'realizacje/' else ''
    sm += f'<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod>{ims}</url>\n'
open('sitemap.xml', 'w', encoding='utf-8').write(sm + '</urlset>\n')
open('robots.txt', 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
open('favicon.svg', 'w', encoding='utf-8').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="8" fill="#2a2e32"/><path d="M12 36V22L24 11l12 11v14" fill="none" stroke="#ea5b0b" stroke-width="4" stroke-linejoin="round"/></svg>')
print('ok', len(WSZ))
