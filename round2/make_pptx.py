"""The PowerPoint file for Round Two ("A set of Power point slides of the presentation", scored on its own as "Quality
of ppt"), made from the built deck so the two can never differ.

  .venv/Scripts/python.exe round2/make.py           # first: build round2/Axis.html
  .venv/Scripts/python.exe round2/make_pptx.py      # then: round2/Axis.pptx

Each slide is the HTML slide in its final state (no builds), captured by headless Chrome at 2x (2560 x 1440) and
placed full-bleed on a 16:9 slide. Pictures, not native shapes, on purpose (25 Oct): the deck's font (Plus Jakarta
Sans) isn't installed on the judges' machines and PowerPoint would swap it, and the charts, the map and the house
are drawn in HTML/SVG. Each picture carries the slide's title as its alt text; the speaker notes carry the spoken
script (the words before "[Notes: ...]"; the bracketed team notes stay out, some are internal). Sections follow the
deck's footer tracker.

Metadata (CLAUDE.md hard rule): author and last-modified-by "Team Axis", no company, no account. Re-saving the file in
PowerPoint while signed in stamps the account into it: don't, or scrub it (File > Info > Check for Issues > Inspect
Document) and check with this script's --check option.
"""
import datetime
import html as H
import os
import re
import subprocess
import sys
import uuid
import zipfile

from pptx import Presentation
from pptx.util import Emu

HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.join(HERE, "Axis.html")
OUT = os.path.join(HERE, "Axis.pptx")
SHOTS = os.path.join(HERE, "build", "pptx")
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
# the footer tracker's sections, by slide number
SECTIONS = [("Cover", [1]), ("The problem", [2, 3]), ("The answer", [4]), ("The five calls", [5, 6, 7, 8, 9]),
            ("Will it hold", [10]), ("What next", [11, 12]), ("Us", [13, 14]), ("Close", [15])]
SEC = re.compile(r'<section class="slide[^"]*"[^>]*>(.*?)</section>', re.S)
plain = lambda s: re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def slides(deck):
    """(title, spoken script) for each slide, in order."""
    out = []
    for body in SEC.findall(deck):
        t = re.search(r"<h2>(.*?)</h2>", body, re.S) or re.search(r"<h1>(.*?)</h1>", body, re.S)
        title = plain(t.group(1).replace("<br>", " ")) if t else ""
        n = re.search(r'<aside class="notes">(.*?)</aside>', body, re.S)
        spoken = plain(n.group(1)).split("[Notes:")[0].strip() if n else ""
        # one paragraph a speaker: "PETE: ..." -> "Pete: ..."
        parts = re.split(r"\b(PETE|FAHTAI|WIN|LOOKBUA|ALL):\s*", spoken)
        lines = [f"{who.title()}: {txt.strip()}" for who, txt in zip(parts[1::2], parts[2::2]) if txt.strip()]
        out.append((title, "\n".join(lines) or spoken))
    return out


