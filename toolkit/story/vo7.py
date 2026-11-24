import json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
k=Kokoro("/home/claude/tts/kokoro.onnx","/home/claude/tts/voices.bin"); v=k.get_voice_style("am_michael")
L=json.load(open("lines7.json")); out=[]
for i,t in enumerate(L):
    s,sr=k.create(t,voice=v,speed=1.15,lang="en-us"); out.append(s); out.append(np.zeros(int(.25*sr)))
sf.write("a7.wav",np.concatenate(out),sr); print("ok",sum(len(x) for x in out)/sr)
