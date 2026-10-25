"""Slide 13's map (Pete, 24 Oct: the Connect slide was bland; a 3D map of the Greater Bay Area). Real boundaries,
drawn as raised slabs on a tilted plane, in the deck's palette: the nine mainland cities in rose, Hong Kong and Macao in
wine and raised higher (the side the Wongs and we stand on), the land around them pale.

Data: geoBoundaries, gbHumanitarian CHN ADM2 (prefecture-level, with the Hong Kong and Macao SARs), simplified,
release 9469f09, CC BY 3.0 IGO (source: OCHA / HDX); the credit is in slide 13's footer.
Run: .venv/Scripts/python.exe -I round2/gba_map.py geoBoundaries-CHN-ADM2_simplified.geojson round2/img/gba_map.svg
It writes the map as a standalone SVG (its own gradients and arrowheads) and prints the anchor points, as shares of the
drawing, for the labels slide 13 lays over it.
To change only the two flows (no boundary file needed): .venv/Scripts/python.exe -I round2/gba_map.py --flows round2/img/gba_map.svg"""
import json
import math
import sys

BOX = (111.15, 21.4, 115.65, 24.5)             # lon/lat window around the nine cities
GBA = ["Guangzhou", "Shenzhen", "Zhuhai", "Foshan", "Huizhou", "Dongguan", "Zhongshan", "Jiangmen", "Zhaoqing"]
SAR = {"Hong Kong Special Administrative Region": "hk", "Macao Special Administrative Region": "mo"}
W, H = 640, 330                                 # the drawing, in slide pixels
SQ, PERSP = 0.58, 0.16                          # the tilt (north squashed) and the perspective (north narrower)


def clip(poly, box):
    """Sutherland-Hodgman: a polygon (list of (lon, lat)) clipped to an axis-aligned box."""
    x0, y0, x1, y1 = box
    edges = [(lambda p: p[0] >= x0, lambda a, b: (x0, a[1] + (b[1] - a[1]) * (x0 - a[0]) / (b[0] - a[0]))),
             (lambda p: p[0] <= x1, lambda a, b: (x1, a[1] + (b[1] - a[1]) * (x1 - a[0]) / (b[0] - a[0]))),
             (lambda p: p[1] >= y0, lambda a, b: (a[0] + (b[0] - a[0]) * (y0 - a[1]) / (b[1] - a[1]), y0)),
             (lambda p: p[1] <= y1, lambda a, b: (a[0] + (b[0] - a[0]) * (y1 - a[1]) / (b[1] - a[1]), y1))]
    out = poly
    for inside, cut in edges:
        if not out:
            break
        src, out = out, []
        for i, p in enumerate(src):
            q = src[i - 1]
            if inside(p):
                if not inside(q):
                    out.append(cut(q, p))
                out.append(p)
            elif inside(q):
                out.append(cut(q, p))
    return out


