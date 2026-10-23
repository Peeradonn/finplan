"""The deck's one decorative idea (Pete, 23 Oct): "Built to Last" drawn as a house from the written case's pillars.

  the roof        what passes on (slide 12)
  the rooms       a place for every voice: Call 4 (left), Call 5 (right)
  the walls       income that lasts: Call 2 (left), Call 3 (right)
  the foundation  protected first: Call 1

house(state, size, labels) returns inline SVG. state maps a part ("1".."5", "roof") to "on" (the accent: this slide's
part), "done" (wine: built on an earlier slide) or "todo" (dashed rose: still to come); parts not named are "todo".
The slides carry the generated markup; rerun this file's main to print it after a change.
"""

PARTS = {  # viewBox 0 0 440 400
    "roof": ("poly", "30,150 220,18 410,150"),
    "4": ("rect", (46, 156, 171, 86)), "5": ("rect", (223, 156, 171, 86)),
    "2": ("rect", (46, 248, 171, 86)), "3": ("rect", (223, 248, 171, 86)),
    "1": ("rect", (24, 340, 392, 44)),
}
NAMES = {"1": ("1", "Insure the income"), "2": ("2", "Home and business"), "3": ("3", "Fix the cost"),
         "4": ("4", "A plan each"), "5": ("5", "Values and crypto"), "roof": ("", "What passes on")}
FILL = {"on": ("#A81E2D", "none", "#fff"), "done": ("#7D1D2A", "none", "#fff"), "todo": ("#fff", "#B99A9C", "#A69E9C"),
        "all": ("#7D1D2A", "none", "#fff")}
# the small title houses, in slide 4's line style (23 Oct): this call solid crimson, built parts rose, the rest dashed
LINE = {"on": ("#A81E2D", "#A81E2D", "solid"), "done": ("#E8DEDC", "#A81E2D", "solid"), "todo": ("#FFFFFF", "#B99A9C", "dash")}


def house(state=None, w=72, labels=False, cls="house", steps=None):
    """steps maps a part to its build step: the part and its labels appear in that step (data-b)."""
    state, steps = state or {}, steps or {}
    out = [f'<svg class="{cls}" viewBox="0 0 440 400" width="{w}" height="{round(w * 400 / 440)}" aria-hidden="true">']
    for part, (kind, geo) in PARTS.items():
        fill, stroke, ink = FILL[state.get(part, "todo")]
        out.append(f'<g data-b="{steps[part]}">' if part in steps else "<g>")
        dash = ' stroke-dasharray="10 8"' if stroke != "none" else ""
        sw = 6 if stroke != "none" else 0
        if kind == "poly":
            out.append(f'<polygon points="{geo}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
            cx, cy = 220, 112
        else:
            x, y, ww, hh = geo
            out.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
            cx, cy = x + ww / 2, y + hh / 2
        if labels:
            num, name = NAMES[part]
            if part == "1":   # the foundation is shallow: number and name on one line
                out.append(f'<text x="{cx}" y="{cy + 7}" text-anchor="middle" font-family="Inter, Arial, sans-serif" '
                           f'font-weight="600" font-size="17" fill="{ink}"><tspan font-family="EBG, Georgia, serif" '
                           f'font-size="24">{num}</tspan>   {name}</text>')
            elif num:
                out.append(f'<text x="{cx}" y="{cy - 6}" text-anchor="middle" font-family="EBG, Georgia, serif" '
                           f'font-weight="600" font-size="30" fill="{ink}">{num}</text>')
                out.append(f'<text x="{cx}" y="{cy + 24}" text-anchor="middle" font-family="Inter, Arial, sans-serif" '
                           f'font-weight="600" font-size="17" fill="{ink}">{name}</text>')
            else:
                out.append(f'<text x="{cx}" y="{cy + 12}" text-anchor="middle" font-family="Inter, Arial, sans-serif" '
                           f'font-weight="600" font-size="17" fill="{ink}">{name}</text>')
        out.append("</g>")
    out.append("</svg>")
    return "".join(out)


def progress(call, w=76):
    """The small house beside a call slide's title: earlier calls built (rose), this one lit (crimson), the rest to come
    (dashed), drawn in slide 4's line style."""
    st = {str(k): "done" for k in range(1, call)}
    st[str(call)] = "on"
    o = [f'<svg class="house mini" viewBox="0 0 440 400" width="{w}" height="{round(w * 400 / 440)}" aria-hidden="true">']
    for part, (kind, geo) in PARTS.items():
        fill, stroke, style = LINE[st.get(part, "todo")]
        extra = ' stroke-dasharray="14 10"' if style == "dash" else ""
        attrs = f'fill="{fill}" stroke="{stroke}" stroke-width="10" stroke-linejoin="round"{extra}'
        if kind == "poly":
            o.append(f'<polygon points="{geo}" {attrs}/>')
        else:
            x, y, ww, hh = geo
            o.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" {attrs}/>')
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    for c in range(1, 6):
        print(c, progress(c)[:80], "...")


def elevation(w=360):
    """Slide 4: the house drawn as an architect's elevation (Pete chose it, 23 Oct): fine crimson lines, light rose fills,
    the foundation hatched like concrete, one ground line, each part numbered. Each part is a group with its build step
    (data-b: Call 1 = step 2 ... Call 5 = step 6, the roof = 7) and class "hq", so the frame where it is named can fill it
    crimson (CSS), and the final slide shows it whole."""
    steps = {"1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "roof": 7}
    o = [f'<svg class="house elev" viewBox="-60 0 560 410" width="{w}" height="{round(w * 410 / 560)}" aria-hidden="true">',
         '<defs><pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<rect width="12" height="12" fill="#F5F1F0"/><line x1="0" y1="0" x2="0" y2="12" stroke="#B99A9C" stroke-width="3"/>'
         '</pattern></defs>',
         '<line x1="-10" y1="386" x2="450" y2="386" stroke="#5A5250" stroke-width="2.5"/>']
    for part, (kind, geo) in PARTS.items():
        fill = "url(#hatch)" if part == "1" else ("#F5F1F0" if part == "roof" else "#FBF4F5")
        o.append(f'<g class="hq" data-b="{steps[part]}">')
        if kind == "poly":
            o.append(f'<polygon points="{geo}" fill="{fill}" stroke="#A81E2D" stroke-width="3" stroke-linejoin="round"/>')
            cx, cy = 220, 108
        else:
            x, y, ww, hh = geo
            o.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" fill="{fill}" stroke="#A81E2D" stroke-width="3"/>')
            cx, cy = x + ww / 2, y + hh / 2
        num = "" if part == "roof" else part
        if num:
            o.append(f'<text x="{cx}" y="{cy + 13}" text-anchor="middle" font-family="EBG, Georgia, serif" font-weight="600" '
                     f'font-size="{30 if part == "1" else 40}" fill="#A81E2D">{num}</text>')
        o.append("</g>")
    o.append("</svg>")
    return "".join(o)
