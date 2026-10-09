from base import *

# ---------------- 1. COVER ----------------
def p_cover():
    CC = {"bills": "#5B86C9", "debt": "#3A3F4A", "buffer": "#E8BC2C"}
    bk = "".join(bucket_svg(CC.get(k, c), "#fff", s=74, label=f"{i+1}. {n}", lfs=12.5)
                 for i, (k, n, c, t, w, r) in enumerate(BUCKETS))
    inside = ["4 short lessons", "Your 6-bucket setup", "4 payday drills", "Payday routine card",
              "30-day lock-in challenge", "Companion spreadsheet"]
    li = "".join(f'<div style="display:flex;gap:9px;align-items:center;font-size:13.5px;font-weight:700;color:{NAVY}">{tick(GREEN,17)}<span>{x}</span></div>' for x in inside)
    body = f'''
<div style="display:flex;align-items:center;gap:10px">{LOGO.replace('width="20" height="20"','width="26" height="26"').replace(f'fill="{NAVY}"','fill="#FFFFFF"').replace(f'fill="{BLACK}"','fill="#E8BC2C"').replace(f'stroke="{GOLD}" stroke-width="12"', f'stroke="{NAVY}" stroke-width="12"')}<span class="eyebrow" style="color:#fff;font-size:12px;letter-spacing:4px">The Payday Plan</span></div>
<div style="margin-top:84px;align-self:flex-start;background:{GOLDB};color:{NAVY};font-size:11.5px;font-weight:900;letter-spacing:3px;padding:8px 16px;border-radius:999px">A 30-DAY TRAINING WORKBOOK</div>
<h1 class="serif" style="margin-top:20px;font-size:60px;line-height:1.06;color:#fff">The Paycheck<br>Budget System</h1>
<div style="margin-top:18px;font-size:19px;font-weight:700;line-height:1.45;color:#DCE3EE">Set it up once. Train it in four paydays.<br><span style="color:{GOLDB}">Then it runs on muscle memory.</span></div>
<div style="margin-top:70px;display:flex;flex-direction:column;align-items:center">
<span style="background:{GREEN};color:#fff;border-radius:999px;padding:8px 26px;font-size:13px;font-weight:900;letter-spacing:3px">PAYDAY</span>
<svg width="640" height="40" viewBox="0 0 640 40" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"><path d="M320 0 V18 M53 18 H587 M53 18 V38 M160 18 V38 M267 18 V38 M373 18 V38 M480 18 V38 M587 18 V38"/></svg>
<div style="width:640px;display:grid;grid-template-columns:repeat(6,1fr);justify-items:center;white-space:nowrap">{bk}</div>
</div>
<div style="margin-top:70px;background:#fff;border-radius:18px;padding:26px 30px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px 18px">{li}</div>
<div style="margin-top:16px;text-align:center;font-size:11.5px;font-weight:800;letter-spacing:1.4px;color:#C3CCDB">15 PRINTABLE PAGES · SPREADSHEET FOR EXCEL + GOOGLE SHEETS · PHONE WALLPAPER</div>
<div class="spacer"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end">
<span class="cav" style="font-size:30px;color:{GOLDB}">from our family to yours</span>
<span style="font-size:12px;font-weight:700;color:#C3CCDB;text-align:right;line-height:1.5">For families paid weekly<br>or every two weeks</span></div>'''
    return f'<section class="page" style="background:{NAVY};padding:46px 56px 40px">{body}</section>'

