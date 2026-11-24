import os
D = "/home/claude/cheat"
FONT = "/usr/share/fonts/truetype/google-fonts"
CSS = f"""
@font-face{{font-family:Lora;src:url(file://{FONT}/Lora-Variable.ttf)}}
@font-face{{font-family:LoraI;src:url(file://{FONT}/Lora-Italic-Variable.ttf)}}
@font-face{{font-family:Pop;src:url(file://{FONT}/Poppins-Regular.ttf)}}
@font-face{{font-family:PopB;src:url(file://{FONT}/Poppins-Bold.ttf)}}
@font-face{{font-family:PopS;src:url(file://{FONT}/Poppins-Medium.ttf)}}
:root{{--bg:#F4ECDF;--card:#FFFBF4;--ink:#3A2233;--ink2:#6E5664;--plum:#4A2440;--rose:#C27A74;--sage:#7F9776;--mustard:#D4A043;--coral:#CF6448;--stitch:rgba(122,74,98,.35)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Pop,sans-serif;color:var(--ink);background:var(--bg);
 background-image:repeating-linear-gradient(45deg,rgba(74,36,64,.03) 0 2px,transparent 2px 7px),repeating-linear-gradient(-45deg,rgba(74,36,64,.03) 0 2px,transparent 2px 7px)}}
h1,h2,h3{{font-family:Lora,serif;color:var(--plum);font-weight:700}}
em{{font-family:LoraI,serif;color:var(--rose);font-style:normal}}
.card{{background:var(--card);border-radius:22px;position:relative;box-shadow:0 10px 30px rgba(74,36,64,.10)}}
.card:after{{content:"";position:absolute;inset:9px;border:2px dashed var(--stitch);border-radius:15px;pointer-events:none}}
.eyebrow{{font-family:PopB;letter-spacing:.2em;font-size:13px;color:var(--rose);text-transform:uppercase}}
table{{border-collapse:collapse;width:100%}}
td,th{{padding:5px 10px;text-align:left;border-bottom:1.5px dashed rgba(74,36,64,.15);font-size:14px}}
th{{font-family:PopB;color:var(--plum);font-size:12px;letter-spacing:.1em;text-transform:uppercase}}
td b{{font-family:PopB;color:var(--plum)}}
.chain{{height:18px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='18'%3E%3Cellipse cx='15' cy='9' rx='11' ry='5.5' fill='none' stroke='%23C27A74' stroke-width='2.4'/%3E%3C/svg%3E") repeat-x center}}
"""
P = "#4A2440"
def sym(kind, s=44, col=P):
    w = 3.2
    g = {
     "ch": f'<ellipse cx="22" cy="22" rx="14" ry="7.5" fill="none" stroke="{col}" stroke-width="{w}"/>',
     "sl": f'<circle cx="22" cy="22" r="6.5" fill="{col}"/>',
     "sc": f'<path d="M12 12 L32 32 M32 12 L12 32" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>',
     "hdc": f'<path d="M22 40 L22 8 M12 8 L32 8" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>',
     "dc": f'<path d="M22 42 L22 4 M12 4 L32 4 M16 26 L28 20" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>',
     "tr": f'<path d="M22 44 L22 2 M12 2 L32 2 M16 30 L28 24 M16 20 L28 14" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>',
     "mr": f'<circle cx="22" cy="22" r="12" fill="none" stroke="{col}" stroke-width="{w}"/><path d="M30 31 Q38 40 34 44" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>',
     "inc": f'<path d="M22 40 L10 8 M22 40 L34 8" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>',
     "dec": f'<path d="M22 6 L10 38 M22 6 L34 38" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>',
    }[kind]
    return f'<svg width="{s}" height="{s}" viewBox="0 0 44 44">{g}</svg>'

ABBR = [("ch","chain"),("sl st","slip stitch"),("sc","single crochet"),("hdc","half double crochet"),("dc","double crochet"),("tr","treble crochet"),
        ("st(s)","stitch(es)"),("sk","skip"),("inc","increase: 2 sts in the same st"),("dec","decrease: work 2 sts together"),("MR","magic ring"),
        ("rep","repeat"),("RS / WS","right side / wrong side"),("FO","fasten off")]
