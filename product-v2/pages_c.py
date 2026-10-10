from base import *

MODES = ["Guided", "Hints", "Prompts", "Solo"]

HELP_FULL = [
    "Copy your Bills number from page 6. Move it to your bill accounts, or pay what’s due before next payday.",
    "Every minimum first. Any extra goes to the smallest balance.",
    "Move it now, before you can spend it. It’s a bill you pay yourself.",
    "Move it into its own account. Out of sight, out of reach.",
    "Plan groceries, gas, kids and fun from what’s left after steps 1 to 4.",
    "Paycheck minus steps 1 to 5. $100 or more? If not, trim step 5.",
]
HELP_HINT = ["from page 6", "minimums first", "move it first", "out of sight", "from what’s left", "$100 or more?"]

def wl(w, h=20, c=LINE):
    return f'<span style="display:inline-block;width:{w}px;height:{h}px;border-bottom:1.4px solid {c}"></span>'

def progress(n):
    out = ""
    for i, m in enumerate(MODES):
        on = i == n - 1
        done = i < n - 1
        bg = GOLDB if on else ("#fff")
        bd = GOLDB if on else "#E2DCCB"
        fg = NAVY if on else (GREEN if done else "#9A927E")
        mark = tick(GREEN, 13) if done else ""

        out += f'<div style="flex:1;display:flex;align-items:center;justify-content:center;gap:6px;background:{bg};border:1.5px solid {bd};border-radius:999px;padding:6px 0;color:{fg};font-size:11px;font-weight:900;letter-spacing:1.5px">{mark}<span>DRILL {i+1} · {m.upper()}</span></div>'
    return f'<div style="display:flex;gap:7px">{out}</div>'

def step_row(i, mode):
    k, n, c, t, what, rule = BUCKETS[i]
    if mode == 4:
        lab = f'<div style="display:flex;flex-direction:column;gap:2px;flex:1"><span style="font-size:9.5px;font-weight:800;color:#9A927E;letter-spacing:1px">BUCKET {i+1}</span>{wl(150, 18)}</div>'
        dot = numdot(i + 1, "#fff", NAVY, s=28, fs=13).replace("background:#fff", f"background:#fff;border:2px solid {NAVY}")
        bg = "#fff"
    else:
        helpt = ""
        if mode == 1:
            helpt = f'<span style="font-size:11px;font-weight:600;line-height:1.38;color:#3C4250">{HELP_FULL[i]}</span>'
        elif mode == 2:
            helpt = f'<span style="font-size:11px;font-weight:700;color:{GREY};font-style:italic">{HELP_HINT[i]}</span>'
        lab = f'<div style="display:flex;flex-direction:column;gap:3px;flex:1;min-width:0"><span style="display:flex;align-items:center;gap:7px">{icon(k, c, 17) if mode < 3 else ""}<span style="font-size:13.5px;font-weight:900;color:{c};text-transform:uppercase;letter-spacing:.4px">{n}</span></span>{helpt}</div>'
        dot = numdot(i + 1, c, s=28, fs=13)
        bg = t if mode == 1 else "#fff"
    done = "Moved" if i < 4 else ("Planned" if i == 4 else "$100+")
    pad = "10px 12px" if mode == 1 else "11px 12px"
    mh = {1: 0, 2: 70, 3: 74, 4: 76}[mode]
    return f'''<div style="display:flex;align-items:center;gap:11px;background:{bg};border:1.5px solid {t if mode != 4 else "#E2DCCB"};border-radius:12px;padding:{pad};min-height:{mh}px">
{dot}{lab}
<span style="flex:none;display:flex;align-items:flex-end;gap:4px;font-size:13px;font-weight:800;color:{INK}">${wl(74, 22)}</span>
<span style="flex:none;width:52px;display:flex;flex-direction:column;align-items:center;gap:3px;font-size:9px;font-weight:800;color:{GREY};letter-spacing:.5px"><span class="box" style="width:15px;height:15px"></span>{done.upper()}</span></div>'''

