from base import *

# ---------------- 5. LESSON 2: THE 6 BUCKETS ----------------
def p_lesson2():
    rows = ""
    for i, (k, n, c, t, what, rule) in enumerate(BUCKETS):
        rows += f'''<div style="display:grid;grid-template-columns:44px 150px 1fr 1.15fr;align-items:center;gap:12px;background:{t};border-radius:12px;padding:9px 14px">
{numdot(i+1, c, s=30, fs=15)}
<div style="display:flex;align-items:center;gap:8px">{icon(k, c, 22)}<span style="font-size:15px;font-weight:900;color:{c};text-transform:uppercase;letter-spacing:.5px">{n}</span></div>
<span style="font-size:12px;font-weight:600;line-height:1.35;color:{INK}">{what}</span>
<span style="font-size:12px;font-weight:800;line-height:1.35;color:{c}">{rule}</span></div>'''
    body = f'''{title("The 6 Buckets", "Every payday fills the same six buckets, in the same order. Every single time.", kicker="Lesson 2")}
<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
<span style="background:{GREEN};color:#fff;border-radius:999px;padding:7px 20px;font-size:12px;font-weight:900;letter-spacing:3px">PAYDAY</span>
<svg width="60" height="14" viewBox="0 0 60 14" fill="none" stroke="{GREEN}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 7 H56 M50 2 L56 7 L50 12"/></svg>
<span style="font-size:12.5px;font-weight:700;color:{GREY}">fills them top to bottom. Spending money is never first.</span></div>
<div style="display:grid;grid-template-columns:44px 150px 1fr 1.15fr;gap:12px;padding:0 14px 5px;font-size:9.5px;font-weight:900;letter-spacing:1.5px;color:{GREY}"><span></span><span>BUCKET</span><span>WHAT GOES IN IT</span><span>THE RULE</span></div>
<div style="display:flex;flex-direction:column;gap:7px">{rows}</div>
<div style="margin-top:16px;display:grid;grid-template-columns:1fr 1.25fr;gap:14px">
<div style="background:{NAVY};border-radius:14px;padding:16px 20px;display:flex;flex-direction:column;gap:8px">
<span class="eyebrow" style="color:#C3CCDB;font-size:10px">The line to remember</span>
<span class="serif" style="font-size:21px;line-height:1.3;color:#fff">Pay the bills.<br>Pay the debt.<br>Pay yourself.<br><span style="color:{GOLDB}">Guard the rest.</span></span>
<span style="font-size:11.5px;font-weight:600;line-height:1.45;color:#DCE3EE">Say it out loud on payday. By the fourth time, you won’t need this page.</span></div>
<div style="background:#fff;border:2px solid {GREEN};border-radius:14px;padding:15px 18px;display:flex;flex-direction:column;gap:7px">
<span class="serif" style="font-size:16px;color:{GREEN}">Our trick: bill accounts</span>
<span style="font-size:12px;font-weight:500;line-height:1.55">Open a few free online savings accounts (or “spaces”, if your bank has them) and name each one: <b>CAR</b>, <b>UTILITIES</b>, <b>PHONE</b>, <b>DON’T TOUCH</b>, <b>SAVINGS</b>. Set an automatic transfer into each one on payday.</span>
<span style="font-size:12px;font-weight:500;line-height:1.55">When a big bill arrives, its account pays it. And you stop seeing money that’s already spoken for, so you stop spending it.</span>
<span style="font-size:11px;font-weight:700;line-height:1.45;color:{GREY}">Rent and debt minimums can still come straight out of your main account.</span></div></div>
<div style="margin-top:14px;background:{TRED};border-radius:14px;padding:12px 18px;display:flex;gap:16px;align-items:center">
<div style="flex:none;display:flex;align-items:center;gap:8px">{icon("touch", RED, 24)}<span style="font-size:12px;font-weight:900;letter-spacing:1.5px;color:{RED};line-height:1.25">THE DON’T<br>TOUCH RULES</span></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;font-size:11.5px;font-weight:600;line-height:1.4">
<span><b>1.</b> It’s for things that break or bleed. Not sales, not takeout.</span>
<span><b>2.</b> Keep it in its own account you don’t look at every day.</span>
<span><b>3.</b> Used it? Top it back up before anything extra.</span></div></div>'''
    return page(5, 2, body)

