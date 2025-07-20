import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Parameters
K = 150
premium = 5
S = np.linspace(100, 200, 500)

# Payoff and Profit functions
def calc_payoff_profit(option_type):
    if option_type == 'long_call':
        payoff = np.maximum(S - K, 0)
        profit = payoff - premium
    elif option_type == 'short_call':
        payoff = -np.maximum(S - K, 0)
        profit = payoff + premium
    elif option_type == 'long_put':
        payoff = np.maximum(K - S, 0)
        profit = payoff - premium
    elif option_type == 'short_put':
        payoff = -np.maximum(K - S, 0)
        profit = payoff + premium
    return payoff, profit

# Segment plotting
def plot_colored_line(ax, x, y, payoff, title):
    for i in range(len(x)-1):
        if payoff[i] == 0:
            color = 'red'     # Not executed
        elif y[i] < 0:
            color = 'yellow'  # Loss
        else:
            color = 'green'   # Profit
        ax.plot(x[i:i+2], y[i:i+2], color=color, linewidth=2)

    ax.plot(x, payoff, 'k--', linewidth=1.5, label='Payoff')
    ax.axhline(0, color='black', linewidth=0.7)
    ax.axvline(K, color='gray', linestyle='--', linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel('Stock Price at Expiry ($)')
    ax.set_ylabel('Payoff / Profit ($)')

    # Custom legend
    legend_elements = [
        Line2D([0], [0], color='green', lw=2, label='Profit'),
        Line2D([0], [0], color='yellow', lw=2, label='Loss'),
        Line2D([0], [0], color='red', lw=2, label='Not Executed'),
        Line2D([0], [0], color='black', linestyle='--', lw=1.5, label='Payoff')
    ]
    ax.legend(handles=legend_elements, loc='upper left')

# Plot all
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
titles = ['Long Call', 'Short Call', 'Long Put', 'Short Put']
types = ['long_call', 'short_call', 'long_put', 'short_put']

for ax, t, title in zip(axs.ravel(), types, titles):
    payoff, profit = calc_payoff_profit(t)
    plot_colored_line(ax, S, profit, payoff, title)

plt.tight_layout()
plt.show()