SYMS = [("ch","Chain"),("sl","Slip stitch"),("sc","Single crochet"),("hdc","Half double"),("dc","Double crochet"),("tr","Treble"),("mr","Magic ring"),("inc","Increase"),("dec","Decrease")]
UKUS = [("Single crochet (sc)","Double crochet (dc)"),("Half double crochet (hdc)","Half treble (htr)"),("Double crochet (dc)","Treble (tr)"),("Treble (tr)","Double treble (dtr)"),("Skip","Miss"),("Slip stitch (sl st)","Slip stitch (ss)")]
TURN = [("sc","1"),("hdc","2"),("dc","3"),("tr","4")]
YARN = [("0","Lace","1.5–2.25 mm"),("1","Super fine","2.25–3.5 mm"),("2","Fine","3.5–4.5 mm"),("3","Light","4.5–5.5 mm"),("4","Medium","5.5–6.5 mm"),("5","Bulky","6.5–9 mm"),("6","Super bulky","9–15 mm"),("7","Jumbo","15 mm +")]
MIST = [("Skipping the last stitch","It hides at the end of the row. Look for it every time."),
        ("Working into the turning chain","That adds a stitch each row. Check where your first stitch goes."),
        ("Pulling too tight","Tight loops are hard to hook into. Loosen your grip and let the yarn flow."),
        ("Not counting","Count at the end of every row. It's the fastest way to catch mistakes."),
        ("Wrong hook for your yarn","Check the yarn label: it tells you the right hook size.")]
KIT = "https://hookandfinish.gumroad.com/l/crochet-kit"

def page(html, w, h):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} html,body{{width:{w}px;height:{h}px;overflow:hidden}}</style></head><body>{html}</body></html>'

