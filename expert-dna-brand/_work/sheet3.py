import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from brand3 import *
def img(s,w): return s.replace("<svg ",f'<svg style="width:{w}px;height:auto;display:block" ',1)
ff=("@font-face{font-family:HK;font-weight:400;src:url(../fonts/HankenGrotesk-Regular.ttf)}@font-face{font-family:HK;font-weight:500;src:url(../fonts/HankenGrotesk-Medium.ttf)}"
    "@font-face{font-family:PM;src:url(../fonts/IBMPlexMono-Medium.ttf)}")
chips=[("Ink","ink","#fff"),("White","white","#101114"),("Paper","paper","#101114"),("Accent","accent","#101114"),("Accent tint","accent_tint","#101114"),("Accent deep","accent_deep","#fff"),("Grey","grey","#fff"),("Line","line","#101114")]
chip="".join(f'<div style="background:{C[k]};color:{t};height:180px;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;border:1px solid #E2E0DB"><span style="font:500 22px HK">{n}</span><span style="font:13px PM">{C[k]}</span></div>' for n,k,t in chips)
pv="../product-visuals"
apps=[f"{pv}/plugin-03-proposal/plugin-03-proposal-s1-interface.png",f"{pv}/plugin-03-proposal/plugin-03-proposal-s2-statement.png",f"{pv}/plugin-03-proposal/plugin-03-proposal-s3-inside.png",f"{pv}/plugin-03-proposal/plugin-03-proposal-s4-before-after.png",f"{pv}/plugin-03-proposal/plugin-03-proposal-s5-plug-in.png"]
apps=[a for a in apps if os.path.exists(os.path.join(ROOT,'_work',a))]
appimg="".join(f'<img src="{a}" style="width:100%;display:block">' for a in apps)
soc=["../applications/social-1080x1350-accent.png","../applications/social-1080x1080-dark.png","../applications/ad-1080x1350-dark.png","../applications/plugins/plugin-03-proposal.png"]
socimg="".join(f'<img src="{a}" style="height:380px;display:block">' for a in soc if os.path.exists(os.path.join(ROOT,'_work',a)))
html=f"""<!doctype html><meta charset=utf-8><style>{ff}*{{margin:0;box-sizing:border-box}}body{{width:2400px;background:#fff;color:#101114;font-family:HK}}
.lab{{font:13px PM;letter-spacing:.12em;text-transform:uppercase}}section{{padding:56px 64px;border-bottom:1px solid #E2E0DB}}h2{{font:500 40px HK;letter-spacing:-.03em;margin:10px 0 28px}}</style><body>
<section style="display:flex;justify-content:space-between;align-items:flex-end;padding-top:72px"><div><div class=lab>Brand sheet / version 2.0</div>
<div style="margin-top:40px">{img(horizontal(C['ink'],C['accent'],C['ink'],True,C['grey']),1000)}</div></div>
<p style="font-size:22px;line-height:1.5;max-width:700px">A half moon for the expert's mind, a plug for the connection to AI. Write down what lives in your head once, plug it in, and let AI run on it. Stay human. Automate the rest.</p></section>
<section style="display:grid;grid-template-columns:1fr 1fr 1fr;padding:0">
<div style="background:#101114;padding:56px 64px">{img(horizontal(C['white'],C['accent'],C['white']),560)}</div>
<div style="background:#FF5533;padding:56px 64px">{img(horizontal(C['ink'],C['ink'],C['ink']),560)}</div>
<div style="background:#F4F3F0;padding:56px 64px;display:flex;gap:48px;align-items:center">{img(mark_only(C['ink'],C['accent']),140)}{img(mark_only(C['ink'],C['accent']),48)}{img(mark_only(C['ink'],C['accent']),16)}</div></section>
<section><div class=lab>Colour</div><h2>White first, one signal accent</h2><div style="display:grid;grid-template-columns:repeat(8,1fr);gap:12px">{chip}</div></section>
<section style="display:grid;grid-template-columns:1.3fr 1fr;gap:64px"><div><div class=lab>Type</div><h2>Hanken Grotesk + IBM Plex Mono</h2>
<div style="font:500 120px HK;letter-spacing:-.03em;line-height:1">Aa Expert DNA</div>
<p style="font-size:20px;line-height:1.55;margin-top:24px;max-width:1000px">AI without context works like a confused intern. You write down what lives in your head, and the AI works from those files instead of from the internet's average.</p>
<div style="font:15px PM;letter-spacing:.12em;margin-top:20px">PLUGIN 03 / PROPOSAL / 29 EUR</div></div>
<div style="position:relative;overflow:hidden"><div class=lab>Motifs</div><h2>Half moon, pins, thin rules</h2>
<div style="display:flex;align-items:center;gap:40px;margin-top:20px"><div style="width:160px;height:320px;border-radius:160px 0 0 160px;background:#101114"></div>
<div style="flex:1"><div style="height:22px;background:#FF5533;width:100%"></div><div style="height:22px;background:#FF5533;width:69%;margin-top:80px"></div></div></div></div></section>
<section><div class=lab>Product visuals / same five styles for every product</div><h2>Interface, Statement, What's inside, Before and after, Plug-in</h2><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:16px">{appimg}</div></section>
<section><div class=lab>Applications</div><h2>Social, ads, plugin tiles</h2><div style="display:flex;gap:16px">{socimg}</div></section>
</body>"""
open("brandsheet3.html","w").write(html)
