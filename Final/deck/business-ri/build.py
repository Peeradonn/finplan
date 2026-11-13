"""Build a standalone business R/I candidate from the Final deck's existing head.

Run from any directory: python Final/deck/business-ri/build.py
The main deck, its order and its timing are untouched. Edit slide.html / slide.css.
"""
from pathlib import Path
import base64
import re

HERE = Path(__file__).resolve().parent
DECK = HERE.parent
head = (DECK / 'src' / '00_head.html').read_text(encoding='utf-8')

def font_data(match):
    font = DECK / match.group(1)
    data = base64.b64encode(font.read_bytes()).decode('ascii')
    return 'url("data:font/ttf;base64,' + data + '")'

head = re.sub(r'url\("(fonts/[^"\)]+)"\)', font_data, head)
css = (HERE / 'slide.css').read_text(encoding='utf-8')
preview = '\nhtml,body{width:1280px;height:720px;overflow:hidden;background:white}.deck{zoom:1;gap:0;padding:0}.slide{box-shadow:none}aside.notes{display:none}\n'
head = head.replace('</style>', css + preview + '</style>')
slide = (HERE / 'slide.html').read_text(encoding='utf-8')
if '{{' in slide or '[[' in slide:
    raise ValueError('Candidate must not contain unresolved placeholders')
qa = '''<script>
document.fonts.ready.then(function () {
  var slide = document.querySelector('.bri-slide'), box = slide.getBoundingClientRect();
  var outside = Array.from(slide.querySelectorAll('p,h2,h3,footer')).filter(function (el) {
    var b = el.getBoundingClientRect();
    return b.left < box.left - 1 || b.right > box.right + 1 || b.top < box.top - 1 || b.bottom > box.bottom + 1;
  }).map(function (el) { return el.textContent.trim(); });
  document.body.setAttribute('data-layout-check', JSON.stringify({
    width: box.width, height: box.height, outside: outside,
    fontLoaded: document.fonts.check('700 20px PJS')
  }));
});
</script>'''
output = head + slide + '\n</main>' + qa + '</body></html>\n'
(HERE / 'Axis.html').write_text(output, encoding='utf-8', newline='\n')
print('Built', HERE / 'Axis.html')
