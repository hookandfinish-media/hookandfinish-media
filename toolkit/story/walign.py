import json, sys, re, numpy as np, soundfile as sf
from scipy.signal import resample_poly
from pocketsphinx import Decoder
NUM={"552":"five hundred fifty two","1918":"nineteen eighteen","1847":"eighteen forty seven","1997":"nineteen ninety seven","1904":"nineteen oh four","1930s":"nineteen thirties"}
n=sys.argv[1]; d=json.load(open(f"data{n}.json")); x,sr=sf.read(f"voice{n}.wav"); x16=resample_poly(x,16000,sr).astype(np.float32)
dec=Decoder(lm=None)
def clean(w): return re.sub(r"[^a-z']","",w.lower())
out=[]
for li,(a,b,txt) in enumerate(d["vo"]):
    ws=txt.replace("...","... ").split()
    spoken=[];owner=[]
    for i,w in enumerate(ws):
        key=re.sub(r"[^0-9s]","",w) if re.search(r"\d",w) else None
        parts=NUM.get(key,key).split() if key else [clean(w)]
        for p in parts:
            if p: spoken.append(p);owner.append(i)
    keep=[k for k,p in enumerate(spoken) if dec.lookup_word(p)]
    if len(keep)<len(spoken): print("unknown",[spoken[k] for k in range(len(spoken)) if k not in keep])
    spoken=[spoken[k] for k in keep];owner=[owner[k] for k in keep]
    sg=None
    for pa,pb in [(.3,.35),(.1,.15),(.5,.6),(.05,.5),(.4,.1)]:
        s0=max(0,a-pa);e0=min(len(x16)/16000,b+pb);seg=x16[int(s0*16000):int(e0*16000)]
        try:
            dec.set_align_text(" ".join(spoken));dec.start_utt();dec.process_raw((seg*32767).astype(np.int16).tobytes(),full_utt=True);dec.end_utt();sg=dec.seg()
        except Exception as ex: sg=None
        if sg is not None: break
    if sg is None: print("FAIL line",n,li);out+=[w for w in d["words"] if w[3]==li];continue
    got=[(s.word,s.start_frame/100+s0,(s.end_frame+1)/100+s0) for s in sg if s.word not in ("<sil>","<s>","</s>","(NULL)") and not s.word.startswith("[")]
    got=[(re.sub(r"\(\d+\)","",w),st,en) for w,st,en in got]
    if len(got)!=len(spoken): print("MISMATCH",n,li,len(got),len(spoken),got[:3]);t=[w for w in d["words"] if w[3]==li];out+=t;continue
    for i,w in enumerate(ws):
        idx=[k for k,o in enumerate(owner) if o==i]
        if not idx: out.append(None); continue
        out.append([round(got[idx[0]][1],3),round(got[idx[-1]][2],3),w,li])
# fill unknown words by interpolation within the line
est=d["words"]
for k,w in enumerate(out):
    if w is None:
        prev=next((out[j] for j in range(k-1,-1,-1) if out[j]),None); nxt=next((out[j] for j in range(k+1,len(out)) if out[j]),None)
        e=est[k]; a0=prev[1] if prev else e[0]; b0=nxt[0] if nxt else e[1]; out[k]=[round(a0,3),round(max(a0+.05,b0),3),e[2],e[3]]
d["words"]=out;json.dump(d,open(f"data{n}.json","w"))
print(n,"aligned",len(out))
