/* analytics signals for Google Tag Manager: form sent, email clicked, film played, CTA clicked */
function fwTrack(name,params){ try{ window.dataLayer=window.dataLayer||[]; var o={event:name}; for(var k in params) o[k]=params[k]; window.dataLayer.push(o); }catch(e){} }
document.addEventListener('click',function(e){ var a=e.target.closest('a'); if(!a) return;
  if((a.getAttribute('href')||'').indexOf('mailto:')===0) fwTrack('fw_email_click',{email:a.getAttribute('href').slice(7), page:location.pathname});
  var c=a.closest('[data-cta]'); if(c) fwTrack('fw_cta_click',{cta_name:c.getAttribute('data-cta'), cta_text:(c.textContent||'').trim().slice(0,60), page:location.pathname});
},true);
(function(){
  var root=document.documentElement; root.classList.add('js');
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var FINE = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var PREVIEW = !!window.__FW_PREVIEW;
  var IO = 'IntersectionObserver' in window;

  /* muted autoplay videos (hero, headline pills) */
  window.addEventListener('load',function(){ document.querySelectorAll('video[data-play-after-load]').forEach(function(v){ if(RM) return; v.setAttribute('preload','auto'); v.load(); var pr=v.play(); if(pr) pr.catch(function(){}); }); });
  document.querySelectorAll('video[autoplay]').forEach(function(v){ v.muted=true; if(RM){ v.removeAttribute('autoplay'); v.pause(); return; } var pr=v.play(); if(pr) pr.catch(function(){}); });

  /* reading-pace speed for the prose ticker */
  document.querySelectorAll('.ticker.words .track').forEach(function(t){ var w=t.scrollWidth/2; if(w) t.style.animationDuration=Math.round(w/50)+'s'; });

  /* ---------- header: adapts to the ground beneath it, hides on scroll down, returns on scroll up ---------- */
  var head=document.querySelector('.site-head'), menu=document.getElementById('menu');
  var DARK_SEL='.hero,.guild,.reel,.film,.sizzle,.mosaic,.strip3,.typo';
  function groundIsDark(el){
    for(var n=el;n&&n!==document.body;n=n.parentElement){
      if(n.matches && n.matches(DARK_SEL)) return true;
      var c=getComputedStyle(n).backgroundColor, m=c.match(/[\d.]+/g);
      if(m && (m.length<4 || +m[3]>.5)){ var l=(.2126*m[0]+.7152*m[1]+.0722*m[2])/255; return l<.5; }
    }
    var b=getComputedStyle(document.body).backgroundColor.match(/[\d.]+/g); return b ? (.2126*b[0]+.7152*b[1]+.0722*b[2])/255<.5 : false;
  }
  var lastY=window.scrollY, ticking=false, headH=head?head.offsetHeight:72;
  function underHead(){
    var x=Math.round(window.innerWidth/2), y=Math.round(headH/2), els=document.elementsFromPoint(x,y);
    for(var i=0;i<els.length;i++){ if(!head.contains(els[i]) && !(menu&&menu.contains(els[i])) && !els[i].classList.contains('skip') && !els[i].classList.contains('progress')) return els[i]; }
    return document.body;
  }
  function onScroll(){
    ticking=false; var y=window.scrollY, dy=y-lastY;
    if(head){
      head.setAttribute('data-theme', groundIsDark(underHead()) ? 'dark' : 'light');
      head.classList.toggle('is-solid', y>24);
      var open=root.classList.contains('menu-open'), focusIn=head.contains(document.activeElement);
      if(!open && !focusIn && y>headH*2 && dy>4) head.classList.add('is-hidden');
      else if(dy<-4 || y<=headH*2 || focusIn) head.classList.remove('is-hidden');
    }
    if(prog && art){ var a=art.getBoundingClientRect(), vh=window.innerHeight; var t=Math.max(0,Math.min(1,(vh-a.top)/(a.height))); prog.style.setProperty('--pr',t.toFixed(4)); }
    if(pxEls.length) parallax();
    lastY=y;
  }
  function requestTick(){ if(!ticking){ ticking=true; requestAnimationFrame(onScroll); } }
  window.addEventListener('scroll',requestTick,{passive:true});
  window.addEventListener('resize',function(){ headH=head?head.offsetHeight:72; requestTick(); },{passive:true});
  if(head) head.addEventListener('focusin',function(){ head.classList.remove('is-hidden'); });
  window.addEventListener('hashchange',function(){ setTimeout(requestTick,80); });

  /* ---------- menu: focus trap, Esc, scroll lock, focus return ---------- */
  var opener=document.querySelector('.site-head .menu-btn');
  if(opener && menu){
    var focusables=function(){ return Array.prototype.slice.call(menu.querySelectorAll('a[href],button')); };
    var openMenu=function(){ menu.classList.add('open'); root.classList.add('menu-open'); opener.setAttribute('aria-expanded','true'); setTimeout(function(){ var f=menu.querySelector('[data-close]'); if(f) f.focus(); },60); };
    var closeMenu=function(back){ menu.classList.remove('open'); root.classList.remove('menu-open'); opener.setAttribute('aria-expanded','false'); if(back!==false) opener.focus(); };
    opener.addEventListener('click',openMenu);
    menu.querySelector('[data-close]').addEventListener('click',function(){ closeMenu(); });
    menu.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ closeMenu(false); }); });
    document.addEventListener('keydown',function(e){
      if(!menu.classList.contains('open')) return;
      if(e.key==='Escape'){ e.preventDefault(); closeMenu(); return; }
      if(e.key==='Tab'){ var f=focusables(), first=f[0], last=f[f.length-1];
        if(e.shiftKey && document.activeElement===first){ e.preventDefault(); last.focus(); }
        else if(!e.shiftKey && document.activeElement===last){ e.preventDefault(); first.focus(); } }
    });
  }

  /* ---------- headlines: words rise out of a mask, staggered (the media pill grows in with them) ---------- */
  var HEADS='.page-hero h1, .proj-hero h1, .contact h2, .contact-page h1, .nf h1, .svc-top h1, .sec-title, .h2, .lw-head h2, .guild .over h2';
  function splitWords(el){
    var texts=[]; (function walk(n){ n.childNodes.forEach(function(c){ if(c.nodeType===3) texts.push(c); else if(c.nodeType===1 && !c.classList.contains('pill')) walk(c); }); })(el);
    texts.forEach(function(t){
      var parts=t.textContent.split(/(\s+)/), f=document.createDocumentFragment();
      parts.forEach(function(p){ if(!p) return; if(/^\s+$/.test(p)){ f.appendChild(document.createTextNode(p)); return; }
        var w=document.createElement('span'); w.className='w'; var wi=document.createElement('span'); wi.className='wi'; wi.textContent=p; w.appendChild(wi); f.appendChild(w); });
      t.parentNode.replaceChild(f,t);
    });
    var step = el.classList.contains('wi-title') ? 150 : 45;   /* the homepage opening statement gets a slower, more deliberate stagger */
    el.querySelectorAll('.wi').forEach(function(w,i){ w.style.transitionDelay=(Math.min(i,12)*step)+'ms'; });
  }
  if(!RM && IO){
    /* reveal headlines once the brand fonts are in (max 1.8s), so the font swap happens while the words are still hidden: no visible jump, no Times flash */
    var fontsIn=(document.fonts&&document.fonts.status!=='loaded') ? Promise.race([document.fonts.ready, new Promise(function(r){ setTimeout(r,1800); })]) : Promise.resolve();
    fontsIn.then(function(){ document.documentElement.classList.remove('fp'); });
    var hio=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ var el=e.target; hio.unobserve(el); fontsIn.then(function(){ requestAnimationFrame(function(){ el.classList.add('in'); }); }); } }); },{rootMargin:'0px 0px -10% 0px'});
    document.querySelectorAll(HEADS).forEach(function(h){ if(!h.textContent.trim()) return;
      if(!h.getAttribute('aria-label')) h.setAttribute('aria-label', h.textContent.replace(/\s+/g,' ').trim());   /* screen readers get the whole line, not word fragments */
      h.classList.add('rw'); if(!h.querySelector('.wi')) splitWords(h); else { var st=h.classList.contains('wi-title')?150:45; h.querySelectorAll('.wi').forEach(function(w,i){ w.style.transitionDelay=(Math.min(i,12)*st)+'ms'; }); } hio.observe(h); });
  } else { document.documentElement.classList.remove('fp'); document.querySelectorAll('.rw').forEach(function(h){ h.classList.add('in'); });
  }

  /* ---------- reveals: opacity + 20px rise, short staggers, nothing above the fold is hidden ---------- */
  var RV_SEL=['.sec-head','.split .l','.split .r','.sec-lbl','.intro-grid>*','.fw-lockup','.intro-three .col','.tile','.cards li','.im-head>*','.im-card',
    '.lw-head','.lw-grid','.dh-top>*','.dh-rows li','.dh-end','.door','.contact h2','.figures>div','.strip3>div',
    '.wwd','.c3-about>*','.box','.c3-steps li','.c3-offers li','.cw-list','.lead-row','.panel .row','.proj-body>*','.cs-sec','.cs-gallery img','.proj-quote>*',
    '.sizzle','.proj-img','.svc-row>*','.svc-logos','.svc-top-row>*','.nf>*',
    '.wi-lead','.pe','.guild .over>p','.guild .over>.sec-link','.ct-card','.sec-head>.sec-link'].join(',');
  if(!RM && IO){
    var rvio=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); rvio.unobserve(e.target); } }); },{rootMargin:'0px 0px -8% 0px',threshold:0.01});
    var vh0=window.innerHeight, groups=new Map();
    document.querySelectorAll(RV_SEL).forEach(function(el){
      if(el.closest('.overlay,.site-head,.foot') || (el.parentElement && el.parentElement.closest('.rv')) || el.matches('.rw') || el.querySelector('.rw')) return;   /* never nest reveals; headlines have their own */
      if(el.getBoundingClientRect().top < vh0*0.92) return;           /* already on screen: leave it */
      var p=el.parentElement, i=groups.get(p)||0; groups.set(p,i+1);
      el.style.setProperty('--rv-delay',(Math.min(i%4,3)*70)+'ms');
      el.classList.add('rv'); rvio.observe(el);
    });
  }

  /* ---------- count up (800ms), keeps the unit spans ---------- */
  function parseNum(s){ var m=s.match(/^([^0-9]*)([0-9][0-9,]*\.?[0-9]*)(.*)$/); if(!m) return null; return {pre:m[1], num:parseFloat(m[2].replace(/,/g,'')), dec:(m[2].split('.')[1]||'').length, comma:m[2].indexOf(',')>-1, suf:m[3]}; }
  function fmt(v,o){ var s=v.toFixed(o.dec); if(o.comma){ var a=s.split('.'); a[0]=a[0].replace(/\B(?=(\d{3})+(?!\d))/g,','); s=a.join('.'); } return o.pre+s+o.suf; }
  if(!RM && IO){
    var co=new IntersectionObserver(function(es){ es.forEach(function(e){ if(!e.isIntersecting) return; co.unobserve(e.target);
      var el=e.target, o=el._o, t0=null, d=2000, lag=(el._i||0)*160;
      function step(t){ if(t0===null) t0=t+lag; if(t<t0){ requestAnimationFrame(step); return; } var k=Math.min(1,(t-t0)/d), ease=1-Math.pow(1-k,3); el.textContent=fmt(o.num*ease,o); if(k<1) requestAnimationFrame(step); }
      requestAnimationFrame(step); }); },{threshold:.5});
    document.querySelectorAll('[data-count]').forEach(function(c){ var el=c.querySelector('.num')||c, o=parseNum(el.textContent.trim()); if(!o) return;
      var cr=c.getBoundingClientRect(); if(cr.height>0 && cr.top < window.innerHeight*0.85) return; /* hidden (zero-size) numbers still count up when shown */
      var g=c.closest('.im-grid,.pstats,.svc-stats'); c._i = g ? Array.prototype.indexOf.call(g.querySelectorAll('[data-count]'),c) : 0;
      el._o=o; el._i=c._i; el.textContent=fmt(0,o); co.observe(el); });
  }

  /* ---------- work tiles: self-hosted hover loops, then Vimeo background as fallback ---------- */
  if(FINE && !RM){
    document.querySelectorAll('.tile[data-loop]').forEach(function(t){ var v=null, m=t.querySelector('.media');
      t.addEventListener('pointerenter',function(){ if(!v){ v=document.createElement('video'); v.className='hv'; v.muted=true; v.loop=true; v.playsInline=true; v.setAttribute('aria-hidden','true'); v.src=t.getAttribute('data-loop'); v.addEventListener('playing',function(){ v.classList.add('on'); }); m.appendChild(v);} v.play().catch(function(){}); });
      t.addEventListener('pointerleave',function(){ if(v){ v.pause(); v.classList.remove('on'); } });
    });
  }
  var lv=document.querySelectorAll('video.lazyvid');
  if(lv.length && IO){
    var lo=new IntersectionObserver(function(es){ es.forEach(function(e){ var v=e.target;
      if(e.isIntersecting){ if(RM) return; if(!v.src){ v.src=v.getAttribute('data-src'); } v.play().catch(function(){}); } else if(v.src){ v.pause(); } }); },{rootMargin:'200px 0px'});
    lv.forEach(function(v){ lo.observe(v); });
  }
  function vsrc(id,h,bg){ return 'https://player.vimeo.com/video/'+id+'?'+(h?'h='+h+'&':'')+(bg?'background=1&muted=1&loop=1&autoplay=1':'autoplay=1&title=0&byline=0&portrait=0')+'&dnt=1'; }
  if(FINE && !RM && !PREVIEW){
    document.querySelectorAll('.tile[data-vimeo]:not([data-loop])').forEach(function(t){ var timer=null, fr=null, m=t.querySelector('.media');
      t.addEventListener('pointerenter',function(){ timer=setTimeout(function(){ if(!fr){ fr=document.createElement('iframe'); fr.allow='autoplay; fullscreen'; fr.title=''; fr.setAttribute('aria-hidden','true'); fr.tabIndex=-1; fr.src=vsrc(t.getAttribute('data-vimeo'),t.getAttribute('data-h'),true); fr.addEventListener('load',function(){ setTimeout(function(){ fr && fr.classList.add('on'); },400); }); m.appendChild(fr);} else { fr.classList.add('on'); } },180); });
      t.addEventListener('pointerleave',function(){ clearTimeout(timer); if(fr){ fr.remove(); fr=null; } });
    });
  }
  /* click to play on project pages */
  document.querySelectorAll('.film[data-vimeo] .play').forEach(function(b){ b.addEventListener('click',function(){ var f=b.closest('.film');
    if(PREVIEW){ if(!f.querySelector('.note')){ var n=document.createElement('p'); n.className='note'; n.textContent='Films play on the live site.'; f.appendChild(n);} return; }
    fwTrack('fw_video_play',{video_title:b.getAttribute('aria-label')||'', page:location.pathname});
    var fr=document.createElement('iframe'); fr.allow='autoplay; fullscreen; picture-in-picture'; fr.allowFullscreen=true; fr.title=b.getAttribute('aria-label'); fr.src=vsrc(f.getAttribute('data-vimeo'),f.getAttribute('data-h'),false); f.innerHTML=''; f.appendChild(fr); fr.focus(); }); });

  /* ---------- parallax: subtle, editorial imagery only ---------- */
  var pxEls=[];
  if(!RM){ document.querySelectorAll('.strip3>div,.panel .media,.wwd .wimg,.tile .media,.mosaic,.door .thumb').forEach(function(m){ m.classList.add('px'); if(m.matches('.tile .media,.door .thumb')) m.classList.add('px-strong'); pxEls.push(m); }); }
  function parallax(){ var vh=window.innerHeight; for(var i=0;i<pxEls.length;i++){ var r=pxEls[i].getBoundingClientRect(); if(r.bottom<0||r.top>vh) continue; var c=(r.top+r.height/2-vh/2)/vh; pxEls[i].style.setProperty('--py',(c*(pxEls[i].classList.contains('px-strong')?-6:-3)).toFixed(2)+'%'); } }

  /* ---------- scarlet dot that trails the pointer over work tiles ---------- */
  if(FINE && !RM){
    var disc=document.createElement('div'); disc.className='cursor-disc'; disc.setAttribute('aria-hidden','true'); document.body.appendChild(disc);
    var tx=-200, ty=-200, dx=-200, dy=-200, on=false, raf=0;
    function follow(){ dx+=(tx-dx)*.35; dy+=(ty-dy)*.35; disc.style.setProperty('--cx',dx+'px'); disc.style.setProperty('--cy',dy+'px');
      raf = (on || Math.abs(tx-dx)+Math.abs(ty-dy)>.5) ? requestAnimationFrame(follow) : 0; }
    window.addEventListener('pointermove',function(e){ tx=e.clientX; ty=e.clientY; if(on && !raf) raf=requestAnimationFrame(follow); },{passive:true});
    document.querySelectorAll('.tile').forEach(function(t){
      t.addEventListener('pointerenter',function(e){ if(!on){ dx=tx=e.clientX; dy=ty=e.clientY; } on=true; disc.classList.add('on'); if(!raf) raf=requestAnimationFrame(follow); });
      t.addEventListener('pointerleave',function(){ on=false; disc.classList.remove('on'); });
    });
  }

  /* article reading progress */
  var prog=null, art=document.querySelector('.article-body');
  if(art){ prog=document.createElement('div'); prog.className='progress'; prog.setAttribute('aria-hidden','true'); document.body.appendChild(prog); }
  onScroll();

  /* ---------- voices carousel: pause control, pauses on hover and focus, no autoplay under reduced motion ---------- */
  document.querySelectorAll('.voices').forEach(function(v){ var s=v.querySelectorAll('.slide'), i=0, c=v.querySelector('.count'), timer=null, paused=RM, hover=false;
    var tg=v.querySelector('[data-toggle]');
    function go(n,manual){ s[i].classList.remove('on'); i=(n+s.length)%s.length; s[i].classList.add('on'); if(c) c.textContent=(i+1)+' / '+s.length; v.setAttribute('aria-live',manual?'polite':'off'); }
    function run(){ clearInterval(timer); if(!paused && !hover) timer=setInterval(function(){ go(i+1); },8000); }
    function setPaused(p){ paused=p; if(tg){ tg.setAttribute('aria-pressed',p?'true':'false'); tg.setAttribute('aria-label',p?'Play quotes':'Pause quotes'); tg.classList.toggle('is-paused',p); } run(); }
    v.querySelector('[data-prev]').addEventListener('click',function(){ go(i-1,true); run(); });
    v.querySelector('[data-next]').addEventListener('click',function(){ go(i+1,true); run(); });
    if(tg) tg.addEventListener('click',function(){ setPaused(!paused); });
    v.addEventListener('pointerenter',function(){ hover=true; run(); }); v.addEventListener('pointerleave',function(){ hover=false; run(); });
    v.addEventListener('focusin',function(){ hover=true; run(); }); v.addEventListener('focusout',function(){ hover=false; run(); });
    setPaused(paused);
  });
})();

