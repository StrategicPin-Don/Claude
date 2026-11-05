"""Expert DNA v2 applications: writes HTML sources + render job list. Run render.js after."""
import os, sys, json, re, base64

ROOT = "/home/user/Claude/expert-dna-brand"
sys.path.insert(0, os.path.join(ROOT, "_work"))
from brand3 import C, mark_inner, MW, MH

APP = os.path.join(ROOT, "applications")
SRC = os.path.join(APP, "src")
LOGO = os.path.join(ROOT, "logo", "svg")
FONTS = os.path.join(ROOT, "fonts")
jobs = []

def logo(name, width, extra=""):
    s = open(os.path.join(LOGO, f"expertdna-{name}.svg")).read()
    s = re.sub(r'<title>.*?</title>', '', s)
    return re.sub(r'<svg ([^>]*?)width="[^"]+" height="[^"]+"', lambda m: f'<svg {m.group(1)}style="width:{width}px;height:auto;display:block{extra}"', s, count=1)

def mark(b, p, width, extra=""):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {MW} {MH}" style="width:{width}px;height:auto;display:block{extra}">{mark_inner(b, p)}</svg>'

def font_css(rel):
    return (f"@font-face{{font-family:HG;font-weight:400;src:url({rel}/HankenGrotesk-Regular.ttf)}}"
            f"@font-face{{font-family:HG;font-weight:500;src:url({rel}/HankenGrotesk-Medium.ttf)}}"
            f"@font-face{{font-family:HG;font-weight:700;src:url({rel}/HankenGrotesk-Bold.ttf)}}"
            f"@font-face{{font-family:PM;font-weight:500;src:url({rel}/IBMPlexMono-Medium.ttf)}}"
            f"@font-face{{font-family:PM;font-weight:400;src:url({rel}/IBMPlexMono-Regular.ttf)}}")

BASE = ("*{margin:0;padding:0;box-sizing:border-box}html,body{overflow:hidden}"
        ".lab{font:500 15px PM;letter-spacing:.12em;text-transform:uppercase;display:flex;align-items:center;gap:12px}"
        ".lab i{display:inline-block;width:16px;height:5px;background:currentColor}"
        ".h{font-family:HG;font-weight:500;letter-spacing:-.03em;line-height:1.04}")

def page(name, w, h, body, css="", bg="#fff", scale=1, measure=True, rel="../../fonts", extra_scales=()):
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{font_css(rel)}{BASE}'
            f'body{{width:{w}px;height:{h}px;background:{bg};position:relative;font-family:HG}}{css}</style></head><body>{body}</body></html>')
    p = os.path.join(SRC, f"{name}.html"); open(p, "w").write(html)
    jobs.append(dict(html=p, out=os.path.join(APP, f"{name}.png"), w=w, h=h, scale=scale, measure=measure))
    for s in extra_scales:
        jobs.append(dict(html=p, out=os.path.join(APP, f"{name}@{s}x.png"), w=w, h=h, scale=s, measure=False))

def prongs(x, y, h_bar, col, side="right", bar=False):
    """Prongs: two bars 16:11, thickness h_bar. Anchored at x (left start), bleeding right."""
    L1 = h_bar * 16 / 3.5; L2 = h_bar * 11 / 3.5; gap = h_bar * (30.5 - 14) / 3.5
    s = ""
    if bar:
        s += f'<div style="position:absolute;left:{x - h_bar*8/3.5:.0f}px;top:{y - h_bar*14/3.5:.0f}px;width:{h_bar:.0f}px;height:{h_bar*48/3.5:.0f}px;background:{col}"></div>'
    if bar:  # finite plug, exactly like the mark
        s += f'<div style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{L1:.0f}px;height:{h_bar:.0f}px;background:{col}"></div>'
        s += f'<div style="position:absolute;left:{x:.0f}px;top:{y + gap:.0f}px;width:{L2:.0f}px;height:{h_bar:.0f}px;background:{col}"></div>'
        return s
    s += f'<div style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;right:0;height:{h_bar:.0f}px;background:{col}"></div>'
    s += f'<div style="position:absolute;left:{x + (L1 - L2) * 3:.0f}px;top:{y + gap:.0f}px;right:0;height:{h_bar:.0f}px;background:{col}"></div>'
    return s

def halfmoon(cx, cy, r, col, side="left"):
    # half disc with flat side on the right (like the mark), positioned absolutely
    return (f'<svg style="position:absolute;left:{cx - r:.0f}px;top:{cy - r:.0f}px;width:{r:.0f}px;height:{2*r:.0f}px" viewBox="0 0 24 48">'
            f'<path d="M24 0 A24 24 0 0 0 24 48 Z" fill="{col}"/></svg>')

# ---------------- social ----------------
HEAD = "Your AI works like a confused intern."
SUB = "Give it your Expert DNA."

