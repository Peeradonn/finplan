"""Exploratory runs for the Final thesis (4 Nov 2026). Not deck numbers: nothing here goes on a slide
until it is added to export_numbers() and logged (Final_Plan.md §2).
Run:  cd model && ../.venv/Scripts/python.exe ../Final/explore_runs.py ."""
import sys
sys.path.insert(0, sys.argv[1])
import run_model as m

full = m.full_plan()
defl = (1 + m.CPI) ** (m.C89 - m.BY)


def run(label, **kw):
    s, _, med = m.sim(*m.MIX2, m.C89, **{**full, **kw})
    print(f"  {label:<58}{s:>7.1%}{med/defl/1e6:>10.2f}M")


print(f"base year {m.BY}, Carmen 89 in {m.C89}; business sale counted {m.BIZ/1e6:.1f}M in {m.BIZ_Y}")
print(f"  {'':<58}{'to 89':>7}{'median pot, today':>18}")
run("Full plan (Round One)")

print("\nA. Carmen's business: sale proceeds")
for v in (0, 1.5e6, 2.0e6, 3.0e6, 4.0e6, 5.0e6):
    run(f"sale proceeds {v/1e6:.1f}M", biz=v)

print("\nB. Price of values: lower expected equity return (fees, tracking)")
for d in (0.0005, 0.001, 0.002, 0.005):
    run(f"equity return -{d*1e4:.0f}bp on all equity", r_eq=m.R_EQ - d)

print("\nC. Funded philanthropy: endowment paid in 2027")
for v in (300_000, 600_000, 750_000):
    run(f"endowment {v/1e3:.0f}K in 2027", inflows={2027: -v})

print("\nD. Property: downsizing instead of reverse mortgage, with a value haircut on the old flat")
base_rel = m.downsize_release(m.DS_Y)
print(f"  downsizing release in {m.DS_Y}: {base_rel/1e6:.2f}M nominal; home value then {m.home_value(m.DS_Y)/1e6:.2f}M")
kw = dict(full); kw.pop("rmp", None)
for cut in (0.0, 0.10, 0.20):
    rel = base_rel - cut * m.home_value(m.DS_Y)
    s, _, med = m.sim(*m.MIX2, m.C89, **{**kw, "rmp": 0, "inflows": {m.DS_Y: rel}})
    print(f"  {'downsize ' + str(m.DS_Y) + f', flat worth {cut:.0%} less':<58}{s:>7.1%}{med/defl/1e6:>10.2f}M")
