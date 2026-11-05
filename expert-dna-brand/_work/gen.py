"""Phase 1 generator: Expert DNA logo directions + contact sheet HTML."""
import os, itertools
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import RecordingPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "_work")
OUT = os.path.join(ROOT, "phase1")
os.makedirs(OUT, exist_ok=True)

INK = "#101114"; PAPER = "#F4F1EC"; WHITE = "#FFFFFF"; ACC = "#FF7520"
_uid = itertools.count()
def uid(p): return f"{p}{next(_uid)}"

# ---------- wordmark outlining ----------
FONT = TTFont(os.path.join(WORK, "fonts", "Schibsted_Grotesk_wght_700.ttf"))
GS = FONT.getGlyphSet(); CMAP = FONT.getBestCmap(); UPM = FONT["head"].unitsPerEm
CAP = FONT["OS/2"].sCapHeight or 700
TRACK = -0.01 * UPM

def text_glyphs(text):
    x = 0; out = []
    for ch in text:
        g = CMAP[ord(ch)]
        out.append((g, x))
        x += GS[g].width + TRACK
    return out, x - TRACK

def glyph_path(g, x, s, bx, by):
    pen = SVGPathPen(GS)
    GS[g].draw(TransformPen(pen, (s, 0, 0, -s, bx + x * s, by)))
    return pen.getCommands()

def glyph_contours(g, x, s, bx, by):
    rec = RecordingPen(); GS[g].draw(rec)
    contours, cur = [], []
    for op, args in rec.value:
        cur.append((op, args))
        if op in ("closePath", "endPath"):
            contours.append(cur); cur = []
    res = []
    for c in contours:
        pen = SVGPathPen(GS); tp = TransformPen(pen, (s, 0, 0, -s, bx + x * s, by))
        xs = []; ys = []
        for op, args in c:
            getattr(tp, op)(*args)
            for pt in args:
                xs.append(bx + (x + pt[0]) * s); ys.append(by - pt[1] * s)
        res.append((pen.getCommands(), (min(xs), min(ys), max(xs), max(ys))))
    return res

def wordmark(cap_px, color, x0=0, baseline=None, dna_counter=None):
    """Return (svg, width). cap_px = cap height in px. dna_counter = (accent, fold_color) for direction 5."""
    s = cap_px / CAP
    by = baseline if baseline is not None else cap_px
    gl, w = text_glyphs("Expert DNA")
    parts = []
    for i, (g, x) in enumerate(gl):
        if dna_counter and g == CMAP[ord("D")]:
            acc, fold = dna_counter
            cs = glyph_contours(g, x, s, x0, by)
            cs.sort(key=lambda c: (c[1][2]-c[1][0])*(c[1][3]-c[1][1]))
            inner_d, (ix0, iy0, ix1, iy1) = cs[0]
            cid = uid("dc")
            parts.append(f'<path d="{glyph_path(g, x, s, x0, by)}" fill="{color}"/>')
            parts.append(f'<clipPath id="{cid}"><path d="{inner_d}"/></clipPath>')
            if acc != color: parts.append(f'<path d="{inner_d}" fill="{acc}"/>')
            else: fold = color
            w_, h_ = ix1 - ix0, iy1 - iy0
            sw = max(h_ * 0.11, 1)
            fd = (f"M{ix0 - 1:.2f} {iy0 + h_*0.38:.2f} "
                  f"C{ix0 + w_*0.45:.2f} {iy0 + h_*0.18:.2f} {ix0 + w_*0.55:.2f} {iy0 + h_*0.62:.2f} {ix1 + 1:.2f} {iy0 + h_*0.48:.2f}")
            parts.append(f'<g clip-path="url(#{cid})"><path d="{fd}" fill="none" stroke="{fold}" stroke-width="{sw:.2f}"/></g>')
        else:
            parts.append(f'<path d="{glyph_path(g, x, s, x0, by)}" fill="{color}"/>')
    return "".join(parts), w * s

# ---------- marks (viewBox 0 0 64 64) ----------
def m_folds(fg, ac):
    mid = uid("m")
    circles = [(24, 31, 16), (38, 22, 14), (48, 34, 12), (34, 41, 12)]
    c = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in circles)
    cuts = ('<path d="M37 7 C33 17 41 22 34 33" />'
            '<path d="M10 39 C20 35 30 43 46 33" />'
            '<path d="M52 23 C51 29 55 33 62 33" />')
    return (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64">'
            f'<g fill="#fff">{c}</g><g fill="none" stroke="#000" stroke-width="3.4" stroke-linecap="round">{cuts}</g></mask>'
            f'<g mask="url(#{mid})" fill="{fg}">{c}</g>'
            f'<circle cx="24" cy="31" r="5" fill="{ac}" mask="url(#{mid})"/>')

