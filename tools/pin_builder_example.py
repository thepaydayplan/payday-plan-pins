import pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "gf" / "ofl"
OUT = HERE / "png"; OUT.mkdir(exist_ok=True)
HTML = HERE / "html"; HTML.mkdir(exist_ok=True)

NAVY, GREEN, GOLD, HL, INK, CREAM = "#1B3A6B", "#1E7A4C", "#C9A227", "#F1DE9A", "#121212", "#FAF8F3"
TBLUE, TGREEN, TGOLD = "#E6ECF5", "#E2F0E7", "#F6EED3"

HEAD = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Montserrat;src:url('{(FONTS/'montserrat/Montserrat[wght].ttf').as_uri()}');font-weight:100 900}}
@font-face{{font-family:'Libre Baskerville';src:url('{(FONTS/'librebaskerville/LibreBaskerville[wght].ttf').as_uri()}');font-weight:400 700}}
@font-face{{font-family:Caveat;src:url('{(FONTS/'caveat/Caveat[wght].ttf').as_uri()}');font-weight:400 700}}
*{{box-sizing:border-box}} body{{margin:0;background:{CREAM}}}
.pin{{width:1000px;height:1500px;background:{CREAM};display:flex;flex-direction:column;font-family:Montserrat;color:{INK};overflow:hidden}}
.body{{flex:1;display:flex;flex-direction:column;padding:44px 56px 0}}
.brand{{display:flex;align-items:center;justify-content:center;gap:12px}}
.brand span{{font-size:19px;font-weight:800;letter-spacing:5px;color:{NAVY}}}
.c{{text-align:center}}
.cav{{font-family:Caveat;font-weight:700}}
.ser{{font-family:'Libre Baskerville';font-weight:700}}
.blk{{font-weight:900}}
.hl{{background:linear-gradient(transparent 60%,{HL} 60%,{HL} 92%,transparent 92%);padding:0 8px}}
.card{{background:#fff;border:2px solid #E2DCCB;border-radius:20px}}
.lab{{font-size:18px;font-weight:900;letter-spacing:2px}}
.pill{{border-radius:999px;padding:10px 22px;font-size:20px;font-weight:800;letter-spacing:1px}}
.foot{{background:{NAVY};padding:28px 56px;display:flex;align-items:center;justify-content:space-between;gap:20px}}
.grow{{display:none}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:space-evenly;padding:10px 0 24px}} .main>*{{margin-top:0!important}}
</style></head><body><div class="pin"><div class="body">
<div class="brand"><svg width="32" height="32" viewBox="0 0 120 120" fill="none"><rect x="12" y="22" width="96" height="86" rx="12" fill="{NAVY}"/><rect x="12" y="22" width="96" height="24" rx="12" fill="{INK}"/><rect x="12" y="34" width="96" height="12" fill="{INK}"/><line x1="38" y1="10" x2="38" y2="30" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/><line x1="82" y1="10" x2="82" y2="30" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/><path d="M40 76 L54 90 L82 62" stroke="{GOLD}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg><span>THE PAYDAY PLAN</span></div>
<div class="main">
"""

FOOT = f"""</div></div>
<div class="foot"><div style="display:flex;align-items:center;gap:16px"><span style="background:{GOLD};color:{INK};border-radius:8px;padding:8px 14px;font-size:22px;font-weight:900;letter-spacing:2px">FREE</span><span class="ser" style="font-size:32px;color:#fff">1-Page Paycheck Budget</span></div>
<div style="display:flex;align-items:center;gap:14px;white-space:nowrap"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{GOLD}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3.5 7 L12 13 L20.5 7"/></svg><div style="display:flex;flex-direction:column;gap:2px"><span style="font-size:22px;font-weight:800;color:#fff">Sent free to your inbox</span><span style="font-size:18px;font-weight:600;color:#C3CCDB">Visit the link in this pin</span></div></div></div>
</div></body></html>"""

FOOT_NOLINK = f"""</div></div>
<div class="foot" style="justify-content:center;gap:22px"><span style="background:{GOLD};color:{INK};border-radius:8px;padding:8px 14px;font-size:22px;font-weight:900;letter-spacing:2px">FOLLOW</span><span class="ser" style="font-size:32px;color:#fff">The Payday Plan</span><span style="font-size:22px;font-weight:700;color:#C3CCDB">for more real-life money ideas</span></div>
</div></body></html>"""

def chip(t, bg):
    return f'<span style="background:{bg};border-radius:14px;padding:16px 26px;font-size:36px;font-weight:900">{t}</span>'

ICON = {
 "cup": '<path d="M4 9 H16 V14 A5 5 0 0 1 11 19 H9 A5 5 0 0 1 4 14 Z"/><path d="M16 10.5 H18 A2.5 2.5 0 0 1 18 15.5 H16"/><path d="M8 3.5 Q9 5 8 6.5"/><path d="M12 3.5 Q13 5 12 6.5"/>',
 "beer": '<path d="M6 7 H15 V19 A2 2 0 0 1 13 21 H8 A2 2 0 0 1 6 19 Z"/><path d="M15 10 H17.5 A1.5 1.5 0 0 1 19 11.5 V15.5 A1.5 1.5 0 0 1 17.5 17 H15"/><path d="M6 7 A2.5 2.5 0 0 1 9 4.5 A3 3 0 0 1 14 5 A2 2 0 0 1 15 7"/><path d="M9.5 11 V17"/><path d="M12 11 V17"/>',
 "water": '<path d="M6 4 H18 L16.5 20 A1.5 1.5 0 0 1 15 21.3 H9 A1.5 1.5 0 0 1 7.5 20 Z"/><path d="M6.8 10 H17.2"/><path d="M12 13 C12 13 10.3 15 10.3 16.2 A1.7 1.7 0 0 0 13.7 16.2 C13.7 15 12 13 12 13 Z"/>',
 "check": '<path d="M5 12.5 L10 17.5 L19 7"/>',
 "cart": '<path d="M3 4.5 H5.5 L8 15.5 H18 L20.5 8 H6.5"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="16.5" cy="19.5" r="1.3"/>',
 "snack": '<rect x="5" y="4" width="14" height="16" rx="2"/><path d="M5 8 H19"/><path d="M5 16 H19"/><path d="M9 11 H15"/>',
 "glass": '<path d="M7 4 H17 L15.5 13 A3.5 3.5 0 0 1 8.5 13 Z"/><path d="M12 16.5 V20.5"/><path d="M8.5 20.5 H15.5"/>',
}
def icon(name, color, size=44, sw=2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>'

P = {}

P["p1-coffee"] = f"""
<div class="c" style="margin-top:26px">
 <div class="cav" style="font-size:58px;line-height:1;color:{GREEN}">had $20 in my pocket. thought…</div>
 <div class="blk" style="font-size:92px;line-height:1;color:{NAVY};margin-top:10px">WHAT’S A</div>
 <div class="ser" style="font-size:118px;line-height:1.15;color:{GREEN}"><span class="hl">$5 coffee?</span></div>
</div>
<div class="card" style="margin-top:30px;padding:28px 30px;display:flex;flex-direction:column;align-items:center;gap:20px">
 <div style="font-size:34px;font-weight:700">Then I did that <b style="font-weight:900">5 days a week.</b></div>
 <div style="display:flex;align-items:center;gap:16px;font-size:34px;font-weight:900;color:{NAVY}">{chip('$5',TGOLD)}×{chip('5 days',TBLUE)}×{chip('52 weeks',TGREEN)}</div>
 <div style="display:flex;align-items:baseline;gap:18px"><span class="blk" style="font-size:44px;color:{NAVY}">=</span><span class="ser" style="font-size:112px;line-height:1.1;color:{GREEN}"><span class="hl">$1,300</span></span><span class="blk" style="font-size:40px;color:{NAVY}">a year</span></div>
</div>
<div class="ser c" style="margin-top:34px;font-size:44px;line-height:1.3;color:{NAVY}">It wasn’t the coffee.<br>It was that I never <span class="hl">planned</span> for it.</div>
<div style="margin-top:34px;background:{TGOLD};border-radius:20px;padding:24px 28px;display:flex;gap:22px;align-items:center">
 <span style="flex:none;width:84px;height:84px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center">{icon('cup','#7A5A0F',50)}</span>
 <div style="display:flex;flex-direction:column;gap:6px"><span class="lab" style="color:#7A5A0F">WHAT WE DO NOW</span><span style="font-size:27px;font-weight:700;line-height:1.35">$50 a week for the little stuff. The coffee comes out of that, so every cup is planned and guilt-free.</span></div>
</div>
"""

P["p2-stopped-no"] = f"""
<div class="c" style="margin-top:34px">
 <div class="blk" style="font-size:62px;line-height:1.05;color:{NAVY}">WE STOPPED TELLING<br>OURSELVES</div>
 <div class="ser" style="font-size:150px;line-height:1.2;color:{INK};position:relative;display:inline-block">“no.”<span style="position:absolute;left:-10px;right:-10px;top:52%;height:16px;background:{GOLD};border-radius:8px;transform:rotate(-6deg)"></span></div>
 <div class="cav" style="font-size:64px;line-height:1;color:{GREEN}">we gave ourselves this instead:</div>
</div>
<div style="margin-top:26px;background:{NAVY};border-radius:28px;padding:30px 30px 34px;display:flex;flex-direction:column;align-items:center">
 <div class="ser" style="font-size:210px;line-height:1;color:{GOLD}">$50</div>
 <div style="font-size:28px;font-weight:900;letter-spacing:4px;color:#fff;margin-top:6px">A WEEK FOR THE LITTLE STUFF</div>
 <div style="display:flex;gap:14px;margin-top:26px">
  <span style="display:flex;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:12px 22px;font-size:24px;font-weight:800">{icon('cup',NAVY,32)}Coffee</span>
  <span style="display:flex;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:12px 22px;font-size:24px;font-weight:800">{icon('snack',NAVY,32)}Snacks</span>
  <span style="display:flex;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:12px 22px;font-size:24px;font-weight:800">{icon('glass',NAVY,32)}Drinks with friends</span>
 </div>
 <div style="font-size:24px;font-weight:700;color:#D7DEEA;margin-top:18px">It all comes out of the $50.</div>
</div>
<div class="ser c" style="margin-top:36px;font-size:58px;line-height:1.2;color:{NAVY}">When it’s gone, it’s <span class="hl">gone.</span></div>
<div style="margin-top:28px;display:flex;justify-content:center;gap:14px">
 <span class="pill" style="background:{TBLUE};color:{NAVY}">NO GUILT</span><span class="pill" style="background:{TGREEN};color:{GREEN}">NO WILLPOWER</span><span class="pill" style="background:{TGOLD};color:#7A5A0F">JUST A NUMBER</span>
</div>
"""

days = [("MON","−$30","$20",1),("TUE","−$20","$0",1),("WED","","$0",0),("THU","","$0",0),("FRI","","$0",0),("SAT","","$0",0),("SUN","","$0",0)]
dcards = "".join(
 f'<div style="flex:1;border-radius:16px;padding:26px 6px;display:flex;flex-direction:column;align-items:center;gap:12px;background:{"#fff" if a else "#ECE7DA"};border:2px solid {"#E2DCCB" if a else "#ECE7DA"}">'
 f'<span style="font-size:22px;font-weight:900;letter-spacing:1px;color:{NAVY if a else "#8A8578"}">{d}</span>'
 f'<span style="font-size:28px;font-weight:900;color:{"#B03A2E" if a else "#8A8578"}">{s or "—"}</span>'
 f'<span style="font-size:17px;font-weight:700;color:#4A4A4A">left {l}</span></div>' for d,s,l,a in days)
P["p3-gone-tuesday"] = f"""
<div class="c" style="margin-top:34px">
 <div class="blk" style="font-size:80px;line-height:1;color:{NAVY}">$50 FOR THE WEEK.</div>
 <div class="ser" style="font-size:104px;line-height:1.25;color:{GREEN}"><span class="hl">Gone by Tuesday?</span></div>
</div>
<div style="margin-top:26px;display:flex;gap:10px">{dcards}</div>
<div class="ser c" style="margin-top:46px;font-size:56px;line-height:1.25;color:{NAVY}">That’s not failing.<br>That’s <span class="hl">the lesson.</span></div>
<div class="c" style="margin-top:26px;font-size:30px;font-weight:600;line-height:1.45;color:#2E2E2E">Wednesday to Sunday, you feel exactly<br>what “gone” means. Next week, you’ll<br>spend it differently. <b style="font-weight:900;color:{INK}">We did.</b></div>
<div style="margin-top:38px;border:3px solid {GOLD};border-radius:20px;padding:22px 26px;display:flex;align-items:center;gap:20px;background:#fff">
 <svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#7A5A0F" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" style="flex:none"><path d="M12 3 L19 6 V11 C19 15.5 16 19 12 21 C8 19 5 15.5 5 11 V6 Z"/><path d="M9 12 L11 14 L15 10"/></svg>
 <div style="display:flex;flex-direction:column;gap:4px"><span class="lab" style="color:#7A5A0F">THE ONLY RULE</span><span style="font-size:28px;font-weight:800">No top-ups from the bills money.</span></div>
</div>
"""

P["p4-beer-water"] = f"""
<div class="c" style="margin-top:30px">
 <div class="cav" style="font-size:72px;line-height:1;color:{GREEN}">at the bar…</div>
</div>
<div style="margin-top:22px;display:flex;align-items:center;gap:18px">
 <div style="flex:1;background:{TGOLD};border-radius:26px;padding:34px 20px;display:flex;flex-direction:column;align-items:center;gap:12px">{icon('beer','#7A5A0F',140,1.6)}<span class="ser" style="font-size:84px;line-height:1;color:#7A5A0F">$9</span><span class="blk" style="font-size:36px;letter-spacing:2px">BEER</span></div>
 <span class="ser" style="flex:none;width:86px;height:86px;border-radius:50%;background:{NAVY};color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center">or</span>
 <div style="flex:1;background:{TBLUE};border-radius:26px;padding:34px 20px;display:flex;flex-direction:column;align-items:center;gap:12px">{icon('water',NAVY,140,1.6)}<span class="ser" style="font-size:84px;line-height:1;color:{NAVY}">Free</span><span class="blk" style="font-size:36px;letter-spacing:2px">WATER</span></div>
</div>
<div class="c" style="margin-top:36px;font-size:32px;font-weight:600;line-height:1.45;color:#2E2E2E">We picked water a couple of times.<br>Didn’t feel like much.</div>
<div class="ser c" style="margin-top:30px;font-size:60px;line-height:1.3;color:{NAVY}">Two weeks later, the leftover paid for <span style="color:{GREEN}" class="hl">date night.</span></div>
<div style="margin-top:38px;display:flex;justify-content:center;gap:14px">
 <span class="pill" style="background:{TBLUE};color:{NAVY}">SMALL CHOICES</span><span class="pill" style="background:{TGREEN};color:{GREEN}">YOUR CHOICE</span><span class="pill" style="background:{TGOLD};color:#7A5A0F">BIG PAYOFF</span>
</div>
"""

items = [("Muffin","$4.00"),("Coffee","$5.50"),("Drink after work","$9.00"),("“Just this once” at the checkout","$6.00"),("App you forgot about","$2.99")]
rows = "".join(f'<div style="display:flex;justify-content:space-between;font-size:26px;font-weight:700;padding:9px 0;border-bottom:2px dashed #E2DCCB"><span>{a}</span><span style="font-weight:900">{b}</span></div>' for a,b in items)
P["p5-the-bits"] = f"""
<div style="margin-top:34px;display:flex;justify-content:center;gap:16px">
 <span style="display:flex;align-items:center;gap:10px;background:{TGREEN};border-radius:999px;padding:12px 24px;font-size:28px;font-weight:800;color:{GREEN}">{icon('check',GREEN,32,3)}Rent’s paid</span>
 <span style="display:flex;align-items:center;gap:10px;background:{TGREEN};border-radius:999px;padding:12px 24px;font-size:28px;font-weight:800;color:{GREEN}">{icon('check',GREEN,32,3)}Bills are paid</span>
</div>
<div class="c" style="margin-top:18px">
 <div class="cav" style="font-size:62px;line-height:1;color:{NAVY}">so why are you broke before payday?</div>
 <div style="display:flex;align-items:baseline;justify-content:center;gap:22px;margin-top:8px"><span class="blk" style="font-size:118px;line-height:1;color:{NAVY}">IT’S THE</span><span class="ser" style="font-size:150px;line-height:1.1;color:{GREEN}"><span class="hl">bits.</span></span></div>
</div>
<div class="card" style="margin-top:22px;padding:24px 34px 26px">
 <div class="lab" style="color:#7A5A0F;margin-bottom:6px">AN EASY DAY OF BITS · EXAMPLE</div>
 {rows}
 <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:14px"><span class="blk" style="font-size:30px">One day</span><span class="ser" style="font-size:58px;color:#B03A2E">$27.49</span></div>
</div>
<div class="ser c" style="margin-top:32px;font-size:50px;line-height:1.3;color:{NAVY}">Give the bits a budget,<br>and they stop <span class="hl">running yours.</span></div>
"""

opts = [
 ("1","Spend it all on day 1","OK. The rest of the week is quiet.","OK","#ECE7DA","#4A4A4A","#fff",INK,"#4A4A4A"),
 ("2","Spread it out","A little something most days.","NICE WORK",TGREEN,GREEN,"#fff",INK,"#4A4A4A"),
 ("3","Save it and roll it over","$100 dinner out next week.","GREAT WORK",GOLD,INK,NAVY,"#fff","#D7DEEA"),
]
ocards = "".join(
 f'<div style="background:{bg};border:2px solid {"#E2DCCB" if bg=="#fff" else bg};border-radius:22px;padding:34px 30px;display:flex;align-items:center;gap:22px">'
 f'<span class="ser" style="flex:none;width:70px;height:70px;border-radius:50%;background:{TBLUE};color:{NAVY};font-size:32px;display:flex;align-items:center;justify-content:center">{n}</span>'
 f'<div style="flex:1;display:flex;flex-direction:column;gap:6px"><span style="font-size:40px;font-weight:900;color:{tc}">{t}</span><span style="font-size:30px;font-weight:600;color:{sc}">{s}</span></div>'
 f'<span class="pill" style="flex:none;background:{pb};color:{pc};font-size:21px">{g}</span></div>'
 for n,t,s,g,pb,pc,bg,tc,sc in opts)
P["p6-you-choose"] = f"""
<div class="c" style="margin-top:34px">
 <div class="blk" style="font-size:74px;line-height:1.05;color:{NAVY}">YOUR $50<br>FOR THE WEEK.</div>
 <div class="ser" style="font-size:112px;line-height:1.25;color:{GREEN}"><span class="hl">You choose.</span></div>
</div>
<div style="margin-top:30px;display:flex;flex-direction:column;gap:18px">{ocards}</div>
<div class="c" style="margin-top:44px;display:flex;flex-direction:column;align-items:center;gap:8px">
 <div class="ser" style="font-size:58px;line-height:1.2;color:{NAVY}">It’s your money.</div>
 <div class="cav" style="font-size:76px;line-height:1;color:{GREEN}">your call.</div>
</div>
"""

only = sys.argv[1:]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1000,"height":1500})
    for name, body in P.items():
        if only and name not in only: continue
        f = HTML / f"{name}.html"; f.write_text(HEAD + body + (FOOT_NOLINK if name=="p4-beer-water" else FOOT))
        pg.goto(f.as_uri()); pg.wait_for_timeout(300)
        # report overflow: content taller than pin
        over = pg.evaluate("()=>{const b=document.querySelector('.body');return b.scrollHeight-b.clientHeight}")
        pg.screenshot(path=str(OUT / f"{name}.png"), clip={"x":0,"y":0,"width":1000,"height":1500})
        print(name, "overflow px:", over)
    b.close()
