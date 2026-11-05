"""Product mockup sample: Plugin 03 Proposal, 5 scenes, 2400x1600. Realistic product mockups (devices, box, course, bundle)."""
import os
D = os.path.dirname(os.path.abspath(__file__))
F = "../../fonts"
ACC, INK = "#FF5533", "#101114"

CSS = f"""
@font-face{{font-family:HK;font-weight:400;src:url({F}/HankenGrotesk-Regular.ttf)}}
@font-face{{font-family:HK;font-weight:500;src:url({F}/HankenGrotesk-Medium.ttf)}}
@font-face{{font-family:HK;font-weight:700;src:url({F}/HankenGrotesk-Bold.ttf)}}
@font-face{{font-family:PM;src:url({F}/IBMPlexMono-Medium.ttf)}}
*{{margin:0;box-sizing:border-box}}
body{{width:2400px;height:1600px;overflow:hidden;font-family:HK;color:{INK};position:relative}}
.mono{{font-family:PM;letter-spacing:.12em;text-transform:uppercase}}
/* ---------- app screen: proposal plugin ---------- */
.app{{width:100%;height:100%;background:#fff;display:grid;grid-template-columns:23% 1fr;font-size:15px}}
.side{{background:#F4F3F0;border-right:1px solid #E2E0DB;padding:26px 20px}}
.side .t{{font:11px PM;letter-spacing:.12em;color:#66655F;margin:22px 0 10px}}
.side .i{{padding:10px 12px;font-size:14px;color:#333;display:flex;justify-content:space-between}}
.side .i.on{{background:#fff;border-left:3px solid {ACC};font-weight:500}}
.side .tag{{font:10px PM;color:#B32F15}}
.doc{{padding:34px 46px;overflow:hidden}}
.doc .top{{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #E2E0DB;padding-bottom:16px}}
.doc .btn{{background:{ACC};color:{INK};font-weight:500;padding:9px 16px;font-size:13px}}
.doc .st{{font:11px PM;letter-spacing:.12em;color:#B32F15}}
.doc h3{{font-weight:500;font-size:30px;letter-spacing:-.02em;margin:22px 0 6px}}
.doc h4{{font-weight:500;font-size:17px;margin:18px 0 6px}}
.doc p{{font-size:14px;line-height:1.55;color:#3A3B3F;max-width:620px}}
.doc .hl{{background:#FFE1D8}}
.doc .src{{font:10px PM;color:#66655F;letter-spacing:.08em;margin-top:4px}}
/* ---------- devices ---------- */
.laptop{{position:absolute}}
.laptop .lid{{background:#1B1C20;border-radius:22px 22px 0 0;padding:22px 22px 30px;box-shadow:0 1px 0 #2a2b30 inset}}
.laptop .screen{{overflow:hidden;background:#fff;border-radius:4px}}
.laptop .base{{height:30px;background:linear-gradient(#D9D8D4,#BDBCB7);border-radius:0 0 26px 26px;margin:0 -70px;position:relative}}
.laptop .base:before{{content:'';position:absolute;left:50%;top:0;width:220px;height:10px;margin-left:-110px;background:#A9A8A3;border-radius:0 0 10px 10px}}
.phone{{position:absolute;background:#1B1C20;border-radius:56px;padding:16px}}
.phone .screen{{border-radius:42px;overflow:hidden;background:#fff;height:100%}}
.tablet{{position:absolute;background:#1B1C20;border-radius:40px;padding:24px}}
.tablet .screen{{border-radius:18px;overflow:hidden;background:#fff;height:100%}}
.shadow{{box-shadow:0 60px 90px -30px rgba(16,17,20,.35),0 24px 40px -20px rgba(16,17,20,.25)}}
.floor{{position:absolute;border-radius:50%;background:radial-gradient(rgba(16,17,20,.28),rgba(16,17,20,0) 70%)}}
"""

def app_screen(scale=1.0):
    return f"""<div class="app" style="zoom:{scale}">
<div class="side"><div style="display:flex;align-items:center;gap:10px"><svg width="34" height="30" viewBox="0 0 54 48"><path d="M24 0 A24 24 0 0 0 24 48 Z" fill="{INK}"/><rect x="30" width="3.5" height="48" fill="{ACC}"/><rect x="38" y="14" width="16" height="3.5" fill="{ACC}"/><rect x="38" y="30.5" width="11" height="3.5" fill="{ACC}"/></svg><b style="font-weight:500">Proposal</b></div>
<div class="t">Your files</div><div class="i">offers-and-prices.md</div><div class="i">ideal-client.md</div><div class="i">method.md</div><div class="i">voice.md</div>
<div class="t">This call</div><div class="i">call-notes.md <span class="tag">NEW</span></div><div class="i on">proposal-draft.md <span class="tag">READY</span></div></div>
<div class="doc"><div class="top"><span class="st">DRAFT FOR {{CLIENT NAME}}</span><span class="btn">Send for review</span></div>
<h3>Proposal for {{Client name}}</h3><div class="src">BUILT FROM: CALL-NOTES.MD, OFFERS-AND-PRICES.MD, VOICE.MD</div>
<h4>Where you are now</h4><p>You told me the work keeps landing on your desk. Every request, every follow-up, every decision still goes through you, and that is what we will change first.</p>
<h4>What we will do together</h4><p>We start with your method, write it down in your words, and turn it into steps your team and your tools can follow. <span class="hl">You keep the parts only you can do.</span></p>
<h4>Investment</h4><p>{{Offer name}}: {{price}}. Starts {{date}}.</p>
<h4>Next step</h4><p>Reply to this proposal and we book the first session.</p></div></div>"""

