import os, json
from PIL import Image, ImageOps
F='_src/foto/'
M=[
('195425110-crop-received-1941415369332097.jpeg.jpg','drzwi-wewnetrzne-biale-ramiakowe-glogow','wew','Białe drzwi wewnętrzne ramiakowe przy ciemnej, strukturalnej tapecie'),
('195425565-crop-received-2625336764439647.jpeg.jpg','drzwi-wewnetrzne-biale-z-niebieskim-paskiem','wew','Białe drzwi wewnętrzne z pionowym niebieskim przeszkleniem i czarną klamką'),
('195425935-crop-received-212120584337337.jpeg.jpg','drzwi-wewnetrzne-biale-frezowane-komplet','wew','Dwoje białych drzwi z poziomymi frezami i czarnymi klamkami w jasnym przedpokoju'),
('195426336-crop-received-494157628660138.jpeg.jpg','drzwi-zewnetrzne-ciemny-orzech-z-przeszkleniem','zew','Drzwi zewnętrzne w kolorze ciemnego orzecha z pionowym przeszkleniem, tuż po osadzeniu'),
('195426971-crop-received-160849952555106.jpeg.jpg','drzwi-zewnetrzne-dwuskrzydlowe-antracyt','zew','Dwuskrzydłowe drzwi zewnętrzne w antracycie z długim pochwytem, wejście do domu jednorodzinnego'),
('195427644-crop-received-632260151054438.jpeg.jpg','drzwi-wewnetrzne-biale-trzy-frezy','wew','Białe drzwi wewnętrzne z trzema poziomymi frezami i czarną klamką'),
('195428189-crop-resized-20200120-170700-439.jpeg.jpg','drzwi-do-mieszkania-szary-dab-wizjer','mie','Drzwi wejściowe do mieszkania w szarym dekorze drewna, z wizjerem i frezami'),
('195429065-crop-received-393476928161030.jpeg.jpg','drzwi-do-mieszkania-ciemne-z-aplikacja','mie','Ciemne drzwi wejściowe do mieszkania z dwiema łukowymi aplikacjami'),
('195430110-crop-received-881983505308808.jpeg.jpg','drzwi-zewnetrzne-czarne-cztery-szyby','zew','Czarne drzwi zewnętrzne z czterema poziomymi szybami w trakcie montażu, Głogów'),
('195431553-crop-received-423210448556413.jpeg.jpg','drzwi-wewnetrzne-biale-z-tulejami','wew','Dwoje białych drzwi wewnętrznych, jedne z tulejami wentylacyjnymi, w narożniku pokoju'),
('195432335-crop-received-2616395465052715.jpeg.jpg','drzwi-wewnetrzne-okleina-drewno-przeszklenia','wew','Dwa modele drzwi wewnętrznych w okleinie drewnopodobnej z poziomymi przeszkleniami'),
('39324_received_907124062794752.jpg','drzwi-do-mieszkania-zloty-dab-intarsje','mie','Drzwi wejściowe do mieszkania w złotym dębie z czterema jasnymi intarsjami'),
('39324_received_916173585223133.jpg','drzwi-przesuwne-biale-przeszklone','prz','Białe, częściowo przeszklone drzwi przesuwne naścienne w trakcie montażu'),
('crop-received-1701524010185951.jpeg.jpg','drzwi-dwuskrzydlowe-dab-czarna-rama-szprosy','wew','Dwuskrzydłowe drzwi w dębowej okleinie z czarną ramą i przeszkleniem ze szprosami'),
('crop-received-2028712427320255.jpeg.jpg','drzwi-przesuwne-grafit-i-skrzydlowe','prz','Grafitowe drzwi przesuwne i skrzydłowe z pionowymi aplikacjami w jednym korytarzu'),
('crop-received-3380617325515423.jpeg.jpg','drzwi-szklane-loft-czarna-rama','wew','Szklane drzwi w czarnej ramie ze szprosami w stylu loft, tuż po montażu'),
('crop-received-475125907840948.jpeg.jpg','drzwi-wewnetrzne-dab-czarna-oscieznica','wew','Drzwi wewnętrzne w jasnym dębie z czarną ościeżnicą i czarną klamką'),
('crop-received-738750737598880.jpeg.jpg','drzwi-wewnetrzne-biale-czarne-oscieznice','wew','Dwoje białych gładkich drzwi z czarnymi ościeżnicami w narożniku przedpokoju'),
('crop-received-908311807255100.jpeg.jpg','drzwi-wewnetrzne-dab-czarne-oscieznice-para','wew','Pojedyncze i dwuskrzydłowe drzwi w jasnym dębie z czarnymi ościeżnicami'),
]
out=[]
for src,slug,cat,alt in M:
    im=ImageOps.exif_transpose(Image.open(F+src)).convert('RGB')
    w,h=im.size; sizes=[]
    for tw in (480,900,1400):
        t=min(tw,w)
        if t in sizes: break
        r=im.resize((t,round(h*t/w)),Image.LANCZOS)
        r.save(f'img/{slug}-{t}.webp','WEBP',quality=80,method=6); sizes.append(t)
    out.append(dict(slug=slug,cat=cat,alt=alt,w=w,h=h,sizes=sizes))
json.dump(out,open('_src/foto.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out)); [print(o['slug'],o['w'],o['h'],o['sizes']) for o in out]
