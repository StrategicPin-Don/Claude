"""Expert DNA product visuals: 15 products x 5 styles, 2400x1600. Writes HTML + jobs.json."""
import os, json, html as H

ROOT = "/home/user/Claude/expert-dna-brand"
OUT = os.path.join(ROOT, "product-visuals")
SRC = os.path.join(OUT, "src")
F = os.path.join(ROOT, "fonts")

INK, WHITE, PAPER = "#101114", "#FFFFFF", "#F4F3F0"
ACC, TINT, DEEP = "#FF5533", "#FFE1D8", "#B32F15"
GREY, GREYD, LINE, LINED, SURF = "#66655F", "#A3A29C", "#E2E0DB", "#2E3036", "#1A1B1F"

CSS = f"""
@font-face{{font-family:HG;font-weight:400;src:url(file://{F}/HankenGrotesk-Regular.ttf)}}
@font-face{{font-family:HG;font-weight:500;src:url(file://{F}/HankenGrotesk-Medium.ttf)}}
@font-face{{font-family:HG;font-weight:700;src:url(file://{F}/HankenGrotesk-Bold.ttf)}}
@font-face{{font-family:PM;font-weight:400;src:url(file://{F}/IBMPlexMono-Regular.ttf)}}
@font-face{{font-family:PM;font-weight:500;src:url(file://{F}/IBMPlexMono-Medium.ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:2400px;height:1600px;overflow:hidden}}
body{{font-family:HG;color:{INK};position:relative}}
.lab{{font:500 22px PM;letter-spacing:.12em;text-transform:uppercase}}
.h{{font-weight:500;letter-spacing:-.03em;line-height:1.04}}
.abs{{position:absolute}}
.mono{{font-family:PM;font-weight:500;letter-spacing:.08em;text-transform:uppercase}}
.bar{{height:14px;background:{LINE}}}
.tag{{display:inline-block;font:500 18px PM;letter-spacing:.08em;text-transform:uppercase;padding:8px 14px;border:1.5px solid {INK}}}
.tag.a{{background:{TINT};border-color:{TINT};color:{DEEP}}}
.tag.f{{background:{ACC};border-color:{ACC};color:{INK}}}
.tag.g{{border-color:{LINE};color:{GREY}}}
"""

def esc(s): return H.escape(s)

