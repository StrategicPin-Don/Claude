"""Expert DNA plugin identity: glyphs, 1080x1080 tiles, overview sheet (HTML; rendered by render.js)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
FONTS = os.path.join(ROOT, "fonts")
LOGO = os.path.join(ROOT, "logo", "svg")

INK, PAPER, ACC, LINE, LINE_D, GREY, GREY_D = "#101114", "#F4F1EC", "#FF5533", "#DCD7CE", "#34383F", "#66655F", "#A3A29C"
FOLDS = ["M4 15 C10 18 16 12 24 16", "M3 33 C10 29 16 36 24 31"]

PLUGINS = [
    ("01", "Lead", "Who Is Ready to Buy"),
    ("02", "Follow-Up", "Follow Up Without Chasing"),
    ("03", "Proposal", "The Proposal You Don't Have to Write"),
    ("04", "Session", "The Hour After the Session"),
    ("05", "Onboarding", "The Intake You Don't Have to Run"),
    ("06", "Content", "Story Library"),
    ("07", "CRM", "The CRM That Updates Itself"),
    ("08", "Ads", "Ads Without an Agency"),
]

GAP = 1.5
BAR_H = (48 - 7 * GAP) / 8

def plugin_glyph(active, size, line, acc=ACC, uid="g"):
    """Right hemisphere (r=24) cut into 8 bars. active: set of bar indexes 1..8 shown in accent."""
    w = size * 24 / 48
    bars = "".join(
        f'<rect x="0" y="{(i - 1) * (BAR_H + GAP):.3f}" width="24" height="{BAR_H:.3f}" fill="{acc if i in active else line}"/>'
        for i in range(1, 9))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 48" width="{w:.1f}" height="{size}">'
            f'<defs><clipPath id="{uid}"><path d="M0 0 A24 24 0 0 1 0 48 Z"/></clipPath></defs>'
            f'<g clip-path="url(#{uid})">{bars}</g></svg>')

def starter_glyph(size, acc=ACC, uid="s"):
    w = size * 24 / 48
    folds = "".join(f'<path d="{d}"/>' for d in FOLDS)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 48" width="{w:.1f}" height="{size}">'
            f'<defs><mask id="{uid}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="30" height="52">'
            f'<path d="M24 0 A24 24 0 0 0 24 48 Z" fill="#fff"/>'
            f'<g fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">{folds}</g></mask></defs>'
            f'<path d="M24 0 A24 24 0 0 0 24 48 Z" fill="{acc}" mask="url(#{uid})"/></svg>')

FONT_CSS = f"""
@font-face{{font-family:'Schibsted Grotesk';font-weight:400;src:url('file://{FONTS}/SchibstedGrotesk-Regular.ttf')}}
@font-face{{font-family:'Schibsted Grotesk';font-weight:500;src:url('file://{FONTS}/SchibstedGrotesk-Medium.ttf')}}
@font-face{{font-family:'Schibsted Grotesk';font-weight:700;src:url('file://{FONTS}/SchibstedGrotesk-Bold.ttf')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url('file://{FONTS}/IBMPlexMono-Medium.ttf')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:400;src:url('file://{FONTS}/IBMPlexMono-Regular.ttf')}}
"""

def tile_html(label, glyph, name, sub, badge, price, dark=False):
    bg, fg, sec, rule = (INK, PAPER, GREY_D, LINE_D) if dark else (PAPER, INK, GREY, LINE)
    logo = os.path.join(LOGO, "expertdna-horizontal-colour-on-dark.svg" if dark else "expertdna-horizontal-colour-on-light.svg")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1080px;background:{bg};color:{fg};font-family:'Schibsted Grotesk';position:relative;overflow:hidden}}
.top{{position:absolute;left:80px;right:80px;top:72px;display:flex;justify-content:space-between;align-items:center;
  font:500 24px 'IBM Plex Mono';letter-spacing:.12em}}
.top .sq{{display:inline-block;width:14px;height:14px;background:{ACC};margin-right:16px;vertical-align:middle;position:relative;top:-2px}}
.rule{{position:absolute;left:0;right:0;top:136px;height:1px;background:{rule}}}
.glyph{{position:absolute;left:80px;top:200px}}
.text{{position:absolute;left:80px;right:80px;bottom:236px}}
h1{{font-weight:700;font-size:104px;letter-spacing:-0.02em;line-height:1}}
h2{{font-weight:500;font-size:46px;letter-spacing:-0.01em;line-height:1.12;margin-top:24px;max-width:900px}}
.rule2{{position:absolute;left:0;right:0;top:880px;height:1px;background:{rule}}}
.bottom{{position:absolute;left:80px;right:80px;top:916px;display:flex;justify-content:space-between;align-items:flex-start}}
.badge{{font:500 22px 'IBM Plex Mono';letter-spacing:.06em;border:1.5px solid {fg};padding:10px 16px;text-transform:uppercase}}
.price{{text-align:right}} .price b{{font-weight:700;font-size:60px;letter-spacing:-0.01em;line-height:1}}
.price span{{display:block;font:400 16px 'IBM Plex Mono';color:{sec};letter-spacing:.1em;margin-top:8px}}
.logo{{position:absolute;right:80px;top:84px;height:0}}
</style></head><body>
<div class="top"><div><span class="sq"></span>{label}</div><img src="file://{logo}" style="height:40px"></div>
<div class="rule"></div>
<div class="glyph">{glyph}</div>
<div class="text"><h1>{name}</h1><h2>{sub}</h2></div>
<div class="rule2"></div>
<div class="bottom"><div class="badge">{badge}</div><div class="price"><b>{price}</b><span>WORKING PRICE, PLACEHOLDER</span></div></div>
</body></html>"""

