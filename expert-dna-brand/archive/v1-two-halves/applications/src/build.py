"""Expert DNA applications: HTML sources for PNG renders. Run from this folder."""
import os, math

HERE = os.path.dirname(os.path.abspath(__file__))
INK, PAPER, WHITE = "#101114", "#F4F1EC", "#FFFFFF"
ACC, TINT, DEEP = "#FF5533", "#FFE1D8", "#B32F15"
GREY, GREY_D, LINE, LINE_D = "#66655F", "#A3A29C", "#DCD7CE", "#34383F"
LOGO = "../../logo/svg/"

FONTS = """
@font-face{font-family:'SG';font-weight:400;src:url(../../fonts/SchibstedGrotesk-Regular.ttf)}
@font-face{font-family:'SG';font-weight:500;src:url(../../fonts/SchibstedGrotesk-Medium.ttf)}
@font-face{font-family:'SG';font-weight:700;src:url(../../fonts/SchibstedGrotesk-Bold.ttf)}
@font-face{font-family:'PM';font-weight:400;src:url(../../fonts/IBMPlexMono-Regular.ttf)}
@font-face{font-family:'PM';font-weight:500;src:url(../../fonts/IBMPlexMono-Medium.ttf)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{overflow:hidden}
body{font-family:'SG',Arial,sans-serif;-webkit-font-smoothing:antialiased}
.page{position:relative;overflow:hidden}
.h{font-weight:700;letter-spacing:-0.02em;line-height:1.02}
.lab{font-family:'PM';font-weight:500;text-transform:uppercase;letter-spacing:.12em;display:flex;align-items:center}
.lab i{display:inline-block;flex:none}
.rule{position:absolute;left:0;right:0;height:1px}
.abs{position:absolute}
"""

# Stripe stack: 5 bars, height:gap = 6:4.5, lengths follow the right hemisphere of the mark.
def bar_lengths():
    out = []
    for y in (0, 10.5, 21, 31.5, 42):
        cy = y + 3
        dy = abs(cy - 24)
        out.append(math.sqrt(24 * 24 - dy * dy) / 24)
    return out
LENS = bar_lengths()

def stack(bar_h, max_w, colour, side="right", top=0, edge=0):
    gap = bar_h * 4.5 / 6
    html = []
    for i, f in enumerate(LENS):
        y = top + i * (bar_h + gap)
        w = max_w * f
        pos = f"{side}:{edge}px"
        html.append(f'<div class="abs" style="{pos};top:{y:.1f}px;width:{w:.1f}px;height:{bar_h}px;background:{colour}"></div>')
    return "".join(html)

def stack_height(bar_h):
    return 5 * bar_h + 4 * bar_h * 4.5 / 6

def label(text, size, colour, bar_colour):
    bw = size * 1.5
    return (f'<div class="lab" style="font-size:{size}px;color:{colour};gap:{size * 0.8}px">'
            f'<i style="width:{bw}px;height:{bw / 3}px;background:{bar_colour}"></i>{text}</div>')

def page(name, w, h, bg, body):
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}'
            f'body{{width:{w}px;height:{h}px;background:{bg}}}.page{{width:{w}px;height:{h}px;background:{bg}}}</style></head>'
            f'<body><div class="page">{body}</div></body></html>')
    open(os.path.join(HERE, name + ".html"), "w").write(html)

MARK_LEFT = "M24 0 A24 24 0 0 0 24 48 Z"
MARK_RIGHT = "M30 0 A24 24 0 0 1 30 48 Z"
FOLDS = ["M4 15 C10 18 16 12 24 16", "M3 33 C10 29 16 36 24 31"]
BARS = (0, 10.5, 21, 31.5, 42)

