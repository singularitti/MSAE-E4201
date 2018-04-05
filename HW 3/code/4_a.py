#!/usr/bin/env python3
"""
Problem 4(c).
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

plt.plot([0.001, 0.002], [400, 400], label="process I")
plt.plot([0.002, 0.002], [400, 300], label="process II")
plt.plot([0.002, 0.001], [300, 300], label="process III")
plt.plot([0.001, 0.001], [300, 400], label="process IV")
plt.text(0.001, 402, "$P_0$")
plt.text(0.002, 402, "$P_1$")
plt.text(0.002, 295, "$P_2$")
plt.text(0.001, 295, "$P_3$")
plt.fill_between(V, 300, 400, alpha=0.3)
plt.xlabel("$V$", fontsize=16)
plt.ylabel("$T$", fontsize=16)
plt.xlim((0.0008, 0.0022))
plt.ylim((280, 420))
plt.legend(loc="best")
plt.title("The Stirling cycle of a monatomic ideal gas", fontsize=18)
# plt.show()
plt.savefig(my_path + "/images/pro_4_a.png", dpi=400)
