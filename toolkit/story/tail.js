window.renderFrame=(f)=>{const t=f/30;let i=0;for(let k=0;k<SHOTS.length;k++)if(t>=SHOTS[k][0])i=k;const s=SHOTS[i];const lt=t-s[0];const dur=(SHOTS[i+1]?SHOTS[i+1][0]:TOT)-s[0];
 G.forEach(g=>g.visible=false);ALL.forEach(c=>{c.m.visible=false;c.m.scale.setScalar(1);c.m.material.color.set("#ffffff")});STARS.visible=false;sky.visible=true;
 ["cnt","lab","diag","bad"].forEach(id=>{EL(id).style.opacity=0;EL(id).innerHTML="";EL(id).style.transform=""});
 const C={t,lt,dur,f,P:[0,1.5,6],Tg:[0,1,0],roll:0,red:0,post:null,blink:sd=>((t+sd)%3.1)<.1};
 C.pop=(id,html,t0=0,extra="")=>{const el=EL(id);el.style.opacity=lt>=t0?1:0;el.innerHTML=html;el.style.transform=`${id==="lab"?"translateX(-50%) ":""}${extra} scale(${Math.max(0,Math.min(1.08,back((lt-t0)/.25)))})`};
 C.slam=(id,html,t0,rot=-6)=>{const el=EL(id);const u=lt-t0;el.style.opacity=u>=0?1:0;el.innerHTML=html;el.style.transform=`${id==="lab"?"translateX(-50%) ":""}scale(${1+2.4*(1-eo(u/.16))}) rotate(${rot}deg)`;if(u>.14&&u<.5)C.roll=Math.sin(t*55)*.014*(1-(u-.14)/.36)};
 C.hookZoom=(far,near,y,ty,x=0)=>{const z=lerp(far,near,eo(lt/.45))-lt*.25;C.P=[x+.4*(1-eo(lt/.45)),y,z];C.Tg=[x,ty,0];C.roll=Math.sin(t*46)*.022*(1-cl(lt/.55))};
 s[1](C);
 cam.position.set(...C.P);cam.lookAt(...C.Tg);sky.position.copy(cam.position);STARS.position.copy(cam.position);cam.rotateZ(C.roll);cam.updateMatrixWorld();ALL.forEach(c=>c.orient());R.render(scene,cam);if(C.post)C.post();
 EL("turb").setAttribute("seed",f%40);EL("red").style.opacity=C.red;
 const q=EL("q");if(s[2]){q.style.opacity=1;q.style.transform=`scale(${Math.max(0,Math.min(1.06,back((lt-.05)/.28)))})`;const w=Math.sin(t*6)*3;EL("q1").style.transform=`rotate(${-3+w}deg)`;EL("q2").style.transform=`rotate(${3-w}deg)`}else q.style.opacity=0;
 captions(t);EL("fade").style.opacity=0;
 EL("flash").style.opacity=SHOTS.slice(1).map(s=>s[0]).reduce((a,s)=>Math.max(a,t>=s&&t<s+.1?1-(t-s)/.1:0),0)*.55;
};
window.CUTS=SHOTS.map(s=>s[0]);window.QT=SHOTS[SHOTS.length-1][0];
document.fonts.ready.then(()=>{window.READY=true});
</script></body></html>