# ---------------- 2. WELCOME ----------------
def p_welcome():
    stages = [
        (1, "LEARN", NAVY, "#fff", "Why the money runs out, and the one number that fixes it.", "20 minutes", "Pages 3–4"),
        (2, "BUILD", GREEN, "#fff", "Set up your 6 buckets. You only do this once.", "About an hour", "Pages 5–7"),
        (3, "TRAIN", GOLDB, NAVY, "Four payday drills. The help fades each time.", "15 min a payday", "Pages 8–11"),
        (4, "LOCK IN", BLACK, GOLDB, "A 30-day challenge and your routine card.", "5 min a day", "Pages 12–15"),
    ]
    st = "".join(f'''<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;overflow:hidden;display:flex;flex-direction:column">
<div style="background:{bg};color:{fg};padding:8px 12px;display:flex;align-items:center;gap:8px"><span style="font-size:20px;font-weight:900">{n}</span><span style="font-size:12px;font-weight:900;letter-spacing:2.5px">{nm}</span></div>
<div style="padding:10px 12px 12px;display:flex;flex-direction:column;gap:8px;flex:1"><span style="font-size:12.5px;font-weight:700;line-height:1.4;color:{INK}">{w}</span><span class="spacer"></span>
<span style="font-size:11px;font-weight:700;color:{GREY};display:flex;align-items:center;gap:5px">{icon("clock", GREY, 13)}{t}</span><span style="font-size:11px;font-weight:800;color:{GREEN}">{pg}</span></div></div>''' for n, nm, bg, fg, w, t, pg in stages)
    have = ["Every bill you pay, found and listed", "A per-payday number for each one",
            "6 buckets that fill themselves on payday", "A routine you can do from memory",
            "A Don’t Touch fund started for surprises"]
    hv = "".join(f'<div style="display:flex;gap:9px;align-items:flex-start;font-size:13px;font-weight:600;line-height:1.35">{tick(GREEN,16)}<span>{x}</span></div>' for x in have)
    need = ["A pencil and a highlighter", "Your last 3 months of bank statements", "About an hour for the setup",
            "The spreadsheet (optional, it does the maths)"]
    nd = "".join(f'<div style="display:flex;gap:9px;align-items:flex-start;font-size:13px;font-weight:600;line-height:1.35"><span class="box" style="width:13px;height:13px;margin-top:1px"></span><span>{x}</span></div>' for x in need)
    body = f'''{title("Welcome. Print this once.", "This isn’t a planner you reprint every payday. It’s training, so the plan ends up living in your head.")}
<div style="background:{CREAM};border-radius:14px;padding:16px 22px;display:flex;flex-direction:column;gap:7px">
<div class="serif" style="font-size:17px;color:{NAVY}">Hi, and welcome.</div>
<div style="font-size:13.5px;font-weight:500;line-height:1.6;color:#2B2B2B">We built this after too many months of being broke before payday. We were budgeting, but our bills didn’t care when we got paid. Monthly ones, quarterly ones, the car registration once a year. They’d all land at once, then a tire would go, and we were back to zero.<br><br>What finally worked wasn’t a fancier budget. It was giving every bill its own bucket, paying our savings like a bill, and doing the same few steps every payday until we didn’t have to think about it anymore. This workbook teaches you exactly that.</div></div>
<div class="eyebrow" style="margin-top:18px;color:{NAVY}">Your 30-day path</div>
<div style="margin-top:9px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px">{st}</div>
<div style="margin-top:16px;display:grid;grid-template-columns:1.15fr 1fr;gap:14px">
<div style="background:#fff;border:2px solid {GOLD};border-radius:14px;padding:14px 18px;display:flex;flex-direction:column;gap:8px"><div class="serif" style="font-size:15.5px;color:{NAVY}">By the end, you’ll have</div>{hv}</div>
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;padding:14px 18px;display:flex;flex-direction:column;gap:8px"><div class="serif" style="font-size:15.5px;color:{NAVY}">What you need</div>{nd}</div></div>
<div style="margin-top:14px;background:{TGREEN};border-radius:14px;padding:12px 18px;display:flex;gap:14px;align-items:center">
<span style="flex:none;font-size:11px;font-weight:900;letter-spacing:2px;color:{GREEN}">PAPER OR<br>SPREADSHEET?</span>
<span style="font-size:12.5px;font-weight:600;line-height:1.5">Both work. Writing it by hand is what makes it stick, so set up on paper first. After that, the spreadsheet does all the maths for you, every payday, with no reprinting.</span></div>
<div style="margin-top:14px;display:flex;justify-content:space-between;align-items:flex-end"><span class="cav" style="font-size:28px;color:{GREEN}">From our family to yours.</span><span style="font-size:10px;font-weight:600;color:{GREY}">General information, not financial advice.</span></div>'''
    return page(2, "start", body)

