import json
from PIL import Image
M=[('s1.webp','salon-fachowiec-glogow-1-maja-16','Salon Fachowiec przy ul. 1 Maja 16 w Głogowie – witryna i wejście'),
('s91.webp','salon-glogow-wnetrze-ekspozycja','Wnętrze salonu: ekspozycja drzwi i podłóg, widok od wejścia'),
('s5.webp','ekspozycja-drzwi-dre-glogow','Ekspozycja drzwi wewnętrznych DRE w salonie w Głogowie'),
('s6.webp','ekspozycja-drzwi-wewnetrznych','Drzwi wewnętrzne w grafitowych portalach ekspozycji'),
('s7.webp','stanowisko-doradcy-fachowiec','Stanowisko doradcy w salonie Fachowiec Głogów'),
('s4.webp','panele-swiss-krono-glogow','Panele podłogowe Swiss Krono na ekspozycji w salonie'),
('s92.webp','panele-winylowe-gerflor-glogow','Wzorniki paneli i podłóg winylowych Gerflor oraz Swiss Krono'),
('s3.webp','wzornik-paneli-podlogowych','Wzornik paneli podłogowych w kolorach drewna'),
('s2.webp','listwy-i-panele-wzorniki','Wzorniki listew przypodłogowych i paneli w salonie'),
('s94.webp','listwy-przypodlogowe-wzornik','Listwy przypodłogowe na stojaku ekspozycyjnym obok wzorników paneli'),
('s991.webp','wzorniki-podlog-salon','Wzorniki podłóg przy witrynie salonu'),
('s992-e1770449411466.webp','klamki-akcesoria-drzwi','Stojak z klamkami i akcesoriami do drzwi'),
('s9.webp','fachowiec-logo-salon','Logo Fachowiec na ścianie salonu'),
('s8-e1770449505598.webp','drzwi-dre-dab-ekspozycja','Drzwi w dekorze dębu z czarnym pochwytem na ekspozycji DRE'),
('s93-e1770449490926.webp','drzwi-wewnetrzne-jasne-ekspozycja','Jasne drzwi wewnętrzne i wzornik okleiny na ekspozycji'),
('s95-e1770449471774.webp','drzwi-porta-szklane-loft','Drzwi Porta: przeszklone w czarnej ramie i z lustrem'),
('s96-e1770449458786.webp','drzwi-porta-szalwia-biale','Drzwi Porta w kolorze szałwii i bieli na ekspozycji'),
('s97-e1770449447929.webp','drzwi-z-przeszkleniem-ekspozycja','Drzwi wewnętrzne z przeszkleniami na ekspozycji'),
('s98-e1770449435825.webp','drzwi-zewnetrzne-dab-ekspozycja','Drzwi wejściowe w dekorze dębu na ekspozycji'),
('s99-e1770449424105.webp','drzwi-zewnetrzne-ekspozycja-glogow','Drzwi zewnętrzne z pochwytami na ekspozycji w Głogowie'),
]
out=[]
for src,slug,alt in M:
    im=Image.open('_src/salon/'+src).convert('RGB'); w,h=im.size; sizes=[]
    for tw in (480,w):
        t=min(tw,w)
        if t in sizes: continue
        im.resize((t,round(h*t/w)),Image.LANCZOS).save(f'img/{slug}-{t}.webp','WEBP',quality=82,method=6); sizes.append(t)
    out.append(dict(slug=slug,cat='salon',alt=alt,w=w,h=h,sizes=sizes))
json.dump(out,open('_src/salon.json','w',encoding='utf-8'),ensure_ascii=False,indent=1); print(len(out))
