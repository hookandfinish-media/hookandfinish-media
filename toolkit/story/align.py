import soundfile as sf, numpy as np, json, sys, re
EP={
1:dict(starts=[0,3,7,9,11,14],L=["Two monks smuggled the world's biggest secret... inside walking sticks!","For centuries, only China knew how silk was made. Leaking the secret could cost your life.","Around the year 552, two monks walked into the Roman emperor's palace.","Inside their hollow canes: silkworm eggs.","That one smuggle gave Europe its own silk... for over six hundred years.","Would you have risked it?"]),
2:dict(starts=[0,3,7,9,14],L=["In 1918, the White House lawn... was mowed by sheep!","During World War One, President Woodrow Wilson wanted to save manpower... so he brought in a flock.","The sheep grazed right on the White House lawn.","Then their wool was auctioned for the Red Cross. It raised over fifty thousand dollars!","Would you swap your lawnmower for a sheep?"]),
3:dict(starts=[0,3,6,10,13],L=["During Ireland's Great Famine, families survived... with a crochet hook.","In 1847, a woman named Cassandra Hand started lace classes in her front room.","Old Venetian lace took two hundred hours for one small piece. Crochet was much faster.","Soon whole families were crocheting lace... and selling it to survive.","Could your hobby feed your family?"]),
4:dict(starts=[0,3,6,10,14],L=["Mathematicians couldn't build this shape... until a woman picked up a crochet hook.","It's called a hyperbolic plane. The old models were fragile paper that fell apart.","In 1997, Daina Taimina crocheted one... adding extra stitches every row.","It curled into this. Coral reefs and lettuce leaves grow the same way!","Still think crochet is just for grannies?"]),
5:dict(starts=[0,2,4,5,7,8],L=["Every Irish fisherman's sweater had a secret pattern... so his family could identify him if he drowned.","Beautiful story, right? There's just one problem.","It isn't true.","The legend grew from a 1904 play... and sellers loved it.","Real Aran sweaters only appear in the 1930s.","Did you believe it too?"]),
}
n=int(sys.argv[1]); E=EP[n]; x,sr=sf.read(f"a{n}.wav")
w=int(.01*sr); e=np.array([np.sqrt((x[i:i+w]**2).mean()) for i in range(0,len(x)-w,w)]); on=e>e.max()*.035
segs=[];s=None
for i,o in enumerate(on):
    if o and s is None: s=i
    if not o and s is not None: segs.append([s*.01,i*.01]); s=None
if s is not None: segs.append([s*.01,len(on)*.01])
m=[segs[0]]
for a,b in segs[1:]:
    if a-m[-1][1]<.13: m[-1][1]=b
    else: m.append([a,b])
m=[s for s in m if s[1]-s[0]>.06]
st=E["starts"]+[len(m)]; out=[]; t=0; words=[]; V=[]
for li in range(len(E["L"])):
    lsegs=m[st[li]:st[li+1]]; newsegs=[]
    for si,(a,b) in enumerate(lsegs):
        if out: gap=.3 if si==0 else min(.24, a-lsegs[si-1][1]); out.append(np.zeros(int(gap*sr))); t+=gap
        a0=max(0,a-.03); b0=min(len(x)/sr,b+.08); c=x[int(a0*sr):int(b0*sr)].copy(); f=int(.01*sr); c[:f]*=np.linspace(0,1,f); c[-f:]*=np.linspace(1,0,f)
        newsegs.append([t+(a-a0),t+(a-a0)+(b-a)]); out.append(c); t+=len(c)/sr
    ws=E["L"][li].replace("...","... ").split(); wts=[max(1.5,len(re.sub(r"[^A-Za-z0-9]","",ww))) for ww in ws]; tot=sum(wts)
    voiced=sum(b-a for a,b in newsegs); 
    def at(p):
        for a,b in newsegs:
            if p<=b-a: return a+p
            p-=b-a
        return newsegs[-1][1]
    acc=0
    for ww,wt in zip(ws,wts):
        a=at(acc/tot*voiced); acc+=wt; b=at(acc/tot*voiced-1e-4); words.append([round(a,3),round(b,3),ww,li])
    V.append([round(newsegs[0][0],3),round(newsegs[-1][1],3),E["L"][li]])
out.append(np.zeros(int(.5*sr))); t+=.5
sf.write(f"voice{n}.wav",np.concatenate(out),sr)
json.dump({"vo":V,"words":words,"total":round(t,2),"starts":[v[0] for v in V]},open(f"data{n}.json","w"))
print(n,round(t,2),[(v[0],v[1]) for v in V])
