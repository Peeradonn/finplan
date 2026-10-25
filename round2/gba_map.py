"""Slide 13's map (Pete, 24 Oct: the Connect slide was bland; a 3D map of the Greater Bay Area). Real boundaries,
drawn as raised slabs on a tilted plane, in the deck's palette: the nine mainland cities in rose, Hong Kong and Macao in
wine and raised higher (the side the Wongs and we stand on), the land around them pale.

Data: geoBoundaries, gbHumanitarian CHN ADM2 (prefecture-level, with the Hong Kong and Macao SARs), simplified,
release 9469f09, CC BY 3.0 IGO (source: OCHA / HDX); the credit is in slide 13's footer.
Run: .venv/Scripts/python.exe -I round2/gba_map.py geoBoundaries-CHN-ADM2_simplified.geojson round2/img/gba_map.svg
It writes the map as a standalone SVG (its own gradients and arrowheads) and prints the anchor points, as shares of the
drawing, for the labels slide 13 lays over it."""
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
         '<stop offset="0" stop-color="#B3202F"/><stop offset="1" stop-color="#7D1D2A"/></linearGradient></defs>',
         '<defs><radialGradient id="gbaFade" cx="50%" cy="52%" r="62%"><stop offset=".55" stop-color="#fff"/>'
         '<stop offset="1" stop-color="#000"/></radialGradient>'
         f'<mask id="gbaMask"><rect x="-20" y="-20" width="{W + 40}" height="{H + 80}" fill="url(#gbaFade)"/></mask></defs>',
         '<g mask="url(#gbaMask)">']                # (no drop shadow under the map: Pete, 24 Oct, it read as a stray oval)
    o += slab(ctx, 3, "#E9DCDF", "#F6EFF0", "#E9DCDF", ".6")          # the land around, pale and fading out
    o.append("</g>")
    o += slab([r for rs in gba.values() for r in rs], 12, "#B98891", "url(#gbaRose)", "#FFFFFF", ".9")   # the nine cities
    o += slab(sar["hk"] + sar["mo"], 15, "#4A1019", "url(#gbaWine)", "#FFFFFF", ".7")                   # Hong Kong, Macao
    # the two flows over the water: Northbound (west, dashed: kept out today), Southbound (east, solid: the market we serve)
    hk = proj(114.12, 22.42)
    nb0, nb1 = (hk[0] - 18, hk[1] - 10), proj(113.30, 23.05)
    sb0, sb1 = proj(114.55, 23.02), (hk[0] + 16, hk[1] - 14)
    o.append('<defs><marker id="gbaArW" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
             '<path d="M0,0 L10,5 L0,10 Z" fill="#7D1D2A"/></marker>'
             '<marker id="gbaArC" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
             '<path d="M0,0 L10,5 L0,10 Z" fill="#A81E2D"/></marker></defs>')
    nbc, nbe = (nb0[0] - 120, nb0[1] + 20), (nb1[0], nb1[1] + 6)
    sbc = (sb0[0] + 70, sb0[1] + 90)
    o.append(f'<path class="nb" d="M{nb0[0]:.1f},{nb0[1]:.1f} Q{nbc[0]:.1f},{nbc[1]:.1f} {nbe[0]:.1f},{nbe[1]:.1f}" '
             'fill="none" stroke="#7D1D2A" stroke-width="3" stroke-dasharray="8 6" stroke-linecap="round" marker-end="url(#gbaArW)"/>')
    o.append(f'<path class="sb" d="M{sb0[0]:.1f},{sb0[1]:.1f} Q{sbc[0]:.1f},{sbc[1]:.1f} {sb1[0]:.1f},{sb1[1]:.1f}" '
             'fill="none" stroke="#A81E2D" stroke-width="4" stroke-linecap="round" marker-end="url(#gbaArC)"/>')
    # where the side headings' leaders land: the middle of each flow (a quadratic's point at t = 1/2)
    mid = lambda a, c, b: (a[0] / 4 + c[0] / 2 + b[0] / 4, a[1] / 4 + c[1] / 2 + b[1] / 4)
    nb_mid, sb_mid = mid(nb0, nbc, nbe), mid(sb0, sbc, sb1)
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
    main()
