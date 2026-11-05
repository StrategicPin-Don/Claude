"""Expert DNA v2 core: 'Plug' mark (half moon + plug). Logo family, tokens, contrast, favicons."""
import os, json, itertools
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(ROOT, "fonts")

C = dict(
    ink="#101114", white="#FFFFFF", paper="#F4F3F0",
    accent="#FF5533", accent_tint="#FFE1D8", accent_deep="#B32F15",
    grey="#66655F", grey_dark="#A3A29C", line="#E2E0DB", line_dark="#2E3036",
    surface_dark="#1A1B1F",
)

def lum(h):
    h = h.lstrip("#"); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return round((la + 0.05) / (lb + 0.05), 2)

class Face:
    def __init__(self, f, track=0.0):
        self.f = TTFont(os.path.join(FD, f)); self.gs = self.f.getGlyphSet(); self.cmap = self.f.getBestCmap()
        self.cap = self.f["OS/2"].sCapHeight; self.track = track * self.f["head"].unitsPerEm
    def path(self, t, cap_px, x0, baseline):
        s = cap_px / self.cap; x = 0; d = []; first = None
        for ch in t:
            g = self.cmap.get(ord(ch), self.cmap[32]); first = first or g
            pen = SVGPathPen(self.gs); self.gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x0 + x * s, baseline))); d.append(pen.getCommands())
            x += self.gs[g].width + self.track
        bp = BoundsPen(self.gs); self.gs[first].draw(bp)
        return " ".join(d), (x - self.track) * s, (bp.bounds[0] if bp.bounds else 0) * s

WORD = Face("HankenGrotesk-Medium.ttf", -0.03)
REG = Face("HankenGrotesk-Regular.ttf", -0.005)

# ---- mark: 54 x 48 box. Half moon r = 24 (x 0..24). Plug: bar x 30..33.5 full height, prongs at y 14 and 30.5.
MW, MH = 54, 48
HALF = "M24 0 A24 24 0 0 0 24 48 Z"
def mark_inner(brain, plug):
    return (f'<path d="{HALF}" fill="{brain}"/>'
            f'<rect x="30" y="0" width="3.5" height="48" fill="{plug}"/>'
            f'<rect x="38" y="14" width="16" height="3.5" fill="{plug}"/>'
            f'<rect x="38" y="30.5" width="11" height="3.5" fill="{plug}"/>')

def svg(inner, w, h, title="Expert DNA"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" width="{w:.0f}" height="{h:.0f}">'
            f'<title>{title}</title>{inner}</svg>')

H = 96.0
TAG = "Stay human. Automate the rest."
END = "by Donatas Jonikas, PhD"
def place(x, y, h, b, p): return f'<g transform="translate({x:.2f},{y:.2f}) scale({h/MH:.4f})">{mark_inner(b, p)}</g>'

def horizontal(b, p, word, tagline=False, tagc=None):
    cap = H * 0.5; mw = H * MW / MH; gap = H / 4
    _, ww, lsb = WORD.path("Expert DNA", cap, 0, 0)
    xw = mw + gap - lsb
    d, ww, _ = WORD.path("Expert DNA", cap, xw, (H + cap) / 2)
    inner = place(0, 0, H, b, p) + f'<path d="{d}" fill="{word}"/>'; w = xw + ww; h = H + 2
    if tagline:
        tc = cap * 0.36; td, tw, tl = REG.path(TAG, tc, 0, 0)
        tb = H + H / 8 * 1.6 + tc
        td, tw, _ = REG.path(TAG, tc, mw + gap - tl, tb)
        inner += f'<path d="{td}" fill="{tagc or word}"/>'; h = tb + tc * 0.3; w = max(w, mw + gap + tw)
    return svg(inner, w, h)

def stacked(b, p, word, tagline=False, tagc=None):
    cap = H * 0.42; mw = H * MW / MH
    _, ww, _ = WORD.path("Expert DNA", cap, 0, 0)
    tc = cap * 0.42; _, tw, _ = REG.path(TAG, tc, 0, 0)
    W = max(ww, mw, tw if tagline else 0)
    inner = place((W - mw) / 2, 0, H, b, p)
    base = H + H / 4 + cap
    d, _, _ = WORD.path("Expert DNA", cap, (W - ww) / 2, base); inner += f'<path d="{d}" fill="{word}"/>'
    h = base + cap * 0.3
    if tagline:
        tb = base + H / 8 * 1.6 + tc
        td, _, _ = REG.path(TAG, tc, (W - tw) / 2, tb); inner += f'<path d="{td}" fill="{tagc or word}"/>'; h = tb + tc * 0.3
    return svg(inner, W, h)

def mark_only(b, p): return svg(mark_inner(b, p), MW, MH)

