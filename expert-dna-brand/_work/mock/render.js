const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 1600 } });
  const dir = process.argv[2], out = process.argv[3];
  for (const f of fs.readdirSync(dir).filter(f=>f.endsWith('.html'))) { await p.goto('file://' + path.join(dir,f)); await p.waitForTimeout(300);
    await p.screenshot({ path: path.join(out, f.replace('.html','.png')) }); }
  await b.close(); })();
