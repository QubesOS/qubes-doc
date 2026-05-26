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
