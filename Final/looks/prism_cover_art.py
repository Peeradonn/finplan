"""The close (slide 14) as an end card: a glass prism in 3D, centred, close to the viewer (16 Nov, Pete: "make the prism
like a main page ... 3d with depth", then "more like ending ... the beam looks weird, like curving ... the prism closer
to us ... more depth ... premium, like a big full stop").

A real triangular prism in 3D, seen in perspective from slightly above with the camera close: glass faces shaded by
their angle to the light, glass thickness (an inner bevel), near edges brighter and thicker than far ones, back edges
faint through the glass, a soft shadow and the prism's reflection on a perspective floor, the rays' colour spilling on
the floor, a vignette. The beam in is level and straight on the page (in screen space) so it never reads as bent.
Same five colours as slide 2 (Profile, Risk, Impact, Select, Monitor, top to bottom).

    python prism_cover_art.py OUT.html [yaw] [pitch]

writes OUT.html (the art alone, 1280 x 720); render it at 2x with headless Chrome, then save as JPEG
(Final/deck/img/prism-cover.jpg) for the deck.
"""
import math
import random
import sys

out = sys.argv[1]
YAW = math.radians(float(sys.argv[2]) if len(sys.argv) > 2 else 26.0)
PITCH = math.radians(float(sys.argv[3]) if len(sys.argv) > 3 else 12.0)

CX, CY = 815, 420          # the prism on the right; the text on the left (Pete, 16 Nov)
D, F = 820.0, 1000.0       # camera close: strong perspective
S = 290.0                  # the triangle's side
TH = S * math.sqrt(3) / 2
L = 360.0                  # the prism's length, into the page
A2, B2, C2 = (0.0, 2 * TH / 3), (-S / 2, -TH / 3), (S / 2, -TH / 3)
FLOOR = -TH / 3
COLOURS = ["#F4B740", "#FF4A57", "#3CC8E6", "#9B7BFF", "#E6E9EE"]   # P R I S M, as slide 2


def rot(p):
    x, y, z = p
    cy, sy = math.cos(YAW), math.sin(YAW)
    x, z = x * cy + z * sy, -x * sy + z * cy
    cp, sp = math.cos(PITCH), math.sin(PITCH)
    y, z = y * cp + z * sp, -y * sp + z * cp
    return x, y, z


def proj(p):
    x, y, z = rot(p)
    k = F / (z + D)
    return CX + x * k, CY - y * k


def depth(p):
    return rot(p)[2]


def pts(ps):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in (proj(p) for p in ps))


def spts(ps):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)


