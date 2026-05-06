(function(){
  if(typeof window === 'undefined') return;
  function createPopover(content){
    const pop = document.createElement('div');
    pop.className = 'av-popover';
    pop.setAttribute('role','dialog');
    pop.setAttribute('aria-modal','true');
    pop.tabIndex = -1;
    const close = document.createElement('button');
    close.className = 'av-close';
    close.innerHTML = '\u00d7';
    close.addEventListener('click', ()=>{ closePopover(pop); });
    pop.appendChild(close);
    const inner = document.createElement('div');
    inner.className = 'av-popover-inner';
    if(typeof content === 'string') inner.innerHTML = content;
    else inner.appendChild(content);
    pop.appendChild(inner);
    document.body.appendChild(pop);
    return pop;
  }
  function closePopover(pop){
    if(!pop) return;
    if(pop.parentNode) pop.parentNode.removeChild(pop);
    document.removeEventListener('keydown', onKeydown);
  }
  function onKeydown(e){
    if(e.key === 'Escape'){
      const pop = document.querySelector('.av-popover');
      if(pop) closePopover(pop);
    }
  }
  function positionPopover(pop, rect){
    const pad = 8;
    const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
    const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
    const popW = Math.min(pop.offsetWidth, vw - 24);
    let top = rect.bottom + pad;
    let left = rect.left;
    // if overflow right
    if(left + popW > vw - 12) left = vw - popW - 12;
    // if overflow bottom, place above
    if(top + pop.offsetHeight > vh - 12){
      top = rect.top - pop.offsetHeight - pad;
    }
    if(top < 12) top = 12;
    pop.style.left = Math.max(12, left) + 'px';
    pop.style.top = top + 'px';
  }
  function buildContentFromCodes(codes){
    const container = document.createElement('div');
    codes.forEach(code => {
      // clone and place in pre for readability
      const pre = document.createElement('pre');
      const c = document.createElement('code');
      c.className = code.className || '';
      c.textContent = code.textContent;
      pre.appendChild(c);
      container.appendChild(pre);
    });
    return container;
  }
  function makeTrigger(td, codes){
    // keep first up to 3 visible
    const visibleCount = 3;
    const wrapper = document.createElement('div');
    wrapper.className = 'av-trigger-wrapper';
    for(let i=0;i<Math.min(visibleCount,codes.length);i++){
      const clone = codes[i].cloneNode(true);
      clone.className = clone.className || '';
      clone.style.marginRight = '6px';
      wrapper.appendChild(clone);
    }
    if(codes.length > visibleCount){
      const btn = document.createElement('button');
      btn.className = 'av-trigger';
      btn.type = 'button';
      btn.innerText = 'Show all';
      btn.addEventListener('click', (ev)=>{
        ev.stopPropagation();
        // remove existing popover
        const existing = document.querySelector('.av-popover');
        if(existing) closePopover(existing);
        const content = buildContentFromCodes(codes);
        const pop = createPopover(content);
        positionPopover(pop, td.getBoundingClientRect());
        // focus for accessibility
        pop.focus();
        document.addEventListener('keydown', onKeydown);
      });
      wrapper.appendChild(btn);
    }
    // provide keyboard activation on wrapper
    wrapper.tabIndex = 0;
    wrapper.addEventListener('keydown', function(e){
      if(e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const btn = wrapper.querySelector('.av-trigger');
        if(btn) btn.click();
      }
    });
    return wrapper;
  }
  function init(){
    // scan table cells for multiple code elements
    const tds = document.querySelectorAll('table td');
    tds.forEach(td => {
      const codes = Array.from(td.querySelectorAll('code'));
      if(codes.length <= 3) return; // nothing to do
      // create trigger and replace cell content
      const trigger = makeTrigger(td, codes);
      // store codes in data attribute? we will keep clones inside closure
      td.innerHTML = '';
      td.appendChild(trigger);
    });
  }
  // init on DOM ready
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
