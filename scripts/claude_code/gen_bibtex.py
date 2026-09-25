#!/usr/bin/env python3
"""Generate refs.bib for the mm-dr-survey from verified arXiv ids.

For each (citekey, arxiv_id) pair in MAPPING, fetch the arXiv abs HTML page,
extract the title and author list, and emit a `@misc{...}` entry with the
arXiv eprint reference. arXiv ids in MAPPING are all verified against the
Awesome-Multimodal-Deep-Research list, so titles / authors come from the real
arXiv pages (no hallucinated entries).

Usage:
    python3 scripts/claude_code/gen_bibtex.py > /path/to/refs.bib

Caches per arxiv_id so duplicates (e.g., realxbench/deepeyesv2) fetch once.
"""
import sys
import time

sys.path.insert(0, ".")
import fetch_arxiv  # noqa: E402

# citekey -> arxiv id. Verified against the Awesome-Multimodal-Deep-Research list.
MAPPING = {
    # Benchmarks: text-only
    "gaia":              "2311.12983",
    "gaia2":             "2602.11964",
    "browsecomp":        "2504.12516",
    "browsecompzh":      "2504.19314",
    "browsecompplus":    "2508.06600",
    "webwalker":         "2501.07572",
    "xbench":            "2506.13651",
    "deepsearchqa":      "2601.20975",
    "deepresearchbench": "2506.11763",
    "deepresearcheval":  "2601.09688",
    "livebrowsecomp":    "2605.28721",
    "autoresearchbench": "2604.25256",

    # Benchmarks: (multi-)image and text
    "mmsearch":          "2409.12959",
    "mmsearchplus":      "2508.21475",
    "mmbrowsecomp":      "2508.13186",
    "browsecompvl":      "2508.05748",   # introduced in WebWatcher
    "browsecompv3":      "2602.12876",
    "vdrbench":          "2602.02185",   # Vision-DeepResearch Benchmark
    "visbrowsebench":    "2603.16289",
    "mcsearch":          "2603.00873",
    "interlvsearch":     "2605.07510",
    "realxbench":        "2511.05271",   # introduced in DeepEyesV2
    "livevqa":           "2504.05288",
    "simplevqa":         "2502.13059",
    "hle":               "2501.14249",
    "dr3eval":           "2604.14683",
    "agenticmme":        "2604.03016",

    # Benchmarks: video and text
    "videobrowsecomp":   "2512.23044",
    "videobrowser":      "2512.23044",   # same paper as videobrowsecomp

    # Methods: text deep research
    "searchr1":          "2503.09516",
    "websailor":         "2507.02592",
    "webdancer":         "2505.22648",
    "webthinker":        "2504.21776",
    "drtulu":            "2511.19399",
    "drvenus":           "2604.19859",
    "tongyidr":          "2510.24701",
    "openseekerv2":      "2605.04036",
    "longseeker":        "2605.05191",
    "argus":             "2605.16217",

    # Methods: multimodal deep research
    "mmsearchr1":        "2506.20670",
    "webwatcher":        "2508.05748",
    "deepeyesv2":        "2511.05271",
    "opensearchvl":      "2605.05185",
    "deepmmsearchr1":    "2510.12801",
    "vdr":               "2601.22060",   # Vision-DeepResearch (method); Rui's existing key
    "visiondr":          "2601.22060",   # same paper
    "mmdeepresearch":    "2603.01050",
    "longhorizonmm":     "2604.12890",   # LMM-Searcher
    "hypereyes":         "2605.07177",
    "segresearch":       "2602.04454",
    "geovista":          "2511.15705",

    # Proprietary / model card
    "seed18":            "2603.20633",   # Seed1.8 Model Card

    # Open data synthesis
    "webshaper":         "2507.15061",
    "opendatasynthdr":   "2509.00375",
    "redsearcher":       "2602.14234",

    # Search-enhanced generation
    "multimodaldr":      "2506.02454",   # Multimodal DeepResearcher
    "gensearcher":       "2603.28767",
    "unifyagent":        "2603.29620",

    # Tools / supporting work cited in Tools and Evaluation sections
    "aris":              "2605.03042",   # ARIS
    "marcodr":           "2603.28376",   # Marco DeepResearch
    "fromwebtopixels":   "2605.12497",   # From Web to Pixels
    "videoseeker":       "2605.16079",
    "gam":               "2511.18423",   # General Agentic Memory

    # Training data
    "encyclopedicvqa":   "2306.09224",
    "infoseek":          "2302.11713",   # visual InfoSeek
}


def year_from_arxiv_id(aid):
    yy = int(aid[:2])
    return 2000 + yy


def escape_bib_value(s):
    # Keep braces around the value so bibtex doesn't mess with capitalisation.
    # We don't need to escape much because we wrap the whole thing in {}.
    return s.replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")


def make_entry(key, aid, meta):
    title = escape_bib_value(meta["title"])
    authors = meta.get("authors") or []
    author_str = " and ".join(authors) if authors else "Anonymous"
    year = year_from_arxiv_id(aid)
    url = f"https://arxiv.org/abs/{aid}"
    return (
        f"@misc{{{key},\n"
        f"  title         = {{{title}}},\n"
        f"  author        = {{{author_str}}},\n"
        f"  year          = {{{year}}},\n"
        f"  eprint        = {{{aid}}},\n"
        f"  archivePrefix = {{arXiv}},\n"
        f"  url           = {{{url}}}\n"
        f"}}\n"
    )


def main():
    cache = {}  # arxiv_id -> meta
    entries = []
    errors = []

    today = "2026-06-23"  # current date; used in the header comment
    print(f"% refs.bib for the mm-dr-survey")
    print(f"% claude-added {today}: generated by scripts/claude_code/gen_bibtex.py")
    print(f"% from verified arXiv ids in the Awesome-Multimodal-Deep-Research list.")
    print()

    # Sort for stable diff
    for key in sorted(MAPPING):
        aid = MAPPING[key]
        try:
            if aid not in cache:
                cache[aid] = fetch_arxiv.fetch_meta_html(aid)
                time.sleep(2)  # be polite
            meta = cache[aid]
            entry = make_entry(key, aid, meta)
            entries.append(entry)
            sys.stderr.write(
                f"OK  {key:20s} {aid}  {meta['title'][:60]}{'...' if len(meta['title'])>60 else ''}  "
                f"({len(meta.get('authors') or [])} authors)\n"
            )
        except Exception as e:
            errors.append((key, aid, str(e)))
            sys.stderr.write(f"ERR {key:20s} {aid}  {e}\n")

    print("".join(entries))

    if errors:
        sys.stderr.write(f"\n{len(errors)} errors:\n")
        for k, a, msg in errors:
            sys.stderr.write(f"  {k} ({a}): {msg}\n")

    sys.stderr.write(f"\nemitted {len(entries)} entries; {len(cache)} unique arxiv ids fetched.\n")


if __name__ == "__main__":
    main()
