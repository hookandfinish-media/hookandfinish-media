import asyncio, os
from playwright.async_api import async_playwright
F="/usr/share/fonts/truetype/google-fonts"
CSS=f"""@font-face{{font-family:Lora;src:url(file://{F}/Lora-Variable.ttf)}}@font-face{{font-family:LoraI;src:url(file://{F}/Lora-Italic-Variable.ttf)}}
@font-face{{font-family:PopB;src:url(file://{F}/Poppins-Bold.ttf)}}@font-face{{font-family:Pop;src:url(file://{F}/Poppins-Regular.ttf)}}@font-face{{font-family:PopM;src:url(file://{F}/Poppins-Medium.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{background:#4A2440;color:#FBEFE2;font-family:Pop;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 80px;position:relative}}
.tag{{font-family:PopB;letter-spacing:.18em;color:#E8B85C;font-size:38px;margin-bottom:40px}}
.h{{font-family:Lora;font-weight:700;font-size:118px;line-height:1.05}}
.h em{{font-family:LoraI;color:#F2A7A0;font-style:normal}}
.card{{background:#FBEFE2;color:#4A2440;border-radius:44px;padding:56px 50px;width:100%;margin:40px 0}}
.q{{font-family:PopB;font-size:70px;line-height:1.2}}
.opt{{display:flex;gap:30px;justify-content:center;margin-top:36px}}
.o{{border:5px solid #4A2440;border-radius:999px;padding:20px 40px;font-family:PopM;font-size:44px}}
.big{{font-family:PopB;font-size:150px;color:#E8B85C;line-height:1}}
.swipe{{position:absolute;bottom:170px;left:0;right:0;font-family:PopB;font-size:46px;color:#F2A7A0}}
.n{{position:absolute;top:150px;left:0;right:0;font-family:PopB;font-size:34px;color:rgba(251,239,226,.55);letter-spacing:.2em}}
.ok{{font-family:PopB;font-size:46px;color:#9FD39A;margin-bottom:20px}}
"""
def q(us,a,b): return f'<div class="card"><div class="q">🇺🇸 {us}<br>= 🇬🇧 ???</div><div class="opt"><div class="o">A) {a}</div><div class="o">B) {b}</div></div></div>'
def reveal(ans,note): return f'<div class="ok">ANSWER</div><div class="big">{ans}</div><div style="font-size:44px;margin-top:24px;color:#EBD3DC">{note}</div>'
S=[
 '<div class="tag">CROCHET QUIZ 🇺🇸 → 🇬🇧</div><div class="h">Can you <em>translate</em> 4 crochet stitches?</div><div style="font-size:52px;margin-top:50px;font-family:PopM">Most beginners get 0/4 😅</div><div class="swipe">Swipe to play →</div>',
 '<div class="n">QUESTION 1 / 4</div>'+q("single crochet","Single crochet","Double crochet")+'<div class="swipe">Swipe for the answer →</div>',
 '<div class="n">1 / 4</div>'+reveal("B) DOUBLE 🤯","Same stitch, different name!")+'<div style="height:60px"></div><div class="n" style="position:static;margin-bottom:10px">QUESTION 2</div>'+q("double crochet","Treble","Half double")+'<div class="swipe">Swipe →</div>',
 '<div class="n">2 / 4</div>'+reveal("A) TREBLE","UK names are always one step taller.")+'<div style="height:60px"></div><div class="n" style="position:static;margin-bottom:10px">QUESTION 3</div>'+q("half double crochet","Half single","Half treble")+'<div class="swipe">Swipe →</div>',
 '<div class="n">3 / 4</div>'+reveal("B) HALF TREBLE","You're getting it 👀")+'<div style="height:60px"></div><div class="n" style="position:static;margin-bottom:10px">LAST ONE (the hardest)</div>'+q("skip","Miss","Pass")+'<div class="swipe">Swipe →</div>',
 '<div class="n">4 / 4</div>'+reveal("A) MISS","\"Miss 1 st\" just means skip one.")+'<div class="card" style="margin-top:70px"><div class="q" style="font-size:62px">What was your score? 🧶</div><div style="font-size:44px;margin-top:20px;font-family:PopM">Comment 0, 1, 2, 3 or 4 👇</div></div>',
 '<div class="tag">SAVE THIS 📌</div><div class="h">All the <em>US ↔ UK</em> terms on one page</div><img src="file:///home/claude/cheat/p1.png" style="width:560px;border-radius:16px;margin:60px 0;transform:rotate(-3deg);box-shadow:0 30px 70px rgba(0,0,0,.4)"><div style="background:#CF6448;color:#fff;font-family:PopB;font-size:50px;padding:30px 56px;border-radius:999px">Free cheat sheet on my profile 👆</div>',
]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        for i,s in enumerate(S):
            open(f"s{i}.html","w").write(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{s}</body></html>")
            await pg.goto(f"file:///home/claude/quiz/s{i}.html"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"TikTok_Quiz_UKUS_{i+1}.jpg",type="jpeg",quality=92)
        await b.close()
asyncio.run(main())