# ---------------------------------------------------------------- products
P = [
 dict(slug="starter", name="Starter", code="ST", kind="starter",
      head="Your knowledge, written down once.",
      line="The first Expert DNA files: what lives in your head, in plain Markdown.",
      inside=["offers-and-prices.md", "ideal-client.md", "method.md", "voice.md", "stories.md", "rules.md"],
      before=["prices in your head", "voice? depends on the day", "method: \"I just know\"", "the same story, retold", "rules nobody wrote down"],
      after=["Offers and prices", "Ideal client", "Method", "Voice", "Stories", "Rules"],
      bline="Everything lives in your head.", aline="Six files the AI can read."),
 dict(slug="plugin-01-lead", name="Lead", num="01", code="01", kind="plugin", sub="Who Is Ready to Buy",
      head="Know who is ready to buy.",
      line="Your contacts, sorted by who is ready now.",
      before=["who replied last week?", "DM from {Name}", "maybe interested", "inbox, page 4", "forgot to answer"],
      after=["Client A: ready to buy", "Client B: ready to buy", "Client C: warming up", "Client D: not now"],
      bline="Leads scattered across inboxes.", aline="One list. Ready ones first."),
 dict(slug="plugin-02-follow-up", name="Follow-Up", num="02", code="02", kind="plugin", sub="Follow Up Without Chasing",
      head="Follow up without chasing.",
      line="Drafted follow-ups in your voice, waiting for your yes.",
      before=["did I follow up?", "\"just checking in\"", "sticky note: call back", "awkward to ask again", "{Name}, 3 weeks ago"],
      after=["To {Name}: drafted", "To Client B: drafted", "To Client C: scheduled", "To Client D: sent"],
      bline="Reminders you keep postponing.", aline="Drafts ready. You approve."),
 dict(slug="plugin-03-proposal", name="Proposal", num="03", code="03", kind="plugin", sub="The Proposal You Don't Have to Write",
      head="The proposal you don't have to write.",
      line="From call notes to a proposal draft in your words.",
      before=["call notes, half typed", "old proposal to copy", "what did we agree?", "price? check last one", "blank page"],
      after=["Your situation", "What we will do", "Investment", "Next step"],
      bline="A blank page after every call.", aline="A draft built from the call."),
 dict(slug="plugin-04-session", name="Session", num="04", code="04", kind="plugin", sub="The Hour After the Session",
      head="The hour after the session, done.",
      line="Notes become a summary, next steps and a follow-up email.",
      before=["scribbled notes", "homework? which one", "summary to write", "email still in drafts", "next steps unclear"],
      after=["Summary", "Next steps", "Homework", "Follow-up email"],
      bline="An hour of admin after each session.", aline="Summary and email, ready."),
 dict(slug="plugin-05-onboarding", name="Onboarding", num="05", code="05", kind="plugin", sub="The Intake You Don't Have to Run",
      head="The intake you don't have to run.",
      line="Intake answers turned into a client profile before you meet.",
      before=["intake call to book", "same questions again", "answers in 3 places", "form never read", "first session = admin"],
      after=["Goals", "Context", "Constraints", "How they like to work"],
      bline="The same intake call, every time.", aline="A profile before you meet."),
 dict(slug="plugin-06-content", name="Content", num="06", code="06", kind="plugin", sub="Story Library",
      head="Every story, ready when you need it.",
      line="Your stories, collected and tagged by topic.",
      before=["that story about {Name}", "where did I tell it?", "voice memo, untitled", "nothing to post today", "story half forgotten"],
      after=["Client win", "Lesson learned", "Behind the scenes", "A mistake I made"],
      bline="Good stories, forgotten.", aline="A library you can draw from."),
 dict(slug="plugin-07-crm", name="CRM", num="07", code="07", kind="plugin", sub="The CRM That Updates Itself",
      head="The CRM that updates itself.",
      line="Emails and calls land in the right record on their own.",
      before=["CRM, last updated ...", "notes in email", "stage? not sure", "copy, paste, repeat", "who owns this lead?"],
      after=["Email received", "Call notes added", "Stage moved: Proposal", "Follow-up scheduled"],
      bline="A CRM nobody updates.", aline="Records that fill themselves."),
 dict(slug="plugin-08-ads", name="Ads", num="08", code="08", kind="plugin", sub="Ads Without an Agency",
      head="Ads without an agency.",
      line="Ad variants drafted from your offers and your voice.",
      before=["agency brief to write", "generic ad copy", "\"sounds like everyone\"", "which offer to push?", "waiting for drafts"],
      after=["Angle: pain", "Angle: outcome", "Angle: story", "Ready to test"],
      bline="Copy that sounds like everyone.", aline="Variants in your voice."),
 dict(slug="all-8-plugins", name="All 8 plugins", code="ALL", kind="bundle", dark5=True,
      head="Eight jobs off your plate.",
      line="Lead, Follow-Up, Proposal, Session, Onboarding, Content, CRM, Ads.",
      before=["leads", "follow-ups", "proposals", "session notes", "intake", "stories", "CRM", "ads"],
      after=["Lead", "Follow-Up", "Proposal", "Session", "Onboarding", "Content", "CRM", "Ads"],
      bline="Eight jobs on your desk.", aline="Eight plugins doing them."),
 dict(slug="setup-call", name="Setup Call", code="SC", kind="service",
      head="Set up with a specialist, in one call.",
      line="A specialist sets it up with you, so it works from day one.",
      inside=["Call with a specialist", "Your files reviewed", "Plugins set up", "First test run", "Questions answered"],
      before=["which file first?", "settings, settings", "stuck on step 3", "watching tutorials", "\"it doesn't work\""],
      after=["Files reviewed", "Plugins set up", "Test run done", "You know the next step"],
      bline="Setting it up alone.", aline="Set up together, in one call."),
 dict(slug="connect-and-run-kit", name="Connect and Run Kit", code="KIT", kind="service",
      head="Connect it. Run it.",
      line="The plugins connected to your own tools and running.",
      inside=["Connection guide", "Tool checklist", "First run steps", "Run routine"],
      before=["email here", "calendar there", "files somewhere", "copy between tools", "nothing talks"],
      after=["Email: connected", "Calendar: connected", "Files: connected", "First run: done"],
      bline="Tools that do not talk.", aline="Connected and running."),
 dict(slug="growth-course", name="Growth course", code="GR", kind="course",
      head="Keep growing, one module at a time.",
      line="A course for the next step, built on your Expert DNA.",
      inside=["Course modules", "Lessons", "Exercises", "Worksheets"],
      before=["random tips", "saved posts, unread", "another webinar", "no clear order", "start, stop, start"],
      after=["Module 1", "Module 2", "Module 3", "Module 4"],
      bline="Advice in random order.", aline="A clear path, module by module."),
 dict(slug="strategy-session", name="Strategy session", code="SS", kind="premium", dark5=True,
      head="A clear plan, with Donatas Jonikas, PhD.",
      line="One session to find the main constraint and the next move.",
      inside=["Session with Donatas Jonikas, PhD", "Where you are", "Main constraint", "Action plan"],
      before=["too many ideas", "what to fix first?", "busy, not moving", "advice from everyone", "plan in your head"],
      after=["Where you are", "Main constraint", "Next move", "Action plan"],
      bline="Ten priorities at once.", aline="One constraint. One plan."),
 dict(slug="done-for-you", name="Done For You", code="DFY", kind="premium", dark5=True,
      head="We build it. You stay human.",
      line="Your Expert DNA files and plugins, built and handed over.",
      inside=["Your Expert DNA files, written with you", "Plugins set up", "Connected to your tools", "Handover"],
      before=["no time to write it down", "tools half set up", "\"I'll do it next month\"", "tech is not your job", "still doing everything"],
      after=["Files written with you", "Plugins set up", "Tools connected", "Handed over"],
      bline="One more project on your list.", aline="Built for you. Handed over."),
]
PLUGINS = [p for p in P if p["kind"] == "plugin"]
PLUGIN_NAMES = [(p["num"], p["name"]) for p in PLUGINS]

# ---------------------------------------------------------------- shared shapes
def half_moon(x, y, r, col, side="left"):
    # flat side facing right by default (like the mark)
    if side == "left":
        return f'<div class="abs" style="left:{x}px;top:{y}px;width:{r}px;height:{2*r}px;background:{col};border-radius:{r}px 0 0 {r}px"></div>'
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{r}px;height:{2*r}px;background:{col};border-radius:0 {r}px {r}px 0"></div>'