def worked():
    rows = [("1 Bills", "1,200"), ("2 Debt", "100"), ("3 Savings", "150"), ("4 Don’t Touch", "80"), ("5 Everyday", "870"), ("6 Buffer", "100")]
    rr = "".join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid #DCE3EE;padding:1px 0"><span class="cav" style="font-size:20px;color:{NAVY}">{a}</span><span class="cav" style="font-size:20px;color:{NAVY}">${b} <span style="color:{GREEN}">✓</span></span></div>' for a, b in rows)
    return f'''<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:4px;transform:rotate(-1deg);box-shadow:4px 4px 0 {CREAM}">
<span class="eyebrow" style="font-size:9.5px;color:{GREEN}">Worked example</span>
<span style="font-size:10.5px;font-weight:700;color:{GREY};line-height:1.35">A family of four, paid $2,500 every two weeks.</span>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:2px"><span class="cav" style="font-size:21px;color:{BLACK}">Paycheck</span><span class="cav" style="font-size:21px;color:{BLACK}">$2,500</span></div>
{rr}
<span class="cav" style="font-size:17px;line-height:1.1;color:{RED};margin-top:4px">Bills = rent $900 + 7 smaller bills, straight from page 6</span>
<span class="cav" style="font-size:17px;line-height:1.1;color:{RED}">2,500 − 2,400 = $100 buffer</span>
<span style="font-size:9.5px;font-weight:600;color:{GREY};margin-top:2px">Example figures only.</span></div>'''

def coach(n):
    hd = lambda t, c=NAVY: f'<span class="serif" style="font-size:15px;color:{c}">{t}</span>'
    if n == 1:
        return worked() + f'''<div style="background:{CREAM};border-radius:14px;padding:12px 14px;font-size:11.5px;font-weight:600;line-height:1.5"><b style="color:{NAVY}">When do I do the drills?</b> One per payday. Paid weekly? These are your next four weeks. Every two weeks? Your next eight.</div>'''
    if n == 2:
        slips = ["Spending on Everyday before the transfers go", "A quarterly bill with no bucket", "The buffer gone by day three"]
        sl = "".join(f'<div style="display:flex;gap:8px;align-items:flex-start;font-size:11.5px;font-weight:600;line-height:1.4">{xmark(RED, 13)}<span>{x}</span></div>' for x in slips)
        return f'''<div style="background:{NAVY};border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:7px;color:#fff">
<span class="eyebrow" style="font-size:9.5px;color:{GOLDB}">Before you start</span>
<span style="font-size:12.5px;font-weight:700;line-height:1.45">Cover page 5 with your hand. Say the six buckets out loud, in order.</span>
<span class="serif" style="font-size:14px;line-height:1.4;color:{GOLDB}">Pay the bills. Pay the debt. Pay yourself. Guard the rest.</span></div>
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;padding:13px 15px;display:flex;flex-direction:column;gap:8px">{hd("Watch for these")}{sl}</div>
<div style="background:{CREAM};border-radius:14px;padding:11px 14px;font-size:11px;font-weight:600;line-height:1.5">Stuck? Peek at Drill 1 on page 8. Then try the next step without looking.</div>'''
    if n == 3:
        mem = "".join(f'<div style="display:flex;align-items:flex-end;gap:6px;font-size:12px;font-weight:800;color:{c}"><span style="flex:1">{nm}</span>${wl(66, 18)}</div>' for k, nm, c, t, w, r in BUCKETS[:4])
        return f'''<div style="background:#fff;border:2px dashed {GOLD};border-radius:14px;padding:13px 15px;display:flex;flex-direction:column;gap:8px">
<span class="eyebrow" style="font-size:9.5px;color:#8A6D12">Memory test first</span>
<span style="font-size:11.5px;font-weight:600;line-height:1.45">Without looking at page 6, write your bucket amounts from memory.</span>
{mem}
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:4px;font-size:12px;font-weight:800;color:{NAVY}"><span>Right first time</span><span>{wl(30, 18)} / 4</span></div></div>
<div style="background:{CREAM};border-radius:14px;padding:12px 14px;font-size:11.5px;font-weight:600;line-height:1.5">Now check page 6. Fix any you missed in a different colour. The ones you got wrong are the ones you’ll remember next time.</div>'''
    checks = ["I can name the 6 buckets in order without looking",
              "My bucket transfers are automatic",
              "I know my safe-to-spend number by heart",
              "This took under 15 minutes",
              "The buffer was still there at the last payday"]
    ck = "".join(f'<div style="display:flex;gap:9px;align-items:flex-start;font-size:11.5px;font-weight:700;line-height:1.38"><span class="box" style="width:14px;height:14px;margin-top:1px;border-color:{GREEN}"></span><span>{x}</span></div>' for x in checks)
    return f'''<div style="background:#fff;border:2px solid {GREEN};border-radius:14px;padding:14px 15px;display:flex;flex-direction:column;gap:9px">
<span class="serif" style="font-size:16px;color:{GREEN}">Graduation check</span>{ck}</div>
<div style="background:{GREEN};border-radius:14px;padding:12px 15px;color:#fff;font-size:11.5px;font-weight:600;line-height:1.5"><b style="color:{GOLDB}">4 or 5 ticked?</b> You’ve graduated. Turn to page 12 and fill in your Payday Routine Card.<br><b style="color:{GOLDB}">Fewer?</b> No reprinting. Run your next payday on the spreadsheet’s Payday tab, then check again.</div>'''

