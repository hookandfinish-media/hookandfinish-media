import sys,json
from playwright.sync_api import sync_playwright
D=sys.argv[1]
open(f"{D}/web/page.html","w").write(open(f"{D}/web/index.html").read().replace("DATA_JSON",open(f"{D}/data.json").read()))
with sync_playwright() as p:
    b=p.chromium.launch(args=["--allow-file-access-from-files","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
    pg=b.new_page(viewport={"width":1080,"height":1920});pg.goto(f"file://{D}/web/page.html");pg.wait_for_function("window.READY===true",timeout=120000)
    json.dump(pg.evaluate("window.CUTS"),open(f"{D}/cuts.json","w"));b.close()
