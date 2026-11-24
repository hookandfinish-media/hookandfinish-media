// ---------- COMMON ----------
class Card{constructor(h,cw=480,ch=800){this.c=document.createElement("canvas");this.c.width=cw;this.c.height=ch;this.g=this.c.getContext("2d");this.t=new THREE.CanvasTexture(this.c);this.t.colorSpace=THREE.SRGBColorSpace;
 this.m=new THREE.Mesh(new THREE.PlaneGeometry(h*cw/ch,h),new THREE.MeshLambertMaterial({map:this.t,alphaTest:.5,side:THREE.DoubleSide}));this.m.geometry.translate(0,h/2-h*.025,0);this.m.castShadow=true;
 this.m.customDepthMaterial=new THREE.MeshDepthMaterial({depthPacking:THREE.RGBADepthPacking,map:this.t,alphaTest:.5});this.key="";scene.add(this.m)}
 draw(key,fn){if(key===this.key)return;this.key=key;const g=this.g;g.setTransform(1,0,0,1,0,0);g.clearRect(0,0,this.c.width,this.c.height);g.setTransform(this.c.width/600,0,0,this.c.height/1000,0,0);fn(new Pen(g),g);this.t.needsUpdate=true}
 place(x,y,z){this.m.position.set(x,y,z)}
 orient(){if(this.m.visible){const d=cam.position.clone().sub(this.m.position);this.m.rotation.set(0,Math.atan2(d.x,d.z),0)}}}
