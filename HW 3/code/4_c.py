#!/usr/bin/env python3
"""
Problem 4(a).
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import os

plt.style.use('classic')

my_path = os.path.abspath(__file__ + "/../../")

if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")

V = np.linspace(0.001, 0.002, num=500, endpoint=True)


def process_i(volume):
    return 202.65 / volume


def process_iii(volume):
    return 151.9875 / volume


plt.figure()
plt.plot(V, map(process_i, V), label="process I")
plt.plot([0.002, 0.002], [process_i(0.002), process_iii(0.002)], label="process II")
plt.plot(V, map(process_iii, V), label="process III")
plt.plot([0.001, 0.001], [process_iii(0.001), process_i(0.001)], label="process IV")
plt.text(0.001, process_i(0.001), "$P_0$")
plt.text(0.002, process_i(0.002), "$P_1$")
plt.text(0.002, process_iii(0.002), "$P_2$")
plt.text(0.001, process_iii(0.001), "$P_3$")
plt.fill_between(V, map(process_i, V), map(process_iii, V), alpha=0.3)
plt.xlabel("$V$", fontsize=16)
plt.ylabel("$P$", fontsize=16)
plt.xlim((0.0008, 0.0022))
plt.legend(loc="best")
plt.title("The Stirling cycle of a monatomic ideal gas", fontsize=18)
# plt.show()
plt.savefig(my_path + "/images/pro_4_c.png", dpi=400)
