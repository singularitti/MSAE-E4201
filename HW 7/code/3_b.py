#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
import os

plt.style.use("classic")
# my_path = os.path.abspath(__file__ + "/../../")
# if not os.path.exists(my_path + "/images"):
#     os.makedirs(my_path + "/images")

omega_alpha = 5200
omega_l = 9600
s_a = 10.5
tm_a = 1300
s_b = 6.5
tm_b = 775
t = 950
R = 8.314


def delta_g_alpha_mix(xb):
    return omega_alpha * (1 - xb) * xb + \
           R * t * ((1 - xb) * np.log(1 - xb) + xb * np.log(xb))


def delta_g_l_mix(xb):
    return omega_l * (1 - xb) * xb + \
           R * t * ((1 - xb) * np.log(1 - xb) + xb * np.log(xb)) + \
           (1 - xb) * s_a * (tm_a - t) + xb * s_b * (tm_b - t)


def slope_delta_g_alpha_mix(xb):
    return omega_alpha * (1 - 2 * xb) + R * t * (np.log(xb / (1 - xb)))


def slope_delta_g_l_mix(xb):
    return 1330 + omega_l * (1 - 2 * xb) + R * t * (np.log(xb / (1 - xb)))


def common_slope(xb):
    slope_g_alpha = [slope_delta_g_alpha_mix(xbb) for xbb in xb]
    slope_g_l = [slope_delta_g_l_mix(xbb) for xbb in xb]
    for i, gl in enumerate(slope_g_l):
        for j, ga in enumerate(slope_g_alpha):
            if abs(gl - ga) < 0.0001:
                return i, j


xb = np.linspace(0.001, 0.999, num=50000, endpoint=True)  # Num has to be large to be detected
print(common_slope(xb))
i, j = common_slope(xb)
x1, x2 = xb[i], xb[j]
plt.plot(xb, list(map(delta_g_alpha_mix, xb)), label="$\\Delta G_{\\alpha}$ curve")
plt.plot(xb, list(map(delta_g_l_mix, xb)), label="$\\Delta G_L$ curve")
plt.plot([x1, x2], [delta_g_l_mix(x1), delta_g_alpha_mix(x2)])
plt.xlabel("$x_B$", fontsize=16)
plt.ylabel("$\\Delta G$", fontsize=16)
plt.title("$\\{ \\alpha\\colon \\alpha \\}$", fontsize=18)
plt.legend(loc="best")
plt.show()
# plt.savefig(my_path + "/images/pro_3_b.pdf")
