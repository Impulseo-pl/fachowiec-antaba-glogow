import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    pg=b.new_page(viewport={'width':1440,'height':900})
    pg.goto('http://127.0.0.1:8125/fachowiec-antaba/?team=1',wait_until='networkidle'); pg.wait_for_timeout(5000)
    print(pg.evaluate(sys.argv[1]))
    b.close()
