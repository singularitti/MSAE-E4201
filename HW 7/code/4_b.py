#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")

hm_ta = 3.6e4
hm_w = 3.5e4
tm_ta = 3290
tm_w = 3695
R = 8.314


def delta_g(hm, tm, t):
    return hm * (1 - t / tm)


def free_energy(hm, tm, t):
    return delta_g(hm, tm, t) / R / t


def liquidus_line(t):
    return (np.exp(free_energy(hm_ta, tm_ta, t)) - 1) / \
           (np.exp(free_energy(hm_ta, tm_ta, t)) - free_energy(hm_w, tm_w, t))


def solidus_line(t):
    return np.exp(free_energy(hm_w, tm_w, t)) * liquidus_line(t)


t = np.linspace(tm_ta, tm_w, 500)
fig, ax = plt.subplots()
plt.plot(list(map(liquidus_line, t)), t, label="liquidus line")
plt.plot(list(map(solidus_line, t)), t, label="solidus line")
plt.gca().invert_xaxis()
plt.ylim((min(t), max(t)))
new_label = np.array(np.linspace(1, 0, 11, endpoint=True))
ax.set_xticklabels(new_label)
plt.xlabel("$x_B$", fontsize=16)
plt.ylabel("$T$", fontsize=16)
plt.title("Parametric plot of Ta and W", fontsize=18)
plt.legend(loc="best")
plt.show()
# plt.savefig(my_path + "/images/pro_4_b.pdf")
