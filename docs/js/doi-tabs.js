(function () {
  if (typeof window === 'undefined') return;

  function setActiveTab(tabButtons, panels, activeId) {
    tabButtons.forEach((button) => {
      const isActive = button.id === activeId;
      button.classList.toggle('active', isActive);
      button.setAttribute('aria-selected', isActive ? 'true' : 'false');
      button.tabIndex = isActive ? 0 : -1;
    });

    panels.forEach((panel) => {
      panel.hidden = panel.id !== document.getElementById(activeId).getAttribute('aria-controls');
    });
  }

  function initTabs() {
    const tablist = document.querySelector('.tab-wrap[role="tablist"]');
    if (!tablist) return;

    const tabButtons = Array.from(tablist.querySelectorAll('[role="tab"]'));
    const panels = Array.from(document.querySelectorAll('.panel[role="tabpanel"]'));

    if (!tabButtons.length || !panels.length) return;

    function activate(tab) {
      if (!tab) return;
      setActiveTab(tabButtons, panels, tab.id);
    }

    tabButtons.forEach((button, index) => {
      button.addEventListener('click', () => activate(button));
      button.addEventListener('keydown', (event) => {
        const key = event.key;
        let nextIndex = null;

        if (key === 'ArrowRight' || key === 'ArrowDown') {
          nextIndex = (index + 1) % tabButtons.length;
        } else if (key === 'ArrowLeft' || key === 'ArrowUp') {
          nextIndex = (index - 1 + tabButtons.length) % tabButtons.length;
        } else if (key === 'Home') {
          nextIndex = 0;
        } else if (key === 'End') {
          nextIndex = tabButtons.length - 1;
        }

        if (nextIndex !== null) {
          event.preventDefault();
          tabButtons[nextIndex].focus();
          activate(tabButtons[nextIndex]);
        }
      });
    });

    activate(tabButtons.find((button) => button.classList.contains('active')) || tabButtons[0]);
  }

  function wrapAllowableValues() {
    const cells = document.querySelectorAll('.doiStyle .schema-wrap table td:nth-child(4), .doiStyle .deprecated-wrap table td:nth-child(4)');
    cells.forEach((cell) => {
      if (cell.querySelector('.allowable-values-scroll')) return;
      const wrapper = document.createElement('div');
      wrapper.className = 'allowable-values-scroll';
      while (cell.firstChild) {
        wrapper.appendChild(cell.firstChild);
      }
      cell.appendChild(wrapper);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initTabs();
      wrapAllowableValues();
    });
  } else {
    initTabs();
    wrapAllowableValues();
  }
})();
