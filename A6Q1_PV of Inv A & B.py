import numpy as np

r = 0.0433
years = np.arange(1, 6)

# Cash flows
A = np.array([225, 215, 250, 225, 205])
B = np.array([220, 225, 250, 250, 210])

# Present value using continuous compounding
pv_A = np.sum(A * np.exp(-r * years))
pv_B = np.sum(B * np.exp(-r * years))

print(f"PV of Investment A: {pv_A:.2f}")
print(f"PV of Investment B: {pv_B:.2f}")
print("Preferable:", "A" if pv_A > pv_B else "B")