const ALL=[];function card(h,cw,ch){const c=new Card(h,cw,ch);ALL.push(c);return c}
const G=[];function grp(x){const g=new THREE.Group();g.position.x=x;scene.add(g);G.push(g);return g}
SHEEPJS
function needle(g,x,y,a){g.save();g.translate(x,y);g.rotate(a);g.strokeStyle="#241726";g.lineWidth=12;g.beginPath();g.moveTo(0,0);g.lineTo(110,0);g.stroke();g.strokeStyle="#d8dde3";g.lineWidth=6;g.beginPath();g.moveTo(0,0);g.lineTo(108,0);g.stroke();g.strokeStyle="#e08a3a";g.lineWidth=4;g.beginPath();g.moveTo(0,0);g.quadraticCurveTo(-40,40,-70,10);g.stroke();g.restore()}
function hookTool(g,x,y,a,col="#c0353a",yarn="#fff"){g.save();g.translate(x,y);g.rotate(a);g.lineCap="round";g.strokeStyle="#241726";g.lineWidth=15;g.beginPath();g.moveTo(-10,0);g.lineTo(110,0);g.stroke();g.strokeStyle=col;g.lineWidth=8;g.beginPath();g.moveTo(-8,0);g.lineTo(108,0);g.stroke();g.strokeStyle="#241726";g.lineWidth=6;g.beginPath();g.arc(112,-5,6,1.6,4.7,true);g.stroke();g.strokeStyle=yarn;g.lineWidth=5;g.beginPath();g.moveTo(108,0);g.quadraticCurveTo(60,50,0,60);g.stroke();g.restore()}
function crochetHands(g,k,o={}){g.setTransform(1,0,0,1,0,0);const SK="#ffd9b8",IN="#241726";g.lineJoin="round";const yarn=o.yarn||"#fbf6ea",work=o.work||"lace",bg=o.bg||"#2a1e1e";
 const arm=(x0,y0,x1,y1,sl)=>{g.lineCap="round";g.strokeStyle=IN;g.lineWidth=150;g.beginPath();g.moveTo(x0,y0);g.lineTo(x1,y1);g.stroke();g.strokeStyle=SK;g.lineWidth=128;g.beginPath();g.moveTo(x0,y0);g.lineTo(x1,y1);g.stroke();
  const mx=x0+(x1-x0)*.55,my=y0+(y1-y0)*.55;g.lineCap="butt";g.strokeStyle=IN;g.lineWidth=176;g.beginPath();g.moveTo(x0,y0);g.lineTo(mx,my);g.stroke();g.strokeStyle=sl;g.lineWidth=154;g.beginPath();g.moveTo(x0,y0);g.lineTo(mx-(x1-x0)*.02,my-(y1-y0)*.02);g.stroke()};
 const blob=(x,y,rx,ry,rot)=>{g.save();g.translate(x,y);g.rotate(rot);g.fillStyle=SK;g.strokeStyle=IN;g.lineWidth=11;g.beginPath();g.ellipse(0,0,rx,ry,0,0,7);g.fill();g.stroke();g.restore()};
 arm(-80,900,230,600,o.sleeve1||"#3f7a5a");
 const cx=360,cy=400,gr=o.grow??1;
 if(work==="lace"){const R=150*gr;g.fillStyle=yarn;g.strokeStyle=IN;g.lineWidth=10;g.beginPath();for(let i=0;i<=72;i++){const a=i/72*6.283,r=R+10*Math.sin(a*12);g.lineTo(cx+Math.cos(a)*r,cy+Math.sin(a)*r)}g.closePath();g.fill();g.stroke();
  g.fillStyle=bg;for(const [rr,n,s] of [[.78,14,11],[.5,9,10],[.22,5,8]])for(let i=0;i<n;i++){const a=i/n*6.283+rr;g.beginPath();g.arc(cx+Math.cos(a)*R*rr,cy+Math.sin(a)*R*rr,s*gr,0,7);g.fill()}
  g.strokeStyle="rgba(36,23,38,.45)";g.lineWidth=4;for(const rr of [.64,.36]){g.beginPath();g.arc(cx,cy,R*rr,0,7);g.stroke()}}
 else{const R=150*gr,n=7+Math.round(6*gr);g.fillStyle=yarn;g.strokeStyle=IN;g.lineWidth=10;g.beginPath();for(let i=0;i<=120;i++){const a=i/120*6.283,r=R*(1+.16*Math.sin(a*n));g.lineTo(cx+Math.cos(a)*r,cy+Math.sin(a)*r*.8)}g.closePath();g.fill();g.stroke();
  g.strokeStyle="rgba(36,23,38,.35)";g.lineWidth=5;for(const rr of [.75,.5,.25]){g.beginPath();for(let i=0;i<=120;i++){const a=i/120*6.283,r=R*rr*(1+.16*rr*Math.sin(a*n));g.lineTo(cx+Math.cos(a)*r,cy+Math.sin(a)*r*.8)}g.stroke()}}
 blob(250,500,34,66,.6);blob(300,540,32,60,.9);
 const tx=lerp(560,505,k),ty=lerp(330,360,k);
 g.lineCap="round";g.strokeStyle=IN;g.lineWidth=13;g.beginPath();g.moveTo(tx,ty);g.bezierCurveTo(tx+40,ty+30,700,420,760,700);g.stroke();g.strokeStyle=yarn;g.lineWidth=7;g.stroke();
 arm(880,900,680,560,o.sleeve2||"#c0566a");
 g.strokeStyle=IN;g.lineWidth=20;g.beginPath();g.moveTo(tx,ty);g.lineTo(690,500);g.stroke();g.strokeStyle=o.hookCol||"#d9a84e";g.lineWidth=11;g.beginPath();g.moveTo(tx+3,ty+3);g.lineTo(688,498);g.stroke();
 g.strokeStyle=IN;g.lineWidth=8;g.beginPath();g.arc(tx-4,ty-2,9,.4,3.6);g.stroke();
 blob(640,470,36,62,-.9);blob(660,540,34,58,-1.6);blob(700,440,30,52,-.5)}
