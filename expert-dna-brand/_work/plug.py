"""Variant E 'plug': brain half + plug. Explore brain stylisation and colour."""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modern import face, svg
from brand import C

W = os.path.dirname(os.path.abspath(__file__))
HAN = face("HankenGrotesk-500.ttf", -0.03)
_i = itertools.count()
S = 3.5  # stroke unit shared by plug and line brains

# Brain silhouette (left half, flat side at x = 24): union of lobe circles
LOBES = [(16.5, 9.5, 9.5), (8, 18.5, 8), (8, 30.5, 8), (16.5, 38.5, 9.5), (17, 24, 10)]

def plug(col):
    # plug body (vertical bar) + two equal prongs with round ends
    return (f'<rect x="29" y="4" width="{S}" height="40" fill="{col}"/>'
            f'<path d="M32 16.5 H52" stroke="{col}" stroke-width="{S}" stroke-linecap="round"/>'
            f'<path d="M32 31.5 H52" stroke="{col}" stroke-width="{S}" stroke-linecap="round"/>')

def lobes_fill(fill):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>' for x, y, r in LOBES)

def b_crescent(col, bg=None):
    return f'<path d="M24 0 A24 24 0 0 0 24 48 Z" fill="{col}"/>'

def b_lobes(col, bg=None):
    i = next(_i)
    cuts = ('<path d="M24 16 C19 13.5 15 19.5 9.5 16.5"/>'
            '<path d="M24 31.5 C19 29 15 34.5 9 32"/>'
            '<path d="M18.5 24 C15.5 22.5 13 26 9.5 24.5"/>')
    return (f'<defs><clipPath id="k{i}"><rect x="-1" y="-1" width="25" height="50"/></clipPath>'
            f'<mask id="m{i}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="30" height="52">{lobes_fill("#fff")}'
            f'<g fill="none" stroke="#000" stroke-width="2.4" stroke-linecap="round">{cuts}</g></mask></defs>'
            f'<g clip-path="url(#k{i})"><g mask="url(#m{i})"><rect x="-2" y="-2" width="30" height="52" fill="{col}"/></g></g>')

def b_monoline(col, bg=None):
    """Outline of the lobe union (thickness S) + two inner gyri, one line weight. Erode = true inner offset."""
    i = next(_i)
    w = S
    gyri = ('<path d="M20.5 16 C17.5 14.5 15 18.5 11 16.8"/>'
            '<path d="M20.5 32 C17.5 30.5 15 34.5 11 32.8"/>')
    return (f'<defs><clipPath id="k{i}"><rect x="-1" y="-1" width="25" height="50"/></clipPath>'
            f'<filter id="e{i}" x="-10%" y="-10%" width="120%" height="120%"><feMorphology operator="erode" radius="{w}"/></filter>'
            f'<mask id="m{i}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="30" height="52">{lobes_fill("#fff")}'
            f'<g filter="url(#e{i})"><g>{lobes_fill("#000")}</g><rect x="23" y="-4" width="10" height="56" fill="#000"/></g></mask></defs>'
            f'<g clip-path="url(#k{i})"><g mask="url(#m{i})"><rect x="-2" y="-2" width="30" height="52" fill="{col}"/></g></g>'
            f'<g fill="none" stroke="{col}" stroke-width="{w*0.85}" stroke-linecap="round">{gyri}</g>')

def b_nested(col, bg=None):
    """Brain as nested folds: three meandering half rings inside each other."""
    w = S
    paths = ["M24 1.75 C10 1.75 1.75 11 1.75 24 C1.75 37 10 46.25 24 46.25",
             "M24 9.5 C17 9.5 9.5 12 10.5 18 C11.5 22 7.5 24 9.5 29 C11 34 15 38.5 24 38.5",
             "M24 17 C20 17 17.5 20 19 23.5 C20 26.5 18.5 29.5 24 31"]
    return (f'<g fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round">'
            + "".join(f'<path d="{p}"/>' for p in paths) + "</g>")

