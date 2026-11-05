"""Modernisation study: current mark vs 4 lighter variants."""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import Face, mark_inner, horizontal, C, MW, MH

W = os.path.dirname(os.path.abspath(__file__))
def face(f, tr):
    x = Face.__new__(Face)
    from fontTools.ttLib import TTFont
    x.f = TTFont(os.path.join(W, "fonts", f)); x.gs = x.f.getGlyphSet(); x.cmap = x.f.getBestCmap()
    x.upm = x.f["head"].unitsPerEm; x.cap = x.f["OS/2"].sCapHeight; x.track = tr * x.upm; x.desc = -x.f["OS/2"].sTypoDescender
    return x

SG_MED = face("SchibstedGrotesk-500.ttf", -0.035)
SG_BOLD = face("SchibstedGrotesk-700.ttf", -0.02)
FUN = face("FunnelDisplay-600.ttf", -0.03)
HAN = face("HankenGrotesk-500.ttf", -0.03)
_i = itertools.count()

# ---- marks, all on the same 54 x 48 box ----
def m_air(l, r):
    # solid left half circle, no folds; right: 3 thin lines with air, clipped to half circle; wider gap
    i = next(_i)
    left = "M22 0 A24 24 0 0 0 22 48 Z"
    right = "M32 0 A24 24 0 0 1 32 48 Z"
    bars = "".join(f'<rect x="32" y="{y}" width="24" height="3.2"/>' for y in (10.4, 22.4, 34.4))
    return (f'<defs><clipPath id="ma{i}"><path d="{right}"/></clipPath></defs>'
            f'<path d="{left}" fill="{l}"/><g clip-path="url(#ma{i})" fill="{r}">{bars}</g>'
            f'<path d="{right}" fill="none" stroke="{r}" stroke-width="2"/>')

def m_cut(l, r):
    # left half circle with one straight cut (a single fold), right: 4 hairlines, no outline
    i = next(_i)
    left = "M24 0 A24 24 0 0 0 24 48 Z"
    right = "M30 0 A24 24 0 0 1 30 48 Z"
    bars = "".join(f'<rect x="30" y="{y}" width="24" height="2.6"/>' for y in (6, 16.5, 27, 37.5))
    return (f'<defs><mask id="mc{i}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="60" height="52"><path d="{left}" fill="#fff"/>'
            f'<rect x="-2" y="22.5" width="30" height="3" fill="#000"/></mask><clipPath id="mcc{i}"><path d="{right}"/></clipPath></defs>'
            f'<path d="{left}" fill="{l}" mask="url(#mc{i})"/><g clip-path="url(#mcc{i})" fill="{r}">{bars}</g>')

def m_text(l, r):
    # left half circle solid; right: 3 lines of text, ragged right, NOT clipped (reads as a written file)
    return (f'<path d="M24 0 A24 24 0 0 0 24 48 Z" fill="{l}"/>'
            f'<rect x="30" y="10" width="24" height="5" fill="{r}"/>'
            f'<rect x="30" y="21.5" width="17" height="5" fill="{r}"/>'
            f'<rect x="30" y="33" width="21" height="5" fill="{r}"/>')

def m_dot(l, r):
    # left half circle; right: a cursor line and two short lines (an AI writing for you)
    return (f'<path d="M24 0 A24 24 0 0 0 24 48 Z" fill="{l}"/>'
            f'<rect x="30" y="0" width="3.5" height="48" fill="{r}"/>'
            f'<rect x="38" y="14" width="16" height="3.5" fill="{r}"/>'
            f'<rect x="38" y="30.5" width="11" height="3.5" fill="{r}"/>')

def svg(inner, w, h):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}">{inner}</svg>'

def lock(markfn, fc, text, l, r, word, capr=0.5):
    H = 96.0; cap = H * capr; mw = H * MW / MH; gap = H / 4
    _, ww, lsb = fc.path(text, cap, 0, 0)
    d, ww, _ = fc.path(text, cap, mw + gap - lsb, (H + cap) / 2)
    m = f'<g transform="scale({H/MH:.4f})">{markfn(l, r)}</g>'
    return svg(m + f'<path d="{d}" fill="{word}"/>', mw + gap + ww, H + cap * 0.3)

def mark(markfn, l, r): return svg(markfn(l, r), MW, MH)

