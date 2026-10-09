import os, sys, asyncio
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
HERE = os.path.dirname(os.path.abspath(__file__))
CC = {"bills": "#5B86C9", "debt": "#3A3F4A", "buffer": "#E8BC2C"}
rules = ["Before it’s due", "Minimums first", "Like a bill", "Only if it breaks", "From what’s left", "$100+ spare"]
rows = ""
for i, (k, n, c, t, w, r) in enumerate(BUCKETS):
    col = CC.get(k, c)
    rows += f'''<div style="display:flex;align-items:center;gap:30px;background:rgba(255,255,255,0.07);border-radius:28px;padding:20px 34px">
<span style="flex:none;width:76px;height:76px;border-radius:50%;background:{col};color:#fff;font-size:40px;font-weight:900;display:flex;align-items:center;justify-content:center">{i+1}</span>
<div style="display:flex;flex-direction:column;gap:4px"><span style="font-size:52px;font-weight:900;color:#fff;text-transform:uppercase;letter-spacing:1px">{n}</span>
<span style="font-size:30px;font-weight:600;color:#C3CCDB">{rules[i]}</span></div></div>'''
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS} *{{box-sizing:border-box}} body{{margin:0}}</style></head><body>
<div style="width:1080px;height:1920px;background:{NAVY};font-family:'Montserrat',sans-serif;padding:540px 80px 120px;display:flex;flex-direction:column">
<div style="font-size:30px;font-weight:900;letter-spacing:8px;color:{GOLDB}">EVERY PAYDAY</div>
<div class="serif" style="font-family:'Libre Baskerville',serif;font-weight:700;font-size:78px;line-height:1.1;color:#fff;margin-top:14px">In this order.</div>
<div style="margin-top:44px;display:flex;flex-direction:column;gap:14px">{rows}</div>
<div style="flex:1"></div>
<div style="font-family:'Caveat',cursive;font-weight:700;font-size:58px;line-height:1.15;color:{GOLDB};text-align:center">Pay the bills. Pay the debt.<br>Pay yourself. Guard the rest.</div>
</div></body></html>'''
p = os.path.join(HERE, "wallpaper.html"); open(p, "w").write(html)
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto("file://" + p); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
        await pg.screenshot(path=os.path.join(HERE, "Payday Routine - Phone Wallpaper.png")); await b.close()
asyncio.run(main())
