import os, glob, subprocess, asyncio, numpy as np, wave
from playwright.async_api import async_playwright
D = "/home/claude/reels2"; C = "/home/claude/cheat/car"
FONT = "/usr/share/fonts/truetype/google-fonts"
SETS = {"ReadPattern": "How to read a crochet pattern", "USvsUK": "US vs UK crochet terms", "MagicRing": "Magic ring in 4 steps", "Mistakes": "5 beginner crochet mistakes"}
CSS = f"""@font-face{{font-family:Lora;src:url(file://{FONT}/Lora-Variable.ttf)}}@font-face{{font-family:LoraI;src:url(file://{FONT}/Lora-Italic-Variable.ttf)}}
@font-face{{font-family:PopB;src:url(file://{FONT}/Poppins-Bold.ttf)}}@font-face{{font-family:Pop;src:url(file://{FONT}/Poppins-Regular.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#F4ECDF;font-family:Pop}}"""

def frame(img):  # slide with top hook + bottom CTA, CTA always visible
    return f'''<html><head><style>{CSS}</style></head><body>
<div style="position:absolute;top:150px;left:0;right:0;text-align:center;font-family:PopB;color:#4A2440;font-size:44px;letter-spacing:.04em">📌 Save this for later</div>
<img src="file://{img}" style="position:absolute;top:255px;left:40px;width:1000px;border-radius:28px;box-shadow:0 20px 50px rgba(74,36,64,.18)">
<div style="position:absolute;top:1545px;left:0;right:0;display:flex;justify-content:center"><div style="background:#4A2440;color:#FBEFE2;font-family:PopB;font-size:38px;padding:24px 44px;border-radius:999px">Free cheat sheet → link in bio</div></div>
</body></html>'''

END = f'''<html><head><style>{CSS}</style></head><body><div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 90px">
<div style="font-family:PopB;color:#C27A74;letter-spacing:.2em;font-size:34px">FREE · PRINTABLE · PDF</div>
<div style="font-family:Lora;font-weight:700;color:#4A2440;font-size:118px;line-height:1.02;margin:30px 0">The crochet <span style="font-family:LoraI;color:#C27A74">cheat sheet</span> beginners save</div>
<img src="file:///home/claude/cheat/p1.png" style="width:560px;border-radius:14px;box-shadow:0 24px 60px rgba(0,0,0,.25);transform:rotate(-3deg);margin:20px 0 60px">
<div style="background:#CF6448;color:#fff;font-family:PopB;font-size:48px;padding:30px 56px;border-radius:999px">Get it free → link in bio</div>
<div style="font-family:LoraI;color:#6E5664;font-size:40px;margin-top:36px">@hookandfinish</div></div></body></html>'''

def music(path, dur, sr=44100):
    t = np.arange(int(dur*sr))/sr; out = np.zeros_like(t)
    notes = [60, 64, 67, 72, 67, 64, 62, 65, 69, 74, 69, 65]; step = 0.42
    for i in range(int(dur/step)):
        m = notes[i % len(notes)]; f = 440*2**((m-69)/12); s = int(i*step*sr); n = min(int(0.9*sr), len(t)-s)
        if n <= 0: break
        tt = np.arange(n)/sr
        out[s:s+n] += 0.18*(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt))*np.exp(-tt/0.35)
    for i in range(int(dur/(step*4))):  # soft bass
        f = 440*2**(([48, 43, 45, 41][i % 4]-69)/12); s = int(i*step*4*sr); n = min(int(step*4*sr), len(t)-s)
        if n <= 0: break
        tt = np.arange(n)/sr; out[s:s+n] += 0.12*np.sin(2*np.pi*f*tt)*np.exp(-tt/1.2)
    fade = np.minimum(1, np.minimum(t/0.5, (dur-t)/1.0)); out *= fade
    out = (out/np.max(np.abs(out))*0.5*32767).astype(np.int16)
    with wave.open(path, "w") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(out.tobytes())

async def render():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for s in SETS:
            os.makedirs(f"{D}/{s}", exist_ok=True)
            for f in sorted((glob.glob(f"{C}/Carousel_{s}_*.jpg") or glob.glob(f"/home/claude/cheat/out/Carousel_{s}_*.jpg")), key=lambda x: int(x.split("_")[-1][:-4])):
                n = f.split("_")[-1][:-4]; h = f"{D}/{s}/f{n}.html"; open(h, "w").write(frame(f))
                await pg.goto(f"file://{h}"); await pg.wait_for_timeout(300); await pg.screenshot(path=f"{D}/{s}/f{int(n):02d}.png")
        open(f"{D}/end.html", "w").write(END); await pg.goto(f"file://{D}/end.html"); await pg.wait_for_timeout(400); await pg.screenshot(path=f"{D}/end.png")
        await b.close()

asyncio.run(render())
for s in SETS:
    frames = sorted(glob.glob(f"{D}/{s}/f*.png"))
    per = 2.6 if len(frames) <= 6 else 2.3
    lst = "".join(f"file '{f}'\nduration {per if i else 2.0}\n" for i, f in enumerate(frames)) + f"file '{D}/end.png'\nduration 3.0\nfile '{D}/end.png'\n"
    open(f"{D}/{s}/list.txt", "w").write(lst)
    dur = 2.0 + per*(len(frames)-1) + 3.0
    music(f"{D}/{s}/m.wav", dur)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{D}/{s}/list.txt", "-i", f"{D}/{s}/m.wav",
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-shortest",
                    "-movflags", "+faststart", f"{D}/Reel_{s}.mp4"], check=True)
    print(s, round(dur, 1))
