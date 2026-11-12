document.addEventListener('DOMContentLoaded', function() {
  const captions = document.querySelectorAll('p.caption');

  captions.forEach(caption => {
    if (caption.textContent.toLowerCase().includes('external')) {
      const warningDiv = document.createElement('div');
      warningDiv.classList.add('rst-content')
      warningDiv.innerHTML = `
        <div class="admonition danger">
            <p class="admonition-title">Danger</p>
            <p>This is unofficial content provided by community members or third parties. These guides are not maintained by the Qubes team. Use them at your own risk.</p>
        </div>
      `;

      // Insert after the caption
      caption.insertAdjacentElement('afterend', warningDiv);
    }
  });
});

// The search modal's backdrop blur makes Firefox crawl without a GPU (qubes-issues#10730).
customElements.whenDefined('readthedocs-search').then(() => {
  const sheet = new CSSStyleSheet();
  sheet.replaceSync(':host > div .background { backdrop-filter: none !important; }');
  const patch = () => {
    const root = document.querySelector('readthedocs-search')?.shadowRoot;
    if (!root) return false;
    if (!root.adoptedStyleSheets.includes(sheet)) {
      root.adoptedStyleSheets = [...root.adoptedStyleSheets, sheet];
    }
    return true;
  };
  if (!patch()) {
    const observer = new MutationObserver(() => { if (patch()) observer.disconnect(); });
    observer.observe(document.documentElement, { childList: true, subtree: true });
  }
});