def social_dark():
    b = (f'<div class="lab" style="position:absolute;left:80px;top:80px;color:{C["grey_dark"]}"><i style="background:{C["accent"]}"></i>Expert DNA / 01</div>'
         f'<div class="h t" style="position:absolute;left:80px;top:170px;width:820px;font-size:88px;color:#fff">{HEAD}</div>'
         f'<div class="t" style="position:absolute;left:80px;top:575px;font:400 36px HG;color:{C["grey_dark"]};letter-spacing:-.01em">{SUB}</div>'
         + prongs(680, 690, 34, C["accent"])
         + f'<div style="position:absolute;left:0;right:0;top:930px;height:1px;background:{C["line_dark"]}"></div>'
         f'<div style="position:absolute;left:80px;top:968px">{logo("horizontal-colour-on-dark", 250)}</div>')
    page("social-1080x1080-dark", 1080, 1080, b, bg=C["ink"])

def social_accent():
    b = (f'<div class="lab" style="position:absolute;left:80px;top:80px;color:{C["ink"]}"><i></i>Expert DNA / 01</div>'
         f'<div class="h t" style="position:absolute;left:80px;top:170px;width:860px;font-size:112px;color:{C["ink"]}">{HEAD}</div>'
         + halfmoon(1080, 1000, 330, C["ink"])
         + f'<div class="t" style="position:absolute;left:80px;top:1150px;font:400 34px HG;color:{C["ink"]};letter-spacing:-.01em">{SUB}</div>'
         f'<div style="position:absolute;left:0;right:0;top:1220px;height:1px;background:{C["ink"]};opacity:.35"></div>'
         f'<div style="position:absolute;left:80px;top:1252px">{logo("horizontal-black", 230)}</div>')
    page("social-1080x1350-accent", 1080, 1350, b, bg=C["accent"])

def social_light():
    b = (f'<div class="lab" style="position:absolute;left:80px;top:80px;color:{C["accent_deep"]}"><i style="background:{C["accent"]}"></i>Expert DNA / 01</div>'
         f'<div class="h t" style="position:absolute;left:80px;top:170px;width:820px;font-size:88px;color:{C["ink"]}">{HEAD}</div>'
         f'<div class="t" style="position:absolute;left:80px;top:575px;font:400 36px HG;color:{C["grey"]};letter-spacing:-.01em">{SUB}</div>'
         + halfmoon(1080, 760, 150, C["ink"])
         + f'<div style="position:absolute;left:0;right:0;top:930px;height:1px;background:{C["line"]}"></div>'
         f'<div style="position:absolute;left:80px;top:968px">{logo("horizontal-colour-on-light", 250)}</div>')
    page("social-1080x1080-light", 1080, 1080, b, bg="#fff")

# ---------------- ads ----------------
AD_H = "Stay human. Automate the rest."
AD_B = "Write down what lives in your head. Let AI work from it, not from the internet's average."

def ad(kind):
    dark = kind == "dark"
    fg = "#fff" if dark else C["ink"]; sub = C["grey_dark"] if dark else C["ink"]
    btn_bg = C["accent"] if dark else C["ink"]; btn_fg = C["ink"] if dark else "#fff"
    lab_col = C["grey_dark"] if dark else C["ink"]; bar = C["accent"] if dark else C["ink"]
    motif = (prongs(640, 760, 40, C["accent"], bar=False) if dark else halfmoon(1080, 760, 260, C["ink"]))
    b = (f'<div class="lab" style="position:absolute;left:80px;top:80px;color:{lab_col}"><i style="background:{bar}"></i>The book</div>'
         f'<div class="h t" style="position:absolute;left:80px;top:170px;width:880px;font-size:112px;color:{fg}">{AD_H}</div>'
         f'<div class="t" style="position:absolute;left:80px;top:440px;width:640px;font:400 32px/1.4 HG;color:{sub}">{AD_B}</div>'
         + motif +
         f'<div class="t" style="position:absolute;left:80px;top:1080px;background:{btn_bg};color:{btn_fg};font:500 32px HG;padding:26px 40px">Get the book, 7 EUR</div>'
         f'<div class="t" style="position:absolute;left:520px;top:1104px;font:500 18px PM;letter-spacing:.1em;color:{sub}">EXPERTDNA.NET</div>'
         f'<div style="position:absolute;left:0;right:0;top:1210px;height:1px;background:{C["line_dark"] if dark else C["ink"]};{"" if dark else "opacity:.35"}"></div>'
         f'<div style="position:absolute;left:80px;top:1244px">{logo("horizontal-colour-on-dark" if dark else "horizontal-black", 230)}</div>')
    page(f"ad-1080x1350-{kind}", 1080, 1350, b, bg=C["ink"] if dark else C["accent"])

