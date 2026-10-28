(function(){
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var FINE = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var DPR = Math.min(window.devicePixelRatio || 1, FINE ? 1.5 : 1);

  var VS = 'attribute vec2 p;varying vec2 v;void main(){v=p*.5+.5;gl_Position=vec4(p,0.,1.);}';
  var NOISE = 'float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}' +
    'float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}' +
    'float fbm(vec2 p){float s=0.,a=.5;for(int i=0;i<5;i++){s+=a*n(p);p=p*2.02+vec2(1.7,9.2);a*=.5;}return s;}';
  var COVER = 'vec2 cover(vec2 uv,vec2 box,vec2 img){float rb=box.x/box.y,ri=img.x/img.y;vec2 s=rb>ri?vec2(1.,ri/rb):vec2(rb/ri,1.);return (uv-.5)*s+.5;}';

  function gl(canvas){
    var o={premultipliedAlpha:true,antialias:false,alpha:true,preserveDrawingBuffer:false};
    return canvas.getContext('webgl',o)||canvas.getContext('experimental-webgl',o);
  }
  function prog(g,fs){
    function sh(t,src){var s=g.createShader(t);g.shaderSource(s,src);g.compileShader(s);if(!g.getShaderParameter(s,g.COMPILE_STATUS)){console.warn(g.getShaderInfoLog(s));return null;}return s;}
    var v=sh(g.VERTEX_SHADER,VS),f=sh(g.FRAGMENT_SHADER,'precision mediump float;varying vec2 v;'+fs);if(!v||!f)return null;
    var p=g.createProgram();g.attachShader(p,v);g.attachShader(p,f);g.linkProgram(p);if(!g.getProgramParameter(p,g.LINK_STATUS))return null;
    g.useProgram(p);var b=g.createBuffer();g.bindBuffer(g.ARRAY_BUFFER,b);g.bufferData(g.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),g.STATIC_DRAW);
    var loc=g.getAttribLocation(p,'p');g.enableVertexAttribArray(loc);g.vertexAttribPointer(loc,2,g.FLOAT,false,0,0);
    var U={};return {p:p,u:function(n){return U[n]||(U[n]=g.getUniformLocation(p,n));}};
  }
  function tex(g){var t=g.createTexture();g.bindTexture(g.TEXTURE_2D,t);
    g.texParameteri(g.TEXTURE_2D,g.TEXTURE_WRAP_S,g.CLAMP_TO_EDGE);g.texParameteri(g.TEXTURE_2D,g.TEXTURE_WRAP_T,g.CLAMP_TO_EDGE);
    g.texParameteri(g.TEXTURE_2D,g.TEXTURE_MIN_FILTER,g.LINEAR);g.texParameteri(g.TEXTURE_2D,g.TEXTURE_MAG_FILTER,g.LINEAR);
    g.pixelStorei(g.UNPACK_FLIP_Y_WEBGL,true);return t;}
  function upload(g,t,src){try{g.bindTexture(g.TEXTURE_2D,t);g.texImage2D(g.TEXTURE_2D,0,g.RGBA,g.RGBA,g.UNSIGNED_BYTE,src);return true;}catch(e){return false;}}
  function fit(c){var r=c.getBoundingClientRect(),w=Math.max(2,Math.round(r.width*DPR)),h=Math.max(2,Math.round(r.height*DPR));if(c.width!==w||c.height!==h){c.width=w;c.height=h;}return [w,h];}
  function scaled(img,maxW){ // keep textures within mobile limits
    var w=img.naturalWidth||img.videoWidth,h=img.naturalHeight||img.videoHeight;if(!w)return img;if(w<=maxW)return img;
    var c=document.createElement('canvas');c.width=maxW;c.height=Math.round(h*maxW/w);c.getContext('2d').drawImage(img,0,0,c.width,c.height);return c;}
  function whenVisible(el,on,off){if(!('IntersectionObserver' in window)){on();return;}
    new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?on():off();});},{rootMargin:'100px 0px'}).observe(el);}
  function canvasIn(host,cls){var c=document.createElement('canvas');c.className='shader '+(cls||'');c.setAttribute('aria-hidden','true');host.appendChild(c);return c;}

  /* 1. flowing brand red: Culture panel + contact band */
  var RED='uniform float t;uniform vec2 res;'+NOISE+
    'void main(){vec2 uv=v*vec2(res.x/res.y,1.)*1.15;'+
    'vec2 q=vec2(fbm(uv+t*.035),fbm(uv+vec2(5.2,1.3)-t*.03));'+
    'vec2 r=vec2(fbm(uv+3.6*q+vec2(1.7,9.2)+t*.045),fbm(uv+3.6*q+vec2(8.3,2.8)-t*.035));'+
    'float f=fbm(uv+3.6*r);'+
    'vec3 dk=vec3(.86,.19,.11),md=vec3(1.,.247,.145),lt=vec3(1.,.36,.24);'+
    'vec3 c=mix(dk,md,smoothstep(.18,.62,f));c=mix(c,lt,smoothstep(.62,.95,f)*.55);'+
    'c+=(h(v*res+t)-.5)*.025;gl_FragColor=vec4(c,1.);}';
  document.querySelectorAll('.panel.p-red').forEach(function(host){
    var c=canvasIn(host,'flow'),g=gl(c);if(!g){c.remove();return;}var P=prog(g,RED);if(!P){c.remove();return;}
    host.classList.add('has-shader');var run=false,t0=performance.now();
    function draw(){if(!run)return;var s=fit(c);g.viewport(0,0,s[0],s[1]);g.uniform1f(P.u('t'),(performance.now()-t0)/1000);g.uniform2f(P.u('res'),s[0],s[1]);g.drawArrays(g.TRIANGLE_STRIP,0,4);requestAnimationFrame(draw);}
    whenVisible(host,function(){if(!run){run=true;requestAnimationFrame(draw);}},function(){run=false;});
  });

  /* 2. fluted glass over the hero film */
  var GLASS='uniform sampler2D tx;uniform float t;uniform vec2 res,img,m;uniform float freq;'+COVER+
    'void main(){vec2 uv=cover(v,res,img);'+
    'float s=v.x*freq+t*.06+m.x*.6+sin(v.y*2.2+t*.25)*.18;float f=fract(s);'+
    'float o=sin((f-.5)*3.14159)*.042;'+
    'vec3 col;col.r=texture2D(tx,uv+vec2(o*1.18,0.)).r;col.g=texture2D(tx,uv+vec2(o,0.)).g;col.b=texture2D(tx,uv+vec2(o*.82,0.)).b;'+
    'col*=.9+.1*cos((f-.5)*3.14159);col+=vec3(1.)*(smoothstep(.965,1.,f)+smoothstep(.035,0.,f))*.07;'+
    'gl_FragColor=vec4(col,1.);}';
  var hero=null; /* fluted glass on the hero switched off */
  if(hero){var vid=hero.querySelector('video'),poster=hero.querySelector('.poster');
    var c=document.createElement('canvas');c.className='shader glass';c.setAttribute('aria-hidden','true');
    (vid||poster).insertAdjacentElement('afterend',c);var g=gl(c),P=g&&prog(g,GLASS);
    if(!P){c.remove();}else{var T=tex(g),run=false,t0=performance.now(),mx=.5,my=.5,emx=.5;
      hero.addEventListener('pointermove',function(e){var r=hero.getBoundingClientRect();mx=(e.clientX-r.left)/r.width;my=(e.clientY-r.top)/r.height;});
      function src(){if(vid&&vid.readyState>=2&&vid.videoWidth)return [vid,vid.videoWidth,vid.videoHeight];var pi=poster||(vid&&vid.poster?null:null);
        if(poster&&poster.complete&&poster.naturalWidth)return [poster,poster.naturalWidth,poster.naturalHeight];return null;}
      function draw(){if(!run)return;var S=src();if(S&&upload(g,T,S[0])){c.classList.add('on');var s=fit(c);g.viewport(0,0,s[0],s[1]);emx+=(mx-emx)*.04;
        g.uniform1f(P.u('t'),(performance.now()-t0)/1000);g.uniform2f(P.u('res'),s[0],s[1]);g.uniform2f(P.u('img'),S[1],S[2]);g.uniform2f(P.u('m'),emx-.5,my);
        g.uniform1f(P.u('freq'),window.innerWidth<700?7.:12.);g.drawArrays(g.TRIANGLE_STRIP,0,4);}requestAnimationFrame(draw);}
      whenVisible(hero,function(){if(!run){run=true;requestAnimationFrame(draw);}},function(){run=false;});
    }}

  if(!FINE) return;

  /* 3. footer wordmark melts and refracts under the cursor */
  var MELT='uniform sampler2D tx;uniform float t,hv,asp;uniform vec2 m;'+NOISE+'float sa(vec2 u){return texture2D(tx,u).a*step(0.,u.x)*step(u.x,1.)*step(0.,u.y)*step(u.y,1.);}'+
    'void main(){vec2 uv=v;'+
    'float idle=.3+.7*hv;uv.y+=(n(vec2(uv.x*7.,t*.25))-.5)*.018*idle;uv.x+=(n(vec2(uv.y*5.,t*.2+3.))-.5)*.008*idle;'+
    'vec2 d=uv-m;d.x*=asp;float r=length(d);float k=hv*exp(-r*r*7.);'+
    'uv-=vec2(d.x/asp,d.y)*k*.28;uv.y-=k*.06*smoothstep(0.,1.,1.-r);'+
    'float w=sin(r*26.-t*5.)*k*.012;uv+=normalize(d+1e-4)*w;'+
    'float ca=.0012+k*.014;float a=sa(uv),ar=sa(uv+vec2(ca,0.)),ab=sa(uv-vec2(ca,0.));'+
    'vec3 col=vec3(1.)*a+vec3(.733,.714,.886)*max(ar-a,0.)*1.4+vec3(.55)*max(ab-a,0.);'+
    'gl_FragColor=vec4(col,max(a,max(ar,ab)));}';
  /* footer wordmark: the watery melt is switched off, so the wordmark sits still and clean */
  [].forEach(function(fm){var im=fm.querySelector('img');if(!im)return;
    function start(){var c=canvasIn(fm,'melt'),g=gl(c),P=g&&prog(g,MELT);if(!P){c.remove();return;}
      var T=tex(g);if(!upload(g,T,scaled(im,2048))){c.remove();return;}fm.classList.add('has-shader');
      var run=false,t0=performance.now(),mx=-1,my=-1,hv=0,inside=false;
      /* mouse interaction removed: the wordmark keeps only its gentle watery drift */
      function draw(){if(!run)return;var s=fit(c);g.viewport(0,0,s[0],s[1]);g.clearColor(0,0,0,0);g.clear(g.COLOR_BUFFER_BIT);hv+=((inside?1:0)-hv)*.08;
        g.uniform1f(P.u('t'),(performance.now()-t0)/1000);g.uniform1f(P.u('hv'),hv);g.uniform1f(P.u('asp'),s[0]/s[1]);g.uniform2f(P.u('m'),mx,my);g.drawArrays(g.TRIANGLE_STRIP,0,4);requestAnimationFrame(draw);}
      whenVisible(fm,function(){if(!run){run=true;requestAnimationFrame(draw);}},function(){run=false;});}
    if(im.complete&&im.naturalWidth)start();else im.addEventListener('load',start);
  });

  /* 4. liquid ripple on work images: switched off */
  if(true) return;
  var RIP='uniform sampler2D tx;uniform float t,amp,asp;uniform vec2 m,box,img;'+COVER+
    'void main(){vec2 d=v-m;d.x*=asp;float r=length(d);'+
    'float wave=sin(r*30.-t*6.)*exp(-r*3.8)*amp*.024;'+
    'vec2 dir=normalize(d+1e-4);dir.x/=asp;'+
    'vec2 uv=v+dir*wave-vec2(d.x/asp,d.y)*exp(-r*r*9.)*amp*.11;'+
    'uv=cover(uv,box,img);float ca=wave*.9;'+
    'vec3 col;col.r=texture2D(tx,uv+dir*ca).r;col.g=texture2D(tx,uv).g;col.b=texture2D(tx,uv-dir*ca).b;'+
    'gl_FragColor=vec4(col,1.);}';
  var rc=document.createElement('canvas');rc.className='shader ripple';rc.setAttribute('aria-hidden','true');
  var rg=gl(rc),RP=rg&&prog(rg,RIP);
  if(RP){var RT=tex(rg),cur=null,amp=0,target=0,mx=.5,my=.5,t0=performance.now(),loop=false;
    function source(tile){var v=tile.querySelector('video.hv');if(v&&v.readyState>=2&&!v.paused&&v.videoWidth)return [v,v.videoWidth,v.videoHeight,true];
      var i=tile.querySelector('.media img');if(i&&i.complete&&i.naturalWidth)return [i,i.naturalWidth,i.naturalHeight,false];return null;}
    var lastStatic=null;
    function frame(){if(!cur){loop=false;return;}amp+=(target-amp)*.09;var S=source(cur);
      if(S){if(S[3]||lastStatic!==S[0]){upload(rg,RT,S[0]);lastStatic=S[3]?null:S[0];}rc.classList.add('on');var s=fit(rc);rg.viewport(0,0,s[0],s[1]);
        rg.uniform1f(RP.u('t'),(performance.now()-t0)/1000);rg.uniform1f(RP.u('amp'),amp);rg.uniform1f(RP.u('asp'),s[0]/s[1]);rg.uniform2f(RP.u('m'),mx,my);
        rg.uniform2f(RP.u('box'),s[0],s[1]);rg.uniform2f(RP.u('img'),S[1],S[2]);rg.drawArrays(rg.TRIANGLE_STRIP,0,4);}
      if(target===0&&amp<.01){rc.classList.remove('on');cur=null;loop=false;return;}requestAnimationFrame(frame);}
    document.querySelectorAll('.tile').forEach(function(tile){var media=tile.querySelector('.media');if(!media||media.querySelector('.typo'))return;
      tile.addEventListener('pointerenter',function(){if(cur!==tile){cur=tile;lastStatic=null;media.appendChild(rc);amp=0;}target=1;if(!loop){loop=true;requestAnimationFrame(frame);}});
      tile.addEventListener('pointermove',function(e){var r=media.getBoundingClientRect();mx=(e.clientX-r.left)/r.width;my=1.-(e.clientY-r.top)/r.height;});
      tile.addEventListener('pointerleave',function(){target=0;});
    });
  }
})();
