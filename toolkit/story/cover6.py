import sys
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
JOBS={6:(0.9,"A HOOK AND SOME THREAD","SAVED FAMILIES?","Cover_Ep6_Irish_Famine.jpg")}
with sync_playwright() as p:
    b=p.chromium.launch(args=["--allow-file-access-from-files","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
    for n,(t,l1,l2,out) in JOBS.items():
        D=f"/home/claude/ep5/e{n}"
        h=open(f"{D}/web/index.html").read().replace("DATA_JSON",open(f"{D}/data.json").read()).replace("</style>","#cnt,#cap,#lab{display:none!important}</style>")
        open(f"{D}/web/page_cov.html","w").write(h)
        pg=b.new_page(viewport={"width":1080,"height":1920});pg.goto(f"file://{D}/web/page_cov.html");pg.wait_for_function("window.READY===true",timeout=120000)
        pg.evaluate(f"renderFrame({int(t*30)})");pg.screenshot(path=f"{D}/cov.png");pg.close()
        im=Image.open(f"{D}/cov.png").convert("RGBA");W,H=im.size;ov=Image.new("RGBA",(W,H),(0,0,0,0));d=ImageDraw.Draw(ov)
        for i in range(620): d.line([(0,i),(W,i)],fill=(20,10,25,int(190*(1-i/620))))
        im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
        def line(y,txt,size,col):
            f=ImageFont.truetype(F,size)
            while d.textlength(txt,font=f)>W-90: size-=4;f=ImageFont.truetype(F,size)
            d.text(((W-d.textlength(txt,font=f))/2,y),txt,font=f,fill=col,stroke_width=int(size*.1),stroke_fill="#1a0f1c")
        line(150,l1,92,"white");line(270,l2,128,"#FFD23F")
        im.convert("RGB").save(f"/home/claude/ep5/{out}",quality=92)
    b.close()
c=Image.new("RGB",(len(JOBS)*216,384))
for i,(n,j) in enumerate(JOBS.items()): c.paste(Image.open(f"/home/claude/ep5/{j[3]}").resize((216,384)),(i*216,0))
c.save("/home/claude/ep5/covers_sheet.jpg")