LESSONS = [
    "The order never changes. That’s what makes it automatic.",
    "Transfers go out the day the pay lands. Not tomorrow.",
    "Spending comes last, from what’s left. Never the other way round.",
    "You don’t need this page anymore. You’ve got this.",
]
SUBS = [
    "Do this on your next payday. Every step is explained.",
    "Same six steps. This time, just hints.",
    "Just the bucket names now. Test your memory first.",
    "No help. Write the buckets from memory and time yourself.",
]

def drill(n):
    steps = "".join(step_row(i, n) for i in range(6))
    write_note = f'<div style="font-size:11.5px;font-weight:700;color:{NAVY};margin-bottom:2px">Write the six buckets in order, from memory. Then fill in the amounts.</div>' if n == 4 else ""
    bar = f'''<div style="margin-top:12px;background:{NAVY};color:#fff;border-radius:12px;padding:10px 16px;display:flex;justify-content:space-between;align-items:flex-end;font-size:12px;font-weight:700">
<span style="display:flex;align-items:flex-end;gap:6px">Pay date<span style="display:inline-block;width:92px;border-bottom:1.5px solid #8DA2C4;height:17px"></span></span>
<span style="display:flex;align-items:flex-end;gap:6px">Paycheck $<span style="display:inline-block;width:92px;border-bottom:1.5px solid #8DA2C4;height:17px"></span></span>
<span style="display:flex;align-items:flex-end;gap:6px">{icon("clock", GOLDB, 15)}Started at<span style="display:inline-block;width:70px;border-bottom:1.5px solid #8DA2C4;height:17px"></span></span></div>'''
    feel = "".join(f'<span style="width:22px;height:22px;border-radius:50%;border:1.6px solid {NAVY};display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:{NAVY}">{j}</span>' for j in range(1, 6))
    bottom = f'''<div style="margin-top:12px;display:grid;grid-template-columns:1.5fr 1fr;gap:12px">
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:12px;padding:10px 14px;display:flex;flex-direction:column;gap:4px">
<span style="font-size:11.5px;font-weight:800;color:{NAVY}">Anything due before next payday that isn’t in a bucket?</span>
<span class="wl" style="height:20px"></span><span class="wl" style="height:20px"></span></div>
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:12px;padding:10px 14px;display:flex;flex-direction:column;gap:9px;font-size:11.5px;font-weight:800;color:{NAVY}">
<span style="display:flex;align-items:flex-end;gap:6px">Time taken{wl(46, 17)}min</span>
<span style="display:flex;flex-direction:column;gap:5px">How sure did it feel?<span style="display:flex;gap:6px">{feel}</span></span></div></div>
<div style="margin-top:10px;background:{TNAVY};border-radius:12px;padding:10px 16px;display:flex;align-items:center;gap:16px;font-size:11.5px;font-weight:800;color:{NAVY}">
<span style="flex:none;font-size:10px;font-weight:900;letter-spacing:1.5px;line-height:1.3">MID-WEEK<br>CHECK</span>
<span style="display:flex;align-items:flex-end;gap:5px">Everyday left ${wl(56, 17)}</span>
<span style="display:flex;align-items:center;gap:6px">Buffer still there?<span class="box" style="width:13px;height:13px"></span>Yes<span class="box" style="width:13px;height:13px"></span>No</span>
<span style="display:flex;align-items:flex-end;gap:5px;flex:1">Watch out for<span class="wl" style="flex:1;height:17px"></span></span></div>
<div style="margin-top:10px;display:flex;align-items:center;gap:12px;background:{GOLDB};border-radius:12px;padding:9px 16px">
<span style="flex:none;font-size:10px;font-weight:900;letter-spacing:2px;color:{NAVY}">TODAY’S LESSON</span>
<span class="serif" style="font-size:14px;line-height:1.35;color:{NAVY}">{LESSONS[n-1]}</span></div>'''
    body = f'''{title(f"Payday Drill {n}: {MODES[n-1]}", SUBS[n-1])}
{progress(n)}{bar}
<div style="margin-top:12px;display:flex;gap:14px;align-items:flex-start">
<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:7px">{write_note}{steps}</div>
<div style="flex:none;width:236px;display:flex;flex-direction:column;gap:11px">{coach(n)}</div></div>
{bottom}'''
    return page(7 + n, 3, body)

