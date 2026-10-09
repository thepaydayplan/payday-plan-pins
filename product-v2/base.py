import os
HERE = os.path.dirname(os.path.abspath(__file__))
GF = os.path.join(os.path.dirname(HERE), "gfonts")

NAVY = "#1B3A6B"; GREEN = "#1E7A4C"; GOLD = "#C9A227"; GOLDB = "#E8BC2C"
OFF = "#FAF8F3"; CREAM = "#F3EFE4"; BLACK = "#121212"; RED = "#B23A3A"
BROWN = "#7A5A0F"; INK = "#23272F"; GREY = "#5B6475"; LINE = "#CFC7B3"
TNAVY = "#E6ECF5"; TGREEN = "#E2F0E7"; TRED = "#F7E6E6"; TGOLD = "#F6EED3"; TBLACK = "#ECEAE4"

def ff(name, file, w, style="normal"):
    return f"@font-face{{font-family:'{name}';src:url('file://{GF}/{file}');font-weight:{w};font-style:{style}}}"

FONTS = "\n".join([
    ff("Montserrat", "Montserrat/static/Montserrat-Medium.ttf", 500),
    ff("Montserrat", "Montserrat/static/Montserrat-SemiBold.ttf", 600),
    ff("Montserrat", "Montserrat/static/Montserrat-Bold.ttf", 700),
    ff("Montserrat", "Montserrat/static/Montserrat-ExtraBold.ttf", 800),
    ff("Montserrat", "Montserrat/static/Montserrat-Black.ttf", 900),
    ff("Libre Baskerville", "Libre_Baskerville/static/LibreBaskerville-Bold.ttf", 700),
    ff("Libre Baskerville", "Libre_Baskerville/static/LibreBaskerville-Italic.ttf", 400, "italic"),
    ff("Caveat", "Caveat/static/Caveat-Bold.ttf", 700),
])

CSS = FONTS + f"""
@page {{ size: 8.5in 11in; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; padding: 0; background: #fff }}
body {{ font-family: 'Montserrat', sans-serif; color: {INK}; -webkit-print-color-adjust: exact; print-color-adjust: exact }}
.page {{ width: 816px; height: 1056px; padding: 40px 52px 28px; background: {OFF}; display: flex; flex-direction: column; position: relative; overflow: hidden; page-break-after: always; break-after: page }}
.serif {{ font-family: 'Libre Baskerville', serif; font-weight: 700 }}
.cav {{ font-family: 'Caveat', cursive; font-weight: 700 }}
.eyebrow {{ font-size: 11px; font-weight: 800; letter-spacing: 2.4px; text-transform: uppercase }}
.wl {{ border-bottom: 1.3px solid {LINE}; height: 26px }}
.box {{ width: 15px; height: 15px; border: 1.8px solid {NAVY}; border-radius: 4px; flex: none; display: inline-block; background: #fff }}
.spacer {{ flex: 1 }}
h1 {{ margin: 0 }}
p {{ margin: 0 }}
"""

LOGO = f'''<svg width="20" height="20" viewBox="0 0 120 120" fill="none" aria-hidden="true"><rect x="12" y="22" width="96" height="86" rx="12" fill="{NAVY}"/><rect x="12" y="22" width="96" height="24" rx="12" fill="{BLACK}"/><rect x="12" y="34" width="96" height="12" fill="{BLACK}"/><line x1="38" y1="10" x2="38" y2="30" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/><line x1="82" y1="10" x2="82" y2="30" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/><path d="M40 76 L54 90 L82 62" stroke="{GOLD}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

ICON_PATHS = {
    "bills": '<path d="M3 11 L12 4 L21 11"/><path d="M5.5 9.5 V20 H18.5 V9.5"/><path d="M10 20 V14 H14 V20"/>',
    "debt": '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10.5 H21"/><path d="M7 15 H10"/>',
    "savings": '<path d="M5 11 C5 7.5 8 5.5 12 5.5 C16 5.5 19 7.5 19 11 C19 14 17 16 15 16.6 V19 H12.5 V17.2 H11 V19 H8.5 V16.4 C6.5 15.6 5 13.6 5 11 Z"/><path d="M10 8.5 H13.5"/>',
    "touch": '<path d="M3 12 C3 7 7 3.5 12 3.5 C17 3.5 21 7 21 12 Z"/><path d="M12 12 V18.5 C12 20 13.8 20.5 14.8 19.4"/>',
    "everyday": '<path d="M3 4.5 H5.5 L8 15.5 H18 L20.5 8 H6.5"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="16.5" cy="19.5" r="1.3"/>',
    "buffer": '<path d="M12 3 L19.5 6 V11.5 C19.5 16 16.3 19.4 12 21 C7.7 19.4 4.5 16 4.5 11.5 V6 Z"/><path d="M8.8 12 L11 14.2 L15.4 9.8"/>',
    "scissors": '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 L8.1 15.9"/><path d="M14.5 14.5 L20 20"/><path d="M8.1 8.1 L12 12"/>',
    "star": '<path d="M12 3 L14.6 9 L21 9.6 L16.2 13.8 L17.6 20.2 L12 16.9 L6.4 20.2 L7.8 13.8 L3 9.6 L9.4 9 Z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7 V12 L15.5 14"/>',
    "warn": '<path d="M12 3 L22 20 H2 Z"/><path d="M12 10 V14"/><circle cx="12" cy="17" r="0.6"/>',
}

def icon(name, color, s=20, sw=2):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none">{ICON_PATHS[name]}</svg>'

def tick(color=GREEN, s=16, sw=3):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="flex:none"><path d="M5 12.5l5 5 9-10"/></svg>'

def xmark(color=RED, s=14, sw=3):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" style="flex:none"><path d="M6 6 L18 18 M18 6 L6 18"/></svg>'

# bucket: key, name, colour, tint, short what, the rule
BUCKETS = [
    ("bills", "Bills", NAVY, TNAVY, "Rent, phone, power, insurance, car registration", "Every bill gets the paycheck before it’s due."),
    ("debt", "Debt", BLACK, TBLACK, "Credit cards, car loan, buy now pay later", "Every minimum, on time. Extra goes to the smallest balance."),
    ("savings", "Savings", GREEN, TGREEN, "Savings, plus Christmas, birthdays, school costs", "Paid like a bill. Even $10 counts."),
    ("touch", "Don’t Touch", RED, TRED, "Tires, repairs, the vet, the dentist", "Only for things that break. Never for a sale."),
    ("everyday", "Everyday", BROWN, TGOLD, "Groceries, gas, kids, fun money", "Planned from what’s left. Never first."),
    ("buffer", "Buffer", "#8A6D12", "#FBF3D9", "The cushion between you and zero", "Keep $100 or more spare until next payday."),
]

CHAPTERS = {
    "start": ("START HERE", NAVY, "#fff"),
    1: ("CH 1 · LEARN", NAVY, "#fff"),
    2: ("CH 2 · BUILD", GREEN, "#fff"),
    3: ("CH 3 · TRAIN", GOLDB, NAVY),
    4: ("CH 4 · LOCK IN", BLACK, GOLDB),
}

def header(ch):
    lab, bg, fg = CHAPTERS[ch]
    return f'''<div style="display:flex;justify-content:space-between;align-items:center">
