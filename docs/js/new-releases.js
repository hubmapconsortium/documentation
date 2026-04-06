// Highlight newly released assays and provide Ctrl+ArrowUp,ArrowUp quick-toggle
(function(){
  'use strict';
  const newReleases = ["10XMultiome", "ATACseq", "AutoFluorescence", "CellDIVE", "CODEX", "DESI", "Histology", "IMC", "LC-MS", "LightSheet", "MALDI", "MIBI", "MUSIC", "RNAseq", "RNAseqWithProbes", "VisiumNoProbes"];

  // Inject minimal styling for the left accent and highlight at runtime
  (function injectStyle(){
    try {
      var css = '' +
        'table.currentMeta tr, .altStyle table tr { border-left: 4px solid #444a65; }' +
        'table.currentMeta td, .altStyle table td { padding-left: .75rem; }' +
        '.new-release-highlight { background-color: #fff8e1; border-left: 4px solid #ffc107; transition: background-color .25s ease, border-color .25s ease; }';

      var style = document.createElement('style');
      style.setAttribute('data-generated','new-release-highlight-and-accent');
      style.appendChild(document.createTextNode(css));
      (document.head || document.documentElement).appendChild(style);
    } catch (e) {
      // silent fail
    }
  })();

  // Detect quick sequence: Ctrl + ArrowUp, ArrowUp
  let seqCount = 0;
  let lastTime = 0;
  const SEQ_TIMEOUT = 800; // ms

  function isAssayPage() {
    return !!document.querySelector('table.currentMeta') || !!document.querySelector('.altStyle table');
  }

  function highlightMatches() {
    document.querySelectorAll('.new-release-highlight').forEach(function(el){ el.classList.remove('new-release-highlight'); });
    var tables = document.querySelectorAll('table.currentMeta, .altStyle table');
    tables.forEach(function(table){
      table.querySelectorAll('tr').forEach(function(row){
        var links = row.querySelectorAll('a');
        for (var i=0;i<links.length;i++){
          var a = links[i];
          var href = a.getAttribute('href') || '';
          var txt = (a.textContent || '').trim();
          for (var j=0;j<newReleases.length;j++){
            var name = newReleases[j];
            if (!name) continue;
            if (href.indexOf(name) !== -1 || txt.indexOf(name) !== -1) {
              row.classList.add('new-release-highlight');
              break;
            }
          }
          if (row.classList.contains('new-release-highlight')) break;
        }
      });
    });
  }

  document.addEventListener('keydown', function(e){
    if (!e.ctrlKey) { seqCount = 0; return; }
    if (e.key === 'ArrowUp'){
      var now = Date.now();
      if (now - lastTime > SEQ_TIMEOUT) seqCount = 0;
      seqCount++;
      lastTime = now;
      if (seqCount >= 2){
        if (isAssayPage()){
          highlightMatches();
          var first = document.querySelector('.new-release-highlight');
          if (first) first.scrollIntoView({behavior: 'smooth', block: 'center'});
        }
        seqCount = 0;
      }
    } else {
      seqCount = 0;
    }
  });

  // Clear highlights on click or Escape
  document.addEventListener('click', function(){
    document.querySelectorAll('.new-release-highlight').forEach(function(el){ el.classList.remove('new-release-highlight'); });
  });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') { document.querySelectorAll('.new-release-highlight').forEach(function(el){ el.classList.remove('new-release-highlight'); }); } });

})();
