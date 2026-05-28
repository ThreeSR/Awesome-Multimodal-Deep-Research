#!/usr/bin/env python3
"""arXiv-first fetcher for the Multimodal Deep Research paper list.

Resolves a paper from --id / --url / --title, pulls metadata from arXiv
(Atom API first, HTML abstract page as fallback when the API is throttled),
and inserts a formatted entry into README.md under a chosen section.

Design notes:
  * stdlib only, no LLM, no auto-push. We write the file; you review and commit.
  * arXiv has two independent rate-limit pools. The Atom API
    (export.arxiv.org/api/query) throttles aggressively with HTTP 429; the
    HTML page (arxiv.org/abs/<id>) is far more lenient. So on 429/empty we
    fall back to HTML rather than retrying the API (a retry only extends the ban).
"""

import argparse
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

API_URL = "http://export.arxiv.org/api/query"
ABS_URL = "https://arxiv.org/abs/{id}"
PDF_URL = "https://arxiv.org/pdf/{id}"
USER_AGENT = "Awesome-Multimodal-Deep-Research/1.0 (paper-list maintenance; mailto:ruis@g.ucla.edu)"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}

ID_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")
TLDR_MAX = 160


class FetchError(Exception):
    pass


# --------------------------------------------------------------------------- #
# HTTP

