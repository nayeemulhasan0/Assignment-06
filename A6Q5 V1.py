import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 150      # Strike price
premium = 5  # Option premium
S = np.linspace(100, 200, 500)  # Range of stock prices

# Payoff functions
long_call_payoff = np.maximum(S - K, 0)
short_call_payoff = -long_call_payoff
long_put_payoff = np.maximum(K - S, 0)
short_put_payoff = -long_put_payoff

# Profit functions (Payoff - Premium or + Premium for short)
long_call_profit = long_call_payoff - premium
short_call_profit = short_call_payoff + premium
long_put_profit = long_put_payoff - premium
short_put_profit = short_put_payoff + premium

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.ravel()

# Long Call
axs[0].plot(S, long_call_payoff, 'b--', label='Payoff')
axs[0].plot(S, long_call_profit, 'b', label='Profit')
axs[0].set_title('Long Call')
axs[0].legend()

# Short Call
axs[1].plot(S, short_call_payoff, 'r--', label='Payoff')
axs[1].plot(S, short_call_profit, 'r', label='Profit')
axs[1].set_title('Short Call')
axs[1].legend()

# Long Put
axs[2].plot(S, long_put_payoff, 'g--', label='Payoff')
axs[2].plot(S, long_put_profit, 'g', label='Profit')
axs[2].set_title('Long Put')
axs[2].legend()

# Short Put
axs[3].plot(S, short_put_payoff, 'm--', label='Payoff')
axs[3].plot(S, short_put_profit, 'm', label='Profit')
axs[3].set_title('Short Put')
axs[3].legend()

for ax in axs:
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(K, color='gray', linestyle='--', linewidth=0.8)
    ax.set_xlabel('Stock Price at Expiration ($)')
    ax.set_ylabel('Payoff / Profit ($)')

plt.tight_layout()
plt.show()
