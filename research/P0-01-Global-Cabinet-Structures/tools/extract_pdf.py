"""Extract text from PDFs in raw_snapshots/ to 09_EVIDENCE/<name>.txt"""
import os, sys
from pypdf import PdfReader

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw_snapshots")
EV = os.path.join(BASE, "evidence_text")
os.makedirs(EV, exist_ok=True)

def extract(path):
    try:
        r = PdfReader(path)
        parts = []
        for i, p in enumerate(r.pages):
            t = p.extract_text() or ""
            parts.append(f"\n===== PAGE {i+1} =====\n{t}")
        return "".join(parts), len(r.pages)
    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    files = sys.argv[1:] or [os.path.join(RAW, f) for f in os.listdir(RAW) if f.lower().endswith(".pdf")]
    for path in files:
        name = os.path.splitext(os.path.basename(path))[0]
        text, info = extract(path)
        if text is None:
            print(f"{name}: FAILED {info}")
            continue
        out = os.path.join(EV, name + ".txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(f"SOURCE_FILE: {path}\nPAGES: {info}\n")
            f.write(text)
        print(f"{name}: {info} pages -> {os.path.relpath(out, BASE)}")