# ---------------- email ----------------
def email():
    hb = (f'<div style="position:absolute;left:40px;top:44px">{logo("horizontal-colour-on-light", 170)}</div>'
          + prongs(470, 50, 8, C["accent"]) +
          f'<div style="position:absolute;left:0;right:0;bottom:0;height:1px;background:{C["line"]}"></div>')
    page("email-header-600", 600, 140, hb, bg="#fff", measure=False, extra_scales=(2,))
    fb = (f'<div style="position:absolute;left:0;right:0;top:0;height:1px;background:{C["line"]}"></div>'
          f'<div style="position:absolute;left:40px;top:36px">{logo("horizontal-tagline-colour-on-light", 190)}</div>'
          f'<div style="position:absolute;left:40px;top:122px;width:520px;border:1px dashed {C["grey"]};padding:12px 14px">'
          f'<div style="font:500 10px PM;letter-spacing:.12em;color:{C["accent_deep"]}">POSTAL ADDRESS PLACEHOLDER</div>'
          f'<div style="font:400 13px HG;color:{C["grey"]};margin-top:4px">{{Company name}}, {{Street}}, {{City}}, {{Country}}</div></div>'
          f'<div style="position:absolute;left:40px;top:200px;font:400 13px HG;color:{C["grey"]}">You get this email because you asked for it. '
          f'<span style="color:{C["ink"]};border-bottom:2px solid {C["accent"]}">Unsubscribe</span></div>')
    page("email-footer-600", 600, 240, fb, bg=C["paper"], measure=False, extra_scales=(2,))

# ---------------- link preview ----------------
def link_preview():
    b = (f'<div class="lab" style="position:absolute;left:72px;top:64px;color:{C["grey_dark"]}"><i style="background:{C["accent"]}"></i>expertdna.net</div>'
         f'<div class="h" style="position:absolute;left:72px;top:130px;width:700px;font-size:76px;color:#fff">Stay human. Automate the rest.</div>'
         + prongs(900, 230, 26, C["accent"], bar=True) +
         f'<div style="position:absolute;left:0;right:0;top:500px;height:1px;background:{C["line_dark"]}"></div>'
         f'<div style="position:absolute;left:72px;top:534px">{logo("horizontal-colour-on-dark", 230)}</div>')
    page("link-preview-1200x630", 1200, 630, b, bg=C["ink"], measure=False)

# ---------------- plugins ----------------
PLUGINS = [("01", "Lead", "Who Is Ready to Buy"), ("02", "Follow-Up", "Follow Up Without Chasing"),
           ("03", "Proposal", "The Proposal You Don't Have to Write"), ("04", "Session", "The Hour After the Session"),
           ("05", "Onboarding", "The Intake You Don't Have to Run"), ("06", "Content", "Story Library"),
           ("07", "CRM", "The CRM That Updates Itself"), ("08", "Ads", "Ads Without an Agency")]

def plug_glyph(lit, dark=False, width=200):
    """Vertical bar + 8 prong slots. lit: set of 1-based indexes in accent."""
    off = C["line_dark"] if dark else C["line"]; barc = "#fff" if dark else C["ink"]
    pitch = 48 / 8; h = 3.0
    s = f'<rect x="0" y="0" width="3.5" height="48" fill="{barc}"/>'
    for i in range(8):
        L = 16 if i % 2 == 0 else 11
        y = i * pitch + (pitch - h) / 2
        s += f'<rect x="8" y="{y:.2f}" width="{L}" height="{h}" fill="{C["accent"] if (i + 1) in lit else off}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 48" style="width:{width}px;height:auto;display:block">{s}</svg>'

def starter_glyph(width=200):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 48" style="width:{width}px;height:auto;display:block"><path d="M24 0 A24 24 0 0 0 24 48 Z" fill="{C["accent"]}"/></svg>'

def tile(name, label, glyph, title, sub, badge, price, dark=False):
    fg = "#fff" if dark else C["ink"]; sc = C["grey_dark"] if dark else C["grey"]; ln = C["line_dark"] if dark else C["line"]
    labc = C["grey_dark"] if dark else C["accent_deep"]
    lg = logo("horizontal-colour-on-dark" if dark else "horizontal-colour-on-light", 190)
    b = (f'<div class="lab" style="position:absolute;left:80px;top:84px;color:{labc}"><i style="background:{C["accent"]}"></i>{label}</div>'
         f'<div style="position:absolute;right:80px;top:76px">{lg}</div>'
         f'<div style="position:absolute;left:0;right:0;top:150px;height:1px;background:{ln}"></div>'
         f'<div style="position:absolute;left:80px;top:210px">{glyph}</div>'
         f'<div style="position:absolute;left:80px;right:80px;bottom:260px">'
         f'<div class="h" style="font-size:96px;color:{fg}">{title}</div>'
         f'<div style="font:400 34px/1.3 HG;color:{sc};margin-top:16px;letter-spacing:-.01em">{sub}</div></div>'
         f'<div style="position:absolute;left:0;right:0;bottom:190px;height:1px;background:{ln}"></div>'
         f'<div style="position:absolute;left:80px;bottom:84px;border:1.5px solid {fg};color:{fg};font:500 14px PM;letter-spacing:.12em;padding:10px 14px">{badge}</div>'
         f'<div style="position:absolute;right:80px;bottom:80px;text-align:right"><div style="font:500 52px/1 HG;letter-spacing:-.03em;color:{fg}">{price}</div>'
         f'<div style="font:400 12px PM;letter-spacing:.1em;color:{sc};margin-top:6px">WORKING PRICE, PLACEHOLDER</div></div>')
    page(f"plugins/{name}", 1080, 1080, b, bg=C["ink"] if dark else "#fff", measure=False, rel="../../../fonts")