def plug(x, y, h, col, prongs=True):
    u = h / 48
    s = f'<div class="abs" style="left:{x}px;top:{y}px;width:{3.5*u:.1f}px;height:{h}px;background:{col}"></div>'
    if prongs:
        s += f'<div class="abs" style="left:{x+8*u:.1f}px;top:{y+14*u:.1f}px;width:{16*u:.1f}px;height:{3.5*u:.1f}px;background:{col}"></div>'
        s += f'<div class="abs" style="left:{x+8*u:.1f}px;top:{y+30.5*u:.1f}px;width:{11*u:.1f}px;height:{3.5*u:.1f}px;background:{col}"></div>'
    return s

def lines(n, widths=None, col=LINE, h=14, gap=16):
    widths = widths or [100, 92, 96, 70, 88, 60, 94, 80]
    return "".join(f'<div style="height:{h}px;width:{widths[i % len(widths)]}%;background:{col};margin-bottom:{gap}px"></div>' for i in range(n))

FIT = '''<script>
document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(el=>{
 const avail=+el.dataset.h; let lo=1, hi=1.9;
 for(let i=0;i<14;i++){const m=(lo+hi)/2; el.style.zoom=m; (el.scrollHeight*m<=avail*0.97)?lo=m:hi=m;}
 el.style.zoom=lo; document.body.dataset.fit=(document.body.dataset.fit||'')+lo.toFixed(2)+' ';});
 document.body.classList.add('ready');});
</script>'''
def page(body, bg):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body style="background:{bg}">{body}'+FIT+'</body></html>'

# ---------------------------------------------------------------- S1 interface bodies
ZOOM = {}
def win(title, body, w=1360, h=1180, x=920, y=210):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{WHITE};border:2px solid {INK}">'
            f'<div style="height:76px;border-bottom:2px solid {INK};display:flex;align-items:center;justify-content:space-between;padding:0 36px">'
            f'<span class="lab">{esc(title)}</span><span style="display:flex;gap:10px"><i style="width:18px;height:18px;border:2px solid {INK};display:block"></i>'
            f'<i style="width:18px;height:18px;background:{ACC};display:block"></i></span></div>'
            f'<div style="padding:44px 48px;height:{h-80}px;position:relative;overflow:hidden"><div class="fit" data-h="{h-80-88}">{body}</div></div></div>')

def row(cells, widths, head=False, bold_first=True):
    st = f"display:grid;grid-template-columns:{' '.join(widths)};align-items:center;gap:24px;padding:24px 0;border-bottom:1.5px solid {LINE}"
    out = ""
    for i, c in enumerate(cells):
        if head: out += f'<div class="mono" style="font-size:18px;color:{GREY}">{esc(c)}</div>'
        elif c.startswith("<"): out += f"<div>{c}</div>"
        else: out += f'<div style="font-size:30px;{"font-weight:500" if (i == 0 and bold_first) else f"color:{GREY}"}">{esc(c)}</div>'
    return f'<div style="{st}">{out}</div>'

def tag(t, k=""): return f'<span class="tag {k}">{esc(t)}</span>'

def body_starter():
    files = ["offers-and-prices.md", "ideal-client.md", "method.md", "voice.md", "stories.md", "rules.md"]
    left = "".join(f'<div style="padding:22px 24px;font:500 26px PM;{"background:"+TINT+";color:"+DEEP if f=="voice.md" else ""}">{f}</div>' for f in files)
    right = (f'<div class="mono" style="font-size:18px;color:{GREY}">voice.md</div>'
             f'<div class="h" style="font-size:52px;margin:18px 0 30px"># How I write</div>{lines(3)}'
             f'<div class="h" style="font-size:36px;margin:30px 0 22px">## Words I use</div>{lines(2,[80,64])}'
             f'<div class="h" style="font-size:36px;margin:30px 0 22px">## Words I never use</div>{lines(2,[72,56])}')
    return f'<div style="display:grid;grid-template-columns:420px 1fr;gap:48px;height:100%"><div style="border-right:1.5px solid {LINE};padding-right:24px">{left}</div><div>{right}</div></div>'

def body_lead():
    rows = row(["Contact", "Source", "Signal"], ["1.2fr", "1fr", "1.1fr"], head=True)
    data = [("Client A", "Website form", tag("Ready to buy", "f")), ("Client B", "Reply to email", tag("Ready to buy", "f")),
            ("Client C", "Webinar", tag("Warming up", "a")), ("Client D", "Referral", tag("Warming up", "a")),
            ("Client E", "LinkedIn", tag("Not now", "g")), ("Client F", "Old enquiry", tag("Not now", "g"))]
    for a, b, c in data: rows += row([a, b, c], ["1.2fr", "1fr", "1.1fr"])
    return f'<div class="h" style="font-size:44px;margin-bottom:28px">Who is ready to buy</div>{rows}'

def body_followup():
    cards = ""
    for n, w, st in [("{Name}", "Tue", "f"), ("Client B", "Wed", "a"), ("Client C", "Thu", "a")]:
        cards += (f'<div style="border:1.5px solid {LINE};padding:28px 32px;margin-bottom:26px;display:grid;grid-template-columns:1fr auto;gap:20px">'
                  f'<div><div style="font-size:30px;font-weight:500">To: {esc(n)}</div><div class="mono" style="font-size:18px;color:{GREY};margin:10px 0 20px">Send: {w}, in your voice</div>{lines(2,[96,70],h=12,gap=12)}</div>'
                  f'<div style="display:flex;flex-direction:column;gap:12px;align-items:flex-end">{tag("Approve","f")}{tag("Edit","g")}</div></div>')
    return f'<div class="h" style="font-size:44px;margin-bottom:28px">Follow-ups waiting for your yes</div>{cards}'