def m_halves(fg, ac):
    mid, cid = uid("m"), uid("c")
    left = "M29 8 C15 8 5 19 5 32 C5 45 15 56 29 56 Z"
    right = "M35 8 C49 8 59 19 59 32 C59 45 49 56 35 56 Z"
    dots = "".join(f'<rect x="35" y="{y}" width="26" height="5"/>' for y in (13, 22.5, 32, 41.5, 51))
    return (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><path d="{left}" fill="#fff"/>'
            f'<g fill="none" stroke="#000" stroke-width="3.2" stroke-linecap="round">'
            f'<path d="M9 23 C15 26 21 20 29 24"/><path d="M8 41 C15 37 21 44 29 39"/></g></mask>'
            f'<path d="{left}" fill="{fg}" mask="url(#{mid})"/>'
            f'<clipPath id="{cid}"><path d="{right}"/></clipPath>'
            f'<g clip-path="url(#{cid})" fill="{ac}">{dots}</g>'
            '')

def m_efold(fg, ac):
    d = ("M54 10 H22 A8 8 0 0 0 14 18 V20 A7 7 0 0 0 21 27 H42 A6 6 0 0 1 42 39 H21 "
         "A7 7 0 0 0 14 46 V46 A8 8 0 0 0 22 54 H54")
    return (f'<path d="{d}" fill="none" stroke="{fg}" stroke-width="7.5" stroke-linejoin="round"/>'
            f'<path d="M42 27 A6 6 0 0 1 42 39" fill="none" stroke="{ac}" stroke-width="7.5"/>')

def m_vessel(fg, ac):
    mid = uid("m")
    outer = [(25, 31, 18), (39, 22, 15), (47, 36, 13), (33, 43, 13)]
    inner = [(x, y, r - 5) for x, y, r in outer]
    co = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in outer)
    ci = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in inner)
    return (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><g fill="#fff">{co}</g><g fill="#000">{ci}</g></mask>'
            f'<g mask="url(#{mid})"><rect width="64" height="64" fill="{fg}"/></g>'
            f'<path d="M24 33 C28 26 34 38 40 30" fill="none" stroke="{ac}" stroke-width="6" stroke-linecap="round"/>')

def m_wordfirst(fg, ac):
    # mark for direction 5 = the D with fold counter, isolated
    s = 52 / CAP
    g = CMAP[ord("D")]
    gw = GS[g].width * s
    svg, _ = "", 0
    x0 = (64 - gw) / 2
    cs = glyph_contours(g, 0, s, x0, 58)
    cs.sort(key=lambda c: (c[1][2]-c[1][0])*(c[1][3]-c[1][1]))
    inner_d, (ix0, iy0, ix1, iy1) = cs[0]
    cid = uid("dc"); w_, h_ = ix1 - ix0, iy1 - iy0
    fd = (f"M{ix0 - 1:.2f} {iy0 + h_*0.38:.2f} C{ix0 + w_*0.45:.2f} {iy0 + h_*0.18:.2f} "
          f"{ix0 + w_*0.55:.2f} {iy0 + h_*0.62:.2f} {ix1 + 1:.2f} {iy0 + h_*0.48:.2f}")
    return (f'<path d="{glyph_path(g, 0, s, x0, 58)}" fill="{fg}"/>'
            f'<clipPath id="{cid}"><path d="{inner_d}"/></clipPath>' + (f'<path d="{inner_d}" fill="{ac}"/>' if ac != fg else '') + \
            f'<g clip-path="url(#{cid})"><path d="{fd}" fill="none" stroke="{fg}" stroke-width="{h_*0.11:.2f}"/></g>')

def m_fissure(fg, ac):
    cid = uid("c")
    fold = "M33 0 C21 14 45 22 32 32 C19 42 43 50 31 64"
    mid = uid("m")
    return (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/>'
            f'<path d="{fold}" fill="none" stroke="#000" stroke-width="3.2"/></mask><g mask="url(#{mid})">'
            f'<rect x="4" y="4" width="56" height="56" fill="{ac}"/>'
            f'<clipPath id="{cid}"><path d="M0 0 H33 C21 14 45 22 32 32 C19 42 43 50 31 64 H0 Z"/></clipPath>'
            f'<rect x="4" y="4" width="56" height="56" fill="{fg}" clip-path="url(#{cid})"/></g>')

