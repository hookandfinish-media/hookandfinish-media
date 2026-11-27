import os, asyncio
from gen import pin_shell, rows, sym, D
from playwright.async_api import async_playwright
def card(inner, pad="26px 40px"): return f'<div class="card" style="padding:{pad}">{inner}</div>'
def head3(a,b): return f'<div style="display:flex;justify-content:space-between;font-family:PopB;color:var(--rose);font-size:22px;letter-spacing:.14em;padding:0 4px 8px">{a}<span>{b}</span></div>'
def steps(items, size=31):
    return "".join(f'<div class="card" style="padding:22px 30px;margin-bottom:14px;display:flex;gap:22px;align-items:center"><div style="flex:none;width:58px;height:58px;border-radius:50%;border:3px dashed var(--rose);color:var(--rose);font-family:PopB;font-size:26px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div style="font-family:PopB;color:var(--plum);font-size:{size}px">{a}</div><div style="font-size:24px;color:var(--ink2);margin-top:2px">{b}</div></div></div>' for i,(a,b) in enumerate(items))
P={}
P["17_terms"]=pin_shell("Learn these first","7 crochet words <em>every beginner</em> must know",card(rows([("Yarn over (yo)","wrap yarn over hook"),("Loop","yarn on your hook"),("Stitch (st)","one finished unit"),("Row","work back and forth"),("Round (rnd)","work in a circle"),("Foundation chain","your starting chain"),("Turning chain","chains to start a row")])),top=400)
P["18_week_plan"]=pin_shell("Learn crochet in 7 days","Your first <em>week</em> of crochet: a simple plan",card(rows([("Day 1","Slip knot + chain"),("Day 2","Single crochet rows"),("Day 3","Half double crochet"),("Day 4","Double crochet"),("Day 5","Straight edges + counting"),("Day 6","Magic ring + rounds"),("Day 7","Your first granny square")])),top=400)
P["19_tension"]=pin_shell("Fix your tension","Too tight or <em>too loose?</em> Easy fixes",steps([("Too tight","Hold the yarn more loosely, try a bigger hook"),("Too loose","Wrap yarn around a finger for more grip"),("Uneven","Pull each loop up to the hook's widest part"),("Sore hands","Take breaks, try an ergonomic hook")]),top=430)
P["20_loops"]=pin_shell("Same stitch, new texture","Front loop, back loop or <em>both loops?</em>",steps([("Both loops","The default. Smooth, sturdy fabric"),("Front loop only (FLO)","Leaves a line on the back, softer"),("Back loop only (BLO)","Makes ribbing, great for hats"),("Tip","Patterns tell you when to switch")]),top=430)
P["21_count"]=pin_shell("Stop losing stitches","How to <em>count</em> crochet stitches",steps([("Count the V's","Each stitch top looks like a sideways V"),("Use a marker","Clip it in the first stitch of each row"),("Count every row","Write the number down as you go"),("Don't count the turning chain","Unless your pattern says so")]),top=430)
P["22_stocking"]=pin_shell("Quick Christmas makes","8 crochet <em>stocking stuffers</em> under an hour",card(head3("GIFT","TIME")+rows([("Bookmark","30 min"),("Coaster","30 min"),("Scrunchie","45 min"),("Keychain heart","30 min"),("Mini star ornament","40 min"),("Mug cozy","1 hr"),("Hair bow","30 min"),("Face scrubbie","20 min")])),top=400)
P["23_winter"]=pin_shell("Cozy season","8 easy <em>winter</em> crochet projects for beginners",card(rows([("Chunky ear warmer","1 evening"),("Ribbed beanie","weekend"),("Simple scarf","weekend"),("Fingerless gloves","2 evenings"),("Granny square blanket","long project"),("Cowl","1 evening"),("Hot water bottle cover","2 evenings"),("Slipper socks","weekend")])),top=400)
P["24_hook_parts"]=pin_shell("Know your tool","The 5 parts of a <em>crochet hook</em>",steps([("Head","Catches the yarn"),("Throat","Guides yarn off the head"),("Shaft","Sets the size of your stitches"),("Thumb rest","Where you hold it"),("Handle","Gives you control")]),top=430)
async def main():
    os.makedirs(f"{D}/pins3",exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1000,"height":1500})
        for k,v in P.items():
            f=f"{D}/pins3/{k}.html"; open(f,"w").write(v); await pg.goto(f"file://{f}"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"{D}/pins3/{k}.jpg",type="jpeg",quality=90)
        await b.close()
asyncio.run(main())
