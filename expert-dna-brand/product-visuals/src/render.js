// Renders every job in jobs.json (html -> png, 2400x1600) and reports overflow.
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(__dirname + '/jobs.json'));
  const only = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2400, height: 1600 } });
  for (const j of jobs) {
    if (only && !j.out.includes(only)) continue;
    await p.goto('file://' + j.html);
    await p.waitForFunction(() => document.body.classList.contains('ready'));
    // overflow check: any element whose right/bottom edge leaves the canvas while not intended (abs elements bleeding are allowed)
    const over = await p.evaluate(() => {
      const bad = [];
      document.querySelectorAll('div,span').forEach(e => {
        if (e.children.length) return;
        const t = (e.textContent || '').trim(); if (!t) return;
        const r = e.getBoundingClientRect();
        if (r.right > 2400 || r.bottom > 1600 || r.left < 0) bad.push(t.slice(0, 40));
        if (e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).overflow !== 'visible') bad.push('clip:' + t.slice(0, 40));
      });
      return bad;
    });
    if (over.length) console.log('OVERFLOW', j.out.split('/').pop(), over.join(' | '));
    await p.screenshot({ path: j.out });
  }
  await b.close();
})();