V = [
    ("A / Current", None, None, "Expert DNA", "Schibsted Grotesk Bold. Five heavy stripes, wavy folds, paper background."),
    ("B / Air", m_air, SG_MED, "Expert DNA", "Same idea, half the weight: three thin lines with air, a thin outline holds the shape. Schibsted Grotesk Medium, tight spacing."),
    ("C / Single cut", m_cut, SG_MED, "expert dna", "One straight cut on the human side, four hairlines on the AI side. Lowercase wordmark: calmer, more current."),
    ("D / Written file", m_text, FUN, "Expert DNA", "The right half becomes three lines of text, ragged like a real paragraph. Reads as 'your knowledge, written down'. Funnel Display."),
    ("E / Cursor", m_dot, HAN, "Expert DNA", "A text cursor and two short lines: your knowledge being written for AI. The most digital of the five. Hanken Grotesk Medium."),
]

def img(s, w, extra=""): return s.replace("<svg ", f'<svg style="width:{w}px;height:auto;display:block{extra}" ', 1)

rows = ""
for name, fn, fc, text, why in V:
    if fn is None:
        L_light = horizontal(C["ink"], C["accent"], C["ink"]); L_dark = horizontal(C["paper"], C["accent"], C["paper"])
        from brand import mark_only
        M = lambda l, r: mark_only(l, r)
        head = "Your AI works like a confused intern."
        hf, bg = "SGB", "#F4F1EC"
    else:
        L_light = lock(fn, fc, text, C["ink"], C["accent"], C["ink"])
        L_dark = lock(fn, fc, text, "#FFFFFF", C["accent"], "#FFFFFF")
        M = lambda l, r, fn=fn: mark(fn, l, r)
        head = "Your AI works like a confused intern."
        hf = {SG_MED: "SGM", FUN: "FUN", HAN: "HAN"}[fc]; bg = "#FFFFFF"
    post = (f'<div style="width:300px;height:300px;background:#0B0B0C;color:#fff;padding:22px;display:flex;flex-direction:column;justify-content:space-between">'
            f'<div style="font:11px PM;letter-spacing:.12em;color:#A3A29C">EXPERT DNA / 01</div>'
            f'<div style="font-family:{hf};font-size:30px;line-height:1.04;letter-spacing:-.03em">{head}</div>'
            f'{img(L_dark, 120)}</div>')
    rows += (f'<section><div class="info"><div class="lab">{name}</div><p>{why}</p></div>'
             f'<div class="c" style="background:{bg}">{img(L_light, 460)}</div>'
             f'<div class="c" style="background:#0B0B0C">{img(L_dark, 460)}</div>'
             f'<div class="c" style="background:{bg};gap:20px">{img(M(C["ink"], C["accent"]), 64)}{img(M(C["ink"], C["accent"]), 32)}{img(M(C["ink"], C["accent"]), 16)}</div>'
             f'<div class="c" style="background:#E9E7E3">{post}</div></section>')

ff = ("@font-face{font-family:SGB;src:url(../fonts/SchibstedGrotesk-Bold.ttf)}@font-face{font-family:SGM;src:url(../fonts/SchibstedGrotesk-Medium.ttf)}"
      "@font-face{font-family:FUN;src:url(fonts/FunnelDisplay-600.ttf)}@font-face{font-family:HAN;src:url(fonts/HankenGrotesk-500.ttf)}"
      "@font-face{font-family:PM;src:url(../fonts/IBMPlexMono-Medium.ttf)}@font-face{font-family:SGR;src:url(../fonts/SchibstedGrotesk-Regular.ttf)}")
html = f"""<!doctype html><meta charset=utf-8><style>{ff}*{{margin:0;box-sizing:border-box}}body{{width:2400px;background:#fff;color:#101114;font-family:SGR}}
header{{padding:48px 56px;border-bottom:1px solid #101114}}h1{{font:40px SGM;letter-spacing:-.03em;margin-top:10px}}
.lab{{font:12px PM;letter-spacing:.12em;text-transform:uppercase}}
section{{display:grid;grid-template-columns:380px 1fr 1fr 300px 360px;border-bottom:1px solid #DCD7CE}}
.info{{padding:32px 40px}} .info p{{font-size:17px;line-height:1.45;margin-top:12px;color:#444}}
.c{{display:flex;align-items:center;justify-content:center;padding:32px}}</style><body>
<header><div class="lab">Expert DNA / modernisation study</div><h1>Same idea, five weights: from current to most digital</h1></header>{rows}</body>"""
open(os.path.join(W, "modern.html"), "w").write(html)
print("ok")