# ---------------- 12. ROUTINE CARD ----------------
def p_routine():
    steps = ""
    for i, (k, n, c, t, w, r) in enumerate(BUCKETS):
        steps += f'''<div style="display:flex;align-items:center;gap:12px;padding:7px 0;border-bottom:1px solid #EEE8DA">
{numdot(i+1, c, s=28, fs=13)}<span style="display:flex;align-items:center;gap:7px;flex:1">{icon(k, c, 19)}<span style="font-size:15px;font-weight:900;color:{c};text-transform:uppercase">{n}</span></span>
<span style="font-size:14px;font-weight:800">${wl(110, 22)}</span><span class="box" style="width:17px;height:17px"></span></div>'''
    scis = f'<span style="position:absolute;top:-11px;left:24px;background:{OFF};padding:0 4px;display:flex">{icon("scissors", GREY, 18)}</span>'
    card = f'''<div style="position:relative;border:2px dashed #A79F8A;border-radius:22px;padding:12px">{scis}
<div style="background:#fff;border-radius:16px;overflow:hidden;border:1.5px solid #E2DCCB">
<div style="background:{NAVY};color:#fff;padding:14px 22px;display:flex;justify-content:space-between;align-items:center">
<span class="serif" style="font-size:22px">My Payday Routine</span>
<span style="display:flex;align-items:flex-end;gap:6px;font-size:12px;font-weight:700">Payday<span style="display:inline-block;width:100px;border-bottom:1.5px solid #8DA2C4;height:17px"></span></span></div>
<div style="padding:6px 22px 14px">{steps}
<div style="margin-top:12px;display:flex;justify-content:space-between;align-items:center;background:{TGREEN};border-radius:12px;padding:10px 16px"><span style="font-size:13px;font-weight:900;color:{GREEN}">SAFE TO SPEND UNTIL NEXT PAYDAY</span><span style="font-size:16px;font-weight:900;color:{GREEN}">${wl(110, 22, GREEN)}</span></div>
<div class="serif" style="margin-top:10px;text-align:center;font-size:14px;color:{NAVY}">Pay the bills. Pay the debt. Pay yourself. <span style="color:#8A6D12">Guard the rest.</span></div></div></div></div>'''
    def mini(head, color, lines):
        li = "".join(f'<div style="display:flex;gap:7px;font-size:11.5px;font-weight:700;line-height:1.38">{x}</div>' for x in lines)
        return f'''<div style="position:relative;border:2px dashed #A79F8A;border-radius:18px;padding:9px">{scis.replace("left:24px","left:18px")}
<div style="background:#fff;border-radius:12px;border:1.5px solid #E2DCCB;overflow:hidden"><div style="background:{color};color:#fff;padding:8px 14px;font-size:11.5px;font-weight:900;letter-spacing:2px">{head}</div>
<div style="padding:10px 14px 12px;display:flex;flex-direction:column;gap:5px">{li}</div></div></div>'''
    pause = mini("THE PAUSE RULE", GREEN, ["Before I buy anything, I ask:", "<b>1.</b> Is it in Everyday?", "<b>2.</b> Is there room left in Everyday?", "If not, it waits until next payday."])
    surprise = mini("SURPRISE BILL?", RED, ["<b>1.</b> Its own bucket", "<b>2.</b> Don’t Touch", "<b>3.</b> The buffer", "<b>4.</b> Pause extras. Never skip a bill."])
    body = f'''{title("Your Payday Routine", "You’ve graduated. This card replaces the drill pages, for good.")}
<div style="display:flex;gap:16px;align-items:center;margin-bottom:14px">
<div style="flex:1;font-size:13px;font-weight:500;line-height:1.55">You don’t need a new budget every payday. You need the same ten minutes. Fill in your numbers, cut along the dashes, and <b>laminate it</b> or slip it into a dry-erase sleeve. Stick it on the fridge and snap a photo for your phone.</div>
<div class="cav" style="flex:none;width:190px;font-size:23px;line-height:1.05;color:{GREEN};transform:rotate(-2deg)">same order, every payday, for good</div></div>
{card}
<div style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:14px">{pause}{surprise}</div>
<div style="margin-top:12px;font-size:11px;font-weight:600;color:{GREY};text-align:center">Pay changed or a new bill turned up? Redo page 6 (or the spreadsheet’s My Budget tab) and update this card in pencil.</div>
<div style="margin-top:18px;display:flex;align-items:flex-end;gap:12px;border-top:2px solid {GOLD};padding-top:14px">
<span class="cav" style="flex:none;font-size:26px;color:{NAVY}">We graduated on</span><span class="wl" style="flex:1;height:24px"></span>
<span class="cav" style="flex:none;font-size:26px;color:{NAVY}">signed</span><span class="wl" style="flex:1.4;height:24px"></span></div>'''
    return page(12, 4, body)