def body_proposal():
    notes = f'<div class="mono" style="font-size:18px;color:{GREY};margin-bottom:22px">Call notes</div>{lines(9,[100,80,92,60,88,74,96,50,84],h=12,gap=18)}'
    sec = ""
    for t in ["Your situation", "What we will do", "Investment: {price}", "Next step"]:
        sec += f'<div class="h" style="font-size:34px;margin:0 0 16px">{esc(t)}</div>{lines(2,[96,72],h=12,gap=12)}<div style="height:18px"></div>'
    return (f'<div style="display:grid;grid-template-columns:380px 90px 1fr;height:100%">'
            f'<div style="background:{PAPER};padding:28px">{notes}</div>'
            f'<div style="position:relative">{plug(26,300,110,ACC)}</div>'
            f'<div><div class="mono" style="font-size:18px;color:{DEEP};margin-bottom:22px">Proposal draft for {{Client name}}</div>{sec}</div></div>')

def body_session():
    steps = "".join(f'<div style="display:flex;gap:18px;align-items:center;margin-bottom:18px"><i style="width:26px;height:26px;border:2px solid {INK};display:block;{"background:"+ACC+";border-color:"+ACC if i<2 else ""}"></i><div style="flex:1;height:12px;background:{LINE};width:{[80,64,72][i]}%"></div></div>' for i in range(3))
    blk = lambda t, b: f'<div style="border-top:2px solid {INK};padding-top:22px"><div class="mono" style="font-size:18px;margin-bottom:22px">{t}</div>{b}</div>'
    email = f'<div style="font-size:26px;font-weight:500;margin-bottom:16px">To: {{Name}}</div>{lines(3,[96,88,60],h=12,gap=12)}{tag("Ready to send","f")}'
    return (f'<div class="h" style="font-size:44px;margin-bottom:34px">After the session with {{Name}}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:44px">{blk("Summary", lines(5,[100,90,96,70,84],h=12,gap=14))}{blk("Next steps", steps)}</div>'
            f'<div style="margin-top:44px">{blk("Follow-up email", email)}</div>')

def body_onboarding():
    qa = ""
    for q in ["What do you want to change?", "What have you tried?", "What gets in the way?", "How do you like to work?"]:
        qa += f'<div style="padding:18px 0;border-bottom:1.5px solid {LINE}"><div style="font-size:24px;font-weight:500;margin-bottom:12px">{esc(q)}</div>{lines(1,[80],h=10,gap=0)}</div>'
    prof = "".join(f'<div style="margin-bottom:24px"><div class="mono" style="font-size:17px;color:{DEEP};margin-bottom:10px">{t}</div>{lines(2,[96,64],h=12,gap=10)}</div>' for t in ["Goals", "Context", "Constraints", "How they like to work"])
    return (f'<div style="display:grid;grid-template-columns:1fr 90px 1fr;height:100%">'
            f'<div><div class="mono" style="font-size:18px;color:{GREY};margin-bottom:12px">Intake answers</div>{qa}</div>'
            f'<div style="position:relative">{plug(22,380,96,ACC)}</div>'
            f'<div style="background:{PAPER};padding:32px"><div class="h" style="font-size:38px;margin-bottom:26px">Client profile: {{Name}}</div>{prof}</div></div>')

def body_content():
    tags_ = ["Client win", "Lesson learned", "Behind the scenes", "A mistake I made", "Client win", "Lesson learned"]
    cards = "".join(f'<div style="border:1.5px solid {LINE};padding:26px;height:290px">{tag(t, "a" if i % 2 == 0 else "g")}<div class="h" style="font-size:32px;margin:24px 0 18px">{{Story title}}</div>{lines(3,[96,84,58],h=11,gap=12)}</div>' for i, t in enumerate(tags_))
    return f'<div class="h" style="font-size:44px;margin-bottom:28px">Story library</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">{cards}</div>'

def body_crm():
    ev = ""
    for i, (t, d) in enumerate([("Email received", "Tue"), ("Call notes added", "Tue"), ("Stage moved: Proposal", "Wed"), ("Follow-up scheduled", "Thu")]):
        ev += (f'<div style="display:grid;grid-template-columns:40px 1fr auto;gap:22px;align-items:start;padding-bottom:36px">'
               f'<i style="width:22px;height:22px;background:{ACC if i else INK};display:block;margin-top:8px"></i>'
               f'<div><div style="font-size:30px;font-weight:500">{t}</div>{lines(1,[70],h=10,gap=0)}</div>'
               f'<div style="display:flex;gap:12px;align-items:center"><span class="mono" style="font-size:18px;color:{GREY}">{d}</span>{tag("Auto","a")}</div></div>')
    head = (f'<div style="display:flex;justify-content:space-between;align-items:center;padding-bottom:30px;border-bottom:2px solid {INK};margin-bottom:40px">'
            f'<div style="display:flex;gap:26px;align-items:center"><div style="width:96px;height:96px;background:{PAPER}"></div>'
            f'<div><div class="h" style="font-size:46px">{{Name}}</div><div class="mono" style="font-size:18px;color:{GREY};margin-top:8px">Contact record</div></div></div>{tag("Stage: Proposal","f")}</div>')
    return head + f'<div class="mono" style="font-size:18px;margin-bottom:28px">Activity</div>' + ev

