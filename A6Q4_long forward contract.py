import numpy as np

S0, r, T = 40, 0.10, 1
F0 = S0 * np.exp(r * T)
print(f"F0={F0:.2f}, V0=0")

St, t = 45, 0.5
Vt = St - F0 * np.exp(-r * (T - t))
Ft_new = St * np.exp(r * (T - t))
print(f"Ft={Ft_new:.2f}, Vt={Vt:.2f}")