def sub(a, b):
    return tuple(i - j for i, j in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(i * j for i, j in zip(a, b))


def norm(a):
    n = math.sqrt(dot(a, a))
    return tuple(i / n for i in a)


def lerp(a, b, t):
    return tuple(i + (j - i) * t for i, j in zip(a, b))


def mirror(p):
    return (p[0], 2 * FLOOR - p[1], p[2])


fa, fb, fc = [(x, y, -L / 2) for x, y in (A2, B2, C2)]
ba, bb, bc = [(x, y, L / 2) for x, y in (A2, B2, C2)]
FACES = {"front": (fa, fb, fc), "back": (ba, bc, bb), "left": (fa, ba, bb, fb),
         "right": (fa, fc, bc, ba), "bottom": (fb, bb, bc, fc)}
EDGES = [(fa, fb), (fb, fc), (fc, fa), (ba, bb), (bb, bc), (bc, ba), (fa, ba), (fb, bb), (fc, bc)]
CAM = (0.0, 0.0, -D)
LIGHT = norm((-0.45, 0.75, -0.5))
ZN, ZF = min(depth(p) for p in (fa, fb, fc, ba, bb, bc)), max(depth(p) for p in (fa, fb, fc, ba, bb, bc))


def face_info(ps):
    r = [rot(p) for p in ps]
    c = tuple(sum(v[i] for v in r) / len(r) for i in range(3))
    n = norm(cross(sub(r[1], r[0]), sub(r[2], r[0])))
    if dot(n, sub(c, rot((0.0, 0.0, 0.0)))) < 0:
        n = tuple(-i for i in n)
    return n, dot(n, sub(CAM, c)) > 0


def visible_edges(geom=lambda p: p):
    """Edges of a visible face are in front; the rest are seen through the glass."""
    front = set()
    for name, ps in FACES.items():
        if face_info([geom(p) for p in ps])[1]:
            for k in range(len(ps)):
                front.add(frozenset((ps[k], ps[(k + 1) % len(ps)])))
    return [(a, b, frozenset((a, b)) in front) for a, b in EDGES]


def prism_svg(geom=lambda p: p, alpha=1.0):
    back, front = [], []
    for name, ps in FACES.items():
        n, vis = face_info([geom(p) for p in ps])
        lit = max(0.0, dot(n, LIGHT))
        (front if vis else back).append((name, [geom(p) for p in ps], lit))
    behind = [f'<polygon points="{pts(ps)}" fill="#BFD0FF" fill-opacity="{0.04 + 0.06 * lit:.3f}"/>' for _, ps, lit in back]
    ahead = [f'<polygon points="{pts(ps)}" fill="url(#sheen-{name})" fill-opacity="{0.6 + 0.6 * lit:.3f}"/>' for name, ps, lit in front]
    lines_b, lines_f = [], []
    for a, b, vis in visible_edges(geom):
        a, b = geom(a), geom(b)
        t = min(1.0, max(0.0, ((depth(a) + depth(b)) / 2 - ZN) / (ZF - ZN)))      # 0 near, 1 far
        p, q = proj(a), proj(b)
        if vis:
            lines_f.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#FFFFFF" '
                           f'stroke-opacity="{0.95 - 0.45 * t:.2f}" stroke-width="{3.4 - 1.6 * t:.2f}" stroke-linecap="round"/>')
        else:
            lines_b.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#FFFFFF" '
                           f'stroke-opacity=".17" stroke-width="1.3"/>')
    cen = (0.0, 0.0, -L / 2)            # glass thickness: an inner bevel on the front triangle
    inset = [geom((p[0], p[1], p[2] + 6)) for p in (lerp(v, cen, 0.075) for v in (fa, fb, fc))]
    bevel = (f'<polygon points="{pts(inset)}" fill="none" stroke="#DCE6FF" stroke-opacity=".3" stroke-width="1.2" '
             'stroke-linejoin="round"/>')
    return (f'<g opacity="{alpha}">' + "".join(behind) + "".join(lines_b),
            "".join(ahead) + bevel + "".join(lines_f) + "</g>", front)


def sheens(front):
    d = []
    for name, ps, lit in front:
        xs, ys = zip(*(proj(p) for p in ps))
        d.append(f'<linearGradient id="sheen-{name}" gradientUnits="userSpaceOnUse" x1="{min(xs):.0f}" y1="{min(ys):.0f}" '
                 f'x2="{max(xs):.0f}" y2="{max(ys):.0f}"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".30"/>'
                 '<stop offset=".5" stop-color="#DCE6FF" stop-opacity=".07"/><stop offset="1" stop-color="#9FB4FF" stop-opacity=".05"/></linearGradient>')
    return "".join(d)


# ---- the light
ENTRY = lerp((A2[0], A2[1], 0.0), (B2[0], B2[1], 0.0), 0.58)
EXITS = [lerp((A2[0], A2[1], 0.0), (C2[0], C2[1], 0.0), t) for t in (0.40, 0.46, 0.52, 0.58, 0.64)]
ANGLES = [math.radians(a) for a in (17, 7, -3, -13, -23)]   # bent toward the base, as a prism bends light
BEAM_DEG = 15.0                 # the beam in, angled down from the top left (on the page)
DZ = 0.18                       # the rays recede a little: they taper into the distance