/* ---------- HubSpot enquiry form: loaded when the contact band comes near, then dressed in the brand ---------- */
(function(){
  var wraps=document.querySelectorAll('.hs-wrap'); if(!wraps.length) return;
  var css=document.querySelector('link[rel="stylesheet"][href*="site.css"]'), FONTS=css?css.href.replace(/site\.css.*$/,'fonts/'):'';
  var FORM_CSS=
    '@font-face{font-family:"Hanken";src:url('+FONTS+'hanken.woff2) format("woff2");font-weight:100 900}'+
    '@font-face{font-family:"FW Cond";src:url('+FONTS+'cond-600.woff2) format("woff2");font-weight:600}'+
    'html,body{background:transparent!important;margin:0}'+
    'body,.hs-form{font-family:"Hanken",system-ui,sans-serif!important;color:#1E1B18;-webkit-font-smoothing:antialiased}'+
    '.hs-form fieldset{max-width:none!important}.hs-form fieldset.form-columns-2 .hs-form-field{width:50%!important;float:left;padding-right:24px;box-sizing:border-box}'+
    '.hs-form fieldset.form-columns-2 .hs-form-field:last-child{padding-right:0}.hs-form .input{margin-right:0!important}'+
    '.hs-form .hs-form-field{margin:0 0 22px}'+
    '.hs-form label:not(.hs-form-booleancheckbox-display){display:block;margin:0 0 4px;font-family:"FW Cond","Arial Narrow",sans-serif!important;font-weight:600;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:#1E1B18!important}'+
    '.hs-form .hs-form-required{color:#C8290F;margin-left:2px}'+
    '.hs-form .hs-input{width:100%!important;box-sizing:border-box;height:auto!important;min-height:48px;margin:0;padding:10px 0!important;background:transparent!important;border:0!important;border-bottom:1px solid rgba(30,27,24,.4)!important;border-radius:0!important;box-shadow:none!important;font:inherit!important;font-size:18px!important;line-height:1.4!important;color:#1E1B18!important;transition:border-color .18s,box-shadow .18s}'+
    '.hs-form textarea.hs-input{min-height:120px;resize:vertical}'+
    '.hs-form .hs-input:hover{border-bottom-color:#20243A!important}'+
    '.hs-form .hs-input:focus{outline:none;border-bottom-color:#20243A!important;box-shadow:0 1px 0 0 #20243A!important}'+
    '.hs-form .hs-input.invalid.error{border-bottom-color:#C8290F!important;box-shadow:0 1px 0 0 #C8290F!important}'+
    '.hs-form select.hs-input{appearance:none;-webkit-appearance:none;background:transparent url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2712%27 height=%278%27%3E%3Cpath d=%27M1 1l5 5 5-5%27 fill=%27none%27 stroke=%27%2320243A%27 stroke-width=%271.5%27/%3E%3C/svg%3E") right 4px center no-repeat!important}'+
    '.hs-form input[type=checkbox],.hs-form input[type=radio]{width:18px!important;min-height:0;height:18px!important;margin:0 10px 0 0!important;accent-color:#20243A}'+
    '.hs-form .inputs-list{list-style:none;padding:0;margin:0}.hs-form .inputs-list label{display:flex;align-items:flex-start;font-size:15px}'+
    '.hs-form .hs-error-msgs{list-style:none;padding:0;margin:6px 0 0}.hs-form .hs-error-msg,.hs-form .hs-error-msgs label{font-family:"Hanken",sans-serif!important;font-size:14px!important;letter-spacing:0!important;text-transform:none!important;color:#C8290F!important}'+
    '.hs-form .legal-consent-container,.hs-form .hs-richtext,.hs-form .legal-consent-container p{font-size:14px!important;line-height:1.5!important;color:#5F5B55!important}.hs-form .legal-consent-container a{color:#20243A}'+
    '.hs-form .hs_submit{margin-top:12px}.hs-form .actions{padding:0;margin:0;text-align:left!important}'+
    '.hs-form .hs-button,.hs-form input[type=submit]{display:inline-flex;align-items:center;min-height:52px;padding:0 30px!important;border:0!important;border-radius:999px!important;background:#20243A!important;color:#EDEBE3!important;'+
      'font-family:"FW Cond","Arial Narrow",sans-serif!important;font-weight:600!important;font-size:14px!important;letter-spacing:.1em!important;text-transform:uppercase!important;cursor:pointer;box-shadow:none!important;transition:background-color .18s,color .18s;-webkit-appearance:none;appearance:none}'+
    '.hs-form .hs-button:hover,.hs-form input[type=submit]:hover{background:#FF3F25!important;color:#1E1B18!important}'+
    '.hs-form .hs-button:focus-visible,.hs-form input[type=submit]:focus-visible{outline:2px solid #20243A;outline-offset:4px}'+
    '.submitted-message{font-family:"Hanken",sans-serif;font-size:20px;line-height:1.4;color:#1E1B18}'+
    '@media (max-width:560px){.hs-form fieldset.form-columns-2 .hs-form-field{width:100%!important;float:none;padding-right:0}}';
  function load(src,cb,fail){ var s=document.createElement('script'); s.src=src; s.async=true; s.onload=cb; s.onerror=function(){ if(fail) fail(); }; document.head.appendChild(s); }
  function dress(t,w){ var fr=t.querySelector('iframe'); if(!fr) { w.classList.add('ready'); return; }
    var go=function(){ try{ var d=fr.contentDocument; if(!d||!d.head) return false; if(!d.getElementById('fw-brand')){ var st=d.createElement('style'); st.id='fw-brand'; st.textContent=FORM_CSS; d.head.appendChild(st); }
      var resize=function(){ fr.style.height=(d.documentElement.scrollHeight)+'px'; }; resize(); if(window.ResizeObserver) new ResizeObserver(resize).observe(d.body); w.classList.add('ready'); return true; }catch(e){ w.classList.add('ready'); return true; } };
    if(!go()){ fr.addEventListener('load',go); } }
  function mount(w){
    if(w.dataset.mounted) return; w.dataset.mounted='1';
    var portal=w.getAttribute('data-hs-portal'), form=w.getAttribute('data-hs-form'), t=w.querySelector('.hs-target');
    var fail=function(){ if(!w.classList.contains('ready')) w.classList.add('failed'); };   /* no form (blocked or offline): collapse to the fallback button */
    setTimeout(fail, 8000);
    function newEmbed(){ if(t.querySelector('form,iframe')) return; t.innerHTML='<div class="hs-form-frame" data-region="eu1" data-form-id="'+form+'" data-portal-id="'+portal+'"></div>';
      load('https://js-eu1.hsforms.net/forms/embed/'+portal+'.js',function(){ var n=0, iv=setInterval(function(){ if(t.querySelector('iframe,form')){ w.classList.add('ready'); clearInterval(iv);} if(++n>40) clearInterval(iv); },250); }); }
    load('https://js-eu1.hsforms.net/forms/embed/v2.js',function(){
      try{ window.hbspt.forms.create({region:'eu1',portalId:portal,formId:form,target:'#'+t.id,css:'',cssClass:'fw-hs',submitButtonClass:'fw-hs-submit',onFormReady:function(){ dress(t,w); },onFormSubmitted:function(){ fwTrack('fw_form_submitted',{form_location:location.pathname}); }}); }catch(e){ newEmbed(); }
      setTimeout(function(){ if(!t.querySelector('form,iframe')) newEmbed(); },4000);
    }, fail);
  }
  if(!('IntersectionObserver' in window)){ wraps.forEach(mount); return; }
  var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ mount(e.target); io.unobserve(e.target);} }); },{rootMargin:'600px 0px'});
  wraps.forEach(function(w){ io.observe(w); });
})();