def rings(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"][0]]
    if geom["type"] == "MultiPolygon":
        return [p[0] for p in geom["coordinates"]]
    return []


lat0 = (BOX[1] + BOX[3]) / 2
kx = math.cos(math.radians(lat0))
span_x, span_y = (BOX[2] - BOX[0]) * kx, BOX[3] - BOX[1]
scale = min(W / span_x, H / (span_y * SQ)) * 0.98


def proj(lon, lat):
    """lon/lat to the tilted plane: north is squashed and drawn narrower, as if seen from the south and above."""
    x = (lon - BOX[0]) * kx * scale
    y = (BOX[3] - lat) * scale * SQ                  # 0 at the north edge
    t = y / (span_y * scale * SQ)                    # 0 north .. 1 south
    cx = span_x * scale / 2
    x = cx + (x - cx) * (1 - PERSP + PERSP * t)
    return x + (W - span_x * scale) / 2, y + (H - span_y * scale * SQ) / 2


def path(ring, dy=0.0):
    pts, last = [], None
    for lon, lat in ring:
        x, y = proj(lon, lat)
        if last and abs(x - last[0]) < 1.6 and abs(y - last[1]) < 1.6:
            continue
        pts.append((x, y + dy))
        last = (x, y)
    if len(pts) < 3:
        return ""
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"


def slab(rs, depth, side, top, stroke, sw):
    """A raised slab: the side wall as copies stepped down every 2.5 px, then the top face."""
    o, d = [], depth
    while d > 0:
        o += [f'<path d="{path(r, d)}" fill="{side}" stroke="{side}" stroke-width="2.6" stroke-linejoin="round"/>' for r in rs]
        d -= 2.5
    o += [f'<path d="{path(r)}" fill="{top}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>' for r in rs]
    return o


def flows():
    """The two flows, each joining Hong Kong and the nine cities (Pete, 25 Oct: Northbound didn't start on Hong Kong,
    and Southbound ended in Shenzhen, so it read as pointing back into the mainland). Northbound, dashed wine (kept out
    for the Wongs today): from a ring on Hong Kong's New Territories, west over the estuary, to an arrowhead in the
    Guangzhou-Foshan core. Southbound, solid crimson (the market we want to serve): from a ring in Dongguan and Huizhou,
    round the east, to an arrowhead on Hong Kong. A white casing under each line and marker keeps them readable where
    they cross Hong Kong's crimson. Returns the SVG pieces and the middle of each flow (where the headings' leaders land)."""
    nb0, nbc, nb1 = proj(114.03, 22.41), proj(113.58, 22.50), proj(113.30, 23.08)
    sb0, sbc, sb1 = proj(114.25, 23.12), proj(114.62, 22.60), proj(114.19, 22.43)   # bowed east, so the heading's leader lands clear of its start
    o = ['<defs>'
         '<marker id="gbaArW" viewBox="0 0 12 12" refX="8" refY="6" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
         '<path d="M1,1 L11,6 L1,11 Z" fill="#971320" stroke="#FFFFFF" stroke-width="1.2" stroke-linejoin="round"/></marker>'
         '<marker id="gbaArC" viewBox="0 0 12 12" refX="8" refY="6" markerWidth="4.4" markerHeight="4.4" orient="auto-start-reverse">'
         '<path d="M1,1 L11,6 L1,11 Z" fill="#C80E1E" stroke="#FFFFFF" stroke-width="1.2" stroke-linejoin="round"/></marker>'
         '<marker id="gbaOrW" viewBox="0 0 12 12" refX="6" refY="6" markerWidth="3.4" markerHeight="3.4">'
         '<circle cx="6" cy="6" r="4.4" fill="#FFFFFF" stroke="#971320" stroke-width="2.4"/></marker>'
         '<marker id="gbaOrC" viewBox="0 0 12 12" refX="6" refY="6" markerWidth="2.8" markerHeight="2.8">'
         '<circle cx="6" cy="6" r="4.4" fill="#FFFFFF" stroke="#C80E1E" stroke-width="2.4"/></marker>'
         '</defs>']
    q = lambda a, c, b: f"M{a[0]:.1f},{a[1]:.1f} Q{c[0]:.1f},{c[1]:.1f} {b[0]:.1f},{b[1]:.1f}"
    o.append(f'<path d="{q(nb0, nbc, nb1)}" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/>')
    o.append(f'<path class="nb" d="{q(nb0, nbc, nb1)}" fill="none" stroke="#971320" stroke-width="3.5" stroke-dasharray="9 6" '
             'stroke-linecap="round" marker-start="url(#gbaOrW)" marker-end="url(#gbaArW)"/>')
    o.append(f'<path d="{q(sb0, sbc, sb1)}" fill="none" stroke="#FFFFFF" stroke-width="8.5" stroke-linecap="round"/>')
    o.append(f'<path class="sb" d="{q(sb0, sbc, sb1)}" fill="none" stroke="#C80E1E" stroke-width="4.5" stroke-linecap="round" '
             'marker-start="url(#gbaOrC)" marker-end="url(#gbaArC)"/>')
    mid = lambda a, c, b: (a[0] / 4 + c[0] / 2 + b[0] / 4, a[1] / 4 + c[1] / 2 + b[1] / 4)
    return o, mid(nb0, nbc, nb1), mid(sb0, sbc, sb1)


def redraw_flows(svg_path):
    """Rewrite only the flows in an existing map (the boundary file isn't needed): everything from the flows' <defs>
    to the end is replaced. Prints where the two leaders should land, as shares of the drawing."""
    s = open(svg_path, encoding="utf-8").read()
    cut = s.index('<defs><marker id="gbaArW"')
    o, nb_mid, sb_mid = flows()
    open(svg_path, "w", encoding="utf-8", newline="\n").write(s[:cut] + "\n".join(o) + "\n</svg>\n")
    vb = (0, -6, W, H + 40)
    print(json.dumps({k: (f"{(v[0] - vb[0]) / vb[2] * 100:.1f}%", f"{(v[1] - vb[1]) / vb[3] * 100:.1f}%")
                      for k, v in {"nb_mid": nb_mid, "sb_mid": sb_mid}.items()}))


def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    ctx, sar, gba = [], {}, {}
    for f in data["features"]:
        name = f["properties"].get("shapeName")
        rs = [clip([tuple(p) for p in r], BOX) for r in rings(f["geometry"])]
        rs = [r for r in rs if len(r) >= 3]
        if not rs:
            continue
        if name in SAR:
            sar[SAR[name]] = rs
        elif name in GBA:
            gba[name] = rs
        else:
            ctx += rs
    assert sorted(gba) == sorted(GBA), sorted(set(GBA) - set(gba))
    assert set(sar) == {"hk", "mo"}

    cx, cy = W / 2, H / 2 + 10
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -6 {W} {H + 40}">',
         '<defs><linearGradient id="gbaRose" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0DADE"/>'
         '<stop offset="1" stop-color="#DDB7BE"/></linearGradient><linearGradient id="gbaWine" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#D40F1F"/><stop offset="1" stop-color="#971320"/></linearGradient></defs>',
         '<defs><radialGradient id="gbaFade" cx="50%" cy="52%" r="62%"><stop offset=".55" stop-color="#fff"/>'
         '<stop offset="1" stop-color="#000"/></radialGradient>'
         f'<mask id="gbaMask"><rect x="-20" y="-20" width="{W + 40}" height="{H + 80}" fill="url(#gbaFade)"/></mask></defs>',
         '<g mask="url(#gbaMask)">']                # (no drop shadow under the map: Pete, 24 Oct, it read as a stray oval)
    o += slab(ctx, 3, "#E9DCDF", "#F6EFF0", "#E9DCDF", ".6")          # the land around, pale and fading out
    o.append("</g>")
    o += slab([r for rs in gba.values() for r in rs], 12, "#B98891", "url(#gbaRose)", "#FFFFFF", ".9")   # the nine cities
    o += slab(sar["hk"] + sar["mo"], 15, "#5F0A14", "url(#gbaWine)", "#FFFFFF", ".7")                   # Hong Kong, Macao
    flow_svg, nb_mid, sb_mid = flows()
    o += flow_svg
    o.append("</svg>")

    def centre(rs):
        xs = [proj(*p)[0] for r in rs for p in r]
        ys = [proj(*p)[1] for r in rs for p in r]
        return (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    anchors = {"hk": centre(sar["hk"]), "mo": centre(sar["mo"]), "gz": proj(113.26, 23.13), "sz": proj(114.06, 22.54),
               "gba": centre([r for rs in gba.values() for r in rs]), "nb_mid": nb_mid, "sb_mid": sb_mid, "w": W, "h": H + 40}
    open(sys.argv[2], "w", encoding="utf-8", newline="\n").write("\n".join(o) + "\n")
    vb = (0, -6, W, H + 40)
    print(json.dumps({k: (f"{(v[0] - vb[0]) / vb[2] * 100:.1f}%", f"{(v[1] - vb[1]) / vb[3] * 100:.1f}%")
                      for k, v in anchors.items() if isinstance(v, tuple)}))


if __name__ == "__main__":
    if sys.argv[1] == "--flows":     # gba_map.py --flows round2/img/gba_map.svg
        redraw_flows(sys.argv[2])
    else:
        main()
