// ===== EP9: MACHINES CANT CROCHET =====
const KEY=/^(Machines|knit|minutes|crochet|1589|hook|twists|tilts|loop|every|real|human|hands|special)/i;
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

// --- extra props for ep6
const BOWL=add(COT,new THREE.SphereGeometry(.22,20,10,0,6.3,Math.PI/2,Math.PI/2),tm({color:"#8a6a4a",side:THREE.DoubleSide}),[.2,1.18,-1.1],[0,0,0],.7);
const LOAF=add(COT,new THREE.SphereGeometry(.28,20,12),tm({color:"#c08040"}),[.2,1.08,-1.15],[0,0,0],.8);LOAF.scale.set(1.4,.6,.8);
const EXT=grp(1200);add(EXT,new THREE.PlaneGeometry(400,400),tm({color:"#4a6a3a"}),[0,0,0],[-Math.PI/2,0,0],0);
for(let i=0;i<10;i++){const r=16+rnd()*18;add(EXT,new THREE.SphereGeometry(r,24,12),tm({color:i%2?"#3f5f35":"#4a6a3e"}),[-120+i*26,-r*.78,-40-rnd()*25],[0,0,0],0)}
const sc=new THREE.Group();EXT.add(sc);sc.position.set(-3.5,0,-7);add(sc,box(3.2,1.9,2.2),tm({map:T.rock,color:"#b0a89c"}),[0,.95,0],[0,0,0],1.2);const th2=new THREE.CylinderGeometry(.01,2,1.3,4,1);th2.rotateY(Math.PI/4);add(sc,th2,tm({color:"#8a7a4a"}),[0,2.5,0],[0,0,0],1.2).scale.set(1.15,1,.8);add(sc,box(.6,1.1,.1),tm({color:"#3a2a1a"}),[.5,.55,1.12]);
for(let i=0;i<14;i++)add(EXT,new THREE.DodecahedronGeometry(.35,0),tm({map:T.rock}),[-9+i*1.1,.25,-3.6],[rnd(),rnd(),0],.8);
const PLANTS=[];for(let r=0;r<5;r++)for(let c=0;c<9;c++){const m=add(EXT,new THREE.ConeGeometry(.22,.5,6),tm({color:"#6a5a30"}),[-4+c*1.0+(r%2)*.5,.2,-.5+r*1.1],[.4*(rnd()-.5),0,.6*(rnd()-.5)],.6);PLANTS.push(m)}
const HID=grp(1400);add(HID,new THREE.PlaneGeometry(30,30),tm({color:"#1a1418"}),[0,0,0],[-Math.PI/2,0,0],0);add(HID,box(30,20,.2),tm({color:"#1a1418"}),[0,0,-3],[0,0,0],0);
add(HID,new THREE.CylinderGeometry(1.1,1.1,.1,32),tm({map:T.wood}),[0,1.0,0]);add(HID,new THREE.CylinderGeometry(.15,.25,1,12),tm({color:"#3a2a1a"}),[0,.5,0]);
const CLOTH=add(HID,new THREE.SphereGeometry(.6,24,12,0,6.3,0,Math.PI/2),tm({color:"#8a7a6a",side:THREE.DoubleSide}),[0,1.05,0],[0,0,0],1);CLOTH.scale.set(1,.55,1);
const hidL=new THREE.PointLight("#ffd27a",0,6);hidL.position.set(0,1.3,.6);HID.add(hidL);const hidS=new THREE.SpotLight("#fff0d0",0,12,.35,.6);hidS.position.set(0,6,2);hidS.target.position.set(1400,1,0);HID.add(hidS);scene.add(hidS.target);
const LADY={jacket:"#5a2a7a",pants:"#3a2a3a",boots:INK,hat:"bonnet",build:"adult",dress:"#5a2a7a",sash:"#d9a84e"},GENT={jacket:"#1f2a44",pants:"#1f2a44",boots:INK,hat:"tophat",build:"adult",moustache:"#3a2a1a"};
const LA=card(2.0),GE=card(2.1);



