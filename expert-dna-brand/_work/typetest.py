fams=["SchibstedGrotesk","HankenGrotesk","FamiljenGrotesk","Onest","Geist"]
monos=["GeistMono","IBMPlexMono","JetBrainsMono"]
ff="".join(f"@font-face{{font-family:{f};font-weight:{w};src:url(fonts/{f}-{w}.ttf)}}" for f in fams for w in (400,500,700))
ff+="".join(f"@font-face{{font-family:{m};font-weight:500;src:url(fonts/{m}-500.ttf)}}" for m in monos)
body="AI without context works like a confused intern. You write down what lives in your head: your offers and prices, your ideal client, your method, your voice. The AI works from those files instead of from the internet's average."
rows=""
for i,f in enumerate(fams):
    rows+=f'''<section style="font-family:{f}"><div class="lab">0{i+1} {f.upper()}</div>
<div class="wm">Expert DNA</div>
<div class="h">Stay human. Automate the rest.</div>
<p>{body}</p>
<div class="num">29 EUR&nbsp;&nbsp;297 EUR&nbsp;&nbsp;1,490&nbsp;&nbsp;0123456789</div>
<div class="ui">PLUGIN 03 · PROPOSAL&nbsp;&nbsp;&nbsp;Add to order&nbsp;&nbsp;&nbsp;The Proposal You Don't Have to Write</div></section>'''
mrow="".join(f'<div style="font-family:{m};font-size:12px;letter-spacing:.12em;margin:10px 0">{m.upper()}: PLUGIN 03 / 29 EUR / 297 EUR / 1,490 / CHAPTER 02</div>' for m in monos)
html=f'''<!doctype html><meta charset=utf-8><style>{ff}*{{margin:0;box-sizing:border-box}}body{{width:2400px;background:#F4F1EC;color:#101114;padding:48px 64px}}
section{{display:grid;grid-template-columns:900px 1fr;gap:12px 48px;padding:32px 0;border-bottom:1px solid #101114}}
.lab{{font:500 12px JetBrainsMono;letter-spacing:.12em;grid-column:1/3;color:#D9560D}}
.wm{{font-size:110px;font-weight:700;letter-spacing:-0.02em;line-height:1}} .h{{font-size:54px;font-weight:700;letter-spacing:-0.015em;line-height:1.05;align-self:center}}
p{{font-size:19px;line-height:1.5;font-weight:400;max-width:860px}} .num{{font-size:44px;font-weight:500;font-variant-numeric:tabular-nums}}
.ui{{font-size:12px;font-weight:500;grid-column:1/3}}</style><body>{rows}<section><div class=lab>MONO CANDIDATES (LABELS ONLY)</div><div>{mrow}</div></section></body>'''
open("typetest.html","w").write(html)
