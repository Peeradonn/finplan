"""
Render the proposal HTML to PDF with headless Chrome, then check it.
Usage:  python render.py [template.html]       -> build/<name>.pdf, build/page-N.png

Checks printed: page count (rule: 15 max), pages that overflow their A4 box,
free space left on each page, and every font size used (rule: body 12pt Times New Roman).
Needs: Chrome or Edge, and PyMuPDF (pip install pymupdf).
"""
import os, re, sys, subprocess, collections
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else "template.html")
BUILD = os.path.join(HERE, "build")
os.makedirs(BUILD, exist_ok=True)
PDF = os.path.join(BUILD, os.path.splitext(os.path.basename(SRC))[0] + ".pdf")

BROWSERS = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
browser = next((b for b in BROWSERS if os.path.exists(b)), None) or sys.exit("No Chrome or Edge found.")
url = "file:///" + SRC.replace("\\", "/")
common = [browser, "--headless=new", "--disable-gpu", "--no-first-run", "--virtual-time-budget=10000"]

subprocess.run(common + ["--no-pdf-header-footer", f"--print-to-pdf={PDF}", url],
               check=True, capture_output=True)
dom = subprocess.run(common + ["--dump-dom", url], check=True, capture_output=True, text=True, encoding="utf-8").stdout

# ---- layout report (from the check script inside the HTML) ----
pages = re.findall(r'<section class="page([^"]*)"([^>]*)>', dom)
print(f"{os.path.basename(PDF)}")
for i, (cls, attrs) in enumerate(pages, 1):
    over = re.search(r'data-overflow="([^"]+)"', attrs)
    free = re.search(r'data-free="([^"]+)"', attrs)
    status = f"OVERFLOWS by {over.group(1)}" if over else (f"fits, {free.group(1)} mm free" if free else "fits")
    print(f"  page {i:>2}: {status}")

# ---- PDF checks ----
doc = pymupdf.open(PDF)
print(f"  pages in PDF: {doc.page_count} (limit 15)")
sizes = collections.Counter()
for page in doc:
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for s in line["spans"]:
                if s["text"].strip():
                    sizes[(s["font"].split("+")[-1], round(s["size"], 1))] += len(s["text"])
print("  text by font and size (characters):")
for (font, size), n in sorted(sizes.items(), key=lambda x: (-x[1])):
    flag = "" if size >= 11.9 or "Times" not in font else "   <- below 12pt"
    print(f"    {font:<28}{size:>5}pt {n:>7}{flag}")
for i, page in enumerate(doc, 1):
    page.get_pixmap(dpi=110).save(os.path.join(BUILD, f"page-{i}.png"))
print(f"  previews: {BUILD}\\page-N.png")
