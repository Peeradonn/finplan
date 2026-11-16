"""The close (slide 14) as a cover page: a glass prism in 3D, the hero of the page (16 Nov, Pete: "make the prism like
a main page ... looks like we're looking at it in 3d with depth").

A real triangular prism in 3D, seen in perspective from slightly above: glass faces shaded by their angle to the
light, back edges seen faintly through the glass, a perspective floor with its reflection, one white beam in through
the left face and PRISM's five coloured rays out of the right face as ribbons that come toward the viewer.
Same five colours as slide 2 (Profile, Risk, Impact, Select, Monitor, top to bottom).

    python prism_cover_art.py OUT.html [yaw_degrees] [pitch_degrees]

writes OUT.html (the art alone, 1280 x 720); render it at 2x to Final/deck/img/prism-cover.png with headless Chrome.
"""
import math
import random
import sys

out = sys.argv[1]
YAW = math.radians(float(sys.argv[2]) if len(sys.argv) > 2 else 28.0)
PITCH = math.radians(float(sys.argv[3]) if len(sys.argv) > 3 else 13.0)

W, HGT = 1280, 720
CX, CY = 735, 405          # where the prism's centre lands on the page
D = F = 1500.0             # camera distance and focal length: a gentle perspective
S = 345.0                  # the triangle's side
TH = S * math.sqrt(3) / 2
L = 440.0                  # the prism's length, into the page
A2, B2, C2 = (0.0, 2 * TH / 3), (-S / 2, -TH / 3), (S / 2, -TH / 3)
FLOOR = -TH / 3
COLOURS = ["#F4B740", "#FF4A57", "#3CC8E6", "#9B7BFF", "#E6E9EE"]   # P R I S M, as slide 2


def rot(p):
    x, y, z = p
    cy, sy = math.cos(YAW), math.sin(YAW)
    x, z = x * cy + z * sy, -x * sy + z * cy
    cp, sp = math.cos(PITCH), math.sin(PITCH)
    y, z = y * cp + z * sp, -y * sp + z * cp        # from above: far points rise, the top comes nearer
    return x, y, z


def proj(p):
    x, y, z = rot(p)
    k = F / (z + D)
    return CX + x * k, CY - y * k


def pts(ps):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in (proj(p) for p in ps))


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


# ---- the prism: front triangle at z = -L/2 (nearer), back at +L/2
fa, fb, fc = [(x, y, -L / 2) for x, y in (A2, B2, C2)]
ba, bb, bc = [(x, y, L / 2) for x, y in (A2, B2, C2)]
FACES = {  # name: corners (outward order irrelevant: normals are oriented from the centre)
    "front": (fa, fb, fc), "back": (ba, bc, bb),
    "left": (fa, ba, bb, fb), "right": (fa, fc, bc, ba), "bottom": (fb, bb, bc, fc),
}
CAM = (0.0, 0.0, -D)
LIGHT = norm((-0.45, 0.75, -0.5))          # from upper left, in front


def face_info(ps):
    r = [rot(p) for p in ps]
    c = tuple(sum(v[i] for v in r) / len(r) for i in range(3))
    n = norm(cross(sub(r[1], r[0]), sub(r[2], r[0])))
    centre = rot((0.0, 0.0, 0.0))
    if dot(n, sub(c, centre)) < 0:
        n = tuple(-i for i in n)
    return n, c, dot(n, sub(CAM, c)) > 0