def ray_poly(q, a, length=900.0, w0=2.2, w1=13.0, n=16):
    d = norm((math.cos(a), math.sin(a), DZ))
    perp = (-math.sin(a), math.cos(a), 0.0)
    top, bot = [], []
    for k in range(n + 1):
        t = k / n
        c = tuple(qi + di * length * t for qi, di in zip(q, d))
        w = w0 + (w1 - w0) * math.sqrt(t)
        top.append(tuple(ci + pi * w for ci, pi in zip(c, perp)))
        bot.append(tuple(ci - pi * w for ci, pi in zip(c, perp)))
    end = tuple(qi + di * length for qi, di in zip(q, d))
    return pts(top + bot[::-1]), proj(q), proj(end)


defs = ['<radialGradient id="bg" cx="0.64" cy="0.54" r="0.78"><stop offset="0" stop-color="#26346A"/>'
        '<stop offset=".42" stop-color="#111C3C"/><stop offset="1" stop-color="#04070F"/></radialGradient>',
        '<radialGradient id="vig" cx="0.55" cy="0.5" r="0.8"><stop offset=".55" stop-color="#000" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#000" stop-opacity=".62"/></radialGradient>',
        '<filter id="glow" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1680" height="1120">'
        '<feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
        '<filter id="bigglow" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1680" height="1120">'
        '<feGaussianBlur stdDeviation="14" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
        '<filter id="bloom" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1680" height="1120"><feGaussianBlur stdDeviation="28"/></filter>',
        '<filter id="soft" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1680" height="1120"><feGaussianBlur stdDeviation="2.4"/></filter>',
        '<filter id="shadow" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1680" height="1120"><feGaussianBlur stdDeviation="16"/></filter>',
        '<radialGradient id="spot" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/>'
        '<stop offset=".3" stop-color="#FFFFFF" stop-opacity=".4"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>',
        '<radialGradient id="pool" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#A9BBFF" stop-opacity=".26"/>'
        '<stop offset="1" stop-color="#A9BBFF" stop-opacity="0"/></radialGradient>']

g = ['<rect width="1280" height="720" fill="url(#bg)"/>']
HZ = proj((0.0, FLOOR, 1e7))[1]
defs.append(f'<linearGradient id="floorfade" gradientUnits="userSpaceOnUse" x1="0" y1="{HZ:.0f}" x2="0" y2="720">'
            '<stop offset="0" stop-color="#02050C" stop-opacity="0"/><stop offset=".3" stop-color="#02050C" stop-opacity=".3"/>'
            '<stop offset="1" stop-color="#02050C" stop-opacity=".6"/></linearGradient>')
g.append(f'<rect x="0" y="{HZ:.0f}" width="1280" height="{720 - HZ:.0f}" fill="url(#floorfade)"/>')
g.append(f'<rect x="0" y="{HZ - 1:.0f}" width="1280" height="2" fill="#9FB4FF" fill-opacity=".10" filter="url(#soft)"/>')
for x in range(-3000, 3001, 120):
    for k in range(8):
        z0, z1 = -700 + k * 800, -700 + (k + 1) * 800
        if min(depth((x, FLOOR, z0)), depth((x, FLOOR, z1))) + D < 200:
            continue
        a, b = proj((x, FLOOR, z0)), proj((x, FLOOR, z1))
        g.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#8FA6E8" '
                 f'stroke-opacity="{0.075 * (1 - k / 8):.3f}" stroke-width="1"/>')
for z in range(-600, 5801, 120):
    xl, xr = -4000, 4000
    while depth((xl, FLOOR, z)) + D < 200:
        xl += 250
    while depth((xr, FLOOR, z)) + D < 200:
        xr -= 250
    if xr <= xl:
        continue
    a, b = proj((xl, FLOOR, z)), proj((xr, FLOOR, z))
    op = 0.09 * max(0.0, 1 - (z + 600) / 6400)
    g.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#8FA6E8" stroke-opacity="{op:.3f}" stroke-width="1"/>')

