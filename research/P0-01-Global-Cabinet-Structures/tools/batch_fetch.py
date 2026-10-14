"""Fetch a list of URLs with robots+ratelimit (reuses fetch.py). Args: file with 'url[,label]' lines."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    url, _, label = line.partition(',')
    fetch(url.strip(), label.strip() or None)