def prism_svg(geom=lambda p: p, alpha=1.0, edges=True):
    """Glass: back faces dim, front faces with a sheen; back edges faint, front edges bright."""
    back, front = [], []
    for name, ps in FACES.items():
        n, c, vis = face_info([geom(p) for p in ps])
        lit = max(0.0, dot(n, LIGHT))
        (front if vis else back).append((name, [geom(p) for p in ps], lit))
    g = []
    for name, ps, lit in back:
        g.append(f'<polygon points="{pts(ps)}" fill="#BFD0FF" fill-opacity="{0.03 + 0.05 * lit:.3f}"/>')
        if edges:
            g.append(f'<polygon points="{pts(ps)}" fill="none" stroke="#FFFFFF" stroke-opacity=".16" stroke-width="1.4" stroke-linejoin="round"/>')
    inner = len(g)
    for name, ps, lit in front:
        g.append(f'<polygon points="{pts(ps)}" fill="url(#sheen-{name})" fill-opacity="{0.55 + 0.6 * lit:.3f}"/>')
    if edges:
        for name, ps, lit in front:
            g.append(f'<polygon points="{pts(ps)}" fill="none" stroke="#FFFFFF" stroke-opacity="{0.55 + 0.35 * lit:.2f}" '
                     f'stroke-width="2.4" stroke-linejoin="round"/>')
    return f'<g opacity="{alpha}">' + "".join(g[:inner]), "".join(g[inner:]) + "</g>", front


def sheens(front):
    """A diagonal sheen across each front face, brightest at the upper-left edge."""
    d = []
    for name, ps, lit in front:
        xs, ys = zip(*(proj(p) for p in ps))
        d.append(f'<linearGradient id="sheen-{name}" gradientUnits="userSpaceOnUse" x1="{min(xs):.0f}" y1="{min(ys):.0f}" '
                 f'x2="{max(xs):.0f}" y2="{max(ys):.0f}"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".30"/>'
                 '<stop offset=".45" stop-color="#DCE6FF" stop-opacity=".08"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".02"/></linearGradient>')
    return "".join(d)


# ---- the light: in through the left face, out of the right face
ENTRY = lerp((A2[0], A2[1], 0.0), (B2[0], B2[1], 0.0), 0.60)
EXITS = [lerp((A2[0], A2[1], 0.0), (C2[0], C2[1], 0.0), t) for t in (0.40, 0.46, 0.52, 0.58, 0.64)]
ANGLES = [math.radians(a) for a in (22, 12, 2, -8, -18)]
DZ = -0.10                          # the rays come toward the viewer
IN_DIR = norm((1.0, 0.16, 0.06))
IN_FROM = tuple(e - 740 * d for e, d in zip(ENTRY, IN_DIR))


def ray_poly(q, a, geom=lambda p: p, length=620.0, w0=3.0, w1=19.0, n=14):
    d = norm((math.cos(a), math.sin(a), DZ))
    perp = (-math.sin(a), math.cos(a), 0.0)
    top, bot = [], []
    for k in range(n + 1):
        t = k / n
        c = tuple(qi + di * length * t for qi, di in zip(q, d))
        w = w0 + (w1 - w0) * t
        top.append(geom(tuple(ci + pi * w for ci, pi in zip(c, perp))))
        bot.append(geom(tuple(ci - pi * w for ci, pi in zip(c, perp))))
    return pts(top + bot[::-1]), proj(geom(q)), proj(geom(tuple(qi + di * length for qi, di in zip(q, d))))


defs = ['<radialGradient id="bg" cx="0.58" cy="0.52" r="0.8"><stop offset="0" stop-color="#22305A"/>'
        '<stop offset=".45" stop-color="#101A36"/><stop offset="1" stop-color="#050913"/></radialGradient>',
        '<filter id="glow" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1480" height="920">'
        '<feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
        '<filter id="bloom" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1480" height="920"><feGaussianBlur stdDeviation="26"/></filter>',
        '<filter id="soft" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1480" height="920"><feGaussianBlur stdDeviation="2.2"/></filter>',
        '<radialGradient id="spot" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/>'
        '<stop offset=".3" stop-color="#FFFFFF" stop-opacity=".4"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>',
        '<radialGradient id="pool" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#9FB4FF" stop-opacity=".22"/>'
        '<stop offset="1" stop-color="#9FB4FF" stop-opacity="0"/></radialGradient>']

