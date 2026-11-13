"""Slide 2 as the framework's introduction page: a dark stage, a large glass prism, five coloured rays (11 Nov)."""
import sys

out = sys.argv[1]
FONT = "../deck/fonts/"   # relative to Final/looks/
DY = -64                # 13 Nov (Pete): the stage moves up to leave room for the price tag, bottom right
A, B, C = (420, 240 + DY), (285, 620 + DY), (555, 620 + DY)
D = (72, -42)
A2, B2, C2 = [(x + D[0], y + D[1]) for x, y in (A, B, C)]
E = (352, 430 + DY)     # the beam enters the front face
X = (536, 444 + DY)     # the middle of the exit, on the right face
EXITS = [(x, y + DY) for x, y in ((522, 405), (529, 425), (536, 445), (543, 465), (550, 485))]   # where each colour leaves the glass
FLOOR = 620 + DY
RX = 724                # where the rays reach the letters
ROWS = [  # letter, colour, name, question, the usual way, ours
    ("P", "#F4B740", "Profile", "who decides, within what limits?", "ask an ESG preference",
     "limits and a values budget, set before anything is priced"),
    ("R", "#FF4A57", "Risk", "what does climate do to their money?", "rate each product",
     "the whole household in one storm: a pre\u2011mortem"),
    ("I", "#3CC8E6", "Impact", "what does their money do to the world?", "report a footprint",
     "footprint or effect: no impact claimed for shares"),
    ("S", "#9B7BFF", "Select", "what does each option do, both ways?", "hit a 25% target",
     "the share is an output; every missing price a decision"),
    ("M", "#E6E9EE", "Monitor", "how do we know it's still true?", "review once a year",
     "decisions with expiry dates and triggers"),
]
YS = [100, 192, 284, 376, 468]   # 13 Nov: rows 92px apart (were 120 from 150), ending above the tag
pt = lambda *ps: " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)

defs = [
    '<radialGradient id="bg" cx="0.33" cy="0.6" r="0.85"><stop offset="0" stop-color="#2E2326"/>'
    '<stop offset=".55" stop-color="#191415"/><stop offset="1" stop-color="#0D0A0B"/></radialGradient>',
    '<linearGradient id="front" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".26"/>'
    '<stop offset=".5" stop-color="#FFFFFF" stop-opacity=".09"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".03"/></linearGradient>',
    '<linearGradient id="side" x1="0" y1="0" x2="1" y2="0.3"><stop offset="0" stop-color="#C9D6FF" stop-opacity=".16"/>'
    '<stop offset="1" stop-color="#FFFFFF" stop-opacity=".03"/></linearGradient>',
    f'<linearGradient id="glint" gradientUnits="userSpaceOnUse" x1="417" y1="{265 + DY}" x2="294" y2="{607 + DY}">'
    '<stop offset="0" stop-color="#FFFFFF" stop-opacity=".8"/><stop offset=".3" stop-color="#FFFFFF" stop-opacity=".22"/>'
    '<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>',
    '<radialGradient id="floorglow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".16"/>'
    '<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>',
    '<radialGradient id="spot" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".9"/>'
    '<stop offset=".35" stop-color="#FFFFFF" stop-opacity=".35"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>',
    '<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".55"/>'
    '<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>',
    f'<mask id="reflmask" maskUnits="userSpaceOnUse" x="0" y="{FLOOR}" width="1280" height="{720 - FLOOR}">'
    f'<rect x="0" y="{FLOOR}" width="1280" height="{720 - FLOOR}" fill="url(#fade)"/></mask>',
    '<filter id="glow" filterUnits="userSpaceOnUse" x="-50" y="-50" width="1380" height="820">'
    '<feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
    '<filter id="haze" filterUnits="userSpaceOnUse" x="-50" y="-50" width="1380" height="820"><feGaussianBlur stdDeviation="22"/></filter>',
    '<linearGradient id="fan" x1="0" y1="0" x2="0" y2="1">'
    + "".join(f'<stop offset="{i / 4:.2f}" stop-color="{r[1]}"/>' for i, r in enumerate(ROWS)) + '</linearGradient>',
]
for i, (r, y, ex) in enumerate(zip(ROWS, YS, EXITS)):
    defs.append(f'<linearGradient id="in{i}" gradientUnits="userSpaceOnUse" x1="{E[0]}" y1="{E[1]}" x2="{ex[0]}" y2="{ex[1]}">'
                f'<stop offset="0" stop-color="#FFFFFF" stop-opacity=".85"/><stop offset=".45" stop-color="#FFFFFF" stop-opacity=".55"/>'
                f'<stop offset="1" stop-color="{r[1]}" stop-opacity=".95"/></linearGradient>')
    defs.append(f'<linearGradient id="ray{i}" gradientUnits="userSpaceOnUse" x1="{ex[0]}" y1="{ex[1]}" x2="{RX}" y2="{y}">'
                f'<stop offset="0" stop-color="{r[1]}" stop-opacity="1"/><stop offset="1" stop-color="{r[1]}" stop-opacity=".78"/></linearGradient>')