# the rays' colour spilling onto the floor beneath them
for q, a, c in zip(EXITS[:4], ANGLES[:4], COLOURS[:4]):
    d = norm((math.cos(a), math.sin(a), DZ))
    path = [(q[0] + d[0] * 700 * t, FLOOR, q[2] + d[2] * 700 * t + 40) for t in (0.0, 0.25, 0.5, 0.75, 1.0)]
    g.append(f'<polyline points="{pts(path)}" fill="none" stroke="{c}" stroke-opacity=".16" stroke-width="34" '
             'stroke-linecap="round" filter="url(#bloom)"/>')
# a soft shadow: the base pushed away from the light
shadow = [(p[0] + 70, FLOOR, p[2] + 90) for p in (fb, fc, bc, bb)]
g.append(f'<polygon points="{pts(shadow)}" fill="#000" fill-opacity=".55" filter="url(#shadow)"/>')
pc = proj((0, FLOOR, 0))
g.append(f'<ellipse cx="{pc[0]:.0f}" cy="{pc[1] + 6:.0f}" rx="330" ry="60" fill="url(#pool)"/>')

# the bloom behind the rays
fan = [EXITS[2]] + [tuple(q + 900 * d for q, d in zip(EXITS[2], norm((math.cos(a), math.sin(a), DZ)))) for a in (ANGLES[0], ANGLES[-1])]
g.append(f'<polygon points="{pts(fan)}" fill="#8F7BFF" fill-opacity=".22" filter="url(#bloom)"/>')

# the reflection
contact = max(proj(p)[1] for p in (fb, fc, bb, bc))
defs.append(f'<linearGradient id="fade" gradientUnits="userSpaceOnUse" x1="0" y1="{contact - 50:.0f}" x2="0" y2="{contact + 200:.0f}">'
            '<stop offset="0" stop-color="#FFFFFF" stop-opacity=".38"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>')
defs.append('<mask id="reflmask" maskUnits="userSpaceOnUse" x="0" y="0" width="1280" height="720">'
            '<rect x="0" y="0" width="1280" height="720" fill="url(#fade)"/></mask>')
rb, rf, _ = prism_svg(mirror, 0.85)
g.append(f'<g mask="url(#reflmask)">{rb}{rf}</g>')

# the beam in: straight on the page, angled down from the top left into the glass (Pete, 16 Nov: "bending towards
# the top left a bit"); straight, never curved, so it reads as light
ex, ey = proj(ENTRY)
BX, BY = -20.0, ey - (ex + 20.0) * math.tan(math.radians(BEAM_DEG))     # where it enters the page, on the left edge
ux, uy = (ex - BX), (ey - BY)
ul = math.hypot(ux, uy)
ux, uy = ux / ul, uy / ul
nx, ny = -uy, ux


def along(t, w):
    return (BX + ux * ul * t + nx * w, BY + uy * ul * t + ny * w)


defs.append(f'<linearGradient id="beam" gradientUnits="userSpaceOnUse" x1="{BX:.0f}" y1="{BY:.0f}" x2="{ex:.0f}" y2="{ey:.0f}">'
            '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".22" stop-color="#FFFFFF" stop-opacity=".85"/>'
            '<stop offset="1" stop-color="#FFFFFF" stop-opacity="1"/></linearGradient>')
g.append(f'<polygon points="{spts([along(0, -10), along(1, -12), along(1, 12), along(0, 10)])}" fill="#C9D6FF" '
         'fill-opacity=".18" filter="url(#bloom)"/>')
g.append(f'<polygon points="{spts([along(0, -2.5), along(1, -5.5), along(1, 5.5), along(0, 2.5)])}" fill="url(#beam)" filter="url(#glow)"/>')
rnd = random.Random(11)
for k in range(10):
    p = along(0.12 + 0.08 * k + rnd.uniform(-0.015, 0.015), rnd.choice((-12, 10, -8, 13)))
    g.append(f'<circle cx="{p[0]:.0f}" cy="{p[1]:.0f}" r="{rnd.choice((1.2, 1.6, 2.0))}" '
             f'fill="#FFFFFF" fill-opacity="{rnd.uniform(.3, .6):.2f}"/>')

