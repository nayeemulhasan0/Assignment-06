import numpy as np

#given,
S = 19;K = 20;C = 1;r = 0.03;T = 4 / 12

# Put-Call Parity: C - P = S - K*e^(-rT)
P = C + K * np.exp(-r * T) - S

print(f"European put option price:{P}")