defs.append(f'<linearGradient id="core" gradientUnits="userSpaceOnUse" x1="{E[0]}" y1="{E[1]}" x2="{X[0]}" y2="{X[1]}">'
            '<stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".6" stop-color="#FFFFFF" stop-opacity=".25"/>'
            '<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>')


def prism(alpha=1.0):
    return (f'<g opacity="{alpha}">'
            f'<g stroke="#FFFFFF" stroke-opacity=".14" stroke-width="1.5" fill="none"><polyline points="{pt(A2, B2, C2)}"/>'
            f'<line x1="{B[0]}" y1="{B[1]}" x2="{B2[0]}" y2="{B2[1]}"/></g>'
            f'<polygon points="{pt(A, C, C2, A2)}" fill="url(#side)"/>'
            f'<polygon points="{pt(A, B, C)}" fill="url(#front)"/>'
            f'<polygon points="{pt((414, 268 + DY), (418, 265 + DY), (296, 606 + DY), (292, 607 + DY))}" fill="url(#glint)"/>'
            f'<g fill="none" stroke="#FFFFFF" stroke-linejoin="round"><polygon points="{pt(A, B, C)}" stroke-width="2.6" stroke-opacity=".9"/>'
            f'<polyline points="{pt(A, A2, C2, C)}" stroke-width="2" stroke-opacity=".55"/></g></g>')


g = [f'<defs>{"".join(defs)}</defs>', '<rect width="1280" height="720" fill="url(#bg)"/>']
# the stage floor: a horizon and a few receding lines, very faint
g.append(f'<rect x="0" y="{FLOOR}" width="1280" height="{720 - FLOOR}" fill="#000" fill-opacity=".22"/>')
g.append(f'<line x1="0" y1="{FLOOR}" x2="1280" y2="{FLOOR}" stroke="#FFFFFF" stroke-opacity=".10"/>')
for k in range(-6, 9):
    g.append(f'<line x1="{420 + k * 40}" y1="{FLOOR}" x2="{420 + k * 150}" y2="720" stroke="#FFFFFF" stroke-opacity=".035"/>')
for yy in (FLOOR + 12, FLOOR + 30, FLOOR + 56, FLOOR + 92):
    g.append(f'<line x1="0" y1="{yy}" x2="1280" y2="{yy}" stroke="#FFFFFF" stroke-opacity=".03"/>')
g.append(f'<ellipse cx="430" cy="{FLOOR + 4}" rx="300" ry="30" fill="url(#floorglow)"/>')
# the fan of light behind the rays
g.append(f'<polygon points="{pt(X, (RX + 30, YS[0] - 40), (RX + 30, YS[-1] + 40))}" fill="url(#fan)" fill-opacity=".16" filter="url(#haze)"/>')
# the reflection on the floor
g.append(f'<g mask="url(#reflmask)"><g transform="translate(0,{2 * FLOOR}) scale(1,-1)">{prism(.75)}</g></g>')
# the beam in, from the label
g.append(f'<line x1="160" y1="{E[1]}" x2="{E[0]}" y2="{E[1]}" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" filter="url(#glow)"/>')
for k, xx in enumerate(range(185, 345, 23)):
    g.append(f'<circle cx="{xx}" cy="{E[1] + (7 if k % 2 else -8)}" r="1.4" fill="#FFFFFF" fill-opacity=".5"/>')
g.append(prism())
# inside the glass: the white beam fades as it spreads into a narrow coloured fan
g.append(f'<polygon points="{pt((E[0], E[1] - 5), (X[0], X[1] - 3), (X[0], X[1] + 3), (E[0], E[1] + 5))}" fill="url(#core)" filter="url(#glow)"/>')
for i, ex in enumerate(EXITS):
    g.append(f'<polygon points="{pt((E[0], E[1] - 2.5), (ex[0], ex[1] - 3.5), (ex[0], ex[1] + 3.5), (E[0], E[1] + 2.5))}" '
             f'fill="url(#in{i})" filter="url(#glow)"/>')
# out of the glass: each colour from its own point on the face
for i, (y, ex) in enumerate(zip(YS, EXITS)):
    w = 20
    g.append(f'<polygon points="{pt((ex[0], ex[1] - 3.5), (RX, y - w / 2), (RX, y + w / 2), (ex[0], ex[1] + 3.5))}" '
             f'fill="url(#ray{i})" filter="url(#glow)"/>')
