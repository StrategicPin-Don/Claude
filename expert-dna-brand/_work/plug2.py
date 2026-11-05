"""Variant E refined: keep crescent + cursor plug, add ONE minimal brain hint."""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modern import face, svg
from brand import C

W = os.path.dirname(os.path.abspath(__file__))
HAN = face("HankenGrotesk-500.ttf", -0.03)
_i = itertools.count()
HALF = "M24 0 A24 24 0 0 0 24 48 Z"
CUT = 2.6

def plug(col):  # identical to variant E
    return (f'<rect x="30" y="0" width="3.5" height="48" fill="{col}"/>'
            f'<rect x="38" y="14" width="16" height="3.5" fill="{col}"/>'
            f'<rect x="38" y="30.5" width="11" height="3.5" fill="{col}"/>')

def masked(shape, cuts, col, round_=True, extra_black=""):
    i = next(_i)
    cap = "round" if round_ else "butt"
    return (f'<defs><mask id="q{i}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="30" height="52">'
            f'<path d="{shape}" fill="#fff"/><g fill="none" stroke="#000" stroke-width="{CUT}" stroke-linecap="{cap}">{cuts}</g>{extra_black}</mask></defs>'
            f'<path d="{shape}" fill="{col}" mask="url(#q{i})"/>')

def v_ref(c):   return f'<path d="{HALF}" fill="{c}"/>'
def v_fold(c):  return masked(HALF, '<path d="M25 19.5 C19 16.5 14.5 22.5 8.5 19.5"/>', c)
def v_fiss(c):  return masked(HALF, '<path d="M-2 29 C7 25 16 32 26 27.5"/>', c, False)
def v_notch(c): return masked(HALF, "", c, extra_black='<circle cx="1.2" cy="30" r="5.2" fill="#000"/>')
def v_wave(c):  return f'<path d="M24 0 A24 24 0 0 0 24 48 C20.5 42 27.5 36 24 30 C20.5 24 27.5 18 24 12 C21.5 7.5 25.5 3.5 24 0 Z" fill="{c}"/>'
def v_echo(c):  return masked(HALF, '<path d="M25 15.75 H13"/><path d="M25 32.25 H17"/>', c)
def v_flow(c):  return masked(HALF, '<path d="M25 15.75 C17 15.75 16 22 9 20.5"/>', c)

V = [
    ("0 / Reference", v_ref, "Variant E as it is: half moon and plug."),
    ("1 / One fold", v_fold, "One thin fold cut into the half moon. The smallest possible brain hint."),
    ("2 / Fissure", v_fiss, "One curved gap splits the half into two lobes, like the line between frontal and temporal lobe."),
    ("3 / Notch", v_notch, "One small notch in the outline. The silhouette turns brain-like without any inner detail."),
    ("4 / Midline", v_wave, "The flat side becomes a gentle wave, the line between the two hemispheres, facing the plug."),
    ("5 / Echo", v_echo, "Two short cuts sit exactly on the prong lines. The folds of the brain continue as the pins of the plug."),
    ("6 / Flow", v_flow, "One fold starts at the top prong and bends into the brain: the connection drawn as a single line."),
]

def mark(f, bc, pc): return svg(f(bc) + plug(pc), 54, 48)
def lock(f, bc, pc, word):
    H = 96.0; cap = H * 0.5; mw = H * 54 / 48; gap = H / 4
    _, ww, lsb = HAN.path("Expert DNA", cap, 0, 0)
    d, ww, _ = HAN.path("Expert DNA", cap, mw + gap - lsb, (H + cap) / 2)
    return svg(f'<g transform="scale({H/48:.4f})">{f(bc)}{plug(pc)}</g><path d="{d}" fill="{word}"/>', mw + gap + ww, H + cap * 0.3)
def img(s, w): return s.replace("<svg ", f'<svg style="width:{w}px;height:auto;display:block" ', 1)

rows = ""
for name, f, why in V:
    rows += (f'<div class="info"><div class="lab">{name}</div><p>{why}</p></div>'
             f'<div class="c">{img(mark(f, C["ink"], C["accent"]), 150)}</div>'
             f'<div class="c" style="background:#0B0B0C">{img(mark(f, "#FFFFFF", C["accent"]), 150)}</div>'
             f'<div class="c">{img(mark(f, C["accent"], C["ink"]), 150)}</div>'
             f'<div class="c" style="gap:18px">{"".join(img(mark(f, C["ink"], C["accent"]), s) for s in (48, 32, 16))}</div>'
             f'<div class="c">{img(lock(f, C["ink"], C["accent"], C["ink"]), 380)}</div>')

ff = ("@font-face{font-family:SGM;src:url(../fonts/SchibstedGrotesk-Medium.ttf)}@font-face{font-family:PM;src:url(../fonts/IBMPlexMono-Medium.ttf)}"
      "@font-face{font-family:SGR;src:url(../fonts/SchibstedGrotesk-Regular.ttf)}")
heads = "".join(f'<div class="ch">{h}</div>' for h in ["", "Ink brain, accent plug", "Dark", "Accent brain, ink plug", "48 / 32 / 16 px", "Lockup"])
html = f"""<!doctype html><meta charset=utf-8><style>{ff}*{{margin:0;box-sizing:border-box}}body{{width:2400px;background:#fff;color:#101114;font-family:SGR}}
header{{padding:44px 56px;border-bottom:1px solid #101114}}h1{{font:38px SGM;letter-spacing:-.03em;margin-top:10px}}
.lab{{font:12px PM;letter-spacing:.12em;text-transform:uppercase}}
.grid{{display:grid;grid-template-columns:340px repeat(3,1fr) 220px 480px}}
.info{{padding:26px 32px;border-bottom:1px solid #DCD7CE}} .info p{{font-size:16px;line-height:1.45;margin-top:10px;color:#444}}
.c{{display:flex;align-items:center;justify-content:center;padding:26px;border-bottom:1px solid #DCD7CE;border-left:1px solid #EEE;background:#fff}}
.ch{{font:11px PM;letter-spacing:.1em;text-transform:uppercase;padding:16px 20px;border-bottom:1px solid #101114;border-left:1px solid #EEE}}</style><body>
<header><div class="lab">Expert DNA / variant E refined</div><h1>Half moon and plug, with one minimal brain hint</h1></header>
<div class="grid">{heads}{rows}</div></body>"""
open(os.path.join(W, "plug2.html"), "w").write(html)
print("ok")
