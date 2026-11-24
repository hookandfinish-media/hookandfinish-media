import sys, subprocess, os, json, time
from playwright.sync_api import sync_playwright
D="/home/claude/moon2"
open(f"{D}/web/page.html","w").write(open(f"{D}/web/index.html").read().replace("DATA_JSON",open(f"{D}/data.json").read()))
with sync_playwright() as p:
    b=p.chromium.launch(args=["--allow-file-access-from-files","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
    pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.on("console", lambda m: print("console:", m.text) if m.type in ("error",) else None)
    pg.on("pageerror", lambda e: print("pageerror:", e))
    pg.goto(f"file://{D}/web/page.html"); pg.wait_for_function("window.READY===true",timeout=120000); pg.wait_for_timeout(500)
    if sys.argv[1]=="stills":
        for t in [float(x) for x in sys.argv[2:]]:
            t0=time.time(); pg.evaluate(f"renderFrame({round(t*30)})"); pg.screenshot(path=f"{D}/st_{t:05.1f}.jpg",type="jpeg",quality=75); print(t, round(time.time()-t0,2))
    else:
        a,bq=int(sys.argv[2]),int(sys.argv[3]); out=f"{D}/part_{a:04d}.mp4"; tmp=out[:-4]+".tmp.mp4"
        ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate","30","-c:v","mjpeg","-i","-","-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r","30",tmp],stdin=subprocess.PIPE)
        for f in range(a,bq):
            pg.evaluate(f"renderFrame({f})"); ff.stdin.write(pg.screenshot(type="jpeg",quality=93))
        ff.stdin.close(); assert ff.wait()==0; os.replace(tmp,out)
    b.close()
