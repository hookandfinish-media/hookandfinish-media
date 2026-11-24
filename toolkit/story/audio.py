import json, sys, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve, resample_poly
from scipy.io import wavfile
import soundfile as sf
D=sys.argv[1]; MOOD=sys.argv[2]
SR=44100; DD=json.load(open(f"{D}/data.json")); DUR=DD["total"]; N=int(DUR*SR); CUTS=json.load(open(f"{D}/cuts.json")); QT=CUTS[-1]
EX=json.load(open(f"{D}/sfx.json")) if __import__("os").path.exists(f"{D}/sfx.json") else []
rng=np.random.default_rng(5); mus=np.zeros(N); sfx=np.zeros(N)
def put(buf,sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if j>i and i>=0: buf[i:j]+=sig[:j-i]*g
mtof=lambda m:440*2**((m-69)/12); tt=lambda d:np.arange(int(d*SR))/SR
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],'bandpass',fs=SR,output='sos'),x)
def nz(d): return rng.standard_normal(int(d*SR))
def pluck(m,d=.3,v=.5): t=tt(d);f=mtof(m);return v*(np.sin(2*np.pi*f*t)+.4*np.sin(2*np.pi*2*f*t)*np.exp(-t/.06))*np.exp(-t/.1)
def bell(m,d=.6,v=.3): t=tt(d);f=mtof(m);return v*(np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*3.01*f*t))*np.exp(-t/.2)
def kick(v=.7): t=tt(.25);return v*np.sin(2*np.pi*np.cumsum(50+90*np.exp(-t/.025))/SR)*np.exp(-t/.08)
def clap(v=.35): t=tt(.15);return v*bp(nz(.15),900,5000)*np.exp(-t/.035)
def boom(t0,g=.9): x=tt(.7); put(sfx,(np.sin(2*np.pi*np.cumsum(55+110*np.exp(-x/.04))/SR)*np.exp(-x/.22)+bp(nz(.7),200,3000)*np.exp(-x/.05)*.5)*g,t0)
M={"silk":(118,[62,65,69,67,65,69,72,70, 62,65,69,74,72,69,67,65],[50,50,46,46,48,48,45,45]),
   "sheep":(124,[72,74,76,77,79,77,76,74, 72,76,79,84,81,79,77,76],[53,53,58,58,60,60,53,53]),
   "irish":(112,[69,71,72,74,76,74,72,71, 69,72,76,79,77,76,74,72],[45,45,48,48,43,43,45,45]),
   "math":(120,[72,76,79,83,81,79,76,74, 72,74,76,79,81,83,84,79],[48,48,45,45,41,41,43,43]),
   "aran":(104,[62,64,65,67,69,67,65,64, 62,65,69,74,72,69,67,65],[50,50,46,46,43,43,45,45])}[MOOD]