def body_ads():
    cards = ""
    for a in ["Pain", "Outcome", "Story"]:
        cards += (f'<div style="border:1.5px solid {LINE};display:flex;flex-direction:column">'
                  f'<div style="height:300px;background:{PAPER};position:relative;overflow:hidden">{half_moon(-60,30,120,INK,"right") if a=="Pain" else ""}'
                  f'{half_moon(140,60,90,ACC) if a=="Outcome" else ""}{plug(150,80,140,ACC) if a=="Story" else ""}</div>'
                  f'<div style="padding:26px">{tag("Angle: "+a, "a")}<div class="h" style="font-size:30px;margin:22px 0 16px">{{Headline}}</div>{lines(3,[96,80,52],h=11,gap=12)}'
                  f'<div class="mono" style="font-size:17px;color:{GREY};margin-top:10px">Draft</div></div></div>')
    return f'<div class="h" style="font-size:44px;margin-bottom:28px">Ad variants from your offers and voice</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px">{cards}</div>'

def body_bundle():
    r = ""
    for n, name in PLUGIN_NAMES:
        r += (f'<div style="display:grid;grid-template-columns:70px 1fr auto;align-items:center;gap:20px;padding:19px 0;border-bottom:1.5px solid {LINE}">'
              f'<span class="mono" style="font-size:24px;color:{DEEP}">{n}</span><span style="font-size:32px;font-weight:500">{esc(name)}</span>'
              f'<span style="display:flex;align-items:center;gap:14px"><span class="mono" style="font-size:17px;color:{GREY}">On</span>'
              f'<span style="width:72px;height:36px;background:{ACC};position:relative;display:block"><i style="position:absolute;right:5px;top:5px;width:26px;height:26px;background:{INK};display:block"></i></span></span></div>')
    return f'<div class="h" style="font-size:44px;margin-bottom:16px">Your plugins</div>{r}'

def body_setup():
    items = ["Review your Expert DNA files", "Set up the plugins", "First test run together", "Questions and next step"]
    ag = "".join(f'<div style="display:grid;grid-template-columns:80px 1fr;gap:20px;padding:30px 0;border-bottom:1.5px solid {LINE}"><span class="mono" style="font-size:28px;color:{DEEP}">0{i+1}</span><span style="font-size:34px;font-weight:500">{t}</span></div>' for i, t in enumerate(items))
    head = (f'<div style="display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:30px;border-bottom:2px solid {INK}">'
            f'<div><div class="mono" style="font-size:18px;color:{GREY}">Call agenda</div><div class="h" style="font-size:50px;margin-top:12px">Setup Call with a specialist</div></div>{tag("{Day}, {Time}","a")}</div>')
    return head + ag

def body_kit():
    steps = [("Email", "Connected"), ("Calendar", "Connected"), ("Files", "Connected"), ("First run", "Done"), ("Weekly routine", "Next")]
    r = ""
    for i, (t, s) in enumerate(steps):
        done = s != "Next"
        r += (f'<div style="display:grid;grid-template-columns:50px 1fr auto;gap:22px;align-items:center;padding:26px 0;border-bottom:1.5px solid {LINE}">'
              f'<i style="width:30px;height:30px;border:2.5px solid {INK};display:block;{"background:"+INK if done else ""}"></i>'
              f'<span style="font-size:34px;font-weight:500">{t}</span>{tag(s, "f" if done else "g")}</div>')
    return f'<div class="h" style="font-size:44px;margin-bottom:20px">Connect and run</div>{r}'

def body_growth():
    mods = ""
    for i in range(6):
        state = "f" if i < 2 else ("a" if i == 2 else "g")
        lab = "Done" if i < 2 else ("Now" if i == 2 else "Next")
        mods += (f'<div style="display:grid;grid-template-columns:150px 1fr auto;align-items:center;gap:20px;padding:22px 0;border-bottom:1.5px solid {LINE}">'
                 f'<span class="mono" style="font-size:22px;color:{GREY}">Module {i+1}</span><span style="font-size:32px;font-weight:500">{{Lesson title}}</span>{tag(lab,state)}</div>')
    player = f'<div style="height:330px;background:{INK};position:relative;margin-bottom:24px;overflow:hidden">{half_moon(60,45,120,WHITE)}{plug(220,45,240,ACC)}</div>'
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:44px"><div>{player}<div class="h" style="font-size:38px">Module 3</div><div style="margin-top:20px">{lines(3,[96,84,60],h=12,gap=14)}</div></div><div>{mods}</div></div>'

def body_strategy():
    secs = ["Where you are", "Where you want to be", "Main constraint", "Action plan"]
    blocks = "".join(f'<div style="border-top:2px solid {INK if i!=2 else ACC};padding-top:22px"><div class="mono" style="font-size:19px;margin-bottom:22px;{"color:"+DEEP if i==2 else ""}">{t}</div>{lines(4,[96,88,72,50],h=12,gap=14)}</div>' for i, t in enumerate(secs))
    head = (f'<div style="padding-bottom:30px;margin-bottom:40px;border-bottom:1.5px solid {LINE}"><div class="mono" style="font-size:18px;color:{GREY}">Session brief</div>'
            f'<div class="h" style="font-size:50px;margin-top:12px">Strategy session</div><div style="font-size:26px;color:{GREY};margin-top:10px">with Donatas Jonikas, PhD, for {{Client name}}</div></div>')
    return head + f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px 52px">{blocks}</div>'

