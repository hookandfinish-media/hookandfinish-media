# forced-align whole script on raw audio, then shorten long pauses; writes voiceN.wav + dataN.json
import json, sys, re, numpy as np, soundfile as sf
from scipy.signal import resample_poly
from pocketsphinx import Decoder
NUM={"1847":"eighteen forty seven","1904":"nineteen oh four","1930s":"nineteen thirties","1997":"nineteen ninety seven"}
n=sys.argv[1]; L=json.load(open(f"lines{n}.json")); x,sr=sf.read(f"a{n}.wav"); x16=(resample_poly(x,16000,sr)*32767).astype(np.int16)
dec=Decoder(lm=None)
def clean(w): return re.sub(r"[^a-z']","",w.lower())
words=[];spoken=[];owner=[]
for li,txt in enumerate(L):
    for w in txt.replace("...","... ").split():
        wi=len(words);words.append([w,li])
        key=re.sub(r"[^0-9s]","",w) if re.search(r"\d",w) else None
        for p in (NUM.get(key,key).split() if key else [clean(w)]):
            if p and dec.lookup_word(p): spoken.append(p);owner.append(wi)
            elif p: print("unknown",p)
dec.set_align_text(" ".join(spoken));dec.start_utt();dec.process_raw(x16.tobytes(),full_utt=True);dec.end_utt()
sg=[s for s in dec.seg() if s.word not in ("<sil>","<s>","</s>","(NULL)") and not s.word.startswith("[")]
assert len(sg)==len(spoken),(len(sg),len(spoken))
T=[None]*len(words)
for s,o in zip(sg,owner):
    a,b=s.start_frame/100,(s.end_frame+1)/100
    T[o]=[a,b] if T[o] is None else [T[o][0],b]
for i in range(len(T)):
    if T[i] is None:
        p=next(T[j] for j in range(i-1,-1,-1) if T[j]); q=next((T[j] for j in range(i+1,len(T)) if T[j]),[p[1]+.4])
        T[i]=[p[1],q[0]]
# build trimmed audio: cut gaps between consecutive words
keep=[];cur=max(0,T[0][0]-.05);out=[];newT=[];shift=0;t_out=0
segs=[];start=max(0,T[0][0]-.05)
for i in range(len(T)):
    if i+1<len(T):
        gap=T[i+1][0]-T[i][1]; mx=.3 if words[i+1][1]!=words[i][1] else .22
        if gap>mx+.05:
            segs.append((start,T[i][1]+mx/2)); start=T[i+1][0]-mx/2
segs.append((start,min(len(x)/sr,T[-1][1]+.08)))
mapping=[];t=0
for a,b in segs:
    c=x[int(a*sr):int(b*sr)].copy();f=int(.008*sr);c[:f]*=np.linspace(0,1,f);c[-f:]*=np.linspace(1,0,f);out.append(c);mapping.append((a,b,t));t+=len(c)/sr
def mp(v):
    for a,b,o in mapping:
        if a-1e-6<=v<=b+1e-6: return o+(v-a)
    best=min(mapping,key=lambda m:min(abs(v-m[0]),abs(v-m[1]))); return best[2]+(min(max(v,best[0]),best[1])-best[0])
out.append(np.zeros(int(.5*sr)));t+=.5
W=[[round(mp(T[i][0]),3),round(mp(T[i][1]),3),words[i][0],words[i][1]] for i in range(len(words))]
V=[];[V.append([min(w[0] for w in W if w[3]==li),max(w[1] for w in W if w[3]==li),L[li]]) for li in range(len(L))]
sf.write(f"voice{n}.wav",np.concatenate(out),sr);json.dump({"vo":V,"words":W,"total":round(t,2),"starts":[v[0] for v in V]},open(f"data{n}.json","w"))
print(n,"raw",round(len(x)/sr,2),"->",round(t,2),[(round(v[0],2),round(v[1],2)) for v in V])
