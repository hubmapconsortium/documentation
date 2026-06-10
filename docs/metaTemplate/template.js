const tabs = document.querySelectorAll('.tab');
const panels = {
  'tab-meta': document.getElementById('panel-meta'),
  'tab-files': document.getElementById('panel-files')
};

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => {
      t.classList.remove('active');
      t.setAttribute('aria-selected', 'false');
    });
    Object.values(panels).forEach(panel => panel.hidden = true);

    tab.classList.add('active');
    tab.setAttribute('aria-selected', 'true');
    panels[tab.id].hidden = false;
  });
});