def plugins():
    os.makedirs(os.path.join(SRC, "plugins"), exist_ok=True); os.makedirs(os.path.join(APP, "plugins"), exist_ok=True)
    for n, nm, sub in PLUGINS:
        tile(f"plugin-{n}-{nm.lower()}", f"Plugin {n}", plug_glyph({int(n)}, width=150), nm, sub, "PLUGIN + MINI COURSE", "29 EUR")
    tile("tile-starter", "Starter", starter_glyph(150), "Starter", "Order bump with the book", "ORDER BUMP", "29 EUR")
    tile("tile-bundle-8", "Bundle / 8 plugins", plug_glyph(set(range(1, 9)), dark=True, width=150), "All 8 plugins",
         "Lead, Follow-Up, Proposal, Session, Onboarding, Content, CRM, Ads", "8 PLUGINS + 8 MINI COURSES", "97 EUR", dark=True)
    # overview
    legend = "".join(f'<div style="display:flex;flex-direction:column;gap:14px;align-items:flex-start">{plug_glyph({int(n)}, width=46)}'
                     f'<div style="font:500 12px PM;letter-spacing:.1em">{n} {nm.upper()}</div></div>' for n, nm, _ in PLUGINS)
    legend += (f'<div style="display:flex;flex-direction:column;gap:14px">{starter_glyph(46)}<div style="font:500 12px PM;letter-spacing:.1em">STARTER</div></div>'
               f'<div style="display:flex;flex-direction:column;gap:14px">{plug_glyph(set(range(1, 9)), width=46)}<div style="font:500 12px PM;letter-spacing:.1em">ALL 8</div></div>')
    names = [f"plugin-{n}-{nm.lower()}" for n, nm, _ in PLUGINS] + ["tile-starter", "tile-bundle-8"]
    tiles = "".join(f'<img src="../../plugins/{t}.png" style="width:100%;display:block;border:1px solid {C["line"]}">' for t in names)
    b = (f'<div style="padding:64px 64px 40px;border-bottom:1px solid {C["ink"]}"><div class="lab" style="color:{C["accent_deep"]}"><i style="background:{C["accent"]}"></i>Expert DNA / plugin identity system</div>'
         f'<div class="h" style="font-size:56px;margin-top:16px">One plug, eight prongs, one lit prong per plugin</div>'
         f'<p style="font:400 20px/1.5 HG;color:{C["grey"]};margin-top:16px;max-width:1400px">The plug from the mark carries 8 prongs, one per plugin, counted from the top. A plugin lights its own prong in accent; the bundle lights all 8. The Starter is the half moon: the expert\'s own files, written first. Number, name and lit prong always appear together.</p></div>'
         f'<div style="display:flex;gap:56px;padding:48px 64px;border-bottom:1px solid {C["line"]}">{legend}</div>'
         f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:24px;padding:48px 64px 64px">{tiles}</div>')
    page("plugins/plugins-overview", 2400, 1500, b, bg="#fff", measure=False, rel="../../../fonts")
    jobs[-1]["full"] = True

# ---------------- logo rules ----------------
def logo_rules():
    u = 6
    grid = "".join(f'<line x1="{x}" y1="-6" x2="{x}" y2="54" stroke="{C["line"]}" stroke-width=".2"/>' for x in range(0, 55, u))
    grid += "".join(f'<line x1="-6" y1="{y}" x2="60" y2="{y}" stroke="{C["line"]}" stroke-width=".2"/>' for y in range(0, 49, u))
    cons = (f'<svg viewBox="-8 -10 72 66" style="width:620px;display:block">{grid}'
            f'<circle cx="24" cy="24" r="24" fill="none" stroke="{C["accent_deep"]}" stroke-width=".35" stroke-dasharray="1.5 1"/>'
            f'<g opacity=".92">{mark_inner(C["ink"], C["accent"])}</g>'
            f'<g font-family="PM" font-size="2.2" fill="{C["accent_deep"]}">'
            f'<text x="30" y="-3">3.5</text><text x="38" y="12.5">16</text><text x="38" y="38.5">11</text><text x="8" y="53">r = 4u</text><text x="24.6" y="53">1u</text></g>'
            f'<line x1="24" y1="50" x2="30" y2="50" stroke="{C["accent_deep"]}" stroke-width=".4"/></svg>')
    # clear space
    lock = logo("horizontal-colour-on-light", 900)
    H = 900 / (1.0) ; # width-based; compute u from mark height ratio
    s = open(os.path.join(LOGO, "expertdna-horizontal-colour-on-light.svg")).read()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    scale = 900 / vb[2]; mark_h = 96 * scale; uu = mark_h / 8; cs = 2 * uu
    clear = (f'<div style="position:relative;width:{900 + 2*cs:.0f}px;height:{vb[3]*scale + 2*cs:.0f}px;border:1px dashed {C["accent_deep"]}">'
             + "".join(f'<div style="position:absolute;{a}:0;{b_}:0;width:{cs:.0f}px;height:{cs:.0f}px;background:{C["accent_tint"]}"></div>' for a in ("left", "right") for b_ in ("top", "bottom"))
             + f'<div style="position:absolute;left:{cs:.0f}px;top:{cs:.0f}px;outline:1px solid {C["line"]}">{lock}</div></div>')
    minis = (f'<div style="display:flex;gap:72px;align-items:flex-end">'
             f'<div>{mark(C["ink"], C["accent"], 16)}<div class="lab" style="margin-top:14px;font-size:12px">Mark: 16 px / 5 mm</div></div>'
             f'<div>{logo("horizontal-colour-on-light", 120)}<div class="lab" style="margin-top:14px;font-size:12px">Horizontal: 120 px / 30 mm</div></div>'
             f'<div>{logo("stacked-colour-on-light", 72)}<div class="lab" style="margin-top:14px;font-size:12px">Stacked: 72 px / 20 mm</div></div>'
             f'<div>{logo("horizontal-tagline-colour-on-light", 220)}<div class="lab" style="margin-top:14px;font-size:12px">With tagline: 220 px / 55 mm</div></div></div>')
    m = lambda b, p: mark_inner(b, p)
    swapped = (f'<path d="M30 0 A24 24 0 0 1 30 48 Z" fill="{C["ink"]}"/><rect x="20.5" y="0" width="3.5" height="48" fill="{C["accent"]}"/>'
               f'<rect x="0" y="14" width="16" height="3.5" fill="{C["accent"]}"/><rect x="5" y="30.5" width="11" height="3.5" fill="{C["accent"]}"/>')
    prong_bad = m(C["ink"], C["accent"]).replace('width="11"', 'width="16"').replace('width="16" height="3.5" fill="' + C["accent"] + '"/><rect x="38" y="30.5"', 'width="8" height="3.5" fill="' + C["accent"] + '"/><rect x="38" y="30.5"')
    items = [
        ("Do not stretch or squash", f'<g transform="translate(-8,10) scale(1.4,0.6)">{m(C["ink"], C["accent"])}</g>', "#fff"),
        ("Do not rotate", f'<g transform="rotate(-20 27 24)">{m(C["ink"], C["accent"])}</g>', "#fff"),
        ("Do not swap half moon and plug", swapped, "#fff"),
        ("Do not use other colours", m("#2B59C3", "#2FB37A"), "#fff"),
        ("No gradients", '<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#FF5533"/><stop offset="1" stop-color="#7A3FC4"/></linearGradient></defs>' + m("url(#g)", "url(#g)"), "#fff"),
        ("No shadows or glow", f'<defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="2" dy="3" stdDeviation="2" flood-opacity=".5"/></filter></defs><g filter="url(#sh)">{m(C["ink"], C["accent"])}</g>', "#fff"),
        ("Do not change the prongs", prong_bad, "#fff"),
        ("No low-contrast placement", m(C["white"], C["accent_tint"]), C["accent_tint"]),
    ]
    cells = "".join(f'<div style="background:{bg};border:1px solid {C["line"]};padding:24px">'
                    f'<svg viewBox="-10 -8 74 64" style="width:100%;display:block">{g}<line x1="-8" y1="54" x2="62" y2="-6" stroke="{C["accent_deep"]}" stroke-width="1.2"/></svg>'
                    f'<div class="lab" style="margin-top:16px;font-size:12px;color:{C["ink"]}">{t}</div></div>' for t, g, bg in items)
    sec = lambda lab, h, body: (f'<section style="padding:56px 64px;border-bottom:1px solid {C["ink"]}"><div class="lab" style="color:{C["accent_deep"]}"><i style="background:{C["accent"]}"></i>{lab}</div>'
                                f'<div class="h" style="font-size:48px;margin:14px 0 36px">{h}</div>{body}</section>')
    body = (sec("Expert DNA / logo rules / construction", "Half moon and plug on a grid of u",
                f'<div style="display:flex;gap:96px;align-items:center">{cons}<p style="font:400 22px/1.55 HG;max-width:880px">The mark sits in a box 9u wide and 8u high (u = 6 units). The half moon is a half circle with radius 4u: the expert\'s mind. One unit of air separates it from the plug. The plug bar is 3.5 units wide and runs the full height. The two prongs are 16 and 11 units long, 3.5 units thick, starting 14 and 30.5 units from the top. Never redraw the mark: always use the supplied files.</p></div>')
            + sec("Clear space", "Keep 2u clear on every side", clear + f'<p style="font:400 18px HG;color:{C["grey"]};margin-top:18px">2u is one quarter of the mark height. Nothing enters the shaded area: no text, no page edge, no other logo.</p>')
            + sec("Minimum sizes", "Smaller than this, it stops reading", minis)
            + sec("Misuse", "Eight things never to do", f'<div style="display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:20px">{cells}</div>'))
    p = os.path.join(SRC, "logo-rules.html")
    open(p, "w").write(f'<!doctype html><meta charset=utf-8><style>{font_css("../../fonts")}{BASE}html,body{{overflow:visible}}body{{width:2400px;background:#fff;font-family:HG;color:{C["ink"]}}}</style><body>{body}</body>')
    jobs.append(dict(html=p, out=os.path.join(ROOT, "logo", "logo-rules.png"), w=2400, h=1200, scale=1, measure=False, full=True))

# ---------------- landing ----------------
def b64(f): return base64.b64encode(open(os.path.join(FONTS, f), "rb").read()).decode()

def landing():
    os.makedirs(os.path.join(APP, "landing"), exist_ok=True)
    ff = (f"@font-face{{font-family:'Hanken Grotesk';font-weight:400;src:url(data:font/ttf;base64,{b64('HankenGrotesk-Regular.ttf')}) format('truetype')}}"
          f"@font-face{{font-family:'Hanken Grotesk';font-weight:500;src:url(data:font/ttf;base64,{b64('HankenGrotesk-Medium.ttf')}) format('truetype')}}"
          f"@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/ttf;base64,{b64('IBMPlexMono-Medium.ttf')}) format('truetype')}}")
    lg = re.sub(r'<title>.*?</title>', '', open(os.path.join(LOGO, "expertdna-horizontal-colour-on-light.svg")).read())
    lg = re.sub(r'width="[^"]+" height="[^"]+"', 'class="logo" role="img" aria-label="Expert DNA"', lg, count=1)
    css = f"""{ff}
:root{{--ink:{C['ink']};--white:#fff;--paper:{C['paper']};--accent:{C['accent']};--deep:{C['accent_deep']};--grey:{C['grey']};--line:{C['line']}}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--white);color:var(--ink);font-family:'Hanken Grotesk',Arial,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
.wrap{{max-width:1344px;margin:0 auto;padding:0 48px}}
header{{border-bottom:1px solid var(--ink)}} header .wrap{{display:flex;justify-content:space-between;align-items:center;height:88px}}
.logo{{width:190px;height:auto;display:block}}
.mono{{font-family:'IBM Plex Mono','Courier New',monospace;font-weight:500;letter-spacing:.12em;text-transform:uppercase;font-size:12px}}
.lab{{display:flex;align-items:center;gap:10px;color:var(--deep)}} .lab i{{width:14px;height:4px;background:var(--accent);display:inline-block}}
.hero{{display:grid;grid-template-columns:7fr 5fr;gap:48px;padding:96px 0 0;position:relative}}
h1{{font-weight:500;font-size:64px;line-height:1.02;letter-spacing:-.03em;margin:24px 0 28px;max-width:720px}}
.lead{{font-size:18px;line-height:1.55;max-width:600px}}
.btns{{display:flex;gap:16px;flex-wrap:wrap;margin-top:36px}}
.btn{{display:inline-block;font-weight:500;font-size:16px;padding:18px 28px;text-decoration:none;border:1.5px solid var(--ink)}}
.btn.primary{{background:var(--accent);border-color:var(--accent);color:var(--ink)}} .btn.secondary{{background:transparent;color:var(--ink)}}
.note{{color:var(--grey);margin-top:24px;font-size:11px}}
.side{{position:relative}}
.photo{{border:1px solid var(--ink);aspect-ratio:1/1;display:flex;align-items:flex-end;padding:16px;color:var(--grey);font-size:11px;line-height:1.6;background:var(--paper)}}
.cap{{font-size:14px;color:var(--grey);margin-top:12px}}
.moonrow{{position:relative;height:200px;margin-top:64px;overflow:hidden}}
.moon{{position:absolute;right:-48px;top:0;width:100px;height:200px;background:var(--ink);border-radius:200px 0 0 200px}}
.prong{{position:absolute;height:14px;background:var(--accent)}}
.p1{{left:max(48px,calc((100vw - 1344px)/2 + 48px));right:0;top:58px}} .p2{{left:calc(max(48px,calc((100vw - 1344px)/2 + 48px)) + 31%);right:0;top:128px}}
.band{{border-top:1px solid var(--ink);margin-top:0}} .band .wrap{{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;padding:56px 48px 72px}}
.band h3{{font-weight:500;font-size:24px;line-height:1.25;letter-spacing:-.02em;margin:12px 0 8px}} .band p{{color:var(--grey);font-size:16px;line-height:1.5}}
.num{{color:var(--deep)}}
@media (max-width:900px){{.hero{{grid-template-columns:1fr;padding-top:56px}} .band .wrap{{grid-template-columns:1fr;gap:32px}}}}
@media (max-width:600px){{.wrap{{padding:0 16px}} header .wrap{{height:72px}} .logo{{width:150px}} .domain{{display:none}}
 h1{{font-size:40px}} .btn{{width:100%;text-align:center}} .band .wrap{{padding:40px 16px 56px}} .moonrow{{height:150px;margin-top:40px}}
 .p1{{left:16px;top:44px}} .p2{{left:calc(16px + 31%);top:96px}} .prong{{height:10px}}}}"""
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Expert DNA: Stay human. Automate the rest.</title><style>{css}</style></head><body>
<header><div class="wrap">{lg}<span class="mono domain">expertdna.net</span></div></header>
<main><div class="wrap"><section class="hero"><div>
<div class="mono lab"><i></i>The book / Expert DNA</div>
<h1>Your AI works like a confused intern. Give it your Expert DNA.</h1>
<p class="lead">You write down what lives in your head: your offers and prices, your ideal client, your method, your voice, your stories and your rules. The AI works from those files instead of from the internet's average. Stay human. Automate the rest.</p>
<div class="btns"><a class="btn primary" href="#">Get the book, 7 EUR</a><a class="btn secondary" href="#">See the 8 plugins</a></div>
<p class="mono note">Working price, placeholder.</p></div>
<div class="side"><div class="photo mono">Photo slot: Donatas Jonikas, PhD. Real photo only.</div><p class="cap">Donatas Jonikas, PhD. Author of the book.</p></div>
</section></div>
<div class="moonrow" aria-hidden="true"><div class="prong p1"></div><div class="prong p2"></div></div>
<section class="band"><div class="wrap">
<div><span class="mono num">01</span><h3>Write it down</h3><p>Offers, prices, ideal client, method, voice, stories and rules, as plain Markdown files.</p></div>
<div><span class="mono num">02</span><h3>The AI works from your files</h3><p>Not from the internet's average. Your judgement stays in charge.</p></div>
<div><span class="mono num">03</span><h3>Clients get more of you</h3><p>AI takes the busywork. You keep the expertise, personality, empathy and care.</p></div>
</div></section></main></body></html>"""
    p = os.path.join(APP, "landing", "landing-hero.html"); open(p, "w").write(html)
    for w in (375, 1440):
        jobs.append(dict(html=p, out=os.path.join(APP, "landing", f"landing-{w}.png"), w=w, h=900, scale=2 if w == 375 else 1, measure=False, full=True, overflow=True))

# ---------------- components ----------------
def components():
    d = os.path.join(APP, "components"); os.makedirs(d, exist_ok=True)
    css = open(os.path.join(ROOT, "tokens", "tokens.css")).read() + f"""
@font-face{{font-family:'Hanken Grotesk';font-weight:400;src:url(../../fonts/HankenGrotesk-Regular.ttf)}}
@font-face{{font-family:'Hanken Grotesk';font-weight:500;src:url(../../fonts/HankenGrotesk-Medium.ttf)}}
@font-face{{font-family:'Hanken Grotesk';font-weight:700;src:url(../../fonts/HankenGrotesk-Bold.ttf)}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(../../fonts/IBMPlexMono-Medium.ttf)}}
.edna{{--bg:var(--edna-white);--fg:var(--edna-ink);--sub:var(--edna-grey);--ln:var(--edna-line);--card:var(--edna-white);--surface:var(--edna-paper);--labc:var(--edna-accent-deep);
  background:var(--bg);color:var(--fg);font-family:var(--edna-font-sans)}}
