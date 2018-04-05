#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import os

my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")

energy = np.linspace(-1, 1, num=500)
mu = 0.1
beta = 40


def zero_occupancy(e):
    return 1 / (np.exp(beta * e) + 1)


def one_occupancy(e):
    return 1 / (np.exp(beta * (e - mu)) + 1)


def two_occupancy(e):
    return 1 / (np.exp(beta * (e - 2 * mu)) + 1)


def three_occupancy(e):
    return 1 / (np.exp(beta * (e - 3 * mu)) + 1)


fig, ax1 = plt.subplots()
ax1.plot(energy, list(map(zero_occupancy, energy)), 'r-', label="$N = 0$")
ax1.plot(energy, list(map(one_occupancy, energy)), 'g-', label="$N = 1$")
ax1.plot(energy, list(map(two_occupancy, energy)), 'b-', label="$N = 2$")
ax1.plot(energy, list(map(three_occupancy, energy)), 'c-', label="$N = 3$")
ax1.plot([mu, mu], [0, 1], 'y--', label="$\\mu$")
ax1.plot([mu + 0.001, mu + 0.001], [0, 1], 'r--', label="$\\mu+0.001$")
ax1.plot([mu + 0.01, mu + 0.01], [0, 1], 'g--', label="$\\mu+0.01$")
ax1.plot([mu + 0.1, mu + 0.1], [0, 1], 'k--', label="$\\mu+0.1$")
ax1.set_xlabel("$\\epsilon$ (eV)", fontsize=16)
ax1.set_ylabel("$\\rho$", fontsize=16)
ax1.legend(loc="best")

ax2 = plt.axes([0.15, 0.17, 0.35, 0.35])
ax2.plot(energy, list(map(zero_occupancy, energy)), 'r-', label="$N = 0$")
ax2.plot(energy, list(map(one_occupancy, energy)), 'g-', label="$N = 1$")
ax2.plot(energy, list(map(two_occupancy, energy)), 'b-', label="$N = 2$")
ax2.plot(energy, list(map(three_occupancy, energy)), 'c-', label="$N = 3$")
ax2.plot([mu, mu], [0, 1], 'y--', label="$\\mu$")
ax2.plot([mu + 0.001, mu + 0.001], [0, 1], 'r--')
ax2.plot([mu + 0.01, mu + 0.01], [0, 1], 'g--')
ax2.plot([mu + 0.1, mu + 0.1], [0, 1], 'k--')
ax2.set_xlim((mu - 0.001, mu + 0.011))
# this locator puts ticks at regular intervals
loc = plticker.MultipleLocator(base=0.01)
ax2.xaxis.set_major_locator(loc)
ax2.set_yticks([])

plt.suptitle("Plot of different occupancies, with $\\mu = 0.1$ eV", fontsize=16)
# plt.show()
fig.savefig(my_path + "/images/pro_5.pdf")
