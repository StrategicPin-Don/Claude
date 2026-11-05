"""Overview sheets: overview-by-style.png (rows = products, cols = styles) + per-style review montages."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
OUT = "/home/user/Claude/expert-dna-brand/product-visuals"
F = "/home/user/Claude/expert-dna-brand/fonts"
prods = json.load(open(os.path.join(OUT, "src", "products.json")))
styles = [("s1", "interface", "S1 Interface"), ("s2", "statement", "S2 Statement"), ("s3", "inside", "S3 What's inside"),
          ("s4", "before-after", "S4 Before / After"), ("s5", "plug-in", "S5 Plug-in")]
TW, TH, LW, G, HH = 480, 320, 300, 12, 70
W = LW + len(styles) * (TW + G) + G
Hh = HH + len(prods) * (TH + G) + G
img = Image.new("RGB", (W, Hh), "#FFFFFF"); d = ImageDraw.Draw(img)
mono = ImageFont.truetype(os.path.join(F, "IBMPlexMono-Medium.ttf"), 18)
sans = ImageFont.truetype(os.path.join(F, "HankenGrotesk-Medium.ttf"), 24)
for j, (_, _, t) in enumerate(styles): d.text((LW + G + j * (TW + G), 26), t.upper(), font=mono, fill="#101114")
for i, p in enumerate(prods):
    y = HH + G + i * (TH + G)
    d.text((24, y + TH / 2 - 14), p["name"], font=sans, fill="#101114")
    for j, (sid, sn, _) in enumerate(styles):
        f = os.path.join(OUT, p["slug"], f'{p["slug"]}-{sid}-{sn}.png')
        im = Image.open(f).convert("RGB").resize((TW, TH), Image.LANCZOS)
        img.paste(im, (LW + G + j * (TW + G), y))
img.save(os.path.join(OUT, "overview-by-style.png"))
if len(sys.argv) > 1:  # review montage for one style
    sid = sys.argv[1]; sn = dict((a, b) for a, b, _ in styles)[sid]
    tw, th = 780, 520; cols = 3; rows = (len(prods) + cols - 1) // cols
    m = Image.new("RGB", (cols * (tw + 10), rows * (th + 10)), "#888")
    for k, p in enumerate(prods):
        im = Image.open(os.path.join(OUT, p["slug"], f'{p["slug"]}-{sid}-{sn}.png')).convert("RGB").resize((tw, th), Image.LANCZOS)
        m.paste(im, ((k % cols) * (tw + 10), (k // cols) * (th + 10)))
    m.save(f"/tmp/claude-0/-home-user-Claude/9ba0c0d8-f349-555d-86b5-8557e92552f7/scratchpad/review-{sid}.png")
print("ok")