.edna-dark{{--bg:var(--edna-ink);--fg:var(--edna-white);--sub:var(--edna-grey-dark);--ln:var(--edna-line-dark);--card:var(--edna-surface-dark);--surface:var(--edna-surface-dark);--labc:var(--edna-grey-dark)}}
.edna *{{box-sizing:border-box;border-radius:0}}
.edna-label{{font:500 12px/1.2 var(--edna-font-mono);letter-spacing:.12em;text-transform:uppercase;color:var(--labc);display:inline-flex;align-items:center;gap:10px}}
.edna-label::before{{content:"";width:14px;height:4px;background:var(--edna-accent)}}
.edna-h{{font-weight:500;letter-spacing:-.03em;line-height:1.05}}
.edna-btn{{display:inline-block;font:500 16px/1 var(--edna-font-sans);padding:16px 24px;border:1.5px solid transparent;text-decoration:none;cursor:pointer}}
.edna-btn--primary{{background:var(--edna-accent);color:var(--edna-ink);border-color:var(--edna-accent)}}
.edna-btn--secondary{{background:transparent;color:var(--fg);border-color:var(--fg)}}
.edna-link{{color:var(--fg);text-decoration:none;border-bottom:2px solid var(--edna-accent);padding-bottom:1px}}
.edna-badge{{display:inline-block;font:500 11px var(--edna-font-mono);letter-spacing:.12em;text-transform:uppercase;padding:6px 9px;border:1px solid var(--fg);color:var(--fg)}}
.edna-card{{background:var(--card);border:1px solid var(--ln);padding:28px;display:flex;flex-direction:column;gap:14px}}
.edna-card__price{{font:500 40px/1 var(--edna-font-sans);letter-spacing:-.03em}}
.edna-card__note{{font:400 10px var(--edna-font-mono);letter-spacing:.1em;color:var(--sub);text-transform:uppercase}}
.edna-bump{{background:var(--edna-accent-tint);color:var(--edna-ink);border-left:3px solid var(--edna-accent);padding:18px 20px;display:flex;gap:14px;align-items:flex-start}}
.edna-bump input{{width:22px;height:22px;accent-color:var(--edna-ink);margin-top:2px;flex:none}}
.edna-bump strong{{font-weight:500;font-size:18px;display:block}} .edna-bump span{{font-size:14px;color:var(--edna-grey)}}
.edna-field label{{display:block;font:500 11px var(--edna-font-mono);letter-spacing:.12em;text-transform:uppercase;color:var(--sub);margin-bottom:8px}}
.edna-field input{{width:100%;font:400 16px var(--edna-font-sans);padding:14px 16px;border:1px solid var(--fg);background:var(--bg);color:var(--fg);outline:none}}
.edna-field small{{display:block;color:var(--sub);font-size:13px;margin-top:6px}}
.edna-callout{{background:var(--edna-accent-tint);color:var(--edna-ink);border-left:3px solid var(--edna-accent);padding:18px 20px;font-size:16px;line-height:1.5}}
.edna-quote{{display:grid;grid-template-columns:120px 1fr;gap:24px;border-top:1px solid var(--ln);padding-top:24px}}
.edna-quote__photo{{width:120px;height:120px;border:1px dashed var(--sub);display:flex;align-items:flex-end;padding:8px;font:500 9px var(--edna-font-mono);letter-spacing:.1em;color:var(--sub);text-transform:uppercase}}
.edna-quote blockquote{{margin:0;font-size:22px;line-height:1.4;letter-spacing:-.01em}}
.edna-quote cite{{display:block;font-style:normal;font:500 12px var(--edna-font-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--sub);margin-top:14px}}
"""
    open(os.path.join(d, "components.css"), "w").write(css)
    def body(dark):
        cls = "edna edna-dark" if dark else "edna"
        card = lambda lab, t, badge, price: (f'<div class="edna-card"><div class="edna-label">{lab}</div><div class="edna-h" style="font-size:26px">{t}</div>'
                                            f'<div><span class="edna-badge">{badge}</span></div><div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid var(--ln);padding-top:16px">'
                                            f'<div><div class="edna-card__price">{price}</div><div class="edna-card__note">Working price, placeholder</div></div><a class="edna-btn edna-btn--primary" href="#">Add</a></div></div>')
        return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="components.css">
<style>body{{margin:0;width:1600px}} .wrap{{padding:64px}} .sec{{border-top:1px solid var(--ln);padding:36px 0;display:grid;grid-template-columns:260px 1fr;gap:40px;align-items:start}}</style></head>
<body class="{cls}"><div class="wrap"><div class="edna-label">Expert DNA / components{' / dark' if dark else ''}</div>
<div class="edna-h" style="font-size:52px;margin:16px 0 40px">Square corners, flat colour, one accent</div>
<div class="sec"><div class="edna-label">Buttons and link</div><div style="display:flex;gap:20px;align-items:center;flex-wrap:wrap">
<a class="edna-btn edna-btn--primary" href="#">Get the book, 7 EUR</a><a class="edna-btn edna-btn--secondary" href="#">See the 8 plugins</a><a class="edna-link" href="#">Read the first chapter</a></div></div>
<div class="sec"><div class="edna-label">Badges</div><div style="display:flex;gap:12px"><span class="edna-badge">Plugin</span><span class="edna-badge">Course</span><span class="edna-badge">Book</span></div></div>
<div class="sec"><div class="edna-label">Product cards</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
{card("Book", "Expert DNA: Stay Human, Automate the Rest", "Book", "7 EUR")}{card("Plugin 03", "Proposal: The Proposal You Don't Have to Write", "Plugin", "29 EUR")}{card("Bundle", "All 8 plugins with mini courses", "Course", "97 EUR")}</div></div>
<div class="sec"><div class="edna-label">Order bump</div><label class="edna-bump" style="max-width:640px"><input type="checkbox" checked><div><strong>Add the Starter for 29 EUR?</strong><span>One click, added to this order.</span></div></label></div>
<div class="sec"><div class="edna-label">Input</div><div class="edna-field" style="max-width:520px"><label for="e">Email</label><input id="e" placeholder="you@example.com"><small>We send the book to this address.</small></div></div>
<div class="sec"><div class="edna-label">Callout</div><div class="edna-callout" style="max-width:820px">AI without context works like a confused intern. Your Expert DNA files give it the context.</div></div>
<div class="sec"><div class="edna-label">Testimonial layout</div><div class="edna-quote" style="max-width:900px"><div class="edna-quote__photo">Photo slot</div>
<div><blockquote>{{Placeholder: a real client quote goes here. Never invented.}}</blockquote><cite>{{Name}}, {{Role}}</cite></div></div></div>
</div></body></html>"""
    for dark in (False, True):
        n = "components-dark" if dark else "components"
        p = os.path.join(d, f"{n}.html"); open(p, "w").write(body(dark))
        jobs.append(dict(html=p, out=os.path.join(d, f"{n}.png"), w=1600, h=900, scale=1, measure=False, full=True))

os.makedirs(SRC, exist_ok=True)
social_dark(); social_accent(); social_light(); ad("dark"); ad("accent"); email(); link_preview()
plugins(); logo_rules(); landing(); components()
# overview must render after tiles: move it to the end
ov = [j for j in jobs if j["out"].endswith("plugins-overview.png")]; jobs = [j for j in jobs if j not in ov] + ov
json.dump(jobs, open(os.path.join(SRC, "jobs.json"), "w"), indent=1)
print(len(jobs), "jobs")
