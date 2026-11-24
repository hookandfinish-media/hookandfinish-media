import os, asyncio
from gen import pin_shell, rows, sym, D
from playwright.async_api import async_playwright

def card(inner, pad="26px 40px"):
    return f'<div class="card" style="padding:{pad}">{inner}</div>'

def head3(t):
    return f'<div style="display:flex;justify-content:space-between;font-family:PopB;color:var(--rose);font-size:22px;letter-spacing:.14em;padding:0 4px 8px">{t[0]}<span>{t[1]}</span></div>'

P = {}
GIFTS = [("Coaster", "30 min"), ("Bookmark", "30 min"), ("Scrunchie", "45 min"), ("Mug cozy", "1 hr"),
         ("Dishcloth", "1–2 hrs"), ("Headband", "1–2 hrs"), ("Ear warmer", "2 hrs"),
         ("Mini amigurumi", "2–3 hrs"), ("Beanie", "3–4 hrs"), ("Scarf", "6–8 hrs")]
P["11_gifts_ranked"] = pin_shell("Start tonight · finish before Christmas",
    "10 last-minute <em>crochet gifts</em>",
    card(head3(("GIFT", "TIME")) + rows([(f"{i+1}. {g}", t) for i, (g, t) in enumerate(GIFTS)]) + '<p style="font-size:21px;color:var(--ink2);margin-top:12px">Fastest first. Rough times for a beginner, medium (#4) yarn.</p>', "22px 40px"), top=380)

COUNT = [("Dec 1", "Scarf, tote bag, blanket squares"), ("Dec 8", "Beanies and ear warmers"),
         ("Dec 15", "Headbands, dishcloths, mini amigurumi"), ("Dec 20", "Mug cozies and scrunchies"),
         ("Dec 23", "Coasters and bookmarks")]
cd = "".join(f'<div style="display:flex;gap:26px;align-items:center;padding:24px 0;border-bottom:2px dashed rgba(74,36,64,.16)"><div style="flex:none;width:150px;font-family:Lora;font-weight:700;color:var(--rose);font-size:40px">{d}</div><div style="font-size:30px"><b style="font-family:PopB;color:var(--plum)">Start:</b> {g}</div></div>' for d, g in COUNT)
P["12_countdown"] = pin_shell("Your Christmas crochet plan", "What to crochet <em>when</em> to finish in time",
    card(cd, "18px 40px") + '<p style="font-size:24px;color:var(--ink2);margin-top:18px">Big projects first, quick ones last. Save this and work backwards.</p>')

YARNG = [("Coasters & dishcloths", "100% cotton"), ("Toys / amigurumi", "Acrylic or cotton"), ("Hats & ear warmers", "Wool blend or acrylic"),
         ("Baby gifts", "Soft acrylic or cotton"), ("Bags & totes", "Cotton or cotton blend"), ("Scarves", "Wool blend")]
P["13_yarn_for_gifts"] = pin_shell("Pick the right yarn", "Which yarn for <em>which gift?</em>",
    card(head3(("GIFT", "YARN")) + rows(YARNG, big=True)) + '<p style="font-size:24px;color:var(--ink2);margin-top:20px">Cotton holds its shape and handles hot mugs. Wool keeps heads warm.</p>')

SCG = [("Coaster", "Rows of sc in a square"), ("Bookmark", "A long, thin strip of sc"), ("Dishcloth", "Bigger square, cotton yarn"),
       ("Headband", "Long strip, seam the ends"), ("Phone pouch", "Fold a rectangle, sew the sides")]
scl = "".join(f'<div class="card" style="padding:24px 30px;margin-bottom:16px;display:flex;gap:22px;align-items:center"><div style="flex:none">{sym("sc",70)}</div><div><div style="font-family:PopB;color:var(--plum);font-size:33px">{a}</div><div style="font-size:25px;color:var(--ink2);margin-top:2px">{b}</div></div></div>' for a, b in SCG)
P["14_single_crochet_gifts"] = pin_shell("Know one stitch? That's enough", "5 gifts you can make with <em>just single crochet</em>", scl, top=430)

YARD = [("Coaster", "20–30 yd"), ("Bookmark", "15–25 yd"), ("Mug cozy", "30–40 yd"), ("Dishcloth", "50–70 yd"),
        ("Headband", "60–80 yd"), ("Beanie", "150–200 yd"), ("Scarf", "300–400 yd")]
P["15_yarn_amounts"] = pin_shell("Before you buy yarn", "How much yarn <em>each gift</em> needs",
    card(head3(("GIFT", "YARN")) + rows(YARD, big=True)) + '<p style="font-size:23px;color:var(--ink2);margin-top:18px">Approximate, for medium (#4) yarn. Buy a little extra.</p>')

TIPS = [("Weave in ends twice", "Gifts get washed. Loose ends unravel."), ("Block it", "Pin it flat, mist with water, let it dry. Instant polish."),
        ("Add a tag", "Write the yarn and care instructions."), ("Wrap it with yarn", "Tie the gift with the same yarn you used.")]
tl = "".join(f'<div class="card" style="padding:26px 32px;margin-bottom:18px;display:flex;gap:20px;align-items:flex-start"><div style="flex:none;width:54px;height:54px;border-radius:50%;border:3px dashed var(--rose);color:var(--rose);font-family:PopB;font-size:26px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div style="font-family:PopB;color:var(--plum);font-size:32px">{a}</div><div style="font-size:26px;color:var(--ink2);margin-top:4px">{b}</div></div></div>' for i, (a, b) in enumerate(TIPS))
P["16_gift_finishing"] = pin_shell("Make it look store-bought", "4 tricks for a <em>professional</em> crochet gift", tl, top=430)

async def main():
    os.makedirs(f"{D}/pins2", exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1000, "height": 1500})
        for k, v in P.items():
            f = f"{D}/pins2/{k}.html"; open(f, "w").write(v)
            await pg.goto(f"file://{f}"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"{D}/pins2/{k}.jpg", type="jpeg", quality=90)
        await b.close()
asyncio.run(main())