# ---------------- 6. BUCKET SETUP ----------------
def p_setup():
    def card(i):
        k, n, c, t, what, rule = BUCKETS[i]
        head = f'<div style="background:{c};color:#fff;padding:8px 14px;display:flex;align-items:center;gap:9px"><span style="font-size:17px;font-weight:900">{i+1}</span>{icon(k, "#fff", 18)}<span style="font-size:12.5px;font-weight:900;letter-spacing:1.5px;text-transform:uppercase">{n}</span></div>'
        lab = lambda s: f'<span style="flex:none;font-size:11px;font-weight:700;color:{GREY}">{s}</span>'
        line = lambda s, w=None: f'<div style="display:flex;align-items:flex-end;gap:8px">{lab(s)}<span class="wl" style="flex:1;height:20px"></span></div>'
        if i < 4:
            inner = f'''{line("Account name")}{line("Pays for")}<div class="wl" style="height:20px"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:2px"><span style="display:flex;align-items:flex-end;gap:6px;font-size:12px;font-weight:800;color:{c}">Per payday $<span class="wl" style="width:80px;height:20px;border-color:{c}"></span></span>
<span style="display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:{GREY}"><span class="box" style="width:13px;height:13px;border-color:{c}"></span>Auto transfer set</span></div>'''
        elif i == 4:
            items = ["Groceries", "Gas", "Kids & household", "Fun money"]
            inner = "".join(f'<div style="display:flex;align-items:flex-end;gap:8px">{lab(x)}<span class="wl" style="flex:1;height:19px"></span><span style="font-size:11px;font-weight:700;color:{GREY}">$</span><span class="wl" style="width:62px;height:19px"></span></div>' for x in items)
            inner += f'<div style="display:flex;justify-content:flex-end;align-items:flex-end;gap:6px;font-size:12px;font-weight:800;color:{c}">Total $<span class="wl" style="width:80px;height:20px;border-color:{c}"></span></div>'
        else:
            inner = f'''<span style="font-size:11.5px;font-weight:600;line-height:1.45">Your paycheck, minus buckets 1 to 5. Whatever is left stays put until next payday.</span>
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:6px"><span style="font-size:11px;font-weight:700;color:{GREY}">Aim for $100 or more</span><span style="display:flex;align-items:flex-end;gap:6px;font-size:12px;font-weight:800;color:{c}">Buffer $<span class="wl" style="width:80px;height:20px;border-color:{c}"></span></span></div>
<div style="font-size:10.5px;font-weight:700;line-height:1.4;color:{RED};margin-top:4px">Under $100? See the box below.</div>'''
        return f'<div style="background:#fff;border:1.5px solid {t};border-radius:14px;overflow:hidden;display:flex;flex-direction:column">{head}<div style="padding:10px 14px 12px;display:flex;flex-direction:column;gap:7px;flex:1">{inner}</div></div>'
    cards = "".join(card(i) for i in range(6))
    numbox = lambda w=120: f'<span class="wl" style="display:inline-block;width:{w}px;height:26px;border-bottom:2px solid {GOLDB};vertical-align:bottom"></span>'
    body = f'''{title("Bucket Setup", "Fill this in once, in pencil. It becomes the baseline every payday follows.")}
<div style="background:{NAVY};color:#fff;border-radius:12px;padding:11px 18px;display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:12px;font-weight:700">
<span style="display:flex;align-items:flex-end;gap:6px">My paycheck $<span style="display:inline-block;width:90px;border-bottom:1.5px solid #8DA2C4;height:18px"></span></span>
<span style="display:flex;align-items:center;gap:6px"><span class="box" style="width:13px;height:13px;border-color:#fff;background:transparent"></span>Weekly</span>
<span style="display:flex;align-items:center;gap:6px"><span class="box" style="width:13px;height:13px;border-color:#fff;background:transparent"></span>Every 2 weeks</span>
<span style="display:flex;align-items:flex-end;gap:6px">Payday is a<span style="display:inline-block;width:90px;border-bottom:1.5px solid #8DA2C4;height:18px"></span></span></div>
<div style="margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:11px">{cards}</div>
<div style="margin-top:14px;background:{NAVY};border-radius:16px;padding:16px 22px;color:#fff;position:relative">
<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="serif" style="font-size:20px">Your Payday Number</span><span class="cav" style="font-size:22px;color:{GOLDB}">this is the one that changes everything</span></div>
<div style="margin-top:10px;display:flex;flex-direction:column;gap:9px;font-size:14px;font-weight:700">
<div>Every payday, ${numbox()} moves automatically into buckets 1 to 4.</div>
<div>${numbox()} is ours to live on.&nbsp;&nbsp;And ${numbox(90)} stays spare.</div></div></div>
<div style="margin-top:10px;background:{CREAM};border-radius:12px;padding:10px 16px;font-size:11.5px;font-weight:600;line-height:1.5"><b style="color:{RED}">Buffer under $100?</b> Fix it in this order: trim Everyday first, then pause any <i>extra</i> debt payments (keep the minimums), then lower Savings, but never to zero. Never skip a bill.</div>'''
    return page(6, 2, body)

