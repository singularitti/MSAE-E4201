#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use("classic")
my_path = os.path.abspath(__file__ + "/../../")
if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")

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
           R * t * ((1 - xb) * np.log(1 - xb) + xb * np.log(xb)) \
           - (1 - xb) * s_a * (tm_a - t) - xb * s_b * (tm_b - t)


def delta_g_l_mix(xb):
    return omega_l * (1 - xb) * xb + \
           R * t * ((1 - xb) * np.log(1 - xb) + xb * np.log(xb))


xb = np.linspace(0.001, 0.999, num=500, endpoint=True)
plt.plot(xb, list(map(delta_g_alpha_mix, xb)), label="$\\Delta G_{\\alpha}$ curve")
plt.plot(xb, list(map(delta_g_l_mix, xb)), label="$\\Delta G_L$ curve")
plt.xlabel("$x_B$", fontsize=16)
plt.ylabel("$\\Delta G$", fontsize=16)
plt.title("$\\{ L ; L \\}$", fontsize=18)
plt.legend(loc="best")
# plt.show()
plt.savefig(my_path + "/images/pro_3_d.pdf")
