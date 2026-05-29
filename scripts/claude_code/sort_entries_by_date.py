#!/usr/bin/env python3
"""Reorder the paper entries in README.md by date, most-recent first.

Each entry is a `#### ...` block; sections are delimited by `#`/`##`/`###`
headings. Within every section the `####` entries are sorted by the YYYY-MM
date on their meta line (descending). Entries without a date (proprietary
products, pointers, pending stubs) sort to the bottom, keeping their relative
order. Content inside fenced code blocks (e.g. the template in How to
Contribute) is ignored so its example `####` is never touched.

Usage: python3 scripts/claude_code/sort_entries_by_date.py [README.md]
"""
import re
import sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "README.md"

with open(PATH, encoding="utf-8") as f:
    lines = f.read().split("\n")

fence_re = re.compile(r"^\s*`{3,}")
head_re = re.compile(r"^(#{1,6})\s+(.*)$")
date_re = re.compile(r"\b(\d{4})-(\d{2})\b")

# Mark which lines sit inside a fenced code block (toggle on each ``` line).
in_fence = False
fenced = [False] * len(lines)
for i, ln in enumerate(lines):
    if fence_re.match(ln):
        fenced[i] = True            # the fence marker line itself
        in_fence = not in_fence
    else:
        fenced[i] = in_fence


def heading_level(i):
    if fenced[i]:
        return None
    m = head_re.match(lines[i])
    return len(m.group(1)) if m else None


def date_key(block):
    """(year, month) of the first YYYY-MM in the block; (0, 0) if undated."""
    for ln in block:
        m = date_re.search(ln)
        if m:
            return (int(m.group(1)), int(m.group(2)))
    return (0, 0)


out = []
i = 0
n = len(lines)
while i < n:
    if heading_level(i) == 4:
        # Collect a run of consecutive #### entry blocks within this section.
        entries = []
        while i < n and heading_level(i) == 4:
            j = i + 1
            while j < n and heading_level(j) is None:
                j += 1
            entries.append(lines[i:j])
            i = j
        for block in sorted(entries, key=date_key, reverse=True):
            while block and block[-1].strip() == "":
                block.pop()
            out.extend(block)
            out.append("")  # exactly one blank line after each entry
    else:
        out.append(lines[i])
        i += 1

text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
if not text.endswith("\n"):
    text += "\n"
with open(PATH, "w", encoding="utf-8") as f:
    f.write(text)
print(f"sorted {PATH}")
