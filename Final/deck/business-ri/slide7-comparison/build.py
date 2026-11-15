"""Copy slide 7 from the compared commits into an isolated comparison folder."""
from pathlib import Path
import base64
import html
import re
import subprocess

HERE = Path(__file__).resolve().parent
DECK = HERE.parents[1]
VERSIONS = [('main', '0f5d8b8'), ('revised', 'efce767')]

def git_text(ref, path):
    return subprocess.check_output(['git', 'show', ref + ':Final/deck/' + path], cwd=DECK).decode('utf-8')

for name, ref in VERSIONS:
    folder = HERE / name
    folder.mkdir(exist_ok=True)
    compiled = git_text(ref, 'Axis.html')
    sections = list(re.finditer(r'<section\b.*?</section>', compiled, re.S))
    slide = next(m.group() for m in sections if 'id="v6"' in m.group())
    head = compiled[:sections[0].start()]
    def font(match):
        data = base64.b64encode((DECK / match.group(1)).read_bytes()).decode('ascii')
        return 'url("data:font/ttf;base64,' + data + '")'
    head = re.sub(r'url\("(fonts/[^"\)]+)"\)', font, head)
    head += '<style>html,body{width:1280px;height:720px;overflow:hidden}.deck{zoom:1;padding:0;gap:0}.slide{box-shadow:none}</style>'
    (folder / 'Axis.html').write_text(head + slide + '</main></body></html>', encoding='utf-8', newline='\n')
    source = git_text(ref, 'src/01_talk.html')
    raw = re.search(r'<section class="slide sec-S" id="v6".*?</section>', source, re.S).group()
    (folder / 'slide.html').write_text(raw + '\n', encoding='utf-8', newline='\n')

comparison = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Axis — slide 7 comparison</title>
<style>
*{box-sizing:border-box}body{margin:0;padding:24px;background:#e9edf2;color:#0f1e3d;font:16px/1.4 Arial,sans-serif}
h1{font-size:22px;margin:0 0 6px}p{margin:0 0 20px;color:#566173}
.compare{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start;min-width:1000px}
h2{font-size:17px;margin:0 0 8px}a{color:#4a3fbf}
.frame{position:relative;width:100%;overflow:hidden;background:white;box-shadow:0 2px 12px #0f1e3d20}
iframe{border:0;display:block;position:absolute;width:1280px;height:720px;transform-origin:top left}
.links{font-size:14px;margin-top:10px}
</style>
<h1>Slide 7 — side-by-side comparison</h1>
<p>Fixed snapshots: main 0f5d8b8 on the left; fahtai efce767 on the right. Scroll horizontally on a narrow screen.</p>
<div class="compare">
<section><h2>Main — footprint and value chain</h2><div class="frame"><iframe title="Main slide 7" src="main/Axis.html"></iframe></div><p class="links"><a href="main/Axis.html">Open full size</a> · <a href="main/slide.html">Source fragment</a></p></section>
<section><h2>Fahtai — actions and decision conditions</h2><div class="frame"><iframe title="Revised slide 7" src="revised/Axis.html"></iframe></div><p class="links"><a href="revised/Axis.html">Open full size</a> · <a href="revised/slide.html">Source fragment</a></p></section>
</div>
<script>
function fit(){document.querySelectorAll('.frame').forEach(f=>{const s=f.clientWidth/1280;f.style.height=720*s+'px';f.querySelector('iframe').style.transform='scale('+s+')';});}
window.addEventListener('resize',fit);fit();
</script></html>'''
(HERE / 'Axis.html').write_text(comparison, encoding='utf-8', newline='\n')
print('Created', HERE / 'Axis.html')
