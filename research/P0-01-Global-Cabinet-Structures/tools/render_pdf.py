"""Render PDF pages to PNG for visual inspection. Usage: python render_pdf.py <pdf_or_hash> [pages like 2,3] [dpi]"""
import sys, os, glob
import pymupdf
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw_snapshots")
OUT = os.path.join(BASE, "evidence_text", "renders")
os.makedirs(OUT, exist_ok=True)
arg = sys.argv[1]
path = arg if os.path.exists(arg) else glob.glob(os.path.join(RAW, f"*{arg}*.pdf"))[0]
pages = [int(p)-1 for p in sys.argv[2].split(",")] if len(sys.argv) > 2 else None
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 110
doc = pymupdf.open(path)
stem = os.path.splitext(os.path.basename(path))[0]
for i, page in enumerate(doc):
    if pages and i not in pages: continue
    pix = page.get_pixmap(dpi=dpi)
    fn = os.path.join(OUT, f"{stem}_p{i+1}.png")
    pix.save(fn)
    print(fn)