def build():
    tiles = []
    for n, name, sub in PLUGINS:
        i = int(n)
        g = plugin_glyph({i}, 300, LINE_D if False else LINE, uid=f"p{n}")
        fn = f"plugin-{n}-{name.lower().replace('-', '')}"
        open(os.path.join(HERE, fn + ".html"), "w").write(tile_html(f"PLUGIN {n}", g, name, sub, "Plugin + mini course", "29 EUR"))
        tiles.append(fn)
    open(os.path.join(HERE, "tile-starter.html"), "w").write(
        tile_html("STARTER", starter_glyph(300, uid="st"), "Expert DNA Starter", "Order bump with the book", "Order bump", "29 EUR"))
    tiles.append("tile-starter")
    open(os.path.join(HERE, "tile-bundle-8.html"), "w").write(
        tile_html("BUNDLE / 8 PLUGINS", plugin_glyph(set(range(1, 9)), 300, LINE_D, uid="b8"), "All 8 plugins", "Lead, Follow-Up, Proposal, Session, Onboarding, Content, CRM, Ads", "8 plugins + 8 mini courses", "97 EUR", dark=True))
    tiles.append("tile-bundle-8")
    # glyph standalone SVGs (system reference)
    for n, name, _ in PLUGINS:
        open(os.path.join(HERE, f"glyph-plugin-{n}-light.svg"), "w").write(plugin_glyph({int(n)}, 96, LINE, uid="g"))
        open(os.path.join(HERE, f"glyph-plugin-{n}-dark.svg"), "w").write(plugin_glyph({int(n)}, 96, LINE_D, uid="g"))
    open(os.path.join(HERE, "glyph-bundle.svg"), "w").write(plugin_glyph(set(range(1, 9)), 96, LINE, uid="g"))
    open(os.path.join(HERE, "glyph-starter.svg"), "w").write(starter_glyph(96, uid="g"))
    # overview sheet (uses rendered PNGs)
    cells = "".join(f'<img src="{t}.png">' for t in tiles)
    glyph_row = "".join(
        f'<div class="g">{plugin_glyph({int(n)}, 120, LINE, uid=f"o{n}")}<span>{n} {name.upper()}</span></div>' for n, name, _ in PLUGINS)
    glyph_row += f'<div class="g">{starter_glyph(120, uid="ost")}<span>STARTER</span></div>'
    glyph_row += f'<div class="g">{plugin_glyph(set(range(1, 9)), 120, LINE, uid="ob")}<span>ALL 8</span></div>'
    open(os.path.join(HERE, "overview.html"), "w").write(f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}
*{{margin:0;box-sizing:border-box}} body{{width:2400px;background:{PAPER};color:{INK};font-family:'Schibsted Grotesk';padding:64px}}
.lab{{font:500 15px 'IBM Plex Mono';letter-spacing:.12em;color:#B32F15}}
h1{{font-size:56px;font-weight:700;letter-spacing:-0.02em;margin:12px 0 16px}}
p{{font-size:20px;line-height:1.5;max-width:1500px}}
.rule{{height:1px;background:{INK};margin:40px -64px}}
.glyphs{{display:flex;gap:56px;align-items:flex-end;flex-wrap:wrap}} .g{{display:flex;flex-direction:column;gap:14px;align-items:flex-start}}
.g span{{font:500 13px 'IBM Plex Mono';letter-spacing:.1em}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}} .grid img{{width:100%;display:block;outline:1px solid {LINE}}}
</style></head><body>
<div class="lab">EXPERT DNA / PLUGIN IDENTITY SYSTEM</div>
<h1>One hemisphere, eight lines, one lit line per plugin</h1>
<p>The right half of the mark stands for the work handed to AI. It is cut into 8 bars, one per plugin, counted from the top. A plugin lights its own bar in accent; the bundle lights all 8. The Starter is the left half: the expert's own files. Number, name and lit bar always appear together.</p>
<div class="rule"></div><div class="glyphs">{glyph_row}</div><div class="rule"></div>
<div class="grid">{cells}</div></body></html>""")
    return tiles

if __name__ == "__main__":
    print(" ".join(build()))