/* Film pop-up: work tiles and stat cards play their film when the case study pages are off */
(function(){
  var tiles=document.querySelectorAll('a.film-tile[data-vimeo]'); if(!tiles.length) return;
  function src(id,h){ return 'https://player.vimeo.com/video/'+id+'?'+(h?'h='+h+'&':'')+'autoplay=1&title=0&byline=0&portrait=0&dnt=1'; }
  var dlg=document.createElement('dialog'); dlg.className='film-modal'; dlg.setAttribute('aria-labelledby','fm-t');
  dlg.innerHTML='<div class="fm-bar"><p class="fm-title" id="fm-t"></p><button type="button" class="fm-close">Close</button></div><div class="fm-frame"></div>';
  document.body.appendChild(dlg);
  var frame=dlg.querySelector('.fm-frame'), title=dlg.querySelector('.fm-title'), last=null;
  function shut(){ if(dlg.open) dlg.close(); }
  dlg.addEventListener('close',function(){ frame.innerHTML=''; document.documentElement.classList.remove('fm-open'); if(last) last.focus(); });
  dlg.querySelector('.fm-close').addEventListener('click',shut);
  dlg.addEventListener('click',function(e){ if(e.target===dlg) shut(); });
  tiles.forEach(function(t){ t.addEventListener('click',function(e){
    if(e.metaKey||e.ctrlKey||e.shiftKey||e.button===1||typeof dlg.showModal!=='function') return;
    e.preventDefault(); last=t; var name=t.getAttribute('data-title')||'Film'; title.textContent=name;
    var fr=document.createElement('iframe'); fr.allow='autoplay; fullscreen; picture-in-picture'; fr.allowFullscreen=true; fr.title=name;
    fr.src=src(t.getAttribute('data-vimeo'),t.getAttribute('data-h')); frame.appendChild(fr);
    document.documentElement.classList.add('fm-open'); dlg.showModal(); dlg.querySelector('.fm-close').focus();
  }); });
})();
/* cookie settings: reopen the consent banner once Cookiebot is live; until then, go to the cookie policy */
document.addEventListener('click',function(e){var b=e.target.closest('[data-cookie-settings]'); if(!b) return; e.preventDefault(); if(window.Cookiebot&&Cookiebot.renew){Cookiebot.renew();} else { var a=document.querySelector('.foot .legal a[href*="cookies/"]'); if(a) location.href=a.href; }});
/* rebrand note: only for visitors redirected from thelibertyguild.com (the redirect adds utm_source), shown once */
(function(){
  var q=new URLSearchParams(location.search), fromOld=/libertyguild/.test(q.get('utm_source')||'') || /libertyguild\.(com|co\.uk)/.test(document.referrer||'');
  if(!fromOld) return;
  try{ if(localStorage.getItem('fw-rebrand-seen')) return; localStorage.setItem('fw-rebrand-seen','1'); }catch(e){}
  var about=(document.querySelector('.site-head nav a[href*="agency/"]')||{}).getAttribute ? document.querySelector('.site-head nav a[href*="agency/"]').getAttribute('href') : 'agency/';
  var el=document.createElement('aside'); el.className='rebrand-note'; el.setAttribute('role','status'); el.setAttribute('aria-label','Looking for The Liberty Guild? We\u2019re now Freedom Works.');
  el.innerHTML='<p><b>Looking for The Liberty Guild?</b> <span>You\u2019re in the right place. We\u2019re now Freedom Works.</span> <a href="'+about+'">About us</a></p><button type="button" class="rn-close" aria-label="Close">\u00d7</button>';
  document.body.appendChild(el);
  setTimeout(function(){ el.classList.add('on'); fwTrack('fw_rebrand_note_view',{page:location.pathname}); }, 1200);
  el.querySelector('a').addEventListener('click',function(){ fwTrack('fw_rebrand_note_click',{page:location.pathname}); });
  el.querySelector('.rn-close').addEventListener('click',function(){ el.classList.remove('on'); setTimeout(function(){ el.remove(); },400); });
})();
window.__fwReady=true;
/* Services dropdown: the arrow button opens and closes it for touch and keyboard; hover and focus work too; Escape closes */
(function(){
  document.querySelectorAll('.nav-dd').forEach(function(dd){
    var b=dd.querySelector('.dd-btn'); if(!b) return;
    function set(o){ dd.classList.toggle('open',o); dd.classList.toggle('closed',!o && dd.matches(':hover')); b.setAttribute('aria-expanded',o?'true':'false'); }
    b.addEventListener('click',function(e){ e.preventDefault(); set(!dd.classList.contains('open')); });
    dd.addEventListener('mouseleave',function(){ dd.classList.remove('closed'); if(dd.classList.contains('open')) set(false); });
    dd.addEventListener('keydown',function(e){ if(e.key==='Escape'){ set(false); dd.classList.add('closed'); b.focus(); setTimeout(function(){dd.classList.remove('closed');},300); } });
    document.addEventListener('click',function(e){ if(!dd.contains(e.target)) set(false); });
  });
})();
/* articles: copy-link button, share tracking, and the sticky "Talk to us" (shows once reading starts, hides near the end panel) */
(function(){
  document.addEventListener('click',function(e){
    var s=e.target.closest('[data-share]'); if(!s) return;
    fwTrack('fw_share',{network:s.getAttribute('data-share'), page:location.pathname});
    if(s.hasAttribute('data-copy')){
      e.preventDefault(); var u=s.getAttribute('data-copy'), out=s.parentNode.querySelector('.copied');
      var done=function(){ if(out){ out.textContent='Link copied'; setTimeout(function(){out.textContent='';},2500);} };
      if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(u).then(done,function(){ window.prompt('Copy this link:',u); }); } else { window.prompt('Copy this link:',u); }
    }
  });
  var st=document.querySelector('.sticky-cta'); if(!st) return;
  var head=document.querySelector('.article-head'), stop=document.querySelector('.next-step')||document.querySelector('section.contact');
  var past=false, near=false;
  function upd(){ st.classList.toggle('on', past && !near); }
  if('IntersectionObserver' in window){
    if(head) new IntersectionObserver(function(es){ past=!es[0].isIntersecting && es[0].boundingClientRect.top<0; upd(); }).observe(head);
    [document.querySelector('.next-step'),document.querySelector('section.contact')].forEach(function(el){ if(!el) return;
      new IntersectionObserver(function(es){ es.forEach(function(x){ x.target.__vis=x.isIntersecting; }); near=[].some.call(document.querySelectorAll('.next-step,section.contact'),function(n){return n.__vis;}); upd(); }).observe(el); });
  }
})();
/* stacked DNA cards: a card taller than the screen scrolls fully into view before it pins, so the next card never covers its image and text */
(function(){
  var ps=document.querySelectorAll('.panels .panel'); if(!ps.length) return;
  function fit(){ ps.forEach(function(p){ if(window.innerWidth<=900){ p.style.top=''; return; } var over=p.offsetHeight-window.innerHeight; p.style.top= over>0 ? (-over)+'px' : ''; }); }
  fit(); window.addEventListener('load',fit); var t; window.addEventListener('resize',function(){ clearTimeout(t); t=setTimeout(fit,120); });
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(fit);
  /* re-fit whenever a card appears or changes size (page switches in the preview, late fonts and images) */
  if('ResizeObserver' in window){ var ro=new ResizeObserver(function(){ fit(); }); ps.forEach(function(p){ ro.observe(p); }); }
  window.addEventListener('hashchange',function(){ setTimeout(fit,50); });
})();