def shoot(deck, n, path):
    """Slide n alone, at 2x, as Chrome renders it (fonts and the arrows drawn after load)."""
    base = '<base href="file:///' + HERE.replace("\\", "/") + '/">'
    css = ("<style>.deck{padding:0!important;gap:0!important;display:block!important}.slide{display:none!important}"
           f".slide:nth-of-type({n}){{display:flex!important}}body{{margin:0;background:#fff}}</style></head>")
    page = os.path.join(SHOTS, f"_slide{n:02d}.html")
    with open(page, "w", encoding="utf-8") as f:
        f.write(deck.replace("<head>", "<head>" + base, 1).replace("</head>", css, 1))
    exe = next(c for c in CHROME if os.path.exists(c))
    subprocess.run([exe, "--headless=new", "--disable-gpu", "--force-device-scale-factor=2", "--window-size=1280,720",
                    "--hide-scrollbars", "--virtual-time-budget=8000", f"--screenshot={path}",
                    "file:///" + page.replace("\\", "/")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(page)


def add_sections(prs):
    """PowerPoint's sections (p14:sectionLst), appended as the presentation's last extension."""
    ids = [s.slide_id for s in prs.slides]
    P = "http://schemas.openxmlformats.org/presentationml/2006/main"
    P14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
    secs = "".join(
        f'<p14:section name="{H.escape(name)}" id="{{{str(uuid.uuid4()).upper()}}}"><p14:sldIdLst>'
        + "".join(f'<p14:sldId id="{ids[i - 1]}"/>' for i in nums) + "</p14:sldIdLst></p14:section>"
        for name, nums in SECTIONS)
    from lxml import etree
    ext = etree.fromstring(f'<p:ext xmlns:p="{P}" uri="{{521415D9-36F7-43E2-AB2F-B90AF26B5E84}}">'
                           f'<p14:sectionLst xmlns:p14="{P14}">{secs}</p14:sectionLst></p:ext>')
    root = prs.part._element
    lst = root.find(f"{{{P}}}extLst")
    if lst is None:
        lst = etree.SubElement(root, f"{{{P}}}extLst")   # extLst is the last child of p:presentation
    lst.append(ext)


def tidy(path, n_slides, cover_png):
    """python-pptx's blank template leaves its own app.xml ("Macintosh PowerPoint", 4:3, 0 slides) and a thumbnail of
    an empty slide: rewrite the first with this deck's facts and no company, and make the thumbnail our cover."""
    import io
    from PIL import Image
    app = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
           '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
           'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
           '<TotalTime>0</TotalTime><Words>0</Words><Application>Microsoft Office PowerPoint</Application>'
           f'<PresentationFormat>Widescreen</PresentationFormat><Paragraphs>0</Paragraphs><Slides>{n_slides}</Slides>'
           f'<Notes>{n_slides}</Notes><HiddenSlides>0</HiddenSlides><MMClips>0</MMClips><ScaleCrop>false</ScaleCrop>'
           '<Company></Company><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc>'
           '<HyperlinksChanged>false</HyperlinksChanged><AppVersion>16.0000</AppVersion></Properties>')
    im = Image.open(cover_png).convert("RGB")
    im.thumbnail((256, 144))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=85)
    tmp = path + ".tmp"
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "docProps/app.xml":
                data = app.encode("utf-8")
            elif item.filename == "docProps/thumbnail.jpeg":
                data = buf.getvalue()
            zout.writestr(item, data)
    os.replace(tmp, path)


def check(path):
    """Print the package's metadata, so nobody submits a file that names an account."""
    with zipfile.ZipFile(path) as z:
        for name in ("docProps/core.xml", "docProps/app.xml"):
            if name in z.namelist():
                print(f"--- {name}\n{z.read(name).decode('utf-8')}")
        bad = [n for n in z.namelist() if "thumbnail" in n.lower()]
        print("thumbnail parts:", bad or "none")


def main():
    if "--check" in sys.argv:
        check(sys.argv[sys.argv.index("--check") + 1] if len(sys.argv) > 2 else OUT)
        return
    deck = open(DECK, encoding="utf-8").read()
    if "{{" in deck or "[[" in deck:
        sys.exit("Axis.html still has unfilled placeholders: run make.py first")
    info = slides(deck)
    assert len(info) == sum(len(n) for _, n in SECTIONS), f"{len(info)} slides, sections cover a different count"
    os.makedirs(SHOTS, exist_ok=True)
    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)    # 13.333 x 7.5 in, 16:9
    blank = prs.slide_layouts[6]
    for i, (title, spoken) in enumerate(info, 1):
        png = os.path.join(SHOTS, f"slide-{i:02d}.png")
        shoot(deck, i, png)
        s = prs.slides.add_slide(blank)
        pic = s.shapes.add_picture(png, 0, 0, prs.slide_width, prs.slide_height)
        pic._element.nvPicPr.cNvPr.set("descr", title)          # alt text: the slide's claim
        pic._element.nvPicPr.cNvPr.set("name", f"Slide {i}")
        s.notes_slide.notes_text_frame.text = spoken
        print(f"{i:2d}  {title[:70]}")
    add_sections(prs)
    cp = prs.core_properties
    now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None, microsecond=0)
    cp.author = cp.last_modified_by = "Team Axis"
    cp.title, cp.subject = "Built to Last", "UFP Award 2026, Round Two: a financial proposal for the Wong family"
    cp.keywords = cp.comments = cp.category = ""
    cp.revision, cp.created, cp.modified = 1, now, now
    prs.save(OUT)
    tidy(OUT, len(info), os.path.join(SHOTS, "slide-01.png"))
    print(f"-> {OUT} ({os.path.getsize(OUT) / 1e6:.1f} MB)")
    check(OUT)


if __name__ == "__main__":
    main()
