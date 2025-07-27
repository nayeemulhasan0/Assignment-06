import mibian

S = 32      
r = 5       
sigma = 30  
T6m = int(0.5 * 365)   #lol, days e input deya lage not year 
T1y = 1 * 365    

# prices calc using BLS model
def call_price(S, K, r, T, vol):
    return mibian.BS([S, K, r, T], volatility=vol).callPrice

def put_price(S, K, r, T, vol):
    return mibian.BS([S, K, r, T], volatility=vol).putPrice

# Option prices
c25_6 = call_price(S, 25, r, T6m, sigma)
c30_6 = call_price(S, 30, r, T6m, sigma)
p25_6 = put_price(S, 25, r, T6m, sigma)
p30_6 = put_price(S, 30, r, T6m, sigma)

c25_12 = call_price(S, 25, r, T1y, sigma)
c30_12 = call_price(S, 30, r, T1y, sigma)
c35_12 = call_price(S, 35, r, T1y, sigma)

p25_12 = put_price(S, 25, r, T1y, sigma)
p30_12 = put_price(S, 30, r, T1y, sigma)
p35_12 = put_price(S, 35, r, T1y, sigma)


# print(c25_12, c30_12, c35_12)

# Strategies
print(f"Bull Spread (Calls): {c25_6 - c30_6}")
print(f"Bear Spread (Puts): {p30_6 - p25_6}")
print(f"Butterfly Spread (Calls): {c25_12 - 2*c30_12 + c35_12}")
print(f"Butterfly Spread (Puts): {p25_12 - 2*p30_12 + p35_12}")
print(f"Straddle (K=30): {call_price(S, 30, r, T6m, sigma) + put_price(S, 30, r, T6m, sigma)}")
print(f"Strangle (K=25,35): {put_price(S, 25, r, T6m, sigma) + call_price(S, 35, r, T6m, sigma)}")