const D=DATA_JSON;const V=D.vo,W=D.words;const TOT=D.total;
const wordT=(re,li,nth=0)=>{const ws=W.filter(x=>x[3]===li&&new RegExp(re,"i").test(x[2].replace(/[^A-Za-z0-9']/g,"")));return ws.length?ws[Math.min(nth,ws.length-1)][0]:V[li][0]};
function camKeys(t,keys){let i=0;while(i<keys.length-2&&t>=keys[i+1][0])i++;const A=keys[i],B=keys[i+1];const k=sm((t-A[0])/(B[0]-A[0]));return[A[1].map((v,j)=>lerp(v,B[1][j],k)),A[2].map((v,j)=>lerp(v,B[2][j],k))]}
function setSky(top,bot,near=60,far=300){const u=sky.material.uniforms;u.uTop.value.set(top);u.uBot.value.set(bot);scene.fog.color.set(bot);scene.fog.near=near;scene.fog.far=far}
function lit(h,hc,hg,s,sc,sp){hemi.intensity=h;hemi.color.set(hc);hemi.groundColor.set(hg);sun.intensity=s;sun.color.set(sc);if(sp){sun.position.set(...sp[0]);sun.target.position.set(...sp[1])}}
const stG=new THREE.BufferGeometry();{const sp=[];for(let i=0;i<1400;i++){const a=rnd()*6.28,b=rnd()*1.4+.05,r=400;sp.push(Math.cos(a)*Math.cos(b)*r,Math.sin(b)*r,Math.sin(a)*Math.cos(b)*r)}stG.setAttribute("position",new THREE.Float32BufferAttribute(sp,3))}
const STARS=new THREE.Points(stG,new THREE.PointsMaterial({color:"#fff",size:2.2,sizeAttenuation:false,fog:false}));scene.add(STARS);
const big=(txt,sub,col="#FFD23F",size=180)=>`<div style="font:${size}px Pop;line-height:1;color:${col};-webkit-text-stroke:9px #241726;paint-order:stroke fill">${txt}</div>${sub?`<div style="font:56px Pop;color:#fff;-webkit-text-stroke:6px #241726;paint-order:stroke fill;letter-spacing:3px;margin-top:10px">${sub}</div>`:""}`;
const labHTML=(txt,bg="#fffaf0",col="#241726",size=62)=>`<span style="display:inline-block;background:${bg};border:8px solid #241726;border-radius:30px;padding:10px 34px;font:${size}px Pop;color:${col}">${txt}</span>`;
const stampHTML=(txt,col="#e2453c",sub="",size=140)=>`<div style="display:inline-block;border:16px solid ${col};border-radius:30px;padding:6px 44px 14px;background:rgba(255,250,240,.95);color:${col}"><div style="font:${size}px Pop;line-height:1.05">${txt}</div>${sub?`<div style="font:48px Pop;letter-spacing:2px">${sub}</div>`:""}</div>`;
const hookHTML=(small,bigt)=>`<div style="font:60px Pop;color:#fff;-webkit-text-stroke:7px #241726;paint-order:stroke fill;letter-spacing:2px">${small}</div><div style="margin-top:14px;transform:rotate(-2deg)">${labHTML(bigt,"#e2453c","#fff",bigt.length>16?84:100)}</div>`;
const capEl=document.getElementById("cap");
function captions(t){let li=-1;V.forEach((v,i)=>{if(t>=v[0]-.06&&t<(V[i+1]?V[i+1][0]-.06:v[1]+.4))li=i});if(li<0){capEl.innerHTML="";return}
 const ws=W.filter(w=>w[3]===li);let ci=0;ws.forEach((w,i)=>{if(t>=w[0])ci=i});const g0=Math.floor(ci/3)*3;const grp=ws.slice(g0,g0+3);
 const gk=t<.2?1:back((t-grp[0][0]+.02)/.16);
 capEl.innerHTML=grp.map((w,i)=>{const on=g0+i===ci;const hl=KEY.test(w[2].replace(/[^A-Za-z0-9-]/g,""));return`<span style="color:${hl?"#FFD23F":"#fff"};display:inline-block;margin:0 22px;transform:scale(${on?1.07:1})">${w[2].replace("...","").toUpperCase()}</span>`}).join("");
 capEl.style.transform=`translateX(-50%) scale(${.85+.15*Math.min(1.1,gk)})`}
const EL=id=>document.getElementById(id);
function proj(x,y,z){const v=new THREE.Vector3(x,y,z).project(cam);return[(v.x*.5+.5)*1080,(-v.y*.5+.5)*1920]}
function flagTex(){return ctex(300,200,(g)=>{for(let i=0;i<13;i++){g.fillStyle=i%2?"#fff":"#c8102e";g.fillRect(0,i*200/13,300,200/13+1)}g.fillStyle="#1a2a6c";g.fillRect(0,0,130,108);g.fillStyle="#fff";for(let r=0;r<5;r++)for(let c=0;c<6;c++){g.beginPath();g.arc(12+c*21,12+r*21,3.5,0,7);g.fill()}})}