g = ['<rect width="1280" height="720" fill="url(#bg)"/>']
# the floor: a dark plane to the horizon, a perspective grid fading with distance
fl = [(-6000, FLOOR, -700), (6000, FLOOR, -700), (6000, FLOOR, 30000), (-6000, FLOOR, 30000)]
HZ = proj((0.0, FLOOR, 1e7))[1]
defs.append(f'<linearGradient id="floorfade" gradientUnits="userSpaceOnUse" x1="0" y1="{HZ:.0f}" x2="0" y2="720">'
            '<stop offset="0" stop-color="#02050C" stop-opacity="0"/><stop offset=".35" stop-color="#02050C" stop-opacity=".25"/>'
            '<stop offset="1" stop-color="#02050C" stop-opacity=".55"/></linearGradient>')
g.append(f'<polygon points="{pts(fl)}" fill="url(#floorfade)"/>')
for x in range(-2400, 3601, 150):
    for k in range(6):          # each line fades with distance, in steps
        z0, z1 = -700 + k * 980, -700 + (k + 1) * 980
        a, b = proj((x, FLOOR, z0)), proj((x, FLOOR, z1))
        g.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#8FA6E8" '
                 f'stroke-opacity="{0.08 * (1 - k / 6):.3f}" stroke-width="1"/>')
for z in range(-600, 5201, 150):
    a, b = proj((-2600, FLOOR, z)), proj((3800, FLOOR, z))
    op = 0.10 * max(0.0, 1 - (z + 600) / 5800)
    g.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#8FA6E8" stroke-opacity="{op:.3f}" stroke-width="1"/>')

# the bloom behind the rays, and a pool of light on the floor under the glass
fan = [EXITS[2]] + [tuple(q + 1100 * d for q, d in zip(EXITS[2], norm((math.cos(a), math.sin(a), DZ)))) for a in (ANGLES[0], ANGLES[-1])]
g.append(f'<polygon points="{pts(fan)}" fill="#8F7BFF" fill-opacity=".20" filter="url(#bloom)"/>')
pc = proj((40, FLOOR, 0))
g.append(f'<ellipse cx="{pc[0]:.0f}" cy="{pc[1] + 8:.0f}" rx="380" ry="70" fill="url(#pool)"/>')