# ---------------- PDF (2 pages, 816x1056 = US Letter at 96dpi) ----------------
def pdf_html():
    abbr = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td></tr>" for a, b in ABBR)
    syms = "".join(f'<div style="text-align:center">{sym(k,40)}<div style="font-size:11.5px;margin-top:2px">{n}</div></div>' for k, n in SYMS)
    ukus = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in UKUS)
    turn = "".join(f'<div style="text-align:center"><div style="font-family:PopB;color:var(--plum);font-size:15px">{s}</div><div style="font-size:26px;font-family:Lora;color:var(--rose);font-weight:700">{n}</div><div style="font-size:11px;color:var(--ink2)">ch</div></div>' for s, n in TURN)
    yarn = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in YARN)
    mist = "".join(f'<div style="display:flex;gap:12px;margin:9px 0"><div style="flex:none;width:28px;height:28px;border-radius:50%;border:2px dashed var(--rose);color:var(--rose);font-family:PopB;display:flex;align-items:center;justify-content:center;font-size:13px">{i+1}</div><div><b style="font-family:PopB;color:var(--plum)">{a}.</b> {b}</div></div>' for i, (a, b) in enumerate(MIST))
    p1 = f'''<div style="width:816px;height:1056px;padding:48px 52px;position:relative">
 <div class="eyebrow">Hook &amp; Finish · Free printable</div>
 <h1 style="font-size:44px;line-height:1;margin:8px 0 4px">Crochet <em>Cheat Sheet</em></h1>
 <p style="color:var(--ink2);font-size:14px">Everything a beginner needs on one page. Print it and keep it next to your hook.</p>
 <div class="chain" style="margin:10px 0 14px;width:260px"></div>
 <div style="display:grid;grid-template-columns:1.05fr .95fr;gap:20px">
  <div class="card" style="padding:20px 20px 12px"><h3 style="font-size:20px;margin-bottom:6px">Abbreviations <span style="font-family:Pop;font-size:12px;color:var(--ink2)">(US terms)</span></h3><table>{abbr}</table></div>
  <div style="display:flex;flex-direction:column;gap:20px">
   <div class="card" style="padding:20px"><h3 style="font-size:20px;margin-bottom:10px">Stitch symbols</h3><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px 6px">{syms}</div></div>
   <div class="card" style="padding:20px"><h3 style="font-size:20px;margin-bottom:4px">Turning chains</h3><p style="font-size:12.5px;color:var(--ink2);margin-bottom:10px">Chain this many at the start of a row to reach the height of your stitch.</p><div style="display:grid;grid-template-columns:repeat(4,1fr)">{turn}</div></div>
  </div>
 </div>
 <div class="card" style="padding:16px 20px 8px;margin-top:16px"><h3 style="font-size:19px;margin-bottom:2px">US vs UK terms <span style="font-family:Pop;font-size:12px;color:var(--ink2)">(same stitch, different name)</span></h3><table><tr><th>US</th><th>UK</th></tr>{ukus}</table></div>
 <div style="position:absolute;bottom:26px;left:52px;right:52px;display:flex;justify-content:space-between;font-size:11px;color:var(--ink2)"><span>Hook &amp; Finish · Beginner crochet, calm and clear</span><span>1 / 2</span></div>
</div>'''
    p2 = f'''<div style="width:816px;height:1056px;padding:48px 52px;position:relative">
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
  <div class="card" style="padding:20px 20px 12px"><h3 style="font-size:20px;margin-bottom:4px">Yarn weight &amp; hook size</h3><p style="font-size:12.5px;color:var(--ink2);margin-bottom:6px">Recommended hook ranges. Your yarn label always wins.</p><table><tr><th>#</th><th>Weight</th><th>Hook</th></tr>{yarn}</table></div>
  <div class="card" style="padding:20px"><h3 style="font-size:20px;margin-bottom:8px">How to read a pattern line</h3>
   <div style="background:#F4ECDF;border-radius:12px;padding:12px 14px;font-family:PopS;color:var(--plum);font-size:15px">R2: ch 1, 2 sc in each st around, sl st to join. (12)</div>
   <div style="font-size:13px;line-height:1.55;margin-top:10px">
    <p><b style="font-family:PopB;color:var(--plum)">R2</b> = round 2</p>
    <p><b style="font-family:PopB;color:var(--plum)">ch 1</b> = make 1 chain</p>
    <p><b style="font-family:PopB;color:var(--plum)">2 sc in each st</b> = an increase in every stitch</p>
    <p><b style="font-family:PopB;color:var(--plum)">sl st to join</b> = close the round</p>
    <p><b style="font-family:PopB;color:var(--plum)">(12)</b> = you should have 12 stitches</p>
    <p style="margin-top:6px;color:var(--ink2)"><b style="font-family:PopB;color:var(--plum)">* … *</b> or <b style="font-family:PopB;color:var(--plum)">[ … ]</b> = repeat what's inside</p>
   </div></div>
 </div>
 <div class="card" style="padding:20px 22px 12px;margin-top:20px"><h3 style="font-size:20px;margin-bottom:4px">5 beginner mistakes (and the fix)</h3><div style="font-size:13.5px">{mist}</div></div>
 <div style="margin-top:20px;background:var(--plum);border-radius:22px;padding:26px 30px;color:#FBEFE2;position:relative">
  <div style="position:absolute;inset:9px;border:2px dashed rgba(241,217,166,.45);border-radius:15px"></div>
  <div class="eyebrow" style="color:#E8B85C">Ready for more?</div>
  <h2 style="color:#FBEFE2;font-size:28px;margin:6px 0 6px">From your first chain to a finished <span style="font-family:LoraI;color:#E8B85C">granny square</span> in 7 days</h2>
  <p style="font-size:14px;color:#EBD3DC;margin-bottom:14px">Tangle to Finished is our step-by-step beginner kit: one short lesson a day, 3 finished projects, a Fix-It Clinic and printables.</p>
  <a href="{KIT}" style="display:inline-block;background:var(--coral);color:#fff;font-family:PopB;padding:12px 24px;border-radius:999px;text-decoration:none;font-size:15px">Get the 7-day kit →</a>
  <span style="font-size:12px;color:#EBD3DC;margin-left:12px">hookandfinish.gumroad.com/l/crochet-kit</span>
 </div>
 <div style="position:absolute;bottom:26px;left:52px;right:52px;display:flex;justify-content:space-between;font-size:11px;color:var(--ink2)"><span>Free for personal use · © Hook &amp; Finish</span><span>2 / 2</span></div>
</div>'''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} @page{{size:816px 1056px;margin:0}} body{{width:816px}}</style></head><body>{p1}{p2}</body></html>'

