import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from brand import *
def img(s,w): return s.replace("<svg ",f'<svg style="width:{w}px;height:auto;display:block" ',1)
ff=("@font-face{font-family:SG;font-weight:400;src:url(../fonts/SchibstedGrotesk-Regular.ttf)}@font-face{font-family:SG;font-weight:500;src:url(../fonts/SchibstedGrotesk-Medium.ttf)}"
    "@font-face{font-family:SG;font-weight:700;src:url(../fonts/SchibstedGrotesk-Bold.ttf)}@font-face{font-family:PM;src:url(../fonts/IBMPlexMono-Medium.ttf)}")
chips=[("Ink","ink","#F4F1EC"),("Paper","paper","#101114"),("White","white","#101114"),("Accent","accent","#101114"),("Accent tint","accent_tint","#101114"),("Accent deep","accent_deep","#FFFFFF"),("Grey","grey","#FFFFFF"),("Line","line","#101114")]
chip="".join(f'<div style="background:{C[k]};color:{t};height:200px;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;border:1px solid #DCD7CE"><b style="font-size:22px">{n}</b><span style="font:13px PM">{C[k]}</span></div>' for n,k,t in chips)
stack="".join(f'<div style="height:{h*3}px;margin-bottom:{4.5*3 if i<4 else 0}px;background:#FF5533;width:{360}px;margin-left:auto"></div>' for i,(y,h) in enumerate(BARS))
apps=["../applications/book-cover-front.png","../applications/social-1080x1350-accent.png","../applications/social-1080x1080-dark.png","../applications/ad-1080x1350-dark.png","../applications/plugins/plugin-03-proposal.png","../applications/plugins/tile-bundle-8.png"]
appimg="".join(f'<img src="{a}" style="height:380px;display:block">' for a in apps)
html=f"""<!doctype html><meta charset=utf-8><style>{ff}*{{margin:0;box-sizing:border-box}}body{{width:2400px;background:#F4F1EC;color:#101114;font-family:SG}}
.lab{{font:13px PM;letter-spacing:.12em;text-transform:uppercase}}.lab:before{{content:'';display:inline-block;width:12px;height:4px;background:#FF5533;margin-right:10px;vertical-align:middle}}
section{{padding:56px 64px;border-bottom:1px solid #101114}}h2{{font-size:40px;letter-spacing:-.02em;margin:10px 0 28px;font-weight:700}}</style><body>
<section style="display:flex;justify-content:space-between;align-items:flex-end;padding-top:72px"><div><div class=lab>Brand sheet / version 1.0 / 2026-11-05</div>
<div style="margin-top:40px">{img(horizontal(C['ink'],C['accent'],C['ink'],True,C['grey']),1000)}</div></div>
<p style="font-size:22px;line-height:1.5;max-width:720px">A brain seen from the front. The left half is solid: the expert's own judgement. The right half is five written lines: the knowledge written down and handed to AI. Stay human. Automate the rest.</p></section>
<section style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0;padding:0">
<div style="background:#101114;padding:56px 64px">{img(horizontal(C['paper'],C['accent'],C['paper']),560)}</div>
<div style="background:#FF5533;padding:56px 64px">{img(horizontal(C['ink'],C['ink'],C['ink']),560)}</div>
<div style="background:#fff;padding:56px 64px;display:flex;gap:48px;align-items:center">{img(mark_only(C['ink'],C['accent']),140)}{img(mark_only(C['ink'],C['accent']),48)}{img(mark_only(C['ink'],C['accent']),16)}</div></section>
<section><div class=lab>Colour</div><h2>Shared neutrals, own accent</h2><div style="display:grid;grid-template-columns:repeat(8,1fr);gap:12px">{chip}</div></section>
<section style="display:grid;grid-template-columns:1.3fr 1fr;gap:64px"><div><div class=lab>Type</div><h2>Schibsted Grotesk + IBM Plex Mono</h2>
<div style="font-size:120px;font-weight:700;letter-spacing:-.02em;line-height:1">Aa Expert DNA</div>
<p style="font-size:20px;line-height:1.55;margin-top:24px;max-width:1000px">AI without context works like a confused intern. You write down what lives in your head, and the AI works from those files instead of from the internet's average.</p>
<div style="font:15px PM;letter-spacing:.12em;margin-top:20px">PLUGIN 03 / PROPOSAL / 29 EUR</div></div>
<div><div class=lab>Motif</div><h2>The stripe stack</h2><div style="margin-right:-64px">{stack}</div>
<p style="font-size:18px;line-height:1.5;margin-top:24px;color:#66655F">The five lines of the mark. Once per layout, always bleeding off one edge. Plus thin full-width rules.</p></div></section>
<section><div class=lab>Applications</div><h2>Book, social, ads, plugins</h2><div style="display:flex;gap:16px">{appimg}</div></section>
</body>"""
open("brandsheet.html","w").write(html)
