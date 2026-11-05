const { chromium } = require('playwright');
(async () => {
  const [,, input, output, width] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: parseInt(width || '2400'), height: 800 } });
  await p.goto('file://' + input);
  await p.waitForTimeout(400);
  await p.screenshot({ path: output, fullPage: true });
  await b.close();
})();
