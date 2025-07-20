import numpy as np

payments = np.array([460, 235, 640, 370, 330, 250])
rate_annual = 0.045
comp_per_year = 4
r = rate_annual / comp_per_year

# Present value for each year using quarterly compounding
pv = sum(p / (1 + r) ** (comp_per_year * t) for t, p in enumerate(payments, 1))
print(f"Present Value: ${pv:.2f}")