# ---------------- 3. LESSON 1 ----------------
def p_lesson1():
    M = list("JFMAMJJASOND")
    pile = {2, 11}  # Mar, Dec
    def cell(i, content):
        bg = TRED if i in pile else "transparent"
        return f'<div style="background:{bg};display:flex;align-items:center;justify-content:center;gap:2px;height:31px">{content}</div>'
    dot = lambda c, s=9: f'<span style="width:{s}px;height:{s}px;border-radius:50%;background:{c};display:inline-block"></span>'
    pay = lambda i: "".join(f'<span style="width:3px;height:12px;background:{GREEN};display:inline-block;border-radius:1px"></span>' for _ in range(5 if i in (0, 4, 7, 9) else 4))
    rows = [
        ("Your pay", "weekly", lambda i: pay(i)),
        ("Rent, phone, power", "monthly", lambda i: dot(NAVY)),
        ("Water, trash", "quarterly", lambda i: dot(GOLD, 11) if i in (2, 5, 8, 11) else ""),
        ("Car registration", "yearly", lambda i: dot(RED, 13) if i == 2 else ""),
        ("Christmas", "yearly", lambda i: dot(RED, 13) if i == 11 else ""),
    ]
    head = '<div></div>' + "".join(f'<div style="text-align:center;font-size:10.5px;font-weight:900;color:{RED if i in pile else GREY};background:{TRED if i in pile else "transparent"};padding-top:3px">{m}</div>' for i, m in enumerate(M))
    grid = head
    for lab, rh, f in rows:
        grid += f'<div style="display:flex;flex-direction:column;justify-content:center;height:31px"><span style="font-size:11.5px;font-weight:800;line-height:1.1">{lab}</span><span style="font-size:9.5px;font-weight:700;color:{GREY};text-transform:uppercase;letter-spacing:1px">{rh}</span></div>'
        grid += "".join(cell(i, f(i)) for i in range(12))
    table = [("Monthly", "÷ 4", "÷ 2"), ("Quarterly", "÷ 12", "÷ 6"), ("Twice a year", "÷ 24", "÷ 12"), ("Yearly", "÷ 48", "÷ 24")]
    tr = "".join(f'<div style="display:grid;grid-template-columns:1.3fr 1fr 1fr;padding:6px 14px;border-top:1px solid #EEE8DA;align-items:center"><span style="font-size:12.5px;font-weight:800">{a}</span><span class="serif" style="text-align:center;font-size:17px;color:{GREEN}">{b}</span><span class="serif" style="text-align:center;font-size:17px;color:{GREEN}">{c}</span></div>' for a, b, c in table)
    qs = [("Phone and internet is $80 a month. You’re paid weekly.", "$20"),
          ("Water is $150 a quarter. You’re paid every two weeks.", "$25"),
          ("Christmas costs about $600. You’re paid weekly.", "$12.50")]
    qq = "".join(f'<div style="display:flex;gap:10px;align-items:flex-end"><span style="flex:none;font-size:12px;font-weight:900;color:{NAVY}">{"abc"[i]})</span><span style="flex:1;font-size:12px;font-weight:600;line-height:1.35">{q}</span><span style="flex:none;font-size:12px;font-weight:800">$</span><span class="wl" style="flex:none;width:62px;height:18px"></span></div>' for i, (q, a) in enumerate(qs))
    ans = " · ".join(f'{"abc"[i]}) {a}' for i, (q, a) in enumerate(qs))
    body = f'''{title("It’s not your pay. It’s your bills.", "Why the money runs out, even when you budget.", kicker="Lesson 1")}
<div style="display:flex;gap:18px;align-items:flex-start">
<div style="flex:1;font-size:13.5px;font-weight:500;line-height:1.6">Your pay arrives on <b>one</b> rhythm. Your bills arrive on <b>four</b>: weekly, monthly, quarterly and yearly. Pay them all from one account and a few months a year they pile up at once. That’s the month you get knocked back to zero, even though you did nothing wrong.</div>
<div class="cav" style="flex:none;width:200px;font-size:24px;line-height:1.05;color:{RED};transform:rotate(-2deg);padding-top:4px">like holding water in your hands</div></div>
<div style="margin-top:10px;background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;padding:8px 14px 8px">
<div style="display:grid;grid-template-columns:132px repeat(12,1fr);column-gap:3px">{grid}</div>
<div style="margin-top:6px;display:flex;gap:8px;align-items:center;font-size:11px;font-weight:700;color:{RED}"><span style="width:14px;height:10px;background:{TRED};display:inline-block;border-radius:2px"></span>Pile-up months. Same pay, three times the bills.</div></div>
<div class="serif" style="margin-top:12px;font-size:19px;color:{NAVY}">The fix: turn every bill into a per-payday number</div>
<div style="margin-top:4px;font-size:13px;font-weight:500;line-height:1.55">Big bill or small, weekly or yearly, every bill becomes a small, same-size amount you set aside <b>every payday</b>. When the bill arrives, the money is already sitting there waiting.</div>
<div style="margin-top:10px;display:grid;grid-template-columns:1fr 1.05fr;gap:14px">
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;overflow:hidden">
<div style="display:grid;grid-template-columns:1.3fr 1fr 1fr;padding:9px 14px;background:{NAVY};color:#fff;font-size:10px;font-weight:900;letter-spacing:1.5px"><span>THE BILL IS</span><span style="text-align:center">PAID<br>WEEKLY</span><span style="text-align:center">EVERY<br>2 WEEKS</span></div>{tr}
<div style="padding:7px 14px 9px;font-size:10.5px;font-weight:600;line-height:1.4;color:{GREY};border-top:1px solid #EEE8DA">Paid twice a month? Use the every-2-weeks column. Paid monthly? Divide by 1, 3, 6 and 12.</div></div>
<div style="display:flex;flex-direction:column;gap:10px">
<div style="background:{TGREEN};border-radius:14px;padding:12px 16px"><div class="eyebrow" style="color:{GREEN};font-size:10px">Example</div><div style="margin-top:4px;font-size:13px;font-weight:700;line-height:1.5">Car registration is $360 a year. You’re paid every two weeks.<br><span class="serif" style="font-size:17px;color:{GREEN}">$360 ÷ 24 = $15 a payday.</span></div></div>
<div style="background:{CREAM};border-radius:14px;padding:11px 16px;font-size:11.5px;font-weight:600;line-height:1.5"><b style="color:{NAVY}">Why 48 and 24, not 52 and 26?</b> A year has a few extra paydays. Dividing this way means you save a little more than you need, so you finish every year slightly ahead.</div></div></div>
<div style="margin-top:12px;background:#fff;border:2px dashed {GOLD};border-radius:14px;padding:12px 16px;position:relative">
<div style="display:flex;justify-content:space-between;align-items:center"><span class="serif" style="font-size:15.5px;color:{NAVY}">Try it: how much per payday?</span><span class="eyebrow" style="font-size:9.5px;color:{GREY}">2 minutes</span></div>
<div style="margin-top:8px;display:flex;flex-direction:column;gap:9px">{qq}</div>
<div style="margin-top:10px;display:flex;justify-content:space-between;align-items:center"><span class="cav" style="font-size:21px;color:{GREEN}">A bill you saw coming isn’t an emergency.</span><span style="transform:rotate(180deg);font-size:10.5px;font-weight:700;color:{GREY}">Answers: {ans}</span></div></div>'''
    return page(3, 1, body)

