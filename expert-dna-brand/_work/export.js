const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
// args: jobs.json  -> [{svg, out, width, height?}]
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2]));
  const b = await chromium.launch(); const p = await b.newPage();
  for (const j of jobs) {
    const s = fs.readFileSync(j.svg, 'utf8');
    const vb = s.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
    const w = j.width, h = j.height || Math.round(w * vb[3] / vb[2]);
    await p.setViewportSize({ width: w, height: h });
    const svg = s.replace(/width="[^"]+" height="[^"]+"/, `width="${w}" height="${h}"`);
    await p.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
    await p.screenshot({ path: j.out, omitBackground: true, clip: { x: 0, y: 0, width: w, height: h } });
  }
  await b.close();
})();