def wordmark(word):
    cap = 60; _, ww, lsb = WORD.path("Expert DNA", cap, 0, 0)
    d, ww, _ = WORD.path("Expert DNA", cap, -lsb, cap)
    return svg(f'<path d="{d}" fill="{word}"/>', ww - lsb, cap * 1.3)

def endorsed(b, p, word, sub):
    cap = H * 0.5; mw = H * MW / MH; gap = H / 4
    _, ww, lsb = WORD.path("Expert DNA", cap, 0, 0); xw = mw + gap - lsb
    d, ww, _ = WORD.path("Expert DNA", cap, xw, (H + cap) / 2); Wd = xw + ww
    ec = cap * 0.3; _, ew, el = REG.path(END, ec, 0, 0)
    ry = H + H / 8 * 1.5; eb = ry + H / 8 * 1.5 + ec
    ed, _, _ = REG.path(END, ec, -el, eb)
    return svg(place(0, 0, H, b, p) + f'<path d="{d}" fill="{word}"/><rect x="0" y="{ry:.2f}" width="{Wd:.2f}" height="1.5" fill="{sub}"/><path d="{ed}" fill="{sub}"/>', Wd, eb + ec * 0.35)

CW = {
    "colour-on-light": (C["ink"], C["accent"], C["ink"], C["grey"]),
    "colour-on-dark": (C["white"], C["accent"], C["white"], C["grey_dark"]),
    "black": (C["ink"], C["ink"], C["ink"], C["ink"]),
    "white": (C["white"], C["white"], C["white"], C["white"]),
    "accent": (C["accent"], C["accent"], C["accent"], C["accent"]),
}

def favicon(px, dark=False):
    bg = C["ink"] if dark else C["white"]; b = C["white"] if dark else C["ink"]
    pad = 6 if px <= 32 else 10; side = MW + 2 * pad
    return svg(f'<rect width="{side}" height="{side}" fill="{bg}"/><g transform="translate({pad},{(side - MH) / 2})">{mark_inner(b, C["accent"])}</g>', side, side)

if __name__ == "__main__":
    sd = os.path.join(ROOT, "logo", "svg"); os.makedirs(sd, exist_ok=True)
    for cw, (b, p, w, s) in CW.items():
        files = {"horizontal": horizontal(b, p, w), "horizontal-tagline": horizontal(b, p, w, True, s),
                 "stacked": stacked(b, p, w), "stacked-tagline": stacked(b, p, w, True, s),
                 "mark": mark_only(b, p), "wordmark": wordmark(w), "endorsed": endorsed(b, p, w, s)}
        for k, v in files.items(): open(os.path.join(sd, f"expertdna-{k}-{cw}.svg"), "w").write(v)
    fd = os.path.join(ROOT, "_work", "fav2"); os.makedirs(fd, exist_ok=True)
    for px in (16, 32, 48, 180, 512): open(os.path.join(fd, f"fav-{px}.svg"), "w").write(favicon(px))
    open(os.path.join(fd, "avatar.svg"), "w").write(favicon(512, dark=True))
    # tokens
    td = os.path.join(ROOT, "tokens"); os.makedirs(td, exist_ok=True)
    space = {f"s{i}": i * 4 for i in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32)}
    json.dump({"color": C, "font": {"sans": "Hanken Grotesk", "mono": "IBM Plex Mono"}, "space": space, "radius": 0}, open(os.path.join(td, "tokens.json"), "w"), indent=2)
    css = [":root {"] + [f"  --edna-{k.replace('_', '-')}: {v};" for k, v in C.items()]
    css += ["  --edna-font-sans: 'Hanken Grotesk', Arial, sans-serif;", "  --edna-font-mono: 'IBM Plex Mono', 'Courier New', monospace;"]
    css += [f"  --edna-{k}: {v}px;" for k, v in space.items()] + ["  --edna-radius: 0;", "}"]
    open(os.path.join(td, "tokens.css"), "w").write("\n".join(css) + "\n")
    rows = []
    for bg in ("white", "paper", "ink", "accent", "accent_tint", "surface_dark"):
        for fg in ("ink", "white", "accent", "accent_deep", "grey", "grey_dark"):
            if fg == bg: continue
            r = ratio(C[fg], C[bg]); rows.append(dict(text=fg, bg=bg, ratio=r, aa_normal=r >= 4.5, aa_large=r >= 3))
    json.dump(rows, open(os.path.join(td, "contrast.json"), "w"), indent=2)
    for r in rows: print(f'{r["text"]:12} on {r["bg"]:13} {r["ratio"]:6} {"AA" if r["aa_normal"] else ("large" if r["aa_large"] else "fail")}')
