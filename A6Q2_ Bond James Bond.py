import numpy as np

FV, c, r1, r2, n = 100, 0.08, 0.11, 0.108, 5
t = np.arange(1, n + 1)
cf = np.full(n, c * FV); cf[-1] += FV

P1 = np.sum(cf * np.exp(-r1 * t))
D = np.sum(t * cf * np.exp(-r1 * t)) / P1
P1_approx = P1 + D * P1 * 0.002
P2 = np.sum(cf * np.exp(-r2 * t))

print(P1, D, P1_approx, P2)
