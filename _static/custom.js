document.addEventListener('DOMContentLoaded', function() {
  const captions = document.querySelectorAll('p.caption');
  
  captions.forEach(caption => {
    if (caption.textContent.toLowerCase().includes('external')) {
      const warningDiv = document.createElement('div');
      warningDiv.style.cssText = `
        background-color: #fff3cd !important;
        border: 1px solid #ffc107 !important;
        border-left: 4px solid #ffc107 !important;
        padding: 12px !important;
        margin: 12px 0 !important;
        border-radius: 4px !important;
        font-size: 0.9em !important;
      `;
      warningDiv.innerHTML = `
        <p style="font-weight: bold; margin: 0 0 8px 0 !important; color: #856404 !important;">⚠️  Warning</p>
        <p style="margin: 0 !important; color: #333 !important;">This is unofficial content provided by community members or third parties. These guides have not been reviewed by the Qubes team. Use them at your own risk.</p>
      `;
      
      // Insert after the caption
      caption.insertAdjacentElement('afterend', warningDiv);
    }
  });
});
