#!/usr/bin/env python3
"""
Problem 4.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

plt.style.use("classic")
my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")

temperature = np.linspace(200, 2000, num=200)


def hs(temp):
    return 20.7 * temp + 0.0062 * temp**2 - 2179.2


def hv(temp):
    return 29 * temp + 6175.6


def ss(temp):
    return 20.7 * np.log(temp) + 0.0124 * temp - 93.325


def sl(temp):
    return 29 * np.log(temp) - 127


def gs(temp):
    return -20.7 * temp * np.log(temp) + 114 * temp - 0.0062 * temp**2 - 2179.2


def gl(temp):
    return -29 * temp * np.log(temp) + 156 * temp + 6175.6


def g(temp):
    return -8.3 * temp * np.log(temp) + 42.02 * temp + 0.0062 * temp**2 + 8354.7


plt.figure()
plt.subplot(221)
plt.plot(temperature, list(map(hs, temperature)), label="$H^{(s)}$")
plt.plot(temperature, list(map(hv, temperature)), label="$H^{(v)}$")
plt.xlabel("$T$", fontsize=16)
plt.ylabel("$H$", fontsize=16)
plt.legend(loc="best")
plt.xticks(rotation=70)
plt.ticklabel_format(style='scientific', scilimits=(0, 3))

plt.subplot(222)
ax = plt.plot(temperature, list(map(ss, temperature)), label="$S^{(s)}$")
plt.plot(temperature, list(map(sl, temperature)), label="$S^{(l)}$")
plt.xlabel("$T$", fontsize=16)
plt.ylabel("$S$", fontsize=16)
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_ticks_position('both')
# plt.gca().yaxis.set_label_position("right")
plt.legend(loc="best")
plt.xticks(rotation=70)
plt.ticklabel_format(style='scientific', scilimits=(0, 3))

ax = plt.subplot(223)
plt.plot(temperature, list(map(gs, temperature)), label="$G^{(s)}$")
plt.plot(temperature, list(map(gl, temperature)), label="$G^{(l)}$")
plt.xlabel("$T$", fontsize=16)
plt.ylabel("$G$", fontsize=16)
plt.legend(loc="best")
plt.xticks(rotation=70)
plt.ticklabel_format(style='scientific', scilimits=(0, 3))

ax = plt.subplot(224)
plt.plot(temperature, list(map(g, temperature)))
plt.xlabel("$T$", fontsize=16)
plt.ylabel("$\\Delta G$", fontsize=16)
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_ticks_position('both')
# plt.gca().yaxis.set_label_position("right")
plt.xticks(rotation=70)
plt.ticklabel_format(style='scientific', scilimits=(0, 3))

plt.tight_layout()   # Use this rather than subplots_adjust
# plt.show()
plt.savefig(my_path + "/images/pro_4.png", dpi=400)
