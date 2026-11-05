"""Expert DNA Phase 2: logo family, tokens, contrast. Single source for geometry."""
import os, json, itertools
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(ROOT, "fonts")
SVGD = os.path.join(ROOT, "logo", "svg"); os.makedirs(SVGD, exist_ok=True)

# ---------------- colour ----------------
C = dict(
    ink="#101114", paper="#F4F1EC", white="#FFFFFF",
    accent="#FF5533", accent_tint="#FFE1D8", accent_deep="#B32F15",
    grey="#66655F", grey_dark="#A3A29C", line="#DCD7CE", line_dark="#34383F",
)
ALT_ACCENT = "#FF7520"

def lum(h):
    h = h.lstrip("#"); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return round((la + 0.05) / (lb + 0.05), 2)

# ---------------- type ----------------
class Face:
    def __init__(self, f, track=0.0):
        self.f = TTFont(os.path.join(FD, f)); self.gs = self.f.getGlyphSet(); self.cmap = self.f.getBestCmap()
        self.upm = self.f["head"].unitsPerEm; self.cap = self.f["OS/2"].sCapHeight; self.track = track * self.upm
        self.desc = -self.f["OS/2"].sTypoDescender
    def layout(self, t):
        x, out = 0, []
        for ch in t:
            g = self.cmap.get(ord(ch), self.cmap[ord(" ")]); out.append((g, x)); x += self.gs[g].width + self.track
        return out, x - self.track
    def path(self, t, cap_px, x0, baseline):
        s = cap_px / self.cap; gl, w = self.layout(t); d = []
        for g, x in gl:
            pen = SVGPathPen(self.gs); self.gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x0 + x * s, baseline))); d.append(pen.getCommands())
        # left side bearing of first glyph for optical alignment
        bp = BoundsPen(self.gs); self.gs[gl[0][0]].draw(bp); lsb = (bp.bounds[0] if bp.bounds else 0) * s
        return " ".join(d), w * s, lsb

BOLD = Face("SchibstedGrotesk-Bold.ttf", -0.02)
MED = Face("SchibstedGrotesk-Medium.ttf", -0.005)
REG = Face("SchibstedGrotesk-Regular.ttf", 0)
MONO = Face("IBMPlexMono-Medium.ttf", 0.08)

# ---------------- mark geometry ----------------
# Construction: two half circles r = 4u, gap u, u = 6 units. Height 8u = 48. Right half = 5 written lines.
U = 6
LEFT = "M24 0 A24 24 0 0 0 24 48 Z"
RIGHT = "M30 0 A24 24 0 0 1 30 48 Z"
FOLDS = ["M4 15 C10 18 16 12 24 16", "M3 33 C10 29 16 36 24 31"]
BARS = [(0, 6), (10.5, 6), (21, 6), (31.5, 6), (42, 6)]
MW, MH = 54, 48
_id = itertools.count()

def mark_inner(left, right):
    i = next(_id)
    folds = "".join(f'<path d="{d}"/>' for d in FOLDS)
    bars = "".join(f'<rect x="30" y="{y}" width="24" height="{h}"/>' for y, h in BARS)
    return (f'<defs><mask id="eL{i}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="60" height="52">'
            f'<path d="{LEFT}" fill="#fff"/><g fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">{folds}</g></mask>'
            f'<clipPath id="eR{i}"><path d="{RIGHT}"/></clipPath></defs>'
            f'<path d="{LEFT}" fill="{left}" mask="url(#eL{i})"/>'
            f'<g clip-path="url(#eR{i})" fill="{right}">{bars}</g>')

def svg(inner, w, h, title="Expert DNA"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" width="{w:.0f}" height="{h:.0f}">'
            f'<title>{title}</title>{inner}</svg>')

def place_mark(x, y, h, left, right):
    s = h / MH
    return f'<g transform="translate({x:.2f},{y:.2f}) scale({s:.4f})">{mark_inner(left, right)}</g>'

TAG = "Stay human. Automate the rest."
END = "by Donatas Jonikas, PhD"

# All lockups built at mark height H = 96 px.
H = 96.0
u = H / 8

