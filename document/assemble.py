"""
Assemble the 15-page proposal from the page sources, in order.
Usage:  python assemble.py          -> proposal.html, numbers filled in (then: python render.py proposal.html)

Sources (edit these, never proposal.html):
  template-v2.html      cover (1), executive summary (2)
  pages-03-09.html      §2 (3), §4 (6), §5 (7), §5-§6 (8), §7 (9)
  section-mock-v3.html  §3 retirement (4-5)
  pages-10-15.html      §8 (10), §9 (11), §9-§10 (12), §11 (13), personal statement (14), appendix (15)
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SECTION = re.compile(r'<section class="page[^"]*">.*?</section>', re.S)
STYLE = re.compile(r"<style>(.*?)</style>", re.S)

def pages(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        html = f.read()
    return SECTION.findall(html), STYLE.findall(html)

tpl, s1 = pages("template-v2.html")
p39, s2 = pages("pages-03-09.html")
p45, s3 = pages("section-mock-v3.html")
p1015, s4 = pages("pages-10-15.html")
order = tpl[:2] + p39[:1] + p45 + p39[1:] + p1015
assert len(order) == 15, f"expected 15 pages, got {len(order)}"

# page-local styles from every source, each rule once
rules = []
for block in s1 + s2 + s3 + s4:
    for line in block.strip().splitlines():
        line = line.strip()
        if line and not line.startswith("/*") and line not in rules:
            rules.append(line)

with open(os.path.join(HERE, "section-mock-v3.html"), encoding="utf-8") as f:
    script = re.search(r"<script>.*?</script>", f.read(), re.S).group(0)

html = (
    '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    "<title>Built to Last: A Financial Plan for the Wong Family</title>\n"
    '<meta name="author" content="Team Axis">\n'
    '<link rel="stylesheet" href="styles-v2.css">\n<style>\n  ' + "\n  ".join(rules) + "\n</style>\n</head>\n<body>\n\n"
    + "\n\n".join(order) + "\n\n" + script + "\n</body>\n</html>\n"
)
# write the model's numbers in, so proposal.html reads correctly when opened directly in a browser
import fill
html = fill.fill_text(html)
with open(os.path.join(HERE, "proposal.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"proposal.html: {len(order)} pages, {len(rules)} page-local style rules, numbers filled from the model")