DIRS = [
    dict(key="d1-folds", name="01 Folds", fn=m_folds,
         why="A brain profile built from four lobe circles on a grid, with three cut folds; the orange core marks the expert's own judgement.",
         risk="Could read as a cloud or a generic brain-health clinic logo; cut folds must stay thick to survive small sizes."),
    dict(key="d2-halves", name="02 Two halves", fn=m_halves,
         why="Frontal view: the left hemisphere is solid and human, the right is drawn as lines of written text, the expert's files handed to AI. It draws 'stay human, automate the rest'.",
         risk="Half solid, half striped brains exist in AI and edtech branding; stripes merge into a tint at 16 px but the silhouette holds."),
    dict(key="d3-efold", name="03 E fold", fn=m_efold,
         why="One continuous line draws the letter E; the middle arm folds back on itself like a cortex fold. The orange hairpin is the expert's thinking.",
         risk="May read as a paperclip, a cable, or a generic 'E' tech monogram if the fold is not visible."),
    dict(key="d4-vessel", name="04 Vessel", fn=m_vessel,
         why="A brain outline holds one orange fold inside: the knowledge the expert carries, captured and contained.",
         risk="Outline brains are common in health and coaching logos; inner stroke is thin at small sizes."),
    dict(key="d5-wordfirst", name="05 Wordmark first", fn=m_wordfirst, wordfirst=True,
         why="The counter of the D is a hemisphere with one fold. The name carries the idea; the D alone becomes the favicon.",
         risk="Low confusion risk; the brain reading is subtle and relies on the orange counter."),
    dict(key="d6-fissure", name="06 Fissure (own)", fn=m_fissure,
         why="A square field split by one fold line, like the line between the hemispheres: one side human, one side handed over. The fold line becomes the brand's rule motif.",
         risk="Abstract; could be read as a flag or a generic two-tone tile without the brand context."),
]

def svg(inner, w, h, vb=None, bg=None):
    vb = vb or f"0 0 {w} {h}"
    b = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{vb}">{b}{inner}</svg>'

def mark_svg(d, px, fg, ac, bg=None):
    return svg(f'<g>{d["fn"](fg, ac)}</g>', px, px, "0 0 64 64", bg)

def lockup_svg(d, cap, fg, ac, word=None, bg=None, pad=0):
    word = word or fg
    if d.get("wordfirst"):
        wm, w = wordmark(cap, word, pad, cap + pad, dna_counter=(ac, word))
        return svg(wm, int(w + 2 * pad), int(cap * 1.32 + 2 * pad), None, bg)
    mk = cap * 1.9
    gap = cap * 0.55
    wm, w = wordmark(cap, word, pad + mk + gap, pad + (mk + cap) / 2)
    m = f'<g transform="translate({pad},{pad}) scale({mk/64})">{d["fn"](fg, ac)}</g>'
    return svg(m + wm, int(pad * 2 + mk + gap + w + 1), int(mk + 2 * pad), None, bg)

# standalone files
for d in DIRS:
    open(os.path.join(OUT, f"{d['key']}-mark.svg"), "w").write(mark_svg(d, 512, INK, ACC))
    open(os.path.join(OUT, f"{d['key']}-lockup-light.svg"), "w").write(lockup_svg(d, 64, INK, ACC, pad=32, bg=PAPER))
    open(os.path.join(OUT, f"{d['key']}-lockup-dark.svg"), "w").write(lockup_svg(d, 64, PAPER, ACC, pad=32, bg=INK))

# ---------- contact sheet ----------
def cell(label, content, bg, fg):
    return (f'<div class="cell" style="background:{bg};color:{fg}"><div class="lab">{label}</div>'
            f'<div class="ct">{content}</div></div>')