BRAINS = [
    ("1 / Current crescent", b_crescent, "Reference: the black half moon from variant E."),
    ("2 / Lobes", b_lobes, "Solid half brain built from five lobes, with three thin folds. Reads as a brain at a glance."),
    ("3 / Monoline", b_monoline, "The same lobes drawn as one line, the same weight as the plug. Lightest and most current."),
    ("4 / Nested folds", b_nested, "Three folds nested inside each other, like the cortex seen in section. Abstract, drawn with the plug's line."),
]

COLOURS = [
    ("Ink brain, accent plug", "#FFFFFF", C["ink"], C["accent"]),
    ("Accent brain, ink plug", "#FFFFFF", C["accent"], C["ink"]),
    ("Grey brain, accent plug", "#FFFFFF", "#8E8C86", C["accent"]),
    ("Dark: white brain, accent plug", "#0B0B0C", "#FFFFFF", C["accent"]),
    ("Dark: accent brain, white plug", "#0B0B0C", C["accent"], "#FFFFFF"),
]

def mark(bf, bc, pc): return svg(bf(bc) + plug(pc), 54, 48)

def lock(bf, bc, pc, word):
    H = 96.0; cap = H * 0.5; mw = H * 54 / 48; gap = H / 4
    _, ww, lsb = HAN.path("Expert DNA", cap, 0, 0)
    d, ww, _ = HAN.path("Expert DNA", cap, mw + gap - lsb, (H + cap) / 2)
    return svg(f'<g transform="scale({H/48:.4f})">{bf(bc)}{plug(pc)}</g><path d="{d}" fill="{word}"/>', mw + gap + ww, H + cap * 0.3)

def img(s, w): return s.replace("<svg ", f'<svg style="width:{w}px;height:auto;display:block" ', 1)

head = "".join(f'<div class="ch">{n}</div>' for n, *_ in COLOURS)
rows = ""
for name, bf, why in BRAINS:
    cells = ""
    for cn, bg, bc, pc in COLOURS:
        cells += f'<div class="c" style="background:{bg}">{img(mark(bf, bc, pc), 150)}</div>'
    small = "".join(img(mark(bf, C["ink"], C["accent"]), s) for s in (48, 32, 16))
    rows += (f'<section><div class="info"><div class="lab">{name}</div><p>{why}</p></div>{cells}'
             f'<div class="c" style="background:#fff;gap:18px">{small}</div>'
             f'<div class="c" style="background:#fff">{img(lock(bf, C["ink"], C["accent"], C["ink"]), 330)}</div></section>')

ff = ("@font-face{font-family:SGM;src:url(../fonts/SchibstedGrotesk-Medium.ttf)}@font-face{font-family:PM;src:url(../fonts/IBMPlexMono-Medium.ttf)}"
      "@font-face{font-family:SGR;src:url(../fonts/SchibstedGrotesk-Regular.ttf)}")
html = f"""<!doctype html><meta charset=utf-8><style>{ff}*{{margin:0;box-sizing:border-box}}body{{width:2400px;background:#fff;color:#101114;font-family:SGR}}
header{{padding:44px 56px;border-bottom:1px solid #101114}}h1{{font:38px SGM;letter-spacing:-.03em;margin-top:10px}}
.lab{{font:12px PM;letter-spacing:.12em;text-transform:uppercase}}
.grid{{display:grid;grid-template-columns:300px repeat(5,1fr) 200px 380px}}
section{{display:contents}} .info{{padding:28px 32px;border-bottom:1px solid #DCD7CE}} .info p{{font-size:16px;line-height:1.45;margin-top:10px;color:#444}}
.c{{display:flex;align-items:center;justify-content:center;padding:28px;border-bottom:1px solid #DCD7CE;border-left:1px solid #EEE}}
.ch{{font:11px PM;letter-spacing:.1em;text-transform:uppercase;padding:16px 20px;border-bottom:1px solid #101114;border-left:1px solid #EEE}}</style><body>
<header><div class="lab">Expert DNA / variant E / plug your brain in</div><h1>Four ways to draw the brain half, five colour options</h1></header>
<div class="grid"><div class="ch"></div>{head}<div class="ch">48 / 32 / 16 px</div><div class="ch">Lockup</div>{rows}</div></body>"""
open(os.path.join(W, "plug.html"), "w").write(html)
print("ok")
