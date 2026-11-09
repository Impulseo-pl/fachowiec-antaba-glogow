# Generator dema: Antaba – Salon Fachowiec Głogów. Uruchamiaj z katalogu repo: python _src/build.py
import json, os, html, datetime
BASE = 'https://impulseo-pl.github.io/fachowiec-antaba-glogow/'
TODAY = datetime.date.today().isoformat()
FOTO = {f['slug']: f for f in json.load(open('_src/foto.json', encoding='utf-8'))}
FOTO['deski-drewniane-poglad'] = dict(slug='deski-drewniane-poglad', cat='', alt='Drewniane deski w narożniku – zdjęcie poglądowe', w=1600, h=1182, sizes=[900, 1600])
LICZNIK = open('_src/licznik.js', encoding='utf-8').read().strip()
TEL1, TEL1H = '781 790 030', '+48781790030'
TEL2, TEL2H = '695 898 059', '+48695898059'
MAIL = 'aslubowski@wp.pl'
e = html.escape

def img(slug, pre, sizes='(max-width: 820px) 100vw, 50vw', eager=False, cls='', alt=None):
    f = FOTO[slug]
    src = ', '.join(f'{pre}img/{slug}-{s}.webp {s}w' for s in f['sizes'])
    mid = f['sizes'][min(1, len(f['sizes']) - 1)]
    h = round(f['h'] * mid / f['w'])
    a = e(alt if alt is not None else f['alt'])
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="{pre}img/{slug}-{mid}.webp" srcset="{src}" sizes="{sizes}" width="{mid}" height="{h}" alt="{a}" {load}>'

def full(slug, pre):
    f = FOTO[slug]; return f'{pre}img/{slug}-{f["sizes"][-1]}.webp'

LOGO = '''<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M15.5 37V11.5h17V37" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M16.3 12.3l10.4 3v23.2l-10.4-1.5z" fill="currentColor"/><circle cx="24.6" cy="26" r=".9" fill="#111c44"/></svg>'''
I_TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
I_OK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg>'
I_STR = '<svg class="str" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'

NAV = [('', 'Start'), ('drzwi/', 'Drzwi'), ('podlogi-i-sciany/', 'Podłogi i ściany'), ('realizacje/', 'Realizacje'), ('kontakt/', 'Kontakt')]

FIRMA = {
    "@type": ["HomeAndConstructionBusiness", "Store"], "@id": BASE + "#firma",
    "name": "Fachowiec Antaba – salon drzwi i podłóg w Głogowie",
    "alternateName": ["Antaba Głogów", "Salon Fachowiec Głogów", "ANTABA Artur Słubowski"],
    "legalName": "ANTABA Artur Słubowski", "founder": {"@type": "Person", "name": "Artur Słubowski"},
    "foundingDate": "2017", "taxID": "6931112891", "url": BASE, "logo": BASE + "favicon.svg", "image": BASE + "og.jpg",
    "telephone": TEL1H, "email": MAIL,
    "description": "Salon drzwi, podłóg i paneli ściennych w Głogowie. Sprzedaż z pomiarem, transportem i montażem drzwi wewnętrznych, zewnętrznych, przesuwnych i do mieszkań.",
    "address": {"@type": "PostalAddress", "streetAddress": "ul. 1 Maja 16", "postalCode": "67-200", "addressLocality": "Głogów", "addressRegion": "dolnośląskie", "addressCountry": "PL"},
    "geo": {"@type": "GeoCoordinates", "latitude": 51.6681, "longitude": 16.0812},
    "hasMap": "https://www.openstreetmap.org/?mlat=51.6681&mlon=16.0812#map=18/51.6681/16.0812",
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"}],
    "areaServed": [{"@type": "City", "name": "Głogów"}, {"@type": "City", "name": "Sława"}, {"@type": "City", "name": "Wschowa"},
                   {"@type": "State", "name": "dolnośląskie"}, {"@type": "State", "name": "lubuskie"}, {"@type": "State", "name": "wielkopolskie"}],
    "contactPoint": [{"@type": "ContactPoint", "telephone": TEL1H, "contactType": "sales", "availableLanguage": "pl"},
                     {"@type": "ContactPoint", "telephone": TEL2H, "contactType": "customer service", "description": "Montaż i pomiary", "availableLanguage": "pl"}],
    "sameAs": ["https://www.facebook.com/p/Antaba-100055216734311/", "https://www.oferteo.pl/antaba-artur-slubowski/firma/2932520", "https://grupafachowiec.eu/salon/glogow/"],
    "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
                   ["Montaż drzwi wewnętrznych", "Montaż drzwi zewnętrznych", "Montaż drzwi wejściowych do mieszkań", "Montaż systemów drzwi przesuwnych", "Pomiar otworów drzwiowych", "Transport zakupionych produktów", "Montaż paneli podłogowych"]],
    "paymentAccepted": "Gotówka, przelew", "currenciesAccepted": "PLN",
}

def ld(page_url, title, desc, crumbs, extra=None):
    g = [FIRMA,
         {"@type": "WebSite", "@id": BASE + "#strona", "url": BASE, "name": "Fachowiec Antaba Głogów", "inLanguage": "pl-PL", "publisher": {"@id": BASE + "#firma"}},
         {"@type": "WebPage", "@id": page_url + "#webpage", "url": page_url, "name": title, "description": desc, "inLanguage": "pl-PL",
          "isPartOf": {"@id": BASE + "#strona"}, "about": {"@id": BASE + "#firma"}, "dateModified": TODAY, "primaryImageOfPage": BASE + "og.jpg"}]
    if crumbs:
        g.append({"@type": "BreadcrumbList", "@id": page_url + "#okruszki", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (u, n) in enumerate(crumbs)]})
    if extra: g += extra
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False) + '</script>'

