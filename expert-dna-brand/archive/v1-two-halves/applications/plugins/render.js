// usage: node render.js <width> <height|full> <in.html> <out.png> [...pairs]
const { chromium } = require('playwright');
(async () => {
  const [,, w, h, ...pairs] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: parseInt(w), height: h === 'full' ? 800 : parseInt(h) } });
  for (let i = 0; i < pairs.length; i += 2) {
    await p.goto('file://' + pairs[i]);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    await p.screenshot({ path: pairs[i + 1], fullPage: h === 'full' });
  }
  await b.close();
})();