def body_dfy():
    cols = [("Your input", ["Interview", "Your examples"], "g"), ("We build", ["Expert DNA files", "Plugins set up", "Tools connected"], "a"), ("Ready for you", ["Handover", "Running"], "f")]
    out = ""
    for t, cs, k in cols:
        cards = "".join(f'<div style="background:{WHITE};border:1.5px solid {LINE};padding:22px;margin-bottom:18px"><div style="font-size:28px;font-weight:500;margin-bottom:14px">{c}</div>{lines(1,[70],h=10,gap=0)}</div>' for c in cs)
        out += f'<div style="background:{PAPER};padding:24px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px"><span class="mono" style="font-size:19px">{t}</span>{tag(str(len(cs)), k) if False else ""}</div>{cards}</div>'
    return f'<div class="h" style="font-size:44px;margin-bottom:30px">Built for you</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px">{out}</div>'

BODIES = {"starter": body_starter, "plugin-01-lead": body_lead, "plugin-02-follow-up": body_followup, "plugin-03-proposal": body_proposal,
          "plugin-04-session": body_session, "plugin-05-onboarding": body_onboarding, "plugin-06-content": body_content,
          "plugin-07-crm": body_crm, "plugin-08-ads": body_ads, "all-8-plugins": body_bundle, "setup-call": body_setup,
          "connect-and-run-kit": body_kit, "growth-course": body_growth, "strategy-session": body_strategy, "done-for-you": body_dfy}

def label_of(p):
    return (f"Plugin {p['num']} / {p['name']}" if p["kind"] == "plugin" else p["name"])

def s1(p):
    left = (f'<div class="abs" style="left:120px;top:210px;width:700px">'
            f'<div class="lab" style="color:{DEEP}">{esc(label_of(p))}</div>'
            f'<div class="h" style="font-size:84px;margin-top:36px">{esc(p["head"])}</div>'
            f'<div style="font-size:32px;line-height:1.45;color:{GREY};margin-top:40px">{esc(p["line"])}</div></div>')
    deco = plug(120, 1250, 140, ACC)
    return page(left + deco + win(p["name"], BODIES[p["slug"]]()), PAPER)

# ---------------------------------------------------------------- S2 statement
def s2(p):
    n = len(p["head"])
    fs = 168 if n <= 26 else (148 if n <= 34 else 128)
    return page(
        half_moon(1640, 260, 760, INK) +
        f'<div class="abs lab" style="left:120px;top:120px">{esc(label_of(p))}</div>'
        f'<div class="abs" style="left:0;right:0;top:186px;height:2px;background:{INK}"></div>'
        f'<div class="abs h" style="left:120px;top:330px;width:1420px;font-size:{fs}px;line-height:1.0">{esc(p["head"])}</div>'
        f'<div class="abs" style="left:120px;bottom:120px;width:1100px;font-size:34px;line-height:1.4">{esc(p["line"])}</div>', ACC)

# ---------------------------------------------------------------- S3 what's inside
PRODUCES = {'plugin-01-lead': 'A list sorted by who is ready', 'plugin-02-follow-up': 'Follow-up drafts in your voice', 'plugin-03-proposal': 'Proposal drafts', 'plugin-04-session': 'Summary, next steps, follow-up email', 'plugin-05-onboarding': 'A client profile before you meet', 'plugin-06-content': 'A story library tagged by topic', 'plugin-07-crm': 'Records that update themselves', 'plugin-08-ads': 'Ad variants to test'}
def inside_items(p):
    if p["kind"] == "plugin":
        return [("Plugin", f'{p["name"]}: {p["sub"]}', True), ("Mini course", f'How to use {p["name"]}', False),
                ("Reads", "Your Expert DNA files", False), ("Produces", PRODUCES[p["slug"]], False)]
    if p["kind"] == "bundle":
        return [(f"Plugin {n}", name, i == 0) for i, (n, name) in enumerate(PLUGIN_NAMES)] + [("Included", "8 mini courses", False)]
    if p["kind"] == "starter":
        return [("File", f, i == 0) for i, f in enumerate(p["inside"])]
    return [("Inside", t, i == 0) for i, t in enumerate(p["inside"])]

