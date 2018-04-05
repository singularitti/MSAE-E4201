#!/usr/bin/env python3
"""
Problem 2.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")
plt.style.use('classic')

R = 8.314
H_s = 637.1e3
H_v = 611e3
A_s = 1.9502e7
A_v = 6.1766e6
T_low = 500
T_high = 5000
T = np.linspace(T_low, T_high, num=500)
T_mp = 2720
T_t = T_mp
T_b = 4700
p_t = 1.1396e-5


def p_s(temperature):
    return A_s * np.exp(-H_s / R / temperature)


def p_v(temperature):
    return A_v * np.exp(-H_v / R / temperature)


fig = plt.figure()
ax = plt.subplot(111)
ax.plot(1 / T_mp, 1, 'ro', label="melting point")
ax.plot(1 / T_b, 1, 'bo', label="boiling point")
ax.plot(1 / T_mp, p_t, 'ko', label="triple point")
ax.plot([1 / T_mp, 1 / T_mp], [1, p_t])
ax.semilogy(1 / T, p_s(T), label="sublimation curve")
ax.semilogy(1 / T, p_v(T), label="vaporization curve")
ax.text(0.4, 0.3, "G", transform=ax.transAxes)
ax.text((1 / T_b / (1 / T_low) + 1 / T_mp / (1 / T_low)) / 5,
        0.96, "L", transform=ax.transAxes)
ax.text(0.4, 0.9, "S", transform=ax.transAxes)
ax.set_xlim((1 / T_high, 1 / T_low))
ax.set_ylim((p_v(T[0]), 1))
ax.set_xlabel("$\\frac{1}{T}$", fontsize=16)
ax.set_ylabel("$\\log (p)$", fontsize=16)
ax.set_title("Phase diagram of Iridium", fontsize=18)
ax.legend(loc="best", numpoints=1)
# plt.show()
fig.savefig(my_path + "/images/pro_2.png", dpi=400)
