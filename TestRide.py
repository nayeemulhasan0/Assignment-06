import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

K, premium = 150, 5
S = np.linspace(100, 200, 500)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

types = ['long_call', 'short_call', 'long_put', 'short_put']
titles = ['Long Call', 'Short Call', 'Long Put', 'Short Put']

for ax, t, title in zip(axs.ravel(), types, titles):
    if 'call' in t:
        payoff = np.maximum(S - K, 0)
    else:
        payoff = np.maximum(K - S, 0)

    if 'short' in t:
        payoff = -payoff
        profit = payoff + premium
    else:
        profit = payoff - premium

    for i in range(len(S)-1):
        color = 'red' if payoff[i] == 0 else ('yellow' if profit[i] < 0 else 'green')
        ax.plot(S[i:i+2], profit[i:i+2], color=color, lw=2)

    ax.plot(S, payoff, 'k--', lw=1.5, label='Payoff')
    ax.axhline(0, color='black', lw=0.7)
    ax.axvline(K, color='gray', ls='--', lw=0.8)
    ax.set(title=title, xlabel='Stock Price', ylabel='Payoff / Profit')

    ax.legend(handles=[
        Line2D([0], [0], color='green', lw=2, label='Profit'),
        Line2D([0], [0], color='yellow', lw=2, label='Loss'),
        Line2D([0], [0], color='red', lw=2, label='Not Executed'),
        Line2D([0], [0], color='black', ls='--', lw=1.5, label='Payoff')
    ], loc='upper left')

plt.tight_layout()
plt.show()