def s3(p):
    items = inside_items(p)
    n = len(items)
    cols = 2 if n == 4 else 3
    cards = ""
    fs = 58 if n <= 4 else (46 if n <= 6 else 38)
    for i, (k, v, hi) in enumerate(items):
        bg, fg, sub = (WHITE, INK, GREY) if (i % 3 != 1) else (SURF, WHITE, GREYD)
        if hi: bg, fg, sub = ACC, INK, INK
        mono = p["kind"] == "starter"
        span = "grid-row:span 2;" if (n == 5 and i == 0) else ""
        cards += (f'<div style="{span}background:{bg};color:{fg};padding:36px 38px;display:flex;flex-direction:column;justify-content:space-between;border:1.5px solid {LINED if bg==SURF else bg}">'
                  f'<div style="display:flex;justify-content:space-between"><span class="mono" style="font-size:20px;color:{sub}">{esc(k)}</span><span class="mono" style="font-size:20px;color:{sub}">{i+1:02d}</span></div>'
                  f'<div style="font-size:{fs - (8 if mono else 0)}px;font-weight:500;letter-spacing:-.025em;line-height:1.1;{"font-family:PM;letter-spacing:-.01em" if mono else ""}">{esc(v)}</div></div>')
    grid_w = 1380
    head = (f'<div class="abs" style="left:120px;top:150px;width:700px"><div class="lab" style="color:{GREYD}">What\'s inside / {esc(p["name"])}</div>'
            f'<div class="h" style="font-size:96px;color:{WHITE};margin-top:36px">{esc(p["head"])}</div></div>'
            f'<div class="abs" style="left:120px;bottom:120px;width:640px;font-size:30px;line-height:1.45;color:{GREYD}">{esc(p["line"])}</div>')
    grid = f'<div class="abs" style="left:900px;top:150px;width:{grid_w}px;height:1300px;display:grid;grid-template-columns:repeat({cols},1fr);grid-auto-rows:1fr;gap:22px">{cards}</div>'
    return page(head + grid + f'<div class="abs" style="left:0;right:0;top:110px;height:1px;background:{LINED}"></div>', INK)

# ---------------------------------------------------------------- S4 before / after
def s4(p):
    bef = p["before"]
    pos = [(130, 300, -6), (600, 420, 5), (220, 640, 3), (650, 820, -5), (170, 1040, -3), (560, 1150, 6), (330, 860, -4), (720, 230, 3)]
    frags = ""
    for i, t in enumerate(bef):
        x, y, r = pos[i % len(pos)]
        bg = WHITE if i % 2 == 0 else TINT
        frags += (f'<div class="abs" style="left:{x}px;top:{y}px;transform:rotate({r}deg);background:{bg};padding:26px 30px;width:{470 if len(bef) <= 5 else 360}px;border:1.5px solid {LINE}">'
                  f'<div style="font-size:{38 if len(bef) <= 5 else 30}px;color:{INK};line-height:1.25">{esc(t)}</div></div>')
    # tangled lines
    tang = ('<svg class="abs" style="left:80px;top:250px" width="1000" height="1200" viewBox="0 0 1000 1200">'
            f'<g fill="none" stroke="{GREY}" stroke-width="3" opacity=".55">'
            '<path d="M60 200 C300 80 420 420 700 260 S900 600 620 700 S240 640 300 900 S700 1100 900 980"/>'
            '<path d="M900 140 C640 260 500 120 360 380 S120 620 420 760 S840 820 760 1100"/>'
            '<path d="M120 1100 L880 300"/><path d="M200 300 L760 1000"/></g></svg>')
    after = ""
    for i, t in enumerate(p["after"]):
        after += (f'<div style="display:grid;grid-template-columns:70px 1fr 44px;align-items:center;gap:20px;padding:{24 if len(p["after"]) > 6 else 46}px 0;border-bottom:1.5px solid {LINE}">'
                  f'<span class="mono" style="font-size:26px;color:{DEEP}">{i+1:02d}</span><span style="font-size:{40 if len(p["after"]) > 6 else 50}px;font-weight:500;letter-spacing:-.02em">{esc(t)}</span>'
                  f'<i style="width:32px;height:32px;background:{INK};display:block"></i></div>')
    left = (f'<div class="abs" style="left:0;top:0;width:1170px;height:1600px;background:{PAPER};overflow:hidden">{tang}{frags}'
            f'<div class="abs lab" style="left:120px;top:120px;color:{GREY}">Before</div>'
            f'<div class="abs h" style="left:120px;bottom:110px;font-size:56px;color:{GREY}">{esc(p["bline"])}</div></div>')
    right = (f'<div class="abs" style="left:1290px;top:0;width:1110px;height:1600px;background:{WHITE}">'
             f'<div class="abs lab" style="left:120px;top:120px;color:{DEEP}">After / {esc(p["name"])}</div>'
             f'<div class="abs" style="left:120px;top:290px;width:880px">{after}</div>'
             f'<div class="abs h" style="left:120px;bottom:110px;font-size:56px">{esc(p["aline"])}</div></div>')
    divider = (f'<div class="abs" style="left:1170px;top:0;width:120px;height:1600px;background:{WHITE}"></div>'
               f'<div class="abs" style="left:1170px;top:0;width:16px;height:1600px;background:{ACC}"></div>'
               f'<div class="abs" style="left:1206px;top:700px;width:84px;height:16px;background:{ACC}"></div>'
               f'<div class="abs" style="left:1206px;top:860px;width:58px;height:16px;background:{ACC}"></div>')
    return page(left + divider + right, WHITE)

# ---------------------------------------------------------------- S5 plug-in (abstract)
def sq(x, y, w, h, c): return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{c}"></div>'

