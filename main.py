#!/usr/bin/env python3
"""News image entry — Thursday 19 November 2026, the whole day in one image.

Validates entry.png (the drawn front page: 3 hero stories, 10 pictured
panels, a dot-matrix world map with numbered pins, and 18 numbered briefs —
31 stories in all), prints the story index, and copies the image to the
output directory. Standard library only.
"""
import hashlib, os, shutil, struct, sys

STORIES = [
    (1, "SHENZHEN", 'Trump, Xi and Putin hold first three-way summit'),
    (2, "WORLDWIDE", 'GTA VI arrives after a 13-year wait'),
    (3, "NASDAQ", 'Anthropic debuts in the biggest IPO on record'),
    (4, "THE HAGUE", "World Court rules on Myanmar's Rohingya case"),
    (5, "ODISHA", 'Akvan bears down as 200,000 flee the coast'),
    (6, "ANTALYA", 'COP31 enters its final 48 hours'),
    (7, "SEOUL", "Half a million sit Korea's Suneung"),
    (8, "FLORIDA", 'Flooded Florida braces for still more rain'),
    (9, "JAZAN", 'Saudi Arabia says danger has passed in three cities'),
    (10, "KYIV", 'Left off the agenda, Ukraine watches Shenzhen'),
    (11, "SPACE", 'Voyager 1, one light-day out — NASA briefs the world'),
    (12, "GAZA", "Israeli tanks cross Gaza's Yellow Line"),
    (13, "BRUSSELS", 'EU proposes a €45bn loan for Ukraine'),
    (14, "KERCH", 'Crimean Bridge hit a third time in a week'),
    (15, "SHENZHEN", 'APEC leaders adopt the Shenzhen Declaration'),
    (16, "NEW YORK", 'Van Gogh sells for a record $190.4m'),
    (17, "WASHINGTON", 'US and Venezuela sign a military cooperation agreement'),
    (18, "PYONGYANG", 'IAEA: North Korea has expanded uranium enrichment at Yongbyon'),
    (19, "JERUSALEM", 'Herzog taps ex-army chief Eisenkot to form a government'),
    (20, "TEHRAN", 'Trump says Iran is exploring chemical and biological weapons'),
    (21, "KUWAIT CITY", 'Kuwait repels its first Iranian attack in two months'),
    (22, "RIYADH", 'Debris from an intercepted Houthi rocket damages the PIF tower'),
    (23, "GAZA", 'Australia, Canada, Italy and UK demand unrestricted aid access'),
    (24, "KINSHASA", 'Ebola cases in DR Congo pass 11,000 in the widening outbreak'),
    (25, "GENEVA", 'Record 589 million children now live in conflict zones'),
    (26, "NAIROBI", "Kenya's drought deepens the milk shortage; prices climb"),
    (27, "PARIS", 'France sees a fourth weekend of cost-of-living protests'),
    (28, "TOKYO", 'Dozens of Japanese firms issue breach notices after KARTE hack'),
    (29, "WASHINGTON", 'Ransomware group N0n claims data from 59 firms, incl. JPMorgan'),
    (30, "MIAMI", 'US court convicts Haitian pastor over the 2021 Moise assassination'),
    (31, "WASHINGTON", 'Trump makes a third Supreme Court bid on Venezuelan protections'),
]

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG"); return 1
    w, h = struct.unpack(">II", data[16:24])
    print(f"THE WORLD IN ONE DAY — Thursday 19 November 2026 ({w}x{h}, {len(data)} bytes)")
    for num, kind, head in STORIES:
        print(f"{num:>2}. [{kind}] {head}")
    print(f"{len(STORIES)} stories · sha256 {hashlib.sha256(data).hexdigest()}")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)
    return 0

if __name__ == "__main__":
    sys.exit(main())
