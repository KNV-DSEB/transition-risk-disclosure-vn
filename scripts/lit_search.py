"""Logged scholarly search for the Gate 1B kill-paper hunt.

Usage:
    python scripts/lit_search.py <SEARCH_ID> openalex "<query>" [--from-year YYYY] [--n 25] [--field title_and_abstract]
    python scripts/lit_search.py <SEARCH_ID> crossref "<query>" [--n 20]
    python scripts/lit_search.py <SEARCH_ID> doi <doi>              (metadata check via Crossref + OpenAlex)

Every call:
- stores the raw API response in literature/search_runs/<SEARCH_ID>.json (never overwritten);
- appends one line to literature/search_runs/index.jsonl (timestamp, source, exact query, filters, hit count);
- prints a compact list of records for screening.
No API key or e-mail address is sent.
"""
import argparse
import datetime as dt
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "literature" / "search_runs"
UA = {"User-Agent": "research-provenance-script/0.1"}


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def abstract_from_inverted(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def save(search_id, payload, meta):
    RUNS.mkdir(parents=True, exist_ok=True)
    out = RUNS / f"{search_id}.json"
    if out.exists():
        sys.exit(f"{out} exists; use a new Search_ID (runs are never overwritten)")
    out.write_text(json.dumps({"meta": meta, "response": payload}, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(RUNS / "index.jsonl", "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")


def run_openalex(a):
    flt = []
    if a.from_year:
        flt.append(f"from_publication_date:{a.from_year}-01-01")
    if a.cites:
        flt.append(f"cites:{a.cites}")
    params = {"per-page": str(a.n)}
    if a.field == "search":
        params["search"] = a.query
    else:
        flt.append(f"{a.field}.search:{a.query}")
    if flt:
        params["filter"] = ",".join(flt)
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = get_json(url)
    meta = {"search_id": a.search_id, "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "source": "OpenAlex API", "query": a.query, "field": a.field, "filters": flt,
            "url": url, "hit_count": data.get("meta", {}).get("count"), "returned": len(data.get("results", []))}
    save(a.search_id, data, meta)
    print(f"[{a.search_id}] OpenAlex hits={meta['hit_count']} returned={meta['returned']}")
    for i, w in enumerate(data.get("results", []), 1):
        au = ", ".join(x["author"]["display_name"] for x in w.get("authorships", [])[:3])
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "")
        abst = abstract_from_inverted(w.get("abstract_inverted_index"))[:260]
        print(f"{i:>2}. {w.get('publication_year')} | {w.get('display_name')}\n    {au} | {src} | {w.get('doi') or w.get('id')}"
              f" | type={w.get('type')} | oa={((w.get('open_access') or {}).get('oa_url') or '')[:90]}\n    ABS: {abst}")


def run_crossref(a):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": a.query, "rows": str(a.n)})
    data = get_json(url)
    items = data.get("message", {}).get("items", [])
    meta = {"search_id": a.search_id, "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "source": "Crossref API", "query": a.query, "filters": [], "url": url,
            "hit_count": data.get("message", {}).get("total-results"), "returned": len(items)}
    save(a.search_id, data, meta)
    print(f"[{a.search_id}] Crossref hits={meta['hit_count']} returned={meta['returned']}")
    for i, it in enumerate(items, 1):
        au = ", ".join(f"{x.get('family', '')}" for x in it.get("author", [])[:3])
        yr = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
        print(f"{i:>2}. {yr} | {(it.get('title') or [''])[0]}\n    {au} | {(it.get('container-title') or [''])[0]} | doi:{it.get('DOI')} | {it.get('type')}")


def run_doi(a):
    doi = a.query.replace("https://doi.org/", "")
    out = {}
    try:
        out["crossref"] = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    except Exception as e:
        out["crossref_error"] = str(e)
    try:
        out["openalex"] = get_json("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi))
    except Exception as e:
        out["openalex_error"] = str(e)
    meta = {"search_id": a.search_id, "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "source": "DOI check (Crossref + OpenAlex)", "query": doi, "filters": [], "url": "",
            "hit_count": int("crossref" in out), "returned": int("crossref" in out)}
    save(a.search_id, out, meta)
    m = out.get("crossref", {}).get("message", {})
    if m:
        au = "; ".join(f"{x.get('given', '')} {x.get('family', '')}".strip() for x in m.get("author", []))
        yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
        print(f"[{a.search_id}] VERIFIED via Crossref: {(m.get('title') or [''])[0]} | {au} | {yr} | "
              f"{(m.get('container-title') or [''])[0]} | vol {m.get('volume')} iss {m.get('issue')} p {m.get('page')} | {m.get('type')}")
    else:
        print(f"[{a.search_id}] Crossref: NOT FOUND ({out.get('crossref_error')})")
    w = out.get("openalex", {})
    if w:
        print(f"    OpenAlex: {w.get('display_name')} | oa={((w.get('open_access') or {}).get('oa_url'))}")
        print("    ABS: " + abstract_from_inverted(w.get("abstract_inverted_index"))[:1500])


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("search_id")
    p.add_argument("source", choices=["openalex", "crossref", "doi"])
    p.add_argument("query")
    p.add_argument("--from-year", type=int)
    p.add_argument("--n", type=int, default=25)
    p.add_argument("--field", default="title_and_abstract", choices=["title_and_abstract", "title", "search"])
    p.add_argument("--cites", help="OpenAlex work ID (W...) for forward citation chasing")
    a = p.parse_args()
    {"openalex": run_openalex, "crossref": run_crossref, "doi": run_doi}[a.source](a)
