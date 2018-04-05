#!/usr/bin/env python3
"""
Problem 2.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']  # for \text command

temp_list_1 = [200, 250, 540]
temp_list_2 = [250, 200, 540]
temp_list_3 = [200, 540, 250]
niter = 50
ncut = 10

my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")


def calculate_temp_work(temp_1, temp_2):
    eqbm_temp = np.sqrt(temp_1 * temp_2)  # Equilibrium temperature
    work = 5 * (temp_1 + temp_2 - 2 * np.sqrt(temp_1 * temp_2))  # Work in one process
    return eqbm_temp, work


def loop(initial_temp_list, niter):
    tmp = np.zeros(niter)  # Intermediate temperature list
    wrk = np.zeros(niter)  # Intermediate work list
    tmp[0], wrk[0] = calculate_temp_work(initial_temp_list[0], initial_temp_list[2])
    tmp[1], wrk[1] = calculate_temp_work(tmp[0], initial_temp_list[1])
    for i in range(2, niter):
        tmp[i], wrk[i] = calculate_temp_work(tmp[i - 1], tmp[i - 2])
    return tmp, wrk


tmp_1, wrk_1 = loop(temp_list_1, niter)
tmp_2, wrk_2 = loop(temp_list_2, niter)
tmp_3, wrk_3 = loop(temp_list_3, niter)
print(tmp_3, wrk_3)

plt.figure()
plt.subplot(211)
plt.plot(range(1, ncut + 1), tmp_1[0:ncut], label="A, C contact first")
plt.plot(range(1, ncut + 1), tmp_2[0:ncut], label="B, C contact first")
plt.plot(range(1, ncut + 1), tmp_3[0:ncut], label="A, B contact first")
plt.gca().get_xaxis().set_ticks([])  # No bottom ticks
plt.ylabel("temperature $T \\text{(K)}$", fontsize=16)
plt.legend(loc="best")

plt.subplot(212)
plt.plot(range(1, ncut + 1), np.add.accumulate(wrk_1[0:ncut]), label="A, C contact first")
plt.plot(range(1, ncut + 1), np.add.accumulate(wrk_2[0:ncut]), label="B, C contact first")
plt.plot(range(1, ncut + 1), np.add.accumulate(wrk_3[0:ncut]), label="A, B contact first")
plt.ylim((min(np.add.accumulate(wrk_3[0:ncut])),
          max(np.add.accumulate(wrk_3[0:ncut])) * 1.05))
plt.xlabel("iteration steps", fontsize=16)
plt.ylabel("accumulated work $W \\text{(J)}$", fontsize=16)
plt.legend(loc="best")

plt.subplots_adjust(wspace=0, hspace=0)  # Remove spaces between subplots
# plt.show()
plt.savefig(my_path + "/images/pro_2.png", dpi=400)