# ---------------- 4. BILL FINDER ----------------
def p_billfinder():
    rows = 20
    hdr = f'<div style="display:grid;grid-template-columns:2.1fr 1.35fr 0.95fr 0.95fr 1.2fr;gap:8px;padding:9px 12px;background:{NAVY};color:#fff;font-size:9.5px;font-weight:900;letter-spacing:1.3px"><span>BILL</span><span>HOW OFTEN</span><span>AMOUNT</span><span>PER PAYDAY</span><span>WHICH ACCOUNT</span></div>'
    often = f'<span style="display:flex;gap:7px;font-size:10.5px;font-weight:800;color:#9A927E">W M Q Y</span>'
    rr = "".join(f'<div style="display:grid;grid-template-columns:2.1fr 1.35fr 0.95fr 0.95fr 1.2fr;gap:8px;padding:0 12px;height:31px;align-items:end"><span class="wl" style="height:22px"></span><span style="border-bottom:1.3px solid {LINE};height:22px;display:flex;align-items:center">{often}</span><span class="wl" style="height:22px;font-size:11px;font-weight:700;color:#9A927E">$</span><span class="wl" style="height:22px;font-size:11px;font-weight:700;color:#9A927E">$</span><span class="wl" style="height:22px"></span></div>' for _ in range(rows))
    forgot = ["Car registration", "Car service and tires", "Insurance renewals", "Water and trash", "Annual subscriptions",
              "Streaming and apps", "School fees, photos, trips", "Back-to-school", "Birthdays and gifts", "Christmas and holidays",
              "Dentist and eye checks", "Pet food, vet, meds", "Kids’ sports and activities", "Haircuts", "Property tax or HOA"]
    fg = "".join(f'<div style="display:flex;gap:8px;align-items:center;font-size:11.5px;font-weight:600"><span class="box" style="width:12px;height:12px;border-width:1.5px"></span>{x}</div>' for x in forgot)
    steps = ["Grab 3 months of bank statements.", "Highlight every payment that repeats.", "Write each one in the list.", "Divide it (page 3) for the per-payday number."]
    sp = "".join(f'<div style="display:flex;gap:8px;align-items:flex-start;flex:1">{numdot(i+1, NAVY, s=20, fs=10.5)}<span style="font-size:11.5px;font-weight:700;line-height:1.35">{s}</span></div>' for i, s in enumerate(steps))
    body = f'''{title("The Bill Finder", "Find every bill, even the sneaky ones. Then turn each one into a per-payday number.")}
<div style="display:flex;gap:12px">{sp}</div>
<div style="margin-top:14px;display:flex;gap:14px;align-items:stretch">
<div style="flex:1;background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;overflow:hidden;padding-bottom:12px">{hdr}{rr}
<div style="margin:14px 12px 0;border:2px solid {GOLD};border-radius:12px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center"><span class="serif" style="font-size:14.5px;color:{NAVY}">Total per payday</span><span style="display:flex;align-items:flex-end;gap:4px;font-weight:800">$<span class="wl" style="width:110px;height:20px"></span></span></div></div>
<div style="flex:none;width:208px;display:flex;flex-direction:column;gap:12px">
<div style="background:{TRED};border-radius:14px;padding:13px 14px;display:flex;flex-direction:column;gap:7px"><div style="display:flex;align-items:center;gap:7px">{icon("warn", RED, 17)}<span class="eyebrow" style="color:{RED};font-size:10px;letter-spacing:1.5px">Bills people forget</span></div>{fg}</div>
<div style="background:{CREAM};border-radius:14px;padding:12px 14px;font-size:11.5px;font-weight:600;line-height:1.5"><b style="color:{NAVY}">W M Q Y</b> = weekly, monthly, quarterly, yearly. Circle one.<br><br><b style="color:{NAVY}">Which account?</b> Leave it blank for now. You’ll fill it in on page 6.</div>
<div class="cav" style="font-size:22px;line-height:1.05;color:{GREEN};transform:rotate(-2deg);padding:0 4px">If it surprised you last year, it goes on the list.</div></div></div>'''
    return page(4, 1, body)

PAGES_A = [p_cover, p_welcome, p_lesson1, p_billfinder]