def horizontal(left, right, word, tagline=False, tagc=None):
    cap = H * 0.5
    gap = 2 * u
    wd, ww, lsb = BOLD.path("Expert DNA", cap, H * MW / MH + gap, 0)
    mw = H * MW / MH
    x_word = mw + gap - lsb
    wd, ww, _ = BOLD.path("Expert DNA", cap, x_word, (H + cap) / 2)
    inner = place_mark(0, 0, H, left, right) + f'<path d="{wd}" fill="{word}"/>'
    w = x_word + ww; h = H + (cap * 0.27 - (H - cap) / 2 if cap * 0.27 > (H - cap) / 2 else 0)
    if tagline:
        tcap = cap * 0.34
        td, tw, tl = MED.path(TAG, tcap, x_word, 0)
        base = H + u * 1.5 + tcap
        td, tw, _ = MED.path(TAG, tcap, x_word + lsb - tl, base)
        inner += f'<path d="{td}" fill="{tagc or word}"/>'
        h = base + tcap * 0.27; w = max(w, x_word + tw)
    return svg(inner, w, h)

def stacked(left, right, word, tagline=False, tagc=None):
    cap = H * 0.42
    _, ww, _ = BOLD.path("Expert DNA", cap, 0, 0)
    mw = H * MW / MH
    tcap = cap * 0.4
    _, tw, _ = MED.path(TAG, tcap, 0, 0)
    W = max(ww, mw, tw if tagline else 0)
    inner = place_mark((W - mw) / 2, 0, H, left, right)
    base = H + 2 * u + cap
    wd, _, _ = BOLD.path("Expert DNA", cap, (W - ww) / 2, base)
    inner += f'<path d="{wd}" fill="{word}"/>'
    h = base + cap * 0.27
    if tagline:
        tb = base + u * 1.5 + tcap + cap * 0.2
        td, _, _ = MED.path(TAG, tcap, (W - tw) / 2, tb)
        inner += f'<path d="{td}" fill="{tagc or word}"/>'
        h = tb + tcap * 0.27
    return svg(inner, W, h)

def mark_only(left, right, pad=0, bg=None, size=None):
    w, h = MW + 2 * pad, MH + 2 * pad
    side = max(w, h) if size == "square" else None
    if side:
        ox, oy = (side - MW) / 2, (side - MH) / 2
        b = f'<rect width="{side}" height="{side}" fill="{bg}"/>' if bg else ""
        return svg(b + f'<g transform="translate({ox},{oy})">{mark_inner(left, right)}</g>', side, side)
    return svg(f'<g transform="translate({pad},{pad})">{mark_inner(left, right)}</g>', w, h)

def wordmark_only(word):
    cap = 60
    wd, ww, lsb = BOLD.path("Expert DNA", cap, 0, 0)
    wd, ww, _ = BOLD.path("Expert DNA", cap, -lsb, cap)
    return svg(f'<path d="{wd}" fill="{word}"/>', ww - lsb, cap + BOLD.desc * cap / BOLD.cap)

def endorsement(left, right, word, sub):
    base = horizontal(left, right, word)
    # rebuild: horizontal + full-width thin rule + endorsement line
    cap = H * 0.5; gap = 2 * u; mw = H * MW / MH
    _, ww, lsb = BOLD.path("Expert DNA", cap, 0, 0)
    x_word = mw + gap - lsb
    wd, ww, _ = BOLD.path("Expert DNA", cap, x_word, (H + cap) / 2)
    W = x_word + ww
    ecap = cap * 0.3
    ed, ew, el = REG.path(END, ecap, 0, 0)
    ry = H + u * 1.5
    eb = ry + u * 1.5 + ecap
    ed, ew, _ = REG.path(END, ecap, -el, eb)
    inner = (place_mark(0, 0, H, left, right) + f'<path d="{wd}" fill="{word}"/>'
             f'<rect x="0" y="{ry:.2f}" width="{W:.2f}" height="1.5" fill="{sub}"/>'
             f'<path d="{ed}" fill="{sub}"/>')
    return svg(inner, W, eb + ecap * 0.3)

COLOURWAYS = {
    # name: (left hemisphere, right lines, wordmark, tagline/secondary)
    "colour-on-light": (C["ink"], C["accent"], C["ink"], C["grey"]),
    "colour-on-dark": (C["paper"], C["accent"], C["paper"], C["grey_dark"]),
    "black": (C["ink"], C["ink"], C["ink"], C["ink"]),
    "white": (C["white"], C["white"], C["white"], C["white"]),
    "accent": (C["accent"], C["accent"], C["accent"], C["accent"]),
}