def mark_svg(left, right, px_h, uid, left_clip=1.0, bars_shown=5, bar_shift=0.0, construction=False, folds=True):
    """Inline mark. left_clip: share of left hemisphere revealed from the bottom. bars_shown: bars present.
    bar_shift: fraction of bar width the newest bar is still offset to the right."""
    w = px_h * 54 / 48
    fold = "".join(f'<path d="{d}"/>' for d in FOLDS) if folds else ""
    reveal_y = 48 * (1 - left_clip)
    bars = ""
    for i, y in enumerate(BARS[:bars_shown]):
        dx = 24 * bar_shift if (i == bars_shown - 1 and bar_shift) else 0
        bars += f'<rect x="{30 + dx:.2f}" y="{y}" width="24" height="6"/>'
    cons = ""
    if construction:
        cons = (f'<g fill="none" stroke="{LINE}" stroke-width="0.4">'
                f'<circle cx="27" cy="24" r="24" stroke-dasharray="1.2 1.2"/>'
                f'<line x1="24" y1="-4" x2="24" y2="52"/><line x1="30" y1="-4" x2="30" y2="52"/>'
                f'<line x1="-3" y1="24" x2="57" y2="24"/></g>')
    left_part = ""
    if left_clip > 0:
        left_part = (f'<clipPath id="lc{uid}"><rect x="-2" y="{reveal_y:.2f}" width="30" height="{52:.2f}"/></clipPath>'
                     f'<g clip-path="url(#lc{uid})"><path d="{MARK_LEFT}" fill="{left}" mask="url(#lm{uid})"/></g>')
    return (f'<svg width="{w:.1f}" height="{px_h}" viewBox="-3 -4 60 56" style="overflow:visible">'
            f'<defs><mask id="lm{uid}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="60" height="52">'
            f'<path d="{MARK_LEFT}" fill="#fff"/><g fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">{fold}</g></mask>'
            f'<clipPath id="rc{uid}"><path d="{MARK_RIGHT}"/></clipPath></defs>'
            f'{cons}{left_part}<g clip-path="url(#rc{uid})" fill="{right}">{bars}</g></svg>')

# ---------------- 1. Book cover front, 1800 x 2700 (6 x 9 in at 300 dpi) ----------------
def book_cover():
    W, H = 1800, 2700
    M = 150
    # giant mark cropped off the right edge: left hemisphere paper, stripe stack accent
    big_h = 1500
    body = f'<div class="abs" style="left:{M}px;top:{M}px">{label("The book", 34, GREY_D, ACC)}</div>'
    body += f'<div class="rule" style="top:{M + 90}px;background:{LINE_D}"></div>'
    body += (f'<div class="abs h fit" style="left:{M}px;top:{M + 180}px;width:{W - 2 * M}px;color:{PAPER};font-size:250px;line-height:.95">Expert DNA</div>')
    body += (f'<div class="abs fit" style="left:{M}px;top:{M + 470}px;width:{W - 2 * M}px;color:{PAPER};font-weight:500;font-size:96px;letter-spacing:-0.015em;line-height:1.08">Stay Human,<br>Automate the Rest</div>')
    # illustration from the mark geometry: hemisphere + stack, bleeding right
    mh = 1150; sc = mh / 48
    body += (f'<div class="abs" style="left:{1800 - 47 * sc:.0f}px;top:{980 - 4 * sc:.0f}px">'
             f'{mark_svg(PAPER, ACC, int(mh * 56 / 48), "cov", folds=True)}</div>')
    # footer: rule + author block
    fy = 2290
    body += f'<div class="rule" style="top:{fy}px;background:{LINE_D}"></div>'
    body += (f'<div class="abs" style="left:{M}px;top:{fy + 60}px;color:{PAPER};font-size:64px;font-weight:700;letter-spacing:-0.01em">Donatas Jonikas, PhD</div>')
    body += (f'<div class="abs fit" style="left:{M}px;top:{fy + 160}px;width:1500px;color:{GREY_D};font-family:PM;font-weight:500;font-size:30px;letter-spacing:.04em;line-height:1.45">'
             f'20+ years advising businesses.<br>Amazon bestselling author of Startup Evolution Curve.</div>')
    page("book-cover-front", W, H, INK, body)

# ---------------- 2. Social posts ----------------
def social(name, w, h, bg, fg, sub, logo, accent_bars, lab_colour, lab_bar, headline, second, stack_side=True, hs=84):
    M = 72
    body = f'<div class="abs" style="left:{M}px;top:{M}px">{label("Expert DNA / 01", 22, lab_colour, lab_bar)}</div>'
    body += f'<div class="rule" style="top:{M + 52}px;background:{sub}"></div>'
    body += (f'<div class="abs h fit txt" style="left:{M}px;top:{M + 110}px;width:{w - 2 * M - 40}px;color:{fg};font-size:{hs}px">{headline}</div>')
    if accent_bars:
        bh = 30
        sh = stack_height(bh)
        body += stack(bh, 420, accent_bars, "right", top=h - M - 60 - sh - 70, edge=0)
    body += (f'<div class="abs fit txt" style="left:{M}px;bottom:{M + 110}px;width:{w - 2 * M - 460}px;color:{fg};font-size:40px;font-weight:500;letter-spacing:-0.01em;line-height:1.15">{second}</div>')
    body += f'<div class="rule" style="bottom:{M + 70}px;background:{sub}"></div>'
    body += f'<img class="abs" src="{LOGO}{logo}" style="left:{M}px;bottom:{M - 8}px;height:44px">'
    page(name, w, h, bg, body)

