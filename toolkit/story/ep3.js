// ===== EP3: THE CROCHET THAT SAVED FAMILIES =====
const KEY=/^(Ireland's|Great|Famine|families|survived|crochet|hook|1847|Cassandra|Hand|lace|classes|front|room|Venetian|two|hundred|hours|Crochet|faster|whole|selling|survive|hobby|feed|family)/i;
const COT=grp(0);add(COT,new THREE.PlaneGeometry(30,30),tm({map:T.dirt}),[0,0,0],[-Math.PI/2,0,0],0);add(COT,box(16,7,.4),tm({map:T.rock,color:"#b8b0a6"}),[0,3.5,-3.5],[0,0,0],0);
add(COT,box(1.6,1.4,.1),tm({color:"#5a6a80",emissive:"#2a3a50"}),[2.6,3.2,-3.25],[0,0,0],1.2);add(COT,box(.12,1.4,.12),tm({color:"#4a2a1a"}),[2.6,3.2,-3.2]);add(COT,box(1.6,.12,.12),tm({color:"#4a2a1a"}),[2.6,3.2,-3.2]);
add(COT,box(2.4,2,1),tm({map:T.rock,color:"#9a9088"}),[-2.6,1,-3.0],[0,0,0],1);add(COT,box(1.4,1.1,.2),tm({color:"#ff8a30",emissive:"#ff5a10"}),[-2.6,.7,-2.45],[0,0,0],0);
const fire=new THREE.PointLight("#ff9a40",0,12);fire.position.set(-2.4,1.2,-1.6);COT.add(fire);
add(COT,box(2.6,.12,1.2),tm({map:T.wood}),[.6,.9,-1.4]);for(const dx of [-1.1,1.1])add(COT,box(.1,.9,.1),tm({color:"#3a2a1a"}),[.6+dx,.45,-1.4]);add(COT,new THREE.CylinderGeometry(.06,.06,.3,10),tm({color:"#f6efe0",emissive:"#806040"}),[1.4,1.11,-1.4]);
const LACEPILE=[];for(let i=0;i<6;i++){const m=add(COT,new THREE.CylinderGeometry(.22,.22,.02,24),tm({color:"#fbf6ea"}),[-.2+(i%3)*.32,.97+Math.floor(i/3)*.03,-1.3-(i%2)*.15],[0,0,0],.6);LACEPILE.push(m)}
const HAN=grp(200);add(HAN,box(30,30,.2),tm({color:"#1f3328"}),[0,0,-3],[0,0,0],0);const hL=new THREE.PointLight("#ffd29a",0,10);hL.position.set(-1.5,3,2);HAN.add(hL);
const PAR=grp(400);add(PAR,new THREE.PlaneGeometry(30,30),tm({map:T.wood}),[0,0,0],[-Math.PI/2,0,0],0);
const wall=ctex(256,256,(g)=>{for(let x=0;x<256;x+=32){g.fillStyle=x%64?"#3f6a52":"#4c7a60";g.fillRect(x,0,32,256)}g.fillStyle="rgba(217,168,78,.5)";for(let y=16;y<256;y+=48)for(let x=16;x<256;x+=64){g.beginPath();g.arc(x,y,5,0,7);g.fill()}},[6,2]);
add(PAR,box(20,7,.3),tm({map:wall}),[0,3.5,-3.5],[0,0,0],0);add(PAR,box(2.6,.25,.6),tm({color:"#f4efe6"}),[0,1.6,-3.1]);add(PAR,box(1.6,1.4,.4),tm({color:"#2a2020"}),[0,.7,-3.2]);add(PAR,box(1.2,.9,.2),tm({color:"#ff8a30",emissive:"#ff5a10"}),[0,.5,-3.0],[0,0,0],0);
add(PAR,new THREE.CylinderGeometry(1.4,1.4,.1,32),tm({map:T.wood}),[0,.85,-.6]);add(PAR,new THREE.CylinderGeometry(.12,.2,.85,10),tm({color:"#3a2a1a"}),[0,.42,-.6]);
const parL=new THREE.PointLight("#ffd6a0",0,14);parL.position.set(0,3,2);PAR.add(parL);
const CLK=grp(600);add(CLK,box(30,30,.2),tm({color:"#2a2030"}),[0,0,-3],[0,0,0],0);add(CLK,new THREE.PlaneGeometry(30,30),tm({color:"#3a2a3a"}),[0,0,0],[-Math.PI/2,0,0],0);
const face=ctex(512,512,(g)=>{g.fillStyle="#f8f1e0";g.beginPath();g.arc(256,256,250,0,7);g.fill();g.lineWidth=18;g.strokeStyle="#241726";g.stroke();g.fillStyle="#241726";g.font="bold 64px Pop";g.textAlign="center";g.textBaseline="middle";for(let i=1;i<=12;i++){const a=i/12*6.283-1.5708;g.fillText(i,256+Math.cos(a)*190,256+Math.sin(a)*190)}});
const CF=new THREE.Group();CLK.add(CF);CF.position.set(0,1.9,-2.5);add(CF,new THREE.CircleGeometry(1.5,48),new THREE.MeshBasicMaterial({map:face}),[0,0,0],[0,0,0],0);
const HR=new THREE.Group(),MN=new THREE.Group();CF.add(HR);CF.add(MN);add(HR,box(.1,.8,.04),tm({color:"#241726"}),[0,.35,.03],[0,0,0],0);add(MN,box(.07,1.2,.04),tm({color:"#c0353a"}),[0,.55,.05],[0,0,0],0);
const MKT=grp(800);const cob=ctex(256,256,(g)=>{g.fillStyle="#6a6460";g.fillRect(0,0,256,256);for(let y=0;y<256;y+=32)for(let x=0;x<256;x+=32){g.fillStyle=jit("#8a847c",40);g.beginPath();g.ellipse(x+16+(y/32%2)*8,y+16,13,11,0,0,7);g.fill()}},[20,20]);
add(MKT,new THREE.PlaneGeometry(300,300),tm({map:cob}),[0,0,0],[-Math.PI/2,0,0],0);for(let i=0;i<6;i++)add(MKT,box(5,6+rnd()*3,4),tm({color:i%2?"#c8b8a0":"#a89880"}),[-12+i*5,3.5,-9],[0,0,0],1);
const awn=ctex(256,64,(g)=>{for(let x=0;x<256;x+=32){g.fillStyle=x%64?"#fff":"#3f7a5a";g.fillRect(x,0,32,64)}});add(MKT,box(3.4,.1,1.6),tm({map:awn}),[0,2.4,-1.6],[.25,0,0],1);for(const x of [-1.6,1.6])add(MKT,box(.08,2.4,.08),tm({color:"#4a2a1a"}),[x,1.2,-.9]);
add(MKT,box(3.2,.12,1.1),tm({map:T.wood}),[0,.95,-1.3]);add(MKT,box(3.1,.9,1),tm({map:T.wood}),[0,.45,-1.3]);for(let i=0;i<7;i++)add(MKT,new THREE.CylinderGeometry(.22,.22,.02,24),tm({color:"#fbf6ea"}),[-1.2+i*.4,1.02,-1.3+(i%2)*.18],[0,0,0],.6);
const MOM={jacket:"#4a6a4a",pants:"#3a3030",boots:"#3a2a20",hat:"bonnet",build:"adult",dress:"#4a6a4a"},GIRL={jacket:"#8a5a7a",pants:"#3a3030",boots:"#3a2a20",hat:"hair",hair:"#8a4a2a",build:"kid",dress:"#8a5a7a"};
const DAD={jacket:"#5a4a3a",pants:"#3a3a3a",boots:"#3a2a20",hat:"cap",cap:"#3a3a3a",build:"adult",moustache:"#5a3a20"},CAS={jacket:"#7a2a3a",pants:"#3a2a2a",boots:INK,hat:"hair",hair:"#3a2a1a",build:"adult",dress:"#7a2a3a",sash:"#d9a84e"};
const W1={jacket:"#5a6a8a",pants:"#3a3030",boots:"#3a2a20",hat:"bonnet",build:"adult",dress:"#5a6a8a"},W2={jacket:"#8a6a4a",pants:"#3a3030",boots:"#3a2a20",hat:"hair",hair:"#c08a4a",build:"stout",dress:"#8a6a4a"};
function laceDot(g,x,y,r=34){g.fillStyle="#fbf6ea";g.strokeStyle=INK;g.lineWidth=6;g.beginPath();g.arc(x,y,r,0,7);g.fill();g.stroke();g.fillStyle="#7a6a5a";for(let i=0;i<6;i++){const a=i/6*6.283;g.beginPath();g.arc(x+Math.cos(a)*r*.55,y+Math.sin(a)*r*.55,r*.12,0,7);g.fill()}}
const HN=card(3.2,800,800),P1=card(1.95),P2=card(1.4),P3=card(2.0),CA=card(2.0),L1=card(1.95),L2=card(1.95),L3=card(1.95),BU=card(2.0);
const famDraw=(C,happy)=>{const k=Math.floor(C.t*6)%3;[[P1,MOM,1,-.95,.4],[P2,GIRL,2,0,.6],[P3,DAD,3,.95,.4]].forEach(([c,o,sd,x,z])=>{c.m.visible=true;c.draw(`f${happy}${k}${C.blink(sd)}`,(p,g)=>{bodyFront(p,o,{mode:"sit",expr:happy?"grin":(sd==3?"stern":"nervous"),blink:C.blink(sd),seed:sd+2});laceDot(g,300,640+k*6);hookTool(g,330,600,-.6+k*.15,"#c0a050")});c.place(x,0,z)})};
const tFam=wordT("^families$",0),tStart=wordT("^started$",1),tCro=wordT("^Crochet$",2),tAnd=wordT("^and$",3);
const hands=(C,spd,o={})=>{HAN.visible=true;sky.visible=false;lit(.5,"#fff0e0","#203020",1.0,"#ffd6a0",[[204,6,10],[200,2,0]]);hL.intensity=8;const k=.5+.5*Math.sin(C.t*spd);HN.m.visible=true;HN.draw(`h${C.f}`,(p,g)=>crochetHands(g,k,Object.assign({bg:"#1f3328",sleeve1:"#4a6a4a",sleeve2:"#4a6a4a"},o)));HN.place(200,.2,0)};
const SHOTS=[
[0,C=>{hands(C,6);C.hookZoom(9,4.9,1.8,1.85,200);EL("cnt").style.opacity=1;EL("cnt").innerHTML=hookHTML("IRELAND'S GREAT FAMINE…","SAVED BY A HOOK?!")}],
[tFam-.05,C=>{COT.visible=true;sky.visible=false;lit(.8,"#b0c0e0","#3a3030",.9,"#b0c0e0",[[5,8,10],[0,0,0]]);fire.intensity=18+4*Math.sin(C.t*13);famDraw(C,false);LACEPILE.forEach(m=>m.visible=false);
 C.P=[lerp(.3,-.2,C.lt/C.dur),1.7,lerp(8.2,7.2,eo(C.lt/.5))];C.Tg=[0,.95,0];C.pop("lab",labHTML("IRELAND · THE GREAT FAMINE",undefined,undefined,54),.08)}],
[V[1][0]-.05,C=>{PAR.visible=true;sky.visible=false;lit(.9,"#fff0d8","#4a3020",1.2,"#ffe0b0",[[404,8,10],[400,0,0]]);parL.intensity=16;CA.m.visible=true;CA.draw(`c${C.blink(4)}`,p=>bodyFront(p,CAS,{mode:"stand",expr:"smile",blink:C.blink(4),seed:6}));CA.place(400,0,.6);
 C.P=[400+lerp(.8,0,eo(C.lt/.5)),2.0,lerp(6,4.8,eo(C.lt/.5))];C.Tg=[400,1.5,.3];if(C.lt<1.2)C.pop("lab",labHTML("1847 · CASSANDRA HAND"),.08);else C.slam("cnt",stampHTML("SHE HAD A PLAN…","#3f7a5a","",96),1.2,-4)}],
[tStart-.05,C=>{PAR.visible=true;sky.visible=false;lit(.9,"#fff0d8","#4a3020",1.2,"#ffe0b0",[[404,8,10],[400,0,0]]);parL.intensity=16;const k=Math.floor(C.t*6)%3;
 CA.m.visible=true;CA.draw(`c2${C.blink(4)}`,p=>bodyFront(p,CAS,{mode:"stand",expr:"grin",blink:C.blink(4),seed:6,wave:1}));CA.place(401.2,0,-1.6);
 [[L1,W1,1,398.7,.4],[L2,W2,2,399.9,.9],[L3,MOM,3,401.1,.5]].forEach(([c,o,sd,x,z])=>{c.m.visible=true;c.draw(`l${k}${C.blink(sd)}`,(p,g)=>{bodyFront(p,o,{mode:"sit",expr:"smile_closed",blink:C.blink(sd),seed:sd+4});laceDot(g,300,640+k*6,28);hookTool(g,330,600,-.6+k*.15,"#c0a050")});c.place(x,0,z)});
 C.P=[400.2,2.5,lerp(7.6,6.8,C.lt/C.dur)];C.Tg=[400.2,1.2,-.3];C.pop("lab",labHTML("LACE CLASSES · HER FRONT ROOM",undefined,undefined,48),.08)}],
[V[2][0]-.05,C=>{CLK.visible=true;sky.visible=false;lit(.7,"#d0c0ff","#2a2030",1.0,"#ffe0c0",[[604,8,10],[600,2,0]]);const sp=C.lt*14;MN.rotation.z=-sp*6.283;HR.rotation.z=-sp*6.283/12;
 L1.m.visible=true;const k=Math.floor(C.t*4)%3;L1.draw(`v${k}${C.blink(1)}`,(p,g)=>{bodyFront(p,W2,{mode:"stand",expr:"pained",blink:C.blink(1),seed:5});needle(g,330,600+k*8,-.4+k*.2);laceDot(g,300,660,18)});L1.place(601.3,0,-.6);
 C.P=[600,2.4,lerp(7.2,6.4,C.lt/C.dur)];C.Tg=[600,1.7,-1.5];const n=Math.round(200*eo((C.lt-.2)/1.6));EL("cnt").style.opacity=1;EL("cnt").innerHTML=big(`${n} HOURS`,"FOR ONE SMALL PIECE","#FFD23F",150);EL("cnt").style.transform=`scale(${Math.min(1.08,back(C.lt/.25))})`}],
[tCro-.05,C=>{hands(C,22);C.P=[200,1.8,lerp(5.6,5.0,eo(C.lt/.3))];C.Tg=[200,1.9,0];C.roll=Math.sin(C.t*40)*.006;C.pop("lab",labHTML("CROCHET: MUCH FASTER!","#3f9a5a","#fff"),.05);
 C.post=()=>{let h="";for(let i=0;i<9;i++){const t0=.2+i*.12;if(C.lt<t0)continue;const x=110+(i%3)*330,y=560+Math.floor(i/3)*170,s=Math.min(1.1,back((C.lt-t0)/.2));h+=`<div style="position:absolute;left:${x}px;top:${y}px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,#fbf6ea 0 22%,#7a6a5a 23% 27%,#fbf6ea 28% 55%,#7a6a5a 56% 60%,#fbf6ea 61%);border:8px solid #241726;transform:scale(${Math.max(0,s)}) rotate(${C.t*90}deg)"></div>`}EL("bad").innerHTML=h}}],
[V[3][0]-.05,C=>{COT.visible=true;sky.visible=false;lit(.75,"#ffe0c0","#3a2a20",1.0,"#ffd6a0",[[5,8,10],[0,0,0]]);fire.intensity=18+4*Math.sin(C.t*13);famDraw(C,true);LACEPILE.forEach((m,i)=>m.visible=C.lt>.2+i*.15);
 C.P=[lerp(-.3,.2,C.lt/C.dur),1.8,lerp(8,7.2,eo(C.lt/.5))];C.Tg=[0,.95,-.2];C.pop("lab",labHTML("WHOLE FAMILIES CROCHETED"),.08)}],
[tAnd-.05,C=>{MKT.visible=true;setSky("#8a9ab0","#c8ccd4",40,200);lit(1.0,"#e0e8f0","#4a4a40",1.6,"#fff0e0",[[805,20,18],[800,0,-1]]);
 P1.m.visible=true;P1.draw(`m${C.blink(1)}`,p=>bodyFront(p,MOM,{mode:"stand",expr:"grin",blink:C.blink(1),seed:3}));P1.place(800.2,0,-2.4);BU.m.visible=true;BU.draw(`b${C.blink(5)}`,p=>bodyFront(p,CAS,{mode:"stand",expr:"smile",look:-.6,blink:C.blink(5),seed:12,wave:C.lt>.8?1:undefined}));BU.place(801.2,0,.4);
 C.P=[800.4,2.0,lerp(7,6.2,C.lt/C.dur)];C.Tg=[800.4,1.3,-1];C.pop("lab",labHTML("LACE = FOOD ON THE TABLE","#d9a84e","#241726",54),.08)}],
[V[4][0]-.05,C=>{hands(C,5);C.P=[200,1.8,lerp(6.2,5.4,eo(C.lt/.4))];C.Tg=[200,1.9,0]},1],
];
