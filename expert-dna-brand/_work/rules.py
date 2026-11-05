import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

R = ROOT
ff = (f"@font-face{{font-family:SG;font-weight:400;src:url(../fonts/SchibstedGrotesk-Regular.ttf)}}"
      f"@font-face{{font-family:SG;font-weight:700;src:url(../fonts/SchibstedGrotesk-Bold.ttf)}}"
      f"@font-face{{font-family:PM;src:url(../fonts/IBMPlexMono-Medium.ttf)}}")
base_css = (ff + "*{margin:0;box-sizing:border-box}body{width:2400px;background:#F4F1EC;color:#101114;font-family:SG}"
            ".lab{font:12px PM;letter-spacing:.12em;text-transform:uppercase}.lab:before{content:'';display:inline-block;width:12px;height:4px;background:#FF5533;margin-right:10px;vertical-align:middle}"
            "section{padding:48px 64px;border-bottom:1px solid #101114}h2{font-size:44px;letter-spacing:-.02em;margin:12px 0 28px}"
            ".grid{display:grid;gap:24px}.cap{font-size:17px;line-height:1.45;margin-top:12px;color:#66655F}")

L = horizontal(C["ink"], C["accent"], C["ink"])

# clear space diagram: lockup with u-grid boxes
def clear_space():
    s = L
    import re
    vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    w, h = vb[2], vb[3]
    cs = 2 * u
    inner = s[s.index("<title>"):s.rindex("</svg>")]
    W, Hh = w + 2 * cs, h + 2 * cs
    boxes = "".join(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#FFE1D8"/>' for x, y in
                    [(0, 0), (W - cs, 0), (0, Hh - cs), (W - cs, Hh - cs)])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W*1.6:.0f}">'
            f'<rect x="0" y="0" width="{W}" height="{Hh}" fill="none" stroke="#B32F15" stroke-width="1" stroke-dasharray="4 4"/>{boxes}'
            f'<rect x="{cs}" y="{cs}" width="{w}" height="{h}" fill="none" stroke="#66655F" stroke-width=".75"/>'
            f'<g transform="translate({cs},{cs})">{inner}</g>'
            f'<rect x="{cs + 4*u}" y="{cs - 0}" width="{u}" height="{H}" fill="#FF5533" opacity="0"/></svg>')

def img(svgs, w):
    return svgs.replace("<svg ", f'<svg style="width:{w}px;height:auto;display:block" ', 1)

mark = mark_only(C["ink"], C["accent"])
# construction diagram of the mark
def construction():
    s = 8
    g = "".join(f'<line x1="{x}" y1="-6" x2="{x}" y2="54" stroke="#DCD7CE" stroke-width=".25"/>' for x in range(0, 55, 6))
    g += "".join(f'<line x1="-6" y1="{y}" x2="60" y2="{y}" stroke="#DCD7CE" stroke-width=".25"/>' for y in range(0, 49, 6))
    g += '<circle cx="24" cy="24" r="24" fill="none" stroke="#B32F15" stroke-width=".4" stroke-dasharray="1.5 1"/>'
    g += '<circle cx="30" cy="24" r="24" fill="none" stroke="#B32F15" stroke-width=".4" stroke-dasharray="1.5 1"/>'
    g += f'<g opacity=".9">{mark_inner(C["ink"], C["accent"])}</g>'
    g += '<rect x="24" y="-5" width="6" height="2" fill="#B32F15"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-8 -8 70 64" width="560">{g}</svg>'

def misuse():
    m = mark_inner
    items = [
        ("Do not stretch or squash", f'<g transform="translate(-10,10) scale(1.5,0.7)">{m(C["ink"], C["accent"])}</g>'),
        ("Do not rotate", f'<g transform="rotate(-18 27 24)">{m(C["ink"], C["accent"])}</g>'),
        ("Do not swap the halves", f'<g transform="translate(54,0) scale(-1,1)">{m(C["ink"], C["accent"])}</g>'),
        ("Do not use other colours", m("#2B59C3", "#7A3FC4")),
        ("No gradients", '<defs><linearGradient id="gx" x1="0" x2="1"><stop offset="0" stop-color="#FF5533"/><stop offset="1" stop-color="#7A3FC4"/></linearGradient></defs>' + m(C["ink"], "url(#gx)")),
        ("No shadows or glow", '<defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="2" dy="3" stdDeviation="2" flood-opacity=".5"/></filter></defs>' + f'<g filter="url(#sh)">{m(C["ink"], C["accent"])}</g>'),
        ("Do not add or remove lines", m(C["ink"], C["accent"]).replace('<rect x="30" y="42"', '<rect x="30" y="38" width="24" height="3"/><rect x="30" y="42"')),
        ("No low-contrast placement", m(C["paper"], C["accent_tint"])),
    ]
    cells = ""
    for t, g in items:
        bg = C["accent_tint"] if t.startswith("No low") else C["white"]
        cells += (f'<div style="background:{bg};padding:24px;border:1px solid #DCD7CE">'
                  f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -6 74 60" width="100%">{g}'
                  f'<line x1="-8" y1="52" x2="62" y2="-4" stroke="#B32F15" stroke-width="1.2"/></svg>'
                  f'<div class="lab" style="margin-top:14px">{t}</div></div>')
    return cells