# ---------------- 13. 30-DAY CHALLENGE ----------------
TASKS = [
    "Read pages 2 and 3", "Pull up 3 months of bank statements", "Highlight every payment that repeats", "Fill in the Bill Finder (page 4)",
    "Hunt down 3 bills you forgot", "Do the Year of Paydays (page 7)", "Rest day. Just look at your list.",
    "Read the 6 Buckets (page 5)", "Open or name your bucket accounts", "Fill in Bucket Setup (page 6)", "Set up the automatic transfers",
    "Put your bills in the spreadsheet", "Show your partner the Payday Number", "Rest day",
    "Check: did every transfer go out?", "Buffer check. Still $100+?", "No-spend day", "Cancel one thing you don’t use",
    "Shop from a list only", "Say the 6 buckets from memory", "Rest day",
    "Check every bucket account balance", "No-spend day", "Log this week’s spending", "Move any leftover to Don’t Touch",
    "Plan your next extra payday", "Do the monthly check-in (page 15)", "Rest day",
    "Fill in your Routine Card (page 12)", "Celebrate. Something free, together.",
]

def p_challenge():
    weeks = {0: ("FIND IT", NAVY), 7: ("BUILD IT", GREEN), 14: ("RUN IT", "#8A6D12"), 21: ("OWN IT", RED), 28: ("LOCK IT", BLACK)}
    tiles = ""
    for d, t in enumerate(TASKS):
        rest = t.startswith("Rest day")
        wk = max(k for k in weeks if k <= d)
        c = weeks[wk][1]
        bg = CREAM if rest else "#fff"
        tiles += f'''<div style="background:{bg};border:1.5px solid {"#E2DCCB" if not rest else CREAM};border-top:4px solid {c};border-radius:10px;padding:7px 8px 8px;display:flex;flex-direction:column;gap:5px;height:104px">
<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-size:10px;font-weight:900;letter-spacing:1px;color:{c}">DAY {d+1}</span><span class="box" style="width:15px;height:15px;border-color:{c}"></span></div>
<span style="font-size:11px;font-weight:{600 if rest else 700};line-height:1.32;color:{GREY if rest else INK}">{t}</span></div>'''
    legend = "".join(f'<span style="display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:800;color:{c}"><span style="width:14px;height:5px;background:{c};border-radius:2px"></span>Days {k+1}–{min(k+7,30)} · {lab}</span>' for k, (lab, c) in weeks.items())
    body = f'''{title("The 30-Day Lock-In Challenge", "One small thing a day. By day 30, this is just how your family does money.")}
<div style="display:grid;grid-template-columns:1fr 1.4fr 1.3fr;gap:10px;margin-bottom:10px">
<div style="background:{NAVY};color:#fff;border-radius:12px;padding:10px 14px;font-size:12px;font-weight:700;display:flex;align-items:flex-end;gap:6px">Start date<span style="display:inline-block;flex:1;border-bottom:1.5px solid #8DA2C4;height:17px"></span></div>
<div style="background:{GOLDB};color:{NAVY};border-radius:12px;padding:8px 14px;font-size:11px;font-weight:800;line-height:1.4;display:flex;gap:8px;align-items:center">{icon("star", NAVY, 18)}<span>Payday during the challenge? Do your next drill that day too.</span></div>
<div style="background:{TGREEN};color:{GREEN};border-radius:12px;padding:8px 14px;font-size:11px;font-weight:800;line-height:1.4;display:flex;align-items:center">Missed a day? Don’t restart. Just do today’s.</div></div>
<div style="display:flex;flex-wrap:wrap;gap:6px 14px;margin-bottom:8px">{legend}</div>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px">{tiles}</div>
<div style="margin-top:12px;display:grid;grid-template-columns:1fr 1.6fr;gap:12px">
<div style="background:#fff;border:2px solid {GOLD};border-radius:12px;padding:10px 16px;display:flex;align-items:flex-end;justify-content:space-between;font-size:13px;font-weight:800;color:{NAVY}">Days done<span>{wl(44, 20)} / 30</span></div>
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:12px;padding:10px 16px;display:flex;align-items:flex-end;gap:8px;font-size:12px;font-weight:800;color:{NAVY}"><span style="flex:none">Our day-30 reward</span><span class="wl" style="flex:1;height:20px"></span></div></div>'''
    return page(13, 4, body)