def composition(slug, fg, ac, alt):
    X, Y = 1000, 400  # area origin; area ~ 960 x 840
    c = ""
    if slug == "starter":  # six files, one in focus
        for i in range(6):
            cx, cy = X + (i % 3) * 300, Y + (i // 3) * 420
            c += sq(cx, cy, 240, 360, ac if i == 3 else (fg if i % 2 == 0 else alt)) + sq(cx + 40, cy + 60, 120, 18, alt if i % 2 == 0 or i == 3 else fg)
    elif slug == "plugin-01-lead":  # sorted bars, ready ones lit
        for i, w in enumerate([820, 760, 520, 440, 300, 220]): c += sq(X, Y + i * 135, w, 80, ac if i < 2 else alt)
    elif slug == "plugin-02-follow-up":  # messages in a queue moving right
        for i in range(4): c += sq(X + i * 150, Y + i * 190, 360, 130, ac if i == 0 else alt)
    elif slug == "plugin-03-proposal":  # notes -> document
        c += sq(X, Y, 260, 820, alt)
        for i in range(5): c += sq(X + 340, Y + i * 170, 560, 110 if i else 160, fg if i else ac)
    elif slug == "plugin-04-session":  # one big block becomes three
        c += half_moon(X, Y, 300, alt, "right")
        for i in range(3): c += sq(X + 420, Y + i * 220, 480, 160, ac if i == 2 else fg)
    elif slug == "plugin-05-onboarding":  # questions fill a profile
        for i in range(4): c += sq(X, Y + i * 210, 280, 140, alt)
        c += sq(X + 380, Y, 520, 820, fg) + sq(X + 440, Y + 60, 400, 120, ac)
    elif slug == "plugin-06-content":  # library grid
        for r in range(3):
            for k in range(3): c += sq(X + k * 300, Y + r * 290, 250, 240, ac if (r, k) == (1, 1) else (fg if (r + k) % 2 == 0 else alt))
    elif slug == "plugin-07-crm":  # timeline
        c += sq(X + 40, Y, 18, 840, alt)
        for i in range(5): c += sq(X, Y + i * 190, 100, 100, ac if i == 2 else fg) + sq(X + 160, Y + 30 + i * 190, 620 - i * 70, 40, alt)
    elif slug == "plugin-08-ads":  # three variants
        for i in range(3):
            c += sq(X + i * 310, Y, 270, 840, alt)
            c += half_moon(X + i * 310 + 30, Y + 80, 105, ac if i == 1 else fg) if i != 2 else sq(X + i * 310 + 40, Y + 80, 190, 190, fg)
    elif slug == "all-8-plugins":  # eight prongs all lit
        for i in range(8): c += sq(X, Y + i * 105, 760 - (i % 2) * 220, 56, ac)
    elif slug == "setup-call":  # two half moons meeting (you + specialist)
        c += half_moon(X, Y + 60, 360, fg, "right") + half_moon(X + 540, Y + 60, 360, ac)
    elif slug == "connect-and-run-kit":  # tools connected by a line
        c += sq(X, Y + 400, 900, 26, ac)
        for i in range(4): c += sq(X + i * 270, Y + 280 if i % 2 else Y + 470, 170, 170 if i % 2 == 0 else 120, fg)
    elif slug == "growth-course":  # steps going up
        for i in range(5): c += sq(X + i * 185, Y + 840 - (i + 1) * 165, 160, (i + 1) * 165, ac if i == 4 else (fg if i % 2 == 0 else alt))
    elif slug == "strategy-session":  # many paths narrowed to one
        for i in range(6): c += sq(X, Y + i * 140, 360, 50, alt)
        c += sq(X + 420, Y, 30, 760, fg) + sq(X + 500, Y + 355, 420, 50, ac)
    elif slug == "done-for-you":  # finished block handed over
        c += sq(X, Y, 620, 620, alt) + sq(X + 80, Y + 80, 460, 460, fg) + sq(X + 380, Y + 620, 540, 120, ac)
    return c

def s5(p):
    dark = p.get("dark5")
    bg, fg, alt, txt, sub = (INK, WHITE, LINED, WHITE, GREYD) if dark else (WHITE, INK, LINE, INK, GREY)
    moon = half_moon(-260, 260, 540, fg)  # bleeds off the left edge
    con = plug(380, 470, 660, ACC)
    num_fs = 200 if len(p["code"]) <= 2 else 170
    txtb = (f'<div class="abs mono" style="left:1000px;top:130px;font-size:{num_fs}px;font-weight:500;letter-spacing:-.02em;color:{txt};line-height:1">{esc(p["code"])}</div>'
            f'<div class="abs" style="right:120px;top:150px;text-align:right"><div class="lab" style="color:{sub}">{esc(label_of(p))}</div></div>'
            f'<div class="abs" style="left:1000px;bottom:100px;font-size:30px;color:{sub}">{esc(p["head"])}</div>')
    return page(moon + con + composition(p["slug"], fg, ACC, alt) + txtb, bg)

STYLES = [("s1", "interface", s1), ("s2", "statement", s2), ("s3", "inside", s3), ("s4", "before-after", s4), ("s5", "plug-in", s5)]

if __name__ == "__main__":
    jobs = []
    for p in P:
        os.makedirs(os.path.join(OUT, p["slug"]), exist_ok=True)
        os.makedirs(os.path.join(SRC, "html", p["slug"]), exist_ok=True)
        for sid, sname, fn in STYLES:
            hp = os.path.join(SRC, "html", p["slug"], f'{p["slug"]}-{sid}-{sname}.html')
            open(hp, "w").write(fn(p))
            jobs.append(dict(html=hp, out=os.path.join(OUT, p["slug"], f'{p["slug"]}-{sid}-{sname}.png')))
    json.dump(jobs, open(os.path.join(SRC, "jobs.json"), "w"), indent=1)
    json.dump([dict(slug=p["slug"], name=label_of(p)) for p in P], open(os.path.join(SRC, "products.json"), "w"))
    print(len(jobs), "visuals")
