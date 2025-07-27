import mibian
import numpy as np

# Given,
S = 30;K = 29
r = 5;vol = 25
T = 4 / 12

# BS Model
bs = mibian.BS([S, K, r, T*365], volatility=vol)  

# European call
call_price = bs.callPrice

# European put 
put_price = bs.putPrice

# For American call on non-dividend stock, price = European call price
american_call_price = call_price

# Verify put-call parity: C - P = S - K * exp(-rT)

parity_holds = abs((call_price - put_price) - (S - K * np.exp(-r * T / 100)) ) < 1e-4

print(f"European call price: {call_price:.4f}")
print(f"American call price: {american_call_price:.4f}")
print(f"European put price: {put_price:.4f}")
print(f"Put-call parity holds: {parity_holds}")