def page(body, bg="#fff"):
    return f'<!doctype html><meta charset=utf-8><style>{CSS}</style><body style="background:{bg}">{body}</body>'

def headline(label, h, sub, x=120, y=150, w=760, dark=False):
    c = "#fff" if dark else INK; s = "#A3A29C" if dark else "#66655F"; l = ACC if dark else "#B32F15"
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px">'
            f'<div class="mono" style="font-size:18px;color:{l}">{label}</div>'
            f'<div style="font-weight:500;font-size:96px;line-height:1.02;letter-spacing:-.03em;color:{c};margin-top:28px">{h}</div>'
            f'<div style="font-size:30px;line-height:1.45;color:{s};margin-top:34px">{sub}</div></div>')

scenes = {}

# M1: laptop hero, angled
scenes["m1-laptop"] = page(
    headline("Plugin 03 / Proposal", "The proposal you don't have to write.", "From your call notes to a proposal in your words, ready to review.") +
    f'''<div class="floor" style="left:1010px;top:1420px;width:1300px;height:90px"></div>
<div class="laptop" style="left:1020px;top:260px;width:1280px;transform:perspective(2600px) rotateY(-14deg) rotateX(3deg)">
<div class="lid shadow"><div class="screen" style="height:740px">{app_screen(1.18)}</div></div><div class="base"></div></div>''', "#F4F3F0")

# M2: device trio
mobile = f"""<div style="padding:70px 34px 30px;font-size:22px"><div class="mono" style="font-size:13px;color:#B32F15">Proposal ready</div>
<div style="font-weight:500;font-size:40px;letter-spacing:-.02em;line-height:1.08;margin-top:16px">Proposal for {{Client name}}</div>
<div style="margin-top:26px;font-size:20px;line-height:1.5;color:#3A3B3F">Built from your call notes, your offers and your voice.</div>
<div style="margin-top:34px;background:{ACC};padding:20px;font-weight:500;text-align:center">Review draft</div>
<div style="margin-top:16px;border:2px solid {INK};padding:18px;font-weight:500;text-align:center">Edit in your words</div></div>"""
scenes["m2-devices"] = page(
    f'''<div style="position:absolute;left:0;right:0;top:110px;text-align:center"><div class="mono" style="font-size:18px;color:#B32F15">Plugin 03 / Proposal</div>
<div style="font-weight:500;font-size:84px;letter-spacing:-.03em;margin-top:22px">Works where you work.</div></div>
<div class="floor" style="left:330px;top:1450px;width:1740px;height:90px"></div>
<div class="laptop" style="left:560px;top:420px;width:1280px"><div class="lid shadow"><div class="screen" style="height:740px">{app_screen(1.18)}</div></div><div class="base"></div></div>
<div class="tablet shadow" style="left:200px;top:640px;width:560px;height:780px"><div class="screen">{app_screen(0.62)}</div></div>
<div class="phone shadow" style="left:1700px;top:600px;width:420px;height:860px"><div class="screen">{mobile}</div></div>''', "#FFFFFF")

# M3: product box (modern software box) with 3D faces
box_front = f"""<div style="position:absolute;inset:0;background:{INK};color:#fff;padding:70px 60px;display:flex;flex-direction:column;justify-content:space-between">
<div class="mono" style="font-size:20px;color:{ACC}">Plugin 03</div>
<div><div style="width:150px;height:300px;border-radius:150px 0 0 150px;background:#fff;margin-bottom:60px"></div>
<div style="font-weight:500;font-size:110px;letter-spacing:-.03em;line-height:1">Proposal</div>
<div style="font-size:30px;color:#A3A29C;margin-top:20px;line-height:1.35">The proposal you don't have to write.</div></div>
<div style="display:flex;gap:16px;align-items:center"><div style="height:10px;width:120px;background:{ACC}"></div><div class="mono" style="font-size:16px;color:#A3A29C">Plugin + mini course</div></div></div>"""
scenes["m3-box"] = page(
    headline("What you get", "A plugin and a mini course.", "Install it once. Every call ends with a proposal draft in your words.", x=120, y=200, w=820) +
    f'''<div class="floor" style="left:1180px;top:1380px;width:1000px;height:110px"></div>
<div style="position:absolute;left:1300px;top:170px;width:720px;height:1060px;transform-style:preserve-3d;transform:perspective(3000px) rotateY(-28deg) rotateX(4deg)">
<div class="shadow" style="position:absolute;inset:0;transform:translateZ(80px)">{box_front}</div>
<div style="position:absolute;top:0;bottom:0;left:-80px;width:160px;background:{ACC};transform:rotateY(-90deg) translateZ(0px);transform-origin:right"></div>
<div style="position:absolute;left:0;right:0;top:-80px;height:160px;background:#2A2B30;transform:rotateX(90deg);transform-origin:bottom"></div></div>''', "#F4F3F0")

