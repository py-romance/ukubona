const glyphs = {
  'glyph-origin': \`🌊 Sea (Origins)...\`,
  'glyph-rules': \`❤️ Love (Rules)...\`,
  'glyph-recursion': \`🔁 Recursion (Games)...\`,
  'glyph-splicing': \`🎭 Theater (Splicing)...\`,
  'glyph-illusion': \`🤖 Illusion (Broadcast)...\`
};
document.querySelectorAll('.glyph').forEach(glyph => {
  glyph.innerText = glyph.getAttribute('data-glyph');
  glyph.addEventListener('click', () => {
    const content = glyphs[glyph.id];
    const details = document.getElementById('details');
    details.innerHTML = content;
    details.classList.add('visible');
  });
});