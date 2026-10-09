import sys, os, asyncio, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import doc
HERE = os.path.dirname(os.path.abspath(__file__))
fns = []
for m in ("pages_a", "pages_b", "pages_c"):
    try:
        fns += importlib.import_module(m).__dict__["PAGES_" + m[-1].upper()]
    except ModuleNotFoundError:
        pass
html = doc([f() for f in fns])
open(os.path.join(HERE, "book.html"), "w").write(html)
from playwright.async_api import async_playwright
only = [int(x) for x in sys.argv[1:]]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 816, "height": 1056}, device_scale_factor=2)
        await pg.goto("file://" + os.path.join(HERE, "book.html"))
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(300)
        over = await pg.evaluate("""()=>[...document.querySelectorAll('.page')].map((p,i)=>{const sp=p.querySelector(':scope > .spacer');return [i+1, sp?Math.round(sp.getBoundingClientRect().height):null, p.scrollHeight>p.clientHeight+1]})""")
        print(over)
        els = await pg.query_selector_all(".page")
        os.makedirs(os.path.join(HERE, "png"), exist_ok=True)
        for i, e in enumerate(els):
            if only and i+1 not in only: continue
            await e.screenshot(path=os.path.join(HERE, "png", f"p{i+1:02d}.png"))
        await pg.pdf(path=os.path.join(HERE, "book.pdf"), width="8.5in", height="11in", print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
        await b.close()
asyncio.run(main())