# ---------------- 14. WHEN LIFE HAPPENS ----------------
def p_life():
    def card(head, c, tint, ico, items, numbered=True):
        li = "".join(f'<div style="display:flex;gap:8px;align-items:flex-start;font-size:11.5px;font-weight:600;line-height:1.42">{numdot(j+1, c, s=18, fs=9.5) if numbered else tick(c, 14)}<span>{x}</span></div>' for j, x in enumerate(items))
        return f'''<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;overflow:hidden;display:flex;flex-direction:column">
<div style="background:{tint};padding:9px 14px;display:flex;align-items:center;gap:8px">{icon(ico, c, 19)}<span class="serif" style="font-size:15px;color:{c}">{head}</span></div>
<div style="padding:10px 14px 12px;display:flex;flex-direction:column;gap:6px">{li}</div></div>'''
    surprise = card("A surprise bill", RED, TRED, "warn", [
        "Is there a bucket for it? Use that first.",
        "No bucket? That’s exactly what Don’t Touch is for.",
        "Not enough? Use the buffer.",
        "Still short? Pause extra debt payments and savings this payday. Keep every minimum and every bill.",
        "Afterwards, give it a bucket so it never surprises you again."])
    over = card("We overspent on Everyday", BROWN, TGOLD, "everyday", [
        "Don’t raid the bill accounts. That money’s already spoken for.",
        "Live on a little less until next payday, not on credit.",
        "Try a no-spend week (below).",
        "Ask what pulled you off track. Write it on the fridge."], numbered=False)
    extra = card("An extra paycheck", GREEN, TGREEN, "star", [
        "It’s a head start, not a bonus to spend.",
        "Decide where it goes before it lands (page 7).",
        "Ideas: top up Don’t Touch, pay extra on the smallest debt, or get a bill ahead."], numbered=False)
    cut = card("Hours cut or pay went down", NAVY, TNAVY, "bills", [
        "Redo page 6 or the spreadsheet with the new number.",
        "Trim in this order: fun money, extra debt payments, then savings (keep even $5 going).",
        "Bills and minimums stay. Always."], numbered=False)
    partner = card("My partner isn’t on board", BLACK, TBLACK, "savings", [
        "Show them one number: what’s safe to spend.",
        "Do payday together. Ten minutes, same time, every payday.",
        "It’s a plan, not a punishment."], numbered=False)
    used = card("We had to use Don’t Touch", "#8A6D12", "#FBF3D9", "buffer", [
        "Good. That’s exactly what it’s for.",
        "Top it back up first, before anything extra.",
        "Ask: should this have had its own bucket?"], numbered=False)
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    ns = "".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:4px"><span style="font-size:9.5px;font-weight:900;letter-spacing:1px;color:{GREEN}">{d}</span><span style="width:34px;height:34px;border-radius:50%;border:2px solid {GREEN};background:#fff"></span></div>' for d in days)
    body = f'''{title("When Life Happens", "Things will go wrong. Here’s what to do, so one bad week doesn’t undo the whole plan.")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:11px">
<div style="display:flex;flex-direction:column;gap:11px">{surprise}{extra}{used}</div>
<div style="display:flex;flex-direction:column;gap:11px">{over}{cut}{partner}</div></div>
<div style="margin-top:12px;background:#fff;border:2px solid {GREEN};border-radius:14px;padding:11px 16px">
<div style="display:flex;justify-content:space-between;align-items:center"><span class="serif" style="font-size:15px;color:{GREEN}">No-Spend Week</span><span style="font-size:11px;font-weight:700;color:{GREY}">Colour in each day you spend $0 outside your bills.</span></div>
<div style="margin-top:8px;display:flex;gap:8px">{ns}</div>
<div style="margin-top:8px;display:flex;align-items:flex-end;gap:8px;font-size:11.5px;font-weight:800;color:{NAVY}">We kept about ${wl(60, 18)} and moved it to<span class="wl" style="flex:1;height:18px"></span></div></div>
<div style="margin-top:12px;background:{GOLDB};border-radius:12px;padding:11px 18px;text-align:center"><span class="serif" style="font-size:15px;color:{NAVY}">The goal isn’t a perfect month. It’s being back on the routine by next payday.</span></div>'''
    return page(14, 4, body)