rows = []
for d in DIRS:
    for mode in ("light", "dark"):
        bg, fg = (PAPER, INK) if mode == "light" else (INK, PAPER)
        cells = [
            cell("MARK", mark_svg(d, 150, fg, ACC), bg, fg),
            cell("LOCKUP", lockup_svg(d, 40, fg, ACC), bg, fg),
            cell("64 / 32 / 16 PX", mark_svg(d, 64, fg, ACC) + mark_svg(d, 32, fg, ACC) + mark_svg(d, 16, fg, ACC), bg, fg),
        ]
        if mode == "light":
            cells += [
                cell("BLACK ONLY", mark_svg(d, 96, INK, INK), WHITE, INK),
                cell("WHITE ON BLACK", mark_svg(d, 96, WHITE, WHITE), "#000", WHITE),
                cell("ON ACCENT", mark_svg(d, 96, INK, WHITE), ACC, INK),
                cell("SQUINT", f'<div style="filter:blur(3px)">{mark_svg(d, 96, INK, ACC)}</div>', bg, fg),
            ]
        else:
            cells += [
                cell("LOCKUP 120 PX WIDE", f'<div class="w120">{lockup_svg(d, 40, fg, ACC)}</div>', bg, fg),
                cell("SQUINT", f'<div style="filter:blur(3px)">{mark_svg(d, 96, fg, ACC)}</div>', bg, fg),
            ]
        head = (f'<div class="head" style="background:{bg};color:{fg}"><div class="lab">{d["name"].upper()}</div>'
                + (f'<p>{d["why"]}</p><p class="risk">Confusion risk: {d["risk"]}</p>' if mode == "light" else "<p></p>")
                + '</div>')
        rows.append(f'<section class="row {mode}">{head}{"".join(cells)}</section>')

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:SG;src:url(fonts/Schibsted_Grotesk_wght_500.ttf)}}
@font-face{{font-family:JM;src:url(fonts/JetBrains_Mono_wght_500.ttf)}}
*{{box-sizing:border-box;margin:0}} body{{width:2400px;background:{PAPER};font-family:SG;color:{INK}}}
header{{padding:56px 64px 40px;border-bottom:1px solid {INK}}}
header .lab{{font-family:JM;font-size:15px;letter-spacing:.12em;color:{ACC}}}
header h1{{font-size:56px;margin-top:12px;font-weight:500}} header p{{font-size:20px;margin-top:12px;max-width:1500px}}
.row{{display:flex;border-bottom:1px solid rgba(128,128,128,.35)}}
.head{{width:420px;padding:28px 32px;flex:none}} .head p{{font-size:16px;line-height:1.45;margin-top:12px}} .head .risk{{opacity:.7}}
.lab{{font-family:JM;font-size:12px;letter-spacing:.12em}}
.cell{{flex:1;padding:20px 22px;min-width:0;border-left:1px solid rgba(128,128,128,.25)}}
.ct{{display:flex;align-items:center;gap:18px;margin-top:16px;min-height:150px}}
.w120 svg{{width:120px;height:auto}}
.cell:nth-child(3) {{flex:2.2}}
</style></head><body>
<header><div class="lab">EXPERT DNA / PHASE 1 / LOGO DIRECTIONS</div>
<h1>Six directions, tested at 16 to 150 px, light and dark</h1>
<p>Wordmark in Schibsted Grotesk Bold as a provisional typeface (final choice in Phase 2). Accent is StrategicPin orange #FF7520 as a placeholder; Phase 2 tests a shifted accent. All text is outlined.</p></header>
{''.join(rows)}<footer style="padding:48px 64px 64px;display:flex;gap:64px">
<div style="flex:1"><div class="lab" style="color:#FF7520">FINALISTS, RANKED</div>
<p style="font-size:22px;line-height:1.5;margin-top:16px"><b>1. 02 Two halves.</b> The only mark that draws the promise itself, keeps its silhouette at 16 px, and is a frontal flat brain, so it sits next to the StrategicPin side-view node brain as a relative, not a twin.<br>
<b>2. 03 E fold.</b> The strongest favicon and the most ownable shape; the brain reading is weaker and needs the story.<br>
<b>3. 05 Wordmark first.</b> Calm and premium, but the idea is subtle; best used as a detail inside the wordmark of the winner.</p></div>
<div style="flex:1"><div class="lab" style="color:#FF7520">DISCARDED</div>
<p style="font-size:22px;line-height:1.5;margin-top:16px"><b>01 Folds:</b> reads as a cloud or a creature (the orange dot looks like an eye) and repeats the StrategicPin side-view brain.<br>
<b>04 Vessel:</b> reads as a cloud or popcorn; the inner fold disappears at 16 px.<br>
<b>06 Fissure:</b> fails as a brain without explanation; its fold line is kept as a candidate for the brand rule motif.</p></div></footer></body></html>"""
open(os.path.join(WORK, "sheet.html"), "w").write(html)
print("ok", len(DIRS))
