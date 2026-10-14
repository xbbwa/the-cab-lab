"""P0-01-B compliant fetcher: robots.txt check, per-domain rate limit, hashing, snapshot.

Usage:
  python fetch.py robots <domain_or_url>     -> check robots.txt status
  python fetch.py get <url> [label]          -> fetch url respecting robots + rate limit
  python fetch.py head <url>                 -> HEAD request only
Outputs a single JSON line to stdout. Snapshots saved under raw_snapshots/.
"""
import hashlib
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw_snapshots")
LOGS = os.path.join(BASE, "logs")
STATE = os.path.join(BASE, "00_RUN_STATE.json")
DOMAIN_STATE = os.path.join(LOGS, "domain_state.json")
ROBOTS_CACHE = os.path.join(LOGS, "robots_cache.json")

UA = "Mozilla/5.0 (compatible; P0-01-Research/1.0; academic evidence collection; +devin)"
RATE_LIMIT_S = 5.0
TIMEOUT = 30

os.makedirs(RAW, exist_ok=True)
os.makedirs(LOGS, exist_ok=True)


def _load(path, default):
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default


def _save(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)


def _now():
    return datetime.now(timezone.utc).isoformat()


def domain_of(url):
    return urllib.parse.urlparse(url).netloc.lower()


def check_robots(url):
    """Return (allowed, robots_url, note). Cached per domain."""
    dom = domain_of(url)
    cache = _load(ROBOTS_CACHE, {})
    if dom in cache:
        c = cache[dom]
        if c.get("error"):
            return True, c.get("robots_url", ""), "robots_fetch_failed_assume_ok"
        rp_data = c.get("rules_text")
        if rp_data is None:
            return True, c.get("robots_url", ""), "no_robots"
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(c["robots_url"])
        rp.parse(rp_data.splitlines())
        allowed = rp.can_fetch(UA, url) and rp.can_fetch("*", url)
        delay = rp.crawl_delay("*") or rp.crawl_delay(UA)
        return allowed, c["robots_url"], ("allowed" if allowed else "disallowed_by_robots") + (f";crawl_delay={delay}" if delay else "")

    parsed = urllib.parse.urlparse(url)
    robots_url = f"{parsed.scheme}://{dom}/robots.txt"
    ctx = ssl.create_default_context()
    req = urllib.request.Request(robots_url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            text = r.read().decode("utf-8", errors="replace")
        cache[dom] = {"robots_url": robots_url, "rules_text": text, "fetched_at": _now()}
        _save(ROBOTS_CACHE, cache)
        return check_robots(url)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            cache[dom] = {"robots_url": robots_url, "rules_text": None, "fetched_at": _now()}
        else:
            cache[dom] = {"robots_url": robots_url, "error": f"http_{e.code}", "fetched_at": _now()}
        _save(ROBOTS_CACHE, cache)
        return True, robots_url, ("no_robots_404" if e.code == 404 else f"robots_http_{e.code}_assume_ok")
    except Exception as e:
        cache[dom] = {"robots_url": robots_url, "error": str(e)[:200], "fetched_at": _now()}
        _save(ROBOTS_CACHE, cache)
        return True, robots_url, "robots_unreachable_assume_ok"


def enforce_rate_limit(dom):
    st = _load(DOMAIN_STATE, {})
    last = st.get(dom, 0)
    wait = RATE_LIMIT_S - (time.time() - last)
    if wait > 0:
        time.sleep(wait)
    st[dom] = time.time()
    _save(DOMAIN_STATE, st)


def fetch(url, label=None, head_only=False):
    dom = domain_of(url)
    allowed, robots_url, note = check_robots(url)
    result = {"url": url, "domain": dom, "robots_url": robots_url, "robots_note": note,
              "accessed_at": _now(), "ok": False}
    if not allowed:
        result["status"] = "BLOCKED_BY_ROBOTS"
        print(json.dumps(result, ensure_ascii=False))
        return result
    enforce_rate_limit(dom)
    ctx = ssl.create_default_context()
    method = "HEAD" if head_only else "GET"
    req = urllib.request.Request(url, headers={"User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/pdf,*/*"}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            body = b"" if head_only else r.read()
            result.update({
                "ok": True, "http_status": r.status,
                "final_url": r.geturl(),
                "content_type": r.headers.get("Content-Type", ""),
                "content_length": len(body),
                "sha256": hashlib.sha256(body).hexdigest() if body else None,
            })
            if not head_only and body:
                h = result["sha256"][:16]
                ext = ".pdf" if "pdf" in result["content_type"].lower() or url.lower().endswith(".pdf") else ".html"
                fn = f"{dom.replace('.','_')}__{h}{ext}"
                path = os.path.join(RAW, fn)
                with open(path, "wb") as f:
                    f.write(body)
                result["snapshot"] = os.path.relpath(path, BASE)
    except urllib.error.HTTPError as e:
        result.update({"http_status": e.code, "error": f"http_{e.code}",
                       "status": "BLOCKED" if e.code in (403, 429) else "HTTP_ERROR"})
    except Exception as e:
        result.update({"error": str(e)[:300], "status": "NETWORK_ERROR"})
    result.setdefault("status", "FETCHED" if result["ok"] else "FAILED")
    with open(os.path.join(LOGS, "fetch_log.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")
    print(json.dumps(result, ensure_ascii=False))
    return result


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    cmd, arg = sys.argv[1], sys.argv[2]
    if cmd == "robots":
        url = arg if arg.startswith("http") else f"https://{arg}/"
        allowed, robots_url, note = check_robots(url)
        print(json.dumps({"domain": domain_of(url), "robots_url": robots_url,
                          "allowed": allowed, "note": note}, ensure_ascii=False))
    elif cmd == "get":
        fetch(arg, label=sys.argv[3] if len(sys.argv) > 3 else None)
    elif cmd == "head":
        fetch(arg, head_only=True)
    else:
        print(__doc__)
        sys.exit(1)