# ---------------- PINS 1000x1500 ----------------
def pin_shell(eyebrow, title, body, footer="FREE CHEAT SHEET · LINK IN BIO", top=400):
    return page(f'''<div style="width:1000px;height:1500px;padding:70px 64px;position:relative">
 <div class="eyebrow" style="font-size:20px">{eyebrow}</div>
 <h1 style="font-size:84px;line-height:1.02;margin:16px 0 22px">{title}</h1>
 <div class="chain" style="width:320px;margin-bottom:10px"></div>
 <div style="position:absolute;left:64px;right:64px;top:{top}px;bottom:150px;display:flex;flex-direction:column;justify-content:center">{body}</div>
 <div style="position:absolute;bottom:56px;left:64px;right:64px;display:flex;align-items:center;justify-content:space-between">
  <div style="font-family:LoraI;color:var(--ink2);font-size:28px">Hook &amp; Finish</div>
  <div style="background:var(--plum);color:#FBEFE2;font-family:PopB;letter-spacing:.12em;font-size:21px;padding:16px 28px;border-radius:999px">{footer}</div>
 </div></div>''', 1000, 1500)

def rows(items, cols=2, big=False):
    fs = 36 if big else 31
    return "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:{22 if big else 17}px 4px;border-bottom:2px dashed rgba(74,36,64,.16);font-size:{fs}px">' + "".join(f'<span style="{"font-family:PopB;color:var(--plum)" if i==0 else ""}">{c}</span>' for i, c in enumerate(r)) + '</div>' for r in items)

PINS = {}
PINS["01_abbreviations"] = pin_shell("Save for later · US terms", "Crochet <em>abbreviations</em> every beginner needs",
    f'<div class="card" style="padding:26px 40px">{rows([(a,b) for a,b in ABBR[:11]])}</div>')
PINS["02_us_vs_uk"] = pin_shell("Same stitch, different name", "US vs UK <em>crochet terms</em>",
    f'<div class="card" style="padding:30px 40px"><div style="display:flex;justify-content:space-between;font-family:PopB;color:var(--rose);font-size:24px;letter-spacing:.14em;padding:0 4px 10px">US<span>UK</span></div>{rows([(a,b) for a,b in UKUS], big=True)}</div><p style="font-size:26px;color:var(--ink2);margin-top:26px">Check which terms your pattern uses before you start.</p>')
PINS["03_yarn_hook"] = pin_shell("Print it · keep it by your hook", "Yarn weight &amp; <em>hook size</em> chart",
    f'<div class="card" style="padding:26px 40px"><div style="display:flex;justify-content:space-between;font-family:PopB;color:var(--rose);font-size:22px;letter-spacing:.14em;padding:0 4px 8px">WEIGHT<span>HOOK</span></div>{rows([(f"{a} · {b}",c) for a,b,c in YARN])}</div><p style="font-size:24px;color:var(--ink2);margin-top:20px">Recommended ranges. Your yarn label always wins.</p>')
