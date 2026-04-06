// Highlight newly released assays and provide Ctrl+ArrowUp,ArrowUp quick-toggle
(function(){
  'use strict';
  const newReleases = ["10XMultiome", "ATACseq", "AutoFluorescence", "CellDIVE", "CODEX", "DESI", "Histology", "IMC", "LC-MS", "LightSheet", "MALDI", "MIBI", "MUSIC", "RNAseq", "RNAseqWithProbes", "VisiumNoProbes"];

  // Styles for new-release highlighting are now provided by /css/releaseHighlight.css

  // Detect quick sequence: Ctrl + ArrowUp, ArrowUp
  let seqCount = 0;
  let lastTime = 0;
  const SEQ_TIMEOUT = 800; // ms

  function isAssayPage() {
    return true
    // return !!document.querySelector('table.currentMeta') || !!document.querySelector('.altStyle table');
  }

  function highlightMatches() {
    console.debug('%c◉ highlighting ', 'color:#2158FF', );
    document.querySelectorAll('.new-release-highlight').forEach(function(el){ el.classList.remove('new-release-highlight'); });
    var tables = document.querySelectorAll('table.currentMeta, .altStyle table');
      if (!tables || tables.length === 0) {
        tables = document.querySelectorAll('.altStyle table');
      }
      if (!tables || tables.length === 0) {
        tables = document.querySelectorAll('table');
      }
      console.debug('%c◉ new-releases: tables found', 'color:#2158FF', tables.length);
    console.debug('%c◉ tablesfound ', 'color:#00ff7b', );
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
                console.debug('%c◉ new-releases: matched', 'color:#00ff7b', name, txt || href);
              break;
            }
          }
          if (row.classList.contains('new-release-highlight')) break;
        }
      });
    });
  }

  document.addEventListener('keydown', function(e){
    console.debug('%c◉ addEventListener ', 'color:#2158FF', );
      // allow Ctrl+1 to trigger highlight immediately
      if (e.ctrlKey && e.key === '1') {
        if (isAssayPage()){
          console.debug('%c◉ highlighting ', 'color:#00ff7b', );
          highlightMatches();
          var first = document.querySelector('.new-release-highlight');
          if (first) first.scrollIntoView({behavior: 'smooth', block: 'center'});
        }
        seqCount = 0;
        return;
      }

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