def build():
    files = {}
    for cw, (l, r, wcol, sub) in COLOURWAYS.items():
        files[f"expertdna-horizontal-{cw}.svg"] = horizontal(l, r, wcol)
        files[f"expertdna-horizontal-tagline-{cw}.svg"] = horizontal(l, r, wcol, True, sub)
        files[f"expertdna-stacked-{cw}.svg"] = stacked(l, r, wcol)
        files[f"expertdna-stacked-tagline-{cw}.svg"] = stacked(l, r, wcol, True, sub)
        files[f"expertdna-mark-{cw}.svg"] = mark_only(l, r)
        files[f"expertdna-wordmark-{cw}.svg"] = wordmark_only(wcol)
        files[f"expertdna-endorsed-{cw}.svg"] = endorsement(l, r, wcol, sub)
    # favicon / avatar sources (square, with background)
    files["_favicon-source.svg"] = mark_only(C["ink"], C["accent"], bg=C["paper"], size="square", pad=0)
    for n, s in files.items():
        open(os.path.join(SVGD, n), "w").write(s)
    return files

def favicon_svg(px):
    """Square favicon art: paper field, mark with optical padding. Small sizes use 3 thicker lines? No: same mark, larger fill."""
    pad = 5 if px <= 32 else 8
    side = MW + 2 * pad
    oy = (side - MH) / 2
    return svg(f'<rect width="{side}" height="{side}" fill="{C["paper"]}"/><g transform="translate({pad},{oy})">{mark_inner(C["ink"], C["accent"])}</g>', side, side)

def avatar_svg():
    side = 100
    s = 60 / MW
    return svg(f'<rect width="100" height="100" fill="{C["ink"]}"/><g transform="translate(20,{(100 - MH * s) / 2:.2f}) scale({s:.4f})">{mark_inner(C["paper"], C["accent"])}</g>', 100, 100)

def tokens():
    t = {
        "color": {k: v for k, v in C.items()},
        "font": {"sans": "Schibsted Grotesk", "mono": "IBM Plex Mono"},
        "space": {f"s{i}": i * 4 for i in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32)},
        "radius": 0,
        "rule": {"hair": "1px", "strong": "2px"},
    }
    os.makedirs(os.path.join(ROOT, "tokens"), exist_ok=True)
    json.dump(t, open(os.path.join(ROOT, "tokens", "tokens.json"), "w"), indent=2)
    css = [":root {"]
    for k, v in C.items(): css.append(f"  --edna-{k.replace('_', '-')}: {v};")
    css += ["  --edna-font-sans: 'Schibsted Grotesk', Arial, sans-serif;",
            "  --edna-font-mono: 'IBM Plex Mono', 'Courier New', monospace;"]
    for k, v in t["space"].items(): css.append(f"  --edna-{k}: {v}px;")
    css += ["  --edna-radius: 0;", "  --edna-rule: 1px solid var(--edna-line);", "}"]
    open(os.path.join(ROOT, "tokens", "tokens.css"), "w").write("\n".join(css) + "\n")

def contrast():
    fg = ["ink", "paper", "white", "accent", "accent_deep", "grey", "grey_dark"]
    bg = ["paper", "white", "ink", "accent", "accent_tint"]
    rows = []
    for b in bg:
        for f in fg:
            if f == b: continue
            r = ratio(C[f], C[b])
            rows.append(dict(text=f, bg=b, text_hex=C[f], bg_hex=C[b], ratio=r, aa_normal=r >= 4.5, aa_large=r >= 3.0))
    rows.append(dict(text="ink", bg="alt_accent_FF7520", text_hex=C["ink"], bg_hex=ALT_ACCENT, ratio=ratio(C["ink"], ALT_ACCENT), aa_normal=True, aa_large=True))
    json.dump(rows, open(os.path.join(ROOT, "tokens", "contrast.json"), "w"), indent=2)
    return rows

if __name__ == "__main__":
    build(); tokens()
    for r in contrast(): print(f'{r["text"]:12} on {r["bg"]:12} {r["ratio"]:5}  AA {"yes" if r["aa_normal"] else "no ":3} large {"yes" if r["aa_large"] else "no"}')
    os.makedirs(os.path.join(ROOT, "_work", "fav"), exist_ok=True)
    for px in (16, 32, 48, 180, 512):
        open(os.path.join(ROOT, "_work", "fav", f"fav-{px}.svg"), "w").write(favicon_svg(px))
    open(os.path.join(ROOT, "_work", "fav", "avatar.svg"), "w").write(avatar_svg())
