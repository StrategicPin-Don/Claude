// Render every HTML page in this folder to ../<name>.png at its own size, and run layout checks.
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const here = __dirname; const out = path.dirname(here);
  const pages = fs.readdirSync(here).filter(f => f.endsWith('.html'));
  const b = await chromium.launch();
  for (const f of pages) {
    const name = f.replace('.html', '');
    const scales = name.startsWith('email-') ? [1, 2] : [1];
    for (const sc of scales) {
      const p = await b.newPage({ viewport: { width: 100, height: 100 }, deviceScaleFactor: sc });
      await p.goto('file://' + path.join(here, f));
      await p.evaluate(() => document.fonts.ready);
      const size = await p.evaluate(() => { const e = document.querySelector('.page'); return [e.offsetWidth, e.offsetHeight]; });
      await p.setViewportSize({ width: size[0], height: size[1] });
      await p.waitForTimeout(250);
      const rep = await p.evaluate(() => {
        const W = document.querySelector('.page').offsetWidth, H = document.querySelector('.page').offsetHeight;
        const issues = [];
        document.querySelectorAll('.fit').forEach(e => { if (e.scrollWidth > e.clientWidth + 1) issues.push('overflow: ' + e.textContent.slice(0, 40)); });
        document.querySelectorAll('.page *').forEach(e => { const r = e.getBoundingClientRect(); if (e.tagName !== 'DIV' || !e.textContent.trim() || e.children.length) return; if (r.right > W + 1 || r.bottom > H + 1) issues.push('outside: ' + e.textContent.slice(0, 40)); });
        // text area: union of line boxes of text-bearing elements
        let area = 0;
        document.querySelectorAll('.txt, .lab').forEach(e => {
          const range = document.createRange(); range.selectNodeContents(e);
          for (const r of range.getClientRects()) area += r.width * r.height;
        });
        return { issues, textShare: Math.round(1000 * area / (W * H)) / 10 };
      });
      const file = path.join(out, name + (sc === 2 ? '@2x' : '') + '.png');
      await p.screenshot({ path: file, clip: { x: 0, y: 0, width: size[0], height: size[1] } });
      console.log(name, sc + 'x', size.join('x'), 'text%', rep.textShare, rep.issues.join(' | '));
      await p.close();
    }
  }
  await b.close();
})();
