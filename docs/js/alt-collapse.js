/* Shared collapse/expand for Allowable Values and Description
   - Wraps content in a measured container and adds a toggle
   - Reusable for any table column index and max line count
*/
(function(){
  'use strict';

  function setupCollapsible(colIndex, maxLines, showText, hideText) {
    var tables = document.querySelectorAll('.altStyle table');
    tables.forEach(function(table){
      var rows = table.querySelectorAll('tr');
      rows.forEach(function(row){
        var tds = row.querySelectorAll('td');
        if (!tds || tds.length <= colIndex) return;
        var cell = tds[colIndex];
        if (!cell) return;
        if (cell.querySelector('.av-wrapper')) return; // already processed
        var raw = cell.innerHTML.trim();
        if (!raw) return;

        // Create wrapper and content container
        var wrapper = document.createElement('div');
        wrapper.className = 'av-wrapper';
        var content = document.createElement('div');
        content.className = 'av-content';
        content.innerHTML = raw;
        wrapper.appendChild(content);
        // Replace cell contents
        cell.innerHTML = '';
        cell.appendChild(wrapper);

        // Measure line-height
        var computed = window.getComputedStyle(content);
        var lineHeight = parseFloat(computed.lineHeight);
        if (!lineHeight || isNaN(lineHeight)) {
          var span = document.createElement('span');
          span.style.visibility = 'hidden';
          span.style.whiteSpace = 'nowrap';
          span.textContent = 'A';
          content.appendChild(span);
          lineHeight = span.getBoundingClientRect().height || 16;
          content.removeChild(span);
        }

        var maxH = Math.round(lineHeight * maxLines);

        // allow content to fully render to measure full height
        wrapper.style.maxHeight = 'none';
        var fullH = wrapper.scrollHeight;
        if (fullH <= maxH + 4) {
          // short content — no toggle needed
          wrapper.style.maxHeight = 'none';
          return;
        }

        // Collapse by default
        wrapper.style.maxHeight = maxH + 'px';
        wrapper.classList.add('collapsed');

        // Create toggle button
        var btn = document.createElement('button');
        btn.className = 'av-toggle';
        btn.setAttribute('aria-expanded', 'false');
        btn.textContent = showText || 'Show more';
        btn.addEventListener('click', function(){
          var expanded = btn.getAttribute('aria-expanded') === 'true';
          if (!expanded) {
            // expand: animate to measured height, then clear to allow natural height
            var full = wrapper.scrollHeight;
            wrapper.style.maxHeight = full + 'px';
            btn.setAttribute('aria-expanded','true');
            btn.textContent = hideText || 'Show less';
            // after the transition completes, remove the max-height limit
            var onEnd = function(e) {
              if (e.propertyName === 'max-height') {
                wrapper.style.maxHeight = 'none';
                wrapper.removeEventListener('transitionend', onEnd);
              }
            };
            wrapper.addEventListener('transitionend', onEnd);
          } else {
            // collapse: ensure we start from a numeric height so the transition eases
            var currentFull = wrapper.scrollHeight;
            // If maxHeight is 'none' or unset, set it to the current full pixel height first
            var computed = window.getComputedStyle(wrapper).maxHeight;
            if (computed === 'none' || !computed) {
              wrapper.style.maxHeight = currentFull + 'px';
              // force a reflow so the browser recognizes the start height
              wrapper.getBoundingClientRect();
            }
            // then animate down to collapsed height
            wrapper.style.maxHeight = maxH + 'px';
            btn.setAttribute('aria-expanded','false');
            btn.textContent = showText || 'Show more';
          }
        });

        cell.appendChild(btn);
      });
    });
  }

  function init() {
    // Description: 3rd column (index 2) — 4 lines
    setupCollapsible(2, 4, 'More...', 'Hide');
    // Allowable Values: 4th column (index 3) — 3 lines (preserve previous behavior)
    setupCollapsible(3, 3, 'More...', 'Less' );

    // Add classes to the first and second tables on the page (if present).
    try {
      var allTables = document.querySelectorAll('table');
      if (allTables && allTables.length >= 1) {
        allTables[0].classList.add('currentMeta');
      }
      if (allTables && allTables.length >= 2) {
        allTables[1].classList.add('deprecated');
      }
    } catch (e) {
      // harmless if DOM isn't as expected
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
