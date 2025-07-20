import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 150
premium = 5
S = np.linspace(100, 200, 500)

# Payoffs
long_call_payoff = np.maximum(S - K, 0)
short_call_payoff = -long_call_payoff
long_put_payoff = np.maximum(K - S, 0)
short_put_payoff = -long_put_payoff

# Profits
long_call_profit = long_call_payoff - premium
short_call_profit = short_call_payoff + premium
long_put_profit = long_put_payoff - premium
short_put_profit = short_put_payoff + premium

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
titles = ['Long Call', 'Short Call', 'Long Put', 'Short Put']
profits = [long_call_profit, short_call_profit, long_put_profit, short_put_profit]
payoffs = [long_call_payoff, short_call_payoff, long_put_payoff, short_put_payoff]

for i, ax in enumerate(axs.ravel()):
    profit = profits[i]
    payoff = payoffs[i]

    # Regions
    ax.fill_between(S, profit, where=(payoff == 0), color='red', alpha=0.3, label='Not Executed')
    ax.fill_between(S, profit, where=(profit < 0) & (payoff != 0), color='yellow', alpha=0.3, label='Loss Zone')
    ax.fill_between(S, profit, where=(profit > 0), color='green', alpha=0.3, label='Profit Zone')

    # Plot lines
    ax.plot(S, payoff, '--', label='Payoff', linewidth=1.5)
    ax.plot(S, profit, label='Profit', linewidth=2)

    ax.axhline(0, color='black', linewidth=0.7)
    ax.axvline(K, color='gray', linestyle='--', linewidth=0.8)
    ax.set_title(titles[i])
    ax.set_xlabel('Stock Price at Expiry ($)')
    ax.set_ylabel('Payoff / Profit ($)')
    ax.legend(loc='upper left')

plt.tight_layout()
plt.show()
