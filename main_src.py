#!/usr/bin/env python3
"""Warm Postcard edition - news-image-20261119, round 3 (wallet w8).

entry.png is the entry: a single hand-drawn front page for Thursday
19 November 2026, styled as a set of stamped postcards from the day's
datelines. This file is the readable source behind the entrypoint.
Running it confirms the page is a genuine PNG, prints the masthead and
the numbered index of every story the page carries (3 leads, 10
pictured postcards, 18 briefs), and copies the page to the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).

Standard library only.
"""
import hashlib
import os
import shutil
import struct
import sys

MASTHEAD = "THE WORLD IN ONE DAY - Thursday 19 November 2026 - Warm Postcard edition"

# Rows of the index printed on the run: (page number, kind, label, headline).
# LEAD stories open the page, PIC rows are the stamped pictured panels,
# BRIEF rows are the one-line briefs along the bottom.
PAGE_INDEX = [
    (1, "LEAD", "SHENZHEN - SUMMIT", "Trump, Xi and Putin hold first three-way summit"),
    (2, "LEAD", "WORLDWIDE - GAMES", "GTA VI arrives after a 13-year wait"),
    (3, "LEAD", "NASDAQ - MARKETS", "Anthropic debuts in the biggest IPO on record"),
    (4, "PIC", "THE HAGUE - LAW", "World Court rules on Myanmar's Rohingya case"),
    (5, "PIC", "ODISHA - STORM", "Akvan bears down as 200,000 flee the coast"),
    (6, "PIC", "ANTALYA - CLIMATE", "COP31 enters its final 48 hours"),
    (7, "PIC", "SEOUL - EDUCATION", "Half a million sit Korea's Suneung"),
    (8, "PIC", "FLORIDA - WEATHER", "Flooded Florida braces for still more rain"),
    (9, "PIC", "JAZAN - GULF", "Saudi Arabia says danger has passed in three cities"),
    (10, "PIC", "KYIV - WAR", "Left off the agenda, Ukraine watches Shenzhen"),
    (11, "PIC", "SPACE - SCIENCE", "Voyager 1, one light-day out - NASA briefs the world"),
    (12, "PIC", "GAZA - WAR", "Israeli tanks cross Gaza's Yellow Line"),
    (13, "PIC", "BRUSSELS - EUROPE", "EU proposes a \u20ac45bn loan for Ukraine"),
    (14, "BRIEF", "KERCH", "Crimean Bridge hit a third time in a week"),
    (15, "BRIEF", "SHENZHEN", "APEC leaders adopt the Shenzhen Declaration"),
    (16, "BRIEF", "NEW YORK", "Van Gogh sells for a record $190.4m"),
    (17, "BRIEF", "WASHINGTON", "US and Venezuela sign a military cooperation agreement"),
    (18, "BRIEF", "PYONGYANG", "IAEA: North Korea has expanded uranium enrichment at Yongbyon"),
    (19, "BRIEF", "JERUSALEM", "Herzog taps ex-army chief Eisenkot to form a government"),
    (20, "BRIEF", "TEHRAN", "Trump says Iran is exploring chemical and biological weapons"),
    (21, "BRIEF", "KUWAIT CITY", "Kuwait repels its first Iranian attack in two months"),
    (22, "BRIEF", "RIYADH", "Debris from an intercepted Houthi rocket damages the PIF tower"),
    (23, "BRIEF", "GAZA", "Australia, Canada, Italy and UK demand unrestricted aid access"),
    (24, "BRIEF", "KINSHASA", "Ebola cases in DR Congo pass 11,000 in the widening outbreak"),
    (25, "BRIEF", "GENEVA", "Record 589 million children now live in conflict zones"),
    (26, "BRIEF", "NAIROBI", "Kenya's drought deepens the milk shortage; prices climb"),
    (27, "BRIEF", "PARIS", "France sees a fourth weekend of cost-of-living protests"),
    (28, "BRIEF", "TOKYO", "Dozens of Japanese firms issue breach notices after KARTE hack"),
    (29, "BRIEF", "WASHINGTON", "Ransomware group N0n claims data from 59 firms, incl. JPMorgan"),
    (30, "BRIEF", "MIAMI", "US court convicts Haitian pastor over the 2021 Moise assassination"),
    (31, "BRIEF", "WASHINGTON", "Trump makes a third Supreme Court bid on Venezuelan protections"),
]

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_dimensions(path):
    """Read the (width, height) pair out of the PNG IHDR chunk."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != PNG_SIGNATURE:
        raise ValueError("entry.png does not start with a PNG signature")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png is missing its IHDR chunk")
    return struct.unpack(">II", head[16:24])


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    page = os.path.join(here, "entry.png")
    try:
        width, height = png_dimensions(page)
    except (OSError, ValueError) as exc:
        print(f"entry.png rejected: {exc}")
        return 1
    print(MASTHEAD)
    print(f"Front page: {width}x{height} PNG, {len(PAGE_INDEX)} stories indexed below.")
    for number, kind, label, headline in PAGE_INDEX:
        print(f"{number:>2}. [{kind}] {label} - {headline}")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.png")
    shutil.copyfile(page, target)
    with open(page, "rb") as fh:
        blob = fh.read()
    digest = hashlib.sha256(blob).hexdigest()
    print(f"{len(PAGE_INDEX)} stories - copied the page to {target}")
    print(f"Page fingerprint: {len(blob)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