const STORM=()=>{setSky("#2a3440","#6a7684",25,140);lit(.75,"#a0b0c0","#2a3020",.8,"#c0c8d0",[[1195,20,15],[1200,0,-2]])};
const hands=(C,spd,o={})=>{HAN.visible=true;sky.visible=false;lit(.55,"#fff0e0","#203020",1.1,"#ffd6a0",[[204,6,10],[200,2,0]]);hL.intensity=10;const k=.5+.5*Math.sin(C.t*spd);HN.m.visible=true;HN.draw(`h${C.f}`,(p,g)=>crochetHands(g,k,Object.assign({bg:"#1f3328",sleeve1:"#3a5a8a",sleeve2:"#3a5a8a",hookCol:"#e8b84e",yarn:"#f08070",work:"round"},o)));HN.place(200,.2,0)};
const parlour=()=>{PAR.visible=true;sky.visible=false;lit(.95,"#fff0d8","#4a3020",1.3,"#ffe0b0",[[404,8,10],[400,0,0]]);parL.intensity=16};

function machine(g,t){g.save();g.translate(300,520);g.fillStyle="#7a8590";g.strokeStyle=INK;g.lineWidth=8;g.fillRect(-230,-150,460,300);g.strokeRect(-230,-150,460,300);
 for(const [x,y,r,d] of [[-110,-20,80,1],[60,30,60,-1],[150,-80,40,1]]){g.save();g.translate(x,y);g.rotate(t*2*d);g.fillStyle="#c9b46a";g.beginPath();for(let i=0;i<16;i++){const a=i*Math.PI/8,rr=i%2?r:r*1.22;g.lineTo(Math.cos(a)*rr,Math.sin(a)*rr)}g.closePath();g.fill();g.stroke();g.fillStyle="#4a4f56";g.beginPath();g.arc(0,0,r*.3,0,7);g.fill();g.stroke();g.restore()}
 g.fillStyle="#e8e0d0";g.fillRect(-200,160,400,60);g.strokeRect(-200,160,400,60);g.fillStyle="#c06a5a";for(let i=0;i<10;i++)g.fillRect(-190+i*40+((t*120)%40),172,26,36);g.restore()}
const MC=card(3.0);
const t1589=wordT("^1589$",1),tHands=wordT("^hands$",3);
const mach=(C)=>{MKT.visible=true;sky.visible=false;lit(.9,"#fff4e0","#3a3030",1.2,"#ffe8c0",[[804,8,10],[800,0,0]]);MC.m.visible=true;MC.draw(`m${C.f}`,(p,g)=>machine(g,C.t));MC.place(800,0,1)};
const SHOTS=[
[0,C=>{mach(C);C.P=[800,1.6,lerp(5.0,4.3,C.lt/C.dur)];C.Tg=[800,1.5,1];EL("cnt").style.opacity=1;EL("cnt").innerHTML=hookHTML("MACHINES CAN KNIT A SWEATER…","BUT THEY CAN'T CROCHET?!")}],
[V[1][0]-.05,C=>{mach(C);C.P=[800+lerp(.6,-.6,C.lt/C.dur),1.7,4.6];C.Tg=[800,1.5,1];if(C.t>=t1589-.1)C.slam("cnt",big("SINCE 1589","KNITTING MACHINES","#FFD23F",150),t1589-.1-(C.t-C.lt),-4);else C.pop("lab",labHTML("KNITTING MACHINES"),.08)}],
[V[2][0]-.05,C=>{hands(C,14,{yarn:"#c06a5a"});C.P=[200,1.8,lerp(6.4,5.0,eo(C.lt/.5))];C.Tg=[200,1.85,0];C.pop("lab",labHTML("TWIST · TILT · NEW LOOP EVERY STITCH","#fffaf0","#241726",40),.08)}],
[V[3][0]-.05,C=>{hands(C,8,{yarn:"#c06a5a"});C.P=[200,1.7,lerp(5.6,5.0,C.lt/C.dur)];C.Tg=[200,1.85,0];if(C.t>=tHands-.2)C.slam("cnt",stampHTML("100% HANDMADE","#e2453c","EVERY REAL CROCHET STITCH",120),tHands-.2-(C.t-C.lt),-4)}],
[V[4][0]-.05,C=>{hands(C,5,{yarn:"#c06a5a"});C.P=[200,1.8,lerp(6.2,5.4,eo(C.lt/.4))];C.Tg=[200,1.9,0]},1],
];
