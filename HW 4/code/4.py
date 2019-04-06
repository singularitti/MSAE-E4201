#!/usr/bin/env python3
"""
Problem 4.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
plt.rcParams['text.usetex'] = True
# for \dfrac command
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

c_1 = [4, -1]
c_2 = [3, -3]
c_V = 1
kappa_T = 2
temperature = np.linspace(1, 1000, num=500)
volume = np.linspace(1, 1000, num=500)

my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")


def F_T_0(temp):
    return c_1[0] * temp - c_V * temp * np.log(temp)


def F_T_1(temp):
    return c_1[1] * temp - c_V * temp * np.log(temp)


def F_V_0(volum):
    return (c_2[0] - 1 / kappa_T) * volum + 1 / kappa_T * volum * np.log(volum)


def F_V_1(volum):
    return (c_2[1] - 1 / kappa_T) * volum + 1 / kappa_T * volum * np.log(volum)


def F_derivative_T_0(temp):
    return - c_V * np.log(temp) + c_1[0]


def F_derivative_T_1(temp):
    return - c_V * np.log(temp) + c_1[1]


def F_derivative_V_0(volum):
    return 1 / kappa_T * np.log(volum) + c_2[0]


def F_derivative_V_1(volum):
    return 1 / kappa_T * np.log(volum) + c_2[1]


plt.figure()
plt.subplot(221)
plt.plot(temperature, list(map(F_T_0, temperature)), label="$C_1 > 0$")
plt.plot(temperature, list(map(F_T_1, temperature)), label="$C_1 < 0$")
plt.xlabel("$T$", fontsize=16)
plt.ylabel("$F$", fontsize=16)
plt.legend(loc="best")

plt.subplot(222)
plt.plot(volume, list(map(F_V_0, volume)), label="$C_2 > 0$")
plt.plot(volume, list(map(F_T_1, volume)), label="$C_2 < 0$")
plt.xlabel("$V$", fontsize=16)
plt.ylabel("$F$", fontsize=16)
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_ticks_position('both')
# plt.gca().yaxis.set_label_position("right")
plt.legend(loc="best")

plt.subplot(223)
plt.plot(volume, list(map(F_derivative_T_0, temperature)), label="$C_1 > 0$")
plt.plot(volume, list(map(F_derivative_T_1, temperature)), label="$C_1 < 0$")
plt.xlabel("$T$", fontsize=16)
plt.ylabel("$\\frac{\\partial F}{\\partial T}$", fontsize=16)
plt.legend(loc="best")

plt.subplot(224)
plt.plot(volume, list(map(F_derivative_V_0, volume)), label="$C_2 > 0$")
plt.plot(volume, list(map(F_derivative_V_1, volume)), label="$C_2 < 0$")
plt.xlabel("$V$", fontsize=16)
plt.ylabel("$\\frac{\\partial F}{\\partial V}$", fontsize=16)
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_ticks_position('both')
# plt.gca().yaxis.set_label_position("right")
plt.legend(loc="best")

plt.subplots_adjust(hspace=0.3)
# plt.show()
plt.savefig(my_path + "/images/pro_4.png", dpi=400)
