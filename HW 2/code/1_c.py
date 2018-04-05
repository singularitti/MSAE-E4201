#!/usr/bin/env python
"""
Problem 2(c).
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
plt.rcParams['text.usetex'] = True
# for \text command
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
my_path = os.path.abspath(__file__ + "/../../")
u = np.linspace(0, 80, num=80 / 0.5)


def s(u_a):
    return (3 * 9 * 10**(-6) * u_a)**(1 / 3) + (2 * 4 * 10**(-6) * (80 - u_a))**(1 / 3)


solution = 240 / 19 * (9 - 2 * np.sqrt(6))
plt.plot(u, s(u))
plt.plot([solution, solution], [0.08, 0.18], 'r-')
plt.plot([0, 80], [s(solution), s(solution)], 'r-')
plt.xlabel("$U_A$", fontsize=16)
plt.ylabel("$S_{\\text{total}}$", fontsize=16)
plt.title("$S_{\\text{total}}$ as a function of $U_A$", fontsize=18)
# plt.show()
plt.savefig(my_path + "/images/pro_1_c.png", dpi=400)