symgrid = "".join(f'<div class="card" style="padding:40px 10px;text-align:center">{sym(k,120)}<div style="font-size:27px;margin-top:8px;font-family:PopS;color:var(--plum)">{n}</div></div>' for k, n in SYMS)
PINS["04_symbols"] = pin_shell("Read any crochet chart", "Crochet <em>stitch symbols</em> explained",
    f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">{symgrid}</div>')
ladder = "".join(f'<div class="card" style="padding:36px 10px;text-align:center"><div style="height:{150+i*55}px;display:flex;align-items:flex-end;justify-content:center">{sym(k,int(90+i*30))}</div><div style="font-family:PopB;color:var(--plum);font-size:30px;margin-top:10px">{s}</div><div style="font-family:Lora;font-weight:700;color:var(--rose);font-size:64px;line-height:1">{n}</div><div style="font-size:22px;color:var(--ink2)">turning ch</div></div>' for i, ((s, n), k) in enumerate(zip(TURN, ["sc", "hdc", "dc", "tr"])))
PINS["05_turning_chains"] = pin_shell("The rule nobody explains", "How many <em>turning chains?</em>",
    f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;align-items:end">{ladder}</div><p style="font-size:27px;color:var(--ink2);margin-top:30px;line-height:1.4">Chain this many at the start of each row so your edges stay straight.</p>')
mistpin = "".join(f'<div class="card" style="padding:28px 32px;margin-bottom:18px;display:flex;gap:20px;align-items:flex-start"><div style="flex:none;width:54px;height:54px;border-radius:50%;border:3px dashed var(--rose);color:var(--rose);font-family:PopB;font-size:26px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div style="font-family:PopB;color:var(--plum);font-size:32px">{a}</div><div style="font-size:26px;color:var(--ink2);margin-top:4px">{b}</div></div></div>' for i, (a, b) in enumerate(MIST))
PINS["06_mistakes"] = pin_shell("Fix these and level up", "5 beginner <em>crochet mistakes</em>", mistpin)
PINS["07_read_pattern"] = pin_shell("Pattern decoder", "How to <em>read</em> a crochet pattern",
    '''<div class="card" style="padding:44px 44px"><div style="background:#F4ECDF;border-radius:16px;padding:26px 30px;font-family:PopS;color:var(--plum);font-size:38px;line-height:1.3">R2: ch 1, 2 sc in each st around, sl st to join. (12)</div>
    <div style="font-size:33px;line-height:1.85;margin-top:28px">
    <p><b style="font-family:PopB;color:var(--rose)">R2</b> → round 2</p><p><b style="font-family:PopB;color:var(--rose)">ch 1</b> → make 1 chain</p>
    <p><b style="font-family:PopB;color:var(--rose)">2 sc in each st</b> → increase in every stitch</p><p><b style="font-family:PopB;color:var(--rose)">sl st to join</b> → close the round</p>
    <p><b style="font-family:PopB;color:var(--rose)">(12)</b> → you should have 12 stitches</p></div></div>''')
mrsteps = [("Wrap", "Wrap the yarn around two fingers to make a loop, tail in front."),
           ("Pull up", "Insert the hook under the loop, grab the working yarn, pull up a loop."),
           ("Chain 1", "Yarn over and pull through to lock it. This chain doesn't count."),
           ("Close", "Work your stitches into the ring, then pull the tail to close the hole.")]
mrpin = "".join(f'<div class="card" style="padding:24px 30px;margin-bottom:16px;display:flex;gap:22px;align-items:center"><div style="flex:none;width:64px;height:64px;border-radius:50%;background:var(--plum);color:#FBEFE2;font-family:PopB;font-size:30px;display:flex;align-items:center;justify-content:center">{i+1}</div><div><div style="font-family:PopB;color:var(--plum);font-size:31px">{a}</div><div style="font-size:24px;color:var(--ink2);margin-top:2px">{b}</div></div></div>' for i, (a, b) in enumerate(mrsteps))
PINS["08_magic_ring"] = pin_shell("Start amigurumi the right way", "Magic ring in <em>4 easy steps</em>",
    f'<div style="display:flex;justify-content:center;margin:-10px 0 20px">{sym("mr",150)}</div>{mrpin}')
stack = "".join(f'<div style="display:flex;align-items:center;gap:26px;padding:30px 0;border-bottom:2px dashed rgba(74,36,64,.16)"><div style="width:110px;display:flex;justify-content:center">{sym(k,int(60+i*16))}</div><div><div style="font-family:PopB;color:var(--plum);font-size:38px">{n}</div><div style="font-size:27px;color:var(--ink2)">{d}</div></div></div>' for i, (k, n, d) in enumerate([("sc", "Single crochet", "Short and dense. Great for amigurumi."), ("hdc", "Half double", "A little taller. Quick and cozy."), ("dc", "Double crochet", "Tall and airy. Granny squares love it."), ("tr", "Treble", "The tallest basic stitch. Lacy and fast.")]))
PINS["09_stitch_heights"] = pin_shell("The 4 basic stitches", "Crochet stitches from <em>short to tall</em>",
    f'<div class="card" style="padding:20px 40px">{stack}</div>')
# promo pin showing the free sheet
PINS["10_free_sheet"] = pin_shell("Free printable · instant download", "The free <em>crochet cheat sheet</em> beginners save",
    '''<div style="display:flex;justify-content:center;margin-top:10px"><div style="position:relative;width:640px;height:820px">
    <img src="file:///home/claude/cheat/p2.png" style="position:absolute;left:150px;top:40px;width:470px;border-radius:12px;box-shadow:0 20px 50px rgba(0,0,0,.25);transform:rotate(5deg)">
    <img src="file:///home/claude/cheat/p1.png" style="position:absolute;left:10px;top:0;width:500px;border-radius:12px;box-shadow:0 24px 60px rgba(0,0,0,.3);transform:rotate(-4deg)">
    </div></div>''', footer="FREE DOWNLOAD · LINK IN BIO")

if __name__ == "__main__":
    os.makedirs(f"{D}/pins", exist_ok=True)
    open(f"{D}/sheet.html", "w").write(pdf_html())
    for k, v in PINS.items():
        open(f"{D}/pins/{k}.html", "w").write(v)
