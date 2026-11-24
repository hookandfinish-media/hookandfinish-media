const CREAM="#fbf4e4",SHADE="#e8dcc2";
function drawSheep(g,o){g.setTransform(1,0,0,1,0,0);const f=o.fluff??.15,sh=f<.06,ground=772,leg=74,ex=o.expr||"happy",ph=o.phase||0;
 const R=sh?0:lerp(150,322,f);const cy=ground-leg-R*.74+(o.bob||0);
 // legs
 const spread=sh?95:Math.min(R*.95,240);[-1,-.38,.38,1].forEach((k,i)=>{const x=400+k*spread*.5,lift=o.walk?Math.max(0,Math.sin(6.283*(ph+(i%2)*.5)))*20:0;
  g.fillStyle="#3d302e";g.strokeStyle=INK;g.lineWidth=9;g.beginPath();g.roundRect(x-18,ground-leg-40-lift,36,leg+40,14);g.fill();g.stroke();g.fillStyle="#241a1a";g.beginPath();g.roundRect(x-20,ground-16-lift,40,18,7);g.fill();g.stroke()});
 let hx=400+(o.look||0)*28,hy;
 if(sh){const by=ground-leg-70+(o.bob||0);g.fillStyle="#f6dcd2";g.strokeStyle=INK;g.lineWidth=13;g.beginPath();g.ellipse(400,by,150,96,0,0,7);g.fill();g.stroke();
  g.strokeStyle="#e4b8ad";g.lineWidth=6;for(const dx of [-70,0,70]){g.beginPath();g.arc(400+dx,by+10,30,.3,2.8);g.stroke()}hy=by-70}
 else{const n=Math.round(13+f*15),r=R*.33,pts=[];for(let i=0;i<n;i++){const a=i/n*6.283+.2;pts.push([400+Math.cos(a)*R*.86,cy+Math.sin(a)*R*.7])}
  g.strokeStyle=INK;g.lineWidth=16;pts.forEach(([x,y])=>{g.beginPath();g.arc(x,y,r,0,7);g.stroke()});
  g.fillStyle=CREAM;pts.forEach(([x,y])=>{g.beginPath();g.arc(x,y,r,0,7);g.fill()});g.beginPath();g.ellipse(400,cy,R*.86,R*.7,0,0,7);g.fill();
  g.fillStyle=SHADE;g.globalAlpha=.55;g.beginPath();g.ellipse(400,cy+R*.42,R*.78,R*.28,0,0,7);g.fill();g.globalAlpha=1;
  let s2=7;const r2=()=>{s2=(s2*16807)%2147483647;return s2/2147483647};g.strokeStyle="#ddd0b2";g.lineWidth=7;g.lineCap="round";
  for(let i=0;i<Math.round(10+f*26);i++){const a=r2()*6.283,d=Math.sqrt(r2())*.78;g.beginPath();g.arc(400+Math.cos(a)*R*.86*d,cy+Math.sin(a)*R*.7*d,10+r2()*14,r2()*3,r2()*3+3);g.stroke()}
  hy=cy+R*(f>.6?.5:.36)}
 // ears
 for(const s of [-1,1]){g.save();g.translate(hx+s*74,hy-30);g.rotate(s*.45);g.fillStyle="#f0c8b8";g.strokeStyle=INK;g.lineWidth=9;g.beginPath();g.ellipse(0,0,44,19,0,0,7);g.fill();g.stroke();g.restore()}
 // face
 g.fillStyle="#f8ece2";g.strokeStyle=INK;g.lineWidth=11;g.beginPath();g.ellipse(hx,hy,68,82,0,0,7);g.fill();g.stroke();
 const ey=hy-6,lk=(o.look||0)*6;
 g.fillStyle="#f4a0a8";g.globalAlpha=sh?.8:.5;for(const s of [-1,1]){g.beginPath();g.ellipse(hx+s*44,hy+24,15,9,0,0,7);g.fill()}g.globalAlpha=1;
 if(o.blink&&ex!=="happy"&&ex!=="shock"){g.strokeStyle=INK;g.lineWidth=8;for(const s of [-1,1]){g.beginPath();g.moveTo(hx+s*26-12,ey);g.lineTo(hx+s*26+12,ey);g.stroke()}}
 else if(ex==="happy"){g.strokeStyle=INK;g.lineWidth=9;g.lineCap="round";for(const s of [-1,1]){g.beginPath();g.arc(hx+s*26,ey+5,12,3.5,5.9);g.stroke()}}
 else if(ex==="shock"){for(const s of [-1,1]){g.fillStyle="#fff";g.strokeStyle=INK;g.lineWidth=7;g.beginPath();g.arc(hx+s*27,ey,21,0,7);g.fill();g.stroke();g.fillStyle=INK;g.beginPath();g.arc(hx+s*27,ey+2,8,0,7);g.fill()}}
 else{for(const s of [-1,1]){g.fillStyle=INK;g.beginPath();g.ellipse(hx+s*26+lk,ey,11,14,0,0,7);g.fill();g.fillStyle="#fff";g.beginPath();g.arc(hx+s*26+lk+4,ey-5,4,0,7);g.fill()}
  if(ex==="sneaky"){g.fillStyle="#f8ece2";g.strokeStyle=INK;g.lineWidth=7;for(const s of [-1,1]){g.beginPath();g.rect(hx+s*26-17,ey-22,34,16);g.fill();g.beginPath();g.moveTo(hx+s*26-16,ey-6);g.lineTo(hx+s*26+16,ey-6-s*3);g.stroke()}}}
 g.fillStyle="#5a3a36";g.beginPath();g.ellipse(hx,hy+30,13,9,0,0,7);g.fill();
 g.strokeStyle=INK;g.lineWidth=7;g.lineCap="round";g.beginPath();
 if(ex==="shock"){g.fillStyle="#7a2a30";g.ellipse(hx,hy+56,12,15,0,0,7);g.fill();g.stroke()}
 else if(ex==="sneaky"){g.moveTo(hx-14,hy+50);g.quadraticCurveTo(hx+4,hy+58,hx+20,hy+46);g.stroke()}
 else if(ex==="nervous"){g.moveTo(hx-18,hy+52);g.quadraticCurveTo(hx-9,hy+46,hx,hy+52);g.quadraticCurveTo(hx+9,hy+58,hx+18,hy+52);g.stroke();
  g.fillStyle="#9fd4ff";g.strokeStyle=INK;g.lineWidth=5;g.beginPath();g.moveTo(hx+70,hy-70);g.quadraticCurveTo(hx+86,hy-46,hx+70,hy-40);g.quadraticCurveTo(hx+54,hy-46,hx+70,hy-70);g.fill();g.stroke()}
 else{g.moveTo(hx-16,hy+46);g.quadraticCurveTo(hx-8,hy+56,hx,hy+46);g.quadraticCurveTo(hx+8,hy+56,hx+16,hy+46);g.stroke()}
 // wool on head / fringe
 if(!sh){const big=f>.6;const tufts=big?[[-62,-58],[-22,-66],[20,-66],[60,-58],[-40,-92],[0,-100],[40,-92]]:[[-28,-80],[0,-92],[28,-80]];const tr=big?34:26;
  g.strokeStyle=INK;g.lineWidth=12;tufts.forEach(([x,y])=>{g.beginPath();g.arc(hx+x,hy+y+(big?12:0),tr,0,7);g.stroke()});g.fillStyle=CREAM;tufts.forEach(([x,y])=>{g.beginPath();g.arc(hx+x,hy+y+(big?12:0),tr,0,7);g.fill()})}
 if(o.shiver){g.strokeStyle="#9fd4ff";g.lineWidth=6;for(const s of [-1,1])for(let k=0;k<3;k++){g.beginPath();g.moveTo(400+s*(175+k*16),ground-leg-110+k*26);g.lineTo(400+s*(195+k*16),ground-leg-100+k*26);g.stroke()}}
}
function drawShears(g,x,y,open,sc=1){g.save();g.translate(x,y);g.scale(sc,sc);for(const s of [-1,1]){g.save();g.rotate(s*open*.35-.4);g.fillStyle="#dfe4ea";g.strokeStyle=INK;g.lineWidth=6;g.beginPath();g.moveTo(0,0);g.lineTo(150,-10*s);g.lineTo(150,4*s);g.lineTo(8,16*s);g.closePath();g.fill();g.stroke();
 g.fillStyle="#c0353a";g.beginPath();g.ellipse(-30,8*s,26,14,0,0,7);g.fill();g.stroke();g.fillStyle="#fff";g.beginPath();g.ellipse(-30,8*s,12,6,0,0,7);g.fill();g.restore()}g.fillStyle="#888";g.beginPath();g.arc(0,0,7,0,7);g.fill();g.stroke();g.restore()}
