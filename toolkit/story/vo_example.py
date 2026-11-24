import json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro("/home/claude/tts/kokoro.onnx", "/home/claude/tts/voices.bin")
v=k.get_voice_style("am_michael")
L=["The computer that landed on the Moon... was woven by hand!",
"In the nineteen sixties, NASA needed a computer small enough for a spaceship.",
"So they stored the software... in wire.",
"And wait until you hear who built it.",
"Women in a Massachusetts factory threaded copper wire through tiny rings.",
["Through the ring:","one.","Around it:","zero."],
"Engineers called it Little Old Lady memory.",
"In nineteen sixty-nine, it guided Apollo eleven to the Moon.",
"Still think handcraft is just a hobby?"]
GAP=[0,.12,.12,.1,.14,.12,.14,.14,.2]
import sys; SPD=float(sys.argv[1]); sr=24000; full=[]; vo=[]; words=[]; t=0
for i,txt in enumerate(L):
    parts=txt if isinstance(txt,list) else [txt]; t+=GAP[i]; full.append(np.zeros(int(GAP[i]*sr))); st=t
    for pi,pt in enumerate(parts):
        s,sr=k.create(pt,voice=v,speed=SPD,lang="en-us")
        idx=np.where(np.abs(s)>0.008)[0]; s=s[max(0,idx[0]-300):idx[-1]+1500]
        if pi: full.append(np.zeros(int(.12*sr))); t+=.12
        p0=t; d=len(s)/sr; full.append(s); t+=d
        ws=pt.split(); wts=[max(1.6,len(w.strip(".,!?"))) + (2.5 if w[-1] in ".,!?" else 0) for w in ws]; a=p0+.03; tot=sum(wts)
        for w,wt in zip(ws,wts): dd=(d-.1)*wt/tot; words.append([round(a,3),round(a+dd,3),w,i]); a+=dd
    txt=" ".join(parts); vo.append([round(st,3),round(t,3),txt]); continue
    ws=txt.replace("...","… ").split()
    wts=[max(1.6,len(w.strip(".,!?…:"))) + (2.5 if w[-1] in ".,!?…:" else 0) for w in ws]
    a=st+.05; span=d-.15; tot=sum(wts)
    for w,wt in zip(ws,wts):
        dd=span*wt/tot; ww=w.replace("…","").strip()
        if ww: words.append([round(a,3),round(a+dd,3),ww,i])
        a+=dd
t+=.45; full.append(np.zeros(int(.45*sr)))
out=[]; i=0
while i<len(words):
    w=words[i]; nx=words[i+1] if i+1<len(words) else None
    if w[2]=="nineteen" and nx: out.append([w[0],nx[1],{"sixties,":"1960s,","sixty-nine,":"1969,"}[nx[2]],w[3]]); i+=2; continue
    if w[2]=="eleven": w[2]="11"
    out.append(w); i+=1
words=out
sf.write("voice.wav",np.concatenate(full),sr)
json.dump({"vo":vo,"words":words,"total":round(t,2),"starts":[x[0] for x in vo]},open("data.json","w"))
print(round(t,2),[ (x[0],x[1]) for x in vo])
