# Pin builder

`pin_builder_example.py` renders The Payday Plan pins (1000x1500 PNG) from HTML with Playwright.
It holds the brand header, the two footers (free-budget and no-link "Follow"), shared CSS and the
six "$50 Week" pins (pins 63-68) as worked examples. Copy it, replace the `P[...]` bodies with the
new pins, and run `python3 pin_builder_example.py`.

Fonts are expected in `gf/ofl/` next to the script:

    git clone --depth 1 --filter=blob:none --sparse https://github.com/google/fonts gf
    cd gf && git sparse-checkout set --no-cone ofl/montserrat/ ofl/caveat/ ofl/librebaskerville/