bpm,mel,bass=M; b=60/bpm; t=0.0; k=0
while t<QT-.05:
    if k%4==0: put(mus,kick(.6),t)
    if k%4==2: put(mus,clap(.26),t)
    put(mus,pluck(bass[(k//4)%8]-12,.22,.5) if k%2==0 else pluck(bass[(k//4)%8],.16,.26),t)
    if k%2==0: put(mus,bell(mel[(k//2)%16],.35,.13),t)
    t+=b/2; k+=1
x=tt(DUR-QT); pad=sum(np.sin(2*np.pi*mtof(m)*x) for m in [bass[0]+12,bass[0]+15+(MOOD!='sheep'),bass[0]+19])*.07*np.minimum(1,x/.2)*np.exp(-x/2.0); put(mus,pad,QT)
boom(0.0,1.0); d=.5; x=tt(d); put(sfx,bp(nz(d),400,8000)*(x/d)**2*.6,0.0)
for s0 in CUTS[1:]: d=.32; x=tt(d); put(sfx,bp(nz(d),600,7000)*np.sin(np.pi*x/d)*.45,s0-.15); put(sfx,bell(84,.25,.12),s0+.08)
put(sfx,bell(mel[0]+12,1.2,.35),QT+.03)
for e in EX:
    kind,t0=e[0],e[1]
    if kind=="boom": boom(t0,e[2] if len(e)>2 else .9)
    elif kind=="ding": put(sfx,bell(84,.5,.5)+bell(91,.5,.25),t0)
    elif kind=="baa":
        d=.7; x=tt(d); f=(e[2] if len(e)>2 else 320)*(1+.03*np.sin(2*np.pi*7*x))*np.interp(x,[0,.1,d],[1.1,1,.85]); ph=2*np.pi*np.cumsum(f)/SR
        s=sum(np.sin(kk*ph)/kk for kk in range(1,12)); s=bp(s,400,3000)*(1+.6*np.sin(2*np.pi*22*x)); put(sfx,s*np.minimum(1,x/.05)*np.minimum(1,(d-x)/.2)*.5,t0)
    elif kind=="ticks":
        tk=t0
        while tk<e[2]: x=tt(.04); put(sfx,bp(nz(.04),2500,8000)*np.exp(-x/.008)*.5,tk); tk+=e[3] if len(e)>3 else .22
    elif kind=="count":
        for i in range(10): put(sfx,np.sin(2*np.pi*(900+i*80)*tt(.05))*np.exp(-tt(.05)/.015)*.3,t0+i*.1)
        put(sfx,bell(88,.8,.5),t0+1.05)
    elif kind=="thunder":
        d=2.2; x=tt(d); put(sfx,sosfilt(butter(2,300,'lowpass',fs=SR,output='sos'),nz(d))*np.exp(-x/.7)*3.0,t0); put(sfx,bp(nz(.3),800,6000)*np.exp(-tt(.3)/.05)*.8,t0)
    elif kind=="scratch":
        d=.45; x=tt(d); put(sfx,bp(nz(d),300,4000)*np.sin(2*np.pi*np.cumsum(8-14*x/d)/SR*40)*(1-x/d)*.9,t0)
    elif kind=="waves":
        d=e[2]-t0; x=tt(d); put(sfx,sosfilt(butter(2,900,'lowpass',fs=SR,output='sos'),nz(d))*(.5+.5*np.sin(2*np.pi*.4*x))**2*.6,t0)
    elif kind=="crowd":
        d=1.6; x=tt(d); put(sfx,bp(nz(d),800,6000)*(np.abs(np.sin(2*np.pi*13*x))+.3)*np.exp(-x/.6)*.5,t0)
    elif kind=="rustle":
        d=e[2]-t0; x=tt(d); put(sfx,bp(nz(d),1500,6000)*(.4+.6*np.abs(np.sin(2*np.pi*1.5*x)))*.25,t0)
def rev(x,d=1.2,mix=.16):
    n=int(d*SR); t3=np.arange(n)/SR; ir=rng.standard_normal(n)*np.exp(-t3/(d/5)); ir/=np.sqrt((ir**2).sum()); return (1-mix)*x+mix*fftconvolve(x,ir)[:len(x)]
mus=rev(mus); sfx=rev(sfx,1.0,.12)
v,vsr=sf.read(f"{D}/voice.wav"); v=resample_poly(v,SR,vsr)[:N]; v=np.pad(v,(0,max(0,N-len(v))))
def grms(x):
    w=int(.4*SR); r=np.array([np.sqrt((x[i:i+w]**2).mean()) for i in range(0,len(x)-w,w)]); r=r[r>10**(-40/20)*np.abs(x).max()]; return np.sqrt((r**2).mean())
rv=grms(v); mus*=(.45*rv)/grms(mus); sfx*=(.5*rv)/grms(sfx)
pk=np.abs(v).max()*.7; sfx=np.where(np.abs(sfx)>pk,np.sign(sfx)*(pk+(np.abs(sfx)-pk)*.2),sfx)
mix=v+mus+sfx; mix/=max(1.0,np.abs(mix).max()/.95)
wavfile.write(f"{D}/mix.wav",SR,(np.stack([mix,mix],1)*32767).astype(np.int16)); print("audio ok")
