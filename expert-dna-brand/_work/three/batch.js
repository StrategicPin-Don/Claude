const { chromium } = require('playwright'); const fs = require('fs');
(async () => { const [,, listFile] = process.argv; const jobs = JSON.parse(fs.readFileSync(listFile));
  const b = await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  for (const j of jobs) { const p = await b.newPage({ viewport: { width: 2400, height: 1600 } });
    p.on('pageerror', e => console.log('err', j.out, e.message));
    await p.goto(j.url); await p.waitForFunction(() => window.__done === true, null, { timeout: 180000 });
    await p.screenshot({ path: j.out, omitBackground: true }); await p.close(); console.log('ok', j.out); }
  await b.close(); })();
