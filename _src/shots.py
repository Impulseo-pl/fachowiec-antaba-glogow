import sys
from playwright.sync_api import sync_playwright
from PIL import Image
pages=sys.argv[2].split(','); w=int(sys.argv[1]); mobile=w<700
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    ctx=b.new_context(viewport={'width':w,'height':900 if not mobile else 844},device_scale_factor=1,is_mobile=mobile,has_touch=mobile)
    pg=ctx.new_page()
    errs=[]; pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append(str(e)))
    for path in pages:
        pg.goto('http://127.0.0.1:8125/fachowiec-antaba/'+path+'?team=1',wait_until='networkidle')
        pg.wait_for_timeout(2500)
        name=(path.strip('/') or 'home').replace('/','_')+f'_{w}'
        pg.screenshot(path=f'_src/sh_{name}_fold.png')
        h=pg.evaluate('document.body.scrollHeight')
        for y in range(0,h,500): pg.evaluate(f'window.scrollTo(0,{y})'); pg.wait_for_timeout(150)
        pg.wait_for_timeout(1200)
        h=pg.evaluate('document.body.scrollHeight')
        # pin/sticky efekty psują full_page – robimy klatki ekranu co wysokość okna
        vh=900 if not mobile else 844; n=0
        for y in range(0,h,vh):
            pg.evaluate(f'window.scrollTo(0,{y})'); pg.wait_for_timeout(700)
            pg.screenshot(path=f'_src/sh_{name}_{n}.png'); n+=1
        sw=pg.evaluate('document.documentElement.scrollWidth')
        print(name,'h',h,'scrollW',sw,'parts',n)
    print('errors',errs)
    b.close()