pb, pf, front = prism_svg()
defs.append(sheens(front))
g.append(pb)
for q, c in zip(EXITS, COLOURS):
    q2 = proj(q)
    g.append(f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{q2[0]:.1f}" y2="{q2[1]:.1f}" stroke="{c}" stroke-opacity=".9" '
             'stroke-width="3.2" filter="url(#glow)"/>')
q2 = proj(EXITS[2])
g.append(f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{q2[0]:.1f}" y2="{q2[1]:.1f}" stroke="#FFFFFF" stroke-opacity=".65" '
         'stroke-width="6" filter="url(#glow)"/>')
g.append(pf)
r0, r1 = proj(fa), proj(ba)
g.append(f'<line x1="{r0[0]:.1f}" y1="{r0[1]:.1f}" x2="{r1[0]:.1f}" y2="{r1[1]:.1f}" stroke="#FFFFFF" stroke-width="3" '
         'stroke-linecap="round" filter="url(#bigglow)" opacity=".85"/>')
g.append(f'<circle cx="{r0[0]:.0f}" cy="{r0[1]:.0f}" r="22" fill="url(#spot)" opacity=".6"/>')

for i, (q, a, c) in enumerate(zip(EXITS, ANGLES, COLOURS)):
    poly, s0, s1 = ray_poly(q, a)
    t = min(1.0, (1250 - s0[0]) / (s1[0] - s0[0])) if s1[0] > s0[0] else 1.0
    s1 = (s0[0] + (s1[0] - s0[0]) * t, s0[1] + (s1[1] - s0[1]) * t)
    defs.append(f'<linearGradient id="ray{i}" gradientUnits="userSpaceOnUse" x1="{s0[0]:.0f}" y1="{s0[1]:.0f}" '
                f'x2="{s1[0]:.0f}" y2="{s1[1]:.0f}"><stop offset="0" stop-color="{c}"/>'
                f'<stop offset=".5" stop-color="{c}" stop-opacity=".92"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>')
    g.append(f'<polygon points="{poly}" fill="url(#ray{i})" filter="url(#bigglow)"/>')
x, y = proj(EXITS[2])
g.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="16" ry="62" fill="url(#spot)" opacity=".8" transform="rotate(-16 {x:.0f} {y:.0f})"/>')
g.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="30" fill="url(#spot)" opacity=".75"/>')
g.append(f'<line x1="{ex - 60 * ux:.0f}" y1="{ey - 60 * uy:.0f}" x2="{ex + 60 * ux:.0f}" y2="{ey + 60 * uy:.0f}" '
         'stroke="#FFFFFF" stroke-opacity=".5" stroke-width="1.5" filter="url(#soft)"/>')
for k in range(40):
    px, py, r = rnd.uniform(0, 1280), rnd.uniform(0, 600), rnd.choice((0.8, 1.0, 1.3, 1.8, 2.8))
    g.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{r}" fill="#C9D6FF" fill-opacity="{rnd.uniform(.06, .24):.2f}"'
             + (' filter="url(#soft)"' if r > 2 else '') + '/>')
g.append('<rect width="1280" height="720" fill="url(#vig)"/>')

svg = (f'<svg viewBox="0 0 1280 720" width="1280" height="720" xmlns="http://www.w3.org/2000/svg">'
       f'<defs>{"".join(defs)}</defs>{"".join(g)}</svg>')
open(out, "w", encoding="utf-8").write('<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;'
                                       'background:#04070F;overflow:hidden}svg{display:block}</style></head><body>' + svg + '</body></html>')
xs = [proj(p)[0] for p in (fa, fb, fc, ba, bb, bc)]
ys = [proj(p)[1] for p in (fa, fb, fc, ba, bb, bc)]
print("ok", out, "prism box", round(min(xs)), round(min(ys)), round(max(xs)), round(max(ys)), "beam y", round(ey), "beam enters at", round(BX), round(BY))
