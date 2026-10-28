(function(){
  document.documentElement.classList.add('js');
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var FINE = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var PREVIEW = !!window.__FW_PREVIEW;

  /* make sure muted autoplay videos (hero, headline pills) are playing */
  document.querySelectorAll('video[autoplay]').forEach(function(v){ v.muted=true; if(RM && v.closest('.pill')) return; var pr=v.play(); if(pr) pr.catch(function(){}); });

  /* reading-pace speed for the prose ticker */
  document.querySelectorAll('.ticker.words .track').forEach(function(t){ var w=t.scrollWidth/2; if(w) t.style.animationDuration=Math.round(w/55)+'s'; });

  /* grain */
  var g=document.createElement('div'); g.className='grain'; g.setAttribute('aria-hidden','true'); document.body.appendChild(g);

  /* reveal words */
  function split(el){
    var walker=[]; (function walk(n){ n.childNodes.forEach(function(c){ if(c.nodeType===3) walker.push(c); else if(c.nodeType===1) walk(c); }); })(el);
    walker.forEach(function(t){
      var parts=t.textContent.split(/(\s+)/), f=document.createDocumentFragment();
      parts.forEach(function(p){ if(!p) return; if(/^\s+$/.test(p)){ f.appendChild(document.createTextNode(p)); return; }
        var w=document.createElement('span'); w.className='w'; var wi=document.createElement('span'); wi.className='wi'; wi.textContent=p; w.appendChild(wi); f.appendChild(w); });
      t.parentNode.replaceChild(f,t);
    });
    el.querySelectorAll('.wi').forEach(function(w,i){ w.style.transitionDelay=(Math.min(i,14)*0.045)+'s'; });
  }
  var heads=document.querySelectorAll('.giant, .page-hero h1, .sec-title, .h2, .contact h2, .contact-page h1, .guild .over h2, .proj-hero h1, .dna .head h2');
  if(!RM && 'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }); },{rootMargin:'0px 0px -12% 0px'});
    heads.forEach(function(h){ h.classList.add('rv'); split(h); io.observe(h); });
  }

  /* count up */
  function parseNum(s){ var m=s.match(/^([^0-9]*)([0-9][0-9,]*\.?[0-9]*)(.*)$/); if(!m) return null; return {pre:m[1], num:parseFloat(m[2].replace(/,/g,'')), dec:(m[2].split('.')[1]||'').length, comma:m[2].indexOf(',')>-1, suf:m[3]}; }
  function fmt(v,o){ var s=v.toFixed(o.dec); if(o.comma){ var a=s.split('.'); a[0]=a[0].replace(/\B(?=(\d{3})+(?!\d))/g,','); s=a.join('.'); } return o.pre+s+o.suf; }
  var counters=document.querySelectorAll('[data-count], .proof .big, .results .n, .figures .n');
  if(!RM && 'IntersectionObserver' in window){
    var co=new IntersectionObserver(function(es){ es.forEach(function(e){ if(!e.isIntersecting) return; co.unobserve(e.target);
      var el=e.target, o=parseNum(el.getAttribute('data-final')||el.textContent.trim()); if(!o) return; var t0=null, d=2000; var g=el.closest('.im-grid'); var lag=0; if(g){ var all=Array.prototype.indexOf.call(g.querySelectorAll('[data-count]'),el); lag=Math.max(0,all)*160; }
      function step(t){ if(!t0) t0=t+lag; if(t<t0){ requestAnimationFrame(step); return; } var k=Math.min(1,(t-t0)/d), ease=1-Math.pow(1-k,3); el.textContent=fmt(o.num*ease,o); if(k<1) requestAnimationFrame(step); }
      requestAnimationFrame(step); }); },{threshold:.4});
    counters.forEach(function(c){ var o=parseNum(c.textContent.trim()); if(!o) return; var r=c.getBoundingClientRect(); if(r.height===0||r.top>window.innerHeight*0.85){ c.setAttribute('data-final',fmt(o.num,o)); c.textContent=fmt(0,o); co.observe(c);} });
    setTimeout(function(){ document.querySelectorAll('[data-final]').forEach(function(c){ var r=c.getBoundingClientRect(); if(r.bottom<0 && /^[^0-9]*0(\.0+)?[^0-9]*$/.test(c.textContent)) c.textContent=c.getAttribute('data-final'); }); },4000);
  }

  /* impact cards rise in */
  var cards=document.querySelectorAll('.im-card');
  if(!RM && cards.length && 'IntersectionObserver' in window){
    var ci=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); ci.unobserve(e.target);} }); },{threshold:.2});
    cards.forEach(function(c,i){ c.style.transitionDelay=((i%6)*0.08)+'s'; c.classList.add('rise'); ci.observe(c); });
  }

  /* pointer state */
  var mx=-999,my=-999; window.addEventListener('pointermove',function(e){mx=e.clientX;my=e.clientY;},{passive:true});

  /* cursor disc */
  var disc=null, dx=-200, dy=-200, discOn=false;
  if(FINE){ disc=document.createElement('div'); disc.className='cursor-disc'; disc.setAttribute('aria-hidden','true'); document.body.appendChild(disc);
    document.querySelectorAll('.tile').forEach(function(t){
      t.addEventListener('pointerenter',function(){ discOn=true; disc.classList.add('on'); });
      t.addEventListener('pointerleave',function(){ discOn=false; disc.classList.remove('on'); });
    });
  }

  /* hover image on lists */
  var himg=null, hx=-400, hy=-400;
  var hoverRows=[]; /* cursor-following images removed */
  if(FINE && hoverRows.length){ himg=document.createElement('img'); himg.className='hover-img'; himg.alt=''; himg.setAttribute('aria-hidden','true'); document.body.appendChild(himg);
    hoverRows.forEach(function(r){ r.addEventListener('pointerenter',function(){ himg.src=r.getAttribute('data-img'); himg.classList.add('on'); });
      r.addEventListener('pointerleave',function(){ himg.classList.remove('on'); }); });
    himg.addEventListener('error',function(){ himg.classList.remove('on'); });
  }

  /* self-hosted hover loops */
  if(FINE && !RM){
    document.querySelectorAll('.tile[data-loop]').forEach(function(t){ var v=null, m=t.querySelector('.media');
      t.addEventListener('pointerenter',function(){ if(!v){ v=document.createElement('video'); v.className='hv'; v.muted=true; v.loop=true; v.playsInline=true; v.setAttribute('aria-hidden','true'); v.src=t.getAttribute('data-loop'); v.addEventListener('playing',function(){ v.classList.add('on'); }); m.appendChild(v);} v.play().catch(function(){}); });
      t.addEventListener('pointerleave',function(){ if(v){ v.pause(); v.classList.remove('on'); } });
    });
  }
  /* lazy autoplay videos (sizzles, project loops) */
  var lv=document.querySelectorAll('video.lazyvid');
  if(lv.length && 'IntersectionObserver' in window){
    var lo=new IntersectionObserver(function(es){ es.forEach(function(e){ var v=e.target;
      if(e.isIntersecting){ if(RM) return; if(!v.src){ v.src=v.getAttribute('data-src'); } v.play().catch(function(){}); } else if(v.src){ v.pause(); } }); },{rootMargin:'200px 0px'});
    lv.forEach(function(v){ lo.observe(v); });
  }
  /* hover-to-play films on tiles */
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
    var fr=document.createElement('iframe'); fr.allow='autoplay; fullscreen; picture-in-picture'; fr.allowFullscreen=true; fr.title=b.getAttribute('aria-label'); fr.src=vsrc(f.getAttribute('data-vimeo'),f.getAttribute('data-h'),false); f.innerHTML=''; f.appendChild(fr); }); });

  /* parallax targets */
  var pxEls=[]; if(!RM){ document.querySelectorAll('.tile .media, .wide, .mosaic, .door .thumb').forEach(function(m){ if(m.classList.contains('wide')){ var w=document.createElement('div'); w.className='px'; w.style.cssText='overflow:hidden'; m.parentNode.insertBefore(w,m); w.appendChild(m); pxEls.push(w);} else { m.classList.add('px'); pxEls.push(m);} }); }

  /* proof colour shift */
  var proof=document.querySelector('.proof');

  /* article progress */
  var prog=null, art=document.querySelector('.article-body');
  if(art){ prog=document.createElement('div'); prog.className='progress'; prog.setAttribute('aria-hidden','true'); document.body.appendChild(prog); }

  function frame(){
    var vh=window.innerHeight;
    if(disc){ dx+=(mx-dx)*(RM?1:.35); dy+=(my-dy)*(RM?1:.35); disc.style.setProperty('--cx',dx+'px'); disc.style.setProperty('--cy',dy+'px'); }
    if(himg){ hx+=(mx+24-hx)*.18; hy+=(my-110-hy)*.18; himg.style.setProperty('--hx',hx+'px'); himg.style.setProperty('--hy',hy+'px'); }
    for(var i=0;i<pxEls.length;i++){ var r=pxEls[i].getBoundingClientRect(); if(r.bottom<0||r.top>vh) continue; var c=(r.top+r.height/2-vh/2)/vh; pxEls[i].style.setProperty('--py',(c*-6).toFixed(2)+'%'); }
    if(proof && !RM){ var pr=proof.getBoundingClientRect(); var p=Math.max(0,Math.min(1,(vh*0.95-pr.top)/(vh*0.55))); proof.style.setProperty('--p',p.toFixed(3)); }
    if(prog && art){ var a=art.getBoundingClientRect(); var t=Math.max(0,Math.min(1,(vh-a.top)/(a.height))); prog.style.setProperty('--pr',t.toFixed(4)); }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  /* voices carousel */
  document.querySelectorAll('.voices').forEach(function(v){ var s=v.querySelectorAll('.slide'), i=0, c=v.querySelector('.count'), timer=null;
    function go(n){ s[i].classList.remove('on'); i=(n+s.length)%s.length; s[i].classList.add('on'); if(c) c.textContent=(i+1)+' / '+s.length; }
    v.querySelector('[data-prev]').addEventListener('click',function(){ go(i-1); restart(); });
    v.querySelector('[data-next]').addEventListener('click',function(){ go(i+1); restart(); });
    function restart(){ clearInterval(timer); if(!RM) timer=setInterval(function(){ go(i+1); },9000); }
    v.addEventListener('pointerenter',function(){ clearInterval(timer); }); v.addEventListener('pointerleave',restart); restart();
  });
})();
/* HubSpot enquiry form, loaded when the contact band comes near */
(function(){
  var wraps=document.querySelectorAll('.hs-wrap'); if(!wraps.length) return;
  function load(src,cb){ var s=document.createElement('script'); s.src=src; s.async=true; s.onload=cb; s.onerror=function(){}; document.head.appendChild(s); }
  function mount(w){
    if(w.dataset.mounted) return; w.dataset.mounted='1';
    var portal=w.getAttribute('data-hs-portal'), form=w.getAttribute('data-hs-form'), t=w.querySelector('.hs-target');
    function ready(){ w.classList.add('ready'); }
    function newEmbed(){ if(t.querySelector('form,iframe')) return; t.innerHTML='<div class="hs-form-frame" data-region="eu1" data-form-id="'+form+'" data-portal-id="'+portal+'"></div>';
      load('https://js-eu1.hsforms.net/forms/embed/'+portal+'.js',function(){ var n=0, iv=setInterval(function(){ if(t.querySelector('iframe,form')){ ready(); clearInterval(iv);} if(++n>40) clearInterval(iv); },250); }); }
    load('https://js-eu1.hsforms.net/forms/embed/v2.js',function(){
      try{ window.hbspt.forms.create({region:'eu1',portalId:portal,formId:form,target:'#'+t.id,css:'',cssClass:'fw-hs',submitButtonClass:'fw-hs-submit',onFormReady:ready}); }catch(e){ newEmbed(); }
      setTimeout(function(){ if(!t.querySelector('form,iframe')) newEmbed(); },4000);
    });
  }
  if(!('IntersectionObserver' in window)){ wraps.forEach(mount); return; }
  var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ mount(e.target); io.unobserve(e.target);} }); },{rootMargin:'600px 0px'});
  wraps.forEach(function(w){ io.observe(w); });
})();