def minsize():
    hz = horizontal(C["ink"], C["accent"], C["ink"]); st = stacked(C["ink"], C["accent"], C["ink"])
    return (f'<div style="display:flex;gap:56px;align-items:flex-end">'
            f'<div>{img(mark,16)}<div class="lab" style="margin-top:12px">Mark: 16 px / 5 mm</div></div>'
            f'<div>{img(hz,120)}<div class="lab" style="margin-top:12px">Horizontal: 120 px / 30 mm</div></div>'
            f'<div>{img(st,72)}<div class="lab" style="margin-top:12px">Stacked: 72 px / 20 mm</div></div>'
            f'<div>{img(horizontal(C["ink"], C["accent"], C["ink"], True, C["grey"]),220)}<div class="lab" style="margin-top:12px">With tagline: 220 px / 55 mm</div></div></div>')

html = f"""<!doctype html><meta charset=utf-8><style>{base_css}</style><body>
<section><div class="lab">Expert DNA / Logo rules</div><h2>Construction</h2>
<div style="display:flex;gap:80px;align-items:center">{construction()}
<p class="cap" style="max-width:900px;font-size:20px;color:#101114">Two half circles with radius 4u, separated by a gap of 1u. The mark is 9u wide and 8u high. The left half carries two folds cut 0.5u wide. The right half is five written lines, each 1u high with 0.75u between them. u is the unit for every rule below.</p></div></section>
<section><div class="lab">Clear space</div><h2>Keep 2u clear on every side</h2>{img(clear_space(), 1100)}
<p class="cap">2u equals one quarter of the mark height. Nothing enters the dashed area: no text, no edge of the page, no other logo.</p></section>
<section><div class="lab">Minimum sizes</div><h2>Smaller than this, it stops reading</h2>{minsize()}</section>
<section><div class="lab">Misuse</div><h2>Eight things never to do</h2><div class="grid" style="grid-template-columns:repeat(8,minmax(0,1fr))">{misuse()}</div></section>
</body>"""
open(os.path.join(R, "_work", "rules.html"), "w").write(html)

# accent comparison
def acc_block(acc, name, note):
    hz = horizontal(C["ink"], acc, C["ink"]); dk = horizontal(C["paper"], acc, C["paper"])
    return (f'<div style="flex:1;border-right:1px solid #101114">'
            f'<div style="padding:40px"><div class="lab">{name}</div><p class="cap" style="color:#101114;font-size:20px">{note}</p></div>'
            f'<div style="padding:40px;background:#F4F1EC">{img(hz,520)}</div><div style="padding:40px;background:#101114">{img(dk,520)}</div>'
            f'<div style="padding:40px;background:{acc};height:260px"><div style="font:700 56px SG;letter-spacing:-.02em;color:#101114;max-width:900px">Stay human. Automate the rest.</div></div></div>')
acc_html = f"""<!doctype html><meta charset=utf-8><style>{base_css}</style><body><div style="display:flex">
{acc_block("#FF7520", "Option A: StrategicPin orange #FF7520", "Same orange as StrategicPin. Reads as the same company. Expert AG, an existing retail brand using the word Expert, also pairs black type with an orange accent.")}
{acc_block(C["accent"], "Option B, recommended: Signal red-orange #FF5533", "Shifted 10 degrees toward red. Keeps the energy and the family warmth, but is clearly its own colour next to StrategicPin. Ink text on it: 5.93 to 1, passes AA.")}
</div></body>"""
open(os.path.join(R, "_work", "accent.html"), "w").write(acc_html)
print("ok")
