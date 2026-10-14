"""Fetch each kaboodle product page, extract storyblok pdf urls, write dedup queue."""
import re, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch, BASE
found = {}
for slug in open(os.path.join(BASE, "logs", "product_pages.txt"), encoding='utf-8'):
    slug = slug.strip()
    if not slug: continue
    url = f"https://kaboodle.com.au/products/cabinets/{slug}"
    r = fetch(url, slug)
    if not r.get("snapshot"):
        continue
    html = open(os.path.join(BASE, r["snapshot"]), encoding='utf-8', errors='replace').read()
    for p in re.findall(r"https://a\.storyblok\.com[^\"' <>]+?\.pdf", html):
        found.setdefault(p, []).append(slug)
q = os.path.join(BASE, "logs", "pdf_queue_all.txt")
with open(q, "w", encoding='utf-8') as f:
    for p, slugs in sorted(found.items()):
        f.write(p + "," + slugs[0].split("/")[-1] + "\n")
print(json.dumps({"pages_done": True, "unique_pdfs": len(found)}))