def socials():
    social("social-1080x1080-dark", 1080, 1080, INK, PAPER, LINE_D, "expertdna-horizontal-colour-on-dark.svg",
           ACC, GREY_D, ACC, "Your AI works like a confused intern.", "Give it your Expert DNA.")
    social("social-1080x1350-accent", 1080, 1350, ACC, INK, INK, "expertdna-horizontal-black.svg",
           None, INK, INK, "Your AI works like a confused intern.", "Give it your Expert DNA.", hs=112)
    social("social-1080x1080-light", 1080, 1080, PAPER, INK, LINE, "expertdna-horizontal-colour-on-light.svg",
           ACC, DEEP, ACC, "Your AI works like a confused intern.", "Give it your Expert DNA.")

# ---------------- 3. Ads 1080 x 1350 ----------------
def ad(name, bg, fg, sub, logo, bars, lab_c, lab_bar, btn_bg, btn_fg):
    w, h, M = 1080, 1350, 72
    body = f'<div class="abs" style="left:{M}px;top:{M}px">{label("The book / Expert DNA", 22, lab_c, lab_bar)}</div>'
    body += f'<div class="rule" style="top:{M + 52}px;background:{sub}"></div>'
    body += (f'<div class="abs h fit txt" style="left:{M}px;top:{M + 110}px;width:{w - 2 * M - 40}px;color:{fg};font-size:92px">Stay human.<br>Automate the rest.</div>')
    body += (f'<div class="abs fit txt" style="left:{M}px;top:{M + 360}px;width:600px;color:{fg};font-size:34px;font-weight:400;line-height:1.3">'
             f'Write down what lives in your head. Let AI work from it, not from the internet\'s average.</div>')
    if bars:
        body += stack(34, 480, bars, "right", top=640, edge=0)
    body += (f'<div class="abs txt" style="left:{M}px;bottom:{M + 150}px;display:flex;align-items:center;gap:28px">'
             f'<div style="background:{btn_bg};color:{btn_fg};font-size:34px;font-weight:700;padding:26px 40px;letter-spacing:-0.005em">Get the book, 7 EUR</div>'
             f'<div style="font-family:PM;font-weight:500;font-size:24px;letter-spacing:.06em;color:{fg}">expertdna.net</div></div>')
    body += f'<div class="rule" style="bottom:{M + 70}px;background:{sub}"></div>'
    body += f'<img class="abs" src="{LOGO}{logo}" style="left:{M}px;bottom:{M - 8}px;height:44px">'
    page(name, w, h, bg, body)

def ads():
    ad("ad-1080x1350-dark", INK, PAPER, LINE_D, "expertdna-horizontal-colour-on-dark.svg", ACC, GREY_D, ACC, ACC, INK)
    ad("ad-1080x1350-accent", ACC, INK, INK, "expertdna-horizontal-black.svg", None, INK, INK, INK, ACC)

