"""Download an open-access full text and print page-located snippets for evidence locators.

Usage:
    python scripts/inspect_fulltext.py <PAPER_ID> <url> "<regex1>" ["<regex2>" ...] [--max 6] [--ctx 220]

- Saves the file to literature/fulltext/<PAPER_ID>.pdf (git-ignored: third-party copyright; sha256 printed
  for the Evidence_Matrix). An existing file is reused, never overwritten.
- Prints, for each regex, up to --max hits with page numbers and surrounding text.
"""
import argparse
import hashlib
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "literature" / "fulltext"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("paper_id")
    p.add_argument("url")
    p.add_argument("patterns", nargs="+")
    p.add_argument("--max", type=int, default=6)
    p.add_argument("--ctx", type=int, default=220)
    a = p.parse_args()
    DIR.mkdir(parents=True, exist_ok=True)
    dest = DIR / f"{a.paper_id}.pdf"
    if not dest.exists():
        req = urllib.request.Request(a.url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        if data[:4] != b"%PDF":
            raise SystemExit(f"not a PDF (first bytes {data[:60]!r}); nothing saved")
        dest.write_bytes(data)
    data = dest.read_bytes()
    print(f"file={dest.relative_to(ROOT)} bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()} url={a.url}")
    import fitz
    with fitz.open(dest) as d:
        pages = [pg.get_text() for pg in d]
    print(f"pages={len(pages)}")
    for pat in a.patterns:
        rx = re.compile(pat, re.I)
        n = 0
        print(f"--- /{pat}/")
        for i, t in enumerate(pages, 1):
            flat = re.sub(r"\s+", " ", t)
            for m in rx.finditer(flat):
                s = flat[max(0, m.start() - a.ctx): m.end() + a.ctx]
                print(f"  p.{i}: …{s}…")
                n += 1
                if n >= a.max:
                    break
            if n >= a.max:
                break
        if n == 0:
            print("  (no hits)")


if __name__ == "__main__":
    main()
