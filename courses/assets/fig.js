/* Спільні помічники фігур — найпоширеніший варіант кожного (framework.py assets).
   Сторінка, де помічник інший, лишає свій: локальне визначення перекриває це.
   Класичний скрипт без модулів — сторінки мають відкриватися з диска.
   Частка сторінок із цим варіантом: I 160/160, css 160/160, LW 155/155, LH 136/136, dpr 155/160, on 95/136, verd 83/117, mono 81/99, segment 72/77, rr 48/72, capt 63/71, gr 23/26, thou 14/25, разів 16/16, крат 9/11, f1 31/32, f2 50/53, f3 31/32, f4 49/51, plural 17/49, fmt 16/26, mkNorm 25/30, clip 17/17, ah 14/14, onc 16/16, onr 10/10, segBind 18/20, fitFont 14/21, sans 13/17, dash 12/20, isDark 9/13, mean 9/11, banner 8/10 */

function I(id){return document.getElementById(id);}

function css(v){return getComputedStyle(document.body).getPropertyValue(v).trim();}

function LW(cv){return +cv.dataset.lw||cv.width;}

function LH(cv){return +cv.dataset.lh||cv.height;}

function dpr(cv){
  var r=window.devicePixelRatio||1;
  if(cv.dataset.scaled!==String(r)){
    var w=+cv.dataset.lw||cv.width, h=+cv.dataset.lh||cv.height;
    cv.dataset.lw=w; cv.dataset.lh=h; cv.dataset.scaled=String(r);
    cv.width=w*r; cv.height=h*r; cv.style.width='100%';
  }
  var g=cv.getContext('2d'); g.setTransform(r,0,0,r,0,0);
  g.clearRect(0,0,+cv.dataset.lw,+cv.dataset.lh);
  return g;
}

function on(id,ev,fn){var e=I(id); if(e) e.addEventListener(ev,fn);}

function verd(id,tag,cap,txt){
  I(id).innerHTML='<span class="tag '+tag+'">'+cap+'</span><br>'+txt;
}

function mono(px,bold){return (bold?'700 ':'')+px+'px "JetBrains Mono",monospace';}

function segment(id, fn){
  var box=I(id); if(!box) return;
  box.addEventListener('click', function(ev){
    var b=ev.target.closest('button'); if(!b) return;
    var all=box.querySelectorAll('button'), k;
    for(k=0;k<all.length;k++) all[k].setAttribute('aria-pressed', all[k]===b?'true':'false');
    fn(+b.dataset.i);
  });
}

function rr(g,x,y,w,h,r){
  var rad=Math.min(r,Math.abs(w)/2,Math.abs(h)/2);
  g.beginPath();
  g.moveTo(x+rad,y);
  g.arcTo(x+w,y,x+w,y+h,rad);
  g.arcTo(x+w,y+h,x,y+h,rad);
  g.arcTo(x,y+h,x,y,rad);
  g.arcTo(x,y,x+w,y,rad);
  g.closePath();
}

function capt(g,txt,x,y,color,px,bold,align){
  g.fillStyle=color||css('--soft'); g.font=mono(px||11,!!bold);
  g.textAlign=align||'left'; g.textBaseline='alphabetic'; g.fillText(txt,x,y);
}

function gr(n){
  var s=String(Math.round(n)), out='', k, c=0;
  for(k=s.length-1;k>=0;k--){ out=s.charAt(k)+out; c++; if(c%3===0 && k>0) out=' '+out; }
  return out;
}

function thou(n){
  var s=String(Math.round(n)), out='', k=0, i;
  for(i=s.length-1;i>=0;i--){ out=s.charAt(i)+out; k++; if(k%3===0 && i>0) out=' '+out; }
  return out;
}

function разів(n){
  var d = n%10, dd = n%100;
  if(d===1 && dd!==11) return 'раз';
  if(d>=2 && d<=4 && (dd<12 || dd>14)) return 'рази';
  return 'разів';
}

function крат(v){
  if(Math.abs(v - Math.round(v)) < 1e-9) return v.toFixed(0) + ' ' + разів(Math.round(v));
  return v.toFixed(1) + ' раза';
}

function f1(v){return (Math.round(v*10)/10).toFixed(1);}

function f2(v){return (Math.round(v*100)/100).toFixed(2);}

function f3(v){return (Math.round(v*1000)/1000).toFixed(3);}

function f4(v){return (Math.round(v*10000)/10000).toFixed(4);}

function plural(n,one,few,many){
  var a=Math.abs(n)%10, b=Math.abs(n)%100;
  if(a===1&&b!==11) return one;
  if(a>=2&&a<=4&&(b<12||b>14)) return few;
  return many;
}

function fmt(v){return Math.round(v).toLocaleString('uk-UA');}

function mkNorm(r){return function(){var u=0,v=0;while(!u)u=r();while(!v)v=r();
  return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);};}

function clip(g,x,y,w,h){g.save(); g.beginPath(); g.rect(x,y,w,h); g.clip();}

function ah(a){var v=Math.round(Math.max(0,Math.min(1,a))*255).toString(16);
  return v.length<2?'0'+v:v;}

function onc(id,fn){I(id).addEventListener('click',fn);}

function onr(id,fn){I(id).addEventListener('input',fn);}

function segBind(id,fn){
  var box=I(id);
  Array.prototype.forEach.call(box.querySelectorAll('button'),function(btn){
    btn.addEventListener('click',function(){
      Array.prototype.forEach.call(box.querySelectorAll('button'),function(b){
        b.setAttribute('aria-pressed', b===btn?'true':'false');});
      fn(btn);
    });
  });
}

function fitFont(g,txt,maxw,base,bold){
  var s=base, pre=bold?'700 ':'';
  g.font=pre+s+'px "JetBrains Mono",monospace';
  while(s>6.5 && g.measureText(txt).width>maxw){
    s-=0.5; g.font=pre+s+'px "JetBrains Mono",monospace';
  }
  return s;
}

function sans(px){return '600 '+px+'px Unbounded,system-ui,sans-serif';}

function dash(g,x0,y,x1,color){
  g.save(); g.setLineDash([5,4]); g.strokeStyle=color; g.lineWidth=1;
  g.beginPath(); g.moveTo(x0,y+0.5); g.lineTo(x1,y+0.5); g.stroke(); g.restore();
}

function isDark(){
  return matchMedia('(prefers-color-scheme: dark)').matches
      || document.documentElement.getAttribute('data-theme')==='dark';
}

function mean(a){var s=0,k;for(k=0;k<a.length;k++)s+=a[k];return s/a.length;}

function banner(g,x,y,w,lines,ok){
  var h=16+lines.length*17, k;
  rr(g,x,y,w,h,9);
  g.fillStyle=(ok?css('--teal'):css('--rose'))+'1c'; g.fill();
  g.strokeStyle=ok?css('--teal'):css('--rose'); g.lineWidth=1.5; g.stroke();
  g.textAlign='left'; g.fillStyle=ok?css('--teal'):css('--rose');
  for(k=0;k<lines.length;k++){
    fitFont(g,lines[k],w-24,12.5,true);
    g.fillText(lines[k],x+12,y+21+k*17);
  }
  return h;
}