# ---------------- 4. Email header and footer, 600 px ----------------
def email():
    w = 600
    body = (f'<img class="abs" src="{LOGO}expertdna-horizontal-colour-on-light.svg" style="left:32px;top:38px;height:34px">'
            + stack(7, 120, ACC, "right", top=34, edge=0)
            + f'<div class="rule" style="bottom:0;background:{LINE}"></div>')
    page("email-header-600", w, 110, PAPER, body)
    body = (f'<div class="rule" style="top:0;background:{LINE_D}"></div>'
            f'<img class="abs" src="{LOGO}expertdna-horizontal-colour-on-dark.svg" style="left:32px;top:36px;height:26px">'
            f'<div class="abs" style="left:32px;top:84px;width:536px;color:{GREY_D};font-size:14px;line-height:1.5">'
            f'Stay human. Automate the rest.</div>'
            f'<div class="abs" style="left:32px;top:124px;width:536px;border:1px dashed {LINE_D};padding:10px 12px;color:{GREY_D};font-family:PM;font-size:11px;letter-spacing:.06em;line-height:1.5">'
            f'POSTAL ADDRESS PLACEHOLDER: company name, street, city, country</div>'
            f'<div class="abs" style="left:32px;top:192px;display:flex;gap:24px;font-family:PM;font-weight:500;font-size:11px;letter-spacing:.12em;text-transform:uppercase">'
            f'<span style="color:{PAPER};text-decoration:underline;text-underline-offset:3px">Unsubscribe</span>'
            f'<span style="color:{PAPER};text-decoration:underline;text-underline-offset:3px">expertdna.net</span></div>')
    page("email-footer-600", w, 236, INK, body)

# ---------------- 5. Link preview 1200 x 630 ----------------
def link_preview():
    w, h, M = 1200, 630, 64
    body = f'<div class="abs" style="left:{M}px;top:{M}px">{label("expertdna.net", 20, GREY_D, ACC)}</div>'
    body += f'<div class="rule" style="top:{M + 48}px;background:{LINE_D}"></div>'
    body += f'<div class="abs h fit txt" style="left:{M}px;top:{M + 110}px;width:780px;color:{PAPER};font-size:84px">Stay human.<br>Automate the rest.</div>'
    body += stack(30, 320, ACC, "right", top=190, edge=0)
    body += f'<div class="rule" style="bottom:{M + 74}px;background:{LINE_D}"></div>'
    body += f'<img class="abs" src="{LOGO}expertdna-horizontal-colour-on-dark.svg" style="left:{M}px;bottom:{M - 4}px;height:44px">'
    page("link-preview-1200x630", w, h, INK, body)

# ---------------- 6. Motion storyboard ----------------
def storyboard():
    frames = [
        dict(t="0.0 s", c="Construction: two half circles, one gap", kw=dict(left_clip=0, bars_shown=0, construction=True)),
        dict(t="0.3 s", c="Left hemisphere fills from the base", kw=dict(left_clip=0.55, bars_shown=0, construction=True)),
        dict(t="0.6 s", c="Left hemisphere complete, folds cut in", kw=dict(left_clip=1, bars_shown=0)),
        dict(t="0.8 s", c="Written lines slide in from the right", kw=dict(left_clip=1, bars_shown=2, bar_shift=0.5)),
        dict(t="1.1 s", c="Last line lands", kw=dict(left_clip=1, bars_shown=5, bar_shift=0.35)),
        dict(t="1.4 s", c="Rest: final mark", kw=dict(left_clip=1, bars_shown=5)),
    ]
    W, M = 2400, 64
    fw = (W - 2 * M - 5 * 24) / 6
    body = f'<div class="abs" style="left:{M}px;top:{M}px">{label("Expert DNA / Motion idea / Proposal", 20, DEEP, ACC)}</div>'
    body += f'<div class="abs h" style="left:{M}px;top:{M + 50}px;color:{INK};font-size:56px">The mark builds in 1.4 seconds</div>'
    body += f'<div class="rule" style="top:{M + 150}px;background:{LINE}"></div>'
    for i, f in enumerate(frames):
        x = M + i * (fw + 24)
        body += (f'<div class="abs" style="left:{x:.0f}px;top:{M + 190}px;width:{fw:.0f}px;height:{fw:.0f}px;background:{WHITE};display:flex;align-items:center;justify-content:center">'
                 f'{mark_svg(INK, ACC, int(fw * 0.5), f"sb{i}", **f["kw"])}</div>')
        body += (f'<div class="abs" style="left:{x:.0f}px;top:{M + 210 + fw:.0f}px;width:{fw:.0f}px;font-family:PM;font-weight:500;font-size:16px;letter-spacing:.08em;color:{INK};line-height:1.5">'
                 f'<span style="color:{DEEP}">{i + 1:02d} / {f["t"]}</span><br><span style="text-transform:none;letter-spacing:.02em;font-weight:400">{f["c"]}</span></div>')
    page("motion-storyboard", W, int(M + 190 + fw + 140), PAPER, body)

if __name__ == "__main__":
    book_cover(); socials(); ads(); email(); link_preview(); storyboard()
    print("html written")