<div style="display:flex;align-items:center;gap:8px">{LOGO}<span class="eyebrow" style="color:{NAVY};letter-spacing:3px">The Payday Plan</span></div>
<span style="background:{bg};color:{fg};font-size:10.5px;font-weight:900;letter-spacing:2px;padding:6px 12px;border-radius:999px">{lab}</span></div>'''

def divider(mt=10, mb=12):
    return f'''<div style="display:flex;align-items:center;gap:10px;margin:{mt}px 0 {mb}px"><div style="flex:1;height:2px;background:{GOLD}"></div><div style="width:8px;height:8px;background:{GOLD};transform:rotate(45deg)"></div><div style="flex:1;height:2px;background:{GOLD}"></div></div>'''

def title(t, sub, size=34, kicker=None):
    k = f'<div class="eyebrow" style="margin-top:14px;color:{GREEN}">{kicker}</div>' if kicker else ""
    mt = 4 if kicker else 14
    return f'''{k}<h1 class="serif" style="margin-top:{mt}px;font-size:{size}px;line-height:1.12;color:{NAVY}">{t}</h1>
<div style="margin-top:6px;font-size:14px;font-weight:600;line-height:1.4;color:{GREEN}">{sub}</div>{divider()}'''

def footer(n):
    return f'''<div style="display:flex;justify-content:space-between;align-items:flex-end;font-size:10.5px;font-weight:500;color:#6B6657;margin-top:10px">
<span>The Paycheck Budget System · The Payday Plan · For personal use only</span><span style="font-weight:800;font-size:12px;color:{NAVY}">{n}</span></div>'''

def page(n, ch, body, bg=OFF, foot=True, extra_style=""):
    f = footer(n) if foot else ""
    return f'<section class="page" style="background:{bg};{extra_style}">{header(ch) if ch else ""}{body}<div class="spacer"></div>{f}</section>'

def doc(pages, title="The Paycheck Budget System"):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

def numdot(n, bg, fg="#fff", s=24, fs=12):
    return f'<span style="flex:none;width:{s}px;height:{s}px;border-radius:50%;background:{bg};color:{fg};font-size:{fs}px;font-weight:900;display:inline-flex;align-items:center;justify-content:center">{n}</span>'

def bucket_svg(fill, stroke, s=60, label=None, lc="#fff", lfs=12):
    svg = f'<svg width="{s}" height="{int(s*0.9)}" viewBox="0 0 100 90"><path d="M8 18 L92 18 L80 86 L20 86 Z" fill="{fill}" stroke="{stroke}" stroke-width="5" stroke-linejoin="round"/><ellipse cx="50" cy="18" rx="42" ry="9" fill="{fill}" stroke="{stroke}" stroke-width="5"/><path d="M14 18 C 14 -10, 86 -10, 86 18" fill="none" stroke="{stroke}" stroke-width="4"/></svg>'
    if label is None:
        return svg
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px">{svg}<span style="font-size:{lfs}px;font-weight:800;color:{lc};text-align:center;line-height:1.1">{label}</span></div>'
