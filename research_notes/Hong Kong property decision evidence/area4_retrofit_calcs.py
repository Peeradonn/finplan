"""Area 4 illustrative arithmetic only; independent of the shared retirement model.

Run: python "research_notes/Hong Kong property decision evidence/area4_retrofit_calcs.py"
All cash flows nominal HKD, flat nominal prices, end-year cash flows, 5% nominal
discount rate. No tax benefits, property premium, verified savings or subsidies
are assumed unless an explicitly named illustrative sensitivity includes one.
"""
import json


def annuity_factor(years, rate=0.05):
    return sum((1 + rate) ** -year for year in range(1, years + 1))


def led(hours=3000, tariff=1.58, years=3, subsidy=0, exit_cost=0):
    # 100 hypothetical tubes, measured whole-circuit wattages required in practice.
    kwh = 100 * (42 - 18) / 1000 * hours
    annual = kwh * tariff + 500  # hypothetical avoided maintenance
    npv = -22000 + annual * annuity_factor(years)
    npv += subsidy / 1.05  # assume receipt at end year 1, not at purchase
    npv -= exit_cost / 1.05 ** years
    return {"hours": hours, "tariff": tariff, "years": years,
            "kwh_saved_per_year": kwh, "annual_net_saving": annual,
            "subsidy_year1": subsidy, "exit_cost": exit_cost,
            "company_npv": npv, "Carmen_50pct_economic_share": npv * 0.5,
            "gross_simple_payback_years": 22000 / annual}


out = {"status": "ILLUSTRATIVE, not shared model outputs or presentation figures",
       "led": {
           "base_no_grant": led(),
           "conditional_6000_grant": led(subsidy=6000),
           "short_lease_one_year": led(years=1),
           "low_use_and_tariff": led(hours=1200, tariff=1.2),
           "low_use_with_grant": led(hours=1200, tariff=1.2, subsidy=6000),
           "reinstatement_5000": led(exit_cost=5000),
           "high_use_and_tariff": led(hours=4500, tariff=1.9),
       }}
base_factor = annuity_factor(3)
out["led_break_even_hours_3yr_no_grant"] = (22000 / base_factor - 500) / (100 * 24 / 1000 * 1.58)
out["home_failed_AC"] = {
    "incremental_capex": 2000,  # efficient7000 versus ordinary5000
    "annual_kwh_saving": 500, "tariff_assumption": 1.5,
    "extra_annual_maintenance": 50, "horizon": 8,
    "npv": -2000 + (500 * 1.5 - 50) * annuity_factor(8),
    "break_even_annual_kwh": (2000 / annuity_factor(8) + 50) / 1.5,
}
# Compare replacing a working unit now with waiting3years to buy same efficient
# unit. At year8 early unit age8; waiting unit age5. Use illustrative straight-line
# residual values over10years:1400 versus3500. Equivalent cooling/output assumed.
out["home_early_AC_vs_wait3"] = {
    "cost_efficient_each_time": 7000,
    "old_unit_years_remaining": 3,
    "old_vs_new_kwh_saving": 400, "tariff_assumption": 1.5,
    "matched_horizon": 8, "terminal_residual_difference": -2100,
    "npv": -7000 + 7000 / 1.05**3 + 600 * annuity_factor(3) - 2100 / 1.05**8,
}
out["home_window_film"] = {
    "capex": 3000, "kwh_saved_per_year": 100,
    "tariff_assumption": 1.5, "horizon": 10,
    "npv": -3000 + 150 * annuity_factor(10),
    "break_even_kwh_per_year": 3000 / annuity_factor(10) / 1.5,
}
out["landlord_savings_share_example"] = {
    "capex": 50000, "annual_tenant_net_saving": 7000,
    "savings_share_for_landlord": 0.7, "horizon": 5,
    "landlord_npv": -50000 + 4900 * annuity_factor(5),
    "tenant_npv": 2100 * annuity_factor(5),
    "landlord_needed_annual_recovery": 50000 / annuity_factor(5),
}
# Per1kWp illustrative rooftop model: start2027, only seven FiT years to2033,
#1000kWh year1,0.5% annual degradation, HK$4/kWh scenario, HK$200paO&M,
#zero post2033/residual credit. Roof rights and all quotes are unverified.
for n in (3, 7):
    cashflows = [1000 * .995**(y - 1) * 4 - 200 for y in range(1, n + 1)]
    out[f"solar_{n}year"] = {"capex": 20000,
        "npv": -20000 + sum(cf / 1.05**y for y, cf in enumerate(cashflows, 1)),
        "break_even_max_capex": sum(cf / 1.05**y for y, cf in enumerate(cashflows, 1))}
out["financed_led"] = {
    "loan_principal": 22000, "loan_nominal_annual_rate": 0.08,
    "annual_payments": 3,
    "annual_debt_service": 22000 / annuity_factor(3, .08),
    "saving_to_debt_service_ratio": led()["annual_net_saving"] / (22000 / annuity_factor(3, .08)),
}
print(json.dumps(out, indent=2))