# ---------------- 7. YEAR OF PAYDAYS ----------------
def p_year():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    def mbox(m):
        lines = "".join(f'<div style="display:grid;grid-template-columns:14px 1fr 14px 0.9fr;gap:5px;align-items:end;height:16.5px"><span style="font-size:10px;font-weight:700;color:{GREY}">{j}</span><span class="wl" style="height:14px"></span><span style="font-size:10px;font-weight:700;color:{GREY}">$</span><span class="wl" style="height:14px"></span></div>' for j in range(1, 6))
        return f'''<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:12px;padding:8px 12px 9px;display:flex;flex-direction:column;gap:2px">
<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid {NAVY};padding-bottom:4px"><span style="font-size:11.5px;font-weight:900;letter-spacing:1.5px;color:{NAVY}">{m.upper()}</span><span style="display:flex;align-items:center;gap:4px;font-size:9.5px;font-weight:800;color:#8A6D12"><span class="box" style="width:11px;height:11px;border-width:1.5px;border-color:{GOLD}"></span>Extra</span></div>
{lines}
<div style="margin-top:4px;display:flex;align-items:flex-end;gap:6px;background:{TRED};border-radius:6px;padding:3px 7px"><span style="flex:none;font-size:9.5px;font-weight:800;color:{RED}">BIG BILLS</span><span style="flex:1;border-bottom:1px solid #E3BDBD;height:14px"></span></div></div>'''
    grid = "".join(mbox(m) for m in months)
    xl = "".join(f'<div style="display:flex;align-items:flex-end;gap:8px;font-size:11.5px;font-weight:700"><span style="flex:none">{i}. Date</span><span class="wl" style="width:62px;height:17px"></span><span style="flex:none;color:{GREY}">goes to</span><span class="wl" style="flex:1;height:17px"></span></div>' for i in range(1, 5))
    body = f'''{title("Year of Paydays", "Every payday for the year, the extra ones, and the months the big bills land.")}
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:-2px;margin-bottom:10px;font-size:12px;font-weight:700">
<span style="display:flex;align-items:flex-end;gap:6px">Year<span class="wl" style="width:90px;height:18px"></span></span>
<span style="display:flex;gap:16px"><span style="display:flex;align-items:center;gap:6px"><span class="box" style="width:13px;height:13px"></span>Weekly</span><span style="display:flex;align-items:center;gap:6px"><span class="box" style="width:13px;height:13px"></span>Every 2 weeks</span></span></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:9px">{grid}</div>
<div style="margin-top:10px;display:grid;grid-template-columns:1fr 1.25fr;gap:12px">
<div style="background:#fff;border:2px solid {GOLD};border-radius:14px;padding:11px 14px;display:flex;gap:10px">{icon("star", GOLD, 22)}<span style="font-size:11.5px;font-weight:600;line-height:1.5"><b style="color:{NAVY}">Extra paydays.</b> Paid every two weeks? Two months a year have a third payday. Paid weekly? Four months have a fifth. Your buckets are already covered, so these are a head start. Decide where they go <i>before</i> they land.</span></div>
<div style="background:#fff;border:1.5px solid #E2DCCB;border-radius:14px;padding:10px 16px;display:flex;flex-direction:column;gap:5px"><span class="eyebrow" style="font-size:9.5px;color:{NAVY}">Our extra paydays</span>{xl}</div></div>'''
    return page(7, 2, body)

PAGES_B = [p_lesson2, p_setup, p_year]