# the reflection: the prism and the rays mirrored in the floor, fading down the page
contact = max(proj(p)[1] for p in (fb, fc, bb, bc))
defs.append('<linearGradient id="fade" gradientUnits="userSpaceOnUse" x1="0" y1="%.0f" x2="0" y2="%.0f">'
            '<stop offset="0" stop-color="#FFFFFF" stop-opacity=".42"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            % (contact - 60, contact + 220))
defs.append(f'<mask id="reflmask" maskUnits="userSpaceOnUse" x="0" y="0" width="1280" height="720">'
            f'<rect x="0" y="0" width="1280" height="720" fill="url(#fade)"/></mask>')
rb, rf, rfront = prism_svg(mirror, 0.8)
rays_m = "".join(f'<polygon points="{ray_poly(q, a, mirror)[0]}" fill="{c}" fill-opacity=".16" filter="url(#bloom)"/>'
                 for q, a, c in zip(EXITS, ANGLES, COLOURS))
g.append(f'<g mask="url(#reflmask)">{rb}{rays_m}{rf}</g>')

# the beam in
a0, a1 = proj(IN_FROM), proj(ENTRY)
g.append(f'<line x1="{a0[0]:.1f}" y1="{a0[1]:.1f}" x2="{a1[0]:.1f}" y2="{a1[1]:.1f}" stroke="#FFFFFF" stroke-width="11" '
         'stroke-linecap="round" filter="url(#glow)"/>')
rnd = random.Random(7)
for k in range(9):       # dust in the beam
    p = proj(lerp(IN_FROM, ENTRY, 0.25 + 0.7 * k / 9))
    g.append(f'<circle cx="{p[0]:.1f}" cy="{p[1] + rnd.choice((-9, 8, -6, 10)):.1f}" r="1.5" fill="#FFFFFF" fill-opacity=".5"/>')

pb, pf, front = prism_svg()
defs.append(sheens(front))
g.append(pb)
# inside the glass: the white beam spreads into a narrow fan
for q, c in zip(EXITS, COLOURS):
    e0, e1 = proj(ENTRY), proj(q)
    g.append(f'<line x1="{e0[0]:.1f}" y1="{e0[1]:.1f}" x2="{e1[0]:.1f}" y2="{e1[1]:.1f}" stroke="{c}" stroke-opacity=".9" '
             'stroke-width="3.5" filter="url(#glow)"/>')
e0, e1 = proj(ENTRY), proj(EXITS[2])
g.append(f'<line x1="{e0[0]:.1f}" y1="{e0[1]:.1f}" x2="{e1[0]:.1f}" y2="{e1[1]:.1f}" stroke="#FFFFFF" stroke-opacity=".7" '
         'stroke-width="6" filter="url(#glow)"/>')
g.append(pf)
r0, r1 = proj(fa), proj(ba)
g.append(f'<line x1="{r0[0]:.1f}" y1="{r0[1]:.1f}" x2="{r1[0]:.1f}" y2="{r1[1]:.1f}" stroke="#FFFFFF" stroke-width="3.2" '
         'stroke-linecap="round" filter="url(#glow)" opacity=".9"/>')
g.append(f'<circle cx="{r0[0]:.0f}" cy="{r0[1]:.0f}" r="16" fill="url(#spot)" opacity=".55"/>')
# the rays out, toward the viewer
for i, (q, a, c) in enumerate(zip(EXITS, ANGLES, COLOURS)):
    poly, s0, s1 = ray_poly(q, a)
    t = min(1.0, (1240 - s0[0]) / (s1[0] - s0[0]))          # fade out by the page's right edge
    s1 = (s0[0] + (s1[0] - s0[0]) * t, s0[1] + (s1[1] - s0[1]) * t)
    defs.append(f'<linearGradient id="ray{i}" gradientUnits="userSpaceOnUse" x1="{s0[0]:.0f}" y1="{s0[1]:.0f}" '
                f'x2="{s1[0]:.0f}" y2="{s1[1]:.0f}"><stop offset="0" stop-color="{c}"/>'
                f'<stop offset=".38" stop-color="{c}" stop-opacity=".95"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>')
    g.append(f'<polygon points="{poly}" fill="url(#ray{i})" filter="url(#glow)"/>')
x, y = proj(EXITS[2])
g.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="18" ry="70" fill="url(#spot)" opacity=".8" transform="rotate(-18 {x:.0f} {y:.0f})"/>')
x, y = proj(ENTRY)
g.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="26" fill="url(#spot)" opacity=".7"/>')
# a little depth in the air: soft motes, larger and blurrier nearer the viewer
for k in range(46):
    px, py, r = rnd.uniform(0, 1280), rnd.uniform(0, 560), rnd.choice((0.8, 1.0, 1.3, 1.8, 2.6))
    g.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{r}" fill="#C9D6FF" fill-opacity="{rnd.uniform(.08, .28):.2f}"'
             + (' filter="url(#soft)"' if r > 2 else '') + '/>')

svg = (f'<svg viewBox="0 0 1280 720" width="1280" height="720" xmlns="http://www.w3.org/2000/svg">'
       f'<defs>{"".join(defs)}</defs>{"".join(g)}</svg>')
open(out, "w", encoding="utf-8").write('<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;'
                                       'background:#050913;overflow:hidden}svg{display:block}</style></head><body>' + svg + '</body></html>')
print("ok", out, "beam starts at", tuple(round(v) for v in proj(IN_FROM)), "ray ends",
      [tuple(round(v) for v in ray_poly(q, a)[2]) for q, a in zip(EXITS, ANGLES)])