def faq_ld(page_url, items):
    return {"@type": "FAQPage", "@id": page_url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def faq_html(items):
    out = ''.join(f'<details><summary>{e(q)}<i aria-hidden="true"></i></summary><div class="odp"><p>{e(a)}</p></div></details>' for q, a in items)
    return f'<div class="faq" data-r>{out}</div>'

def crumbs_html(crumbs, pre):
    li = []
    for i, (u, n) in enumerate(crumbs):
        if i == len(crumbs) - 1: li.append(f'<li aria-current="page">{e(n)}</li>')
        else: li.append(f'<li><a href="{(pre + u) or "./"}">{e(n)}</a></li>')
    return f'<nav class="okruszki fade" aria-label="Okruszki"><ol>{"".join(li)}</ol></nav>'

def lines(*ls):
    return ''.join(f'<span class="ln"><span class="ln-i">{l}</span></span>' for l in ls)

def page(path, title, desc, body, crumbs=None, extra_ld=None, home=False, leaflet=False, og_img='og.jpg'):
    depth = path.count('/')
    pre = '' if path == '404/' else '../' * depth
    L = lambda u: (pre + u) or './'
    url = BASE + path
    nav = ''.join(f'<a href="{L(u)}"{" aria-current=page" if u == path else ""}>{n}</a>' for u, n in NAV)
    mnav = ''.join(f'<a href="{L(u)}">{n}</a>' for u, n in NAV)
    intro = '''<div class="intro" aria-hidden="true"><div class="intro-in"><svg viewBox="0 0 120 120"><circle class="ok" cx="60" cy="60" r="54"/><path class="oscieznica" d="M38 92V28h44v64"/><rect class="skr" x="39.4" y="29.4" width="41.2" height="62.6"/></svg><div class="napis">ANTABA</div><div class="napis2">Salon Fachowiec · Głogów</div></div></div>''' if home else ''
    lf_css = '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="">' if leaflet else ''
    lf_js = '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>' if leaflet else ''
    intro_script = '<script>document.documentElement.classList.add("js");try{if(sessionStorage.getItem("an_intro")||matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.remove("intro-on")}catch(e){}</script>'
    crumbs_ld = [('', 'Start')] + (crumbs or []) if crumbs else None
    doc = f'''<!DOCTYPE html>
<html lang="pl"{' class="intro-on"' if home else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:locale" content="pl_PL"><meta property="og:site_name" content="Fachowiec Antaba Głogów">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="PL-DS"><meta name="geo.placename" content="Głogów"><meta name="geo.position" content="51.6681;16.0812">
<meta name="theme-color" content="#111c44">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@500;600;700&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/styles.css">{lf_css}
{intro_script}
<script>{LICZNIK}</script>
{ld(url, title, desc, crumbs_ld, extra_ld)}
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
{intro}<div class="kurtyna" aria-hidden="true"></div>
<header class="top">
 <div class="wrap">
  <a class="logo" href="{pre or './'}" aria-label="Fachowiec Antaba – strona główna">{LOGO}<span><b>ANTABA</b><small>Salon Fachowiec · Głogów</small></span></a>
  <nav class="nav" aria-label="Menu główne">{nav}</nav>
  <a class="tel" href="tel:{TEL1H}">{I_TEL}{TEL1}</a>
  <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="mmenu"><span></span><span></span><span></span></button>
 </div>
</header>
<nav class="mmenu" id="mmenu" aria-label="Menu mobilne">{mnav}<div class="mm-kontakt">Sprzedaż i doradztwo<a href="tel:{TEL1H}">{TEL1}</a></div></nav>
<main id="tresc">
{body(pre)}
</main>
<footer class="stopka">
 <div class="wrap">
  <div>
   <a class="logo" href="{pre or './'}">{LOGO}<span><b>ANTABA</b><small>Salon Fachowiec · Głogów</small></span></a>
   <p>Drzwi, podłogi i panele ścienne z pomiarem, transportem i montażem. Montujemy drzwi od 2017 roku.</p>
  </div>
  <div><h2>Salon</h2><address>ul. 1 Maja 16<br>67-200 Głogów<br><br>Pon.–pt. 9:00–17:00<br>Sob.–niedz. nieczynne</address></div>
  <div><h2>Kontakt</h2><ul><li>Sprzedaż: <a href="tel:{TEL1H}">{TEL1}</a></li><li>Montaż i pomiary: <a href="tel:{TEL2H}">{TEL2}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="https://www.facebook.com/p/Antaba-100055216734311/" rel="noopener" target="_blank">Facebook</a></li></ul></div>
  <div><h2>Strona</h2><ul>{''.join(f'<li><a href="{L(u)}">{n}</a></li>' for u, n in NAV)}</ul></div>
  <div class="marka" aria-hidden="true">ANTABA</div>
  <div class="dol"><span>ANTABA Artur Słubowski · NIP 693-111-28-91 · salon partnerski Grupy Fachowiec</span><span>© {datetime.date.today().year} Fachowiec Antaba Głogów</span></div>
 </div>
</footer>
<div class="kom-cta"><a class="btn btn-red" href="tel:{TEL1H}">{I_TEL}Zadzwoń</a><a class="btn btn-line" style="background:var(--navy)" href="{pre}kontakt/">Umów pomiar</a></div>
{lf_js}<script src="{pre}assets/lenis.min.js" defer></script><script src="{pre}assets/app.js" defer></script>
</body>
</html>
'''
    out = path + 'index.html' if path else 'index.html'
    if path == '404/': out = '404.html'
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    open(out, 'w', encoding='utf-8').write(doc)

# ---------------- treści wspólne ----------------
OPINIE = [
    ('A. I.', '2018', 'Usługa wykonana perfekcyjnie – doradztwo, wybór, uzgodniony czas wykonania usługi, fachowość, ceny przyzwoite, duży wybór, fachowa obsługa. Ja i moja żona jesteśmy zadowoleni w 110%. Polecam.'),
    ('T.', '2024', 'Super doradztwo, bardzo miła Pani, kompetentna. Duży wybór drzwi, super montażyści, fachowo podchodzą do swojej pracy. Wykonanie na 5+, bez uwag. Bardzo polecam, solidna firma.'),
    ('K. T.', '2019', 'Termin założony przez firmę był naprawdę bardzo szybki, a jakość oraz podejście do wykonania powierzonych prac były profesjonalne. Uczciwość oraz fachowość – tak mogę opisać tę firmę.'),
]

def opinie_html():
    k = ''.join(f'<figure class="op" data-r="{i+1}"><div class="gw" aria-label="5 na 5">★★★★★</div><blockquote>„{e(t)}”</blockquote><figcaption class="kto">{e(a)} · opinia na Oferteo, {r}</figcaption></figure>' for i, (a, r, t) in enumerate(OPINIE))
    return f'<div class="opinie">{k}</div><p class="op-zrodlo" data-r>Średnia 5,0 z 7 opinii na <a class="link" href="https://www.oferteo.pl/antaba-artur-slubowski/firma/2932520" rel="noopener" target="_blank">Oferteo</a>.</p>'

def pas_html(pre):
    return f'''<section class="pas ciemna" aria-labelledby="pas-h">
 <div class="wrap">
  <div data-r><h2 id="pas-h">Umów pomiar albo wpadnij do salonu</h2><p class="lead">Najpierw zobacz drzwi i podłogi na żywo, potem przyjedziemy zmierzyć otwory i ustalimy termin montażu.</p>
   <a class="wielki-tel" href="tel:{TEL1H}">{TEL1}</a><br><a class="btn btn-red" href="{pre}kontakt/">Napisz do nas</a></div>
  <dl data-r="2"><dt>Salon</dt><dd>ul. 1 Maja 16, 67-200 Głogów</dd><dt>Godziny</dt><dd>pon.–pt. 9:00–17:00</dd><dt>Montaż i pomiary</dt><dd><a href="tel:{TEL2H}">{TEL2}</a></dd><dt>E-mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></dl>
 </div>
</section>'''

def cta_pas(pre, h, p):
    return f'<div class="cta-pas" data-r><div><h2>{h}</h2><p>{p}</p></div><div class="cta"><a class="btn btn-red" href="tel:{TEL1H}">{I_TEL}{TEL1}</a><a class="btn btn-line" href="{pre}kontakt/">Umów pomiar</a></div></div>'

# ---------------- START ----------------
TYPY = [
    ('drzwi-wewnetrzne-biale-czarne-oscieznice', 'Drzwi wewnętrzne', ['przylgowe', 'bezprzylgowe', 'z ościeżnicą regulowaną'], 'Do pokoi, łazienki i kuchni. Gładkie, frezowane albo z przeszkleniem, w bieli, okleinie drewnopodobnej lub z czarną ościeżnicą. Dobierzemy kolor do podłogi, którą wybierzesz w tym samym salonie.', 'wewnetrzne'),
    ('drzwi-wewnetrzne-biale-trzy-frezy', 'Rewersyjne, ukryte i łamane', ['rewersyjne', 'ukryte', 'łamane'], 'Kiedy drzwi mają zniknąć w ścianie albo zmieścić się tam, gdzie zwykłe skrzydło przeszkadza. To modele, przy których precyzyjny pomiar i montaż decydują o efekcie.', 'rewersyjne'),
    ('drzwi-szklane-loft-czarna-rama', 'Drzwi szklane', ['całoszklane', 'w ramie ze szprosami', 'styl loft'], 'Doświetlą ciemny przedpokój i oddzielą kuchnię bez zamykania przestrzeni. Szkło w czarnej ramie pasuje do jasnego dębu i surowych ścian.', 'szklane'),
    ('drzwi-przesuwne-grafit-i-skrzydlowe', 'Systemy przesuwne', ['naścienne', 'chowane w ścianie', 'do garderoby'], 'Skrzydło jedzie wzdłuż ściany zamiast otwierać się w pokój. Dobre do garderoby, małej łazienki i między salonem a kuchnią.', 'przesuwne'),
    ('drzwi-do-mieszkania-zloty-dab-intarsje', 'Drzwi do mieszkań', ['do bloku', 'z wizjerem', 'z wyciszeniem'], 'Wejściowe do mieszkania w bloku, dobrane do wymiaru otworu i drzwi wewnętrznych. Montaż po pomiarze.', 'mieszkania'),
    ('drzwi-zewnetrzne-czarne-cztery-szyby', 'Drzwi zewnętrzne do domów', ['jedno- i dwuskrzydłowe', 'z przeszkleniem', 'ocieplane'], 'Do nowego domu i do wymiany. Osadzamy je w stanie surowym albo w wykończonej elewacji, z pianką, taśmami i regulacją okuć.', 'zewnetrzne'),
]

def start(pre):
    tryp = [('drzwi-wewnetrzne-dab-czarna-oscieznica', 'Dąb i czarna ościeżnica'), ('drzwi-zewnetrzne-dwuskrzydlowe-antracyt', 'Drzwi zewnętrzne, dom jednorodzinny'), ('drzwi-szklane-loft-czarna-rama', 'Szkło w ramie, styl loft')]
    tr = ''.join(f'<figure class="drzwi">{img(s, pre, "(max-width: 560px) 50vw, 22vw", eager=(i == 0))}<div class="skrz" aria-hidden="true"></div><figcaption>{c}</figcaption></figure>' for i, (s, c) in enumerate(tryp))
    typy_fot = ''.join(img(s, pre, '45vw', alt=FOTO[s]['alt']).replace('<img ', f'<img data-podpis="{e(FOTO[s]["alt"])}" ') for s, *_ in TYPY)
    typy = ''.join(f'''<article class="typ">{img(s, pre, '100vw', cls='mfot')}<h3>{h}</h3><ul class="rodz">{''.join(f'<li>{x}</li>' for x in rodz)}</ul><p>{t}</p><a class="link" href="{pre}drzwi/#{a}">Więcej o tym rodzaju</a></article>''' for s, h, rodz, t, a in TYPY)
    gal = ['drzwi-dwuskrzydlowe-dab-czarna-rama-szprosy', 'drzwi-zewnetrzne-ciemny-orzech-z-przeszkleniem', 'drzwi-wewnetrzne-dab-czarne-oscieznice-para', 'drzwi-do-mieszkania-szary-dab-wizjer', 'drzwi-przesuwne-biale-przeszklone', 'drzwi-wewnetrzne-biale-ramiakowe-glogow', 'drzwi-wewnetrzne-okleina-drewno-przeszklenia', 'drzwi-do-mieszkania-ciemne-z-aplikacja', 'drzwi-wewnetrzne-biale-z-tulejami']
    tor = ''.join(f'<figure>{img(s, pre, "30vw")}<figcaption>{e(FOTO[s]["alt"])}</figcaption></figure>' for s in gal)
    mats = [('Panele laminowane', 'Twarde, odporne na ścieranie, w dekorach drewna i kamienia. Rozsądny wybór do salonu i sypialni.', 'laminowane'),
            ('Panele winylowe', 'Cieplejsze w dotyku i cichsze. Sprawdzają się w kuchni i przedpokoju – przy wilgoci zawsze patrzymy na parametry modelu.', 'winylowe'),
            ('Podłogi drewniane', 'Deska z naturalnego drewna na lata. Pokażemy próbki, żeby ocenić usłojenie i kolor w świetle dziennym.', 'drewniane'),
            ('Panele ścienne', 'Ściana za łóżkiem, telewizorem albo w przedpokoju bez kucia i tynkowania.', 'scienne'),
            ('Deski tarasowe', 'Kompozytowe i drewniane, z legarami i akcesoriami montażowymi.', 'tarasowe')]
    mat = ''.join(f'<li><a href="{pre}podlogi-i-sciany/#{a}"><h3>{h}</h3>{I_STR}<p>{t}</p></a></li>' for h, t, a in mats)
    return f'''
<section class="hero" aria-labelledby="h1">
 <div class="wrap">
  <div>
   <p class="gdzie fade">{I_PIN}Salon Fachowiec Antaba · ul. 1 Maja 16, Głogów</p>
   <h1 id="h1">{lines('Drzwi i podłogi', 'w Głogowie', 'z montażem')}</h1>
   <p class="lead fade">Wybierasz w salonie, my mierzymy, przywozimy i montujemy. Drzwi wewnętrzne, zewnętrzne, przesuwne i do mieszkań, panele podłogowe i ścienne.</p>
   <div class="cta fade f2"><a class="btn btn-red" href="{pre}kontakt/">Umów pomiar</a><a class="btn btn-line" href="tel:{TEL1H}">{I_TEL}{TEL1}</a></div>
  </div>
  <div class="tryptyk">{tr}</div>
 </div>
 <div class="fakty"><ul>
  <li><b>Montujemy od 2017 roku</b>drzwi wewnętrzne, zewnętrzne i do mieszkań</li>
  <li><b>Pomiar, transport, montaż</b>jedna firma od wyboru do regulacji</li>
  <li><b>5,0 na Oferteo</b>7 opinii klientów</li>
  <li><b>Dojeżdżamy</b>dolnośląskie, lubuskie, wielkopolskie</li>
 </ul></div>
</section>

<section class="sek" aria-labelledby="salon-h">
 <div class="wrap salon">
  <figure class="fot odslon" style="margin:0">{img('drzwi-dwuskrzydlowe-dab-czarna-rama-szprosy', pre, '(max-width: 820px) 100vw, 42vw')}</figure>
  <div>
   <h2 id="salon-h" class="ln-wrap">{lines('Jeden salon,', 'cały komplet')}</h2>
   <p class="lead" data-r>Drzwi i podłoga to jedna aranżacja. U nas dobierzesz je obok siebie, na żywo, zamiast zgadywać odcień ze zdjęcia w internecie.</p>
   <ul data-r="2">
    <li>{I_OK}<span>Doradca pomoże wybrać model, kolor i kierunek otwierania</span></li>
    <li>{I_OK}<span>Próbki podłóg i okleiny drzwi do porównania w salonie</span></li>
    <li>{I_OK}<span>Pomiar otworów przed zamówieniem, żeby nic nie trzeba było docinać na siłę</span></li>
    <li>{I_OK}<span>Transport i montaż przez naszą ekipę</span></li>
   </ul>
   <a class="btn btn-dark" href="{pre}drzwi/" data-r="3">Zobacz ofertę drzwi</a>
  </div>
 </div>
</section>

<section class="sek sek-n ciemna" aria-labelledby="typy-h">
 <div class="wrap">
  <div class="glowa"><h2 id="typy-h" class="ln-wrap">{lines('Jakie drzwi', 'montujemy')}</h2><p class="lead" data-r>Sprzedajemy i montujemy drzwi od 2017 roku. Na zdjęciach nasze realizacje z Głogowa i okolic.</p></div>
  <div class="typy">
   <div class="typy-fot" aria-hidden="true">{typy_fot}<span class="lic"></span></div>
   <div>{typy}</div>
  </div>
 </div>
</section>

<section class="sek sek-o" aria-labelledby="mat-h">
 <div class="wrap mat">
  <div class="fot odslon">{img('deski-drewniane-poglad', pre, '(max-width: 820px) 100vw, 45vw', alt='Drewniane deski – zdjęcie poglądowe')}<small>Zdjęcie poglądowe</small></div>
  <div>
   <h2 id="mat-h" class="ln-wrap">{lines('Podłogi, ściany', 'i tarasy')}</h2>
   <p class="lead" data-r>Laminat, winyl czy drewno? Odpowiedź zależy od pomieszczenia, ogrzewania podłogowego i tego, kto po niej chodzi. Przyjdź z wymiarami, doradzimy.</p>
   <ul class="lista" data-r="2">{mat}</ul>
  </div>
 </div>
</section>

<section class="sek sek-b" aria-labelledby="proc-h">
 <div class="wrap">
  <div class="glowa"><h2 id="proc-h" class="ln-wrap">{lines('Od wyboru', 'do klamki')}</h2><p class="lead" data-r>Prowadzimy całą realizację. Nie musisz szukać osobno sklepu, transportu i montażysty.</p></div>
  <div class="proces"><div class="pasek"></div>
   <div class="krok" data-r><span class="kto">W salonie</span><h3>Doradztwo i próbki</h3><p>Oglądasz drzwi i podłogi na żywo, porównujesz okleiny i dekory, wybierasz z doradcą.</p></div>
   <div class="krok" data-r="2"><span class="kto">U Ciebie</span><h3>Pomiar</h3><p>Mierzymy otwory i sprawdzamy ściany, zanim cokolwiek zamówimy.</p></div>
   <div class="krok" data-r="3"><span class="kto">Dowozimy</span><h3>Transport</h3><p>Przywozimy zakupiony towar pod wskazany adres.</p></div>
   <div class="krok" data-r="4"><span class="kto">Montujemy</span><h3>Montaż i regulacja</h3><p>Osadzamy ościeżnice, wieszamy skrzydła i regulujemy okucia.</p></div>
  </div>
 </div>
</section>

<section class="poziom" aria-labelledby="gal-h">
 <div class="poziom-in">
  <div class="wrap"><div class="glowa"><h2 id="gal-h" class="ln-wrap">{lines('Nasze realizacje')}</h2><p class="lead" data-r>Zdjęcia prosto z montażu – czasem jeszcze z folią na skrzydle i pianką przy ościeżnicy.</p></div></div>
  <div class="tor">{tor}<div class="koniec"><h3>Zobacz wszystkie montaże</h3><p>Drzwi wewnętrzne, zewnętrzne, przesuwne i do mieszkań – z podziałem na rodzaje.</p><a class="btn btn-dark" href="{pre}realizacje/">Galeria realizacji</a></div></div>
 </div>
</section>

<section class="sek" aria-labelledby="op-h">
 <div class="wrap">
  <div class="glowa"><h2 id="op-h" class="ln-wrap">{lines('Co mówią klienci')}</h2><p class="lead" data-r>Opinie z Oferteo, gdzie jesteśmy od 2017 roku. Przytaczamy je bez skrótów.</p></div>
  {opinie_html()}
 </div>
</section>
{pas_html(pre)}'''

# ---------------- DRZWI ----------------
FAQ_D = [
    ('Co to znaczy, że drzwi są bezprzylgowe?', 'Skrzydło drzwi bezprzylgowych po zamknięciu licuje z ościeżnicą – nie ma wystającego zakładu (przylgi), a zawiasy są ukryte. Drzwi wyglądają gładko i nowocześnie. Przylgowe mają zakład, który nachodzi na ościeżnicę, i widoczne zawiasy.'),
    ('Drzwi przylgowe czy bezprzylgowe – co wybrać?', 'Przylgowe są prostsze i zwykle tańsze, dobrze sprawdzają się w klasycznych wnętrzach. Bezprzylgowe dają gładką, jednolitą płaszczyznę i pasują do nowoczesnych aranżacji. W salonie zobaczysz oba rozwiązania obok siebie i porównasz je na żywo.'),
    ('Czym są drzwi rewersyjne?', 'To drzwi montowane odwrotnie niż standardowe: skrzydło otwiera się do wnętrza ościeżnicy, a od strony otwierania licuje ze ścianą. Ościeżnica jest schowana, więc z jednej strony widać tylko gładkie skrzydło.'),
    ('Czy przed zamówieniem robicie pomiar?', 'Tak. Montaż poprzedzamy pomiarem otworów u klienta. Dzięki temu zamawiamy właściwe wymiary skrzydeł i ościeżnic, a na montażu nie ma niespodzianek.'),
    ('Czy montujecie drzwi kupione w innym sklepie?', 'Pomiar, transport i montaż wykonujemy dla produktów kupionych w naszym salonie. Wtedy odpowiadamy za całość – od wyboru modelu po regulację okuć.'),
    ('Czy dojeżdżacie poza Głogów?', 'Tak. Pracujemy w województwach dolnośląskim, lubuskim i wielkopolskim, m.in. w Sławie i Wschowie. Zadzwoń, a potwierdzimy dojazd do Twojej miejscowości.'),
    ('Czy mogę zamówić drzwi przez telefon?', 'Jeśli byłeś już w salonie i masz wybrane produkty, możesz zamówić je telefonicznie lub mailowo, bez ponownej wizyty.'),
]

def drzwi(pre):
    def rzad(anchor, h, txt, pkt, fots, odwr=False):
        f = ''.join(f'<figure class="odslon">{img(s, pre, "(max-width: 820px) 50vw, 24vw")}<figcaption>{e(FOTO[s]["alt"])}</figcaption></figure>' for s in fots)
        p = ''.join(f'<li>{x}</li>' for x in pkt)
        one = ' jedno' if len(fots) == 1 else ''
        return f'<section class="rzad{" odwr" if odwr else ""}" id="{anchor}" aria-labelledby="{anchor}-h"><div><h2 id="{anchor}-h" class="ln-wrap">{h}</h2><div data-r>{txt}</div><ul class="pkt" data-r="2">{p}</ul></div><div class="fots{one}">{f}</div></section>'
    rz = ''.join([
        rzad('wewnetrzne', lines('Drzwi wewnętrzne', 'w Głogowie'), '<p>Do pokoi, łazienki i kuchni: gładkie, frezowane, ramiakowe i z przeszkleniem. W bieli, okleinach drewnopodobnych, w szarościach i z czarną ościeżnicą.</p>',
             ['Przylgowe i bezprzylgowe', 'Ościeżnice regulowane i stałe', 'Tuleje lub podcięcie wentylacyjne do łazienki', 'Klamki, zamki i wkładki do kompletu'], ['drzwi-wewnetrzne-dab-czarna-oscieznica', 'drzwi-wewnetrzne-biale-frezowane-komplet']),
        rzad('rewersyjne', lines('Rewersyjne, ukryte', 'i łamane'), '<p>Drzwi, które mają zlewać się ze ścianą albo zmieścić tam, gdzie zwykłe skrzydło blokuje przejście. Przy tych modelach o efekcie decydują milimetry, dlatego zawsze zaczynamy od pomiaru.</p>',
             ['Rewersyjne – skrzydło licuje ze ścianą', 'Ukryte – do pomalowania na kolor ściany', 'Łamane – do wąskich korytarzy i spiżarni'], ['drzwi-wewnetrzne-biale-trzy-frezy', 'drzwi-wewnetrzne-biale-z-niebieskim-paskiem'], True),
        rzad('szklane', lines('Drzwi szklane', 'i loftowe'), '<p>Szkło w czarnej ramie ze szprosami doświetla przedpokój i oddziela kuchnię, nie zamykając przestrzeni. Pasuje do jasnego dębu, betonu i białych ścian.</p>',
             ['Skrzydła całoszklane', 'Rama ze szprosami w stylu loft', 'Szkło przezroczyste i matowe'], ['drzwi-szklane-loft-czarna-rama', 'drzwi-dwuskrzydlowe-dab-czarna-rama-szprosy']),
        rzad('przesuwne', lines('Drzwi przesuwne', 'i systemy przesuwne'), '<p>Skrzydło przesuwa się wzdłuż ściany albo chowa w niej, zamiast otwierać się w pokój. Rozwiązanie do garderoby, małej łazienki i między salonem a kuchnią.</p>',
             ['Systemy naścienne z widoczną szyną', 'Kasety chowane w ścianie', 'Skrzydła pełne i przeszklone'], ['drzwi-przesuwne-grafit-i-skrzydlowe', 'drzwi-przesuwne-biale-przeszklone'], True),
        rzad('mieszkania', lines('Drzwi do mieszkania', 'w bloku z montażem'), '<p>Wymiana drzwi wejściowych w bloku to zwykle wymiana całego kompletu z ościeżnicą. Pomożemy dobrać model z odpowiednią izolacją akustyczną i klasą zabezpieczeń, a nasza ekipa go zamontuje.</p>',
             ['Wizjer, zamki i wkładki o podwyższonej klasie', 'Wyciszenie od klatki schodowej', 'Kolory pasujące do drzwi wewnętrznych'], ['drzwi-do-mieszkania-zloty-dab-intarsje', 'drzwi-do-mieszkania-szary-dab-wizjer']),
        rzad('zewnetrzne', lines('Drzwi zewnętrzne', 'z montażem'), '<p>Do nowego domu i do wymiany starych. Jedno- i dwuskrzydłowe, z przeszkleniem, długim pochwytem albo klasyczne. Osadzamy je w stanie surowym albo w wykończonej elewacji.</p>',
             ['Drzwi ocieplane do domów jednorodzinnych', 'Modele dwuskrzydłowe i z doświetlem', 'Montaż z pianką, taśmami i regulacją okuć'], ['drzwi-zewnetrzne-dwuskrzydlowe-antracyt', 'drzwi-zewnetrzne-czarne-cztery-szyby'], True),
    ])
    tab = '''<div class="tab-wrap" data-r><table class="por"><caption class="sr" style="position:absolute;left:-9999px">Porównanie rodzajów drzwi wewnętrznych</caption>
<thead><tr><th scope="col">Rodzaj</th><th scope="col">Jak wygląda</th><th scope="col">Zawiasy</th><th scope="col">Kiedy wybrać</th></tr></thead><tbody>
<tr><th scope="row">Przylgowe</th><td>Skrzydło nachodzi zakładem na ościeżnicę</td><td>Widoczne</td><td>Klasyczne wnętrza, rozsądny budżet</td></tr>
<tr><th scope="row">Bezprzylgowe</th><td>Skrzydło licuje z ościeżnicą, gładka płaszczyzna</td><td>Ukryte</td><td>Nowoczesne aranżacje, minimalizm</td></tr>
<tr><th scope="row">Rewersyjne</th><td>Od strony otwierania skrzydło licuje ze ścianą</td><td>Ukryte</td><td>Gdy ościeżnica ma zniknąć z jednej strony</td></tr>
<tr><th scope="row">Ukryte</th><td>Skrzydło zlicowane ze ścianą, do malowania</td><td>Ukryte</td><td>Drzwi niewidoczne w ścianie</td></tr>
<tr><th scope="row">Przesuwne</th><td>Skrzydło jedzie po szynie lub chowa się w ścianie</td><td>Brak – wózki i prowadnica</td><td>Mało miejsca na otwieranie skrzydła</td></tr>
</tbody></table></div><p class="tab-nota" data-r>Nie wiesz, który rodzaj pasuje do Twojego mieszkania? Przyjdź do salonu przy ul. 1 Maja 16 – pokażemy je obok siebie.</p>'''
    return f'''
<section class="phero ciemna" aria-labelledby="h1">
 <div class="wrap">
  <div>{crumbs_html([('', 'Start'), ('drzwi/', 'Drzwi')], pre)}<h1 id="h1">{lines('Drzwi w Głogowie', 'z pomiarem i montażem')}</h1></div>
  <div class="side fade"><p class="lead">Wewnętrzne, zewnętrzne, przesuwne i do mieszkań. Sprzedajemy, mierzymy, przywozimy i montujemy – od 2017 roku.</p><a class="btn btn-red" href="{pre}kontakt/">Umów pomiar</a></div>
 </div>
</section>
<div class="sek" style="padding-top:clamp(30px,4vw,60px)"><div class="wrap">{rz}</div></div>
<section class="sek sek-b" aria-labelledby="por-h"><div class="wrap">
 <div class="glowa"><h2 id="por-h" class="ln-wrap">{lines('Przylgowe, bezprzylgowe,', 'rewersyjne – różnice')}</h2><p class="lead" data-r>Najczęstsze pytanie w salonie. Tak wyglądają różnice w skrócie.</p></div>
 {tab}
</div></section>
<section class="sek" aria-labelledby="faq-h"><div class="wrap">
 <div class="glowa"><h2 id="faq-h" class="ln-wrap">{lines('Pytania o drzwi')}</h2><p class="lead" data-r>Odpowiedzi na to, o co klienci pytają nas przy ladzie i przez telefon.</p></div>
 {faq_html(FAQ_D)}
 <div style="margin-top:60px">{cta_pas(pre, 'Wybrałeś drzwi? Zmierzymy otwory', 'Zadzwoń albo napisz – ustalimy termin pomiaru.')}</div>
</div></section>'''

# ---------------- PODŁOGI ----------------
FAQ_P = [
    ('Panele winylowe czy laminowane – które lepsze?', 'To zależy od pomieszczenia. Laminat jest twardy i odporny na ścieranie, dobry do salonu i sypialni. Winyl jest cieplejszy w dotyku, cichszy i lepiej znosi wilgoć, dlatego częściej trafia do kuchni i przedpokoju. W salonie porównasz je na próbkach.'),
    ('Jakie panele na ogrzewanie podłogowe?', 'Na ogrzewanie podłogowe nadają się zarówno panele laminowane, jak i winylowe, jeśli producent dopuszcza taki montaż. Sprawdzamy to w parametrach konkretnego modelu i dobieramy właściwy podkład.'),
    ('Panele winylowe czy laminowane do kuchni?', 'Do kuchni częściej polecamy winyl, bo lepiej znosi wilgoć i rozlane płyny. Przy każdym modelu sprawdzamy jednak, czy producent dopuszcza go do pomieszczeń o podwyższonej wilgotności.'),
    ('Czy mogę zobaczyć próbki przed zakupem?', 'Tak. W salonie przy ul. 1 Maja 16 są próbki podłóg i paneli. Odcień, struktura i połysk wyglądają na żywo inaczej niż na zdjęciu, więc warto je porównać w dziennym świetle.'),
    ('Czy montujecie panele podłogowe?', 'Tak, oferujemy montaż podłóg. Zapytaj doradcę w salonie lub zadzwoń – ustalimy pomiar pomieszczeń i termin układania.'),
]

def podlogi(pre):
    poz = [
        ('laminowane', 'Panele laminowane', 'Twarda warstwa wierzchnia, odporność na ścieranie i duży wybór dekorów: dąb w wielu odcieniach, jesion, kamień i beton. Dobry wybór do salonu, sypialni i pokoju dziecka.', ['Dekory drewna i kamienia', 'Różne klasy ścieralności', 'Podkłady i listwy do kompletu']),
        ('winylowe', 'Panele winylowe', 'Cieplejsze w dotyku i cichsze od laminatu. Lepiej znoszą wilgoć, dlatego trafiają do kuchni, przedpokoju i na poddasza. Przy łazience zawsze sprawdzamy przeznaczenie konkretnego modelu.', ['Wersje klejone i na zatrzask', 'Do ogrzewania podłogowego – zgodnie z kartą produktu', 'Dekory drewna i kamienia']),
        ('drewniane', 'Podłogi drewniane', 'Deska z naturalnego drewna: każda inna, z prawdziwym usłojeniem. Na lata, z możliwością odnowienia. Pokażemy próbki i pomożemy wybrać wykończenie – olej albo lakier.', ['Deski warstwowe i lite', 'Wykończenie olejowane lub lakierowane', 'Listwy w kolorze podłogi']),
        ('scienne', 'Panele ścienne', 'Efektowna ściana za łóżkiem, telewizorem albo w przedpokoju bez kucia i tynkowania. Lamele, panele 3D i dekory drewna.', ['Lamele drewniane i drewnopodobne', 'Panele dekoracyjne', 'Montaż na klej lub listwy']),
        ('tarasowe', 'Deski tarasowe', 'Kompozytowe, które nie wymagają olejowania, i drewniane dla miłośników naturalnego materiału. Doradzimy też legary i system montażu.', ['Deski kompozytowe', 'Deski drewniane', 'Legary, klipsy i listwy maskujące']),
        ('akcesoria', 'Akcesoria', 'Wszystko, co potrzebne do wykończenia podłogi i drzwi: listwy przypodłogowe, progi, podkłady, klamki i wkładki.', ['Listwy przypodłogowe i progi', 'Podkłady pod panele', 'Klamki, zamki, wkładki']),
    ]
    rows = ''.join(f'<section class="rzad" id="{a}" aria-labelledby="{a}-h" style="grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);align-items:start"><h2 id="{a}-h" class="ln-wrap">{lines(h)}</h2><div><p class="lead" data-r style="color:var(--text)">{t}</p><ul class="pkt" data-r="2">{"".join(f"<li>{x}</li>" for x in p)}</ul></div></section>' for a, h, t, p in poz)
    tab = '''<div class="tab-wrap" data-r><table class="por"><caption style="position:absolute;left:-9999px">Panele laminowane a winylowe</caption>
<thead><tr><th scope="col">Cecha</th><th scope="col">Panele laminowane</th><th scope="col">Panele winylowe</th></tr></thead><tbody>
<tr><th scope="row">Odporność na wilgoć</th><td>Ograniczona, zależy od modelu</td><td>Wyższa – dobre do kuchni i przedpokoju</td></tr>
<tr><th scope="row">W dotyku</th><td>Twarde i chłodniejsze</td><td>Cieplejsze i bardziej sprężyste</td></tr>
<tr><th scope="row">Akustyka</th><td>Głośniejsze, warto dobrać dobry podkład</td><td>Cichsze przy chodzeniu</td></tr>
<tr><th scope="row">Ogrzewanie podłogowe</th><td>Tak, jeśli dopuszcza producent</td><td>Tak, jeśli dopuszcza producent</td></tr>
<tr><th scope="row">Gdzie najczęściej</th><td>Salon, sypialnia, pokój dziecka</td><td>Kuchnia, przedpokój, poddasze</td></tr>
</tbody></table></div><p class="tab-nota" data-r>Ostatecznie decydują parametry konkretnego modelu – sprawdzimy je z Tobą w salonie.</p>'''
    return f'''
<section class="phero ciemna" aria-labelledby="h1">
 <div class="wrap">
  <div>{crumbs_html([('', 'Start'), ('podlogi-i-sciany/', 'Podłogi i ściany')], pre)}<h1 id="h1">{lines('Panele podłogowe', 'i ścienne w Głogowie')}</h1></div>
  <div class="side fade"><p class="lead">Laminat, winyl, deska drewniana, panele ścienne i deski tarasowe. Próbki w salonie, doradztwo i montaż.</p><a class="btn btn-red" href="{pre}kontakt/">Zapytaj o podłogę</a></div>
 </div>
</section>
<section class="sek sek-o" aria-labelledby="w-h" style="padding:clamp(60px,8vw,110px) 0"><div class="wrap mat" style="align-items:center">
 <div class="fot odslon" style="position:static">{img('deski-drewniane-poglad', pre, '(max-width: 820px) 100vw, 45vw', alt='Drewniane deski – zdjęcie poglądowe')}<small>Zdjęcie poglądowe</small></div>
 <div><h2 id="w-h" class="ln-wrap">{lines('Podłoga i drzwi', 'w jednym miejscu')}</h2><p class="lead" data-r>Najlepiej dobrać je razem. W salonie położysz próbkę panelu obok okleiny drzwi i od razu zobaczysz, czy kolory do siebie pasują – zestawione tonalnie albo na kontraście.</p><a class="btn btn-dark" data-r="2" href="{pre}drzwi/">Zobacz drzwi</a></div>
</div></section>
<div class="sek" style="padding-top:clamp(30px,4vw,60px)"><div class="wrap">{rows}</div></div>
<section class="sek sek-b" aria-labelledby="por-h"><div class="wrap">
 <div class="glowa"><h2 id="por-h" class="ln-wrap">{lines('Panele winylowe', 'czy laminowane?')}</h2><p class="lead" data-r>Krótko o różnicach, o które pytacie najczęściej.</p></div>
 {tab}
</div></section>
<section class="sek" aria-labelledby="faq-h"><div class="wrap">
 <div class="glowa"><h2 id="faq-h" class="ln-wrap">{lines('Pytania o podłogi')}</h2><p class="lead" data-r>Jeśli nie ma tu Twojego pytania, zadzwoń – odpowiemy od ręki.</p></div>
 {faq_html(FAQ_P)}
 <div style="margin-top:60px">{cta_pas(pre, 'Przyjdź po próbki', 'Salon przy ul. 1 Maja 16 w Głogowie, pon.–pt. 9:00–17:00.')}</div>
</div></section>'''

# ---------------- REALIZACJE ----------------
KAT = [('wew', 'Wewnętrzne'), ('mie', 'Do mieszkań'), ('zew', 'Zewnętrzne'), ('prz', 'Przesuwne')]
KOLEJ = ['drzwi-wewnetrzne-dab-czarna-oscieznica', 'drzwi-zewnetrzne-dwuskrzydlowe-antracyt', 'drzwi-szklane-loft-czarna-rama', 'drzwi-do-mieszkania-zloty-dab-intarsje',
         'drzwi-przesuwne-grafit-i-skrzydlowe', 'drzwi-wewnetrzne-dab-czarne-oscieznice-para', 'drzwi-zewnetrzne-czarne-cztery-szyby', 'drzwi-wewnetrzne-biale-czarne-oscieznice',
         'drzwi-dwuskrzydlowe-dab-czarna-rama-szprosy', 'drzwi-do-mieszkania-szary-dab-wizjer', 'drzwi-wewnetrzne-okleina-drewno-przeszklenia', 'drzwi-przesuwne-biale-przeszklone',
         'drzwi-zewnetrzne-ciemny-orzech-z-przeszkleniem', 'drzwi-wewnetrzne-biale-ramiakowe-glogow', 'drzwi-do-mieszkania-ciemne-z-aplikacja', 'drzwi-wewnetrzne-biale-trzy-frezy',
         'drzwi-wewnetrzne-biale-z-tulejami', 'drzwi-wewnetrzne-biale-frezowane-komplet', 'drzwi-wewnetrzne-biale-z-niebieskim-paskiem']
assert sorted(KOLEJ) == sorted(k for k in FOTO if k != 'deski-drewniane-poglad')

def realizacje(pre):
    ile = {k: sum(1 for s in KOLEJ if FOTO[s]['cat'] == k) for k, _ in KAT}
    btn = f'<button type="button" data-f="all" aria-pressed="true">Wszystkie<sup>{len(KOLEJ)}</sup></button>' + ''.join(f'<button type="button" data-f="{k}" aria-pressed="false">{n}<sup>{ile[k]}</sup></button>' for k, n in KAT)
    figs = ''.join(f'<figure data-k="{FOTO[s]["cat"]}" tabindex="0">{img(s, pre, "(max-width: 600px) 100vw, (max-width: 1100px) 50vw, 25vw").replace("<img ", f"<img data-full=\"{full(s, pre)}\" ")}<figcaption>{e(FOTO[s]["alt"])}</figcaption></figure>' for s in KOLEJ)
    arrow = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="{d}"/></svg>'
    return f'''
<section class="phero ciemna" aria-labelledby="h1">
 <div class="wrap">
  <div>{crumbs_html([('', 'Start'), ('realizacje/', 'Realizacje')], pre)}<h1 id="h1">{lines('Montaż drzwi –', 'nasze realizacje')}</h1></div>
  <div class="side fade"><p class="lead">{len(KOLEJ)} montaży z Głogowa i okolic. Zdjęcia robione telefonem na budowie i w mieszkaniach klientów, bez retuszu.</p></div>
 </div>
</section>
<section class="sek" aria-label="Galeria realizacji" style="padding-top:clamp(40px,5vw,70px)"><div class="wrap">
 <div class="filtry" role="group" aria-label="Filtruj realizacje">{btn}</div>
 <div class="siatka">{figs}</div>
 <div style="margin-top:70px">{cta_pas(pre, 'Chcesz takie drzwi u siebie?', 'Przyjdź do salonu albo zadzwoń – zaczniemy od pomiaru.')}</div>
</div></section>
<div class="lb" role="dialog" aria-modal="true" aria-label="Podgląd zdjęcia"><button class="poprz" aria-label="Poprzednie">{arrow('M15 5l-7 7 7 7')}</button><figure><img alt=""><figcaption></figcaption></figure><button class="nast" aria-label="Następne">{arrow('M9 5l7 7-7 7')}</button><button class="zamk" aria-label="Zamknij">{arrow('M6 6l12 12M18 6L6 18')}</button></div>'''

def realizacje_ld():
    u = BASE + 'realizacje/'
    return [{"@type": "ImageGallery", "@id": u + "#galeria", "name": "Realizacje montażu drzwi – Fachowiec Antaba Głogów", "url": u,
             "associatedMedia": [{"@type": "ImageObject", "contentUrl": BASE + full(s, '')[0:], "caption": FOTO[s]['alt'], "creator": {"@id": BASE + "#firma"}} for s in KOLEJ]}]

# ---------------- KONTAKT ----------------
def kontakt(pre):
    return f'''
<section class="phero ciemna" aria-labelledby="h1">
 <div class="wrap">
  <div>{crumbs_html([('', 'Start'), ('kontakt/', 'Kontakt')], pre)}<h1 id="h1">{lines('Salon przy', 'ul. 1 Maja 16')}</h1></div>
  <div class="side fade"><p class="lead">Wpadnij obejrzeć drzwi i podłogi na żywo albo zadzwoń i umów pomiar. Odpowiadamy w godzinach pracy salonu.</p></div>
 </div>
</section>
<section class="sek" aria-label="Dane kontaktowe i formularz"><div class="wrap">
 <div class="kontakt">
  <div class="dane" data-r>
   <h2>Zadzwoń</h2>
   <ul class="tel-lista"><li><span>Sprzedaż i doradztwo</span><a href="tel:{TEL1H}">{TEL1}</a></li><li><span>Montaż i pomiary</span><a href="tel:{TEL2H}">{TEL2}</a></li><li><span>E-mail</span><a href="mailto:{MAIL}" style="font-size:clamp(20px,2vw,26px)">{MAIL}</a></li></ul>
   <h2 style="font-size:24px;margin-top:10px">Godziny otwarcia</h2>
   <table class="godz"><tbody><tr><td>Poniedziałek – piątek</td><td>9:00–17:00</td></tr><tr><td>Sobota – niedziela</td><td>nieczynne</td></tr></tbody></table>
   <address style="font-style:normal">Fachowiec Antaba<br>ul. 1 Maja 16, 67-200 Głogów<br><a class="link" href="https://www.google.com/maps/dir/?api=1&destination=51.6681,16.0812" target="_blank" rel="noopener">Wyznacz trasę</a></address>
  </div>
  <div class="form" data-r="2">
   <h2>Umów pomiar</h2>
   <p style="color:var(--muted)">Napisz, czego potrzebujesz – oddzwonimy i ustalimy termin.</p>
   <form>
    <div class="pola2"><div class="pole"><label for="f-imie">Imię</label><input id="f-imie" name="imie" autocomplete="given-name" required></div>
    <div class="pole"><label for="f-tel">Telefon</label><input id="f-tel" name="telefon" type="tel" autocomplete="tel" required></div></div>
    <div class="pola2"><div class="pole"><label for="f-co">Czego dotyczy</label><select id="f-co" name="temat"><option>Drzwi wewnętrzne</option><option>Drzwi do mieszkania</option><option>Drzwi zewnętrzne</option><option>Drzwi przesuwne</option><option>Panele podłogowe</option><option>Panele ścienne lub deski tarasowe</option><option>Inne</option></select></div>
    <div class="pole"><label for="f-msc">Miejscowość</label><input id="f-msc" name="miejscowosc" autocomplete="address-level2" placeholder="np. Głogów"></div></div>
    <div class="pole"><label for="f-wiad">Wiadomość</label><textarea id="f-wiad" name="wiadomosc" placeholder="Ile drzwi, jakie pomieszczenia, kiedy chcesz montaż…"></textarea></div>
    <label class="zgoda"><input type="checkbox" required><span>Zgadzam się na kontakt w sprawie mojego zapytania. Administratorem danych jest ANTABA Artur Słubowski.</span></label>
    <button class="btn btn-red" type="submit">Wyślij zapytanie</button>
   </form>
   <p class="ok-msg" role="status">Dziękujemy! To wersja pokazowa strony – po wdrożeniu wiadomość trafi prosto na {MAIL}.</p>
  </div>
 </div>
 <div id="mapa" role="region" aria-label="Mapa dojazdu do salonu"></div>
 <div class="dojazd">
  <div data-r><h3>Salon</h3><p>ul. 1 Maja 16, 67-200 Głogów. Wejście od ulicy, na miejscu próbki drzwi i podłóg.</p></div>
  <div data-r="2"><h3>Obszar montażu</h3><p>Głogów i okolice, Sława, Wschowa – województwa dolnośląskie, lubuskie i wielkopolskie.</p></div>
  <div data-r="3"><h3>Zamówienie na odległość</h3><p>Masz już wybrane produkty? Zamówisz je telefonicznie lub mailowo, bez ponownej wizyty.</p></div>
 </div>
</div></section>'''

def nie_ma(pre):
    return f'''<section class="phero ciemna" style="min-height:80vh;display:flex;align-items:center"><div class="wrap" style="grid-template-columns:1fr"><div><h1 id="h1">{lines('Tych drzwi', 'tu nie ma')}</h1><p class="lead fade">Strona, której szukasz, nie istnieje albo zmieniła adres.</p><p class="fade f2"><a class="btn btn-red" href="{BASE}">Strona główna</a></p></div></div></section>'''

# ---------------- generowanie ----------------
page('', 'Drzwi i podłogi Głogów z montażem – Fachowiec Antaba', 'Salon drzwi i podłóg w Głogowie, ul. 1 Maja 16. Drzwi wewnętrzne, zewnętrzne, przesuwne i do mieszkań z pomiarem, transportem i montażem. Tel. 781 790 030.', start, home=True)
page('drzwi/', 'Drzwi Głogów – wewnętrzne, zewnętrzne, przesuwne z montażem', 'Drzwi wewnętrzne przylgowe i bezprzylgowe, rewersyjne, szklane, przesuwne, do mieszkań i zewnętrzne. Pomiar i montaż w Głogowie i okolicach od 2017 roku.', drzwi,
     crumbs=[('drzwi/', 'Drzwi')], extra_ld=[faq_ld(BASE + 'drzwi/', FAQ_D)])
page('podlogi-i-sciany/', 'Panele podłogowe Głogów – laminowane, winylowe, drewniane', 'Panele laminowane, winylowe, podłogi drewniane, panele ścienne i deski tarasowe w Głogowie. Próbki w salonie przy ul. 1 Maja 16, doradztwo i montaż.', podlogi,
     crumbs=[('podlogi-i-sciany/', 'Podłogi i ściany')], extra_ld=[faq_ld(BASE + 'podlogi-i-sciany/', FAQ_P)])
page('realizacje/', 'Montaż drzwi Głogów – realizacje Fachowiec Antaba', 'Zdjęcia montażu drzwi wewnętrznych, zewnętrznych, przesuwnych i do mieszkań w Głogowie i okolicach. Realizacje salonu Fachowiec Antaba.', realizacje,
     crumbs=[('realizacje/', 'Realizacje')], extra_ld=realizacje_ld())
page('kontakt/', 'Kontakt – salon drzwi i podłóg Głogów, ul. 1 Maja 16', 'Salon Fachowiec Antaba, ul. 1 Maja 16, 67-200 Głogów. Pon.–pt. 9:00–17:00. Sprzedaż: 781 790 030, montaż i pomiary: 695 898 059.', kontakt,
     crumbs=[('kontakt/', 'Kontakt')], leaflet=True)
page('404/', 'Nie znaleziono strony – Fachowiec Antaba Głogów', 'Strona nie istnieje.', nie_ma)
# 404 bez indeksowania i z absolutnymi ścieżkami (GitHub Pages serwuje ją pod dowolnym adresem)
s = open('404.html', encoding='utf-8').read().replace('index, follow, max-image-preview:large', 'noindex').replace('href="assets/', f'href="{BASE}assets/').replace('src="assets/', f'src="{BASE}assets/').replace('href="favicon', f'href="{BASE}favicon')
for u, _ in NAV: s = s.replace(f'href="{u}"', f'href="{BASE}{u}"') if u else s.replace('href="./"', f'href="{BASE}"')
s = s.replace('href="kontakt/"', f'href="{BASE}kontakt/"')
open('404.html', 'w', encoding='utf-8').write(s)

urls = ['', 'drzwi/', 'podlogi-i-sciany/', 'realizacje/', 'kontakt/']
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
for u in urls:
    imgs = ''
    if u == 'realizacje/':
        imgs = ''.join(f'<image:image><image:loc>{BASE}{full(s, "")}</image:loc></image:image>' for s in KOLEJ)
    sm += f'<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod>{imgs}</url>\n'
open('sitemap.xml', 'w', encoding='utf-8').write(sm + '</urlset>\n')
open('robots.txt', 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
open('favicon.svg', 'w', encoding='utf-8').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="24" fill="#111c44"/><path d="M15.5 37V11.5h17V37" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round"/><path d="M16.3 12.3l10.4 3v23.2l-10.4-1.5z" fill="#fff"/></svg>')
print('ok')