# ---------------- 15. CHECK-IN + TRACKERS ----------------
def p_checkin():
    qs = [
        ("Did every transfer go out on payday?", '<span style="display:flex;gap:14px;font-size:11.5px;font-weight:700">' + "".join(f'<span style="display:flex;align-items:center;gap:5px"><span class="box" style="width:13px;height:13px"></span>{x}</span>' for x in ["Yes", "Mostly", "No"]) + "</span>"),
        ("Was there a bill that wasn’t in a bucket?", None),
        ("How much buffer was left before each payday?", None),
        ("What surprised us this month?", None),
        ("One thing we’ll change next month:", None),
        ("One win to celebrate:", None),
    ]
    qq = "".join(f'<div style="display:flex;gap:10px;align-items:flex-end">{numdot(i+1, NAVY, s=22, fs=11)}<span style="flex:none;font-size:12px;font-weight:700">{q}</span>{a if a else "<span class=wl style=flex:1;height:20px></span>"}</div>' for i, (q, a) in enumerate(qs))
    def boxes(c, n=25):
        return f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:5px">' + "".join(f'<span style="height:30px;border:1.6px solid {c};border-radius:5px;background:#fff"></span>' for _ in range(n)) + "</div>"
    def tracker(head, c, tint, ico, inner):
        return f'''<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;overflow:hidden;display:flex;flex-direction:column">
<div style="background:{tint};padding:9px 14px;display:flex;align-items:center;gap:8px">{icon(ico, c, 18)}<span style="font-size:12px;font-weight:900;letter-spacing:1px;color:{c}">{head}</span></div>
<div style="padding:10px 14px 12px;display:flex;flex-direction:column;gap:8px;flex:1">{inner}</div></div>'''
    goal = lambda c: f'<div style="display:flex;flex-direction:column;gap:6px;font-size:11px;font-weight:800;color:{c};white-space:nowrap"><span style="display:flex;align-items:flex-end;gap:4px">Goal $<span class="wl" style="flex:1;height:16px"></span></span><span style="display:flex;align-items:flex-end;gap:4px">Each box $<span class="wl" style="flex:1;height:16px"></span></span></div>'
    touch = tracker("DON’T TOUCH FUND", RED, TRED, "touch", goal(RED) + boxes(RED) + f'<span style="font-size:10.5px;font-weight:600;color:{GREY};line-height:1.4">Colour a box each time it grows. Start with a small first goal, like $500, then keep going.</span>')
    save = tracker("SAVINGS GOAL", GREEN, TGREEN, "savings", f'<div style="display:flex;align-items:flex-end;gap:6px;font-size:11px;font-weight:800;color:{GREEN}">For{wl(150, 16)}</div>' + goal(GREEN) + boxes(GREEN))
    drows = "".join(f'<div style="display:grid;grid-template-columns:1.4fr 1fr 22px;gap:8px;align-items:end"><span class="wl" style="height:20px"></span><span style="display:flex;align-items:flex-end;gap:3px;font-size:11px;font-weight:700;color:{GREY}">$<span class="wl" style="flex:1;height:20px"></span></span><span class="box" style="width:15px;height:15px;border-color:{BLACK}"></span></div>' for _ in range(7))
    debt = tracker("DEBT SNOWBALL", BLACK, TBLACK, "debt", f'<div style="display:grid;grid-template-columns:1.4fr 1fr 22px;gap:8px;font-size:9px;font-weight:900;letter-spacing:1px;color:{GREY}"><span>DEBT</span><span>BALANCE</span><span>PAID</span></div>' + drows + f'<span style="font-size:10.5px;font-weight:600;color:{GREY};line-height:1.4">Smallest balance at the top. Pay it off, tick it, roll that payment into the next one.</span>')
    body = f'''{title("The 10-Minute Monthly Check-In", "Once a month, sit down together. Ten minutes, six questions. Then look at how far you’ve come.")}
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;padding:14px 18px;display:flex;flex-direction:column;gap:15px">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><span class="serif" style="font-size:16px;color:{NAVY}">This month</span><span style="display:flex;align-items:flex-end;gap:6px;font-size:12px;font-weight:700">Month{wl(120, 18)}</span></div>
{qq}</div>
<div class="eyebrow" style="margin-top:16px;color:{NAVY}">Watch it grow</div>
<div style="margin-top:8px;display:grid;grid-template-columns:repeat(3,1fr);gap:11px">{touch}{save}{debt}</div>
<div style="margin-top:14px;display:flex;align-items:center;justify-content:space-between;gap:16px;background:{NAVY};border-radius:14px;padding:13px 20px;color:#fff">
<span style="font-size:12px;font-weight:600;line-height:1.5;color:#DCE3EE">Next month? Use the Check-In tab in the spreadsheet, or print just this page. Everything else in this workbook you only ever print once.</span>
<span class="cav" style="flex:none;font-size:26px;color:{GOLDB}">proud of you</span></div>'''
    return page(15, 4, body)

PAGES_C = [lambda: drill(1), lambda: drill(2), lambda: drill(3), lambda: drill(4), p_routine, p_challenge, p_life, p_checkin]