g.append(f'<ellipse cx="{X[0]}" cy="{X[1]}" rx="15" ry="58" fill="url(#spot)" opacity=".75" transform="rotate(-20 {X[0]} {X[1]})"/>')
svg = f'<svg viewBox="0 0 1280 720" width="1280" height="720" style="position:absolute;left:0;top:0">{"".join(g)}</svg>'

rows = "".join(
    f'<div class="row" style="top:{y - 46}px"><p class="L" style="color:{c}">{L}</p><div>'
    f'<b>{n} <span>· {q}</span></b><em><i>{u}</i>{o}</em></div></div>'
    for (L, c, n, q, u, o), y in zip(ROWS, YS))

html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>PRISM intro</title>
<style>
@font-face{{font-family:"PJS";src:url("{FONT}PlusJakartaSans-Regular.ttf");font-weight:400}}
@font-face{{font-family:"PJS";src:url("{FONT}PlusJakartaSans-Medium.ttf");font-weight:500}}
@font-face{{font-family:"PJS";src:url("{FONT}PlusJakartaSans-SemiBold.ttf");font-weight:600}}
@font-face{{font-family:"PJS";src:url("{FONT}PlusJakartaSans-Bold.ttf");font-weight:700}}
@font-face{{font-family:"PJS";src:url("{FONT}PlusJakartaSans-ExtraBold.ttf");font-weight:800}}
*{{box-sizing:border-box}} html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{margin:0;background:#E2E2DF}} p{{margin:0}}
.deck{{display:flex;flex-direction:column;align-items:center;padding:28px 0}}
.slide{{position:relative;width:1280px;height:720px;overflow:hidden;color:#fff;font:400 17px/1.4 "PJS",Arial,sans-serif;background:#120E0F}}
@page{{size:1280px 720px;margin:0}} @media print{{body{{background:#fff}}.deck{{padding:0;display:block}}}}
.kick{{position:absolute;left:48px;top:40px;font:700 15px/1 "PJS";color:#FF6B75;letter-spacing:.4px}}
.word{{position:absolute;left:44px;top:60px;font:800 92px/1 "PJS";letter-spacing:10px;color:#fff}}
.sub{{position:absolute;left:48px;top:162px;width:360px;font:600 24px/1.25 "PJS";color:#fff}}
.sub2{{position:absolute;left:48px;top:226px;width:300px;font:500 16px/1.4 "PJS";color:#B9ACAF}}
.chip{{position:absolute;left:48px;top:{E[1] - 21}px;background:#3F9A55;color:#fff;font:800 18px/1 "PJS";padding:12px 16px;border-radius:22px;
  white-space:nowrap;box-shadow:0 0 22px rgba(63,154,85,.45)}}
.under{{position:absolute;left:48px;top:{E[1] + 34}px;font:600 15px/1.3 "PJS";color:#B9ACAF}}
.row{{position:absolute;left:{RX + 14}px;right:34px;height:92px;display:flex;gap:16px;align-items:flex-start}}
.L{{font:800 46px/0.95 "PJS";width:42px;flex:none;text-shadow:0 0 18px currentColor}}
.row b{{display:block;font:700 19px/1.25 "PJS";color:#fff;white-space:nowrap}}
.row b span{{font-weight:500;color:#C4B8BB}}
.row em{{display:block;font:600 16px/1.35 "PJS";font-style:normal;margin-top:5px;color:#fff}}
.row em i{{font-style:normal;color:#A99EA1;text-decoration:line-through;font-weight:500;margin-right:6px}}
.std{{position:absolute;left:48px;bottom:22px;width:440px;font:500 13.5px/1.4 "PJS";color:#9C9093}}
.pg{{position:absolute;right:40px;bottom:22px;font:700 13px "PJS";color:#9C9093}}
</style></head><body><main class="deck">
<section class="slide">
{svg}
<p class="kick">How we think</p>
<p class="word">PRISM</p>
<p class="sub">Look both ways.</p>
<p class="sub2">A label gives one word. PRISM splits it into what's really there.</p>
<span class="chip">ESG ✓</span><p class="under">one word on a label</p>
{rows}
<p class="std">Built on double materiality (the EU requires it of companies), applied to a family's whole balance sheet</p>
<p class="pg">2</p>
</section></main></body></html>'''
open(out, "w", encoding="utf-8").write(html)
# the art alone (no words), for the deck: render at 2x to Final/deck/img/prism-stage.png (13 Nov)
art = ('<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#120E0F}'
       'svg{display:block}</style></head><body>' + svg.replace('style="position:absolute;left:0;top:0"', "") + "</body></html>")
open(out.replace(".html", "-art.html"), "w", encoding="utf-8").write(art)
print("ok")