def _get(url, timeout=30):
    """Single GET. Returns (status, body_text). Never retries on 429."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace") if e.fp else ""
    except TimeoutError as e:
        raise FetchError(
            f"timed out fetching {url} (arXiv slow or throttled); try again shortly"
        ) from e
    except urllib.error.URLError as e:
        raise FetchError(f"network error fetching {url}: {e.reason}") from e


# --------------------------------------------------------------------------- #
# ID resolution

def normalize_title(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def extract_id(url_or_id):
    m = ID_RE.search(url_or_id)
    if not m:
        raise FetchError(f"could not parse an arXiv id from {url_or_id!r}")
    return m.group(1)  # bare id, no version, for stable links


def search_id_by_title(title):
    """Query the Atom API by title, return the best-matching arXiv id.

    Refuses to guess when the closest match is weak, to avoid pulling in the
    wrong paper (a recurring failure mode of fuzzy title search).
    """
    q = urllib.parse.quote(f'ti:"{title}"')
    url = f"{API_URL}?search_query={q}&max_results=5"
    status, body = _get(url)
    if status == 429:
        raise FetchError(
            "arXiv API returned 429 (throttled). Wait 5+ minutes; do NOT retry "
            "in a loop. If you know the id, pass --id instead (title search has "
            "no HTML fallback)."
        )
    if status != 200:
        raise FetchError(f"arXiv API returned HTTP {status} for title search")

    root = ET.fromstring(body)
    entries = root.findall("atom:entry", NS)
    if not entries:
        raise FetchError(f"no arXiv results for title {title!r}")

    want = normalize_title(title)
    scored = []
    for e in entries:
        t = (e.findtext("atom:title", default="", namespaces=NS) or "").strip()
        score = _title_score(want, normalize_title(t))
        aid = extract_id(e.findtext("atom:id", default="", namespaces=NS))
        scored.append((score, aid, t))
    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best_id, best_title = scored[0]

    def _candidates():
        return "\n".join(f"  [{s:.2f}] {i}  {t}" for s, i, t in scored[:3])

    if best_score < 0.6:
        raise FetchError(
            f"no confident title match (best score {best_score:.2f}). "
            f"Candidates:\n{_candidates()}\n"
            "Pass --id explicitly if one of these is right."
        )
    if len(scored) > 1 and scored[1][0] >= 0.85 and best_score - scored[1][0] < 0.1:
        raise FetchError(
            "ambiguous title match (top candidates score too close, e.g. a "
            f"'Name' vs 'Name-Plus' collision):\n{_candidates()}\n"
            "Pass --id explicitly to disambiguate."
        )
    if best_score < 0.85:
        sys.stderr.write(
            f"[warn] fuzzy title match {best_score:.2f}: '{best_title}' -> {best_id}\n"
        )
    return best_id


def _title_score(want, cand):
    if want == cand:
        return 1.0
    if cand.startswith(want):  # arXiv "ShortName: long subtitle" pattern
        return 0.95
    if want in cand:
        return 0.88
    return SequenceMatcher(None, want, cand).ratio()


# --------------------------------------------------------------------------- #
# Metadata fetch

def fetch_meta_api(arxiv_id):
    url = f"{API_URL}?id_list={arxiv_id}&max_results=1"
    status, body = _get(url)
    if status == 429:
        return None  # caller falls back to HTML
    if status != 200:
        raise FetchError(f"arXiv API returned HTTP {status} for id {arxiv_id}")

    root = ET.fromstring(body)
    entry = root.find("atom:entry", NS)
    if entry is None:
        return None
    title = entry.findtext("atom:title", default="", namespaces=NS)
    summary = entry.findtext("atom:summary", default="", namespaces=NS)
    if not title or not summary.strip():
        return None

    authors, affils = [], []
    for a in entry.findall("atom:author", NS):
        name = a.findtext("atom:name", default="", namespaces=NS).strip()
        if name:
            authors.append(name)
        aff = a.findtext("arxiv:affiliation", default="", namespaces=NS)
        if aff and aff.strip():
            affils.append(aff.strip())

    published = entry.findtext("atom:published", default="", namespaces=NS)
    journal_ref = entry.findtext("arxiv:journal_ref", default="", namespaces=NS)

    return {
        "id": arxiv_id,
        "title": clean_text(title),
        "abstract": clean_text(summary),
        "authors": authors,
        "affiliations": sorted(set(affils)),
        "date": published[:7] if published else "",  # YYYY-MM
        "journal_ref": clean_text(journal_ref) if journal_ref else "",
        "source": "api",
    }


def fetch_meta_html(arxiv_id):
    """Fallback parser for arxiv.org/abs/<id> (lenient rate-limit pool)."""
    status, html = _get(ABS_URL.format(id=arxiv_id))
    if status == 429:
        raise FetchError(
            "arXiv HTML page also returned 429. Both rate-limit pools are "
            "throttled, which is unusual. Wait several minutes and retry once."
        )
    if status != 200:
        raise FetchError(f"arXiv HTML page returned HTTP {status} for {arxiv_id}")

    abs_m = re.search(
        r'<blockquote[^>]*class="abstract[^"]*"[^>]*>(.*?)</blockquote>', html, re.S
    )
    title_m = re.search(r'<h1[^>]*class="title[^"]*"[^>]*>(.*?)</h1>', html, re.S)
    date_m = re.search(r"\[Submitted on\s+(.*?)[\]\(]", html)
    if not abs_m or not title_m:
        raise FetchError(f"could not parse title/abstract from HTML for {arxiv_id}")

    title = re.sub(r"^\s*Title:\s*", "", strip_tags(title_m.group(1)))
    abstract = re.sub(r"^\s*Abstract:\s*", "", strip_tags(abs_m.group(1)))

    date = ""
    if date_m:
        # e.g. "5 Aug 2025" -> 2025-08
        date = parse_loose_date(date_m.group(1))

    return {
        "id": arxiv_id,
        "title": clean_text(title),
        "abstract": clean_text(abstract),
        "authors": [],
        "affiliations": [],
        "date": date,
        "journal_ref": "",
        "source": "html",
    }


def fetch_meta(arxiv_id):
    meta = fetch_meta_api(arxiv_id)
    if meta is None:
        sys.stderr.write("[info] Atom API empty/throttled; falling back to HTML page\n")
        meta = fetch_meta_html(arxiv_id)
    return meta


# --------------------------------------------------------------------------- #
# Text helpers

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def clean_text(s):
    s = html.unescape(s)
    s = re.sub(r"\\([%&_#$])", r"\1", s)  # unescape LaTeX char escapes
    s = s.replace("\n", " ").replace("\r", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


_MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def parse_loose_date(s):
    m = re.search(r"(\d{1,2})\s+([A-Za-z]{3})[a-z]*\s+(\d{4})", s)
    if not m:
        return ""
    mon = _MONTHS.get(m.group(2)[:3], 0)
    return f"{m.group(3)}-{mon:02d}" if mon else m.group(3)


def make_tldr(abstract):
    """First-sentence fallback TL;DR, truncated. Refined by hand afterwards."""
    first = re.split(r"(?<=[.!?])\s+", abstract.strip(), maxsplit=1)[0]
    first = first.strip()
    if len(first) > TLDR_MAX:
        first = first[:TLDR_MAX].rsplit(" ", 1)[0] + "..."
    return first


# --------------------------------------------------------------------------- #
# Entry rendering

def github_stars_badge(url):
    """Auto-updating shields.io star badge for a github repo URL, else ''."""
    m = re.search(r"github\.com/([^/\s]+)/([^/\s#?]+)", url)
    if not m:
        return ""
    owner, repo = m.group(1), m.group(2)
    if repo.endswith(".git"):
        repo = repo[:-4]
    badge = f"https://img.shields.io/github/stars/{owner}/{repo}?style=social"
    return f"[![Stars]({badge})]({url})"


def render_entry(meta, *, tldr, affiliation, venue, base, code, project):
    abs_url = ABS_URL.format(id=meta["id"])
    pdf_url = PDF_URL.format(id=meta["id"])

    venue = venue or meta.get("journal_ref") or ""
    aff = affiliation or (meta["affiliations"][0] if meta["affiliations"] else "")

    tldr_text = (tldr or "").strip()
    tldr_is_auto = not tldr_text
    if tldr_is_auto:
        tldr_text = make_tldr(meta["abstract"])

    lines = [f'#### [{meta["title"]}]({abs_url})']

    meta_tokens = []
    if aff:
        meta_tokens.append(f"`{aff}`")
    if venue:
        meta_tokens.append(f"`{venue}`")
    if meta.get("date"):
        meta_tokens.append(meta["date"])
    if base:
        meta_tokens.append(f"Base: `{base}`")
    meta_tokens.append(f"[PDF]({pdf_url})")
    if code:
        token = f"[Code]({code})"
        badge = github_stars_badge(code)
        if badge:
            token += f" {badge}"
        meta_tokens.append(token)
    if project:
        meta_tokens.append(f"[Project]({project})")
    lines.append(" · ".join(meta_tokens))
    lines.append("")
    lines.append(f"> **TL;DR.** {tldr_text}")
    if tldr_is_auto:
        lines.append("<!-- TLDR: refine -->")
    lines.append("")
    lines.append("<details><summary>Abstract</summary>")
    lines.append("")
    lines.append(meta["abstract"])
    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# README insertion

def find_section_bounds(text, section):
    """Return (insert_line_index, heading_level) for the named section.

    insert_line_index is the line at which to insert a new entry (end of the
    section, just before the next heading of the same or higher level).
    """
    lines = text.splitlines()
    head_re = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
    start = None
    level = None
    for i, line in enumerate(lines):
        m = head_re.match(line)
        if m and normalize_title(m.group(2)) == normalize_title(section):
            start = i
            level = len(m.group(1))
            break
    if start is None:
        raise FetchError(
            f"section {section!r} not found in README. "
            "Add the heading first, or check spelling."
        )

    end = len(lines)
    for j in range(start + 1, len(lines)):
        m = head_re.match(lines[j])
        if m and len(m.group(1)) <= level:
            end = j
            break
    # back up over trailing blank lines so we insert right after content
    while end - 1 > start and lines[end - 1].strip() == "":
        end -= 1
    return end, level


def insert_entry(readme_path, section, entry_md):
    with open(readme_path, encoding="utf-8") as f:
        text = f.read()
    insert_at, _ = find_section_bounds(text, section)
    lines = text.splitlines()
    block = ["", entry_md]  # blank separator + entry
    new_lines = lines[:insert_at] + block + lines[insert_at:]
    new_text = "\n".join(new_lines)
    if not new_text.endswith("\n"):
        new_text += "\n"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_text)


def id_already_present(readme_path, arxiv_id):
    try:
        with open(readme_path, encoding="utf-8") as f:
            return arxiv_id in f.read()
    except FileNotFoundError:
        return False


# --------------------------------------------------------------------------- #
# CLI

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--id", help="arXiv id, e.g. 2508.01234")
    src.add_argument("--url", help="arXiv abs/pdf URL")
    src.add_argument("--title", help="paper title (Atom API search, no HTML fallback)")

    p.add_argument("--section", default="Benchmarks",
                   help="README heading to insert under (default: Benchmarks)")
    p.add_argument("--readme", default="README.md")
    p.add_argument("--tldr", help="one-line TL;DR (recommended; else first-sentence fallback)")
    p.add_argument("--affiliation", help="affiliation (arXiv rarely provides this)")
    p.add_argument("--venue", help="venue, e.g. 'ICLR 2026'")
    p.add_argument("--base", help="base model, e.g. 'Qwen2.5-VL'")
    p.add_argument("--code", help="code repo URL")
    p.add_argument("--project", help="project page URL")
    p.add_argument("--html-only", action="store_true",
                   help="skip the Atom API and parse the HTML abstract page directly "
                        "(use with --id/--url when the API is throttled)")
    p.add_argument("--dry-run", action="store_true", help="print entry, do not write")
    p.add_argument("--force", action="store_true", help="insert even if id already in README")
    args = p.parse_args()

    try:
        if args.title:
            arxiv_id = search_id_by_title(args.title)
        else:
            arxiv_id = extract_id(args.url or args.id)

        if not args.dry_run and not args.force and id_already_present(args.readme, arxiv_id):
            sys.stderr.write(
                f"[skip] {arxiv_id} already present in {args.readme}. "
                "Use --force to insert anyway.\n"
            )
            return 0

        meta = fetch_meta_html(arxiv_id) if args.html_only else fetch_meta(arxiv_id)
        entry = render_entry(
            meta, tldr=args.tldr, affiliation=args.affiliation, venue=args.venue,
            base=args.base, code=args.code, project=args.project,
        )

        if args.dry_run:
            print(entry)
        else:
            insert_entry(args.readme, args.section, entry)

        # short report to stderr
        aff_status = (args.affiliation or (meta["affiliations"][0]
                      if meta["affiliations"] else "(none from arXiv — omitted)"))
        tldr_status = "manual" if args.tldr else "AUTO (refine!)"
        sys.stderr.write(
            "\n[report]\n"
            f"  id        : {arxiv_id}\n"
            f"  title     : {meta['title']}\n"
            f"  date      : {meta['date'] or '?'}\n"
            f"  source    : {meta['source']}\n"
            f"  affiliation: {aff_status}\n"
            f"  tldr      : {tldr_status}\n"
            f"  section   : {args.section}\n"
            f"  written   : {'no (dry-run)' if args.dry_run else args.readme}\n"
        )
        return 0
    except FetchError as e:
        sys.stderr.write(f"[error] {e}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
