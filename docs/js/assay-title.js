(function () {
  'use strict';

  if (typeof document === 'undefined') {
    return;
  }

  var TITLE_MAP = {
    '4i': '4i',
    '10x-multiome': '10X Multiome',
    'auto-fluorescence': 'Autofluorescence (AF)',
    'atacseq': 'ATACseq',
    'codex': 'CODEX',
    'comet': 'COMET',
    'cosmx-proteomics': 'CosMx Proteomics',
    'cosmx-transcriptomics': 'CosMx Transcriptomics',
    'desi': 'DESI',
    'dna-methylation': 'DNA-Methylation',
    'enhancedsrs': 'Enhanced SRS',
    'geomx': 'GeoMx',
    'hifi': 'HiFi',
    'histology': 'Histology',
    'iclap': 'iCLAP',
    'illumina-spatial': 'Illumina Spatial ver0',
    'imc': 'IMC',
    'imc-2d': 'IMC-2D',
    'lc-ms': 'LC-MS',
    'light-sheet': 'Light Sheet',
    'maldi': 'MALDI-IMS',
    'mibi': 'MIBI',
    'merfish': 'MERFISH',
    'music': 'MUSIC',
    'music-(cedar)': 'MUSIC (CEDAR)',
    'mplex': 'MPLEx',
    'pixel-seqv2': 'Pixel-seqV2',
    'rnaseq': 'RNAseq',
    'rnaseq-(with-probes)': 'RNAseq with Probes',
    'raman-imaging': 'Raman-Imaging',
    'secondharmonicgeneration': 'SHG',
    'seq-scope': 'Seq-Scope',
    'seqfish': 'SeqFISH',
    'sims': 'SIMS',
    'slide-seq': 'Slide-seq',
    'snareseq2': 'SnareSeq2',
    'starmap': 'STARmap',
    'thicksectionmultiphotonmxif': 'MxIF',
    'visium-(no-probes)': 'Visium No Probes',
    'visiumwithprobes': 'Visium with Probes',
    'visium-hd': 'Visium HD',
    'wgs': 'WGS'
  };

  function normalizeKey(value) {
    return (value || '')
      .toString()
      .trim()
      .replace(/\s+metadata\s+attributes$/i, '')
      .replace(/\s+/g, ' ')
      .toLowerCase();
  }

  function prettifyFallback(value) {
    return (value || '')
      .replace(/\s+metadata\s+attributes$/i, '')
      .replace(/-/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function updateAssayHeading() {
    var heading = document.querySelector('.c-documentation h1');
    if (!heading) return;

    var rawText = heading.textContent || '';
    var key = normalizeKey(rawText);
    var title = TITLE_MAP[key] || prettifyFallback(rawText);
    var pageTitle = 'HuBMAP Documentation | Assays | Metadata\n' + title;

    heading.textContent = title;
    document.title = pageTitle;

    var titleEl = document.querySelector('title');
    if (titleEl) {
      titleEl.textContent = pageTitle;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateAssayHeading);
  } else {
    updateAssayHeading();
  }
})();
