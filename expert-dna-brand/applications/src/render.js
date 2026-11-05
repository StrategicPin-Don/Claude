const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2]));
  const only = process.argv[3];
  const b = await chromium.launch();
  for (const j of jobs) {
    if (only && !j.out.includes(only)) continue;
    const ctx = await b.newContext({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: j.scale || 1 });
    const p = await ctx.newPage();
    await p.goto('file://' + j.html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
    let info = '';
    if (j.measure) {
      const r = await p.evaluate(() => { let a = 0; document.querySelectorAll('.t').forEach(e => { const b = e.getBoundingClientRect(); a += b.width * b.height; }); return a / (innerWidth * innerHeight); });
      info += ` text=${(r * 100).toFixed(1)}%`;
    }
    if (j.overflow) {
      const o = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); info += ` hoverflow=${o}`;
    }
    // collision check: any element extending beyond the canvas (non-full pages)
    if (!j.full) {
      const out = await p.evaluate(() => { const W = innerWidth, H = innerHeight; const bad = []; document.querySelectorAll('.t,.h,.lab').forEach(e => { const r = e.getBoundingClientRect(); if (r.right > W + 1 || r.bottom > H + 1) bad.push(e.textContent.slice(0, 30)); }); return bad; });
      if (out.length) info += ` OUTSIDE:${JSON.stringify(out)}`;
    }
    await p.screenshot({ path: j.out, fullPage: !!j.full });
    console.log(j.out.split('/').slice(-2).join('/') + info);
    await ctx.close();
  }
  await b.close();
})();