# M4: mini course: video player + lesson list + workbook page
lessons = ["Write your offer file", "Turn call notes into a draft", "Check the draft in your voice", "Send, follow up, close"]
lesson_html = "".join(f'<div style="display:flex;gap:22px;padding:22px 0;border-bottom:1px solid #2E3036;font-size:26px"><span class="mono" style="font-size:16px;color:{ACC};padding-top:6px">0{i+1}</span><span>{l}</span></div>' for i, l in enumerate(lessons))
scenes["m4-course"] = page(
    f'''<div style="position:absolute;left:120px;top:150px;width:900px"><div class="mono" style="font-size:18px;color:{ACC}">Mini course included</div>
<div style="font-weight:500;font-size:92px;line-height:1.02;letter-spacing:-.03em;color:#fff;margin-top:28px">Learn it in one sitting.</div>
<div style="margin-top:60px;color:#fff;max-width:760px">{lesson_html}</div></div>
<div class="shadow" style="position:absolute;left:1160px;top:220px;width:1120px;height:700px;background:#1A1B1F;border:1px solid #2E3036">
<div style="position:absolute;inset:0;background:#F4F3F0;overflow:hidden"><div style="position:absolute;left:-120px;top:120px;width:460px;height:460px;border-radius:50%;background:{INK}"></div>
<div style="position:absolute;left:420px;top:150px"><div class="mono" style="font-size:16px;color:#B32F15">Lesson 02</div><div style="font-weight:500;font-size:58px;letter-spacing:-.02em;margin-top:16px;width:560px;line-height:1.05">Turn call notes into a draft</div></div>
<div style="position:absolute;left:500px;top:420px;width:120px;height:120px;border-radius:50%;background:{ACC}"><div style="position:absolute;left:48px;top:34px;border-left:40px solid {INK};border-top:26px solid transparent;border-bottom:26px solid transparent"></div></div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:56px;background:rgba(16,17,20,.85);display:flex;align-items:center;padding:0 24px;gap:18px"><div style="width:40%;height:6px;background:{ACC}"></div><div style="flex:1;height:6px;background:#3A3B40"></div><span class="mono" style="color:#A3A29C;font-size:13px">06:12</span></div></div>
<div class="shadow" style="position:absolute;left:1580px;top:820px;width:620px;height:700px;background:#fff;transform:rotate(4deg);padding:56px 50px">
<div class="mono" style="font-size:14px;color:#B32F15">Worksheet</div><div style="font-weight:500;font-size:40px;letter-spacing:-.02em;margin-top:14px">Your offer file</div>
{''.join(f'<div class="mono" style="font-size:12px;color:#66655F;margin-top:34px">{t}</div><div style="border-bottom:2px solid #E2E0DB;height:46px"></div>' for t in ["Offer name","Price","Who it is for","What the client gets"])}</div>''', INK)

# M5: bundle stack: everything you get
scenes["m5-stack"] = page(
    f'''<div style="position:absolute;left:0;right:0;top:100px;text-align:center"><div class="mono" style="font-size:18px;color:#B32F15">Everything inside Plugin 03</div>
<div style="font-weight:500;font-size:84px;letter-spacing:-.03em;margin-top:22px">Plugin. Mini course. Worksheets.</div></div>
<div class="floor" style="left:300px;top:1460px;width:1800px;height:100px"></div>
<div class="laptop" style="left:720px;top:470px;width:1100px"><div class="lid shadow"><div class="screen" style="height:640px">{app_screen(1.02)}</div></div><div class="base"></div></div>
<div class="shadow" style="position:absolute;left:250px;top:560px;width:560px;height:820px;transform:perspective(2400px) rotateY(18deg);">{box_front.replace("110px","84px").replace("padding:70px 60px","padding:56px 48px").replace("width:150px;height:300px;border-radius:150px","width:110px;height:220px;border-radius:110px")}</div>
<div class="shadow" style="position:absolute;left:1700px;top:700px;width:470px;height:640px;background:#fff;transform:rotate(5deg);padding:46px 40px">
<div class="mono" style="font-size:13px;color:#B32F15">Worksheet</div><div style="font-weight:500;font-size:34px;letter-spacing:-.02em;margin-top:12px">Your offer file</div>
{''.join(f'<div class="mono" style="font-size:11px;color:#66655F;margin-top:30px">{t}</div><div style="border-bottom:2px solid #E2E0DB;height:40px"></div>' for t in ["Offer name","Price","Who it is for"])}</div>''', "#FFFFFF")

os.makedirs(os.path.join(D, "html"), exist_ok=True)
for k, v in scenes.items():
    open(os.path.join(D, "html", f"proposal-{k}.html"), "w").write(v)
print(list(scenes))
